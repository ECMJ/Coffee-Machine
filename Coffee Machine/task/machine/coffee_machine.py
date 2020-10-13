# Presentation
# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")

# Asking the amount of ingredients the coffee machine have and amount of cups than can be done
water = int(input("Write how many 'ml' of water the coffee machine has: "))
milk = int(input("Write how many 'ml' of milk the coffee machine has: "))
beans = int(input("Write how many 'g' of coffee beans the coffee machine has: "))
q = int(input("Write how many cups of coffee you will need: "))
# Formulas
cups_water = water//200
cups_milk = milk//50
cups_beans = beans//15
enough_coffee = [cups_water, cups_milk, cups_beans]
lowest = int(min(enough_coffee))
more = lowest - 1
# Show the results
if q == lowest:
    print("Yes, I can make that amount of coffee")
elif q < lowest:
    print("Yes, I can make that amount of coffee (and even", more, "more than that)")
else:
    print("No, I can make only", more + 1, "cups of coffee")

# Output the amount of cups, water, milk and coffee beans
# print("For",q , "cups of coffee you will need:")
# print(water, "ml of water")
# print(milk, "ml of milk")
# print(beans, "g of coffee beans")
