# chat_message
import numpy as np
import streamlit as st

with st.chat_message("assistant"):
    st.write("Hello human")
    st.bar_chart(np.random.randn(30, 3))