def string_match(a, b):
  count = 0
  for i in range(len(a)):
      print(i)
      print(a[i:i+2])
      print(b[i:i+2])
      print(' ')
      if a[i:i+2] == b[i:i+2]:
          count +=1
  return count