from models import *
from bs4 import BeautifulSoup
from urlparse import urlparse
import urllib2
from types import *

class Extractor:		

	def __init__(self, source):
		self.source = source
	

	def init(self):
		htmlPage = urllib2.urlopen(self.source.url)
		domObjects = BeautifulSoup(htmlPage)

		for linkObject in domObjects.findAll('a'):
			url = linkObject.get("href")
			print url

			if self.validate(url):
				if not(Link.exists(url)):
					Link(url=url, source=self.source).save()

	def validate(self, u):

		if type(u) is NoneType:
			return False

		if not u.startswith("http://"):
			return False

		return True

	
		
		