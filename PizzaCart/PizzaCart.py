import pandas as pd

foods = []
prices = []
total = 0

items = ['Margherita', 'Supreme', '5 Cheese', 'Meat Monster', 'Garden']
costs = [14.25, 18.50, 18, 19, 17.50]
#SrNo = [1,2,3,4,5]
#df = pd.DataFrame(data= [items, costs], columns= ['Pizza', 'Cost in $'])
data = {'Pizza': items, 'Cost in $': costs}
df = pd.DataFrame(data=data)
df.index += 1
#print(df)

print("🍕 Welcome to The Pizza Cart 🍕")
print(df.to_string())

while True:
    food =input('Enter number to buy (Q to quit): ').strip()
    if food.upper() == 'Q':
        break
    if food.isdigit():
        food1 = int(food)
        if food1 in df.index:
            foods.append(df.loc[food1, 'Pizza'])
            prices.append(df.loc[food1, 'Cost in $'])
        else:
            print("❌ Invalid item number. Try again.")
        #price = float(input(f'Enter the price of a {food}: $'))
        #foods.append(food)
        #prices.append(price)
    else:
        print("❌ Please enter a number or 'Q' to quit.")

total = sum(prices)
tax = total * 0.10
final = total + tax

df2 = {}

print('\n-----------Your Cart-----------')

for x, y in zip(foods, prices):
    print (f'{x:20} ${y:.2f}')
#print(data2)
print()
print('-------------------------------')
print(f'Total:          ${total:.2f}')
print(f'Tax (10%) :     ${tax:.2f}')
print('-------------------------------')
print(f'Grand Total : ${final:.2f}')
print('🍕 Thank you for ordering from The Pizza Cart! 🍕')
print('Hope you have a wonderful day and do visit us again!')
