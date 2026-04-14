import cv2 as cv

# Segment space image using thresholding
space = cv.imread('Assets/space.jpg')
gray = cv.cvtColor(space, cv.COLOR_BGR2GRAY)

# Binary Inversion: everything above 50 is replaced by 255 (white)
# This creates a mask where the background is isolated
_, mask = cv.threshold(gray, 50.0, 255, cv.THRESH_BINARY_INV)
cv.imwrite('Assets/maskinv.jpg', mask)

# Change the background color to blue (assigned as BGR: 255, 0, 0)
# This uses the mask to locate specific pixels and modify them
space[mask == 255] = (255, 0, 0)
cv.imwrite("Assets/bluespace.jpg", space)

# Segment circle image using Otsu's automatic thresholding
circle = cv.imread('Assets/circle.jpg')
# Converting the processed 'space' image back to grayscale for Otsu testing
graycircle = cv.cvtColor(space, cv.COLOR_BGR2GRAY)
thresh, mask = cv.threshold(graycircle, 50, 255, cv.THRESH_OTSU)

print(f"The calculated Otsu threshold is: {thresh}")
cv.imwrite("Assets/circlemask.jpg", mask)