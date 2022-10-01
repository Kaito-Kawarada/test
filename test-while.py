is_awake=True
count=0
while is_awake==True:
    count +=1
    print('羊が{}匹'.format(count))
    key=input('Are you sleeping?(y/n)>>')
    if key=='y':
        is_awake=False
print("Good night...")