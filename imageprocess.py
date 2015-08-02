from PIL import Image
import argparse


"""

"""

class GRAYSCALE:
	# http://paulbourke.net/dataformats/asciiart/
	SHORT = ' .:-=+*#%@'
	LONG = ' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

class ImgProcess():
	def __init__(self, img_path, width=100, grayscale=GRAYSCALE.LONG, invert=False):
		self.img = Image.open(img_path)

		# Resize first
		self.size = self.resize_to_width(width)
		self.width,self.height = self.size
		self.img.thumbnail(self.size, Image.ANTIALIAS)

		# Convert to greyscale
		self.img = self.img.convert('L')		

		# Get pixels
		self.pix = self.img.load()
		self.grayscale = grayscale if invert else grayscale[::-1]
		self.gs_length = len(grayscale)

	def resize_to_width(self, width):
		size = (int(width), int(float(width)/self.img.size[0]*self.img.size[1]))
		return size

	def pixel_to_ascii(self, value):
		normalized_value = int(value/256.0*self.gs_length)
		return self.grayscale[normalized_value]

	def convert_image_to_ascii(self):
		result = ''
		for v in range(self.height):
			for h in range(self.width):
				result = result+self.pixel_to_ascii(self.pix[h,v])
			result +=  '\n' 
		return result


def main():
	parser = argparse.ArgumentParser(description="Convert an image to ASCII")
	parser.add_argument("path", action="store", help="Path of image to convert to ascii")
	parser.add_argument("-w", "--width", action="store", required=False, dest="width", default=60, help="Width of pixels")
	parser.add_argument('-i', '--invert', action='store_true')
	parser.add_argument('-l', '--long', action='store_true', help="Use a longer ASCII representation")

	args = parser.parse_args()
	if args.path:
		print ImgProcess(img_path=args.path, width=args.width, grayscale=GRAYSCALE.LONG if args.long else GRAYSCALE.SHORT, invert=args.invert).convert_image_to_ascii()

if __name__ == "__main__":
    main()




