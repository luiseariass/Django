from django.http import HttpResponse

# Orderbook bitfinex prueba
def bitfinex_orderbook_btcusd(requisito):
	import requests, urllib.request, numpy
	price= []
	amount= []
	respuesta= []
	request=requests.get('https://api.bitfinex.com/v1/book/BTCUSD')
	request_json=request.json()
	
	if requisito==1:
		for i in range(0,25):
			price.append(request_json['bids'][i]['price'])
			amount.append(request_json['bids'][i]['amount'])
			respuesta.append([float(price[i]),float(amount[i])])
	elif requisito==-1:
		for i in range(0,25):
			price.append(request_json['asks'][i]['price'])
			amount.append(request_json['asks'][i]['amount'])
			respuesta.append([float(price[i]),float(amount[i])])

	return(respuesta)
def bitfinex_orderbook_dshusd(requisito):
	import requests, urllib.request, numpy
	price= []
	amount= []
	respuesta= []
	request=requests.get('https://api.bitfinex.com/v1/book/dshusd')
	request_json=request.json()
	
	if requisito==1:
		for i in range(0,25):
			price.append(request_json['bids'][i]['price'])
			amount.append(request_json['bids'][i]['amount'])
			respuesta.append([float(price[i]),float(amount[i])])
	elif requisito==-1:
		for i in range(0,25):
			price.append(request_json['asks'][i]['price'])
			amount.append(request_json['asks'][i]['amount'])
			respuesta.append([float(price[i]),float(amount[i])])

	return(respuesta)	
def bitfinex_orderbook_dshbtc(requisito):
	import requests, urllib.request, numpy
	price= []
	amount= []
	respuesta= []
	request=requests.get('https://api.bitfinex.com/v1/book/dshbtc')
	request_json=request.json()
	
	if requisito==1:
		for i in range(0,25):
			price.append(request_json['bids'][i]['price'])
			amount.append(request_json['bids'][i]['amount'])
			respuesta.append([float(price[i]),float(amount[i])])
	elif requisito==-1:
		for i in range(0,25):
			price.append(request_json['asks'][i]['price'])
			amount.append(request_json['asks'][i]['amount'])
			respuesta.append([float(price[i]),float(amount[i])])

	return(respuesta)		

#Ticker bitfinex prueba	
def bitfinex_ticker_btcusd():
	import requests, urllib.request
	import tabulate
	import time
	import numpy 


	request=requests.get('https://api.bitfinex.com/v1/pubticker/BTCUSD')
	request_json=request.json()
	last_price=request_json["last_price"]
	return(float(last_price))
def bitfinex_ticker_dshusd():
	import requests, urllib.request
	import tabulate
	import time
	import numpy 


	request=requests.get('https://api.bitfinex.com/v1/pubticker/dshusd')
	request_json=request.json()
	last_price=request_json["last_price"]
	return(float(last_price))
def bitfinex_ticker_dshbtc():
	import requests, urllib.request
	import tabulate
	import time
	import numpy 


	request=requests.get('https://api.bitfinex.com/v1/pubticker/dshbtc')
	request_json=request.json()
	last_price=request_json["last_price"]
	return(float(last_price))

def index(request):
	lp_btcusd=bitfinex_ticker_btcusd()
	lp_dshbtc=bitfinex_ticker_dshbtc()
	lp_dshusd=bitfinex_ticker_dshusd()
	resultado=("El precio del BTCUSD en bitfinex es de %08.2f \n El precio del DSHUSD en bitfinex es de %05.2f \n El precio del DSHBTC en bitfinex es de %08.7f \n ")	%(lp_btcusd,lp_dshusd,lp_dshbtc)
	return HttpResponse(resultado)
