#Bytes and bits

# t=int(input())
#
# for x in range(t):
#
#     bits=1
#     nibble=0
#     byte=0
#
#     n=int(input())
#
#     for y in range(n):
#
#         if y%2==0:
#             bits=bits-1
#             nibble=nibble+1
#
#         elif y%10==0:
#             nibble=nibble-1
#             byte=byte+1
#
#         elif y%26==0:
#             byte=byte-1
#             bits=bits+2
#
#     print(bits,nibble,byte)


import urllib.request,urllib.parse,urllib.error
import json
import ssl

api_key=False

if api_key==False:
    api_key=42
    serviceurl='http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl='https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address=input("Enter Location=")
    if len(address)<1:
        break

    parms=dict()

    parms['address']=address
    if api_key is not False: parms['key']=api_key

    url=serviceurl+urllib.parse.urlencode(parms)
    print('Retrieving ', url)

    uh=urllib.request.urlopen(url,context=ctx)
    data=uh.read().decode()
    print("Retrieved ",len(data),'characters')

    try:
        js=json.loads(data)
    except:
        js=None

    if not js or 'status' not in js or js['status']!='OK':
        print("Failed to retrieve data")
        print(data)
        continue

    print(json.dumps(js,indent=4))
    print(js['results'][0]['geometry']['location']['lat'])
    print(js['results'][0]['geometry']['location']['lng'])
    location = js['results'][0]['formatted_address']
    print("Place Id=",js['results'][0]['place_id'])
