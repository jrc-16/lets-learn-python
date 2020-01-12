print("\nRoad Meister auto shop")
print("==========================\n")
print("Description: Enter the item name, cost and amount. The program calculates the cost (without VAT applied) for the amount wanted, the VAT cost, and the total cost with VAT applied.\n")

# The vat cost. 
vat = int(20)

# Displays costs with 2 decimal places.
costFormatter = '.2f'

itemOneName = input("Enter the item name: ").capitalize()
print("Item name:", itemOneName)
print("\n-------------------------------------------------------\n")

itemOneCost = float( input("How much does one "+itemOneName+" cost? £ ") )
print("One "+itemOneName+" costs: £", format(itemOneCost, costFormatter))
print("\n-------------------------------------------------------\n")

itemOneCount = int( input("Enter the amount of "+ itemOneName + "'s you plan to order? "))
print("Amount:", itemOneCount)
print("\n-------------------------------------------------------\n")

# Multiply the item cost (without vat) by the total amount wanted.
itemOneCostMinusVat = itemOneCount * itemOneCost
print("The total cost (without VAT) for "+itemOneName+ "'s: £", format(itemOneCostMinusVat, costFormatter))
print("\n-------------------------------------------------------\n")

# Display the total vat. 
# The forumula calculates the vat for the total amount of items.
# calculatePercentage() is a reusable function, which in this case, calculates vat.
def calculatePercentage(percent, whole):
  return  (percent * whole) / 100.0 

itemOneCostWithVat = calculatePercentage(vat, itemOneCostMinusVat)
print("The VAT calculated for "+itemOneName+"'s: £", format(itemOneCostWithVat, costFormatter))
print("\n-------------------------------------------------------\n")

# Display the total cost of the item with vat added.
itemOneTotalCost = itemOneCostWithVat+itemOneCostMinusVat
print("The total cost (with VAT added) for " + itemOneName +"'s: £", format(itemOneTotalCost, costFormatter) )
