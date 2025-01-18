p_cost=int(input("enter the product amount:"))
location=input("enter your location:")
amount=0
match location:
    case "us":
        s_cost=5
    case "europe":
        s_cost=7
    case "canada":
        s_cost=3
amount=p_cost+s_cost
print('amount',amount)




