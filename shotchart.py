import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
import streamlit as st

"""
Drawing the court and then scattering
the individual coordinates
"""

def shot_chart(x_made, y_made, x_missed, y_missed, selected_player):
    hoop = Circle((300, 58), radius=9, linewidth=1, color="blue", fill=False)
    backboard = Rectangle((264, 46), 72, 0, linewidth=2, color="blue")
    # The paint
    # outer box
    outer_box = Rectangle((204, 0), 192, 228, linewidth=2, color="blue", fill=False)
    # inner box
    inner_box = Rectangle((228, 0), 144, 228, linewidth=2, color="blue", fill=False)
    top_free_throw = Arc((300, 228), 144, 144, theta1=0, theta2=180, linewidth=2, color="blue", fill=False)
    bottom_free_throw = Arc((300, 228), 144, 144, theta1=180, theta2=0, linewidth=2, color="blue")
    restricted = Arc((300, 46), 96, 108, theta1=0, theta2=180, linewidth=2, color="blue")

    # Three Point Line
    corner_three_a = Rectangle((36, 0), 0, 168, linewidth=2, color="blue")
    corner_three_b = Rectangle((564, 0), 0, 168, linewidth=2, color="blue")
    three_arc = Arc((300, 168), 528, 380, theta1=0, theta2=180, linewidth=2, color="blue")

    plt.xlim(0, 600)
    plt.ylim(0, 564)
    plt.gca().add_patch(hoop)
    plt.gca().add_patch(backboard)
    plt.gca().add_patch(inner_box)
    plt.gca().add_patch(outer_box)
    plt.gca().add_patch(top_free_throw)
    plt.gca().add_patch(bottom_free_throw)
    plt.gca().add_patch(restricted)
    plt.gca().add_patch(corner_three_a)
    plt.gca().add_patch(corner_three_b)
    plt.gca().add_patch(three_arc)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.title(f"{selected_player}")
    plt.scatter(x_made, y_made, edgecolors='g', marker='o', facecolors='none')
    plt.scatter(x_missed, y_missed, marker='x', facecolors='r')
    st.title("Player Shot Chart")
    st.pyplot(plt.gcf())