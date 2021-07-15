#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
    high_record = 0
    low_record = 0
    temp_high = scores[0]
    temp_low = scores[0]
    for i in range(1,len(scores)):
        if scores[i] > temp_high:
            temp_high = scores[i]
            high_record += 1
        if scores[i] < temp_low:
            temp_low = scores[i]
            low_record += 1
    return str(high_record), str(low_record)


n = int(input())
scores = list(map(int, input().rstrip().split()))
result = breakingRecords(scores)
print(' '.join(result))
