# -*- coding: utf-8 -*-
import csv


filepath = 'C:\\Project\\Amazon\\test1.csv'
f = open(filepath, 'a+',encoding='utf8',newline='')
writer = csv.writer(f)
writer.writerow([4, 5, 6])
f.close()