
number_of_lookups = 1000000

for i in range(10):
    exec(open('list_lookup.py').read())
    exec(open('set_lookup.py').read())
    exec(open('BloomFilter_lookup.py').read())
    exec(open('sqlite_lookup.py').read())