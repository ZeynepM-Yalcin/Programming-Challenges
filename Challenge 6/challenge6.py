def latin():
  order = int(input("enter order: "))
  top_left = int(input("enter top left number: "))
  numbers = []
  lines= []
  
  top_left -= 1
  for i in range(1,order+1):
    numbers.append(i)
    
  for j in range(0,order):
    lines.append(numbers[j:])
    lines[j].extend(numbers[:j])
    
  for k in range(top_left,len(lines)):
    print(*lines[k])
    
  for l in range(0,top_left):
    print(*lines[l])

if __name__ == '__main__':
    latin()
