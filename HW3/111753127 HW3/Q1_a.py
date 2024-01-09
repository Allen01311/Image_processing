import os
import numpy as np
from PIL import Image

def add_salt_and_pepper_noise(image, noise_percentage):
    np.random.seed(42)  # Set random seed for reproducibility
    img_array = np.array(image)

    # Calculate the number of noisy pixels based on the noise percentage
    noisy_pixels = int((noise_percentage / 100) * img_array.size)

    # Generate random coordinates for salt and pepper noise
    salt_coords = [np.random.randint(0, i - 1, int(noisy_pixels / 2)) for i in img_array.shape]
    pepper_coords = [np.random.randint(0, i - 1, int(noisy_pixels / 2)) for i in img_array.shape]

    # Add salt noise (white pixels)
    img_array[tuple(salt_coords)] = 255

    # Add pepper noise (black pixels)
    img_array[tuple(pepper_coords)] = 0

    noisy_image = Image.fromarray(img_array)
    return noisy_image


# Load and display the original images
baboon = Image.open('baboon.bmp')
peppers = Image.open('peppers.bmp')

# baboon.show()
# peppers.show()

# Add salt-and-pepper noise to the images with different percentages
noise_percentages = [10, 30, 50, 70, 90]

# Specify the directory for saving the noisy images
save_dir = "../helloworld/Q1_a_outputs"

for percentage in noise_percentages:
    noisy_baboon = add_salt_and_pepper_noise(baboon, percentage)
    noisy_peppers = add_salt_and_pepper_noise(peppers, percentage)

    # Display the noisy images
    print(f"Noisy Baboon ({percentage}% noise):")
    noisy_baboon.show()

    print(f"Noisy Peppers ({percentage}% noise):")
    noisy_peppers.show()
    
    # Save the noisy images to files in the specified directory
    file_name_baboon = os.path.join(save_dir, f"noisy_baboon_{percentage}.bmp")
    file_name_peppers = os.path.join(save_dir, f"noisy_peppers_{percentage}.bmp")
    noisy_baboon.save(file_name_baboon)
    noisy_peppers.save(file_name_peppers)