#! /usr/bin/python3
import argparse
import os
import re
import time

home = '/home/fan/.github/fankunpeng.github.io/_posts/'
#博客的markdown文档的存放文件夹
editor = 'emacs '
#默认编辑器，用于打开和编辑markdown文档, 注意后面留个空格 

parser = argparse.ArgumentParser(description='Process jekyll blog file')
parser.add_argument('-l', '--list', action="store_true", help='list the blog title')
parser.add_argument('-a', '--add', action="store_true", help='add a markdown file to your _posts directory with a given title')
parser.add_argument('title', help='the title of your markdown file that you dare to add')
parser.add_argument('-s', '--search', action="store_true", help='search a file with a fragment of its tile')
parser.add_argument('-e', '--edit', action="store_true", help='edit the blogfile with a given tile or a given fragment of the title')
parser.add_argument('-p', '--publish', action="store_true", help='publish to gitpages with default comment the title')

args =  parser.parse_args()

if args.list:
    home_dir = os.listdir(home)
    tit = re.compile(r'^([0-9]*)-([0-9]*)-([0-9]*)-(``.*)\.markdown')
    for filename in home_dir:
        u = tit.match(filename)
        print(u.group(4))

if args.add:
    now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    filename = "{}-{}.markdown".format(now, args.title)
    path = home + filename
    with open(path, 'at') as f:
        print('---', file=f)
        print('layout: post', file=f)
        print('title: {}'.format(args.title), file=f)
        print('tags: ', file=f)
        print('---', file=f)

if args.search:
    se = re.compile(r'^.*%s.*\.markdown'%(args.title))
    post_dir = os.listdir(home)
    for filename in post_dir:
        if se.match(filename):
            print(filename)

if args.edit:
    se = re.compile(r'^.*%s.*\.markdown'%(args.title))
    post_dir = os.listdir(home)
    for filename in post_dir:
        if se.match(filename):
            os.system(editor + home + filename + ' &')

if args.publish:
    os.system("cd " + home)
    os.system("git add --all && git commit -m '" + args.title + "'")
    os.system("git push origin master")
