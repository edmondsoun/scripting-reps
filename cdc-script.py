""" PLAN FOR SCRIPT:

Needs to run every 24hrs
Needs to send a query that limits the returned information to that 24 hour period:
    can do w/ query params
    
Write that 24 period's worth of information to appropriately coded file
*A DIFFERENT script will then parse that information and update our DB

Idea for improvement: ping API for latest update and use this as lower bound timestamp?
Because otherwise this may miss data if updates are not consistent day to day

"""

# ENV SETUP
import os
from dotenv import load_dotenv

# SOCRATA DEPENDENCIES
import pandas as pd
from sodapy import Socrata

load_dotenv()

API_TOKEN = os.environ['TOKEN']
DATA_URL = "data.oaklandca.gov"
DATA_SET = "ppgh-7dqv"

client = Socrata(DATA_URL, API_TOKEN)

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get(DATA_SET,
                    where="""
                        date_diff_d(to_floating_timestamp(get_utc_date(), 'UTC'), `datetime`) <= 1 
                        AND date_diff_d(to_floating_timestamp(get_utc_date(), 'UTC'), `datetime`) > 0""",
                    order="datetime ASC"
                    )

print(results)
# print(START_DATE)