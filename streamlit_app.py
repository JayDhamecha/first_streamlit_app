import streamlit

streamlit.title('This is Jay Dhamecha.')
streamlit.header('I am here to help you in every manner which can i do!!')
streamlit.text('Lets Resolve your error for better output')
streamlit.title('Figurative Analytics Pvt Ltd an Ahmedabad based Analytical company with global rating')

streamlit.header('Hey!!')
streamlit.text('How are you?')
streamlit.title('We are welcoming you!!')


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Tea/Coffee')
streamlit.text('🥗 Bread with butter and Avocado')
streamlit.text('🥑 Avocado with bread and butter')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruit_selected = streamlit.multiselect("Please choose fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruit_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
