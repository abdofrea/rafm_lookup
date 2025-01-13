import random

def generate_msisdn(country_code="+1", total_length=12, count=10):
    """
    Generate random MSISDNs.

    :param country_code: The country code as a string (default is '+1').
    :param total_length: The total length of the MSISDN, including the country code.
    :param count: The number of MSISDNs to generate.
    :return: A list of randomly generated MSISDNs.
    """
    msisdns = []
    number_length = total_length - len(country_code)

    if number_length <= 0:
        raise ValueError("Total length must be greater than the length of the country code.")

    for _ in range(count):
        # Generate a random number with the specified number of digits
        random_number = ''.join(random.choices("0123456789", k=number_length))
        msisdns.append(f"{country_code}{random_number}")

    return msisdns

# Example usage
# country_code = "+21899"   # US country code
# total_length = 13     # Total MSISDN length, including country code
# count = 1000000             # Number of MSISDNs to generate

# random_msisdns = generate_msisdn(country_code, total_length, count)
# output_file = open('MSISDNs.txt','w')
# for msisdn in random_msisdns:
#     output_file.write(str(msisdn)+'\n')
#     print(msisdn)