#https://www.hackerrank.com/challenges/priyanka-and-toys/problem?h_r=next-challenge&h_v=zen

def min_weight_ontainer(w):
        temp = min(w) + 4
        count = 1
        print(sorted(w))
        for i in sorted(w):
            if i > temp:
                temp = i + 4
                count += 1
        return count


n = int(input())
w = list(map(int, input().split()))
print(min_weight_ontainer(w))
