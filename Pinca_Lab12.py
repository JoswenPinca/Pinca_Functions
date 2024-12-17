fooditems = ["Chicken Burger", "Cheeseburger", "Fries", "6 Pc Chicken Nuggets", "Coke Float", "Coca Cola", "Ice Tea", "Sprite"]
foodprice = [60, 52, 35, 80, 50, 25, 25, 25]
orderlist = []
orderlistprice = []

def OrderSystem():
    order=input("Choose between 1-8: ")
    while True:
        if order == "Exit":
            break
        elif order == "1" or order == "2" or order == "3" or order == "4" or order == "5" or order == "6" or order == "7" or order == "8":
            order=int(order)
            index = order-1
            foodorder = fooditems[index]
            priceorder = foodprice[index]
            orderlist.append(foodorder)
            orderlistprice.append(priceorder)
            print(f"You have ordered {foodorder} for {priceorder}₱")
        else:
            print("Invalid Input. Please Try Again!")
        order=input("Order more? (Type Exit to Finish Order): ")
        
def PaymentSystem():
    while True:
        payment = int(input("Input your Payment: "))
        if payment >= totalprice:
            print(f"I received {payment}₱")
            change = payment - totalprice
            if change > 0:
                print(f"Your Change is {change}₱. Thank you for Ordering at MCDonalds! See you next time!")
                break
            else:
                print("You receive no change. Thank you for Ordering at MCDonalds! See you next time!")
                break
        else:
            print("Payment is Insufficient for your Order. Please Try Again!")

print("Welcome to MCDonalds! Here is our Menu:")
for num in fooditems:
    index = fooditems.index(num)
    price = foodprice[index]
    print(f"{index+1}. {num}: {price}₱")
print("What will be your Order?")
OrderSystem()
totalprice = sum(orderlistprice)
print(f"You have ordered:")
for item in orderlist:
    print(item, end=' ')
    print()
print(f"for {totalprice}₱.")
PaymentSystem()