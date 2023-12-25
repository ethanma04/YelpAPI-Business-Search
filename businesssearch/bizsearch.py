#Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
#Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'
#Phone Search         URL -- 'https://api.yelp.com/v3/businesses/search/phone'

#Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'



import requests
import cred
from yelpapi import YelpAPI


#define api key, endpoint, and header
API_KEY = cred.api_key
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#define parameters
term = input('What are you searching for? \n')
print()
location = input('Where is the location? \n')
print()
    


PARAMETERS = {'term': term, 'limit': 25, 'radius': 10000, 'location': location}

#make request to yelpapi
response = requests.get(url = ENDPOINT, params= PARAMETERS, headers = HEADERS)

#convert JSON string to a dictionary
business_data = response.json()
#print(business_data.keys())

#print reccomended places
print('Here is a list of highly rated ' + term + ' places in ' + location + ' that have 20+ reviews on Yelp: ')
count = 1
for biz in business_data['businesses']:
    if(int(biz['review_count']) >= 20 ):
        if(float(biz['rating']) >= 4):
            print(str(count) + '.) ' + biz['name'])
            count += 1
    

#print data on user inputted place
check = False
select = input('\nWhich place would you like to select? (Select a Number) \n')
while(not select.isdigit()):
    select = input('\nNot valid input. Please try again. ')


while(check != True):
    uh = str(biz['location']['display_address'])
    strip = uh.strip(uh)

    num = 1
    print()
    for biz in business_data['businesses']:
        if(num == int(select)):
            print(biz['name'] + '\nAddress: ' + str(biz['location']['address1']) + '\nReviews: ' + str(biz['review_count']) + '\nRating: ' + str(biz['rating']) + '\nPhone Number: ' + biz['display_phone'])
            if(biz['is_closed'] == False):
                print('Is Currently Open.')
            else:
                print('Is Currently Closed.')
            print('Yelp URL: ' + biz['url'])
        num += 1

    select = input('\nWhich place would you like to select? (. to Exit)\n')
    while(not select.isdigit() and select != '.'):
        select = input('\nNot valid input. Please try again. ')

    if(select == '.'):
        check = True
    