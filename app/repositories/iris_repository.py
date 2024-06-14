from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from app.interfaces.i_repository import IRepository


class IrisRepository(IRepository):
    def __init__(self):
        self.model = self._train_model()

    def _train_model(self):
        iris = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(
            iris.data, iris.target, test_size=0.2, random_state=42)
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        return model

    def predict(self, features):
        return self.model.predict([features])[0]
