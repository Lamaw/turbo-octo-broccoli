import logging

class BotLogger(object):
	@property
	def logger(self):
		name = '.'.join([__name__, self.__class__.__name__])
		return logging.getLogger(name)