
import unittest

from imageprocess import ImgProcess

class ImageProcessTestCase(unittest.TestCase):

	def setUp(self):
		self.imageprocess = ImgProcess('./grumpy.png')

	def tearDown(self):
		self.imageprocess = None

    # Use the grumpy image for testing
	def test_resize_to_width(self):
		self.assertEqual(self.imageprocess.resize_to_width(300), (300, 225))

	def test_pixel_to_ascii(self):
		self.assertEqual(self.imageprocess.pixel_to_ascii(0), "$")

if __name__ == '__main__':
    unittest.main()