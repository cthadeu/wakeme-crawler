from models import *
from bs4 import BeautifulSoup
from urlparse import urlparse
from types import *
from lepl.apps.rfc3696 import HttpUrl
import urllib2
import logging

log = logging.getLogger('extractor')
log.addHandler(logging.StreamHandler())
log.handlers[0].setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
log.setLevel(logging.DEBUG)

class Extractor:		

	def __init__(self, source, host):
		self.source = source
		self.host = self.checkHost(host)
	

	def init(self):
		htmlPage = urllib2.urlopen(self.source.url)
		domObjects = BeautifulSoup(htmlPage)

		log.debug("HOST =>" + self.host)

		validator = HttpUrl()

		for linkObject in domObjects.findAll('a'):
			url = self.checkURL(linkObject.get("href"))			
			if validator(url):					
				try:
					Link(url=url, source=self.source).save()
					log.debug("Saving Link => " + url)						
				except Exception, e:
					log.debug("Link already saved")
				

	def checkURL(self, url):

		if type(url) is NoneType:
			return ""

		if url.find("#") == 0:
			return ""

		if not self.host in url:
			return ""

		if url.find("/") == 0:
			return "http://"+self.host+"/"+url

		return url

	def checkHost(self, host):
		return host.replace("www.","")		
		