from PIL import Image


def make_preview(size, n_colors):
    im = Image.open('res.jpg')
    im = im.resize(size)
    im = im.quantize(n_colors)
    im.save('res.bmp')


exec(input())
