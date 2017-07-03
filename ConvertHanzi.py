# -*- coding:UTF-8 -*-


import os
import os.path
import string
import sys
import csv
from hanziconv import HanziConv
reload(sys)
sys.setdefaultencoding( "utf-8" )



count = 0
count1 = 0

listnew = '/home/hongliang/Desktop/inpho/corpus/kmx'


for root, dirs, files in os.walk( listnew ):
    count1 += 1
    for fn in files:
        a = os.path.join(root,fn)
	#print a
        count += 1
        raw = open(a)
        content = raw.read()
	    #raw.close
        content = content.encode('utf-8')
        contents = HanziConv.toSimplified(content)

        b = HanziConv.toSimplified(a.encode('utf-8'))

    	raw = open(a,'w')
    	raw.write(content)
    	raw.close
    	os.renames(a,b)
        if a != b:
            print a,b
        if content != contents:
            print content
            print contents
        print 'files id',count
print 'folders number:',count1



