### GENERAL CONFIGURATION ###

CONF_FILE='conf.json'

SUPPORTED_CURRENCIES={
						"ada":"Ada",
						"adt":"AdToken",
						"adx":"AdEx",
						"ant":"Aragon",
						"avt":"Aventus",
						"bat":"Basic Attention Token",
						"bch":"Bitcoin Cash",
						"bcn":"Bytecoin",
						"blk":"BlackCoin",
						"bnt":"Bancor",
						"btc":"Bitcoin",
						"btcd":"BitcoinDark",
						"btg":"Bitcoin Gold",
						"cfi":"Cofound.it",
						"crb":"CreditBit",
						"cvc":"Civic",
						"dash":"Dash",
						"dgb":"Digibyte",
						"dgd":"DigixDAO",
						"dnt":"District0x",
						"edo":"Eidoo",
						"eng":"Enigma",
						"eos":"EOS",
						"etc":"Ethereum Classic",
						"eth":"Ethereum",
						"etp":"Metaverse ETP",
						"fct":"Factom",
						"fun":"FunFair",
						"gas":"Gas",
						"gno":"Gnosis",
						"gnt":"Golem",
						"gup":"Guppy",
						"hmq":"Humaniq",
						"iot":"Iota",
						"lgd":"Legends",
						"lsk":"Lisk",
						"ltc":"Litecoin",
						"lun":"Lunyr",
						"maid":"MaidSafeCoin",
						"mana":"Decentraland",
						"myst":"Mysterium",
						"mco":"Monaco",
						"mtl":"Metal",
						"neo":"Neo",
						"nmr":"Numeraire",
						"nxt":"nxt",
						"omg":"OmiseGo",
						"pay":"TenX Pay Token",
						"powr":"PowerLedger",
						"ptoy":"Patientory",
						"qsh":"Qash",
						"qrl":"Quantum Resistant Ledger",
						"qtum":"Qtum",
						"rcn":"Ripio Credit Network",
						"rep":"Augur",
						"rlc":"IEx.ec",
						"salt":"Salt",
						"san":"Santander",
						"sc":"Siacoin",
						"sngls":"SingularDTV",
						"snt":"Status Network Token",
						"storj":"Storj",
						"strat":"Stratis",
						"tix":"Blocktix",
						"trst":"Trustcoin",
						"usdt":"Tether",
						"vib":"Viberate",
						"waves":"Waves",
						"wings":"Wings DAO",
						"xem":"NewEconomyMovement",
						"xlm":"Lumen",
						"xmr":"Monero",
						"xrp":"Ripple",
						"yyw":"Yoyow",
						"zec":"Zcash",
						"zrx":"0x",
						"1st":"FirstBlood"
							}

SUPPORTED_EXCHANGES = {
					"bitfinex":"Bitfinex",
					"bittrex":"Bittrex",
					"poloniex":"Poloniex",
					"kraken":"Kraken"
					}

### BITTREX CONFIGURATION ###

BITTREX_SPECIFIC_NAMES = {
				"bch":"bcc"
}

BITTREX_REF_CURRENCIES = {
				"usdt":0,
				"btc":1,
				"eth":2
}

BITTREX_PAIRS = {
			("btc","eth"):[
							"ltc",
							"xrp",
							"bcc",
							"omg",
							"neo",
							"etc",
							"ada",
							"qtum",
							"xlm",
							"xem",
							"xmr",
							"dash",
							"zec",
							"waves",
							"btg",
							"mco",
							"pay",
							"salt",
							"strat",
							"bat",
							"ant",
							"cvc",
							"mana",
							"gnt",
							"ptoy",
							"bnt",
							"rlc",
							"powr",
							"sngls",
							"dgd",
							"snt",
							"sc",
							"adx",
							"trst",
							"cfi",
							"gup",
							"rcn",
							"storj",
							"rep",
							"dgb",
							"fun",
							"hmq",
							"mtl",
							"gno",
							"eng",
							"wings",
							"dnt",
							"fct",
							"nmr",
							"qrl",
							"tix",
							"myst",
							"lun",
							"vib",
							"crb",
							"lgb",
							"adt",
							"1st"
							],
			("usdt","btc"):[
							"ltc",
							"eth",
							"xrp",
							"bcc",
							"etc",
							"neo",
							"btg",
							"omg",
							"dash",
							"zec",
							"xmr"
							],
			("usdt","eth"):[
							"ltc",
							"xrp",
							"bcc",
							"etc",
							"neo",
							"btg",
							"omg",
							"dash",
							"zec",
							"xmr"
							]
}

### POLONIEX CONFIGURATION ###

POLONIEX_SPECIFIC_NAMES = {
				"xlm":"str"
}

POLONIEX_REF_CURRENCIES = {
				"usdt":0,
				"btc":1,
				"eth":2,
				"xmr":2
}

POLONIEX_PAIRS = {
			("btc","eth"):[
							"bch",
							"cvc",
							"etc",
							"gas",
							"gno",
							"gnt",
							"lsk",
							"omg",
							"steem",
							"zec",
							"zrx"
							],
			("btc","xrm"):[
							"bcn",
							"blk",
							"btcd",
							"dash",
							"ltc",
							"maid",
							"nxt",
							"zec"
							],
			("usdt","btc"):[
							"bch",
							"dash",
							"etc",
							"eth",
							"ltc",
							"nxt",
							"rep",
							"str",
							"xmr",
							"xrp",
							"zec"
							],
			("usdt","eth"):[
							"bch",
							"etc",
							"rep",
							"zec"
							],
			("usdt","xrm"):[
							"dash",
							"ltc",
							"nxt",
							"zec"
							]
			


}
### BITFINEX CONFIGURATION ###

BITFINEX_SPECIFIC_NAMES = {
				"dash":"dsh",
				"qtum":"qtm"
}

BITFINEX_REF_CURRENCIES = {
				"usd":0,
				"btc":1,
				"eth":2
}

BITFINEX_PAIRS = {
			("btc","eth"):[
							"iot",
							"eos",
							"san",
							"omg",
							"bch",
							"neo",
							"etp",
							"edo",
							"qtm",
							"avt",
							"qsh",
							"yyw"
							],
			("usd","btc"):[
							"ltc",
							"eth",
							"etc",
							"zec",
							"xmr",
							"dsh",
							"xrp",
							"iot",
							"eos",
							"san",
							"omg",
							"bch",
							"neo",
							"etp",
							"edo",
							"qtm",
							"avt",
							"btg",
							"qsh",
							"yyw"
							],
			("usd","eth"):[
							"iot",
							"eos",
							"san",
							"omg",
							"bch",
							"neo",
							"etp",
							"edo",
							"qtm",
							"avt",
							"qsh",
							"yyw"
							]
}
