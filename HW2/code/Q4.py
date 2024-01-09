import cv2

# Read the image and convert it to grayscale
image = cv2.imread("aerialview-washedout.tif", cv2.IMREAD_GRAYSCALE)

# Calculate the histogram
histogram = [0] * 256
total_pixels = 0
for row in image:
    for pixel_value in row:
        histogram[pixel_value] += 1
        total_pixels += 1

# Compute the median μ
halfway = total_pixels // 2
cumulative_sum = 0
median = 0
for intensity in range(256):
    cumulative_sum += histogram[intensity]
    if cumulative_sum >= halfway:
        median = intensity
        break

# Divide the histogram into two sub-histograms
sub_hist1 = [0] * (median + 1)
sub_hist2 = [0] * (256 - median - 1)

for intensity in range(median + 1):
    sub_hist1[intensity] = histogram[intensity]

for intensity in range(median + 1, 256):
    sub_hist2[intensity - median - 1] = histogram[intensity]

# Compute the total number of pixels for each sub-histogram
total_pixels1 = sum(sub_hist1)
total_pixels2 = sum(sub_hist2)

# Calculate the normalization factor for each sub-histogram
norm_factor1 = 255 / total_pixels1
norm_factor2 = 255 / total_pixels2

# Compute the cumulative distribution function (CDF) for each sub-histogram
cdf1 = [0] * (median + 1)
cdf2 = [0] * (256 - median - 1)
cdf1[0] = sub_hist1[0] * norm_factor1
cdf2[0] = sub_hist2[0] * norm_factor2

for intensity in range(1, median + 1):
    cdf1[intensity] = cdf1[intensity - 1] + sub_hist1[intensity] * norm_factor1

for intensity in range(1, 256 - median - 1):
    cdf2[intensity] = cdf2[intensity - 1] + sub_hist2[intensity] * norm_factor2

# Perform Histogram Equalization on each sub-histogram
equalized_hist1 = [0] * (median + 1)
equalized_hist2 = [0] * (256 - median - 1)

for intensity in range(median + 1):
    equalized_hist1[intensity] = round(cdf1[intensity])

for intensity in range(256 - median - 1):
    equalized_hist2[intensity] = round(cdf2[intensity])

# Apply Histogram Equalization to the image using the computed histograms
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        pixel_value = image[i, j]
        if pixel_value <= median:
            image[i, j] = equalized_hist1[pixel_value]
        else:
            image[i, j] = equalized_hist2[pixel_value - median - 1]

# Save the equalized image
cv2.imwrite("Q4.tif", image)
