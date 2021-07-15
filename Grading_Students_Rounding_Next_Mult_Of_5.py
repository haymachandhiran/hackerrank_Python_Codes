#https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(g):
    for i in range(len(g)):
        # print(g[i])
        if g[i] > 37:
            t = (g[i]//5) + 1
            # print(t)
            if (t * 5) - g[i] < 3:
                g[i] = t * 5
    return g


grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
result = gradingStudents(grades)
print('\n'.join(map(str, result)))
