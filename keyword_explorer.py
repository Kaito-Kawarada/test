import csv
from collections import Counter

CTV_list=list()
l=list()
with open('tokyo_2021syazyounerai.csv','r', encoding = "Shift-JIS") as read_file:
    for text in csv.reader(read_file):
        CTV_list.append(text[6])
        l=Counter(CTV_list)
del l['市区町村（発生地）']
del l['']
print(l)