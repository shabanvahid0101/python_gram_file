import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Load Bitcoin data
data = yf.download('BTC-USD', start='2020-01-01', end='2024-12-01')
data = data[['Close']]

# Preprocess data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# Create sequences
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

seq_length = 60
X, y = create_sequences(scaled_data, seq_length)

# Split data into training and test sets
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Build LSTM model
model = Sequential()
model.add(LSTM(units=10, return_sequences=True, input_shape=(seq_length, 1)))
model.add(Dropout(0.2))  # Add dropout layer
model.add(LSTM(units=10, return_sequences=True))
model.add(Dropout(0.2))  # Add dropout layer
model.add(LSTM(units=10))
model.add(Dropout(0.2))  # Add dropout layer
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

# Train model
model.fit(X_train, y_train, epochs=32, batch_size=32)  # Increase the number of epochs

# Evaluate model
loss = model.evaluate(X_test, y_test)
print(f"Test loss: {loss}")

# Make predictions
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)

# Plot results
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 5))
plt.plot(data.index[-len(y_test):], scaler.inverse_transform(y_test.reshape(-1, 1)), color='blue', label='Actual BTC Price')
plt.plot(data.index[-len(predictions):], predictions, color='red', label='Predicted BTC Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
