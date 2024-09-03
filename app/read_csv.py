import  csv
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data=[]
        for row in reader:
            iterable = zip(header,row)
            country_dict={key:value for key, value in iterable}
            data.append(country_dict)
        return data
if __name__=='__main__':
    data=read_csv(r'c:/Users/Andersson Torres/Documents/udemy/cusroPython/Introduccion/Python102/app/data.csv')
    print(data)

# def read_csv(path):
#     with open(path, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         suma=0
#         for row in reader:
#             print(row[1])
#             suma +=int(row[1])
#         return suma
# if __name__=='__main__':
#     data=read_csv(r'c:/Users/Andersson Torres/Documents/udemy/cusroPython/Introduccion/Python102/app/data_1.csv')
#     print(data)