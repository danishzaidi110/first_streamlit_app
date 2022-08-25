import streamlit 
import pandas 


streamlit.title("  My Parents new health Diner")
streamlit.header("   Breakfast Menu")
streamlit.text(" 🥣  Omega 3 & Bluberry Oatmeal")
streamlit.text("🥗 Kale,Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some Fruits: ", list(my_fruit_list.index),['Avocado','Strawberries'])
Fruit_to_show = my_fruit_list.loc[fruits_selected] 

streamlit.dataframe(Fruit_to_show)

streamlit.header('Fruity Vice Fruit advise!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','cherry')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
# Normalizes the json format of data into a table  
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# the dataframe infers the schema of fruityvice_response and loads the data accordingly 
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
