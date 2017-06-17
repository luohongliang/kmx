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

raw = open('/home/hongliang/Downloads/workspace/Nichol_stop.txt')
content = raw.read()
raw.close
content = HanziConv.toSimplified(content)
raw = open('/home/hongliang/Downloads/workspace/Nichol_stop.txt','w')
raw.write(content)
raw.close
