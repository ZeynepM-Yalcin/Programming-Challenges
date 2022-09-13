def in_joules(richter):
    joules = 10**((1.5*richter)+4.8)
    return joules

def in_TNT(joules):
    TNT = joules / (4.184*(10**9))
    return TNT


def calculate():
    richter = float(input("Enter Richter scale value: "))
    joules = in_joules(richter)
    TNT = in_TNT(joules)
    
    print(f"Richter value {richter}")
    print(f"Equivalence in joules: {joules}")
    print(f"Equivalence in tons of TNT: {TNT}")

if __name__ == '__main__':
   calculate()
   
   # for unit test check
   print("xxxxx",in_joules(2))
   print("xxxxx",in_TNT(2))

 


   
