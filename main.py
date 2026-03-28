import pandas as pd
import pickle
import time

try:
    with open('price-predictor.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    print("Error: Could not find the model. Run model-trainer.py first!")
    exit()



print("\n" + "="*50)
print("  ESTIMATE YOUR PROPERTY'S MARKET VALUE ")
print("="*50)

area = input("Enter Carpet Area in sqft:   ")
bhk = input("Enter number of Bedrooms : ")
        
baths = input("Enter number of Bathrooms:")
        
print("\n--- Details ---")
location = input("Enter City/Location where you want to buy: ")
furnish = input("Furnishing details (e.g. furnished/unfurnished): ")
floor = input("Floor detail (e.g. 1st floor, 2nd floor): ")

resale_input = input("🔄 Is it a Resale? (y/n): ")
is_resale = 1 if resale_input.lower() == 'y' else 0

user_data = pd.DataFrame([{
            'BHK': float(bhk),
            'Area': float(area),
            'Is_Resale': is_resale,
            'Bathrooms': float(baths),
            'Location': location,
            'Floor': floor,
            'Furnishing': furnish
        }])

print("\n Calculating market value based on current data...")

predicted_price = model.predict(user_data)[0]

print("\n" + "-"*50)
print(f"  ESTIMATED PROPERTY VALUE: ₹{predicted_price:,.2f}")
print("-"*50 + "\n")