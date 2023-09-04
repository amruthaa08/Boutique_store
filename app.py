import streamlit as st
import utils

st.title("Boutique Name Generator")

origin = st.sidebar.selectbox("Pick an origin", ("Indian", "Arabic", "Japanese", "American", "Korean"))

if origin:
    response = utils.generate_boutique_name_items(origin)
    st.header(response["boutique_name"].strip())

    dress_items = response["dress_items"].strip().split(",")
    st.write("**Dress Items**")
    for item in dress_items:
        st.write("-", item)