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

def dp(s1,s2):
    global m, n, table
    m = len(s1)
    n = len(s2)
    table = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        table[i][0] = i*delta
    for j in range(n+1):
        table[0][j] = j*delta
    for i in range(1,m+1):
        for j in range(1,n+1):
            table[i][j] = min(table[i-1][j-1]+alpha[look_up[s1[i-1]]][look_up[s2[j-1]]], table[i-1][j]+delta, table[i][j-1]+delta)
  
    return table[m][n]

def topDown(table, optCost):
    dp_s1=list()
    dp_s2=list()
    i = m
    j = n

    table[m][n] = -1

    optval = optCost
    while (i != 0) or (j != 0):
        if (optval - alpha[look_up[generatedStr1[i-1]]][look_up[generatedStr2[j-1]]] == table[i-1][j-1]):
            optval = table[i-1][j-1]
            table[i-1][j-1] = -1
            j -= 1
            i -= 1
        elif (optval - delta == table[i][j-1]): #가로 체크
            optval = table[i][j-1]
            table[i][j-1] = -1
            j -= 1
        elif (optval - delta == table[i-1][j]): #세로 체크
            optval = table[i-1][j]
            table[i-1][j] = -1
            i -= 1
      
    table[0][0] = 0
    prev_x=0
    prev_y=0
  
    for i in range(m+1):
        for j in range(n+1):
            if (table[i][j] == -1):
                if (i != prev_x and j != prev_y):
                    dp_s1.append(generatedStr1[i-1])
                    dp_s2.append(generatedStr2[j-1])
                elif(i == prev_x):
                    dp_s1.append('_')
                    dp_s2.append(generatedStr2[j-1])
                elif(j == prev_y):
                    dp_s1.append(generatedStr1[i-1])
                    dp_s2.append('_')
            
                prev_x = i
                prev_y = j
    
    return (''.join(dp_s1), ''.join(dp_s2))
 

def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed
 
def time_wrapper(generatedStr1, generatedStr2):
    start_time = time.time()
    optval = dp(generatedStr1,generatedStr2)
    strSol1, strSol2 = topDown(table, optval)
    end_time = time.time()
    time_taken = (end_time - start_time)*1000
    return [optval, strSol1, strSol2, time_taken] # returns [cost, strsol1, strsol2, time]
 
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

# ==== main() ====
def main():
    global s1, s2
    global strinput, s1_j, s2_k
    global generatedStr1, generatedStr2
    strinput = []
    s1_j = []
    s2_k = []
    global delta, alpha, look_up
    delta = 30
    alpha = [[0,110,48,94],[110,0,118,48],[48,118,0,110],[94,48,110,0]]
    look_up = {'A':0, 'C':1, 'G':2, 'T':3}
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    OpenFile(input_file)
    generatedStr1, generatedStr2 = generateStr(strinput, s1_j, s2_k)
    answers = time_wrapper(generatedStr1, generatedStr2) # optivalVal, strSol1, strSol2, time
 
    memory  = process_memory()
    toOutput(output_file, answers[0], answers[1], answers[2], answers[3], memory)

# == Call Main() ==
main()