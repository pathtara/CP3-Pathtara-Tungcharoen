from googlefinance import getQuotes
import json
json.dumps(getQuotes('PPT'), indent=2)

