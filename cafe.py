# Create a menu
menu = ["coffee" , "muffin", "sandwich", "burger"]
stock = {
     "coffee":  40,
     "muffin": 30,
     "sandwich": 50,
    "burger" : 80
 }
price = {
     "coffee": 20,
     "muffin": 15,
     "sandwich": 25,
     "burger": 40
 }  
total_stock = 0 
total_stock1 = 0 
total_stock2 = 0 
total_stock3 = 0 


for item in menu:
    item_value =  stock["coffee"] * price["coffee"]
    total_stock += item_value
    item_value1 = stock["muffin"] * price["muffin"]
    total_stock1 += item_value1
    item_value2 =  stock["sandwich"] * price["sandwich"]
    total_stock2 += item_value2
    item_value3 = stock["burger"] * price["burger"]
    total_stock3 += item_value3

    total_stock4 = item_value3 + item_value + item_value2 +item_value1


print("The total stock is : " , total_stock4)


