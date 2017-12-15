import constants
import json

class Processor(object):
	"""docstring for Processor"""
	def __init__(self):
		super(Processor, self).__init__()
		self.last_profit=0
		self.exp_roi=self._read_expected_roi()
		self.market_fee=0
		self.target=0
		
	def is_profitable(self, pairs ,tickers, market_fee):
		if market_fee != self.market_fee:
			self.market_fee = market_fee
			self._get_target_number()
		try:
			res1 = float(tickers[pairs[0]][0]) * float(tickers[pairs[2]][0]) / float(tickers[pairs[1]][1])
			res2 = float(tickers[pairs[1]][0]) / (float(tickers[pairs[0]][1]) * float(tickers[pairs[2]][1]))
		except Exception as e:
			print "Error in profitability processing, could not read tickers values."
			return None
		if res1 > self.target:
			self.last_profit=res1
			return res1
		if res2 > self.target:
			self.last_profit=res2
			return res2
		return None

	def get_profitability(self, result):
		profit = ((result * (1-self.market_fee)**3) - 1)*100
		return profit

	def _read_expected_roi(self):
		with open(constants.CONF_FILE) as json_data:
			data = json.load(json_data)
			json_data.close()
		self.exp_roi = data['EXPECTED_ROI']

	def _get_target_number(self):
		self._read_expected_roi()
		self.target = (1/(1-self.market_fee)**3)*(1+float(self.exp_roi))