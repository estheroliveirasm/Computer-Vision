import cv2 as cv
import numpy as np

# Load an image
img = cv.imread("Assets/cute.jpg")

# Get the shape and pixel intensity range
print(f"Shape: {img.shape}")
print(f"Max pixel value: {img.max()}")
print(f"Min pixel value: {img.min()}")

# Draw a rectangle
# Arguments: image, top-left corner, bottom-right corner, color (B, G, R), thickness
img2 = cv.rectangle(
    img, (50,50), (100, 100), (0, 0, 255)
)

# Save the modified image
cv.imwrite('Assets/modified.jpg', img2)

#Channel Manipulation Examples

# Set blue channel to 0
# img[:, :, 0] = 0

# Set green channel to 0
# img[:, :, 1] = 0

# Save red-focused image
# cv.imwrite('red_tint.jpg', img)

#Color Space Conversion

# Change color space to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Get the shape of the grayscale image (it will only have 2 dimensions)
print(f'Gray Shape: {gray.shape}')

# Save grayscale image
cv.imwrite('Assets/gray.jpg', gray)

#Image Inversion

# Invert the colors (Negative)
# Subtracting from 255 flips the intensity
inv = 255 - img

# Save inverted image
cv.imwrite('Assets/inverted.jpg', inv)

#Pixel-wise Manipulation (Removing/Replacing White)

# Get dimensions
height, width, _ = img.shape

# Loop through every pixel
# Note: Using nested loops in Python is slow for large images; 
# NumPy masks are usually preferred for performance.
for h in range(height):
    for w in range(width):
        pixel = img[h][w]
        # Check if the pixel is close to white (High values in Blue, Green, and Red)
        if pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200:
            # Change white pixels to Cyan/Yellow (depending on BGR interpretation)
            img[h][w] = (0, 255, 255)

# Save result
cv.imwrite('Assets/processed_color.jpg', img)