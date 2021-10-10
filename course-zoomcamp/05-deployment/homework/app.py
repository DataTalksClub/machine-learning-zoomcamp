from flask import Flask, request, jsonify
from predict import predict_single, load_dv_model

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    dv, model = load_dv_model()
    prediction = predict_single(customer, dv, model)
    
    churn = prediction >= 0.5
    
    result = {
        'churn_probability': float(prediction),
        'churn': bool(churn),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)