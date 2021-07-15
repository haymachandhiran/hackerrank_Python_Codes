# def dis_word_order(w, n):
#     dis_word = 1
#     dis_word_count = []
#     for i in range(N-1):
#         temp = 0
#         c = 1
#         for j in range(i+1, N):
#             if w[i] != w[j]:
#                 pass
#             else:
#                 temp = 1
#                 c += 1
#         if temp == 0:
#             dis_word += 1
#         dis_word_count.append(str(c))
#     print(dis_word)
#     print(' '.join(dis_word_count))
#
#
# N = input()
# N = int(N)
# words = []
# for i in range(N):
#     words.append(input())
# dis_word_order(words, N)

from collections import Counter
N = input()
N = int(N)
words = []
for i in range(N):
    words.append(input())
unique_words = set(words)
# print(unique_words)
dis_word = len(unique_words)
dis_word_count = Counter(words)
# print(dis_word_count)
print(dis_word)
for i, j in dis_word_count.items():
    print(j, end=' ')



