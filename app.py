from flask import Flask, render_template, request
from src.pipeline.predict import PredictPipe,CustomData
application = Flask(__name__)
app = application

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/predictdata',methods = ['GET','POST'])
def prediction():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        custom_data= CustomData(
            gender=request.form.get("gender"),
            SeniorCitizen=int(request.form.get("SeniorCitizen")),
            Partner=request.form.get("Partner"),
            Dependents=request.form.get("Dependents"),
            tenure=int(request.form.get("tenure")),
            PhoneService=request.form.get("PhoneService"),
            MultipleLines=request.form.get("MultipleLines"),
            InternetService=request.form.get("InternetService"),
            OnlineSecurity=request.form.get("OnlineSecurity"),
            OnlineBackup=request.form.get("OnlineBackup"),
            DeviceProtection=request.form.get("DeviceProtection"),
            TechSupport=request.form.get("TechSupport"),
            StreamingTV=request.form.get("StreamingTV"),
            StreamingMovies=request.form.get("StreamingMovies"),
            Contract=request.form.get("Contract"),
            PaperlessBilling=request.form.get("PaperlessBilling"),
            PaymentMethod=request.form.get("PaymentMethod"),
            MonthlyCharges=float(request.form.get("MonthlyCharges")),
            TotalCharges=float(request.form.get("TotalCharges"))
        )
        custom_data_as_df = custom_data.get_data_as_df()
        model = PredictPipe()

        result = model.predict(custom_data_as_df)
        return render_template('form.html',result = result[0])


if __name__ =="__main__":
    app.run(debug=True)