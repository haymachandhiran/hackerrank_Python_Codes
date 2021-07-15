#https://www.hackerrank.com/challenges/migratory-birds/problem


def migratoryBirds(arr):
    type_list = []
    for i in range(1, 6):
        type_list.append(arr.count(i))
    x = max(type_list)
    return type_list.index(x) + 1


arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
print(migratoryBirds(arr))

# 6
# 1 4 4 4 5 3
