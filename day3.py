#booleans
print(10 > 9) #is this true or false?
#booleans are used to evaluate expressions and conditions in python
#they are used to check if an experession is true or false
broughtFood = True 
print(broughtFood)

is_raining = True
if is_raining:
    print("Take an umbrella!")
else:
    print("No umbrella needed.")

temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


age = 22 
if age >= 19:
    message = "Eligible"
else:
    message = "Not elegible"
print(message)


# Ask the user to input the current weather. This can be simplified to three categories for ease: "sunny", "rainy", or "cold".

weather = input("What is the current weather? (sunny, rainy, or cold):" )
print(weather)

# Implement the decision structure to advise on what to wear:
# If the weather is "sunny", recommend "wear sunglasses and a hat".
elif weather == "sunny":
    print("wear sunglasses and a hat")

# If the weather is "rainy", recommend "carry an umbrella and wear waterproof boots".
elif weather == "rainy":  
    print("carry an umbrella and wear waterproof boots")
# If the weather is "cold", recommend "wear a warm coat and gloves".
elif weather == "cold"
    print("wear a warm coat and gloves")
# If the input doesn't match any category, inform the user with a message saying the input was not recognized.
else:
    print("input not recognized")