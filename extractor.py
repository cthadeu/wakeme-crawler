from models import *
from bs4 import BeautifulSoup
from urlparse import urlparse
from types import *
from lepl.apps.rfc3696 import HttpUrl
import urllib2

class Extractor:		

	def __init__(self, source, host):
		self.source = source
		self.host = host
	

	def init(self):
		htmlPage = urllib2.urlopen(self.source.url)
		domObjects = BeautifulSoup(htmlPage)

		for linkObject in domObjects.findAll('a'):
			url = checkURL(linkObject.get("href"))
			           
			validator = HttpUrl()

			if validator(url):				
				Link(url=url, source=self.source).save()

	def checkURL(self, url):
		if not url.contains(self.host):
			return ""

		if not u.startswith("http://"):
			return = "http://" + url

		
		