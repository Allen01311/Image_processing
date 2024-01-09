import cv2
import numpy as np

# Load the image and convert it to grayscale
img = cv2.imread('aerialview-washedout.tif', cv2.IMREAD_GRAYSCALE)

# Define the block size
block_size = 7

# Divide the image into non-overlapping blocks
rows, cols = img.shape
num_blocks_rows = rows // block_size
num_blocks_cols = cols // block_size

# Iterate over each block
for i in range(num_blocks_rows):
    for j in range(num_blocks_cols):
        # Extract the current block
        block = img[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size]

        # Compute the histogram of the block
        hist, bins = np.histogram(block.flatten(), 256, [0, 256])

        # Compute the cumulative distribution function (CDF) of the histogram
        cdf = hist.cumsum()

        # Normalize the CDF to have values between 0 and 255
        cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())

        # Compute the mapping function that maps each input intensity level to its corresponding output intensity level based on the CDF
        mapping = np.floor(cdf_normalized).astype('uint8')

        # Apply the mapping function to each pixel in the block
        block_equalized = cv2.LUT(block, mapping)

        # Replace the current block with the equalized block
        img[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size] = block_equalized

# Save the equalized image
cv2.imwrite('Q5.tif', img)
