def romantoInteger(roman):
  map={
          'I', 1 ,
     'V', 5 ,
     'X', 10 ,
     'L', 50 ,
     'C', 100 ,
     'D', 500 ,
     'M', 1000 
  }
  sum=0
  for i in range(0,len(roman)-1):
      if map[roman[i]]<map[roman[i+1]]:
          z-=map[roman[i]]
      else:
          z+=map[roman[i]]
  return z+map[roman[-1]]