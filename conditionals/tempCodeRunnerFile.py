weather = {"sunny", "rain"}

# Convert the set to a list for easier indexing if needed
weather_list = list(weather)

# Print the options
print("Weather options:", weather_list)

# Prompt the user to enter their choice
weather_choice = input("Please enter the weather (sunny/rain): ").lower()

# Validate the user's input
if weather_choice in weather:
    print(f"You chose: {weather_choice}")
else:
    print("Invalid choice. Please enter either 'sunny' or 'rain'.")