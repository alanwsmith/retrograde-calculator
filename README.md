# Retrograde Calculator

Figuring out what's in retrograde and when

## Overview

This project produces a JSON file the identifies if a planet
(or the moon) is in retrograde on any given day between
Jan. 1, 2000 and Dec. 31, 2100.

The calculations were made for midnight UTC time each day.

## Data File Keys

The data comes from the `de440s.bsp` file. The keys in that
file are:

```
1 MERCURY BARYCENTER
2 VENUS BARYCENTER
3 EARTH BARYCENTER
4 MARS BARYCENTER
5 JUPITER BARYCENTER
6 SATURN BARYCENTER
7 URANUS BARYCENTER
8 NEPTUNE BARYCENTER
9 PLUTO BARYCENTER
10 SUN
199 MERCURY
99 EARTH
299 VENUS
301 MOON
499 MARS
```

The project uses the `BARYCENTER` for each planent. The moon
is pulled from the only available source (key: 301).


## Validation

The code identifies Mercury as being in retrograde from:

- 2022-12-30 ~ 2023-01-18

Other sources list the following

- 2022-12-29 ~ 2023-01-18 - [Source](https://www.popsugar.com/smart-living/what-planets-are-retrograde-right-now-48669539)

- 2022-12-22 ~ 2023-01-18 - [Source](https://www.lifestyleasia.com/ind/astrology/last-mercury-retrograde-2022-how-to-survive-it/)

- 2022-12-28 ~ 2023-01-18 - [Source](https://www.almanac.com/content/mercury-retrograde-dates)

The specific dates float around each other, but the overall blocks of time
line up. Given that there doesn't seem to be a definitive source
this takes the validaiton as far as I know how. 


## References

I didn't use all of these, but they're what I ended
up having open so dropping them here.

-   [Mathematically calculate if a Planet is in Retrograde](https://astronomy.stackexchange.com/q/18832) - This is the page that I used to figure out the formula from.
-   https://www.popsugar.com/smart-living/what-planets-are-retrograde-right-now-48669539
-   https://rhodesmill.org/skyfield/api.html#osculating-orbital-elements
-   https://towardsdatascience.com/space-science-with-python-quite-around-the-sun-6faa206a1210
-   https://rhodesmill.org/skyfield/planets.html
-   https://rhodesmill.org/skyfield/positions.html
-   https://rhodesmill.org/skyfield/api-topos.html#skyfield.toposlib.GeographicPosition
-   https://astronomy.stackexchange.com/q/24012
-   https://github.com/G-Street/is-mercury-in-retrograde
-   https://rhodesmill.org/skyfield/
-   https://rhodesmill.org/skyfield/api.html
-   https://rhodesmill.org/skyfield/api-iokit.html
-   https://rhodesmill.org/skyfield/api-ephemeris.html
-   https://rhodesmill.org/skyfield/planets.html
-   https://rhodesmill.org/skyfield/planets.html#ephemeris-download-links
-   https://docs.python.org/3/library/calendar.html
