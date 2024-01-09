import cv2
import numpy as np

def sobel_edge_detection(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel filters to compute gradients
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Compute the gradient magnitude and normalize it
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # Threshold the gradient magnitude to obtain the edge map
    _, edge_map = cv2.threshold(gradient_magnitude, 50, 255, cv2.THRESH_BINARY)

    return edge_map

# Load the 'pepper.bmp' image
pepper_image = cv2.imread('peppers.bmp')
pepper_edge_map = sobel_edge_detection(pepper_image)

# Load the 'pepper_0.04.bmp' image
pepper_004_image = cv2.imread('peppers_0.04.bmp')
pepper_004_edge_map = sobel_edge_detection(pepper_004_image)

# Display the edge maps
cv2.imshow('Pepper Edge Map', pepper_edge_map)
cv2.imshow('Pepper 0.04 Edge Map', pepper_004_edge_map)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the edge maps to desired paths
cv2.imwrite("../helloworld/Q2_a_outputs/pepper_edge_map.bmp", pepper_edge_map)
cv2.imwrite("../helloworld/Q2_a_outputs/pepper_0.04_edge_map.bmp", pepper_004_edge_map)