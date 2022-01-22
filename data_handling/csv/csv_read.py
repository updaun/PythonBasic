# CSV - Comma Separate Value
# TSV, SSV
# Character-Separated Values 통칭

line_counter = 0
data_header = []
mover_list = []

with open("data_handling/dataset/sample_data.csv", encoding='utf8') as customer_data:

    while True:
        data = customer_data.readline()
        if not data: break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            mover_list.append(data.split(","))
        line_counter += 1
    
    print("Header :\t", data_header)
    for i in range(0, 10):
        print("Data ", i, ":\t\t", mover_list[i])
    print(len(mover_list))