from utils.image_operations import draw_countours, convert_to_sketch


if __name__ == '__main__':
    convert_to_sketch('photo.jpeg')
    draw_countours("sketch.jpg")