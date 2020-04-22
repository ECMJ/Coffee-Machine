# Presentation
#print("Starting to make a coffee")
#print("Grinding coffee beans")
#print("Boiling water")
#print("Mixing boiled water with crushed coffee beans")
#print("Pouring coffee into the cup")
#print("Pouring some milk into the cup")
#print("Coffee is ready!")

# Amount of ingridients to make a cup of coffee(Constants)
water = 200
milk = 50
beans = 15
counter = 0
if water == 250 and milk == 50 and beans == 15:
    cups = 1
    counter += cups

# Asking the amount of ingridients the coffee machine have
qwater = int(input("Write how many ml of water the coffee machine has: "))
qmilk = int(input("Write how many ml of milk the coffee machine has: "))
qbeans = int(input("Write how many ml of coffee beans the coffee machine has: "))

# Asking how many cups of coffees do you need
quant = int(input("Write how many cups of coffee you will need: "))

# Formulas
nwater = quant * qwater
nmilk = quant * qmilk
nbeans = quant * qbeans
ncups = counter
if ncups == 1:
    print("Yes, I can make that amount of coffee")
elif ncups > 1:
    print("(and even", ncups, "more than that)")
else:
    print("No, I can make only",ncups ,"cups of coffee")

# Output the amount of cups, water, milk and coffee beans
#print("For",quant , "cups of coffee you will need:")
#print(nwater, "ml of water")
#print(nmilk, "ml of milk")
#print(nbeans, "g of coffee beans")
