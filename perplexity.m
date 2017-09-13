function  p  = perplexity( WP, DP, tokens ,ALPHA , BETA, T, WS, DS )
%WP: a sparse matrix of size W x T with full form, where W is the number of
%words in the vocabulary and T is the number of topics. WP(i,j) contains
%the number of times word i has been assigned to topic j.
%DP: a sparse D x T matrix, where D is the number of documents. DP(d,j)
%contains the number of times a word token in document d has been assigned
%to topic j.
%Tokens is the length of DS which is dipected as follows 
%ALPHA and BETA are hyper-parameters for Dir distribution. 
%Tis the number of topics. 
%WS: a 1 x N vector where WS(k) contains the vocabulary index of the kth
%word token, and N is the number of word tokens. The word indices are not
%zero based, i.e., min( WS )=1 and max( WS ) = W = number of distinct words
%in vocabulary.
%DS: a 1 x N vector where DS(k) contains the document index of the kth word
%token. The document indices are not zero based, i.e., min( DS )=1 and max(
%DS ) = D = number of documents.
temp = 0;
log_pwd = 0;
perp = 0;
doc_number = max(DS);  
for i=1:doc_number
    index = find(DS == i);
    sum1 = sum(DP(i,:))+ T * ALPHA;
    for l=1:length(index)
        j = WS(index(l));
        sum2 = sum(WP(j,:)) + 80 * BETA;
        for k=1:T
            temp = temp + ((DP(i,k) + ALPHA) / sum1) *((WP(j,k) + BETA) / sum2);
        end
        log_pwd = log_pwd + log(temp);
        temp = 0;
    end
    perp = perp + log_pwd;
    log_pwd = 0;
end

p = exp(-perp/tokens);


