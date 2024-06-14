document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const data = {
        sepal_length: parseFloat(document.getElementById('sepal_length').value),
        sepal_width: parseFloat(document.getElementById('sepal_width').value),
        petal_length: parseFloat(document.getElementById('petal_length').value),
        petal_width: parseFloat(document.getElementById('petal_width').value)
    };

    fetch('/api/v1/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.error) {
            resultDiv.textContent = 'Error: ' + data.error;
        } else {
            resultDiv.textContent = 'Prediction: ' + data.prediction;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
