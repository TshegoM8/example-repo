
def hotel_cost(nights):
    return nights * 1500

def plane_cost(city):
    if city.lower() == "Bloemfontein":
        return 950
    if city.lower() == "Durban":
        return 800
    elif city.lower() == "Johannesburg":
        return 1040
    else:
        return 600
# Rental car
def car_rental(days):
    return days * 500
#Total amount
def holiday_cost(nights, city, days):
    return hotel_cost(nights) + plane_cost(city) + car_rental(days)
print("City: Bloemfontein, Durban or Johannesburg")
city = input("Where do you want to go?: ")

# User to type number of nights
nights = int(input("For how many nights?: "))
# User to input number of days to rent the car
days = int(input("How many days are you going to rent the car for?: "))

total = holiday_cost(nights, city, days)

print("Your holiday costs")
print(f" Plane to {city} costs R{plane_cost(city)}")
print(f" Hotel for {nights} nights costs R{hotel_cost(nights)}")
print(f" Car for {days} days costs R{car_rental(days)}")
print(f" Total = R{total}")
