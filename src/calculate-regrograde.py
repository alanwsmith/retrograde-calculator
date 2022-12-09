#!/usr/bin/env python3

import json
import numpy as np 
import matplotlib.pyplot as plt
import os
import sys

from datetime import datetime, timedelta, timezone
from pathlib import Path
from skyfield.api import load


script_dir = sys.path[0]
data_dir = os.path.abspath(os.path.join(script_dir, "..", "data"))

planets = load('de440s.bsp')
earth = planets['earth']
scale = load.timescale(builtin=True)


def get_rads(date, target):
    t = scale.utc(date)
    lat, lon, dist = earth.at(t).observe(target).ecliptic_latlon()
    return (180./np.pi) * lon.radians


def is_retro(target_object, date):
    target = planets[target_object]

    alfa = get_rads(date, target)
    bravo = get_rads(date + timedelta(hours=1), target)

    if alfa < bravo:
        return False
    else:
        return True 


if __name__ == "__main__":

    data = {"dates": {}}

    planet_list = [
        (1, "mercury"), (2, "venus"), (4, "mars"), (5, "jupiter"), 
        (6, "saturn"), (7, "uranus"),  (8, "neptune"), 
        (9, "pluto"), (301, "moon") 
    ]

    print(data_dir)

    start_date  = datetime(2000, 1, 1, 0, 0, 0, 0, timezone.utc)
    for i in range(0, 36890):
        date = start_date + timedelta(i)
        date_dir = os.path.join(data_dir, str(date.year), str(date.month), str(date.day))
        Path(date_dir).mkdir(parents=True, exist_ok=True)
        details = {}
        for planet in planet_list:
            value = is_retro(planet[0], date)
            details[planet[1]] = value

            planet_json = { "retrograte": value }
            planet_file = os.path.join(date_dir, f"{planet[1]}.json")
            print(planet_file)

            with open(planet_file, 'w') as _planet:
                json.dump(planet_json, _planet)

        data["dates"][date.strftime("%Y-%m-%d")] = details

    with open("retrogrades.json", "w") as _out:
        json.dump(data, _out)

