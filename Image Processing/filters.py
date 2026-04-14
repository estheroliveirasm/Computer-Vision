# Apply blur to space using GaussianBlur

import cv2 as cv

# Load the image
space = cv.imread('Assets/randomspace.jpg')

# Gaussian Blur: Useful for reducing image noise and detail
# (5, 5) is the kernel size, 100.0 is the standard deviation (sigma)
blurred = cv.GaussianBlur(space, (5, 5), 100.0)
cv.imwrite("Assets/blurredspace.jpg", blurred)

# Median Blur: Highly effective against "salt and pepper" noise
medblurred = cv.medianBlur(space, 5)
cv.imwrite("Assets/mediamblurspace.jpg", medblurred)

# Convert the median blurred image to grayscale
blurred_gray = cv.cvtColor(medblurred, cv.COLOR_BGR2GRAY)

# Thresholding: Creating a binary mask
# Using Otsu's method to automatically determine the best threshold value
_, backgroundmask = cv.threshold(blurred_gray, 50, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# Save the resulting background mask
cv.imwrite("Assets/backgroundmask.jpg", backgroundmask)