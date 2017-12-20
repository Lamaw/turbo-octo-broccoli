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
					"poloniex":"Poloniex"
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

POLONIEX_SPECIFIC_NAME = {
				"xlm":"str"
}

### BITFINEX CONFIGURATION ###

BITFINEX_SPECIFIC_NAME = {
				"dash":"dsh",
				"qtum":"qtm"
}