import utils  
import read_csv
import charts
import pandas as pd

# data=[
#     {'Country':'Colombia',
#      'Population':411
#      },
#      {'Country':'Colombia',
#      'Population':6010
#      }
#      ,
#      {'Country':'Bolvia',
#      'Population':100
#      }
# ]

def run(country):
    data=read_csv.read_csv(r'c:/Users/Andersson Torres/Documents/udemy/cusroPython/Introduccion/Python102/app/data.csv')
    result=utils.population_by_country(data, country)
    
    if len(result)>0:
        country = result[0]
        keys,values=utils.get_population(country)
        print(keys,values)
        charts.generate_bar_chart(keys, values)

def run_2():
    data=read_csv.read_csv(r'c:/Users/Andersson Torres/Documents/udemy/cusroPython/Introduccion/Python102/app/data.csv')
    result=utils.get_population_mundial(data)
    
    if len(result)>0:
        keys,values=result
        print(keys,values)
        charts.generate_bar_chart(keys, values)

def run_3():
   # data=read_csv.read_csv(r'c:/Users/Andersson Torres/Documents/udemy/cusroPython/Introduccion/Python102/app/data.csv')
    
    #data=read_csv.read_csv('data.csv')
    df =pd.read_csv('data.csv')

    #data=list(filter(lambda item:item['Continent']=='South America',data))
    df = df[df['Continent']=='Africa']
   
    #countries=list(map(lambda x:x['Country/Territory'],data))
    countries=df['Country/Territory'].values
    
    #percentagen=list(map(lambda x:float(x['World Population Percentage']),data))
    percentagen=df['World Population Percentage'].values

    charts.generate_pie_chart(countries, percentagen)

if __name__ == '__main__':
    #run('Colombia')
    #run_2()
    run_3()

