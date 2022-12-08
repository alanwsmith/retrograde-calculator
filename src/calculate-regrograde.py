#!/usr/bin/env python3

import json
import datetime, time, re

# from datetime import timedelta
from skyfield.api import load


def get_planet_retrograde(planet, t1):
    # fetch data from the United States Naval Observatory and the International Earth Rotation Service
    planets = load('de421.bsp')
    # planets = load('de440.bsp')
    # planets = load('de441.bsp')
    # define planets earth and target planet 
    earth, target_planet = planets['earth'], planets[planet]

    # Load a timescale so that we can translate between different systems for expressing time
    ts = load.timescale(builtin=True)

    # Set times 1 and 2 as terrestrial time
    precise_second_t1 = float(t1.strftime("%-S.%f"))

    t2 = t1 + datetime.timedelta(minutes=5)
    precise_second_t2 = float(t2.strftime("%-S.%f"))
    #t1 = datetime.datetime.utcnow() - datetime.timedelta(minutes=5)

    # Sanity check for times
    #print(t1.year, t1.month, t1.day, t1.hour, t1.minute, precise_second_t1)
    #print(t2.year, t2.month, t2.day, t2.hour, t2.minute, precise_second_t2)

    # setting times 1 and 2 as terrestrial times
    ttime1 = ts.utc(t1.year, t1.month, t1.day, t1.hour, t1.minute, precise_second_t1)
    ttime2 = ts.utc(t2.year, t2.month, t2.day, t2.hour, t2.minute, precise_second_t2)
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
    RA_diff = float(time2_seconds - time1_seconds)

    # interpret output of differences in RAs
    if RA_diff < 0.000000:
        # MercRet = "The right ascension of Mercury is negative: Mercury is in retrograde"
    	MercRet = "Yes"
    elif RA_diff > 0.000000:
        # MercRet = "The right ascension of Mercury is positive: Mercury is not in retrograde"
    	MercRet = "No"
    else:
        MercRet = "The stars are not alligned"
	# MercRet = "The stars are not aligned. I cannot tell if Mercury is in retrograde at the present time. Please come back later."
        
    return MercRet


planets = ['mercury', 'venus', 'mars', 'MARS', 'moon', 'JUPITER BARYCENTER', 7, 8, 9]

#R, 1 MERCURY BARYCENTER, 2 VENUS BARYCENTER, 3 EARTH BARYCENTER, 4 MARS BARYCENTER, 5 JUPITER BARYCENTER,
#6 SATURN BARYCENTER, 7 URANUS BARYCENTER, 8 NEPTUNE BARYCENTER, 9 PLUTO BARYCENTER, 10 SUN, 199 MERCURY, 3
#99 EARTH, 299 VENUS, 301 MOON, 499 MARS"


planets = [(1, "mercury"), (2, "venus"), (4, "mars"), (5, "jupiter"), (6, "saturn"), (7, "uranus"), 
           (8, "neptune"), (9, "pluto") ]

data = {}

today = datetime.datetime.now()

for planet in planets:
    retrogrades = []
    for i in range (0, 100):
        new_date = today + datetime.timedelta(i)
        retrogrades.append({
            "date":
                new_date.strftime("%Y-%m-%d"), 
            "retrograde":
                get_planet_retrograde(
                    planet[0], new_date
                )
            })
    #print(retrogrades)
    data[planet[1]] = retrogrades

with open('retrograte.json', 'w') as _out:
    json.dump(data, _out)

# print(data)


# via: https://github.com/G-Street/is-mercury-in-retrograde/blob/master/astro.py





