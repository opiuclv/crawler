# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:44:34 2018

@author: User
"""

#!/usr/bin/env python

"""
Program:
This program will record log into Excel.
History:
20170707 Kuanlin Chen
"""

#匯入模組(Module)
import sys
import xlwt

#建立Workbook物件
book = xlwt.Workbook(encoding="utf-8")
#使用Workbook裡的add_sheet函式來建立Worksheet
sheet1 = book.add_sheet("Sheet1")

def main(orig_args):
    filename = "example.xls"
    output(filename)

def output(filename):
    #使用Worksheet裡的write函式將值寫入
    sheet1.write(0,0,'AAA')
    sheet1.write(0,1,'BBB')
    #將Workbook儲存為原生Excel格式的檔案
    book.save(filename)

if __name__ == '__main__':
    main(sys.argv)