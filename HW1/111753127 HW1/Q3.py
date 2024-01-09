import cv2
import numpy as np

def bilinear_interpolation(img, new_size):
    old_size = img.shape[:2]
    x_scale = float(old_size[1] - 1) / (new_size[1] - 1)
    y_scale = float(old_size[0] - 1) / (new_size[0] - 1)
    new_img = np.zeros((new_size[0], new_size[1], img.shape[2]), dtype=np.uint8)

    for i in range(new_size[0]):
        for j in range(new_size[1]):
            x = int(x_scale * j)
            y = int(y_scale * i)
            x_diff = (x_scale * j) - x
            y_diff = (y_scale * i) - y
            if x < old_size[1]-1 and y < old_size[0]-1:
                # Bilinear interpolation
                for k in range(img.shape[2]):
                    new_img[i,j,k] = (img[y,x,k] * (1 - x_diff) * (1 - y_diff) +
                                      img[y+1,x,k] * x_diff * (1 - y_diff) +
                                      img[y,x+1,k] * (1 - x_diff) * y_diff +
                                      img[y+1,x+1,k] * x_diff * y_diff).astype(np.uint8)
            else:
                new_img[i,j] = img[y,x]

    return new_img

# 導入圖像
img = cv2.imread('lena.bmp')

# 用 bilinear interpolation 來重製圖像
resized_img = bilinear_interpolation(img, (1024, 1024))

# 儲存並展示重製後的圖像
cv2.imshow('lena_resized.bmp', resized_img)
cv2.imwrite('lena_resized.bmp', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
