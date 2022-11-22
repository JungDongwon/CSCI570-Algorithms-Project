# Plot for BASIC (Used the 15 outputs txt files for the input txt files in datapoints directory)

CPUTime = [0.087738037109375,
           0.8220672607421875,
           2.5179386138916016,
           10.80179214477539,
           22.105932235717773,
           41.975975036621094,
           90.14415740966797,
           162.93096542358398,
           266.3109302520752,
           367.57397651672363,
           688.9848709106445,
           1046.4961528778076,
           1545.1898574829102,
           2140.9618854522705, 
           2552.2098541259766]
Memory = [13072,
          13220,
          13356,
          13804,
          14624,
          15908,
          19272,
          23912,
          29832,
          37044,
          55356,
          79000,
          107652,
          141560,
          170420]
ProblemSize = [16,    
               64,
               128,
               256,
               384,
               512,
               768,
               1024,
               1280,
               1536,
               2048,
               2560,
               3072,
               3584,
               3968]


import matplotlib.pyplot as plt

# plotting the points 
plt.plot(CPUTime, ProblemSize)
  
# naming the x axis
plt.xlabel('CPU Time in milliseconds')
# naming the y axis
plt.ylabel('Problem Size')
  
# giving a title to my graph
plt.title('(Basic) CPU time vs problem size')
  
# function to show the plot
plt.show()


######### Memory usage vs problem size
# plotting the points 
plt.plot(Memory, ProblemSize)
  
# naming the x axis
plt.xlabel('Memory usage in KB')
# naming the y axis
plt.ylabel('Problem Size')
  
# giving a title to my graph
plt.title('(Basic) Memory usage vs problem size')
  
# function to show the plot
plt.show()



# (1)
# 0.087738037109375
# 13072
# 16

# (2)
# 0.8220672607421875
# 13220
# 64

# (3)
# 2.5179386138916016
# 13356
# 128

# (4)
# 10.80179214477539
# 13804
# 256

# (5)
# 22.105932235717773
# 14624
# 384

# (6)
# 41.975975036621094
# 15908
# 512

# (7)
# 90.14415740966797
# 19272
# 768

# (8)
# 162.93096542358398
# 23912
# 1024

# (9)
# 266.3109302520752
# 29832
# 1280

# (10)
# 367.57397651672363
# 37044
# 1536

# (11)
# 688.9848709106445
# 55356
# 2048

# (12)
# 1046.4961528778076
# 79000
# 2560

# (13)
# 1545.1898574829102
# 107652
# 3072

# (14)
# 2140.9618854522705
# 141560
# 3584

# (15)
# 2552.2098541259766
# 170420
# 3968