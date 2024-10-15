import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pickle


file_path = 'C:\Users\kesha\Downloads\Annual_CO2_emissions_from_aircraft_operators.xlsx'
try:
    data = pd.read_excel(r'C:\Users\kesha\Downloads\Annual_CO2_emissions_from_aircraft_operators.xlsx')
except FileNotFoundError:
    print(f"Error: The file {"C:\Users\kesha\Downloads\Annual_CO2_emissions_from_aircraft_operators.xlsx"} was not found.")
    exit(1)
except Exception as e:
    print(f"Error reading the Excel file: {e}")
    exit(1)


label_encoder = LabelEncoder()
try:
    if 'Operator Name' not in data.columns:
        raise KeyError("Error: 'Operator Name' column not found in the data.")
    data['Operator Name'] = data['Operator Name'].fillna('Unknown')
    data['Operator_encoded'] = label_encoder.fit_transform(data['Operator Name'])
except KeyError as e:
    print(e)
    exit(1)
except Exception as e:
    print(f"Error encoding 'Operator Name': {e}")
    exit(1)


X = data[['Operator_encoded']]  
y = data['Summary Total Reportable Emissions']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


with open('co2_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training complete and saved to co2_model.pkl.")
