def BracketMatcher(strParam):
  count=0
  for c in strParam:
    if c=='(':
      count+=1
    elif c==')':
      count-=1
  if count!=0:
    return 0
  elif count==0:
    return 1

# keep this function call here 
print(BracketMatcher(input()))
