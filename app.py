# pip install -U streamlit
# pip install -U plotly

# you can run your app with: streamlit run app.py

import streamlit as st
import pickle

# loading the trained model
model = pickle.load(open('model.pkl', 'rb'))

# create title
st.title('Predicting if message is spam or not')

message = st.text_input('Enter a message')

submit = st.button('Predict')

if submit:
    prediction = model.predict([message])

    # print(prediction)
    # st.write(prediction)
    
    if prediction[0] == 'spam':
        st.warning('This message is spam')
    else:
        st.success('This message is Legit (HAM)')


st.balloons()