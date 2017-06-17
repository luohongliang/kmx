# -*- coding:UTF-8 -*-


import os
import os.path
import string
import sys
import csv
import json
from collections import defaultdict
reload(sys)
sys.setdefaultencoding( "utf-8" )


csvfile = open('test.csv','r')
jsonfile = open('test.json','w')
filednames = ('book','dynasty','year')
reader = csv.DictReader(csvfile,filednames)
out = json.dumps([row for row in reader])

ceng1 = []
ceng2 = []
listnew = '/home/hongliang/Downloads/allcorpus/H3/HandianCorpus'
def list_files(startPath):
  fileSave = open('list.txt','w')
  for root, dirs, files in os.walk(startPath):
    level = root.replace(startPath, '').count(os.sep)
    indent = ' ' * 1 * level
    #fileSave.write('{}{}/'.format(indent, os.path.basename(root)) + '\n')
    fileSave.write('{}{}\\'.format(indent, os.path.abspath(root)) + '\n')
    subIndent = ' ' * 1 * (level + 1)

    # 得出最后的那一个文件或者文件夹名字
    #print os.path.basename(root),level
    #startpath的最后一个的文件夹名字，也就是mirrorfunctions文件夹
    #print os.path.basename(startPath),level
    # 全路径
    #print os.path.abspath(root),level
    #print os.path.abspath(root).split('/')
    #print os.path.dirname(startPath)
    #print os.path.dirname(root)
    #print 'compare',root,level
    for f in files:
      #fileSave.write('{}{}'.format(subIndent, f) + '\n')
        fileSave.write('{}{}{}'.format(subIndent, os.path.abspath(root), f) + '\n')
        #print os.path.abspath(root),level
        ceng1.append(os.path.abspath(root)+f)
  fileSave.close()

list_files(listnew)

for i in ceng1:
    ceng2.append(i.split('/')[5:])
print ceng2
#

def tree():
    return defaultdict(tree)




def add(t,keys):
    for key in keys:
        t = t[key]
taxonomy = tree()


print ceng1


for i in ceng2:
  add(taxonomy,i)


x =  json.dumps(taxonomy)



fileSave = open('taxonomy.json','w')
fileSave.write(x)
fileSave.close()

# class TreeNode(dict):
#     def __init__(self, name, children=None):
#
#         self.__dict__ = self
#         self.name = name
#         self.children = [] if not children else children
#
#
#
# tree = TreeNode('mirrorfunctions')
#
# for i in tree.children:
#     print i
# # for i in ceng2:
# #     if i[0] not in tree.name:
# #         tree = TreeNode(i[0])
# #     else:
# #         temp = TreeNode(i[1])
# #         if temp not in tree.children:
# #             tree.children.append(temp)
#
# #将此path变成一个树
# def Tree_Branch(list):
#     temp = 1
#     final =1
#     for i in range(len(list),0,-1):
#         if temp != 1:
#             final = TreeNode(list[i-1])
#             final.children.append(temp)
#             temp = final
#         else:
#
#             temp = TreeNode(list[i-1])
#     return final
#
#
#
#
# tree = Tree_Branch(['mirrorfunctions', '\xe5\x87\xba\xe5\x9c\x9f\xe6\x96\x87\xe7\x8c\xae', '\xe9\xa9\xac\xe7\x8e\x8b\xe5\xa0\x86', '\xe8\x80\x81\xe5\xad\x90A\xe8\x80\x81\xe5\xad\x90\xe7\x94\xb2\xe9\x81\x93\xe7\xbb\x8f.txt'])
#
# #融合两个树
# # def merge_tree(trees1,tree2):
# #     if trees1.name ==tree2.name:
# #
#
# # for i in ceng2:
# #     temp = Tree_Branch(i)
# #     if tree.name == temp.name:
# #         sub = []
# #         for i in tree.children:
# #             sub.append(i.name)
# #         if temp.children[0].name not in sub:
# #             tree.children.append(temp.children[0])
# #         else:
# #             if
# #
# #         # if temp.children[0] not in tree.children:
# #         #     tree.children.append(temp.children[0])
# # #
# # #
# #
# # json_str = json.dumps(tree, sort_keys=True, indent=2)
# # print(json_str)
# #
# # print len(ceng2)
# print len(tree.children)