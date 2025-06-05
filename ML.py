# 1. Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# 2. Load your CSV
df = pd.read_csv(r"C:\products.csv")

# 3. Drop rows with missing values in relevant columns
df = df.dropna(subset=['category', 'id', 'title', 'price'])

# 4. Select features (X) and target (y)
X = df[['id', 'title', 'price']]
y = df['category']

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 7. Make predictions and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# 8. Save model
joblib.dump(model, 'baro_altitude_model.pkl')
print("Model saved as 'baro_altitude_model.pkl'.")