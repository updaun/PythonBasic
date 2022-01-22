import csv
seoung_nam_data = []
header = []
rownum = 0

with open("data_handling/dataset/sample_data.csv", "r", encoding="utf8") as file:
    csv_data = csv.reader(file, delimiter=",")
    for row in csv_data:
        if rownum == 0:
            header = row
        location = row[7]
        if location.find(u"성남시") != -1:
            seoung_nam_data.append(row)

        rownum +=1

with open("data_handling/dataset/seoung_nam_data.csv", "w", encoding="utf8") as w_file:
    writer = csv.writer(w_file, delimiter='\t', quotechar="'", quoting=csv.QUOTE_ALL)
    writer.writerow(header)
    for row in seoung_nam_data:
        writer.writerow(row)