import requests,json
from openpyxl import Workbook
book = Workbook()
sheet = book.active
sheet.append(['ID','LISTING ID','URL','TRAVELLERS','ROOMS','BEDS','BATHROOMS','LATITUDE','LONGITUDE','MINIMUM NIGHTS','TOTAL REVIEWS','REVIEWS IN 2019','REVIEWS IN 2018','MOST RECENT REVIEW DATE','AVERAGE SCORE','AVERAGE PRICE','AVAILABLE DAYS (JANUARY 2020)','AVAILABLE DAYS (FEBRUARY 2020)','AVAILABLE DAYS (MARCH 2020)','AVAILABLE DAYS (APRIL 2020)','AVAILABLE DAYS (JUNE 2020)','AVAILABLE DAYS (JULY 2020)','AVAILABLE DAYS (AUGUST 2020)','AVAILABLE DAYS (SEPTEMBER 2020)','AVAILABLE DAYS (OCTOBER 2020)','AVAILABLE DAYS (NOVEMBER 2020)','AVAILABLE DAYS (DECEMBER 2020)','AVERAGE PRICE (JANUARY 2020)','AVERAGE PRICE (FEBRUARY 2020)','AVERAGE PRICE (MARCH 2020)','AVERAGE PRICE (APRIL 2020)','AVERAGE PRICE (MAY 2020)','AVERAGE PRICE (JUNE 2020)','AVERAGE PRICE (JULY 2020)','AVERAGE PRICE (AUGUST 2020)','AVERAGE PRICE (SEPTEMBER 2020)','AVERAGE PRICE (OCTOBER 2020)','AVERAGE PRICE (NOVEMBER 2020)','AVERAGE PRICE (DECEMBER 2020)'])
head={"Accept":'application/json','Accept-Encoding':'gzip, deflate','User-Agent':'Airbnb/16.41 iPhone/10.0.3 Type/Phone','X-Airbnb-API-Key':"d306zoyjsyarp7ifhu67rjxn52tv0t20",'X-Airbnb-Currency':"EUR","X-Airbnb-Locale":"fr","X-Airbnb-Network-Type":"wifi"}
index = 1
def scrap(id_):
	global index
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
	totalRev = 0
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
	revs = {rev["id"]:rev["created_at"] for rev in details['sorted_reviews']}
	avrRate = details['reviews_module']['localized_overall_rating']
	print("URL:",url)
	try:
		recentRev =  revs.get(max(revs.keys()))
	except:
		recentRev =  None

	reviews = {}
	# #reviews api
	resp=requests.get(f'https://api.airbnb.com/v2/homes_pdp_reviews?_format=for_mobile_client&listing_id={id_}&role=all&limit=1000&offset=0',headers=head).json()
	for review in resp['reviews']:
		year = review["localized_date"].split(" ")[-1]
		if reviews.get(year):
			reviews[year] += 1
		else:
			reviews[year] = 1
	totalRev = resp["metadata"]["reviews_count"]

	avlDays = {}
	prices = {}
	resp=requests.get(f'https://api.airbnb.com/v2/calendar_months?_format=with_conditions&count=12&listing_id={id_}&year=2020',headers=head).json()
	for month in resp["calendar_months"]:
		mName = month['name']
		avlDays[mName] = 0
		prices[mName] = []
		for day in month['days']:
			if day['available']:
				avlDays[mName] += 1
			prices[mName].append(day['price']['local_price'])
		prices[mName] = round(sum(prices[mName])/(len(prices[mName]) if prices[mName] else 1),2)
	avrPrice = round(sum(prices.values())/len(prices.values()),2)
	row = [index,id_,url,travellers,rooms,beds,bathrooms,lat,lng,minNights,totalRev,reviews.get('2019',0),reviews.get('2018',0),recentRev,avrRate,avrPrice]
	row.extend(list(avlDays.values()))
	row.extend(list(prices.values()))
	sheet.append(row)
	index += 1
	print()
for id_ in open("ids.txt").read().splitlines():
	try:
		scrap(id_)
	except:
		print(id_,"Failed to Load========")
		with open('errors.txt','a') as f:
				f.write(id_+'\n')  
	if index%100==0:
		book.save("Rooms.xlsx")
book.save("Rooms.xlsx")