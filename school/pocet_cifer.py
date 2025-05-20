# sejf
count = 0
for a in (2,4,6,8):
   for b in range (1,10):
      for c in range (1,10):
         for d in range (1,10):
            if a+b+c+d !=21:
               continue
            print(a,b,c,d, sep="-")
            count += 1

print (f"pocet cifer: {count}")


