import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="MitraPohamba Community",page_icon=":tada:",layout="wide")
#--buat sidebar--#
with st.sidebar:
  selected = option_menu( 
    menu_title="Menu Utama", #required
    options=["Navigasi", "Layanan","Kontak"], # required
    icons=["house","book","envelope"],# optional
    menu_icon="cast", # optional
    default_index=0, # optional
    )   
  

if selected =="Navigasi":
  st.title(f"kamu memilih{selected}")
if selected =="Layanan":
    st.title(f"kamu memilih{selected}")
if selected =="Kontak":
   st.title(f"kamu memilih {selected}")
   

#-----header-----#

st.subheader("hi, welcome to MitraPohamba Community :tada:")
st.title("MitraPohamba Community")
st.write("MitraPohamba Community adalah sebuah komunitas yang bergerak di bidang pendidikan dan beberapa layanan lainnya.")
st.write("[learn more >](https://www.djangoproject.com/start/)")