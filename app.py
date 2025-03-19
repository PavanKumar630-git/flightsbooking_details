from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_akasa_token():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.akasaair.com',
        'priority': 'u=1, i',
        'referer': 'https://www.akasaair.com/',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientType': 'WEB',
    }

    try:
        response = requests.post('https://prod-bl.qp.akasaair.com/api/ibe/token', headers=headers, json=json_data)
        response_data = response.json()
        print(response_data)
        # Extract token from the first object in data
        token = response_data.get('data', [{}]).get('token', None)

        return token

    except Exception as e:
        print(f"Error: {e}")
        return None

# Route for fetching booking details
@app.route('/akasaair_bookingdetails', methods=['GET'])
def get_akasaair_booking_details():
    record_locator = request.args.get('pnr')  # Default if not provided
    last_name = request.args.get('lastname')  # Default if not provided
    # data = request.get_json()
    # # record_locator = data.get('recordLocator', 'F4EMPS')  # Default if not provided
    # # last_name = data.get('lastName', 'bansal')  # Default if not provided
    # record_locator = data.get('pnr')  # Default if not provided
    # last_name = data.get('lastname')  # Default if not provided

    akasaair_token = get_akasa_token()
    print("==========token=======",akasaair_token)
    # Headers to be used in the request
    HEADERS = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': akasaair_token,
        'origin': 'https://www.akasaair.com',
        'priority': 'u=1, i',
        'referer': 'https://www.akasaair.com/',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    }
    params = {
        'recordLocator': record_locator,
        'lastName': last_name,
    }

    try:
        response = requests.get('https://prod-bl.qp.akasaair.com/api/ibe/booking/retrieve', params=params, headers=HEADERS)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 500



# Route for fetching booking details
@app.route('/airindia_bookingdetails', methods=['GET'])
def get_airindia_booking_details():
    record_locator = request.args.get('pnr')  # Default if not provided
    last_name = request.args.get('lastname')  # Default if not provided
    # data = request.get_json()
    # # record_locator = data.get('recordLocator', 'F4EMPS')  # Default if not provided
    # # last_name = data.get('lastName', 'bansal')  # Default if not provided
    # record_locator = data.get('pnr')  # Default if not provided
    # last_name = data.get('lastname')  # Default if not provided

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'undefined',
    'content-type': 'application/json',
    'ocp-apim-subscription-key': 'fe65ec9eec2445d9802be1d6c0295158',
    'origin': 'https://www.airindiaexpress.com',
    'priority': 'u=1, i',
    'referer': 'https://www.airindiaexpress.com/manage-booking',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    }
    try:

        json_data = {
            'addtnlDetail': last_name,
            'recordLocator': record_locator,
            'sessionType': 'WebAnonUser',
        }

        response = requests.post(
            'https://api.airindiaexpress.com/b2c-CheckIn/v2/mmb/retrieve/byRecordLocator',
            headers=headers,
            json=json_data,
        )
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route for fetching booking details
@app.route('/spicejet_bookingdetails', methods=['GET'])
def get_spicejet_booking_details():
    record_locator = request.args.get('pnr')  # Default if not provided
    last_name = request.args.get('lastname')  # Default if not provided
    # data = request.get_json()
    # # record_locator = data.get('recordLocator', 'F4EMPS')  # Default if not provided
    # # last_name = data.get('lastName', 'bansal')  # Default if not provided
    # record_locator = data.get('pnr')  # Default if not provided
    # last_name = data.get('lastname')  # Default if not provided

    headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkb3RSRVogQVBJIiwianRpIjoiMDZiYzc2MzQtMmRkMS03ZjU5LWRiYTAtOWQ1YjBlYmQxMzdmIiwiaXNzIjoiZG90UkVaIEFQSSJ9.wQ0jHWsAk2qp33q9t17SjJmp8AWw3vAjr-hijfk-ymA',
    'Referer': 'https://www.spicejet.com/trips/details?pnr=XY6G6F&last=Verma',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'os': 'desktop',
    }

    params = {
        'recordLocator': 'XY6G6F',
        'lastName': 'Verma',
    }

    json_data = {
        'userData': {},
        'method': 'GET',
    }

    try:

        response = requests.post(
        'https://www.spicejet.com/api/v1/booking/retrieveBookingByPNR',
        params=params,
        headers=headers,
        json=json_data,
    )
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
