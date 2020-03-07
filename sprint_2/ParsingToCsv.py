import csv

def make_csv(dicos,name="DefaultName",headers=None):
    with open (name+".csv", 'w', newline="") as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames=headers if headers else dicos[0].keys())

        writer.writeheader()
        for i in dicos:
            writer.writerow(i)
