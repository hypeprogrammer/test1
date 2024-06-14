from flask import Blueprint, request, jsonify, render_template
from app.services.iris_service import IrisService
from app.validators.iris_validator import IrisValidator

iris_bp = Blueprint('iris', __name__)

@iris_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not IrisValidator.validate(data):
        return jsonify({'error': 'Invalid input'}), 400

    prediction = IrisService.predict(data)
    return jsonify({'prediction': prediction})
