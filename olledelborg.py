import streamlit as st
from PIL import Image
import time
from streamlit_timeline import timeline



#--------- IMAGES --------
me = Image.open('Images/avatar.png')
ch = Image.open('Images/contraction.jpg')
vm = Image.open('Images/vehicle-model.jpg')
eg = Image.open('Images/eg.jpg')

# -------- LINKS ---------
THESIS_STRING = "https://urn.kb.se/resolve?urn=urn:nbn:se:uu:diva-505219"
LINKED_STRING = "https://se.linkedin.com/in/olle-nilsson-delborg-810211228"
EG_STRING = "https://energigemenskaper.se"


with st.sidebar:
    st.image(me, width = 300)
    st.markdown("<h2 style='font-weight:bold;'>Data Science. Data Engineering. Embedded Systems.  </h2>", unsafe_allow_html=True)
    #st.markdown("<h3 style='font-weight:bold;'>These are some of my expertieses and domains I am working with.  </h3>", unsafe_allow_html=True)
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
    st.markdown("**Hello! :wave:  I am a Data Scientist currently working with routing optimization and embedded systems for electric trucks at the pre-development section of Scania.**")
    st.markdown("I am passionate about sustainability, electrification and *everything* data. Please go ahead and scroll through my journey so far below. ")
    with open('example.json', "r") as f:
        data = f.read()
    timeline = timeline(data)


with tab2:
    c = st.container()
    with c:
            #col11, col12 = st.columns([4,3])
            #with col11
        st.write("**Checkout some of my work so far below**")
            #with col12:
            #    st.image(me, width = 300)
        with st.expander("Master Thesis @Scania"):
            st.markdown("During the spring of 2023 I had the pleasure to work on my Master Thesis at Scania. As the extremely simple name **Route Planning of Battery Electric Heavy-Duty Commercial Vehicles - Using Contraction Hierarchies and Mixed Integer Programming**, the work regarded efficient routing of electric trucks. ")
            st.markdown("The report describes a solution that utilizes Contraction Hierarchies and a physical model of Electric Trucks in order to proces map data. The processed data is then used as an input to an optimization model that finds the optimal order to visit a set of customers and chargers.")
            st.markdown("Working on this thesis was incredibly rewarding and insightful. Please checkout some of the images from the report below :point_down:")
            st.image(vm)
            st.image(ch)
        with st.expander("Fullstack Developer @Energigemenskaper"):
            st.markdown("After working on my bachelor thesis for STUNS, I was hired to develop the web service **Energigemenskaper**. The service aims to provide knowlede about the limitations in the current power grid and shed light on a possible solution; *Energy Communities*.")
            st.markdown("The work was in part funded by the EU :rocket:, with the aim to invest in innovative energy solutions.")
            link = st.markdown(
                f'<a href="{EG_STRING}">Checkout Energigemenskaper!</a>',
                unsafe_allow_html=True)
            st.image(eg)
        with st.expander("Other"):
            st.write("During my studies I worked as a teachers assistant for a couple of programming courses!")
            st.markdown("The work as a TA as well as being a Scrum Master at Scania, has helped med developing skills in leadership.")
with tab3:
    st.markdown("**During my studies and work I have been forunate to learn and work with a wide set of programming languages, tools and frameworks.**")
    st.markdown("As a Data Scientist I'm very comfortable working with Matlab, **Python** and Python libraries such as **pandas**, **TensorFlow**, **Keras** and **numpy**. Further, using the cloud platform **OpenStack** I have developed skills using frameworks such as **Docker**, **Kubernetes**, Apache **Spark** and **Kafka** as well as working with **micro services**, and for automation and orchestration **Ansible** and **Docker Swarm**, to name a few.")
    st.markdown("Working at Energigemenskaper I got to learn how to use **Docker** to configure and host a website on a server, as well as refining my skills in backend and frontend development.")
    st.markdown("In my current line work I am continuing to hone my skills in writing efficient **C**, **C++**, **Matlab** and **Simulink** code for embedded systems. I am also continuing developing skills in effective data pipelines and mathemathical optimization!")
    st.markdown("Lastly, I am used to work in **agile environments** from both my work and studies, and I am currently taking courses in being a **Scrum Master** for one of the projects I am involved with.")