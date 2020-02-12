import requests,json

head={"Accept":'application/json','Accept-Encoding':'gzip, deflate','User-Agent':'Airbnb/16.41 iPhone/10.0.3 Type/Phone','X-Airbnb-API-Key':"d306zoyjsyarp7ifhu67rjxn52tv0t20",'X-Airbnb-Currency':"USD","X-Airbnb-Locale":"fr","X-Airbnb-Network-Type":"wifi"}
for id_ in open("ids.txt").read().splitlines():
# for id_ in ["11996314"]:
	url = "https://www.airbnb.fr/rooms/"+id_
	travellers = 0
	rooms = 0
	beds = 0
	bathrooms = 0
	lat = 0
	lng = 0
	minNights = 0
	recentRev = ''
	avrRate = ''
	#lisiting details api
	resp=requests.get(f'https://api.airbnb.com/v2/pdp_listing_details/{id_}?_format=for_rooms_show&tier_override=0',headers=head).json()
	# print(json.dumps(resp["pdp_listing_detail"] ,indent=4))
	details = resp["pdp_listing_detail"]
	beds = details["bed_label"].split()[0]
	rooms = details["bedroom_label"].split()[0] if not details["bedroom_label"].split()[0].isalpha() else '0'
	travellers = details["guest_label"].split()[0]
	bathrooms = details["bathroom_label"].split()[0]
	lat = details['lat']
	lng = details['lng']
	minNights = details['min_nights']
	totalRev = details["review_details_interface"].get("review_count")
	revs = {rev["id"]:rev["created_at"] for rev in details['sorted_reviews']}
	avrRate = details['reviews_module']['localized_overall_rating']
	# #reviews api
	# resp=requests.get(f'https://api.airbnb.com/v2/homes_pdp_reviews?_format=for_mobile_client&listing_id={id_}&role=all&limit=1000&offset=0',headers=head).json()
	# # print(resp)

	# #rooms availibility
	# resp=requests.get(f'https://api.airbnb.com/v2/calendar_months?_format=with_conditions&count=12&listing_id={id_}&month=1&year=2020',headers=head).json()
	# # print(resp)

	print("URL:",url)
	print("Beds:", beds)
	print("Rooms:", rooms)
	print("Travellers:", travellers)
	print("Bathrooms:", bathrooms)
	print("Latitude:", lat)
	print("Longitude:", lng)
	print("Longitude:", lng)
	print("Minimum Nights:", minNights)
	print("Average Score:", avrRate)
	print()
	print(revs.get(max(revs.keys())))
	break