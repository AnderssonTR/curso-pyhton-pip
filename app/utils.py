def get_population(country_dict):
    population_dict={
        '2022':int(country_dict['2022 Population']),
        '2020':int(country_dict['2020 Population']),
        '2015':int(country_dict['2015 Population']),
        '2010':int(country_dict['2010 Population']),
        '2000':int(country_dict['2000 Population']),
        '1990':int(country_dict['1990 Population']),
        '1980':int(country_dict['1980 Population']),
        '1970':int(country_dict['1970 Population'])
    }
    #keys=['col','bol']
    #values=[300,400]
    return population_dict.keys(),population_dict.values()

def population_by_country(data,country):
    result = list(filter(lambda item:item['Country/Territory']==country,data))
    return result
def get_population_mundial(data):
    data_keys=tuple(country['Country/Territory'] for country in data)
    data_values=tuple(float(Percentage['World Population Percentage'])for Percentage in data)
    data_dict=dict(zip(data_keys,data_values))
    return data_dict.keys(),data_dict.values()
