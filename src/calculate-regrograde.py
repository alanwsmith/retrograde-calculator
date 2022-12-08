#!/usr/bin/env python3

import calendar
import datetime 
import json
import re
import time

from skyfield.api import load

def check_retro(planet, t1):

    # Fetch data from the United States Naval Observatory 
    # and the International Earth Rotation Service
    planets = load('de440s.bsp')

    # Setup earth and target planet 
    earth, target_planet = planets['earth'], planets[planet]

    # Load a timescale so that we can translate 
    # between different systems for expressing time
    ts = load.timescale(builtin=True)

    # Create a new time with a delta for comparison
    t2 = t1 + datetime.timedelta(minutes=5)

    # Move to terrestrial times
    ttime1 = ts.utc(t1.year, t1.month, t1.day, t1.hour, t1.minute)
    ttime2 = ts.utc(t2.year, t2.month, t2.day, t2.hour, t2.minute)

    # Get atrometric measurements 
    astrometric1 = earth.at(ttime1).observe(target_planet)
    astrometric2 = earth.at(ttime2).observe(target_planet)

    # Load: right ascension (ra),
    # decline (dec), and distance (dist)
    ra1, dec1, dist1 = astrometric1.radec()
    ra2, dec2, dist2 = astrometric2.radec()

    # Split arrays to pull only the numeric values
    arr1 = re.sub(r'[a-zA-Z]+', '', str(ra1)).split()
    arr2 = re.sub(r'[a-zA-Z]+', '', str(ra2)).split()

    ftr = [3600,60,1]

    # Get Angle outputs in seconds
    time1_seconds = sum([a*b for a,b in zip(ftr, map(float,arr1))])
    time2_seconds = sum([a*b for a,b in zip(ftr, map(float,arr2))])

    # Find difference in RAs between times
    ra_diff = float(time2_seconds - time1_seconds)

    # Interpret output of differences in RAs
    if ra_diff < 0.000000:
        # In retrograde
    	is_retro = True
    elif ra_diff > 0.000000:
        # Not in retrograte
    	is_retro = False 
    else:
        # Not aligned (leaving this for possible 
        # third display value that was used in source)
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

for year in range(2000, 2101):
    print(f"Calculating year: {year}")
    start_date  = datetime.datetime(year, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)
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

