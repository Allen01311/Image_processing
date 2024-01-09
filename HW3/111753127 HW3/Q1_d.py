import os
import numpy as np
from PIL import Image
# from scipy.ndimage import median_filter

def calculate_psnr(original_image, noisy_image, denoised_image):
    mse_noisy = np.mean((np.array(original_image) - np.array(noisy_image)) ** 2)
    mse_denoised = np.mean((np.array(original_image) - np.array(denoised_image)) ** 2)
    psnr_noisy = 10 * np.log10(255**2 / mse_noisy)
    psnr_denoised = 10 * np.log10(255**2 / mse_denoised)
    return psnr_noisy, psnr_denoised


def get_smallest_valid_kernel_size(noisy_image, i, j):
    kernel_size = 3
    height, width = noisy_image.shape

    while kernel_size <= min(height, width):
        start_row = max(0, i - kernel_size // 2)
        end_row = min(height, i + kernel_size // 2 + 1)
        start_col = max(0, j - kernel_size // 2)
        end_col = min(width, j + kernel_size // 2 + 1)

        kernel = noisy_image[start_row:end_row, start_col:end_col]
        if np.any(kernel != 0) and np.any(kernel != 255):
            break

        kernel_size += 2

    return kernel_size


def apply_trimmed_median_filter(image):
    img_array = np.array(image)
    filtered_array = np.zeros_like(img_array)

    height, width = img_array.shape

    for i in range(height):
        for j in range(width):
            if img_array[i, j] == 0 or img_array[i, j] == 255:
                kernel_size = get_smallest_valid_kernel_size(img_array, i, j)
                start_row = max(0, i - kernel_size // 2)
                end_row = min(height, i + kernel_size // 2 + 1)
                start_col = max(0, j - kernel_size // 2)
                end_col = min(width, j + kernel_size // 2 + 1)

                kernel = img_array[start_row:end_row, start_col:end_col]
                filtered_pixel = np.median(kernel)
                filtered_array[i, j] = filtered_pixel
            else:
                filtered_array[i, j] = img_array[i, j]

    filtered_image = Image.fromarray(filtered_array.astype(np.uint8))
    return filtered_image


# Load the original images
baboon = Image.open('baboon.bmp')
peppers = Image.open('peppers.bmp')

# Define the noise percentages
noise_percentages = [10, 30, 50, 70, 90]

# Specify the directory for saving the noisy images
save_dir = "../helloworld/Q1_d_outputs"

# Specify the directory containing the noisy images
noisy_images_dir = "../helloworld/Q1_a_outputs"

for percentage in noise_percentages:
    # Load the noisy images
    noisy_baboon = Image.open(os.path.join(noisy_images_dir, f"noisy_baboon_{percentage}.bmp"))
    noisy_peppers = Image.open(os.path.join(noisy_images_dir, f"noisy_peppers_{percentage}.bmp"))

    # Apply the Modified Decision-based Unsymmetrical Trimmed Median Filter
    denoised_baboon = apply_trimmed_median_filter(np.array(noisy_baboon))
    denoised_peppers = apply_trimmed_median_filter(np.array(noisy_peppers))

    # Calculate PSNR
    psnr_noisy_baboon, psnr_denoised_baboon = calculate_psnr(baboon, noisy_baboon, denoised_baboon)
    psnr_noisy_peppers, psnr_denoised_peppers = calculate_psnr(peppers, noisy_peppers, denoised_peppers)

    # Display PSNR values
    print(f"Noisy Baboon ({percentage}% noise):")
    print("PSNR (Noisy):", psnr_noisy_baboon)
    print("PSNR (Denoised):", psnr_denoised_baboon)
    print()

    print(f"Noisy Peppers ({percentage}% noise):")
    print("PSNR (Noisy):", psnr_noisy_peppers)
    print("PSNR (Denoised):", psnr_denoised_peppers)
    print()

    # Save the denoised images
    # denoised_baboon_image = Image.fromarray(denoised_baboon.astype(np.uint8))
    # denoised_peppers_image = Image.fromarray(denoised_peppers.astype(np.uint8))
    
    file_name_baboon = os.path.join(save_dir, f"denoised_baboon_{percentage}_trimmed_median.bmp")
    file_name_peppers = os.path.join(save_dir, f"denoised_peppers_{percentage}_trimmed_median.bmp")
    noisy_baboon.save(file_name_baboon)
    noisy_peppers.save(file_name_peppers)
    # denoised_baboon_image.save(f"denoised_baboon_{percentage}_trimmed_median.bmp")
    # denoised_peppers_image.save(f"denoised_peppers_{percentage}_trimmed_median.bmp")
