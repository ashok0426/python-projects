def check(tem):
    if tem>=35:
        return "Very hot"
    elif tem>=25:
        return "Warm"
    else:
        return "Cold"
tem=int(input("Enter to check Temperature \n"))
result=check(tem)
print("Temperature of",tem,"is",result)
