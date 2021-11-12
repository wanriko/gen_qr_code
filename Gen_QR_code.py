# Gen QR code
import qrcode
input_ = input('input link...')
print(input_)
img = qrcode.make(input_)
img.save("youtubeQR.jpg")


