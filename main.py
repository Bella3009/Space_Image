import streamlit as st
import requests

# Setting up the API
API_KEY = "5uRZ1IrSjEGpLOWd6CTaAtYEiJaV66IkaLKNrPsQ"
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

# Retrieve the data
response = requests.get(url)
data = response.json()

pic_title = data["title"]
image_url = data["url"]
pic_explanation = data["explanation"]

# Download the image
img_path = "PicOfTheDay.png"
image_response = requests.get(image_url)
with open(img_path, "wb") as file:
    file.write(image_response.content)

# Setting up the website
st.title(pic_title)
st.image(img_path)
st.info(pic_explanation)
