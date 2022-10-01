scores={'math':90, 'English':33, 'Classical_Japanese':4}
scores['physics']=90
scores['chemistry']=80
scores['Classical_Japanese']=40
total=sum(scores.values())
print(total)
print(scores)
del scores['Classical_Japanese']
total=sum(scores.values())
print(total)
print (scores)