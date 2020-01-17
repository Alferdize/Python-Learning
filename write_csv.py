import csv 

with open("data.csv","w") as wf:
    data_csv = csv.writer(wf,delimiter=",",quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_csv.writerow(['John Smith', 'Accounting', 'November'])
    data_csv.writerow(['Erica Meyers', 'IT', 'March'])