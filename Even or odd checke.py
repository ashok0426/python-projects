def check(num):
    if num%2==0:
        return "Even"
    else:
        return "odd"
num=int(input("enter a number to check even if its odd or even \n"))
result = check(num)
print("The given number",num,"is",result)