import cv2
import numpy as np
from PIL import Image

def main(file_path):

    # Görseli ekle
    img = cv2.imread(file_path)

    # Numpy array'e dönüştür.
    img_array = np.array(img)

    def decode_LSB(img):
        pixels = img.load()
        width, height = img.size

        # LSB Algoritması
        binary_data = ''
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                binary_data += str(r & 1)
                binary_data += str(g & 1)
                binary_data += str(b & 3)
                if binary_data[-16:] == '1111111111111110':
                    return binary_data[:-16]

        # Eğer bir değişme bulunamadıysa boş dön
        return ''

    # LSB tespit edilip edilmediğini kontrol edecek fonksiyon
    def detect_LSB_steganography(img_array):
        # numpy array'i PIL görseline dönüştür.
        img = Image.fromarray(img_array)

        # Görsel RGB formatında mı kontrol et
        if img.mode == 'RGB':
            data = decode_LSB(img)
            if data:
                return True

        # Steganografi yoksa False dön
        return False

    result = detect_LSB_steganography(img_array)

    if result:
        return "Steganography detected!"
    else:
        return "No steganography detected."