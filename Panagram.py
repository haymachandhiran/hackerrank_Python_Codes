def pangrams(s):
    s = s.lower()
    alpha = list(map(chr, range(97, 123)))
    for i in range(len(alpha)):
        if alpha[i] not in s:
            return 'not pangram'
    return 'pangram'


s = input()
print(pangrams(s))
