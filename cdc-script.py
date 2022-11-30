""" PLAN FOR SCRIPT:

Needs to run every 24hrs
Needs to send a query that limits the returned information to that 24 hour period:
    can do w/ query params
    
Write that 24 period's worth of information to appropriately coded file
*A DIFFERENT script will then parse that information and update our DB

"""

import pandas as pd
from datetime import datetime, timedelta
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.oaklandca.gov", None)

START_DATE = datetime.now() - timedelta(days=1)
# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.oaklandca.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("ppgh-7dqv",
                    where="""
                        date_diff_d(to_floating_timestamp(get_utc_date(), 'UTC'), `datetime`) <= 1 
                        AND date_diff_d(to_floating_timestamp(get_utc_date(), 'UTC'), `datetime`) >= 0""",
                    order="datetime ASC"
                    )

# Convert to pandas DataFrame
print(results)

print(START_DATE)