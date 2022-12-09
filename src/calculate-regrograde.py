#!/usr/bin/env python3


import datetime
import json
import numpy as np 
import matplotlib.pyplot as plt

from skyfield.api import load

planets = load('de421.bsp')
earth = planets['earth']
scale = load.timescale(builtin=True)

def is_retro(target_planet, date):
    target = planets[target_planet]

    time_alfa = scale.utc(date)
    time_bravo = scale.utc(date + datetime.timedelta(minutes=5))

    lat_alfa, lon_alfa, dist_alfa = earth.at(time_alfa).observe(target).ecliptic_latlon()
    lat_bravo, lon_bravo, dist_bravo = earth.at(time_bravo).observe(target).ecliptic_latlon()

    num_alfa = (180./np.pi) * lon_alfa.radians
    num_bravo = (180./np.pi) * lon_bravo.radians

    if num_alfa < num_bravo:
        return False
    else:
        return True

if __name__ == "__main__":

    data = {
        "dates": {}
    }

    planet_list = [
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

    start_date  = datetime.datetime(2022, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)
    for i in range(0, 365):
        date = start_date + datetime.timedelta(i)
        details = {}
        for planet in planet_list:
            details[planet[1]] = is_retro(planet[0], date)
        data["dates"][date.strftime("%Y-%m-%d")] = details

    with open("retrogrades.json", "w") as _out:
        json.dump(data, _out, sort_keys=True, indent=2)

