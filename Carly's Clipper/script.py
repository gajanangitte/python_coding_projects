hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0

for p in prices:
  total_price += p
  
average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))

new_prices = [p-5 for p in prices ]

print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue = prices[i]*last_week[i]
  
print("Total revenue: "+ str(total_revenue))

average_daily_revenue = total_revenue/7

cuts_under_30 = []
for i in range(len(hairstyles)):
  if prices[i] < 30:
    cuts_under_30.append(hairstyles[i])
    
print(cuts_under_30)
    
  