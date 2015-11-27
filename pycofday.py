#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import urllib
import urllib2
import os
import sys
import json

wallpaper_dir = u'/home/ceslat/Imágenes/Wallpaper/'
services = [
	{
		'name': 'bing',
		'api': 'http://www.bing.com/HPImageArchive.aspx?format=js&n=1'
	},
	{
		'name': 'natgeo',
		'api': 'https://natgeoapi.herokuapp.com/api/dailyphoto'
	},
	{
		'name': 'nasa',
		'api': 'https://api.nasa.gov/planetary/apod?hd=True&api_key=DEMO_KEY'
	}
]


while True:
	for i in services:
		sys.stdout.write('PycOfDay: Download image from (%s)\n' % i['name'])
		try:
			response = urllib2.urlopen(i['api'])
			data = json.loads(response.read())
	
			if i['name'] == 'bing':
				image_url = 'http://www.bing.com' + data['images'][0]['url']
				image_name = data['images'][0]['url'].split('/')[-1]
			elif i['name'] == 'natgeo':
				image_url = 'http:' + data['src']
				image_name = data['src'].split('/')[-1]
			else:
				image_url = data['url']
				image_name = data['url'].split('/')[-1]
		
			file_name = os.path.join(wallpaper_dir, image_name)
			if not os.path.exists(file_name):
				urllib.urlretrieve(image_url, filename=file_name)
				sys.stdout.write('PycOfDay: Download (%s)\n' % image_name)
			else:
				sys.stdout.write('PycOfDay: File Exits (%s)\n' % image_name)
		except urllib2.URLError as e:
			if e.code == 404:
				sys.stderr.write('PycOfDay: Error 404\n')
			else:
				sys.stderr.write('PycofDay: %s\n' % e)
	sys.stderr.write('PycOfDay: Sleep for 60 minutes... ZzZzZzzz\n')
	sleep(60 * 60)			
