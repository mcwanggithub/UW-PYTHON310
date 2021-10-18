def string_bits(str):
  result =""
  for i in range(len(str)):
    clip = str[i:i+1]
    print(i)
    print(clip)
    if i%2 == 0:
        result += clip
  return result
