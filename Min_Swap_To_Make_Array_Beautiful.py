#https://www.hackerrank.com/challenges/lilys-homework/problem

def cntSwaps(arr):
    print('Enum', list(enumerate(arr)))
    positions = sorted(list(enumerate(arr)), key=lambda e: e[1])
    print('POS', positions)
    swaps = 0

    for idx in range(len(arr)):
        while True:
            if (positions[idx][0] == idx):
                break
            else:
                swaps += 1
                swapped_idx = positions[idx][0]
                positions[idx], positions[swapped_idx] = positions[swapped_idx], positions[idx]

    return swaps


def lilysHomework(arr):
    return min(cntSwaps(arr), cntSwaps(arr[::-1]))


n = int(input())
arr = list(map(int, input().split()))
print(lilysHomework(arr))
