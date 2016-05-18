from prettytable import PrettyTable
import csv

def csv_pretty_printer(csv_location,list,limit,header):
    f = open("datagovbldgrexus.csv", "r")
    reader = csv.reader(f)
    if header == True:
        next(reader)
    fields = list
    cnt = 0
    a=[]
    for i in reader:
        a.append(i)
        cnt = cnt + 1
        if cnt > limit:
            break

    p = PrettyTable(field_names=fields)
    for i in a:
        p.add_row(i)

    print(p)

