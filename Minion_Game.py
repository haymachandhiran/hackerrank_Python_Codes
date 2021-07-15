# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
#
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#
# Your task is to determine the winner of the game and their score.
#
# Input Format
#
# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .
#
# Constraints
#
#
#
# Output Format
#
# Print one line: the name of the winner and their score separated by a space.
#
# If the game is a draw, print Draw.
#
# ample Input
#
# BANANA
# Sample Output
#
# Stuart 12
# Note :
# Vowels are only defined as AEIOU. In this problem,Y  is not considered a vowel.



def minion_game(s, n):
    v = set()
    nv = set()
    vr = 0
    nvr = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in s:
        if i in vowels:
            v.add(i)
        else:
            nv.add(i)
    v = list(v)
    v.sort()
    nv = list(nv)
    nv.sort()
    print(f'Vowels List = {v}')
    print(f'Consonants List = {nv}')
    for i in range(n):
        if s[i] in v:
            vr += n - i
        else:
            nvr += n - i
    print(f'VR = {vr} and NVR = {nvr}')
    if nvr > vr:
        return 'Stuart'+' '+str(nvr)
    elif vr > nvr:
        return 'Kevin' + ' ' + str(vr)
    else:
        return 'Draw'


S = 'APPLE'
N = len(S)
print(minion_game(S, N))
