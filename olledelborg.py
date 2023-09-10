import streamlit as st
from PIL import Image
import time

#with open( "style.css" ) as css:
#        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

me = Image.open('avatar.png')

# -------- LINKS ---------
THESIS_STRING = "https://urn.kb.se/resolve?urn=urn:nbn:se:uu:diva-505219"
LINKED_STRING = "https://se.linkedin.com/in/olle-nilsson-delborg-810211228"


with st.sidebar:
    st.image(me, width = 300)
    st.markdown("<h2 style='font-weight:bold;'>Data Science. Data Engineering. Embedded Systems.  </h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight:bold;'>These are some of my expertieses and domains I am working with.  </h3>", unsafe_allow_html=True)
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
         

st.markdown("<h1 style='text-align: center; color: #091747; font-family: Playfair Display, serif; font-weight: normal;'>Olle Delborg</h1>", unsafe_allow_html=True)

#st.title('Olle Delborg')

tab1, tab2, tab3 = st.tabs(["About Me", "Work", "Skills"])

with tab1:
    st.markdown("**Hello! I am a Data Scientist Engineer currently working with embedded systems and routing optimization on the pre-development section at Scania.**")
    st.markdown("I am passionate about sustainability, electrification and *everything* data.")

with tab2:
    c = st.container()
    with c:
            #col11, col12 = st.columns([4,3])
            #with col11
        st.write("Checkout some of my work so far below!")
            #with col12:
            #    st.image(me, width = 300)
        with st.expander("Master Thesis @Scania"):
            st.markdown("During the spring of 2023 I had the pleasure to work on my Master Thesis at Scania. As the extremely simple name *'Route Planning of Battery Electric Heavy-Duty Commercial Vehicles - Using Contraction Hierarchies and Mixed Integer Programming'*, the work regarded efficient routing of electric trucks. ")
        with st.expander("Fullstack Developer @Energigemenskaper"):
            st.write("TODO")
        with st.expander("More"):
            st.write("TODO")
with tab3:
    st.write("TODO")