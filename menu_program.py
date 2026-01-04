count =0
while True:
    print("Choose what to do ")
    print("Add ")
    print("Subtract")
    print("multiply")
    A=input("Choose option \n").lower()
    if A=="exit":
        break
    B=int(input("Enter a first number "))
    C=int(input("Enter second number"))
    if A=="Add":
        count=B+C
        print("result",count)
    elif A=="subtract":
        count=B-C
        print("Result",count)
    elif A=="multiply":
        count=B*C
        print("Result",count)
    else:
     print("INVALID")