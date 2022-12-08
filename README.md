# Retrograde Calculator

Figuring out what's in retrograde and when

## Notes

This is code is largely a copy of [G-Street/is-mercury-in-retrograte](https://github.com/G-Street/is-mercury-in-retrograde)

That source makes the determination for Mercury at a specific time.

The alterations I made are to produce a JSON file that denotes
the status for all the planets (and the moon) for every day of the
year from 2000 until 2050 with the aim of powering an API.

Because celestial bodies move with a fairly high degree of
consistency I'm precalculating all the data. The results are lower
resolution than if the calculation was made second by second, but
it'll be pretty close.

Each entry is made by calculating the result from noon UTC on the
given day.


## Data File Keys

These are keys from the `de421.bsp` data file that
were used for reference.

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

## References

I didn't use all of these, but they're what I ended
up having open so dropping them here.

-   [G-Street/is-mercury-in-retrograte](https://github.com/G-Street/is-mercury-in-retrograde) - This is the place I pull the source code from that I tweaked to produce the JSON.
-   https://www.popsugar.com/smart-living/what-planets-are-retrograde-right-now-48669539 - This had a list of dates I used to validate the output from the script.
-   [Mathematically calculate if a Planet is in Retrograde](https://astronomy.stackexchange.com/q/18832)
-   https://rhodesmill.org/skyfield/api.html#osculating-orbital-elements
-   https://towardsdatascience.com/space-science-with-python-quite-around-the-sun-6faa206a1210
-   https://rhodesmill.org/skyfield/planets.html
-   https://rhodesmill.org/skyfield/positions.html
-   https://rhodesmill.org/skyfield/api-topos.html#skyfield.toposlib.GeographicPosition
-   https://astronomy.stackexchange.com/q/24012
-   https://rhodesmill.org/skyfield/
-   https://rhodesmill.org/skyfield/api.html
-   https://rhodesmill.org/skyfield/api-iokit.html
-   https://rhodesmill.org/skyfield/api-ephemeris.html
-   https://rhodesmill.org/skyfield/planets.html
-   https://rhodesmill.org/skyfield/planets.html#ephemeris-download-links
-   https://docs.python.org/3/library/calendar.html
