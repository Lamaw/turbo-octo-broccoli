import datetime
import sys
import threading
import json

from exchange import Bittrex, Poloniex, Bitfinex
from processor import Processor
import constants


class CryptoBot(threading.Thread):
	"""The main instance, managing the whole process"""
	def __init__(self, exchange, pairs, chain=None):
		super(CryptoBot, self).__init__()
		self.nb_assessed_chains=0
		self.nb_profitable_tx=0
		self.exchange = self.create_exchange(exchange)
		self.processor = Processor()
		if chain and len(chain) == 3:
			self.pairs = self.exchange.make_pairs(chain)
		else:
			self.pairs = pairs

		self.id="["+exchange.upper()+" : "+self.pairs[0][0]+"-"+self.pairs[2][0]+"-"+self.pairs[1][1]+"]"

	def create_exchange(self, name):
		try:
			classname = constants.SUPPORTED_EXCHANGES[name]
			if classname:
				get_class = lambda x: globals()[x]
				return get_class(classname)()
		except Exception as e:
			exchange_list =""
			for key in constants.SUPPORTED_EXCHANGES:
				exchange_list += key + " - " 
			raise ValueError("\nExchange name should be one of these : " + exchange_list)

	def run(self):
		self.loop(10)

	def loop(self, cycles=None, trace=True):
		stop = False
		looped = 0
		try:
			while (not stop):
				tickers = self.exchange.get_tickers_for_pairs(self.pairs)
				self.nb_assessed_chains+=1
				profit = self.processor.is_profitable(self.pairs, tickers, self.exchange.market_fee)
				if profit:
					self.nb_profitable_tx+=1
					if trace:
						print self.id, "Found one transaction profitable for", self.processor.get_profitability() , "%. It is the", self.nb_profitable_tx,"th since the beginning."
				elif trace:
					print self.id, self.nb_assessed_chains , "unprofitable chain assessed. (gain : ", self.processor.get_profitability()-1, "%)"
				looped+=1
				if cycles and (looped >= cycles):
					stop=True
			return True
		except  Exception as e:
			return False

##########  MAIN  ##############

if __name__ == "__main__":
	exchange = sys.argv[1]
	if len(sys.argv) is 5: # cmd line of the form : python crypto_bot.py {exchange} {crypto1} {crypto2} {crypto3}
		pairs = list()
		pairs.append((sys.argv[2],sys.argv[3]))
		pairs.append((sys.argv[2],sys.argv[4]))
		pairs.append((sys.argv[3],sys.argv[4]))
		chain = list()
		chain.append(sys.argv[2])
		chain.append(sys.argv[3])
		chain.append(sys.argv[4])
		bot = CryptoBot(exchange, pairs, chain)
		bot.loop()

	elif len(sys.argv) is 2: # cmd line of the form : python crypto_bot.py {exchange}
		bots = list()
		with open(constants.CONF_FILE) as json_data:
			data = json.load(json_data)
			json_data.close()
		chain_dict = data['CHAINS_TO_WORK_ON']
		for chain in chain_dict:
			pairs = list()
			pairs.append((chain[0],chain[1]))
			pairs.append((chain[0],chain[2]))
			pairs.append((chain[1],chain[2]))
			print pairs
			bot = CryptoBot(exchange, pairs)
			bots.append(bot)
		for bot in bots:
			bot.start()

	else:
		print "Wrong arguments"
