import csv

written_file = open('shajoarashi.txt','w')
with open('tokyo_2021syazyounerai.csv','r', newline = '') as read_file:
    for text in csv.reader(read_file):
        written_file.writelines(str(text))