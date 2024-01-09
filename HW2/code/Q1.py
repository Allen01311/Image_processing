import cv2

# Read in the fixed image
img = cv2.imread('text-broken.tif', 0)


#task 1

# Define structuring element for dilation and erosion
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

for i in range(2):
    img = cv2.dilate(img, kernel)
# Perform dilation and erosion multiple times to remove noise and fill gaps
for j in range(2):
    img = cv2.erode(img, kernel)

# Save text_fixed image
cv2.imwrite('Q1-1.tif', img)

#----------------------------------------------------

#task 2

# Perform the erosion operation
img_eroded = cv2.erode(img, kernel)

# Subtract the eroded image from the fixed image to obtain the boundaries
img_boundaries = cv2.subtract(img, img_eroded)

# Save the boundaries image
cv2.imwrite('Q1-2.tif', img_boundaries)