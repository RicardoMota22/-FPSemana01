#Semana01


name = str(input("Enter name of first creature?: "))
name2 = str(input("Enter name of second creature?: "))
name3 = str(input("Enter name of third creature?: "))

HP = int(input("How much Hp does " + name +" have? : "))
Lv = int(input("What Level is " + name +" ? : "))

HP2 = int(input("How much Hp does " + name2 +" have? : "))
Lv2 = int(input("What Level is " + name2 +" ? : "))

HP3 = int(input("How much Hp does " + name3 +" have? : "))
Lv3 = int(input("What Level is " + name3 +" ? : "))


array = [
    [(name), (HP), (Lv)],
    [(name2), (HP2), (Lv2)],
    [(name3), (HP3), (Lv3)]
]  

a = Lv
b = Lv2 
c = Lv3

print (name)
print(HP)
print(Lv)
print (name2)
print(HP2) 
print(Lv2)
print (name3)
print(HP3)
print(Lv3)

print(array)

#ranking levels
def lv ():
    if a < b < c :
        print(name3)
        print(name2)
        print(name)
    elif b < a < c :
        print(name3)
        print(name)
        print(name2)
    elif c < b < a :
        print(name)
        print(name2)
        print(name3)
    elif b < c < a :
        print(name)
        print(name3)
        print(name2)
    elif a < c < b :
        print(name2)
        print(name3)
        print(name)
    else:
        print(name2)
        print(name)   
        print(name3)   
lv()
    
