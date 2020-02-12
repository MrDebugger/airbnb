import requests,json

def pprint(j):
	print(json.dumps(j,indent=4))


head={"Accept":'application/json','Accept-Encoding':'gzip, deflate','User-Agent':'Airbnb/16.41 iPhone/10.0.3 Type/Phone','X-Airbnb-API-Key':"d306zoyjsyarp7ifhu67rjxn52tv0t20",'X-Airbnb-Currency':"USD","X-Airbnb-Locale":"en","X-Airbnb-Network-Type":"wifi"}
# for id_ in open("ids.txt").read().splitlines():
for id_ in ["33107915"]:
	#lisiting details api
	# resp=requests.get(f'https://api.airbnb.com/v2/pdp_listing_details/{id_}?_format=for_native&tier_override=0',headers=head).json()
	# print(json.dumps(resp["pdp_listing_detail"] ,indent=4))

	# #reviews api
	# resp=requests.get(f'https://api.airbnb.com/v2/homes_pdp_reviews?_format=for_mobile_client&listing_id={id_}&role=all&limit=1000&offset=0',headers=head).json()
	# pprint(resp)
	
	# #rooms availibility
	avlDays = {}
	prices = {}
	resp=requests.get(f'https://api.airbnb.com/v2/calendar_months?_format=with_conditions&count=12&listing_id={id_}&year=2020',headers=head).json()
	# pprint(resp["calendar_months"][2])
	for month in resp["calendar_months"]:

		mName = month['name']
		avlDays[mName] = 0
		prices[mName] = []
		for day in month['days']:
			if not int(day["date"].split('-')[1]) == resp["calendar_months"].index(month)+1:
				continue
			if day['available']:
				avlDays[mName] += 1
			prices[mName].append(day['price']['local_price'])
		prices[mName] = round(sum(prices[mName])/(len(prices[mName]) if prices[mName] else 1),2)
	print(avlDays)
	print(prices)
	break

