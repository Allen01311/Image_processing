import os
import numpy as np
from PIL import Image

def apply_mean_filter(image):
    img_array = np.array(image)
    filtered_array = np.zeros_like(img_array)

    height, width = img_array.shape

    for i in range(2, height - 2):
        for j in range(2, width - 2):
            neighbors = img_array[i-2:i+3, j-2:j+3]
            filtered_array[i, j] = np.mean(neighbors)

    filtered_image = Image.fromarray(filtered_array.astype(np.uint8))
    return filtered_image

def calculate_psnr(original_image, noisy_image, denoised_image):
    mse_noisy = np.mean((np.array(original_image) - np.array(noisy_image)) ** 2)
    mse_denoised = np.mean((np.array(original_image) - np.array(denoised_image)) ** 2)
    psnr_noisy = 10 * np.log10(255**2 / mse_noisy)
    psnr_denoised = 10 * np.log10(255**2 / mse_denoised)
    return psnr_noisy, psnr_denoised


# Load the original images
baboon = Image.open('baboon.bmp')
peppers = Image.open('peppers.bmp')

# Define the noise percentages
noise_percentages = [10, 30, 50, 70, 90]

# Specify the directory for saving the noisy images
save_dir = "../helloworld/Q1_b_outputs"

# Specify the directory containing the noisy images
noisy_images_dir = "../helloworld/Q1_a_outputs"

for percentage in noise_percentages:
    # Load the noisy images
    noisy_baboon = Image.open(os.path.join(noisy_images_dir, f"noisy_baboon_{percentage}.bmp"))
    noisy_peppers = Image.open(os.path.join(noisy_images_dir, f"noisy_peppers_{percentage}.bmp"))

    # Apply mean filtering
    denoised_baboon = apply_mean_filter(noisy_baboon)
    denoised_peppers = apply_mean_filter(noisy_peppers)

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
    file_name_baboon = os.path.join(save_dir, f"denoised_baboon_{percentage}.bmp")
    file_name_peppers = os.path.join(save_dir, f"denoised_peppers_{percentage}.bmp")
    noisy_baboon.save(file_name_baboon)
    noisy_peppers.save(file_name_peppers)
    # denoised_baboon.save(f"denoised_baboon_{percentage}.bmp")
    # denoised_peppers.save(f"denoised_peppers_{percentage}.bmp")