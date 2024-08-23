import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from fetch import *
import games


with st.sidebar:
    selected = option_menu(
        menu_title="Nav Bar",
        options=["Games"],
        icons=["cast"],
        menu_icon="caret-right-square-fill",
        default_index=0
    )

def call_game():
    games.games_list(date.year, date.month, date.day)

if selected == "Games":
    st.title(f"Pick a Date for {selected}")
    date = st.date_input("📅 Enter a date: ")
    call_game()