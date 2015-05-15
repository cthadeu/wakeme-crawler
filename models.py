from mongoengine import *

class Source(Document):
	
	NEW=0
	MINING=1
	MINED=2
	
	name 	= StringField(required=True)
	url 	= URLField(unique=True)
	status 	= IntField()
	rules 	= ListField(StringField(max_length=250))	

class Link(Document):	
	
	NEW=0
	EXTRACTING=1
	EXTRACTED=2
	
	url 	= StringField(required=True, unique=True)
	status 	= IntField()
	source 	= ReferenceField('Source', required=True)

	@staticmethod
	def exists(link):
		return Link.objects(url=link).count() > 0		
	
	@staticmethod
	def findLinksBySource(source):
		return Links.objects(source=source)

	
class News(Document):
	content = StringField(required=True)
	link 	= StringField()