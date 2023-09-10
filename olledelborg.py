import streamlit as st
from PIL import Image
import time

with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

me = Image.open('avatar.png')

# -------- LINKS ---------
THESIS_STRING = "https://urn.kb.se/resolve?urn=urn:nbn:se:uu:diva-505219"
LINKED_STRING = "https://se.linkedin.com/in/olle-nilsson-delborg-810211228"


with st.sidebar:
    st.image(me, width = 300)
    st.markdown("<h1 style='font-weight:bold;'>Welcome! I am a Data Scientist Engineer, graduated from Uppsala University in the summer of 2023. Currently working as a Development Engineer @Scania. </h1>", unsafe_allow_html=True)
    sidebar_col_1, sidebar_col_2 = st.columns([1,1])
    with sidebar_col_1:
         #st.image(linked,width=50)
         st.markdown(
                f'<a href="{LINKED_STRING}" style="display: inline-block; padding: 12px 20px; background-color: #091747; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px; font-family: Trebuchet MS, sans-serif;">LinkedIn</a>',
                unsafe_allow_html=True)
    with sidebar_col_2:
         st.markdown(
                f'<a href="{THESIS_STRING}" style="display: inline-block; padding: 12px 20px; background-color: #091747; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px; font-family: Trebuchet MS, sans-serif;">Master Thesis</a>',
                unsafe_allow_html=True)
         

st.markdown("<h1 style='text-align: center; color: #091747;'>Olle Delborg</h1>", unsafe_allow_html=True)

#st.title('Olle Delborg')

#tab1, tab2 = st.tabs(["About Me", "Work"])
#with tab1:
c = st.container()
with c:
        #col11, col12 = st.columns([4,3])
        #with col11:
    st.write("Currently working with embedded systems and routing optimization at Scania. The work is in part an extension of my master thesis, which you can checkout in the sidebar!")
        #with col12:
        #    st.image(me, width = 300)
#with tab2:
#     st.write("TODO")