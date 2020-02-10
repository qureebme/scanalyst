import csv

def make_csv(dicos):
    with open ("project_template.csv", 'w', newline="") as csvfile:
        writer= csv.DictWriter(csvfile, fieldnames=dicos[0].keys())

        writer.writeheader()
        for i in dicos:
            writer.writerow(i)
