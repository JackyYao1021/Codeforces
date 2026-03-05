import sys
#import random,os
#from math import ceil,floor,gcd,lcm,sqrt,isqrt #, log, factorial, comb, perm,
#log10, log2, log, sin, asin, tan, atan, radians
#from collections import defaultdict as dd
#from collections import OrderedDict as Od  #ordered set
#from collections import Counter
#from collections import deque as dq #deque  e.g. myqueue=dq(list)
#from bisect import * #bisect_left, bisect(a,value)
#from heapq import * #heappop(Q),heappush,heapify,Q[0] is smallest
#from itertools import permutations(p,r)#combinations(p,r)
#combinations(p,r) gives r-length tuples #combinations_with_replacement
#sys.setrecursionlimit(100000) #default is 1000 
# input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = lambda: sys.stdin.readline().rstrip("\r\n")
sint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
###############################################
#from functools import *
#def cc(i,j):return -1 if abs(i)<abs(j) else 1 if abs(i)>abs(j) else 0
#-1 for less, +1 for greater, 0 for equal 
#a.sort(key=cmp_to_key(cc))
#def query(x, y):print('?', x, y,  flush=True);return sint()
#def answer(x):print('!', x, flush=True)
##from random import getrandbits   ##set up RANDOM for hashing
##RANDOM = getrandbits(32)
#dij = [(0, 1), (-1, 0), (0, -1), (1, 0)] #4 directions
#dij = [(0, 1), (-1, 0), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)] #8 d
#big = float('inf')
#mod=10**9+7
#T = 1
T = sint()
for _ in range(T):
    n,k,x=mint()
#    n=sint()
    a=aint()
    a.sort()
    L=0;R=x+1
    while R-L>1:
        m=(L+R)//2
        tot=max(0,a[0]-m+1)+max(0,x-a[-1]-m+1)
        for i in range(n-1):
            tot+=max(0,(a[i+1]-a[i])-2*m+1)
        if tot>=k:L=m
        else:R=m
    if L==0:
        ans=[i for i in range(k)]
    else:
        ans=[]
        for i in range(a[0]-L+1):ans.append(i)
        for i in range(a[-1]+L,x+1):ans.append(i)
        for i in range(n-1):
            for j in range(a[i]+L,a[i+1]-L+1):
                ans.append(j)
    print(*ans[:k])
