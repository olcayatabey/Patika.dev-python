def StringChanges(strParam):
  l = list(strParam)
  res = [] 

  flag = False
  for i in range(len(l)):
    if flag == True: 
      flag = False
      continue

    if l[i] == 'M':  
      if len(res) == 0:  
        continue
      else: 
        res.append(res[-1])
        continue

    if l[i] == 'N':  
      if i == len(l) - 1: 
        continue
      else: 
        flag = True 
        continue

    
  strParam = ''.join(res)

 
  return strParam

print(StringChanges(input()))
