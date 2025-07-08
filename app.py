import streamlit as st
from streamlit.components.v1 import html

st.write("Hello world")
st.json({
    'text' : 'Hello world'
})
html(
    "<h1 style=\"color: aqua\">My custom component!</h1>"
)
