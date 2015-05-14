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

		print "HOST => " + self.host

		validator = HttpUrl()

		for linkObject in domObjects.findAll('a'):
			url = self.checkURL(linkObject.get("href"))
			print url

			if validator(url):	
				print "valid url => " + url		
				try:
					Link(url=url, source=self.source).save()
				except Exception, e:
					print "Link ja extraido"
				

	def checkURL(self, url):

		if type(url) is NoneType:
			return ""

		if url.find("#") == 0:
			return ""

		if not url.find(self.host):
			return ""

		return url
		
		