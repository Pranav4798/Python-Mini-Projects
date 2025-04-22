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
print(df)


while True:
    food =input('Enter number to buy (Q to quit): ')
    food1 = int(food)
    if food1 in df.index:
        foods.append(df['Pizza'][food1])
        prices.append(df['Cost in $'][food1])
    else:
        break
        #price = float(input(f'Enter the price of a {food}: $'))
        #foods.append(food)
        #prices.append(price)
for price in prices:
    total += price

tax = total * 10/100

Final = tax + total
df2 = {}

print('-----------Your Cart-----------')

for x, y in zip(foods,prices):
    print (x,y)
#print(data2)
print()
print('--------------------------')
print(f'Total: ${total:.2f}')
print(f'Tax : ${tax:.2f}')
print('--------------------------')
print(f'Grand Total : ${Final:.2f}')