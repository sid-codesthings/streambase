import streamlit as st
import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate("key_st_fb.json")
if not firebase_admin._apps:
    app = firebase_admin.initialize_app(cred,{'databaseURL':'https://streambase-5d9e4-default-rtdb.firebaseio.com/'})
from firebase_admin import db
st.set_page_config(page_title='Streamlit&FB',page_icon='shark')
mymenu = st.sidebar.selectbox('My Menu',('Home','Input Data'))
st.title('Data from streamlit into firebase')

if(mymenu=='Home'):
    st.markdown('<h1>Welcome</h1>',unsafe_allow_html=True)
    st.image('https://groups.google.com/group/firebase-talk/attach/22f22cb2df0ca/Streamlit--Firestore-1.png?part=0.1&view=1')
    st.text('Go to the Input Data Section in the menu beside for entering data into the Firebase.')
elif(mymenu=='Input Data'):
    with st.form('Enter Data'):
        emp_id = st.text_input('Enter ID')
        name = st.text_input('Enter Name')
        city = st.text_input('Enter City')
        locality = st.text_input('Enter locality') # Slider for sliding and chosing marks
        k = st.form_submit_button("Submit Form")
        #d = {"Name":name,"City":city,"Locality":locality}
        #m = "/" + emp_id
        #ref = db.reference(m)
        #ref.update(d)
        if k:
            st.write('Name:',name,'City:',city,'Loacality:',locality)
            d = {"Name":name,"City":city,"Locality":locality}
            m = "/" + emp_id
            ref = db.reference(m)
            ref.update(d)
            
            
