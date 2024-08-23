from fetch import DailyGames
import streamlit as st
from streamlit_option_menu import option_menu
import players

def games_list(year, month, day):
    dg = DailyGames(year, month, day).get_games()
    selected_game = st.sidebar.selectbox('Games', [game for game in dg])
    if selected_game is not None:
        players.player_list(dg[selected_game])