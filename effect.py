from PIL import Image, ImageFilter

import string
import random
import os

def random_filename(path=None, length=None):
	text = string.ascii_letters + string.digits

	if path == None:
		path = 'greyscale/'

	if length == None:
		guess = random.randrange(8,15)
		length = range(guess)

	return path + ''.join( [random.choice(text) for x in length] ) + '.png'

def processor(img_filename, delete_sections=False, delete_converts=False):
	original = Image.open(img_filename)

	img_height, img_width = original.height, original.width
	
	greyscale = original.convert('1')
	grey_filename = random_filename()
	greyscale.save(grey_filename)

	edges = original.filter(ImageFilter.CONTOUR)
	edged_filename = random_filename(path="outline/")
	edges.save(edged_filename)

	bottom = (img_width/3) * 2
	grey_section = greyscale.crop([img_width/3, 0, bottom, img_height]) 
	grey_section_filename = random_filename(path="sections/")
	grey_section.save(grey_section_filename)

	edge_section = edges.crop([0, 0, img_width/3, img_height])
	edge_section_filename = random_filename(path="sections/")
	edge_section.save(edge_section_filename)

	top = (img_width/3) * 2
	original_section = original.crop([top, 0, img_width, img_height])
	original_section_filename = random_filename(path="sections/")
	original_section.save(original_section_filename)

	sections = [edge_section, grey_section, original_section]

	merged = Image.new('RGB', (img_width, img_height))

	offset = 0
	for section in sections:
		merged.paste(section, (offset, 0))
		offset += section.size[0]

	merged_filename = random_filename(path="merged/")
	merged.save(merged_filename)

	if delete_sections:
		os.remove(grey_section_filename)
		os.remove(edge_section_filename)
		os.remove(original_section_filename)

	if delete_converts:
		os.remove(grey_filename)
		os.remove(edged_filename)


	return merged_filename
