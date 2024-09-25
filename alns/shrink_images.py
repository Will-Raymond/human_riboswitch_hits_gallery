# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:23:20 2024

@author: willi
"""

import os
import PIL
from PIL import Image

folder = './dot/'
for file in os.listdir(folder):
    img_path = file
    img = Image.open(folder + img_path)
    img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
    ratio = .8
    s = img.size
    img.resize((int(s[0]*ratio), int(s[1]*ratio)))
    img.save(folder + file, optimize=True)