from mongoengine import connect
import unittest
from models import *
from extractor import *

class TextExtractor(unittest.TestCase):
	
	def setUp(self):
		connect('crawler', host='mongodb://localhost/crawler')
	
	def test_should_extract_links_from_source(self):
		s = Source.objects().first()		
		Extractor(s).init()