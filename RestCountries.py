#Information about code:

import requests

base_url = 'https://restcountries.com/v2/'


print("Which country do you want to know more about?")
country = input('')

print("Select which information you would like to know about or press 0 to exit")
print("1. Official Languages \n2. Population \n3. Borders")
selection = int(input(''))


params = {'fields' : 'languages; population; borders', 'fullText' : 'true'}
#data not sanitized!!!!
r = requests.get(base_url + 'name/{}'.format(country)) #, params=params)


json_response = r.json()
country = json_response[0]



while selection > 0:
   
    if selection ==1:
        languages = country['languages']
        print('The Languages are {}'.format(languages[0]['name']))

        
    elif selection ==2:
        population = country['population']
        print('Population is {}'.format(population))
        
    elif selection ==3:
        border = country['borders']
        print("Boarder countries below")
        for i in border:
            print(i)
    else:
        print("Invalid Selection")
    
    
    
    country = input("Select a new country: ")
    r = requests.get(base_url + 'name/{}'.format(country))
    json_response = r.json()
    country = json_response[0]
    selection = int(input("Enter new selection or press 0 to exit: "))

    
#last step... loop to ask if staying on same country + add comments 
