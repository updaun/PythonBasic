import pprint

words = "The quick brown fox jumps over the lazy dog".split()

pprint.pprint([[w.upper(), w.lower(), len(w)] for w in words])

case_1 = ["A","B","C"]
case_2 = ["C","E","A"]

print([i+j for i in case_1 for j in case_2])
print([[i+j for i in case_1] for j in case_2])
print([[j+i for i in case_1] for j in case_2])
print([[j+i for i in case_1 if j != "C"] for j in case_2])