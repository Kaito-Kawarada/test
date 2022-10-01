import csv

CTVcount_list=list()
CTV_list=list()
preCTV='o'
with open('tokyo_2021syazyounerai.csv','r', encoding = "Shift-JIS") as read_file:
    count=1
     for text in csv.reader(read_file):
        if (preCTV != text[6] && CTV_list.find(text) >= 1):
            CTVcount_list.append(count)
            preCTV=text[6]
        else:
            count += 1

