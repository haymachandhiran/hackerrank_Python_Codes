# Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index ).

# NOTE: Required Time Complexity O(n2).

# Input:
# The first line of input consists number of the testcases. The following T lines consist of a string each.

# Output:
# In each separate line print the longest palindrome of the string given in the respective test case.

# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ Str Length ≤ 104

# Example:
# Input:
# 1
# aaaabbaa

# Output:
# aabbaa

# Explanation:
# Testcase 1: The longest palindrome string present in the given string is "aabbaa".


T = int(input())

def palind(s):
  pal=[]
  for i in range(len(s)):
    for j in range(i,len(s)):
        if s[i]==s[j]:
            temp=s[i:j+1]
            if temp==temp[::-1]:
                pal.append(temp)

  sor_pal=sorted(pal,key=len,reverse=True)
  return (''.join(sor_pal[0:1]))

     
     
while(T>0):
 s= str(input()) 
 print(palind(s))
 T-=1
 
  
#another method

T = int(input())

def palind(s):
  pal=''
  l=0
  for i in range(len(s)):
    for j in range(i,len(s)):
        if s[i]==s[j]:
            temp=s[i:j+1]
            if l == len(temp):
              pass
            if temp==temp[::-1] and l<len(temp):
                pal = temp
                l = len(pal)
  return pal
     
     
while(T>0):
 s= str(input()) 
 print(palind(s))
 T-=1  

     
     