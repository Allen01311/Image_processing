from PIL import Image
import numpy as np
import math
import os

# 載入Image
watermarked_img = Image.open("lena_watermarked.bmp")

#壓縮率
compression_ratios = [10, 30, 50]

# compressed images 和 decoded images 所儲存的資料夾 
output_dir = "compressed_images"

# 如果以上資料夾不存在，則創建新的資料夾
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop over the compression ratios and compress the image at each ratio
for compression_ratio in compression_ratios:
    # 定義壓縮後的Image名稱
    compressed_filename = os.path.join(output_dir, "lena_compressed_q" + str(compression_ratio) + ".jpg")

    # 讓Image符合JPEG standard
    watermarked_img.save(compressed_filename, quality=compression_ratio, subsampling=0)

    # 載入壓縮後的Image
    compressed_img = Image.open(compressed_filename)

    # 將Image轉成numpy array以方便後續計算PSNR
    watermarked_arr = np.asarray(watermarked_img)
    compressed_arr = np.asarray(compressed_img)

    # 計算原始Image和壓縮Image之間的PSNR
    mse = np.mean((watermarked_arr - compressed_arr) ** 2)
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    print("Compression ratio:", compression_ratio, "PSNR:", psnr)

    # Decode上面壓縮的Image並保存成新的Image
    decoded_img = Image.fromarray(compressed_arr)
    decoded_filename = os.path.join(output_dir, "lena_decoded_q" + str(compression_ratio) + ".png")
    decoded_img.save(decoded_filename)