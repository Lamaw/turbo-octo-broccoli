import requests
import json
import constants

class Exchange(object):
	"""docstring for Exchange"""
	def __init__(self):
		super(Exchange, self).__init__()


	def get(self, url):
		return requests.get(url)

	def make_pairs(self, chain):
		pairs = list()
		ref_pair = list()
		chain = self._check_specific_name(chain)
		for i in xrange(len(self.reference_currencies)):
			for ref_cur, ind in self.reference_currencies.iteritems():
				if ind == i and ref_cur in chain:
					ref_pair.append(ref_cur)
					break
			if len(ref_pair) == 2:
				break

		if len(ref_pair) != 2:
			str_currencies = ""
			for c in self.reference_currencies:
				str_currencies += c + " -- "
			raise ValueError("\nOne or more of the reference currencies could not be found, make sure there are at least two of these currencies in your chain : " + str_currencies)
			
		ref_pair = tuple(ref_pair)

		if ref_pair in self.pairs:
			for cur in chain:
				if cur in self.pairs[ref_pair]:
					pairs = self._create_pairs(ref_pair, cur)
		
		if pairs:
			return pairs
		else:
			raise ValueError("The currency chain " + str(chain) + " could not be found for " + self.name)

	def _create_pairs(self, ref_pair, currency):
		pairs = list()
		pairs.append((ref_pair[0],ref_pair[1]))
		pairs.append((ref_pair[0],currency))
		pairs.append((ref_pair[1],currency))
		return pairs

	def _check_specific_name(self, chain):
		new_chain = list()
		for cur in chain:
			if cur in self.specific_names:
				new_chain.append(self.specific_names[cur])
			else:
				new_chain.append(cur)
		return new_chain


class Bittrex(Exchange):
	def __init__(self):
		super(Bittrex, self).__init__()
		self.name = "Bittrex"
		self.market_fee=0.0025
		self.specific_names = constants.BITTREX_SPECIFIC_NAMES
		self.reference_currencies = constants.BITTREX_REF_CURRENCIES
		self.pairs = constants.BITTREX_PAIRS

	def get_tickers_for_pairs(self, pairs):
		tickers = dict()
		for pair in pairs:
			url = "https://bittrex.com/api/v1.1/public/getticker?market=" + pair[0] + "-" + pair[1]
			tickers[pair]= self._get_ticker(self.get(url))
		return tickers

	def _get_ticker(self, http_resp):
		json_object = json.loads(http_resp.text)
		try:
			return (json_object["result"]["Bid"], json_object["result"]["Ask"])
		except Exception as e:
			return None

class Poloniex(Exchange):
	def __init__(self):
		super(Poloniex, self).__init__()
		self.name = "Poloniex"
		self.market_fee=0.0025
		self.specific_names = constants.POLONIEX_SPECIFIC_NAMES
		self.reference_currencies = constants.POLONIEX_REF_CURRENCIES
		self.pairs = constants.POLONIEX_PAIRS


	def get_tickers_for_pairs(self, pairs):
		tickers = dict()
		url = "https://poloniex.com/public?command=returnTicker"
		resp = self.get(url)
		for pair in pairs:
			tickers[pair]= self._get_ticker(resp, pair)
		return tickers

	def _get_ticker(self, http_resp, pair):
		json_object = json.loads(http_resp.text)
		try:
			str_pair = pair[0].upper() + "_" + pair[1].upper()
			return (json_object[str_pair]["highestBid"], json_object[str_pair]["lowestAsk"])
		except Exception as e:
			return None


class Bitfinex(Exchange):
	def __init__(self):
		super(Bitfinex, self).__init__()
		self.name = "Bitfinex"
		self.market_fee=0.002
		self.specific_names = constants.BITFINEX_SPECIFIC_NAMES
		self.reference_currencies = constants.BITFINEX_REF_CURRENCIES
		self.pairs = constants.BITFINEX_PAIRS


	def get_tickers_for_pairs(self, pairs):
		tickers = dict()
		for pair in pairs:
			url = "https://api.bitfinex.com/v1/book/" + pair[1] + pair[0] + "?limit_bids=1&limit_asks=1"
			tickers[pair]= self._get_ticker(self.get(url))
		return tickers

	def _get_ticker(self, http_resp):
		json_object = json.loads(http_resp.text)
		try:
			return (json_object["bids"][0]["price"], json_object["asks"][0]["price"])
		except Exception as e:
			return None