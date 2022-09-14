def in_joules(richter):
    joules = 10**((1.5*richter)+4.8)
    return joules

def in_tnt(joules):
    tnt = joules / (4.184*(10**9))
    return tnt


def calculate():
    richter = float(input("Enter Richter scale value: "))
    joules = in_joules(richter)
    tnt = in_tnt(joules)
    
    print(f"Richter value {richter}")
    print(f"Equivalence in joules: {joules}")
    print(f"Equivalence in tons of TNT: {tnt}")

if __name__ == '__main__':
   calculate()
   
   # for unit test check
   print("xxxxx",in_joules(2))
   print("xxxxx",in_tnt(2))

 


   
