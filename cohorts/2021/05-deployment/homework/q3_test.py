import pickle

def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv = load('dv.bin')
model = load('model1.bin')

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]

print(y_pred)