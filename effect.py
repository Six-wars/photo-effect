from PIL import Image, ImageFilter

import string
import random

def random_filename(path=None, length=None):
	text = string.ascii_letters + string.digits

	if path == None:
		path = 'greyscale/'

	if length == None:
		guess = random.randrange(8,15)
		length = range(guess)

	return path + ''.join( [random.choice(text) for x in length] ) + '.png'

def processor(img_filename):
	original = Image.open(img_filename)

	img_height, img_width = original.height, original.width
	
	greyscale = original.convert('1')
	grey_filename = random_filename()
	greyscale.save(grey_filename)

	edges = original.filter(ImageFilter.CONTOUR)
	edged_filename = random_filename(path="outline/")
	edges.save(edged_filename)

	grey_section = greyscale.crop([0, 0, img_width/3, img_height])
	grey_section_filename = random_filename(path="sections/")
	grey_section.save(grey_section_filename)

	bottom = (img_width/3) * 2
	edge_section = edges.crop([img_height/3, 0, img_height, bottom])
	edge_section_filename = random_filename(path="sections/")
	edge_section.save(edge_section_filename)

	top = (img_height/3) * 2
	original_section = original.crop([top, 0, img_height, img_width])
	original_section_filename = random_filename(path="sections/")
	original_section.save(original_section_filename)

	return None
