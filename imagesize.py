# program to find the width and height of a image
import PIL
from PIL import Image
img=PIL.Image.open("C:/Users/lenovo/OneDrive/Desktop/ZZZZZZZ")
width,height=img.size
print(width,'x',height)