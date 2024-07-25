print("Welcome in zaika")
menu = {
    "chowmin": 70,
    "cold drink": 50,
    "chicken rice": 130,
    "biryani": 140,
    "roasted chicken": 250,
    "pasta": 70,
    "pawbhaji": 60,
    "sandwich": 20
}
print("our menu:")
print("_____")
total_order = 0
for item , price in menu.items():
    print(f"{item}: rs.{price}")

next_order = True
while next_order:
    order = input("enter the name of item you want to order").lower()
    if order in menu:
        total_order += menu[order]
        print(f"{order} added in your order")
        another_order = input("do you want to add another item? pres(yes/no").lower()
        if another_order =='yes':
            next_order = True
        else:
            next_order = False

    else:
        print(f"{order} is not available")
        another_order = input("do you want to add another item? pres(yes/no)".lower())
        if another_order =='yes':
           next_order = True
        else:
           next_order = False

print(f"your total bill is : rs.{total_order}")