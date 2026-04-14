# You are trying to create an artistic piece based on James Webb Telescope images.
# You must first extract the black background from the image and replace it with one of three RGB colors randomly:
# [(194,211,205), (159,164,169), (86,73,76)]

# Note: Remember that by default OpenCV opens images in BGR instead of RGB! [cite: 1]

import cv2 as cv
import random 

# Load an image [cite: 1]
space = cv.imread("Assets/space.jpg")
cat = cv.imread("Assets/cat.jpg")
colors = [(205,211,194), (169,164,159), (76,73,86)]

# Remove black background [cite: 1]
height, width, _ = space.shape

# Resize the cat image to match the space image dimensions [cite: 1]
cat = cv.resize(cat, (width, height))

for h in range(height):
    for w in range(width):
        pixel = space[h][w]
        # Check if the pixel is dark enough to be considered "background" [cite: 1]
        if pixel[0] < 90 and pixel[1] < 50 and pixel[2] < 100:
            # Replace the background pixel with the corresponding pixel from the cat image [cite: 1]
            space[h][w] = cat[h][w]

# Save image [cite: 1]
cv.imwrite('Assets/spacecat.jpg', space)