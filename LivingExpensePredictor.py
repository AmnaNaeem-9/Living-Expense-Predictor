# Living Expense Predictor (Simple Python Project)

print("====== Living Expense Predictor ======")

# User Inputs
city = input("Enter city name: ").lower()

living_type = input("Living type (hostel/apartment/house): ").lower()

room_type = input("Room type (single/shared): ").lower()

food = input("Food type (mess/cooking/restaurant): ").lower()

transport = input("Transport (walk/bike/public/car): ").lower()

# Base expenses
rent = 0
food_cost = 0
transport_cost = 0
utility = 0
other = 0


# City based rent
if city == "lahore":
    base_rent = 15000
elif city == "islamabad":
    base_rent = 20000
elif city == "karachi":
    base_rent = 18000
else:
    base_rent = 12000


# Living type calculation
if living_type == "hostel":
    rent = base_rent * 0.7

elif living_type == "apartment":
    rent = base_rent * 1.5

elif living_type == "house":
    rent = base_rent * 2

else:
    rent = base_rent


# Room type
if room_type == "shared":
    rent = rent / 2


# Food calculation
if food == "mess":
    food_cost = 8000

elif food == "cooking":
    food_cost = 5000

elif food == "restaurant":
    food_cost = 15000

else:
    food_cost = 7000


# Transport calculation
if transport == "walk":
    transport_cost = 500

elif transport == "bike":
    transport_cost = 3000

elif transport == "public":
    transport_cost = 5000

elif transport == "car":
    transport_cost = 15000

else:
    transport_cost = 3000


# Utilities
utility = 5000

# Other expenses
other = int(input("Enter other monthly expenses: "))


# Total
total = rent + food_cost + transport_cost + utility + other


print("\n====== Expense Prediction ======")

print("Estimated Monthly Expense: Rs.", int(total))

print("Estimated Yearly Expense: Rs.", int(total * 12))


print("\nBreakdown:")
print("Rent: Rs.", int(rent))
print("Food: Rs.", food_cost)
print("Transport: Rs.", transport_cost)
print("Utilities: Rs.", utility)
print("Other: Rs.", other)


if total < 25000:
    print("\nSuggestion: Your budget is economical.")

elif total < 50000:
    print("\nSuggestion: Your budget is moderate.")

else:
    print("\nSuggestion: Your budget is high.")