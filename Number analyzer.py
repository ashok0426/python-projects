def check(num):
    if num >=0:
        return "positive"
    else:
        return "negative"
num=int(input("Enter the number to check"))
result = check(num)
if num%2==0:
  print("The entered number",num,"is",result,"and even")
else:
    print("The entered number",num,"is",result,"and odd")