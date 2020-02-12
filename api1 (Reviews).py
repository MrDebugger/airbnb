import requests,json

def pprint(j):
	print(json.dumps(j,indent=4))


head={"Accept":'application/json','Accept-Encoding':'gzip, deflate','User-Agent':'Airbnb/16.41 iPhone/10.0.3 Type/Phone','X-Airbnb-API-Key':"d306zoyjsyarp7ifhu67rjxn52tv0t20",'X-Airbnb-Currency':"USD","X-Airbnb-Locale":"en","X-Airbnb-Network-Type":"wifi"}
for id_ in open("ids.txt").read().splitlines():
# for id_ in ["11996314"]:
	#lisiting details api
	# resp=requests.get(f'https://api.airbnb.com/v2/pdp_listing_details/{id_}?_format=for_native&tier_override=0',headers=head).json()
	# print(json.dumps(resp["pdp_listing_detail"] ,indent=4))

	reviews = {}
	# #reviews api
	resp=requests.get(f'https://api.airbnb.com/v2/homes_pdp_reviews?_format=for_mobile_client&listing_id={id_}&role=all&limit=1000&offset=0',headers=head).json()
	for review in resp['reviews']:
		year = review["localized_date"].split(" ")[-1]
		if reviews.get(year):
			reviews[year] += 1
		else:
			reviews[year] = 1

	print("Total Reviews:", resp["metadata"]["reviews_count"])
	print("Reviews in 19:",reviews.get('2019',0))
	print("Reviews in 18:",reviews.get('2018',0))
	# #rooms availibility
	# resp=requests.get(f'https://api.airbnb.com/v2/calendar_months?_format=with_conditions&count=12&listing_id={id_}&month=1&year=2020',headers=head).json()
	# # print(resp)


	print()

