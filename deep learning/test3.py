import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Load dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Preprocess data
X = df.drop('target', axis=1)
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define and compile model
from tensorflow import keras
import tensorflow as tf

def create_model(hidden_units=16, optimizer='adam'):
    model = keras.Sequential()
    model.add(keras.layers.InputLayer(input_shape=(X_train.shape[1],)))
    model.add(keras.layers.Dense(units=hidden_units, activation='relu'))
    model.add(keras.layers.Dense(units=3, activation='softmax'))
    
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Wrap model for use with scikit-learn
from scikeras.wrappers import KerasClassifier
model = KerasClassifier(model=create_model, loss='sparse_categorical_crossentropy', epochs=10, batch_size=32, verbose=0)

# Define parameters for Grid Search
params = {
    'model__hidden_units': [16, 32, 64],
    'model__optimizer': ['adam', 'rmsprop']
}

# Perform Grid Search
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(estimator=model, param_grid=params, cv=3)
grid_result = grid.fit(X_train, y_train)

# Display best parameters and score
print(f"Best parameters: {grid_result.best_params_}")
print(f"Best score: {grid_result.best_score_}")

# Evaluate on test data
test_score = grid.score(X_test, y_test)
print(f"Test score: {test_score}")