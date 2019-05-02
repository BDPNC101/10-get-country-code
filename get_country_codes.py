def get_country_codes(prices):
    new_list = []
#country codes will go in here
    for item in prices.split():
#splits country codes into a list, then goes through the list
        new_list.append(item[:2]
#creates new list for country codes to go into
    return ', '.join(new_list) 
#returns string of country codes
