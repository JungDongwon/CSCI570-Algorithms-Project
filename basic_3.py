#Sample
s1 = 'AACAAGAG'
s2 = 'CAAGAC'

#input 1
s1 = 'ACACACTGACTACTGACTGGTGACTACTGACTGGACTGACTACTGACTGGTGACTACTGACTGG'
s2 = 'TATTATTATACGCTATTATACGCGACGCGGACGCGTATACGCTATTATACGCGACGCGGACGCG'

# #input 2
# s1 = 'ACACACTGACTACTGACTGGTGACTACTGACTGGACTGACTACTGACTGGTGACTACTGACTGG'
# s2 = 'TTATTATACGCGACGCGATTATACGCGACGCG'

# #input 3
# s1 = 'AAAAAAGTCGTCAGTCGTCAAGTCGTCAGTCGTCAAAGTCGTCAGTCGTCAAGTCGTCAGTCGTCAAAAGTCGTCAGTCGTCAAGTCGTCAGTCGTCAAAGTCGTCAGTCGTCAAGTCGTCAGTCGTC'
# s2 = 'TATATATATATACGCGTACGCGTATACGCGTACGCGTATATACGCGTACGCGTATACGCGTACGCGTATATATACGCGTACGCGTATACGCGTACGCGTATATACGCGTACGCGTATACGCGTACGCG'

# #input 4
# s1 = 'TCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGTCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGAA'
# s2 = 'TCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGA'

# # #input 5
# # s1 = 'ACACACAAAAACACACAAAACACACACAAAAACACACAAAACACACAAACACACAACACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACAACACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACAAACACACAACACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACAACACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTACACAAACACACAACACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACAACACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACAAACACACAACACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACAACACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACACACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTCACACGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTGTACGACGTACGTTACGTACGACGTACGTTGTACGACGTACGTT'
# # s2 = 'TTTATTTTTTATTTTTATTTTATTTTTTATTTTTATTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTATTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTATTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTATTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTATTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTATTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTATTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTATTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTATTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTATTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTATTATTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCGTTTATTATACGCGACGCGATTATACGCGACGCGATACGCGACGCGATTATACGCGACGCG'

delta = 30
alpha = [[0,110,48,94],[110,0,118,48],[48,118,0,110],[94,48,110,0]]
look_up = {'A':0, 'C':1, 'G':2, 'T':3}

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

    # print(table)
 
    i = m
    j = n

    table[m][n] = -1

    optval = optCost

    while (i != 0) or (j != 0):
        if (optval - alpha[look_up[s1[i-1]]][look_up[s2[j-1]]] == table[i-1][j-1]):
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
                    dp_s1.append(s1[i-1])
                    dp_s2.append(s2[j-1])
                elif(i == prev_x):
                    dp_s1.append('_')
                    dp_s2.append(s2[j-1])
                elif(j == prev_y):
                    dp_s1.append(s1[i-1])
                    dp_s2.append('_')

                prev_x = i
                prev_y = j

    print(''.join(dp_s1))
    print(''.join(dp_s2))

# ==== main() ====
optval = dp(s1, s2)
print(optval)
topDown(table, optval)