import pickle
from datetime import datetime, timedelta
from generate_random_msisdn import generate_msisdn


#############
## Part 1 ###
#############
start_time = datetime.now()

MSISDNs_list = []

msisdn_reader = open('MSISDNs.txt').readlines()
for elem in msisdn_reader:
    MSISDNs_list.append(elem)

with open("MSISDNs_list.pik", "wb") as file:  # Use 'wb' for writing in binary mode
    pickle.dump(MSISDNs_list, file)


end_time_creating_list = datetime.now()
part_1_time = end_time_creating_list - start_time
##############
### Part 2 ###
##############

with open("MSISDNs_list.pik", "rb") as file:  # Use 'wb' for writing in binary mode
    MSISDNs_list = pickle.load(file)

# Make 10 milion lookup process from bloom filter,
#number_of_lookups = 1000000
for i in range(number_of_lookups):
    country_code = "+21899"  # US country code
    total_length = 13  # Total MSISDN length, including country code
    count = 1  # Number of MSISDNs to generate
    random_msisdns = generate_msisdn(country_code, total_length, count)[0]
    look_for_msisdn = random_msisdns in MSISDNs_list

end_time_lookup_process = datetime.now()
part_2_time = end_time_lookup_process - end_time_creating_list

log_file = open('log_file.txt','a')
log_file.write('LIST,'+str(part_1_time)+','+str(part_2_time)+'\n')
print('Total Time Creating List is',part_1_time)
print('Total Time Lookup process of List is',part_2_time)