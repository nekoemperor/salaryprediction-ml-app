import numpy as np
import pickle
from salaryprediction.data import load_data, clean_data
from salaryprediction.encoder import label_encoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import LabelEncoder


def train_data():
    X = df_encoded.drop("Salary", axis=1)
    y = df_encoded["Salary"]

    regressor = DecisionTreeRegressor(random_state=0)
    max_depth = [None, 2, 4, 6, 8, 10, 12]
    parameters = {"max_depth": max_depth}

    gs = GridSearchCV(regressor, parameters, scoring='neg_mean_squared_error')
    gs.fit(X, y)

    regressor = gs.best_estimator_
    regressor.fit(X, y)
    y_pred = regressor.predict(X)
    error = np.sqrt(mean_squared_error(y, y_pred))
    return [regressor, error]

def save_model():
    le_education = label_encoder(df)[0]
    le_country = label_encoder(df)[1]
    regressor = train_data()[0]
    data = {"model": regressor, "le_country": le_country, "le_education": le_education}
    with open('model.pkl', 'wb') as file:
        pickle.dump(data, file)
    return (f"model saved")

def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    le_education = label_encoder(df)[0]
    le_country = label_encoder(df)[1]

    df_encoded = df.copy()

    df_encoded['EdLevel'] = le_education.transform(df_encoded['EdLevel'])
    df_encoded['Country'] = le_country.transform(df_encoded['Country'])

    train_data()

    save_model()

    data = load_model()

    regressor_loaded = data["model"]
    le_country = data["le_country"]
    le_education = data["le_education"]

    X = np.array([['United States of America', 'Master’s degree', 15]])
    X[:, 0] = le_country.transform(X[:,0])
    X[:, 1] = le_education.transform(X[:,1])
    X = X.astype(float)
    y_pred = regressor_loaded.predict(X)
    print(y_pred)
