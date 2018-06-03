#!/usr/bin/env python3
#
# Pelican to Hugo v20180603
#
# Convert Markdown files using the pseudo YAML frontmatter syntax
# from Pelican to files using the strict YAML frontmatter syntax
# that Hugo and other static engines expect.
#
# Anthony Nelzin-Santos
# https://anthony.nelzin.fr
# anthony@nelzin.fr
#
# European Union Public Licence v1.2
# https://joinup.ec.europa.eu/collection/eupl/eupl-text-11-12

import os, os.path, re

#  Add the path to your files below
path = 'your/path/here'
files = os.listdir(path)

for file in files:
	file_name, file_extension = os.path.splitext(file)
	# Input files will be left in place,
	# output files will be suffixed with "_hugo".
	regexed_file = file_name + '_hugo' + file_extension

	# Only convert visible Markdown files.
	# This precaution is useless… until it is useful,
	# mainly on .DS_Store-ridden macOS folders.
	if not file_name.startswith('.') and file_extension in ('.md') : 
		input_file = os.path.join(path, file)
		output_file = os.path.join(path, regexed_file)

		# The files will be edited line by line using regex.
		# The conversion of a thousand files only takes a few seconds.
		with open(input_file, 'rU') as fi, open(output_file, 'w') as fo:
			for line in fi:
				# Add opening frontmatter delimiter before the title.
				line = re.sub(r'(title:)', r'---\n\1', line)
				# Add closing frontmatter delimiter after the tags.
				line = re.sub(r'(tags: .*)$$', r'\1\n---', line)
				# Enclose the title in quotes.
				line = re.sub(r'title: (.*)', r'title: "\1"', line)
				# Change date formatting.
				line = re.sub(r'(date: \d{4}-\d{2}-\d{2}) (\d{2}:\d{2})', r'\1T\2:00Z', line)
				# Slow but insightful way to edit the tags.
				if re.match(r'tags: (.*)', line):
					# Split the comma separated list of tags.
					tag_split = re.sub(r'(.*)', r'\1', line).split(', ')
					# Output the new list of tags.
					tag_plist = '\n- '.join(tag_split)
					# Insert a newline before the list.
					tag_list = re.sub(r'tags: (.*)', r'tags: \n- \1', tag_plist)
					# And enclose the tags in quotes.
					line = re.sub(r'- (.*)', r'- "\1"', tag_list)
				fo.write(line)
			# Print a little something about the conversion.
			print(file_name + ' converted.')