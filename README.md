# Pelican to Hugo v20180603

A little Python script to convert Markdown files using the pseudo YAML frontmatter syntax from Pelican to files using the strict YAML frontmatter syntax that Hugo and other static engines expect. By [Anthony Nelzin-Santos](https://anthony.nelzin.fr).

## Usage

Input from Pelican:

	title: Lorem ipsum dolor sit amet
	date: 2018-06-03 12:00
	tags: Lorem, ipsum, dolor
	
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla tincidunt rutrum nulla eget mollis. Quisque quis velit ac neque porta egestas et eget ex. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris id enim varius ligula scelerisque vehicula. Sed consequat id ligula viverra condimentum. Vestibulum a consectetur risus, vitae pretium est. Maecenas eu arcu sit amet est commodo malesuada. Nulla mattis mauris et dictum ultrices. Nullam consequat blandit mauris non pulvinar.
	
Open the script and add the path to your (backup of your) files:

	path = 'your/path/here'
	
Run the script:

	python3 pelican-to-hugo.py

Output for Hugo : 

	---
	title: "Lorem ipsum dolor sit amet"
	date: 2018-06-03T12:00:00Z
	tags:
	- "Lorem"
	- "ipsum"
	- "dolor"
	---
	
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla tincidunt rutrum nulla eget mollis. Quisque quis velit ac neque porta egestas et eget ex. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris id enim varius ligula scelerisque vehicula. Sed consequat id ligula viverra condimentum. Vestibulum a consectetur risus, vitae pretium est. Maecenas eu arcu sit amet est commodo malesuada. Nulla mattis mauris et dictum ultrices. Nullam consequat blandit mauris non pulvinar.

You’re probably going to have to adapt this script to your own needs (TOML syntax, custom taxonomies…). Have fun!

## Licence

Licenced under the terms of the [European Union Public Licence v1.2](https://joinup.ec.europa.eu/collection/eupl/eupl-text-11-12).