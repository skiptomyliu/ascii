from PIL import Image

"""

"""

class GRAYSCALE:
	# http://paulbourke.net/dataformats/asciiart/
	SHORT = ' .:-=+*#%@'
	SHORT = '@%#*+=-:. '
	LONG = ' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

class ImgProcess:
	def __init__(self, img_path, width=100, grayscale=GRAYSCALE.LONG):
		self.img = Image.open(img_path)

		# Resize first
		self.size = self.resize_to_width(width)
		self.width,self.height = self.size
		self.img.thumbnail(self.size, Image.ANTIALIAS)

		# Convert to greyscale
		self.img = self.img.convert('L')		

		# Get pixels
		self.pix = self.img.load()
		self.grayscale = grayscale
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

print ImgProcess(img_path="grumpy.png", width=50, grayscale=GRAYSCALE.SHORT).convert_image_to_ascii()








