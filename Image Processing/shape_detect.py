# Activity: Detects shapes, calculates the geometric center via point averaging, 
# and labels primary colors using the HSV color space.

import cv2 as cv
import numpy as np

# Load the source image
img = cv.imread("Assets/circles.png")

# Convert to different color spaces for processing
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Binarization: Creating a mask to isolate the shapes
# Thresholding with BINARY_INV because we want the shapes to be white (255)
_, th = cv.threshold(gray, 200, 255, cv.THRESH_BINARY_INV)
cv.imwrite("Assets/binary_mask.jpg", th)

# Contour Detection: Finding the boundaries of the shapes
contours, hierarchy = cv.findContours(th, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(f"Total contours found: {len(contours)}")

# Filtering contours by area to ignore noise
contours_filtered = []
for con in contours:
    area = cv.contourArea(con)
    if area > 500: 
        print(f"Detected area: {area}")
        contours_filtered.append(con)

# Draw the filtered contours on the original image for visualization
drawn_img = cv.drawContours(img.copy(), contours_filtered, -1, (0, 0, 255), 3)

for con in contours_filtered:
    # Reshape the contour points to a 2D array (x, y)
    points = con.reshape(-1, 2)
    
    # Calculate the geometric center (Centroid) manually using NumPy
    sum_x = np.sum(points[:, 0])
    sum_y = np.sum(points[:, 1])
    num_points = len(points)

    height, width = hsv.shape[:2]
    
    # Coordinates calculation with clipping to ensure they stay within image bounds
    cX = int(sum_x / num_points)
    cY = int(sum_y / num_points)
    cX = max(0, min(cX, width - 1))
    cY = max(0, min(cY, height - 1))
    
    # Color detection using the HSV space (Hue channel)
    pixel_hsv = hsv[cY, cX] 
    h = pixel_hsv[0] 

    # Classifying the color based on the Hue (H) value
    if h < 10 or h > 160:
        color_label = "Red"
    elif 35 < h < 85:
        color_label = "Green"
    elif 100 < h < 140:
        color_label = "Blue"
    else:
        color_label = "Unknown"

    print(f"Center: ({cX}, {cY}) | Hue: {h} | Color: {color_label}")

    # Draw a circle at the center and add the color label text
    cv.circle(drawn_img, (cX, cY), 5, (255, 0, 0), -1)
    cv.putText(drawn_img, color_label, (cX - 25, cY - 15), 
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)   
        
# Save the final analysis result
cv.imwrite("Assets/shape_analysis.jpg", drawn_img)