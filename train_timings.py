# Problem:
#
# In
# one
# pass, Train
# A
# can
# start
# from the source
#
# station
# at
# time
# T[0], halt
# at
# each
# station
# for h unit of time until it reaches the last station at time T[N – 1], where N is the positive integer representing a total number of stations.
#
# Given, Train
# A’s
# timings
# at
# each
# unit
# of
# time as T[] = {10.00, 10.04, 10.09, 10.15, 10.19, 10.22}.
#
# Now, suppose
# Railway
# Admin
# wants
# to
# add
# more
# trains
# to
# increase
# the
# frequency.So, to
# launch
# other
# Train
# B,
# for the same stations as of Train A’s.Provided the Train B starts at time t, they would like to know the timings for Train B.The program should return a String array S (timestamp( in float) for Train B at each station from first to the last station like train A).
#
# Note:
#
# The
# time is represented in 24 - Hour.
# Start
# Hour
# should
# be in the
# range[0, 23].
# Start
# Minute
# should
# be in the
# range[0, 59].
# Enter
# start
# time(24
# Hrs)
# Examples:
#
# Input: t = 11.00
# Output: 11.00
# 11.04
# 11.09
# 11.15
# 11.19
# 11.22
# Explanation: Start
# time
# for train B is 11.00 and also the time difference between the stations for train B is same as for train A.
#
# Input: t = -26.15
# Output: Invalid
# Input
# Explanation: No
# such
# time as -26.15
# exists.Hence, print “Invalid
# Input”.


import math 

def train_timings(t):
  Train_B=[]
  m= (t-math.trunc(t))*100
  if (math.trunc(t) not in range(24)) or (round(m) not in range(60)):
    return 'Invalid Input'
  Train_B.append(t) 
  for i in range(1,N):
    Train_B.append(round(Train_B[i-1]+(Train_A[i]-Train_A[i-1]),2))
  Train_B= list(map(str,Train_B))  
  return  ' '.join(Train_B)


Train_A = [10.00, 10.04, 10.09, 10.15, 10.19, 10.22]
N = len(Train_A) 
t= round(float(input()),2)
print(train_timings(t))  

    
