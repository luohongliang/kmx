# -*- coding:UTF-8 -*-

import chardet
import codecs
import os
import os.path
import string
import sys
import csv
import json
from hanziconv import HanziConv
from collections import defaultdict
reload(sys)
sys.setdefaultencoding( "utf-8" )


def tree():
    return defaultdict(tree)

users = tree()
users['first']['second']='luohongliang'
users['first1']['second']='lhl'


print json.dumps(users)

def add(t,keys):
    for key in keys:
        t = t[key]

class TreeNode(dict):
    def __init__(self, name, children=None):

        self.__dict__ = self
        self.name = name
        self.children = [] if not children else children

def from_dict(dict_):
    """ Recursively (re)construct TreeNode-based tree from dictionary. """
    root = TreeNode(dict_['name'], dict_['children'])
    root.children = list(map(TreeNode.from_dict, root.children))
    return root

import json

tree = TreeNode('Parent')
tree.children.append(TreeNode('Child 1'))
child2 = TreeNode('Child 2')
tree.children.append(child2)
child2.children.append(TreeNode('Grand Kid'))
child2.children[0].children.append(TreeNode('Great Grand Kid'))

json_str = json.dumps(tree, sort_keys=True, indent=2)
print(json_str)

print()

