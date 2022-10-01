count = 0
passing = 'P'
failed = 'F'
student_num = int(input('How many students are?>>'))
score_list = list()
student_judge_list = list()
while count < student_num:
    score = int(input('No.{} student point is...>>'.format(count+1)))
    score_list.append(score)
    if score_list[count] >= 60:
        student_judgement = passing
    else:
        student_judgement = failed
    student_judge_list.append(student_judgement)
    count += 1
print(score_list)
print(student_judge_list)
total = sum(score_list)
print('Ave:{}'.format(total/student_num))

