import math
from PIL import Image

def bilinear_interpolation(x, y, pixels, width, height):
    x1, y1 = int(x), int(y)
    x2, y2 = math.ceil(x), math.ceil(y)

    q11 = pixels[y1 * width + x1] if 0 <= x1 < width and 0 <= y1 < height else (0, 0, 0)
    q12 = pixels[y2 * width + x1] if 0 <= x1 < width and 0 <= y2 < height else (0, 0, 0)
    q21 = pixels[y1 * width + x2] if 0 <= x2 < width and 0 <= y1 < height else (0, 0, 0)
    q22 = pixels[y2 * width + x2] if 0 <= x2 < width and 0 <= y2 < height else (0, 0, 0)

    r1 = tuple(((x2 - x) * q11_comp + (x - x1) * q21_comp) for q11_comp, q21_comp in zip(q11, q21))
    r2 = tuple(((x2 - x) * q12_comp + (x - x1) * q22_comp) for q12_comp, q22_comp in zip(q12, q22))

    return tuple(int(round((y2 - y) * r1_comp + (y - y1) * r2_comp)) for r1_comp, r2_comp in zip(r1, r2))


def rotate_image(input_image_path, output_image_path, rotation_angle=0):
    
    # 導入圖像
    input_image = Image.open(input_image_path).convert('RGB')

    input_pixels = list(input_image.getdata())

    # 計算輸出圖像的大小
    width, height = input_image.size
    angle_radians = math.radians(rotation_angle)
    new_width = int(abs(width * math.cos(angle_radians)) + abs(height * math.sin(angle_radians)))
    new_height = int(abs(width * math.sin(angle_radians)) + abs(height * math.cos(angle_radians)))

    # 計算輸入和輸出圖像的中心點
    input_center = (width / 2, height / 2)
    output_center = (new_width / 2, new_height / 2)

    output_pixels = []
    for y in range(new_height):
        row = []
        for x in range(new_width):
            # 計算輸出圖像像素的相對坐標
            rel_x, rel_y = x - output_center[0], y - output_center[1]
            # 計算像素的旋轉坐標
            rot_x = rel_x * math.cos(angle_radians) + rel_y * math.sin(angle_radians)
            rot_y = -rel_x * math.sin(angle_radians) + rel_y * math.cos(angle_radians)
            # 計算輸入圖像坐標
            input_x, input_y = rot_x + input_center[0], rot_y + input_center[1]
            row.append(bilinear_interpolation(input_x, input_y, input_pixels, width, height))
        output_pixels.append(row)

    output_image = Image.new('RGB', (new_width, new_height))
    for y, row in enumerate(output_pixels):
        for x, pixel in enumerate(row):
            output_image.putpixel((x, y), pixel)
    
    # 儲存旋轉後的圖片
    output_image.show(output_image_path)
    output_image.save(output_image_path)


# 導入及輸出圖像及需要旋轉的角度
input_image_path = 'combine.png'
output_image_path = 'rotated_image.png'
rotation_angle = 15
rotate_image(input_image_path, output_image_path, rotation_angle)

