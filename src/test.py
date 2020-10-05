
from itertools import groupby 
  
# initializing list  
# test_list = ['geek_1', 'coder_2', 'geek_4', 'coder_3', 'pro_3'] 
test_list = ['5*X^0', '-4*X^1', '-9.3*X^2', "-5*X^2"]
test_list = ['5*X^0', '-4*X^1', '-9.3*X^2', '2*X^0']
# sort list  
# essential for grouping 
test_list.sort() 
  
# printing the original list  
print ("The original list is : " + str(test_list)) 
  
# using lambda + itertools.groupby() + split() 
# group similar substrings 
# res = [list(i) for j, i in groupby(test_list, lambda a: a.split('_')[0])]
res = [list(i) for j, i in groupby(test_list, lambda a: a[a.find('^') + 1])]
  
# printing result 
print ("The grouped list is : " + str(res)) 