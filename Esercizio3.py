import random
import csv
import os
import pandas as pd

def createrandom_list():
    for i in range (0,30):
        randomlist = []
        number_transaction = random.randint(-100, 100)
        randomlist.append(number_transaction)
        return randomlist

def insertdata():
    descriptions = ['dipartimento finanza', 'dipartimento commerciale', 'dipartimento ict', 'direzione',
                    'risorse umane']
    categories = ['acquisto', 'incasso', 'storno']
    finalvalue = []
    for i in range(0, 30):
        data = []
        data.append(i)
        data.append(random.choice(descriptions))
        data.append(random.choice(createrandom_list()))
        data.append(random.choice(categories))
        finalvalue.append(data)
    return finalvalue

def analyze(path,filename, categoria):
    with open(os.path.join(path, filename), newline='', encoding='UTF8') as third:
        third_df = pd.read_csv(third)
        bilancio= third_df.loc[(third_df['categoria'] == categoria), 'importo'].sum()
    with open(os.path.join(path, filename), newline='', encoding='UTF8') as second:
        second_df = pd.read_csv(second)
        costo = second_df.loc[(second_df['categoria'] == categoria) & (second_df['importo'] < 0), 'importo'].sum()
    with open(os.path.join(path, filename), newline='', encoding='UTF8') as first:
        first_df = pd.read_csv(first)
        ricavo = first_df.loc[(first_df['categoria'] == categoria) & (first_df['importo'] > 0), 'importo'].sum()
    return bilancio, costo, ricavo

def writeread(header, filedata, path, filename):
    with open(os.path.join(path, filename), 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(0, 30):
                writer.writerows(filedata)

    with open(os.path.join(path, filename), newline='', encoding='UTF8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)




header = ['id','descrizione', 'importo', 'categoria']
file_data = insertdata()
original_path = r'*insert_path*'
original_filename = 'transazioni.csv'
writeread(header, file_data, original_path, original_filename)

report_header = ['bilancio','costo', 'ricavo']
report_path = r'*insert_path*'
report_filename = 'report.csv'
categoria_acquisto = 'acquisto'
categoria_incasso = 'incasso'
categoria_storno = 'storno'
report_data = []
report_data.append(analyze(original_path,original_filename, categoria_acquisto))
report_data.append(analyze(original_path,original_filename, categoria_incasso))
report_data.append(analyze(original_path, original_filename, categoria_storno))
print(report_header, '\n', report_data[0], '\n', report_data[1], '\n', report_data[2])











