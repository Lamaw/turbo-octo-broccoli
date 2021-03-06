import datetime
import sys
import threading
import json
import logging

from exchange import Bittrex, Poloniex, Bitfinex, Kraken
from processor import Processor
from utils import BotLogger
import constants

class CryptoBot(threading.Thread, BotLogger):
	"""
	CryptoBot constructor: A CryptoBot is the main worker of the prokect.
	Given an exchange and 3 pair of chained currencies, it loops on
	the order book of these currencies until a favorable trade is detected.
	INPUTS: 
	exchange: 	string
	chain:      list(string)"""
	def __init__(self, exchange, chain=None):
		super(CryptoBot, self).__init__()
		file_name = exchange.upper()+"_"+chain[0]+"_"+chain[1]+"_"+chain[2]
		logging.basicConfig(level=logging.INFO,
					filename=file_name+".log", filemode='w',
					format='%(name)s %(levelname)s %(message)s')

		self.nb_unprofitable_chains=0
		self.nb_profitable_tx=0
		self.long_profitable=0
		self.exchange = self.create_exchange(exchange)
		self.processor = Processor()
		if chain and len(chain) == 3:
			self.pairs = self.exchange.make_pairs(chain)
		else:
			self.pairs = None

		self.id="["+exchange.upper()+" : "+self.pairs[0][0]+"-"+self.pairs[2][0]+"-"+self.pairs[1][1]+"]"


	"""
	Instanciate an Exchange object given an exchange name:
	INPUTS:
	name:     string"""
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


	"""
	Override the run() method of Tthreading.Thread class
	this method is used to launch the main working method (loop() )
	in a new thread, in order to make several bots work in parallel"""
	def run(self):
		self.loop(10)

	"""
	Main working method, it keeps reading the order book of given pairs of currencies
	and analyse opportunities to make profitable trades
	INPUTS:
	[OPT]cycles:     int        => a number of loop to do before stoping. (default: endless)
	[OPT]trace:      boolean    => should traces be printed (default: True)"""
	def loop(self, cycles=None, trace=True):
		stop = False
		looped = 0
		nb_last_tx_profitable=0
		consecutive_profitable=list()
		try:
			while (not stop):
				tickers = self.exchange.get_tickers_for_pairs(self.pairs)
				profit = self.processor.is_profitable(self.pairs, tickers, self.exchange.market_fee)
				if profit:
					self.nb_profitable_tx+=1
					if trace:
						msg = self.id, "Found one transaction profitable for", self.processor.get_profitability() , "%. It is the", self.nb_profitable_tx,"th since the beginning."
						self.logger.info(msg)

					nb_last_tx_profitable+=1
				else:
					self.nb_unprofitable_chains+=1
					if nb_last_tx_profitable > 0:
						consecutive_profitable.append(nb_last_tx_profitable)
					nb_last_tx_profitable =0
					if trace:	
						msg = self.id, self.nb_unprofitable_chains , "unprofitable chain assessed. (gain : ", self.processor.get_profitability()-1, "%)"
						self.logger.info(msg)

				msg = self.id, self.nb_unprofitable_chains + self.nb_profitable_tx , "chains assessed : ", self.nb_profitable_tx , "were profitable => here is a list of number of consecutive profitable transaction", consecutive_profitable
				self.logger.info(msg)
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
		chain = list()
		chain.append(sys.argv[2])
		chain.append(sys.argv[3])
		chain.append(sys.argv[4])
		bot = CryptoBot(exchange, chain)
		bot.loop()
	else:
		print "Wrong arguments => USAGE : python crypto_bot.py {exchange} {crypto1} {crypto2} {crypto3}"
