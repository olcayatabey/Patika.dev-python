def  FindIntersection(strArr):
  inside=[]
  for x in strArr[0].split(", "):
    if x in strarr[1].split(", "):
      inside.append(x)
      if len(inside)<1:
        return "false"
     return ",".join(inside)
  
  # Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
  print(FindIntersection( input()))  
  #output 1,4,13
  
  print(FindIntersection(["1, 3, 4, 57, 133", "1, 2, 4, 13, 15"]))
  #output 1,4
  
