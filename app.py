# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)

# def get_akasa_token():
#     headers = {
#         'accept': 'application/json, text/plain, */*',
#         'accept-language': 'en-US,en;q=0.9',
#         'content-type': 'application/json',
#         'origin': 'https://www.akasaair.com',
#         'priority': 'u=1, i',
#         'referer': 'https://www.akasaair.com/',
#         'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
#     }

#     json_data = {
#         'clientType': 'WEB',
#     }

#     try:
#         response = requests.post('https://prod-bl.qp.akasaair.com/api/ibe/token', headers=headers, json=json_data)
#         response_data = response.json()
#         print(response_data)
#         # Extract token from the first object in data
#         token = response_data.get('data', [{}]).get('token', None)

#         return token

#     except Exception as e:
#         print(f"Error: {e}")
#         return None


# def get_airindia_oauth_token():
#     headers = {
#         'accept': 'application/json',
#         'accept-language': 'en-US,en;q=0.9',
#         'content-type': 'application/x-www-form-urlencoded',
#         'origin': 'https://travel.airindia.com',
#         'priority': 'u=1, i',
#         'referer': 'https://travel.airindia.com/',
#         'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
#     }
    
#     data = {
#         'client_id': 'DCkj8EM4xxOUnINtcYcUhGXVfP2KKUzf',
#         'client_secret': 'QWgBtA2ARMfdAf1g',
#         'grant_type': 'client_credentials',
#         'guest_office_id': 'DELAI08AA',
#     }
    
#     response = requests.post('https://api-des.airindia.com/v1/security/oauth2/token', headers=headers, data=data)
    
#     return response.json()


# # Route for fetching booking details
# @app.route('/akasaair_bookingdetails', methods=['GET'])
# def get_akasaair_booking_details():
#     record_locator = request.args.get('pnr')  # Default if not provided
#     last_name = request.args.get('lastname')  # Default if not provided
#     # data = request.get_json()
#     # # record_locator = data.get('recordLocator', 'F4EMPS')  # Default if not provided
#     # # last_name = data.get('lastName', 'bansal')  # Default if not provided
#     # record_locator = data.get('pnr')  # Default if not provided
#     # last_name = data.get('lastname')  # Default if not provided

#     akasaair_token = get_akasa_token()
#     print("==========token=======",akasaair_token)
#     # Headers to be used in the request
#     HEADERS = {
#         'accept': 'application/json, text/plain, */*',
#         'accept-language': 'en-US,en;q=0.9',
#         'authorization': akasaair_token,
#         'origin': 'https://www.akasaair.com',
#         'priority': 'u=1, i',
#         'referer': 'https://www.akasaair.com/',
#         'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
#     }
#     params = {
#         'recordLocator': record_locator,
#         'lastName': last_name,
#     }

#     try:
#         response = requests.get('https://prod-bl.qp.akasaair.com/api/ibe/booking/retrieve', params=params, headers=HEADERS)
#         return jsonify(response.json())

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500



# # Route for fetching booking details
# @app.route('/airindia_express_bookingdetails', methods=['GET'])
# def get_airindia_express_booking_details():
#     record_locator = request.args.get('pnr')  # Default if not provided
#     last_name = request.args.get('lastname')  # Default if not provided
#     # data = request.get_json()
#     # # record_locator = data.get('recordLocator', 'F4EMPS')  # Default if not provided
#     # # last_name = data.get('lastName', 'bansal')  # Default if not provided
#     # record_locator = data.get('pnr')  # Default if not provided
#     # last_name = data.get('lastname')  # Default if not provided

#     headers = {
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'en-US,en;q=0.9',
#     'authorization': 'undefined',
#     'content-type': 'application/json',
#     'ocp-apim-subscription-key': 'fe65ec9eec2445d9802be1d6c0295158',
#     'origin': 'https://www.airindiaexpress.com',
#     'priority': 'u=1, i',
#     'referer': 'https://www.airindiaexpress.com/manage-booking',
#     'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
#     }
#     try:

#         json_data = {
#             'addtnlDetail': last_name,
#             'recordLocator': record_locator,
#             'sessionType': 'WebAnonUser',
#         }

#         response = requests.post(
#             'https://api.airindiaexpress.com/b2c-CheckIn/v2/mmb/retrieve/byRecordLocator',
#             headers=headers,
#             json=json_data,
#         )
#         return jsonify(response.json())

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # Route for fetching booking details
# @app.route('/airindia_bookingdetails', methods=['GET'])
# def get_airindia_booking_details():
#     record_locator = request.args.get('pnr')  # Default if not provided
#     last_name = request.args.get('lastname')  # Default if not provided
#     # data = request.get_json()
#     # # record_locator = data.get('recordLocator', 'F4EMPS')  # Default if not provided
#     # # last_name = data.get('lastName', 'bansal')  # Default if not provided
#     # record_locator = data.get('pnr')  # Default if not provided
#     # last_name = data.get('lastname')  # Default if not provided
#     get_airindia_tokens = get_airindia_oauth_token()
#     headers = {
#     'accept': 'application/json',
#     'accept-language': 'en-US,en;q=0.9',
#     # 'ama-client-ref': '91c9e175-4c95-49b3-9c61-647a5a415659:0',
#     'authorization': '{0} {1}'.format(get_airindia_tokens['token_type'],get_airindia_tokens['access_token']),
#     'cache-control': 'max-age=0',
#     'content-type': 'application/json',
#     'origin': 'https://travel.airindia.com',
#     'priority': 'u=1, i',
#     'referer': 'https://travel.airindia.com/',
#     'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
#     # 'x-d-token': '3:DXTSyvsGoRZqn1HNUiL9cQ==:RAyF3p+z7ZJdL5/UWSvnn6aBBbqiN7Eh1TIY9aaHdACKuLFcKEvD4OCbwtjPE7nEWv2GRC6obFYgjzFoBZL4a/zIaBKVI10hy5/8x/rsSaZIem9OjPAD7s8pz5srP/mxqyK/oSQm0Se/DQyzxSoaK1yEXiy1ZFbk/aF8miEXLL8hzCYG5d+pRADNfujA0lV50WybPfKAcjH3WRwKCGFxBssHzX4x1lsndptcCBK2+W07l4LSGKTbmhco4lD2Aq84Rse89nMyX/Xi4AOTCA/GyQxa36VhiwsGQCsJtYg3I6bJ8zEMLyvZ/cxFHGphPRsqlCBQBRHcUOm7owj/o4jlgWauWXZvopWqHTeXsExXz16LQ1T8F3i2HYewQ7Iak9Q/wPKIMGCYdrk42hq14urcrcb6mlf42t/ZTZiJy/0NL+zCq1R8n2g4g/i0UTWtGAXF47VSOtBCBXvL4kLZtuPr2oUWhcxfPTW7jePLZ1ipv/JWdeda+jHiNoHx2aG8sl/YGGFuGDCsbT8p3O4Pr0AqToSVF4GkzD8k+a+oWmsdcI4zsXwKGd2xAzokAYjgg4qdMQumOTOa6navrWHizDJmSpjCpTU6+8z7q+y9340JVYbjKr6k34UQUDrq8FsJMxF1dv0Jn7Y7/OesUeb3avGLZwjFOzgTrJxy5Ptiu5OLuBe0dAdeKlR7vjXBnm7JVabpYqegfl5kMzzhRRSeJDkSTohX0RVWPq/RwD/yCqMyM+3i3lP5qEpHf7AjAgHCSeynx6XLEk3gAGxq47c4BPtLafR2wgfzhgWyWFoo4IVdAoTOfHAp2r/BkKBwvKSIWHc3qqcQHN1K/vn67t7dyqpFW5sl4YAYRC9SMSGv6dwIbp6N961U2ytyTpshmADsOs16VnDDAQqgFwB9e3YRPruzXivGmUgTI9oaB7Hyfv+epfo=:NdvmoWO07tRYma62+1caWxo1vyMCgURt0xNsrGRxigM=',
#     }

#     params = {
#         'lastName': last_name,
#         'showOrderEligibilities': 'true',
#         'checkServicesAndSeatsIssuanceCurrency': 'false',
#     }

#     try:
#         response = requests.get('https://api-des.airindia.com/v2/purchase/orders/{0}'.format(record_locator), params=params, headers=headers)

#         return jsonify(response.json())

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # Route for fetching booking details
# @app.route('/spicejet_bookingdetails', methods=['GET'])
# def get_spicejet_booking_details():
#     record_locator = request.args.get('pnr')  # Default if not provided
#     last_name = request.args.get('lastname')  # Default if not provided
#     # data = request.get_json()
#     # # record_locator = data.get('recordLocator', 'F4EMPS')  # Default if not provided
#     # # last_name = data.get('lastName', 'bansal')  # Default if not provided
#     # record_locator = data.get('pnr')  # Default if not provided
#     # last_name = data.get('lastname')  # Default if not provided

#     headers = {
#     'sec-ch-ua-platform': '"Windows"',
#     'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkb3RSRVogQVBJIiwianRpIjoiMDZiYzc2MzQtMmRkMS03ZjU5LWRiYTAtOWQ1YjBlYmQxMzdmIiwiaXNzIjoiZG90UkVaIEFQSSJ9.wQ0jHWsAk2qp33q9t17SjJmp8AWw3vAjr-hijfk-ymA',
#     'Referer': 'https://www.spicejet.com/trips/details?pnr=XY6G6F&last=Verma',
#     'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
#     'Content-Type': 'application/json',
#     'os': 'desktop',
#     }

#     params = {
#         'recordLocator': 'XY6G6F',
#         'lastName': 'Verma',
#     }

#     json_data = {
#         'userData': {},
#         'method': 'GET',
#     }

#     try:

#         response = requests.post(
#         'https://www.spicejet.com/api/v1/booking/retrieveBookingByPNR',
#         params=params,
#         headers=headers,
#         json=json_data,
#     )
#         return jsonify(response.json())

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
# if __name__ == '__main__':
#     app.run(debug=True)







from fastapi import FastAPI, Query
import requests

app = FastAPI(title="Flight Booking API", description="APIs for retrieving booking details", version="1.0")


def get_akasa_token():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'origin': 'https://www.akasaair.com',
        'referer': 'https://www.akasaair.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    json_data = {'clientType': 'WEB'}

    try:
        response = requests.post('https://prod-bl.qp.akasaair.com/api/ibe/token', headers=headers, json=json_data)
        response_data = response.json()
        return response_data.get('data', {}).get('token', None)
    except Exception as e:
        return {"error": str(e)}


def get_airindia_oauth_token():
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://travel.airindia.com',
    }
    data = {
        'client_id': 'DCkj8EM4xxOUnINtcYcUhGXVfP2KKUzf',
        'client_secret': 'QWgBtA2ARMfdAf1g',
        'grant_type': 'client_credentials',
        'guest_office_id': 'DELAI08AA',
    }
    
    response = requests.post('https://api-des.airindia.com/v1/security/oauth2/token', headers=headers, data=data)
    return response.json()


@app.get("/akasaair_bookingdetails")
def get_akasaair_booking_details(pnr: str = Query(...), lastname: str = Query(...)):
    akasaair_token = get_akasa_token()

    headers = {
        'accept': 'application/json',
        'authorization': akasaair_token,
        'origin': 'https://www.akasaair.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    params = {'recordLocator': pnr, 'lastName': lastname}

    try:
        response = requests.get('https://prod-bl.qp.akasaair.com/api/ibe/booking/retrieve', params=params, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@app.get("/airindia_express_bookingdetails")
def get_airindia_express_booking_details(pnr: str = Query(...), lastname: str = Query(...)):
    headers = {
        'accept': 'application/json',
        'authorization': 'undefined',
        'content-type': 'application/json',
        'ocp-apim-subscription-key': 'fe65ec9eec2445d9802be1d6c0295158',
        'origin': 'https://www.airindiaexpress.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    json_data = {'addtnlDetail': lastname, 'recordLocator': pnr, 'sessionType': 'WebAnonUser'}

    try:
        response = requests.post(
            'https://api.airindiaexpress.com/b2c-CheckIn/v2/mmb/retrieve/byRecordLocator',
            headers=headers,
            json=json_data,
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@app.get("/airindia_bookingdetails")
def get_airindia_booking_details(pnr: str = Query(...), lastname: str = Query(...)):
    airindia_token = get_airindia_oauth_token()

    headers = {
        'accept': 'application/json',
        'authorization': f"{airindia_token['token_type']} {airindia_token['access_token']}",
        'content-type': 'application/json',
        'origin': 'https://travel.airindia.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    params = {'lastName': lastname, 'showOrderEligibilities': 'true', 'checkServicesAndSeatsIssuanceCurrency': 'false'}

    try:
        response = requests.get(f'https://api-des.airindia.com/v2/purchase/orders/{pnr}', params=params, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@app.get("/spicejet_bookingdetails")
def get_spicejet_booking_details(pnr: str = Query(...), lastname: str = Query(...)):
    headers = {
        'Authorization': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkb3RSRVogQVBJIiwianRpIjoiYjM1OTZjYWYtNzIxMC04ODIzLTFjYWUtNzBjOWZkZTU4NmRiIiwiaXNzIjoiZG90UkVaIEFQSSJ9.q8v8McYrEoRiDin3hZ0tZkjEdXd1kAuv5tbU1-KKsoA",
        'Referer': f'https://www.spicejet.com/trips/details?pnr={pnr}&last={lastname}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Content-Type': 'application/json',
        'os': 'desktop',
    }
    params = {'recordLocator': pnr, 'lastName': lastname}
    json_data = {'userData': {}, 'method': 'GET'}

    try:
        response = requests.post('https://www.spicejet.com/api/v1/booking/retrieveBookingByPNR', params=params, headers=headers, json=json_data)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
