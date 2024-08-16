import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc

"""
Working with sample instance of data here just 
to test whether the coordinates scatter smoothly
"""

Made = {
        'Christian Wood': [(58, 301), (74, 301), (368, 349), (68, 307), (56, 319)], 
        'Jahlil Okafor': [(234, 199), (132, 170), (173, 303), (68, 303), (95, 324), (83, 331), (68, 299), (68, 288), (65, 304), (216, 298), (56, 305), (56, 274), (64, 305)], 
        'Stephen Curry': [(369, 213)], 
        'Jacob Evans': [(44, 452), (73, 299), (249, 461)], 
        'Elfrid Payton': [(68, 318), (302, 115), (58, 305), (181, 571), (345, 185), (67, 294)], 
        'DeMarcus Cousins': [(62, 305), (56, 338), (67, 322), (52, 285), (65, 302), (70, 279), (139, 326), (359, 281), (138, 314)], 
        'Alfonzo McKinnie': [(58, 274), (307, 110), (68, 293)], 
        'Kevon Looney': [(46, 455), (123, 580), (65, 283)], 
        'Ian Clark': [(203, 309), (178, 301), (280, 337), (369, 383), (71, 283), (256, 319), (80, 464), (357, 195)], 
        'Draymond Green': [(218, 441)], 
        'Quinn Cook': [(286, 510), (53, 285), (67, 319), (231, 262), (372, 290), (95, 399), (64, 327), (70, 278)], 
        'Solomon Hill': [(222, 98), (111, 359)], 
        'Jonas Jerebko': [(283, 488), (243, 248), (57, 300), (245, 283)], 
        'Cheick Diallo': [(67, 308), (221, 46), (71, 303), (64, 298), (93, 122)], 
        'Jordan Bell': [(83, 304), (363, 279), (57, 300), (371, 356), (305, 239), (56, 300)], 
        'Kenrich Williams': [(76, 324), (214, 27), (347, 176), (67, 282)], 
        'Damion Lee': [(70, 269), (282, 95), (359, 301)], 
        'Dairis Bertans': [(73, 311)], 
        'Marcus Derrickson': [(64, 476), (270, 80)]
    }

Missed = {
        'Kenrich Williams': [(107, 576), (55, 24), (138, 23), (119, 349), (488, 195), (342, 377), (252, 173)], 
        'DeMarcus Cousins': [(139, 111), (71, 288), (141, 282), (368, 298), (70, 324), (295, 497), (163, 138), (292, 501), (119, 346), (335, 439), (64, 292)], 
        'Christian Wood': [(362, 392), (74, 276), (249, 192), (203, 337), (107, 278), (366, 337), (67, 282), (230, 544), (59, 322), (67, 583), (99, 30)], 
        'Alfonzo McKinnie': [(314, 207), (99, 307), (264, 80), (254, 540)], 
        'Ian Clark': [(369, 392), (356, 236), (148, 327), (255, 448), (302, 502), (136, 215), (56, 404), (191, 291), (65, 27), (173, 551), (384, 172), (332, 436), (117, 292)], 
        'Stephen Curry': [(46, 517), (302, 142)], 
        'Elfrid Payton': [(83, 409), (96, 299), (231, 561)], 
        'Jacob Evans': [(164, 26), (77, 324), (245, 48), (322, 466), (341, 446), (227, 212)], 
        'Draymond Green': [(58, 277), (157, 266)], 
        'Jahlil Okafor': [(206, 301), (126, 337), (157, 251), (114, 303), (132, 291), (293, 502), (68, 363), (83, 252), (81, 304)], 
        'Solomon Hill': [(380, 412), (90, 264), (359, 366), (290, 279), (255, 535)], 
        'Damion Lee': [(207, 167), (64, 326), (363, 280), (337, 143), (92, 461), (45, 30)], 
        'Quinn Cook': [(262, 297), (362, 211), (67, 126), (107, 289), (90, 159)], 
        'Cheick Diallo': [(50, 465), (122, 201)], 
        'Dairis Bertans': [(203, 526), (377, 361), (71, 29), (55, 108)], 
        'Jonas Jerebko': [(87, 294), (369, 247), (371, 302), (73, 327), (353, 243)], 
        'Jordan Bell': [(130, 180), (132, 373)], 
        'Shaun Livingston': [(239, 403)], 
        'Kevon Looney': [(291, 409)], 
        'Marcus Derrickson': [(261, 303), (55, 18)]
    }

def access_made(player_name):
    return Made[player_name]

def access_misses(player_name):
    return Missed[player_name]

am = access_made("Kenrich Williams")
x_made = [x[0] for x in am]
y_made = [x[1] for x in am]

am2 = access_misses("Kenrich Williams")
x_missed = [x[0] for x in am2]
y_missed = [x[1] for x in am2]

hoop = Circle((282, 58), radius=9, linewidth=1, color="blue", fill=False)
backboard = Rectangle((246, 48), 72, 0, linewidth=1, color="blue")
# The paint
# outer box
outer_box = Rectangle((186, 0), 192, 228, linewidth=1, color="blue", fill=False)
# inner box
inner_box = Rectangle((210, 0), 144, 228, linewidth=1, color="blue", fill=False)
top_free_throw = Arc((282, 228), 144, 144, theta1=0, theta2=180, linewidth=1, color="blue", fill=False)
bottom_free_throw = Arc((282, 228), 144, 144, theta1=180, theta2=0, linewidth=1, color="blue")
restricted = Arc((282, 58), 96, 96, theta1=0, theta2=180, linewidth=1, color="blue")

# Three Point Line
corner_three_a = Rectangle((36, 0), 0, 168, linewidth=1, color="blue")
corner_three_b = Rectangle((528, 0), 0, 168, linewidth=1, color="blue")
three_arc = Arc((282, 68), 528, 528, theta1=22, theta2=158, linewidth=1, color="blue")

plt.xlim(0, 564)
plt.ylim(0, 600)
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
plt.scatter(x_made, y_made, edgecolors='g', marker='o', facecolors='none')
plt.scatter(x_missed, y_missed, marker='x', facecolors='r')
plt.show()