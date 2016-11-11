# Name: Kendra Repo
# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import urllib.request, urllib.parse, urllib.error
import requests
import re
from bs4 import BeautifulSoup

file = open('newpage.html', 'w')
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
html = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(html, "html.parser")

# Part 1
change = soup.prettify()
change = change.replace('student', "AMAZING student")

# Part 2
change = change.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', 'kendra.jpg')

# Part 3
change = change.replace('logo2.png', 'media/logo.png')

file.write(change)