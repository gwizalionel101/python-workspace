import barcode
from barcode.writer import ImageWriter
from IPython.display import  image, display
user_data = input("Enter the data to encode in the barcode: ")
code = barcode.get('code128', user_data, write=ImageWriter())
filename = code.save("lionelbarcode")
display(Image(filename=filename))