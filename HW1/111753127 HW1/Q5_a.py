import numpy as np
from PIL import Image

# 載入Images
lena = np.array(Image.open('lena.bmp'))
graveler = np.array(Image.open('graveler.bmp'))

# 調整浮水印大小
graveler = np.array(Image.fromarray(graveler).resize((lena.shape[1], lena.shape[0])))

# 水平翻轉Lena的Image
lena = np.fliplr(lena)

# 嵌入浮水印
alpha = 0.7
watermarked = alpha * lena + (1 - alpha) * graveler

# 儲存有加入浮水印的Image
Image.fromarray(np.uint8(watermarked)).show('lena_watermarked.bmp')
Image.fromarray(np.uint8(watermarked)).save('lena_watermarked.bmp')