#!/usr/local/bin/python3 
# Add it as a system tool: mv tzme.py tzme; chmod +x tzme; mv tzme /usr/local/bin/
from datetime import datetime
from pytz import timezone

fmt = "%H:%M %Y-%m-%d"
timezonelist = ['Europe/Berlin','Europe/London','UTC','US/Eastern','US/Pacific']
for zone in timezonelist:

    nownow = datetime.now(timezone(zone))
    print(nownow.strftime(fmt), zone )