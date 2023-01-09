
#print("Arvuta peast! ...4*100-55")

#o_vastus=4*100-55

#vastus=int(input("Lahenda ülesanne ..."))

#k=1

#while vastus!=o_vastus:

#    print("Viga! Sisesta Õige vastus on ...", )

#    vastus=int(input("Sisesta vastus ..."))
#    k+=1

#print("Õige vastus! Katsed oli ...",k )

#2varinat while true abil

#print("Arvuta peast! ...4*100-55")
#o_vastus=4*100-55
#vastus=int(input("Lahenda ülesanne ..."))
#k=1
#while True:
#    if vastus ==o_vastus:
#       break
#    else:
#        print("Viga! Sisesta Õige vastus on ...", )
#        vastus=int(input("Sisesta vastus ..."))
#        k+=1
#print("Õige vastus! Katsed oli ...",k )

#x=0

#while x<30:

#    if x%2==1:

#        print(x, end=" ")

#    x+=1

#x=0
#while True:
#    if x%2==1: 
#        print(x, end=" ")
#    x+=1
#    if x==30: break
        
#print("For:")
#for x in range (0,30,1):
#    if x%2==1: print(x, end=" ")

print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => "))))
        break
    except ValueError:
         print("See pole tasiarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("See ei ole täisarv")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c = b = a
    paaris = 0
    paaritu = 0
    while b > 0:
            if b % 2 == 0: #parandatud indeks
                    paaris += 1
            else:
                    paaritu += 1
            b = b // 10           
    print(f"Paarisarvud:{paaris}")
    print(f"Paarituid numbreid:{paaritu}")
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Tagurda* sisestatud number")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b = b + number # b + number
    print("*Ümberpööratud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print(("Syracuse hüpoteesi testimine"))
    print()
    if c % 2 == 0: #parandatud indeks
        print("c on paarisarv. Jagame 2-ga..")
    else:
        print("c on paaritu arv. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
    while c != 1:
            if c % 2 == 0:     #parandatud indeks
                    c = c / 2  #parandatud indeks
            else:
                    c = (3*c + 1) / 2     #parandatud indeks
            print(str(round(c)), end=" ") #ümardati kogusumma
    print()
    print("Hüpotees on õige") #parandatud indeks

