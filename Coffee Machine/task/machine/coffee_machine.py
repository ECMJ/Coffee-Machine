# Write your code here
print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")
water = 200
milk = 50
beans = 15
quant = int(input("Write how many cups of coffee you will need: "))
nwater = quant * water
nmilk = quant * milk
nbeans = quant * beans
print("For",quant , "cups of coffee you will need:")
print(nwater, "ml of water")
print(nmilk, "ml of milk")
print(nbeans, "g of coffee beans")
