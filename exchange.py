import requests
import json
class Exchange(object):
	"""docstring for Exchange"""
	def __init__(self):
		super(Exchange, self).__init__()


	def get(self, url):
		return requests.get(url)

class Bittrex(Exchange):
	def __init__(self):
		super(Bittrex, self).__init__()
		self.market_fee=0.0025

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
		self.market_fee=0.0025


	def get_tickers_for_pairs(self, pairs):
		tickers = dict()
		url = "https://poloniex.com/public?command=returnTicker"
		resp = self.get(url)
		for pair in pairs:
			tickers[pair]= self._get_ticker(resp, pair)

		print tickers
		
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
		self.market_fee=0.0025

	def get_tickers_for_pairs(self, pairs):
		pass
		# tickers = dict()
		# url = "https://poloniex.com/public?command=returnTicker"
		# resp = self.get(url)
		# for pair in pairs:
		# 	tickers[pair]= self._get_ticker(resp, pair)

		# print tickers
		
		# return tickers

	def _get_ticker(self, http_resp, pair):
		pass
		# json_object = json.loads(http_resp.text)
		# try:
		# 	str_pair = pair[0].upper() + "_" + pair[1].upper()
		# 	return (json_object[str_pair]["highestBid"], json_object[str_pair]["lowestAsk"])
		# except Exception as e:
		# 	return None