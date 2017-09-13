def perplexity(WP, DP, tokens ,ALPHA , BETA, T, WS, DS ):
    # WP: a sparse matrix of size W x T with full form,
    # where W is the number of words in the vocabulary
    # and T is the number of topics.
    # WP(i,j) contains the number of times word i has been assigned to topic j.


    temp = 0
    log_pwd = 0
    perp = 0
    doc_number = max(DS)
    for i in range(0,doc_number):
        index =