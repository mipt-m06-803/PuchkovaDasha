#Список учеников
a_9 = set([str(i) for i in input().split()])
b_9 = set([str(i) for i in input().split()])
c_9 = set([str(i) for i in input().split()])
a_10 = set([str(i) for i in input().split()])
b_10 = set([str(i) for i in input().split()])

all_9 = a_9 | b_9 | c_9
all_10 = a_10 | b_10

college = all_9 - all_10
college_list = sorted(list(college))

print(' '.join(str(v) for v in college_list))
