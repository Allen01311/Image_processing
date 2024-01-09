from PIL import Image

image1=Image.open("laptop_left.png")
image2=Image.open("laptop_right.png")

# 取得圖像的長寬
width1, height1 = image1.size

# 創造一個寬度為原圖2倍的新圖像(前提是2張圖必須同寬高)
new_image = Image.new('RGB', (width1 * 2, height1))

# 將兩張圖像並排貼到新圖像上
new_image.paste(image1, (0, 0))
new_image.paste(image2, (width1, 0))

# 顯示新圖像
new_image.show()

# 保存新圖像
new_image.save("combine.png")