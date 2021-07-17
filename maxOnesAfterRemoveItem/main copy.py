# input_string='100000000011100000000000010101000000001'
# input_list=[0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0]

# input_list=[1,0]
# print("input" + str(input_list))
# print()
# f=1
# new_list=[]
def maxOnesAfterRemoveItem(input_string,f):
  maxLen, c, cnt=0, 0, 0
  input_string.append(0)
  for i in range(len(input_string)):
    if int(input_string[i]) == f:
      c=c+1
    else:
      if c!=0:
        new_list.append(c)
      new_list.append(int(input_string[i]))
      c=0
  
  print(new_list)

  for i in range(len(new_list)):
    try:
      if int(new_list[i]) == 0 and (int(new_list[i-1] != 0 ) or i-1<0) and (int(new_list[i+1]) != 0 or i+1>len(new_list)):
        cnt=int(new_list[i-1]) + int(new_list[i+1])
        maxLen=max(cnt,maxLen)
    except:
      print("asdasd")
  
  print(maxLen)
    # c=c+1 if int(i) == f else 0
    # maxLen=max(c,maxLen)
  # return(maxLen)

# def maxOnesAfterRemoveItem(input_string,f):
#   maxLen, c, cnt, i=0, 0, 0, 0
#   while i < len(input_string):
#     # print(i)
#     if input_string[i] == 1:
#       c=c+1
#     else:
#       c=0
#     i+=1
#     print(c)

def maxOnesAfterRemoveItem(input_string):
  # print("input" + str(input_string))
  f = 1
  maxLen = 0
  for i in range(len(input_string)):
    c=0
    new_list = input_string.copy()
    del new_list[i]
    # print(new_list)
    # for j in range(len(new_list)):
    # max_len=max(max_len,maxLen(new_list,f))
    for j in new_list:
      c=c+1 if int(j) == f else 0
      maxLen=max(c,maxLen)
  print(maxLen)
  return(maxLen)

def maxLen(input_string,f):
  maxLen, c=0, 0
  for i in input_string:
    c=c+1 if int(i) == f else 0
    maxLen=max(c,maxLen)
  return(maxLen)

# maxOnesAfterRemoveItem(input_list,f)


maxOnesAfterRemoveItem([0,0])
maxOnesAfterRemoveItem([0,1])
maxOnesAfterRemoveItem([1,0])
maxOnesAfterRemoveItem([1,1])
maxOnesAfterRemoveItem([1, 1, 0, 1, 1])
maxOnesAfterRemoveItem([1, 1, 0, 1, 1, 0, 1, 1, 1])
maxOnesAfterRemoveItem([1, 1, 0, 1, 1, 0, 1, 1, 1, 0])



# maxLen, i = 0, 0
# len_str=len(input_string)
# while i < len_str:
#   if int(input_string[i]) == 0:
#     c=1
#     for j in range(i+1,len_str):
#       if int(input_string[j]) == 0:
#         c+=1
#       else:
#         break
#     maxLen=max(c,maxLen)
#     i=j
#   i+=1
# print("max: " + str(maxLen))


