import cv2
import numpy as np

def laplacian_edge_detection(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian smoothing
    smoothed = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply Laplacian operator
    laplacian = cv2.Laplacian(smoothed, cv2.CV_64F)

    # Compute the absolute Laplacian to obtain the edge map
    edge_map = np.absolute(laplacian)
    edge_map = cv2.normalize(edge_map, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return edge_map

# Load the 'pepper.bmp' image
pepper_image = cv2.imread('peppers.bmp')
pepper_edge_map = laplacian_edge_detection(pepper_image)

# Load the 'pepper_0.04.bmp' image
pepper_004_image = cv2.imread('peppers_0.04.bmp')
pepper_004_edge_map = laplacian_edge_detection(pepper_004_image)

# Display the edge maps
cv2.imshow('Pepper Edge Map', pepper_edge_map)
cv2.imshow('Pepper 0.04 Edge Map', pepper_004_edge_map)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the edge maps to desired paths
cv2.imwrite("../helloworld/Q2_b_outputs/pepper_edge_map.bmp", pepper_edge_map)
cv2.imwrite("../helloworld/Q2_b_outputs/pepper_0.04_edge_map.bmp", pepper_004_edge_map)
