import cv2
import numpy as np

# Read in the image
img = cv2.imread('einstein-low-contrast.tif', cv2.IMREAD_GRAYSCALE)

# Compute the 1st and 99th percentile of pixel values in the image
min_value, max_value = np.percentile(img, (1, 99))

# Apply linear stretching to enhance the contrast
img_stretched = ((img - min_value) * 255 / (max_value - min_value)).astype(np.uint8)

# Save the stretched image
cv2.imwrite('Q2.tif', img_stretched)