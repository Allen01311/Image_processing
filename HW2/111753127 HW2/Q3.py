import cv2
import numpy as np

# Read in the image
img = cv2.imread('aerialview-washedout.tif', cv2.IMREAD_GRAYSCALE)

# Compute the histogram of the image
hist, _ = np.histogram(img, bins=256, range=(0, 255))

# Compute the cumulative distribution function (CDF) of the histogram
cdf = np.zeros(256, dtype=np.uint32)
cdf[0] = hist[0]
for i in range(1, 256):
    cdf[i] = cdf[i-1] + hist[i]

# Compute the normalized CDF
norm_cdf = cdf / cdf[-1]

# Compute the mapping function from input intensities to output intensities
map_func = np.zeros(256, dtype=np.uint8)
for i in range(256):
    map_func[i] = np.uint8(norm_cdf[i] * 255 + 0.5)

# Apply the mapping function to the image to perform histogram equalization
img_he = np.zeros_like(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_he[i, j] = map_func[img[i, j]]

# Save the histogram-equalized image
cv2.imwrite('Q3.tif', img_he)