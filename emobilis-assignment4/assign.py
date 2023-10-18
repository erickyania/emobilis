name = str(input(" enter your name--> "))
mark1= int(input("\nenter your maths---> "))
mark2 = int(input("\nenter your geo---> "))
mark3 = int(input("\nenter your physics---> "))
mark4 = int(input("\nenter your chem---> "))

total = mark1 + mark2 + mark3 + mark4
totalmarks = total/4

if totalmarks <=0:
    print(f"{name} {totalmarks} This is invalid mark's")

elif totalmarks >= 1 and totalmarks <= 30:
    print(f"{name} a mark of {totalmarks} = D")


elif totalmarks >=31 and totalmarks <=50:
    print(f"{name} a mark of {totalmarks} == C")


elif totalmarks >=51 and totalmarks <=70:
    print(f"{name} a mark of {totalmarks} == B")


elif totalmarks >=71 and totalmarks <=100:
    print(f"{name} a mark of {total} == A")


else:
    print("invalid because it execeds 100")