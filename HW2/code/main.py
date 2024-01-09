from PIL import Image

def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2-1] / 2.0 + s[n//2] / 2.0, s[n//2])[n % 2] if n else None

def histogram_equalization(input_path, output_path):
    image = Image.open(input_path).convert('L')
    width, height = image.size
    pixels = list(image.getdata())
    new_pixels = []

    # create a histogram
    histogram = [0] * 256
    for pixel in pixels:
        histogram[pixel] += 1

    # calculate the median
    mu = int(median(pixels))

    # divide the histogram into two sub-histograms
    lower_histogram = histogram[:mu+1]
    upper_histogram = histogram[mu+1:]

    # calculate the cumulative distribution function for each sub-histogram
    lower_cdf = [0] * (mu + 1)
    lower_cdf[0] = lower_histogram[0]
    upper_cdf = [0] * (256 - mu - 1)
    upper_cdf[0] = upper_histogram[0]
    for i in range(1, mu + 1):
        lower_cdf[i] = lower_cdf[i - 1] + lower_histogram[i]
    for i in range(1, 256 - mu - 1):
        upper_cdf[i] = upper_cdf[i - 1] + upper_histogram[i]

    # normalize the cdfs
    lower_cdf_min = min(filter(lambda x: x > 0, lower_cdf))
    upper_cdf_min = min(filter(lambda x: x > 0, upper_cdf))
    total_pixels = width * height
    lower_cdf_normalized = [(x - lower_cdf_min) / (total_pixels - 1) * mu for x in lower_cdf]
    upper_cdf_normalized = [(x - upper_cdf_min) / (total_pixels - 1) * (255 - mu - 1) for x in upper_cdf]

    # apply histogram equalization
    for pixel in pixels:
        if pixel <= mu:
            new_pixels.append(int(lower_cdf_normalized[pixel]))
        else:
            new_pixels.append(int(upper_cdf_normalized[pixel - mu - 1] + mu + 1))

    # save the result
    new_image = Image.new('L', (width, height))
    new_image.putdata(new_pixels)
    new_image.save(output_path)


input_path = "../helloworld/aerialview-washedout.tif"
output_path = "Q4.tif"
histogram_equalization(input_path, output_path)