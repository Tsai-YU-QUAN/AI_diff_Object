# -*- coding: utf-8 -*-
"""
tsai Editor
"""

#參考 https://github.com/nicolashahn/diffimg/blob/master/diffimg/diff.py 改寫
#可參考 https://vimsky.com/zh-tw/examples/detail/python-method-PIL.ImageChops.difference.html

from PIL import Image
from PIL import ImageChops
from PIL import ImageStat

import datetime

def diff(im1_file, 
         im2_file, 
         delete_diff_file=False, 
         diff_img_file=None):
    im1 = Image.open(im1_file)
    im2 = Image.open(im2_file)
    diff_img = ImageChops.difference(im1,im2)
    
    now = datetime.datetime.now()
    diff_img_file = "diff_img_"+str(now.year)+"_"+str(now.month)+"_"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+".png"
    diff_img.convert('RGB').save(diff_img_file)
    stat = ImageStat.Stat(diff_img)
    # can be [r,g,b] or [r,g,b,a]
    sum_channel_values = sum(stat.mean)
    max_all_channels = len(stat.mean) * 100
    diff_ratio = sum_channel_values/max_all_channels
    #if delete_diff_file:
        #remove(diff_img_file)
    return diff_ratio 

import sys
 
def main():
    #intValue = int(sys.argv[1])#如果要將變數搞成數字的話可以使用 int()來轉
    
    diff_ratio  = diff(sys.argv[1],sys.argv[2])
    
    print("分析完成，與合格的圖差 %.2f" %(diff_ratio * 100))
 
if __name__ == "__main__":
    main()