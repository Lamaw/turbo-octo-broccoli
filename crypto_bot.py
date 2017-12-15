from exchange import Bittrex, Poloniex
from processor import Processor
import datetime
import sys


class CryptoBot(object):
	"""The main instance, managing the whole process"""
	def __init__(self, exchange, pairs):
		super(CryptoBot, self).__init__()
		self.pairs = pairs
		self.nb_assessed_chains=0
		self.nb_profitable_tx=0
		self.exchange = self.create_exchange(exchange)
		self.processor = Processor()
		if self.pairs is None:
			self.get_pairs_from_conf()

	def create_exchange(self, name):
		if (name == 'bittrex'):
			return Bittrex()
		if (name == 'poloniex'):
			return Poloniex()
		return None

	def get_pairs_from_conf(self):
		pass

	def loop(self):
		stop = False
		while (not stop):
			tickers = self.exchange.get_tickers_for_pairs(self.pairs)
			self.nb_assessed_chains+=1
			profit = self.processor.is_profitable(self.pairs, tickers, self.exchange.market_fee)
			if profit:
				self.nb_profitable_tx+=1
				print "Found one transaction profitable for", self.processor.get_profitability(profit) , "%%. It is the", self.nb_profitable_tx,"th since the beginning."
			else:
				print self.nb_assessed_chains , "unprofitable chain assessed."


##########  MAIN  ##############

if __name__ == "__main__":
	exchange = sys.argv[1]
	if len(sys.argv) is 5: # cmd line of the form : python crypto_bot.py {exchange} {crypto1} {crypto2} {crypto3}
		pairs = list()
		pairs.append((sys.argv[2],sys.argv[3]))
		pairs.append((sys.argv[2],sys.argv[4]))
		pairs.append((sys.argv[3],sys.argv[4]))
		_bot = CryptoBot(exchange, pairs)
		_bot.loop()

	elif len(sys.argv) is 2: # cmd line of the form : python crypto_bot.py {exchange}
		pairs = None
		_bot = CryptoBot(exchange, pairs)
		_bot.loop

	else:
		print "Wrong arguments"
