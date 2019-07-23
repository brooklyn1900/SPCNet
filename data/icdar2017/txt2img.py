#! /usr/bin/python

import os, sys

src_img_dir = "./JPEGImages/"

img_names = []
train_file = open('train.txt','w+')
for filename in os.listdir(src_img_dir):
    img_names.append(filename)
    train_file.writelines(filename + '\n')

train_file.close()
