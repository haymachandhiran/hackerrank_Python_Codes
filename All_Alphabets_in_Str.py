#https://www.youtube.com/watch?v=YizKS-di6gM&list=PL7f0FYY_3hQDS79OekQv5PO7jCDGUaEyk&index=10

#If str contains all alpha then print YES. If not print NO

#IP: The quick brown fox jumps over the little lazy dog

#IP: The quick1203^&*$Q) brown fox jumps over the little lazy dog

#IP: The quicq brown fox jumps over the little lazy dog
s = input()
alpha_count = [0] * 26
s.lower()
for i in s:
    if i.isalpha():
        x = ord(i) - 97
        alpha_count[x] += 1
print(alpha_count)
if 0 in alpha_count:
    print('NO')
else:
    print('YES')
print(ord('A'))