#!/usr/bin/env python3
"""
Takes a screenshot of android phone and looks for certain key words
"""

#standard imports
import re

#3rd party imports

pattern = re.compile('(?<=node index=\"0\")(((?!OfferItemTimes).)*)\"Decline\".*?\"Claim\".*?bounds=\"\[\d+,\d+\]\[\d+,\d+\]\"')

with open('/home/wynand/4jobs.xml', 'r') as file:
    data = file.read()

all_offers = pattern.findall(data)
print(all_offers)

for offer in all_offers:
    location = re.findall('(?<=text=\").*?(?=\")', str(offer))[0]
    print(location)
