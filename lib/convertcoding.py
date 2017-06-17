# -*- coding:UTF-8 -*-

import chardet
import codecs
import os
import os.path
import string
import sys
import csv
from hanziconv import HanziConv
reload(sys)
sys.setdefaultencoding( "utf-8" )


countsig = 0
count1 =0
count = 0
listnew = '/home/hongliang/Downloads/workspace/mirrorfunctions'
for root, dirs, files in os.walk( listnew ):
    for fn in files:
        a = os.path.join(root,fn)

	raw = open(a)
	content = raw.read()
	raw.close
	if chardet.detect(content)['encoding'] == 'utf-8':
		count1 += 1
		print a,'success'
	elif chardet.detect(content)['encoding'] == 'UTF-8-SIG':
		print a,'sig success'
		countsig +=1
	else:
		print a
		content = content.decode('gbk').encode('utf-8')

	content = HanziConv.toSimplified(content)
	
	raw = open(a,'w')
	raw.write(content)
	raw.close


        a = a.encode('utf-8')
        b = HanziConv.toSimplified(a)


	os.renames(a,b)
	count += 1
print count
print count1,countsig


