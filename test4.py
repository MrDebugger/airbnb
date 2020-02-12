import requests,json

headers = {
    'authority': 'www.airbnb.fr',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-csrf-token': 'V4$.airbnb.fr$57iQ2sw3mI8$V_4QjFwkV65hkm4utfDMzeb1WF4rBHXOJOcQvjvPjnA=',
    'x-requested-with': 'XMLHttpRequest',
    'x-csrf-without-token': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.airbnb.fr/s/corfou-greece/homes?refinement_paths%5B%5D=%2Fhomes&current_tab_id=home_tab&selected_tab_id=home_tab&search_type=pagination&screen_size=large&place_id=ChIJ-eybj9ZNWxMRRMWtTGMS40U&click_referer=t%3ASEE_ALL%7Csid%3A7f269da3-35e4-4622-b211-852319978fa3%7Cst%3AMAGAZINE_HOMES&title_type=MAGAZINE_HOMES&hide_dates_and_guests_filters=false&s_tag=c0eJFIN9&section_offset=5&items_offset=18&last_search_session_id=77b54f1a-0eb2-4152-bd6c-41164b55c144',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'bev=1579542606_sYy%2FN9jc6dhFAFz0; jitney_client_session_id=17f5a172-86f0-4821-afa9-d840a390165a; jitney_client_session_created_at=1579542606; cdn_exp_18481319c2a05a012=treatment; cdn_exp_0c334cfc9a3f42bca=control; cfrmfctr=DESKTOP; cbkp=3; _ga=GA1.2.373531986.1579542618; _gid=GA1.2.1757812010.1579542618; __ssid=5d8e4e3a5ef1f5b25fc94328345d07d; _gcl_au=1.1.1912483831.1579542624; fbs=not_authorized; OptanonAlertBoxClosed=2020-01-20T17:51:47.098Z; cdn_exp_f6632ab691b5e6351=control; 016951b48=control; cdn_exp_62a1d4bf423854e1e=control; sdid=; _csrf_token=V4%24.airbnb.fr%2457iQ2sw3mI8%24V_4QjFwkV65hkm4utfDMzeb1WF4rBHXOJOcQvjvPjnA%3D; _airbed_session_id=a6e0735f6f5cb4144b4973e29c74c640; __svt=398; _user_attributes=%7B%22curr%22%3A%22EUR%22%2C%22guest_exchange%22%3A0.90167%2C%22device_profiling_session_id%22%3A%221579542606--d2ab74535799410b8782620d%22%2C%22giftcard_profiling_session_id%22%3A%221579546267--2e8d30ee30cddb5ceea98a7b%22%2C%22reservation_profiling_session_id%22%3A%221579546267--3c31669ad9591171e2a1d439%22%7D; AMP_TOKEN=%24NOT_FOUND; OptanonConsent=landingPath=NotLandingPage&datestamp=Mon+Jan+20+2020+23%3A51%3A16+GMT%2B0500+(Pakistan+Standard+Time)&version=4.6.0&groups=0_179751%3A1%2C1%3A1%2C2%3A1%2C0_183217%3A1%2C3%3A1%2C0_183345%3A1%2C0_183219%3A1%2C4%3A1%2C0_183240%3A1%2C0_179739%3A1%2C0_179743%3A1%2C0_185813%3A1%2C0_183096%3A1%2C0_179755%3A1%2C0_183215%3A1%2C0_185808%3A1%2C0_179747%3A1%2C0_179740%3A1%2C0_179744%3A1%2C0_185810%3A1%2C0_185814%3A1%2C0_183097%3A1%2C0_179756%3A1%2C0_183216%3A1%2C0_183344%3A1%2C0_185809%3A1%2C0_179748%3A1%2C0_179752%3A1%2C0_183241%3A1%2C0_179741%3A1%2C0_183098%3A1%2C0_179745%3A1%2C0_183346%3A1%2C0_185811%3A1%2C0_179737%3A1%2C0_185815%3A1%2C0_179757%3A1%2C0_179749%3A1%2C0_179753%3A1%2C0_185831%3A1%2C0_183099%3A1%2C0_179738%3A1%2C0_179742%3A1%2C0_183095%3A1%2C0_185816%3A1%2C0_183243%3A1%2C0_179754%3A1%2C0_183214%3A1%2C0_179750%3A1&AwaitingReconsent=false; flags=268697600; jitney_client_session_updated_at=1579546296',
}

params = (
    ('_format', 'for_explore_search_web'),
    ('auto_ib', 'true'),
    ('click_referer', 't:SEE_ALL|sid:7f269da3-35e4-4622-b211-852319978fa3|st:MAGAZINE_HOMES'),
    ('client_session_id', '17f5a172-86f0-4821-afa9-d840a390165a'),
    ('currency', 'EUR'),
    ('current_tab_id', 'home_tab'),
    ('experiences_per_grid', '20'),
    ('federated_search_session_id', '8dc6e440-ba67-493f-aad4-2cef979a1341'),
    ('fetch_filters', 'true'),
    ('guidebooks_per_grid', '20'),
    ('has_zero_guest_treatment', 'true'),
    ('hide_dates_and_guests_filters', 'false'),
    ('is_guided_search', 'true'),
    ('is_new_cards_experiment', 'true'),
    ('is_standard_search', 'true'),
    ('items_offset', '18'),
    ('items_per_grid', '18'),
    ('key', 'd306zoyjsyarp7ifhu67rjxn52tv0t20'),
    ('last_search_session_id', '77b54f1a-0eb2-4152-bd6c-41164b55c144'),
    ('locale', 'fr'),
    ('metadata_only', 'false'),
    ('place_id', 'ChIJ-eybj9ZNWxMRRMWtTGMS40U'),
    ('query', 'corfou greece'),
    ('query_understanding_enabled', 'true'),
    ('refinement_paths[]', '/homes'),
    ('s_tag', 'c0eJFIN9'),
    ('satori_version', '1.1.1'),
    ('screen_height', '625'),
    ('screen_size', 'large'),
    ('screen_width', '1366'),
    ('search_type', 'pagination'),
    ('section_offset', '5'),
    ('selected_tab_id', 'home_tab'),
    ('show_groupings', 'true'),
    ('supports_for_you_v3', 'true'),
    ('timezone_offset', '300'),
    ('title_type', 'MAGAZINE_HOMES'),
    ('version', '1.7.0'),
)

response = requests.get('https://www.airbnb.fr/api/v2/explore_tabs', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.airbnb.fr/api/v2/explore_tabs?_format=for_explore_search_web&auto_ib=true&click_referer=t%3ASEE_ALL%7Csid%3A7f269da3-35e4-4622-b211-852319978fa3%7Cst%3AMAGAZINE_HOMES&client_session_id=17f5a172-86f0-4821-afa9-d840a390165a&currency=EUR&current_tab_id=home_tab&experiences_per_grid=20&federated_search_session_id=8dc6e440-ba67-493f-aad4-2cef979a1341&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_offset=18&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&last_search_session_id=77b54f1a-0eb2-4152-bd6c-41164b55c144&locale=fr&metadata_only=false&place_id=ChIJ-eybj9ZNWxMRRMWtTGMS40U&query=corfou%20greece&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&s_tag=c0eJFIN9&satori_version=1.1.1&screen_height=625&screen_size=large&screen_width=1366&search_type=pagination&section_offset=5&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=300&title_type=MAGAZINE_HOMES&version=1.7.0', headers=headers)
for data in response.json()["explore_tabs"]:
    for section in data["sections"]:
        if section.get("listings"):
            for room in section["listings"]:
                print(json.dumps(room,indent=4))
                break