import os
import requests, csv, datetime
from threading import Thread

# convert a 2010-01-01T21:30:00Z to 11:00 AM
def convert_time(time):
    return datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ').strftime('%I:%M %p')



url = "https://www.pedidosya.com.pa/mobile/v1/countries"


querystring = None

payload = ""
headers = {
    "cookie": "dhhPerseusGuestId=1659641719361.405997869287282300.avau0xs3mz8; dhhPerseusSessionId=1659641719361.8910198179083118.ajm4apzi85m; dhhPerseusHitId=1659641774327.866079587100899100.e5teu9lg76t; __Secure-peya.sid=s%253Ae2489cec-f40b-42fa-9462-aa3811aaa9f7.OcS52tVxDx98FP%252F2F13IE0VLumslX49mGqUtoKU8Xt0; __Secure-peyas.sid=s%253A5138a72c-600a-499a-98e9-6ee7bd2339d1.9gQdNmJySElwevTuMSt7yehAp2Ip9gqzk3qZ4Viqa2M; _pxhd=IarEOiReEtYotqgJtsLwo-PnQVqYuvNozcDGnAAv%2FhLhL3nO9eAM02hkQYFBHMSVSAwDqiT2tO99XtSv3GPY5g%3D%3D%3ARACVrtKAZFsqovZ939EZkbry2x5UUArNX%2Fyzs8fPMkSIp-ej2iXSpJlwx73r8hiL5AnR9UKOyaR2suVEhfomsjMukJUoPV4mdTr-AXdEGaw%3D; __cf_bm=dpgsvyBs0WVhwa77VQwBuI9M3M4NUAmFEVMUUFVueYI-1659641774-0-AaXbfOgis4yZLEcpnUd4LcJCx4YUd%2FkRWPy8hFFOZxtYMBhC5bD%2BQjzHrxw49itZuAPU46YDkySflwoNCbc7yYo%3D",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Max": "999",
    "Referer": "https://www.pedidosya.com.pa/",
    "sentry-trace": "882cd9b36f7c40b5875c1b739baf0957-94f170c246d9c27f-0",
    "Connection": "keep-alive",
    "Cookie": "dhhPerseusGuestId=1659641719361.405997869287282300.avau0xs3mz8; dhhPerseusSessionId=1659641719361.8910198179083118.ajm4apzi85m; dhhPerseusHitId=1659641719361.591683611162875800.a93985ufu8; __Secure-peya.sid=s%3Ae2489cec-f40b-42fa-9462-aa3811aaa9f7.OcS52tVxDx98FP%2F2F13IE0VLumslX49mGqUtoKU8Xt0; __Secure-peyas.sid=s%3A5138a72c-600a-499a-98e9-6ee7bd2339d1.9gQdNmJySElwevTuMSt7yehAp2Ip9gqzk3qZ4Viqa2M; _pxhd=IarEOiReEtYotqgJtsLwo-PnQVqYuvNozcDGnAAv/hLhL3nO9eAM02hkQYFBHMSVSAwDqiT2tO99XtSv3GPY5g==:RACVrtKAZFsqovZ939EZkbry2x5UUArNX/yzs8fPMkSIp-ej2iXSpJlwx73r8hiL5AnR9UKOyaR2suVEhfomsjMukJUoPV4mdTr-AXdEGaw=; __cf_bm=lg_0RwjLGEwRJuJjgf75Z3Rptss0Csrf85s5ClzQFSg-1659641719-0-ARRzZKgERwrdKACVIZEkfNAKZn2Z/UfHeFjqqc690dzDMmQoyRaR63iEjKwzlXFNWUYPvhDHWf59NHb9K2lVVGA=; pxcts=93b5e315-142c-11ed-ae44-444968476e6e; _pxvid=925433ae-142c-11ed-85db-4e4e49577247; _px3=3c83f3fdfd3e425dc6081f6d2a51267024ebf0a68d6a93526f117d8b916cd094:PauTkRmHC+HenZ58XjHCjywTuJh3la4K67oKri5nlkgw3wPFCXIy74KuH1BJgOeBgvSH9uSPmy+SkNvrbFPLYQ==:1000:rRUGi+KqcBReMT0BunPuk9sGihROVsUMVfBUGz+nm18JwCI5XM56llFrFhKwwIji2Xq25bT/sOzfJlk+Z/n37Vxr0E20VTF0Po+0rYy93YW5LskuyQDDBb++WNzV108wwSTK3hqZ0up0TIeJQE6fvwElUGCgI1y9yucHxtnxr8hFozi9dRDa0iCkvuYpTvJGl/R7HKMVyvcvRfNKltZDng==",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}
base_hero_url = 'https://images.deliveryhero.io/image/pedidosya/profile-headers/'

url = "https://www.pedidosya.com.pa/mobile/v1/countries/11/cities"

city_response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
data = city_response.json()['data']

def get_city_data(city):

        cid = city['id']
        curl = city['name'].lower().replace(' ', '-')
        url = f"https://www.pedidosya.com.pa/mobile/v1/cities/{cid}/areas"
        zone_response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        try:
            zone_list = zone_response.json()['data']
            for area in zone_list:
                if not os.path.exists(city["name"]):
                    os.makedirs(city["name"])

                with open(f'{city["name"]}/{area["name"]}.csv', 'w') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(['Restaurant URL', 'Restaurant name', 'Restaurant background Image','Opens At', 'Close At', 'Restaurant Rating', 'Categories', 'Product name', 'Product description', 'product price', 'Image Url', 'Product Rating', 'Option Group ID', 'Option Group Name', 'Option ID', 'Option Name', 'Option Price', 'Total reviews', 'Accept online payment', 'delivery Time', 'shipping cost', 'Best Seller Product', 'Accepts Pre Order', 'Affected By Porygon Events', 'City', 'City Latitude', 'City Longitude', 'Area', 'Area Latitude', 'Area Longitude', 'Business Type', 'Capacity Check', 'Delivers', 'Logo', 'Restaurant Latitude', 'Restaurant Longitude', 'Product Id', 'Walking Time', 'Walking Distance', 'Distance', 'Payment Methods List', 'menu Id', 'Country Id', 'City Id', 'Area Id'])
                    latitude = area['latitude']
                    longitude = area['longitude']
                    restourant_url = f"https://www.pedidosya.com.pa/mobile/v5/shopList?businessType=RESTAURANT&country=11&point={latitude},{longitude}"
                    rest_response = requests.request("GET", restourant_url, data=payload, headers=headers, params=querystring)
                    try:
                        rest_data = rest_response.json()['list']['data']

                        for rest in rest_data:

                            rest_hero_url = f"{base_hero_url}20404491-d96e6a7f-44e8-4d86-b763-6fbdcabc4b0a.jpeg"
                            if rest.get('headerImage'):
                                rest_hero_url = f"{base_hero_url}{rest.get('headerImage')}"
                            rest_url = f'https://www.pedidosya.com.pa/restaurantes/{curl}/{rest["link"]}-menu?origin=shop_list'
                            re_id = rest['id']
                            print(re_id)
                            item_url = f"https://www.pedidosya.com.pa/v2/niles/partners/{re_id}/menus"
                            item_response = requests.request("GET", item_url, data=payload, headers=headers, params=querystring)
                            if item_data := item_response.json().get('sections'):
                                try:
                                    for item in item_data:
                                        for pto in item.get('products', []):
                                            product_name = pto.get('name', '')
                                            product_description = pto.get('description', '')
                                            product_price = f"${pto.get('price',{'finalPrice':0})['finalPrice']}"
                                            try:
                                                product_image_url = f"https://images.deliveryhero.io/image/pedidosya/products/{pto.get('images')['urls'][0]}"
                                            except Exception as e:
                                                product_image_url = ''
                                            product_rating = pto.get('rating')
                                            rest_total_reviews = rest.get('validReviewsCount') or 0
                                            rest_accept_online_payment = 'yes' if rest.get('hasOnlinePaymentMethods') else ''
                                            rest_shipping_cost = f"${rest.get('shippingAmount', 0)}"
                                            rest_delivery_time = rest.get('deliveryTime',  '')
                                            product_best_seller_product = 'yes' if pto.get('tags').get('isMostOrdered') else ''
                                            optionGroups_url = f"https://www.pedidosya.com.pa/mobile/v1/products/{pto['id']}?restaurantId={rest['id']}&businessType=RESTAURANT"
                                            optionGroups_response = requests.request("GET", optionGroups_url, data=payload, headers=headers, params=querystring)
                                            if optionGroups_data := optionGroups_response.json().get('optionGroups'):
                                                for optionGroup in optionGroups_data:
                                                    for option in optionGroup.get('options'):
                                                        try:
                                                            writer.writerow(
                                                            [rest_url, rest['name'], rest_hero_url, convert_time(rest['nextHour']), convert_time(rest['nextHourClose']),rest['generalScore'], item['name'], product_name, product_description, product_price, product_image_url, product_rating, optionGroup['id'], optionGroup['name'], option['id'], option['name'], option['amount'], rest_total_reviews, rest_accept_online_payment, rest.get('deliveryTime'), rest_shipping_cost, product_best_seller_product, 'yes' if rest.get('acceptsPreOrder') else '', 'yes' if rest.get('affectedByPorygonEvents') else '', rest.get('cityName'), city['latitude'], city['longitude'], rest.get('area'), latitude, longitude, rest.get('businessType'), 'yes' if rest.get('capacityCheck') else '', rest.get('delivers'), f'https://images.deliveryhero.io/image/pedidosya/restaurants/{rest["logo"]}', rest['latitude'], rest['longitude'], pto.get('id'), rest.get('walkingTime'), rest.get('walkingDistance'), rest.get('distance'), rest.get('paymentMethodsList'), rest.get('menuId'), rest.get('countryId'), city['id'], area['id']]
                                                            )
                                                        except Exception as e:
                                                            pass
                                            else:
                                                writer.writerow(
                                                [rest_url, rest['name'], rest_hero_url, convert_time(rest['nextHour']), convert_time(rest['nextHourClose']),rest['generalScore'], item['name'], product_name, product_description, product_price, product_image_url, product_rating, '', '', '', '', '', rest_total_reviews, rest_accept_online_payment, rest.get('deliveryTime'), rest_shipping_cost, product_best_seller_product, 'yes' if rest.get('acceptsPreOrder') else '', 'yes' if rest.get('affectedByPorygonEvents') else '', rest.get('cityName'), city['latitude'], city['longitude'], rest.get('area'), latitude, longitude, rest.get('businessType'), 'yes' if rest.get('capacityCheck') else '', rest.get('delivers'), f'https://images.deliveryhero.io/image/pedidosya/restaurants/{rest["logo"]}', rest['latitude'], rest['longitude'], pto.get('id'), rest.get('walkingTime'), rest.get('walkingDistance'), rest.get('distance'), rest.get('paymentMethodsList'), rest.get('menuId'), rest.get('countryId'), city['id'], area['id']]
                                                )
                                except Exception as e:
                                    pass
                    except Exception as e:
                        pass
        except Exception as e:
            pass

def main():
    task_list = []
    for city in data:
        task = Thread(target=get_city_data, args=(city,))
        task_list.append(task)
    
    for task in task_list:
        task.daemon = True
        task.start()
    for task in task_list:
        task.join()
    

if __name__ == '__main__':
    main()