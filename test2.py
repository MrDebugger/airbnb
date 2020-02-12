import requests,json

headers = {
    'authority': 'www.airbnb.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-csrf-token': 'V4$.airbnb.com$AOm_S-0C5d4$yyetP065473zBqaPKzHbWUG5iLpd-OyX6AWphGBeqjQ=',
    'x-requested-with': 'XMLHttpRequest',
    'x-csrf-without-token': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.airbnb.com/s/corfou-greece/all?refinement_paths%5B%5D=%2Ffor_you&source=mc_search_bar&search_type=search_query&screen_size=large',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'bev=1579541040_ODVmN2JmZTA3YmRm; jitney_client_session_id=1dda873a-236b-4695-bf81-2cd6238a49c2; jitney_client_session_created_at=1579541040; _csrf_token=V4%24.airbnb.com%24AOm_S-0C5d4%24yyetP065473zBqaPKzHbWUG5iLpd-OyX6AWphGBeqjQ%3D; sticky_locale=en; cdn_exp_18481319c2a05a012=control; cdn_exp_62a1d4bf423854e1e=control; cdn_exp_0c334cfc9a3f42bca=control; cdn_exp_f6632ab691b5e6351=treatment; sdid=; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1286833705.1579541054; _gid=GA1.2.1725741496.1579541054; fbs=not_authorized; __ssid=701f228de679bc0268b7bac7ff64798; _gcl_au=1.1.538465696.1579541157; __svt=156; cfrmfctr=DESKTOP; cbkp=3; hyperloop_exp_p3_p4_v2_exp=2; _user_attributes=%7B%22curr%22%3A%22USD%22%2C%22guest_exchange%22%3A1.0%2C%22device_profiling_session_id%22%3A%221579541040--b2a462b8026d97c6aeccfe07%22%2C%22giftcard_profiling_session_id%22%3A%221579541040--9b0a7b80b55cfe651289e9aa%22%2C%22reservation_profiling_session_id%22%3A%221579541040--b018ac561af1660b9276d8a2%22%7D; flags=0; jitney_client_session_updated_at=1579541695',
}

params = (
    ('_format', 'for_explore_search_web'),
    ('auto_ib', 'true'),
    ('client_session_id', '1dda873a-236b-4695-bf81-2cd6238a49c2'),
    ('currency', 'USD'),
    ('current_tab_id', 'all_tab'),
    ('experiences_per_grid', '200'),
    ('federated_search_session_id', '57754a07-6d3b-42bf-8961-3805780a69b8'),
    ('fetch_filters', 'true'),
    ('guidebooks_per_grid', '200'),
    ('has_zero_guest_treatment', 'true'),
    ('hide_dates_and_guests_filters', 'false'),
    ('is_guided_search', 'true'),
    ('is_new_cards_experiment', 'true'),
    ('is_standard_search', 'true'),
    ('items_offset', '0'),
    ('items_per_grid', '10000'),
    ('key', 'd306zoyjsyarp7ifhu67rjxn52tv0t20'),
    ('locale', 'en'),
    ('metadata_only', 'false'),
    ('place_id', 'ChIJ-eybj9ZNWxMRRMWtTGMS40U'),
    ('query', 'corfou greece'),
    ('query_understanding_enabled', 'true'),
    ('refinement_paths[]', '/for_you'),
    ('satori_version', '1.1.1'),
    ('screen_height', '625'),
    ('screen_size', 'large'),
    ('screen_width', '1366'),
    ('search_type', 'search_query'),
    ('section_offset', '13'),
    ('selected_tab_id', 'all_tab'),
    ('show_groupings', 'true'),
    ('source', 'mc_search_bar'),
    ('supports_for_you_v3', 'true'),
    ('tab_id', 'all_tab'),
    ('timezone_offset', '300'),
    ('version', '1.7.0'),
)

response = requests.get('https://www.airbnb.com/api/v2/explore_tabs', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web&auto_ib=true&client_session_id=1dda873a-236b-4695-bf81-2cd6238a49c2&currency=USD&current_tab_id=all_tab&experiences_per_grid=20&federated_search_session_id=57754a07-6d3b-42bf-8961-3805780a69b8&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_offset=0&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en&metadata_only=false&place_id=ChIJ-eybj9ZNWxMRRMWtTGMS40U&query=corfou%20greece&query_understanding_enabled=true&refinement_paths%5B%5D=%2Ffor_you&satori_version=1.1.1&screen_height=625&screen_size=large&screen_width=1366&search_type=search_query&section_offset=13&selected_tab_id=all_tab&show_groupings=true&source=mc_search_bar&supports_for_you_v3=true&tab_id=all_tab&timezone_offset=300&version=1.7.0', headers=headers)
print(json.dumps(response.json(),indent=4))
