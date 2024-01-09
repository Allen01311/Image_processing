from PIL import Image

# 將照片的白色部分去除
def remove_white_background(image):
    image = image.convert("RGBA")
    data = image.getdata()
    new_data = []

    for item in data:
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    image.putdata(new_data)
    return image

# 重製graveler.bmp的大小
def resize_image(image_path, size):
    image = Image.open(image_path)
    image_resized = image.resize(size, Image.Resampling.LANCZOS)
    image_resized.save(image_path) # saves the resized image back to the original file path.

#將graveler.bmp丟入remove_white_background(image)函式，讓它去除白色的部分
#之後利用PIL的函式.paste讓graveler.bmp及lena.bmp能夠成功疊合
def overlay_image(overlay_image_path, enlarged_image_path, output_path, position):
    image_overlay = Image.open(overlay_image_path)
    image_enlarged = Image.open(enlarged_image_path)
    
    image_no_white = remove_white_background(image_overlay)
    image_enlarged.paste(image_no_white, position, image_no_white)
    image_enlarged.show(output_path)
    image_enlarged.save(output_path)


# 導入圖像
overlay_image_path = "graveler.bmp"
enlarged_image_path = "lena.bmp"
output_path = "graveler_with_lena.bmp"

# 重製圖像的大小
new_size = (300, 300)  # Replace with the desired size
resize_image(overlay_image_path, new_size)

# 疊合圖像
position = (50, 70)  # Replace with the desired position
overlay_image(overlay_image_path, enlarged_image_path, output_path, position)