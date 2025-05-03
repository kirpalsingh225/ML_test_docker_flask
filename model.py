from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

x, y = load_iris(return_X_y=True)

rf = RandomForestClassifier()

rf.fit(x, y)

with open("model.pkl", "wb") as model_file:
    pickle.dump(rf, model_file)