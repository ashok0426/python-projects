def check(num):
    if num>=0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"
num=int(input("Enter the number to check if number is positive , negaive or zero \n"))
result=check(num)
print("The number ",num,"is",result)
