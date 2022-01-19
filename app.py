from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('classifier.pkl','rb'))
#classifier=pickle.load(model)

@app.route('/')
def hello_world():
    return render_template("page.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)

    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    #output = round(prediction[0], 2)


    return render_template('page.html', predicted_text='currency is {}'.format(prediction))


if __name__ == '__main__':
    #app.run(host='127.0.0.1',port=7071)
    #app.run(debug=True)
    app.run(host ='0.0.0.0', port = 5001, debug = True)