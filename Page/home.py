import streamlit as st

from tensorflow.keras.models import load_model
import numpy as np
import pickle as pkl


with open('Notebook/pickle_encoder/gender_encoder.pickle' , 'rb') as file:
    gender_encoder = pkl.load(file )
with open('Notebook/pickle_encoder/institute_encoder.pickle' , 'rb') as file:
    institute_encoder = pkl.load(file )
with open('Notebook/pickle_encoder/program_encoder.pickle' , 'rb') as file:
    program_encoder = pkl.load(file )
with open('Notebook/pickle_encoder/pwd_encoder.pickle' , 'rb') as file:
    pwd_encoder = pkl.load(file )
with open('Notebook/pickle_encoder/seat_encoder.pickle' , 'rb') as file:
    seat_encoder = pkl.load(file )
with open('Notebook/pickle_scaler/X_scaler.pickle' , 'rb') as file:
    X_scaler = pkl.load(file )
with open('Notebook/pickle_scaler/y_scaler.pickle' , 'rb') as file:
    y_scaler = pkl.load(file )
def app():
    st.title('Home')

    institute = st.selectbox('Select institute : ' , institute_encoder.classes_ , key="input1")
    quota = st.selectbox("Select Quota :" , ["AI"] , key="input2" )
    gender = st.selectbox('Select Gender : ' , gender_encoder.classes_ , key="input3" )
    year = st.number_input("Enter Year :" , min_value=2016 , max_value=2026 , key="input4")
    program = st.selectbox('Select Program : ' , program_encoder.classes_ , key="input5")
    seat = st.selectbox('Select Seat : ', seat_encoder.classes_ , key="input6")
    pwd = st.selectbox('Select PWD :', pwd_encoder.classes_ , key="input7")
    if st.button('Predict Rank' , key="button1"):
        try :
            institute = institute_encoder.transform([institute])
            quota = 0
            gender = gender_encoder.transform([gender])
            program = program_encoder.transform([program])
            seat = seat_encoder.transform([seat])
            pwd = pwd_encoder.transform([pwd])

            input = np.array([institute[0] , quota , gender[0] , year , program[0] , seat[0] , pwd[0]])

            input = X_scaler.transform([input])

            model = load_model('Notebook/model/ann_model.keras')
            output = model.predict(input)
            output = y_scaler.inverse_transform(output)
            st.success("Opening Rank is " + str(output[0][0]) , key="output1")
            st.success("Closing Rank is " + str(output[0][1]) , key="output1")
        except Exception as e:
            st.warning(e , key="warning1")
