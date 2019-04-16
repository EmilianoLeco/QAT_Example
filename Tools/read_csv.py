import csv

def read_csv(path):
    with open(path) as f:
        data = [tuple(line) for line in csv.reader(f)]

    return (data[1:])


#print(read_csv('..\..\Configuration\Parameters.csv'))