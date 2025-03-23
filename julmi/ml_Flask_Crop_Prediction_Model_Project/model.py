import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('julmi\ml_Flask_Crop_Prediction_Model_Project\Crop_recommendation.csv',header=0)

x = df.drop('label',axis=1)
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train,y_train)

pickle.dump(model, open('model.pkl','wb'))