# -*- coding: utf-8 -*-
#16916 2
import sys
str = input()
S = list(str)
find = input()
P = list(find)
pi_s = 1
pi_m = 0
S_s = 0
S_m = 0
pi = [0 for i in range(len(P))]
while(pi_s + pi_m < len(P)):
    if (P[pi_s + pi_m] == P[pi_m]):
        pi_m += 1
        pi[pi_s + pi_m - 1] = pi_m
    else:
        if pi_m == 0:
            pi_s += 1
        else:
            pi_s += pi_m - pi[pi_m - 1]
            pi_m = pi[pi_m - 1]
            
            
while(S_s <= len(S) - len(P)):
    if S_m < len(P) and S[S_s + S_m] == P[S_m]:
        S_m += 1
        if S_m == len(P):
            print(1)
            sys.exit()
    else:
        if S_m == 0:
            S_s += 1
        else:
            S_s += S_m - pi[S_m - 1]
            S_m = pi[S_m - 1]
print(0)