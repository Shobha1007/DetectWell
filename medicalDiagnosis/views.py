from django.shortcuts import render
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

from joblib import load

model = load('./Models and Data/heart_model')
dmodel = load('./Models and Data/diabetes_model')
pmodel = load('./Models and Data/parkinson_model')

# Create your views here.

def base(request):
    return render( request, 'index.html')


def heartdis(request):
    if request.method == 'POST':

        age = float(request.POST['age'])
        sex = float(request.POST['sex'])
        cp = float(request.POST['cp'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])
        fbs = float(request.POST['fbs'])
        restecg = float(request.POST['restecg'])
        thalach = float(request.POST['thalach'])
        exang = float(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = float(request.POST['slope'])
        ca = float(request.POST['ca'])
        thal = float(request.POST['thal'])

        inp = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

        inp_data_asarr = np.asarray(inp)
        inp_reshaped = inp_data_asarr.reshape(1,-1)
        prediction = model.predict(inp_reshaped)

        if(prediction ==0):
            res = "Does not have heart disease"
        else:
            res = "Person has heart disease."



        return render(request,'heartdis2.html',{'result': res})
    

    else:
        return render(request,'heartdis2.html')


def diabetes(request):
    if request.method == 'POST':

        age = int(request.POST['age'])
        Pregnancies = int(request.POST['Pregnancies'])
        Glucose = int(request.POST['Glucose'])
        BloodPressure = int(request.POST['BloodPressure'])
        SkinThickness = int(request.POST['SkinThickness'])
        Insulin = int(request.POST['Insulin'])
        BMI = float(request.POST['BMI'])
        DiabetesPedigreeFunction = float(request.POST['DiabetesPedigreeFunction'])
        

        inp = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,age]


        # input_data = (3,171,72,33,135,33.3,0.199,24 )
        inp_data = np.asarray(inp)
        inp_reshaped_data = inp_data.reshape(1,-1)
        scaler = StandardScaler()
        
        std_inp_data = scaler.fit_transform( inp_reshaped_data )
        print(std_inp_data)

        prediction = dmodel.predict(std_inp_data)


        if(prediction[0] ==0):
            res = "Non Diabetic"
        else:
            res = "Diabetic"



        return render(request,'diabetes2.html',{'result': res})
    

    else:
        return render(request,'diabetes2.html')
    

def parkinsons(request):
    
        if request.method == 'POST':

            
            
            Fo = float(request.POST['Fo'])
            Fhi = float(request.POST['Fhi'])
            Flo = float(request.POST['Flo'])
            Jitter_perc = float(request.POST['Jitter_perc'])
            Jitter = float(request.POST['Jitter'])
            RAP = float(request.POST['RAP'])
            PPQ = float(request.POST['PPQ'])
            DDP = float(request.POST['DDP'])
            Shimmer = float(request.POST['Shimmer'])
            Shimmerdb = float(request.POST['Shimmerdb'])
            APQ3 = float(request.POST['APQ3'])
            APQ5 = float(request.POST['APQ5'])
            APQ = float(request.POST['APQ'])
            DDA = float(request.POST['DDA'])
            NHR = float(request.POST['NHR'])
            HNR = float(request.POST['HNR'])
            RPDE = float(request.POST['RPDE'])
            DFA = float(request.POST['DFA'])
            spread1 = float(request.POST['spread1'])
            spread2 = float(request.POST['spread2'])
            D2 = float(request.POST['D2'])
            PPE = float(request.POST['PPE'])

            

            inp = [Fo,Fhi,Flo,Jitter_perc,Jitter,RAP,PPQ,DDP,Shimmer,Shimmerdb,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]


            # input_data = (3,171,72,33,135,33.3,0.199,24 )
            inp_data = np.asarray(inp)
            inp_reshaped_data = inp_data.reshape(1,-1)
            scaler = StandardScaler()
            
            std_inp_data = scaler.fit_transform( inp_reshaped_data )
            print(std_inp_data)

            prediction = pmodel.predict(std_inp_data)


            if(prediction[0] ==0):
                res = "No disease detected"
            else:
                res = "Parkinson disease is detected "



            return render(request,'parkinsons2.html',{'result': res})
        

        else:
            return render(request,'parkinsons2.html')

        