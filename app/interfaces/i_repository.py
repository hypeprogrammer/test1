from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def predict(self, features):
        pass
