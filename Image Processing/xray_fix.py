# You are trying to process multiple X-rays to detect anomalies. Unfortunately, some X-rays are not in the correct format to make your research easy.
# Generally, X-rays use darker colors to represent less dense areas of the image, while light colors represent high-density areas, such as bones.
# Transform the 'xray-inverted.jpg' image so that it follows the same pattern—white bones and black background—instead of its current structure.

import cv2 as cv

# Load an image
img = cv.imread("Assets/xray-inverted.jpg")

# Invert the image colors (bones become white and background becomes black)
# Since the max value of a pixel is 255, subtracting the current value flips the intensity.
inv = 255 - img

# Save the processed image
cv.imwrite('Assets/inverted.jpg', inv)