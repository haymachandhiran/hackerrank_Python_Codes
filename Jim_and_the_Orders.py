#https://www.hackerrank.com/challenges/jim-and-the-orders/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#
# def jimOrders(n, orders):
#     delivery = {}
#     for i in range(1, n + 1):
#         delivery[sum(orders[i-1])] = i
#     print(delivery)
#     print(sorted(delivery))
#     res = []
#     for i in sorted(delivery):
#         res.append(delivery[i])
#     return res
#
#
# n = int(input())
# orders = []
# for _ in range(n):
#     orders.append(list(map(int, input().rstrip().split())))
# result = jimOrders(n, orders)
# result = list(map(str, result))
# print(f"{' '.join(result)}")


def jimOrders(orders):
    print(list(enumerate(orders,1)))
    s = sorted(enumerate(orders,1),key=lambda x:sum(x[1]))
    print(s)
    return (i[0] for i in s)


n = input()
n = int(input())
orders = [tuple(map(int, input().split())) for i in range(n)]
print(*jimOrders(orders))
