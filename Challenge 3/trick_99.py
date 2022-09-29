def check_input(your_number, start, end):
    if (your_number <start) or (your_number > end):
        return True
    else: 
        return False
        

def calculations(your_number, friend_number):
    factor = 99 - your_number
    step1 = int(friend_number + factor)
    step1 = str(step1)
    first_digit = int(step1[0])

    rest_str= step1[1:]
    #print(rest_str)
    result = int(rest_str) + first_digit
    #print(result)
    return result

x = True
y = True
while x == True:
    your_number = int(input("(You)Enter number between 1-49: "))
    x = check_input(your_number, 1, 49)
while y == True:
    friend_number = int(input("(Friend)Enter number between 50-99: "))
    y = check_input(friend_number, 50, 99)
    
final = calculations(your_number, friend_number)
print(final)

if __name__ == '__main__':
    unittest.main()

