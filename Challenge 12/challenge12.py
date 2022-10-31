import re

def validate():
    x = True
    while x == True:
        card_no = input("Enter card number: ")
        val = re.search('^[0-9]+$',card_no)
        #print(val)
        if val is None:
            print("must only contain integers")
        else: 
            if len(card_no) < 16:
                print("Too short")
            elif len(card_no) > 16:
                print("Too long")
            else:
                x = False
                print("Card number OK")
                return card_no

def pan(card_no):
    pan_no = card_no[6:15]
    return pan_no

def checksum(card_no):
    checksum_no = card_no[-1]
    return checksum_no

def issuer(card_no):
    if card_no[0] is 3:
        if card_no[1] is not 4 or 7:
            print("Issuer: JCB")
        else:
            print("Issuer: American Express")
    elif card_no[0] is 4:
        print("Issuer: Visa")
    if (card_no[:1]>= 51) and (card_no[:1] <= 55):
        print("Issuer: MasterCard")
    return issuer

def isReal(card_no):
   sum = 0
   length = len(card_no)
   if length%2 == 0:
       for i in range (length):
           if (i+1)%2 == 0:
               sum += int(card_no[i])
           else:
               sum += isReal2(int(card_no[i]))
   else:
       for i in range(length):
           if (i+1)%2 == 0:
               sum += isReal2(int(card_no[i]))
           else:
              sum += int(card_no[i])
   return sum%10



def isReal2(card_no):
   num = 2*int(card_no)
   if num>9:
       return num-9
   else:
       return num

if __name__ == "__main__":
    validate()
    pan(card_no)
    checksum(card_no)
    isReal(card_no)


