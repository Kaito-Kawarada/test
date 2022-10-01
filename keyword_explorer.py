import csv
from collections import Counter

ctv_list=list()
ctv_countlist=list()
with open('tokyo_2021syazyounerai.csv','r', encoding = "Shift-JIS") as read_file:
    for text in csv.reader(read_file):
        ctv_list.append(text[6])
ctv_countlist=Counter(ctv_list)
del ctv_countlist['市区町村（発生地）']
del ctv_countlist['']
print(ctv_countlist)