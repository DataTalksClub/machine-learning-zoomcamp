import pickle

def load_dv_model():
    with open('dv.bin', 'rb') as dv_in:
        dv = pickle.load(dv_in)
    with open('model1.bin', 'rb') as model_in:
        model = pickle.load(model_in)
    return dv, model

def predict_single(customer, dv, model):
  X = dv.transform([customer])
  y_pred = model.predict_proba(X)[:, 1]
  return y_pred[0]

if __name__ == '__main__':
    customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}
    dv, model = load_dv_model()
    print(predict_single(customer, dv, model))