#!/usr/bin/env python3

import calendar
import datetime 
import json
import re
import time

from skyfield.api import load

def check_retro(planet, t1):
    # fetch data from the United States Naval Observatory and the International Earth Rotation Service
    planets = load('de421.bsp')
    # planets = load('de440.bsp')
    # planets = load('de441.bsp')
    # define planets earth and target planet 
    earth, target_planet = planets['earth'], planets[planet]

    # Load a timescale so that we can translate between different systems for expressing time
    ts = load.timescale(builtin=True)

    # Set times 1 and 2 as terrestrial time
    # precise_second_t1 = float(t1.strftime("%-S.%f"))

    t2 = t1 + datetime.timedelta(minutes=5)
    # precise_second_t2 = float(t2.strftime("%-S.%f"))
    #t1 = datetime.datetime.utcnow() - datetime.timedelta(minutes=5)

    # Sanity check for times
    #print(t1.year, t1.month, t1.day, t1.hour, t1.minute, precise_second_t1)
    #print(t2.year, t2.month, t2.day, t2.hour, t2.minute, precise_second_t2)

    # setting times 1 and 2 as terrestrial times
    ttime1 = ts.utc(t1.year, t1.month, t1.day, t1.hour, t1.minute)
    ttime2 = ts.utc(t2.year, t2.month, t2.day, t2.hour, t2.minute)
    # ttime1 = ts.utc(t1.year, t1.month, t1.day, t1.hour, t1.minute, precise_second_t1)
    # ttime2 = ts.utc(t2.year, t2.month, t2.day, t2.hour, t2.minute, precise_second_t2)
    # ttime2 = ts.now()
    # sanity check for times 1 and 2 terrestrial time for when mercury is not in retrograde
    #ttime1 = ts.utc(2020, 4, 1, 12, 0, 0)
    #ttime2 = ts.utc(2020, 4, 1, 12, 5, 0)

    # get atrometric measurements from earth to mercury at times 1 and 2
    astrometric1 = earth.at(ttime1).observe(target_planet)
    astrometric2 = earth.at(ttime2).observe(target_planet)

    """
     set values from astrometric arrays
        ra = right ascension
        dec = decline
        ditance = distance
    """
    ra1, dec1, distance1 = astrometric1.radec()
    ra2, dec2, distance2 = astrometric2.radec()

    # Split arrays to pull only the numeric values
    arr1 = re.sub(r'[a-zA-Z]+', '', str(ra1)).split()
    arr2 = re.sub(r'[a-zA-Z]+', '', str(ra2)).split()

    ftr = [3600,60,1]

    # Get Angle outputs in seconds
    time1_seconds = sum([a*b for a,b in zip(ftr, map(float,arr1))])
    time2_seconds = sum([a*b for a,b in zip(ftr, map(float,arr2))])

    # get difference in RAs between times
    ra_diff = float(time2_seconds - time1_seconds)

    # interpret output of differences in RAs
    if ra_diff < 0.000000:
        # MercRet = "The right ascension of Mercury is negative: Mercury is in retrograde"
    	is_retro = True
    elif ra_diff > 0.000000:
        # MercRet = "The right ascension of Mercury is positive: Mercury is not in retrograde"
    	is_retro = False 
    else:
	    # MercRet = "The stars are not aligned. I cannot tell if Mercury is in retrograde at the present time. Please come back later."
	    # I'm putting this in as False because I need a binary
        # MercRet = "The stars are not alligned"
        is_retro = False 
        
    return is_retro 

planets = [
        (1, "mercury"), 
        (2, "venus"), 
        (4, "mars"), 
        (5, "jupiter"), 
        (6, "saturn"), 
        (7, "uranus"), 
        (8, "neptune"), 
        (9, "pluto"), 
        (301, "moon") 
    ]

data = {"dates": {}}

for year in range(2000, 2005):
    start_date  = datetime.datetime(year, 1, 1, 12, 0, 0, 0, datetime.timezone.utc)
    days = 365
    if calendar.isleap(year):
        days = 366
    for offset in range(0, days):
        d = start_date + datetime.timedelta(offset)
        details = {}
        for planet in planets:
            details[planet[1]] = check_retro(planet[0], d)
        data["dates"][d.strftime("%Y-%m-%d")] = details

with open('retrograte.json', 'w') as _out:
    json.dump(data, _out, sort_keys=True, indent=2)

