from mongoengine import connect
import unittest
from models import *
from extractor import *
from urlparse import urlparse

class TestMiner(unittest.TestCase):
	
	def setUp(self):
		connect('crawler', host='mongodb://localhost/crawler')
	
	def test_should_extract_links_from_source(self):
		s = Source.objects().first()		
		parsedURL = urlparse(s.url)
		Extractor(source=s, host=parsedURL.netloc).init()