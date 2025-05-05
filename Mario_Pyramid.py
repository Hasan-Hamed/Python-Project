def make_mario_pyramid(length):
  l = [" "]*length
  for i in range(1, length+1): 
     l[-i] = "*"
     print(l)


num = 5
make_mario_pyramid(num)