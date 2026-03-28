from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression    
import pickle

import pandas

data=pandas.read_csv('dataset.csv')

features=['Location', 'Floor', 'Furnishing']
numbers=['BHK', 'Area', 'Is_Resale', 'Bathrooms']
input_features =data.drop('Price',axis=1)
predicted_price=data['Price']

processer =ColumnTransformer(
    transformers=[
    ('num', 'passthrough', numbers),
    ('cat', OneHotEncoder(handle_unknown='ignore'), features)
])
final   = Pipeline(steps=[
         ('preprocessor', processer),
        ('model', LinearRegression())
])




final.fit(input_features, predicted_price)

with open('price-predictor.pkl', 'wb') as file:
      pickle.dump(final, file)
print("model is now saved in model folder ")
