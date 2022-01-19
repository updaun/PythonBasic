for i, v in enumerate(['tic', 'tac', 'toc']):
    print(i, v)

my_str  = "ABCD"
print({v:i for i, v in enumerate(my_str)})


# zip
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

print([[a,b] for a, b in zip(alist, blist)])


# enumerate & zip

for i, value in enumerate(zip(alist, blist)):
    print(i, value)