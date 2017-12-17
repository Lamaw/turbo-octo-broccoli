from crypto_bot import CryptoBot

def test_bittrex():
	pairs = list()
	pairs.append(("btc","eth"))
	pairs.append(("btc","ltc"))
	pairs.append(("eth","ltc"))
	bot = CryptoBot('bittrex',pairs)
	return bot.loop(10,False)

def test_poloniex():
	pairs = list()
	pairs.append(("btc","eth"))
	pairs.append(("btc","etc"))
	pairs.append(("eth","etc"))
	bot = CryptoBot('poloniex',pairs)
	return bot.loop(10,False)

print "Test Bittrex :", test_bittrex()
print "Test Poloniex :", test_poloniex()