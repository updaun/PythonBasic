# CSV - Comma Separate Value
# TSV, SSV
# Character-Separated Values 통칭

line_counter = 0
data_header = []
mover_list = []
weekend = []
weekend_mover_list = []

with open("data_handling/dataset/sample_data.csv", encoding='utf8') as customer_data:

    while True:
        data = customer_data.readline()
        if not data: break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            mover = data.split(",")
            if mover[2] == "주말":
                weekend_mover_list.append(mover)
        line_counter += 1
    
    print("Header :\t", data_header)
    for i in range(0, 10):
        print("Data ", i, ":\t\t", weekend_mover_list[i])
    print(len(weekend_mover_list))

    with open("data_handling/dataset/weekend_mover.csv", "w", encoding="utf8") as csv_writer:
        for mover in weekend_mover_list:
            csv_writer.write(",".join(mover).strip('\n')+"\n")