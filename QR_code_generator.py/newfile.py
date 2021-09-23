#python QR code generator
import qrcode
image= qrcode.make(input("please enter the URL/TEXT for converting to qrcode: "))
#save the generated qrcode as extention .png
image.save("qrcode.png")

