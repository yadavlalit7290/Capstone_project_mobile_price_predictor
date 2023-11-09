import streamlit as st
import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import  plotly.graph_objects as go
import altair as alt


st.set_page_config(layout='wide')

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

full = pd.read_csv("Fully_Cleaned_data.csv")

def predictor():
    
    st.title('Smart Phone Price Prdictor')

    col1,col2,col3 = st.columns(3)

    with col1:


        os = st.selectbox('Select Operating System',sorted(df['os'].unique()))
        dual_display = st.selectbox('Dual Display ?',['Yes','No'])
        has_5g = st.selectbox('Is it 5g ?',['Yes','No'])
        has_nfc = st.selectbox('Does it have NFC ?',['Yes','No'])
        has_ir_blaster = st.selectbox('Does it have IR Blaster ?',['Yes','No'])

        processor___ = list(df['processor_brand'].unique())
        processor___.remove('missing')
        
        processor_brand = st.selectbox('Select Processor',sorted(processor___))
        num_core = st.number_input(f'How much number of Cores ? Expected value between {df["num_core"].min()} and {df["num_core"].max()}',min_value=0)
        
        
        processor_speed_GHz = st.number_input('How much Processor speed in GHz',min_value=0.0)
        

    with col2:
        ram_capacity = st.selectbox(f'How much Ram in GB ? ',[1,2,4,6,8,12,16,18,24])
        
        
        internal_memory = st.selectbox(f'How much Internal memory in GB ? ',[16,32,64,128,256,512,1048,2096])
        
        
        battery_capacity_mAh = st.number_input(f'How much Battery in mAh ? Expected value between {df["battery_capacity_mAh"].min()} and {df["battery_capacity_mAh"].max()}',min_value=0)
        
        
        fast_charging_available = st.selectbox('Fast charging ?',['Yes','No'])
        
        fast_charging = st.number_input(f'How much watt fast charger ? Expected value between {df["fast_charging"].min()} and {df["fast_charging"].max()}',min_value=0)
        
        screen_size_inches = st.number_input(f'What is the screen size in inches ?  Expected value between {df["screen_size_inches"].min()} and {df["screen_size_inches"].max()}',min_value=0.0)
        
        
        refresh_rate = st.number_input(f'How much Refresh Rate in Hz ? Expected value between {df["refresh_rate"].min()} and {df["refresh_rate"].max()}',min_value=0)
        
    
    with col3:
        num_rear_cameras = st.number_input(f'How many rear camera  ? Expected value between {df["num_rear_cameras"].min()} and {df["num_rear_cameras"].max()}',min_value=0)
        
        
        num_front_cameras = st.number_input(f'How many front camera ? Expected value between {df["num_front_cameras"].min()} and {df["num_front_cameras"].max()}',min_value=0)
        
        
        primary_camera_rear = st.number_input(f'How much pixel is primary rear camera ? Expected value between {df["primary_camera_rear"].min()} and {df["primary_camera_rear"].max()}',min_value=0)
        
        
        primary_camera_front = st.number_input(f'How much pixel is primary front camera ? Expected value between {df["primary_camera_front"].min()} and {df["primary_camera_front"].max()}',min_value=0)
        
        
        brand_name = st.selectbox('Select brand of smartphone',sorted(df['brand_name'].unique()))
        resolution = st.selectbox('Select the resolution',sorted(full['resolution'].unique()))
        resolution = str(resolution)

# Split the resolution string and convert width and height to integers
    resolution_parts = resolution.split('x')
    resolution_width = int(resolution_parts[0])
    resolution_height = int(resolution_parts[1])


    predict = st.button('Predict')
    if predict:
        if (num_core < df['num_core'].min()) or (num_core > df['num_core'].max()):
            st.error(f"Unexpected ! Number of cores")


        if (primary_camera_front < df['primary_camera_front'].min()) or (primary_camera_front > df['primary_camera_front'].max()):
            st.error(f"Unexpected ! Primary front camera")

        if (processor_speed_GHz < df['processor_speed_GHz'].min()) or (processor_speed_GHz > df['processor_speed_GHz'].max()):
              st.error(f"Unexpected ! Processor speed")


        if (ram_capacity < df['ram_capacity'].min()) or (ram_capacity > df['ram_capacity'].max()):
            st.error(f"Unexpected ! Ram")

        if (internal_memory < df['internal_memory'].min()) or (internal_memory > df['internal_memory'].max()):
            st.error(f"Unexpected ! Internal Memory")

        if (fast_charging < df['fast_charging'].min()) or (fast_charging > df['fast_charging'].max()):
            st.error(f"Unexpected ! Fast charger")


        if (screen_size_inches < df['screen_size_inches'].min()) or (screen_size_inches > df['screen_size_inches'].max()):
            st.error(f"Unexpected ! Screen Size")


        if (refresh_rate < df['refresh_rate'].min()) or (refresh_rate > df['refresh_rate'].max()):
            st.error(f"Unexpected ! Refresh Rate")


        if (battery_capacity_mAh < df['battery_capacity_mAh'].min()) or (battery_capacity_mAh > df['battery_capacity_mAh'].max()):
            st.error(f"Unexpected ! Battery Capacity")

        if (num_rear_cameras < df['num_rear_cameras'].min()) or (num_rear_cameras > df['num_rear_cameras'].max()):
            st.error(f"Unexpected ! Number of Rear Cameras")

        if (num_front_cameras < df['num_front_cameras'].min()) or (num_front_cameras > df['num_rear_cameras'].max()):
            st.error(f"Unexpected ! Number of front cameras")


        if (primary_camera_rear < df['primary_camera_rear'].min()) or (primary_camera_rear > df['primary_camera_rear'].max()):
            st.error(f"Unexpected ! Primary rear Camera")





        dual_display_dict = {'Yes':1,'No':0}
        has_5g_dict = {'Yes':1,'No':0}
        has_nfc_dict = {'Yes':1,'No':0}
        fast_charging_available_dict = {'Yes':1,'No':0}
        has_ir_blaster_dict =  {'Yes':1,'No':0}

        

        result = pipe.predict([[os,dual_display_dict[dual_display],has_5g_dict[has_5g],has_nfc_dict[has_nfc],has_ir_blaster_dict[has_ir_blaster],processor_brand,num_core,processor_speed_GHz,ram_capacity,internal_memory,battery_capacity_mAh,fast_charging_available_dict[fast_charging_available],fast_charging,screen_size_inches,refresh_rate,num_rear_cameras,num_front_cameras,primary_camera_rear,primary_camera_front,brand_name,resolution_width,resolution_height]])

        rounded_result_str = str(np.round(np.expm1(result)[0], 2))

        # Display the rounded result using st.write
        st.header(f'The Expected price is ₹{rounded_result_str}')
        st.subheader(f'Price should be between ₹{str(np.round(float(rounded_result_str) - 5893, 2))} and ₹{str(np.round(float(rounded_result_str) + 5893, 2))}')



def Data_Dashboard():

    st.title('Information of data on which model is trained')
    col1 , col2 = st.columns(2)

    with col1:
        
        fig = go.Figure(
        go.Pie(
        labels = df['brand_name'].value_counts().index,
        values = df['brand_name'].value_counts().values,
        hoverinfo = "label+percent",
        textinfo = "value"))

        st.subheader("Pie chart for Mobile brand with number of mobiles in this data")
        st.plotly_chart(fig)

        st.write('*******************************************************')

        fig = go.Figure(
        go.Pie(
        labels = df['processor_brand'].value_counts().index,
        values = df['processor_brand'].value_counts().values,
        hoverinfo = "label+percent",
        textinfo = "value"))

        st.subheader("Pie chart for processor brand with number of mobiles in this data")
        st.plotly_chart(fig)

        st.write('*******************************************************')
        
        fig = go.Figure(
        go.Pie(
        labels = df['ram_capacity'].value_counts().index,
        values = df['ram_capacity'].value_counts().values,
        hoverinfo = "label+percent",
        textinfo = "value"))

        st.subheader("Pie chart for Ram with number of mobiles in this data")
        st.plotly_chart(fig)
        
    with col2:

        st.subheader("Bar chart for Mobile brand name with Price")
        fig = px.bar(        
        df,
        x = df['brand_name'],
        y = df['price'],
        title = "Bar Graph",
        color=df['brand_name'])
        st.plotly_chart(fig)

        
        st.write('')
        st.write('')
        st.write('*******************************************************')
        
        st.subheader("Bar chart for processor brand  with Price")
        fig = px.bar(        
        df,
        x = df['processor_brand'],
        y = df['price'],
        title = "Bar Graph",
        color=df['brand_name'])
        st.plotly_chart(fig)

        st.write('')
        st.write('')
        st.write('*******************************************************')

        fig = go.Figure(
        go.Pie(
        labels = df['internal_memory'].value_counts().index,
        values = df['internal_memory'].value_counts().values,
        hoverinfo = "label+percent",
        textinfo = "value"))

        st.subheader("Pie chart for Internal Memory with number of mobiles in this data")
        st.plotly_chart(fig)


    st.dataframe(df)  



def about_project():
    st.title('About Project')

    st.subheader("Summary of my Machine Learning End to End project")

    st.write("""I built a Machine Learning End to End project to predict the price of mobile phones. I collected data from the smartprix website and scraped it to create a dataframe. I cleaned the data and filled in missing values using KNN imputer. I assumed that if a fast charger was available, it would be a 15W fast charger.

I used the VotingRegressor ensemble technique to combine the predictions of multiple regression models to improve accuracy. I used the RandomForestRegressor, Ridge, ExtraTreeRegressor, and GradientBoostingRegressor models.

My model achieved an R2 score of 0.90 and a mean absolute error (MAE) of 5893. I tried to create a column for pixel per inch, but the R2 score remained at 0.90, so I didn't include it in the model because it didn't improve the accuracy.

I deployed my model to a Streamlit website, where users can enter the specifications of a mobile phone and receive a predicted price. A data dashboard page also present that shows information about the data used to train the model. The website also displays the predicted price plus and minus the MAE.""")


    st.subheader("About me")
    st.write("""I am Lalit Yadav. I am B.com(Hons) Graduate (2020-2023). I made this capstone project. """)
    url_ = "https://github.com/yadavlalit7290?tab=repositories"
    st.write("check out this for my [Github](%s)" % url_)
    url_l = "https://www.linkedin.com/in/lalit-yad7290"
    st.markdown("check out this for my [Linkedin](%s)" % url_l)
    



st.sidebar.title('Select one option')

option = st.sidebar.selectbox('',['Mobile Price Predictor','Data Dashboard','About Project'])

if option == 'Mobile Price Predictor':
    predictor()
elif option == 'Data Dashboard':
    Data_Dashboard()
elif option == 'About Project':
    about_project()




