class IrisValidator:
    @staticmethod
    def validate(data):
        required_fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        for field in required_fields:
            if field not in data:
                return False
            if not isinstance(data[field], (int, float)):
                return False
        return True
