class Miner:
	
	def __init__(self, source):
		self.source = source
	
	def start(self):
		links = Link.findLinksBySource(self.source)
		return links
		
		
		