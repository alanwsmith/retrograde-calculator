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

# via: https://github.com/G-Street/is-mercury-in-retrograde/blob/master/astro.py

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
