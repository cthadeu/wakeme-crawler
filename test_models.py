from mongoengine import connect
import unittest
from models import *

class TestSourceModel(unittest.TestCase):
	
	def setUp(self):
		connect('crawler', host='mongodb://localhost/crawler')
	
	
	def test_should_create_new_source_with_rules(self):
		saved_source = Source(name="Globo.com", 
							url="http://www.globo.com", 
							status=Source.NEW,  
							rules=["div.materia-titulo > h1"]).save()
		self.assertIsNotNone(saved_source)
							
	def test_should_create_new_link_with_source(self):
		globo_source = Source.objects.first()
		
		saved_link = Link(url="http://g1.globo.com/fantastico/noticia/2015/05/fotos-podem-esclarecer-queda-de-helicoptero-com-thomaz-alckmin.html",
						  status=Link.NEW, 
						  source=globo_source).save()
		self.assertIsNotNone(saved_link)

	def test_should_get_mined_urls_from_given_source(self):
		globo_source = Source.objects.first()
		links = Link.findLinksBySource(globo_source)
		self.assertTrue(len(links) > 0)
		