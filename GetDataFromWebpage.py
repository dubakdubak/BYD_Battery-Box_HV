import requests
from lxml import html

# URL of the target page that asks for authentication
target_url = 'http://192.168.1.133/asp/StatisticInformation.asp'  # Replace with actual target URL

# Your login credentials
username = 'installer'
password = 'byd@12345'

# Send a GET request with the credentials for basic authentication
response = requests.get(target_url, auth=(username, password))

# Check if the request was successful
if response.ok:
    # Parse the target page's content
    tree = html.fromstring(response.text)

    # Locate the general information table
    general_info_table = tree.xpath('//table[@class="common_table"]')  # Adjust XPath if needed

    if general_info_table:
        # Initialize an empty dictionary to store key-value pairs
        data_dict = {}

        # Find all rows in the table
        rows = general_info_table[0].xpath('.//tr')

        # Loop through each row to extract key and value
        for row in rows:
            # Extract the key (column name or label), which might be in <td> or <th>
            key_elements = row.xpath('.//td[2]//text()')
            value_elements = row.xpath('.//td[3]//text()')

            if key_elements and value_elements:
                # Clean up the text and assign to dictionary
                key = key_elements[0].strip()
                value = float(value_elements[0].strip().replace('\xa0\xa0KWH',''))
                data_dict[key] = value

        # Print the resulting dictionary
        print(data_dict)

    else:
        print("General Information table not found.")
else:
    print("Failed to authenticate or access the page.")
