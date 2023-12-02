import cv2
import numpy as np
import pandas as pd
import argparse

# Creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

# Reading the image with opencv
img = cv2.imread(img_path)

# Declaring global variables (are used later on)
clicked = False
r = g = b = xpos = ypos = 0
current_color = None

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# Function to calculate minimum distance from all colors and get the most matching color
def getColorName(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Function to get x, y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked, current_color
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        current_color = (r, g, b)
    elif event == cv2.EVENT_LBUTTONDOWN:
         clicked = False
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    cv2.imshow("image", img)
    if clicked:
        # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), current_color, -1)

        # Creating text string to display( Color name and RGB values )
        text = getColorName(*current_color) + ' R=' + str(current_color[2]) + ' G=' + str(current_color[1]) + ' B=' + str(current_color[0])

        # Calculate color percentages
        total = sum(current_color)
        r_percent = (current_color[2] / total) * 100
        g_percent = (current_color[1] / total) * 100
        b_percent = (current_color[0] / total) * 100

        # Display color percentages
        text_percent = f'R%={r_percent:.2f} G%={g_percent:.2f} B%={b_percent:.2f}'
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, text_percent, (50, 80), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colours, display text in black colour
        if sum(current_color) >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(img, text_percent, (50, 80), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Break the loop when the user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
