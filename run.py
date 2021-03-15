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

points = []
img = np.zeros((y_bounds[1], x_bounds[1], CHANNELS), np.uint8)

# trigger drawing circles and lines on mouse click events
def on_click(event, x, y, p1, p2):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) == POINTS_NEEDED:
            points = [] # start again
        
        # draw a circle at the click point
        cv2.circle(img, (x, y), RADIUS, GREEN, THICKNESS)
        cv2.imshow('', img)

        # store the click point to be able to get two of them
        points.append((x, y))
        print(f"Point {len(points)} selected at x {x} and y {y}")

        # if we've got two click points, draw the line
        if len(points) == POINTS_NEEDED:
            # calculate the angle between the two click points and the distance between them
            p1 = points[0]
            p2 = points[1]
            dy = p2[1]-p1[1] # delta_y
            dx = p2[0]-p1[0] # delta_x
            theta = np.arctan2(dy, dx)
            dist = np.sqrt(dx*dx + dy*dy)
            
            # scale the length of the line proportionally to the distance between them
            m = dist * SCALING

            # calculate the point at the end of the line (p3)
            p3 = (int(m * np.cos(theta) + p1[0]),int(m * np.sin(theta) + p1[1]))

            # draw the line between p1 and p3, and show it
            cv2.line(img, p1, p3, RED, THICKNESS)
            cv2.imshow('', img)

# show the image ready for capturing click events
cv2.imshow('', img)
cv2.setMouseCallback('', on_click)
print("Select two points...")
cv2.waitKey(0)
