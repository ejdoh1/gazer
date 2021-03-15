import cv2
import numpy as np

x_bounds = [0, 640]
y_bounds = [0, 480]
CHANNELS = 3
SCALING = 5
THICKNESS = 5
RADIUS = 5
POINTS_NEEDED = 2
GREEN = (0, 255, 0)
RED = (0, 0, 255)

p = [] # points
img = np.zeros((y_bounds[1], x_bounds[1], CHANNELS), np.uint8)

# calculate the point at the end of the line (p3)
def p3(p1, p2, scaling):
    # calculate the angle between the two click points and the distance between them
    d = [p2[0]-p1[0],p2[1]-p1[1]] # x, y deltas
    theta = np.arctan2(d[1], d[0])
    # scale the length of the line proportionally to the distance between them
    m = np.sqrt(d[0]*d[0] + d[1]*d[1]) * scaling
    # calculate the point at the end of the line (p3)
    return (int(m * np.cos(theta) + p1[0]), int(m * np.sin(theta) + p1[1]))

# trigger drawing circles and lines on mouse click events
def on_click(event, x, y, p1, p2):
    global p
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(p) == POINTS_NEEDED:
            p = []  # start again

        # draw a circle at the click point
        cv2.circle(img, (x, y), RADIUS, GREEN, THICKNESS)
        cv2.imshow('', img)

        # store the click point to be able to get two of them
        p.append((x, y))
        print(f"Point {len(p)} selected at x {x} and y {y}")

        # if we've got two click points, draw the line
        if len(p) == POINTS_NEEDED:
            # draw the line between p1 and p3, and show it
            cv2.line(img, p[0], p3(p[0], p[1], SCALING), RED, THICKNESS)
            cv2.imshow('', img)

# show the image ready for capturing click events
cv2.imshow('', img)
cv2.setMouseCallback('', on_click)
print("Select two points...")
cv2.waitKey(0)
