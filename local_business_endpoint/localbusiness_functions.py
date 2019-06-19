# parsers
def get_listings(json):
    return [i for i in json['places']['value']]

def get_names(json):
    return [i['name'] for i in json['places']['value']]

def get_geo_dicts(json):
    return [i['geo'] for i in json['places']['value']]

def get_lats(json):
    return [i['geo']['latitude'] for i in json['places']['value']]

def get_longs(json):
    return [i['geo']['longitude'] for i in json['places']['value']]

def get_addr_dicts(json):
    return [i['address'] for i in json['places']['value']]

def get_neighborhoods(json):
    return [i['address']['neighborhood'] for i in json['places']['value']]

def get_zipcodes(json):
    return [i['address']['postalCode'] for i in json['places']['value']]

def get_cities(json):
    return [i['address']['addressLocality'] for i in json['places']['value']]

def get_states(json):
    return [i['address']['addressRegion'] for i in json['places']['value']]

def get_phone_nums(json):
    return [i['telephone'] for i in json['places']['value']]