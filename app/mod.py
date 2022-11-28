def get_population():
    keys = ['col', 'bol','nic']
    values = [300,400,500]
    return keys, values
def A():
    A = 'Hola' 
    return A 

def population_by_country(data,country):
    result = list(filter(lambda item: item ['Country']== country, data))
    return result