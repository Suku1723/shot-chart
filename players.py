from fetch import Players
import streamlit as st
import shotchart


def player_list(id):
    players = Players(id).game_data()
    selected_player = st.sidebar.selectbox('Available Player Shot Charts', players)
    

    if selected_player is not None:
        o = Players(id).Made[selected_player]
        x = Players(id).Missed[selected_player]
        x_made = [i[0] for i in o]
        y_made = [i[1] for i in o]

        x_missed = [i[0] for i in x]
        y_missed = [i[1] for i in x]
        print(x_made, y_made)
        shotchart.shot_chart(x_made, y_made, x_missed, y_missed, selected_player)
