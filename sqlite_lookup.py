import sqlite3
from datetime import datetime, timedelta
from generate_random_msisdn import generate_msisdn


#############
## Part 1 ###
#############

start_time = datetime.now()

con = sqlite3.connect('MSISDNs.db')
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS MSISDNs (MSISDN TEXT NOT NULL);""")
cursor.execute("""CREATE INDEX IF NOT EXISTS idx_msisdn ON MSISDNs(MSISDN);""")
cursor.execute("delete from MSISDNs;")

msisdn_reader = open('MSISDNs.txt').readlines()
for elem in msisdn_reader:
    cursor.execute("INSERT INTO MSISDNs (MSISDN) VALUES (?)", (elem,))
    con.commit()

end_making_sqlite = datetime.now()
part_1_time = end_making_sqlite - start_time
##############
### Part 2 ###
##############

# Make 10 milion lookup process from bloom filter,
number_of_lookups = 1000000
for i in range(number_of_lookups):
    country_code = "+21899"  # US country code
    total_length = 13  # Total MSISDN length, including country code
    count = 1  # Number of MSISDNs to generate
    random_msisdns = generate_msisdn(country_code, total_length, count)[0]
    cursor.execute("select count(1) from MSISDNs where MSISDN = ? ",(random_msisdns,))
    cursor.fetchone()

end_time_lookup_process = datetime.now()
part_2_time = end_time_lookup_process - end_making_sqlite

########
log_file = open('log_file.txt','a')
log_file.write('SQLITE,'+str(part_1_time)+','+str(part_2_time)+'\n')
print('Total Time Creating SQLITE is',part_1_time)
print('Total Time Lookup process of SQLITE is',part_2_time)