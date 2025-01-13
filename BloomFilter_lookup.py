from bloom_filter import BloomFilter
import pickle
from datetime import datetime, timedelta
from generate_random_msisdn import generate_msisdn

#############
## Part 1 ###
#############
start_time = datetime.now()
# Create a Bloom Filter with a desired capacity and error rate
capacity = 1000000  # The maximum number of items you expect to store
error_rate = 0.001  # The acceptable false positive probability
bloom = BloomFilter(max_elements=capacity, error_rate=error_rate)
# Read from previous generated MSISDNs list and add them to bloom filter instance
msisdn_reader = open('MSISDNs.txt').readlines()
for elem in msisdn_reader:
    bloom.add(elem)

# Save the Bloom Filter to a file
with open("MSISDNs_bloom_filter.pik", "wb") as file:  # Use 'wb' for writing in binary mode
    pickle.dump(bloom, file)

end_time_creating_bloom = datetime.now()
part_1_time = end_time_creating_bloom - start_time
##############
### Part 2 ###
##############

# Load the Bloom Filter from a file
with open("MSISDNs_bloom_filter.pik", "rb") as file:  # Use 'rb' for reading in binary mode
    bloom = pickle.load(file)

# Make 10 milion lookup process from bloom filter,
# number_of_lookups = 1000000
for i in range(number_of_lookups):
    country_code = "+21899"  # US country code
    total_length = 13  # Total MSISDN length, including country code
    count = 1  # Number of MSISDNs to generate
    random_msisdns = generate_msisdn(country_code, total_length, count)[0]
    look_for_msisdn = random_msisdns in bloom # Return True or False if the MSISDN exist in the Bloom Filter


end_time_lookup_process = datetime.now()
part_2_time = end_time_lookup_process - end_time_creating_bloom

log_file = open('log_file.txt','a')
log_file.write('BLOOM,'+str(part_1_time)+','+str(part_2_time)+'\n')
print('Total Time Creating Bloom Filter is',part_1_time)
print('Total Time Lookup process of Bloom Filter is',part_2_time)