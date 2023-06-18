#  01  without color QRcode
# my you-tube channel qr-code
import qrcode as qr
img =qr.make("https://www.youtube.com/channel/UCrqpJRz037P__tyAf78irxw")
img.save("AK Invisible.png")

#  02  with color Qr code

#import qrcode 
#from PIL import Image

# qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=10)
# qr.add_data("https://www.youtube.com/channel/UCrqpJRz037P__tyAf78irxw")
# qr.make(fit=True)
# img=qr.make_image(fill_color="green",back_color="white")
# img.save("Color QR ")
