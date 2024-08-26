import PIL
from PIL import Image
def new_func():
    return PIL.Image.open("C:/Users/lenovo/OneDrive/Desktop/ZZZZZZZ")

img=new_func()
width,height=img.size
print(width ,"x",height)
