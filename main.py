from openpyxl.styles.builtins import total

menu = {
    "pizza": 59.9,
    "burger": 39.5,
    "tacos": 34.5,
    "sandwich": 24.0,
    "panini": 29.5,
    "salade": 19.0,
    "frites": 14.5,
    "jus": 9.5,
    "coca": 11.5,
    "eau": 5.0
}
cart = []
total = 0
print("-----MENU-----")
for key,value in menu.items():
    print(f"{key}:{value}$")
print("-"*20)
while True:
    food = input("what do you like(q for quit): ").lower()
    if food == "q":
        print("Goodbye!")
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu.get(food)
print("--------YOUR ORDER-------")
for food in cart:
    print(food, end=",")
print()
print(f"so the total is: {total}")
print("-"*25)
