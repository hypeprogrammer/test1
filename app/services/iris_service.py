from app.interfaces.i_repository import IRepository
from app.repositories.iris_repository import IrisRepository

class IrisService:
    _repository: IRepository = IrisRepository()

    @classmethod
    def predict(cls, data):
        features = [
            data['sepal_length'],
            data['sepal_width'],
            data['petal_length'],
            data['petal_width']
        ]
        return cls._repository.predict(features)
