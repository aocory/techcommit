import qrcode
from datetime import datetime

now=datetime.now().strftime("%Y/%m/%d %H:%M:%S")

img = qrcode.make(now)

print(type(img))
print(img.size)
# <class 'qrcode.image.pil.PilImage'>
# (290, 290)
print(now)
img.save('qrcode.png')

from datetime import datetime
datetime.now().strftime("%Y/%m/%d %H:%M:%S")
from PIL import Image, ImageDraw

im = Image.new("RGB",(500,500),"blue")# Imageインスタンスを作る
draw = ImageDraw.Draw(im)# im上のImageDrawインスタンスを作る
draw.text((0,0),now)
im.paste(img, (100, 50))
im.save("./qrcode1.png")

from IPython.display import Image,display_png
display_png(Image('qrcode1.png'))
