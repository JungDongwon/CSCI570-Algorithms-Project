import sys
from resource import *
import time
import psutil

def OpenFile(input_file):
    with open(input_file, 'r') as input:
        on_s1 = True
        strinput.append(input.readline().strip())
        for line in input:
            if on_s1:
                if line.strip()[0] in {"A","C","G","T"}:
                    strinput.append(line.strip())
                    on_s1 = False
                else:
                    s1_j.append(int(line.strip()))
            else:
                s2_k.append(int(line.strip()))

def generateStr(strings, j, k):
    str1, str2 = strings[0], strings[1]
    for idx in range(len(j)):
        str1 = changeStr(str1, j[idx])
        
    for idx in range(len(k)):
        str2 = changeStr(str2, k[idx])
        
    return str1, str2

def changeStr(string, idx):
    left = string[:idx+1]
    right = string[idx+1:]
    return left + string + right

def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed

def time_wrapper(generatedStr1, generatedStr2):
    start_time = time.time()
    strSol1, strSol2, optval = efficient(generatedStr1,generatedStr2,0)
    end_time = time.time()
    time_taken = (end_time - start_time)*1000
    return [optval, strSol1, strSol2, time_taken] # returns [cost, strsol1, strsol2, time]

def optimized_dp(s1,s2):
    m = len(s1)
    n = len(s2)
    table = [[0]*(n+1) for _ in range(2)]
    for j in range(n+1):
        table[0][j] = j*delta
    for i in range(1,m+1):
        table[i%2][0] = i*30
        for j in range(1,n+1):
            table[i%2][j] = min(table[(i-1)%2][j-1]+alpha[look_up[s1[i-1]]][look_up[s2[j-1]]], table[(i-1)%2][j]+delta, table[i%2][j-1]+delta)
    return table[m%2]

def efficient(s1,s2,cost):   
    m = len(s1)
    n = len(s2) 
    if n == 0:
        return s1, '_'*m, cost+30*m
    elif m == 0:
        return '_'*n, s2, cost+30*n
    elif m == 1:
        if n == 1:
            return s1, s2, cost+alpha[look_up[s1]][look_up[s2]]
        else:
            pivot = s2.find(s1)
            if pivot == -1:
                if s1 == 'G':
                    pivot1 = s2.find('A')
                    if pivot1 == -1:
                        return s1 + '_'*n, '_'*m + s2, cost+30*(m+n)
                    else:
                        return '_'*(pivot1) + s1 + '_'*(n-pivot1-1), s2, cost+30*(n-1)+alpha[look_up['G']][look_up['A']]
                elif s1 == 'A':
                    pivot1 = s2.find('G')
                    if pivot1 == -1:
                        return s1 + '_'*n, '_'*m + s2, cost+30*(m+n)
                    else:
                        return '_'*(pivot1) + s1 + '_'*(n-pivot1-1), s2, cost+30*(n-1)+alpha[look_up['A']][look_up['G']]
                elif s1 == 'C':
                    pivot1 = s2.find('T')
                    if pivot1 == -1:
                        return s1 + '_'*n, '_'*m + s2, cost+30*(m+n)
                    else:
                        return '_'*(pivot1) + s1 + '_'*(n-pivot1-1), s2, cost+30*(n-1)+alpha[look_up['C']][look_up['T']]
                elif s1 == 'T':
                    pivot1 = s2.find('C')
                    if pivot1 == -1:
                        return s1 + '_'*n, '_'*m + s2, cost+30*(m+n)
                    else:
                        return '_'*(pivot1) + s1 + '_'*(n-pivot1-1), s2, cost+30*(n-1)+alpha[look_up['T']][look_up['C']]
                else:
                    return s1 + '_'*n, '_'*m + s2, cost+30*(m+n)
            else:
                return '_'*(pivot) + s1 + '_'*(n-pivot-1), s2, cost+30*(n-1)
    else:
        mid = m//2
        result1 = optimized_dp(s1[:mid],s2) 
        result2 = optimized_dp(s1[mid:][::-1],s2[::-1])[::-1]
        min_val, pivot = float("inf"), 0
        for i in range(len(result1)):
            cur = result1[i] + result2[i]
            if cur < min_val:
                min_val = cur
                pivot = i
        s1_left, s1_right, cost1 = efficient(s1[:mid],s2[:pivot],cost)
        s2_left, s2_right, cost2 = efficient(s1[mid:],s2[pivot:],cost)
        return s1_left + s2_left, s1_right + s2_right, cost1+cost2

def toOutput(output_filename, optval, strSol1, strSol2, time, memory):
    outF = open(output_filename, "w")
    # write line to output file
    outF.write(str(optval))
    outF.write("\n")
    outF.write(str(strSol1))
    outF.write("\n")
    outF.write(str(strSol2))
    outF.write("\n")
    outF.write(str(time))
    outF.write("\n")
    outF.write(str(memory))
    outF.close()

alpha = [[0,110,48,94],[110,0,118,48],[48,118,0,110],[94,48,110,0]]
delta = 30
look_up = {'A':0, 'C':1, 'G':2, 'T':3}
input_file = sys.argv[1]
output_file = sys.argv[2]
strinput = []
s1_j = []
s2_k = []
OpenFile(input_file)
generatedStr1, generatedStr2 = generateStr(strinput, s1_j, s2_k)
answers = time_wrapper(generatedStr1, generatedStr2) # optivalVal, strSol1, strSol2, time

memory  = process_memory()
toOutput(output_file, answers[0], answers[1], answers[2], answers[3], memory)








