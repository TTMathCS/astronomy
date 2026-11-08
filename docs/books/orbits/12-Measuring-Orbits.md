# 12. Measuring orbits

*An orbit is only as good as the measurements behind it. This chapter follows how a few dots on the sky became a
whole orbit, how Gauss found a lost planet with a new kind of arithmetic, and how radar echoes, radio from spacecraft
and lasers fired at the Moon now pin the planets down. Mars, with its landers and orbiters, has become the anchor for
the whole inner solar system.*

!!! abstract "In this chapter"
    **You will learn:**

    - why a telescope gives the direction to a planet but not its distance
    - how Gauss found Ceres again in 1801, and what "least squares" means
    - how radar echoes from Venus fixed the size of the solar system in 1961
    - how dishes round the world follow a spacecraft by its distance, its Doppler shift and its direction
    - why the astronomical unit has been an exact number of metres since 2012
    - how one huge fit of the whole solar system gives the planet tables, and how good they are
    - why radio from spacecraft at Mars pins down the orbits of all the inner planets
    - how to fit a straight line to scattered measurements

    **You need:** chapters 3, 4 and 5.

    **Levels:** 12.1 to 12.3 are beginner; 12.4 to 12.8 are intermediate; 12.9 is advanced; 12.10 is expert.

## 12.1 Dots on the sky { #sky }

Point a telescope at a planet and you can measure exactly where it is against the stars: two angles, like a longitude
and a latitude on the sky. What you cannot see is how far away it is. A planet that is near and slow and one that is
far and fast can make the same dot.

An orbit needs six numbers, its **elements**: its size, its shape, its tilt, which way the tilt faces, which way the
long axis points, and where the body is along the orbit at one moment (chapter 4,
[section 4.6](04-Ellipses.md#elements)). Each sighting gives two angles, so three sightings a few weeks apart give six
numbers, just enough. Turning them into an orbit is hard, because the distance is hidden, but Kepler's laws (chapter 3)
say how a body on any given orbit must move, and that is enough to work the orbit out.

Newton gave the first method, in the *Principia* of 1687, for a body moving on a path close to a parabola, from three
observations. Halley used it to work out the orbits of many comets, including the one named after him (history book,
[section 16.5](../history/16-Newton-Halley-and-Romer.md#halley)). Euler turned Newton's step-by-step method into
formulas in 1744, and Lambert, between 1761 and 1777, extended it to ellipses and hyperbolas.

??? note "Sources"
    - Newton's method of 1687 for a parabolic path from three observations, Halley's use of it for comets, Euler in
      1744, Lambert from 1761 to 1777, and three observations giving the six elements: Wikipedia,
      [Orbit determination](https://en.wikipedia.org/wiki/Orbit_determination) (weaker).
    - Two angles from each sighting, and the hidden distance: standard.

## 12.2 Gauss and the lost planet { #gauss }

On **1 January 1801** Giuseppe Piazzi, at the Palermo observatory in Sicily, found a faint "star" that moved. It was
**Ceres**, the first asteroid (history book, [section 17.4](../history/17-Herschel-and-the-Canals-of-Mars.md#rule)).
He followed it for 40 days before it went into the glare of the Sun. When it came out on the other side, nobody knew
where to look: 40 days was a tiny piece of an orbit that takes more than four years.

Carl Friedrich Gauss, then 24, invented a new way of working out an orbit from just three observations, and sent his
prediction to Franz Xaver von Zach. On **31 December 1801**, von Zach and Heinrich Olbers found Ceres close to where
Gauss said it would be. Other astronomers had made predictions too; only Gauss's worked.

Gauss also had a way to use **all** the observations, not just three, so that their small errors cancel as far as
possible. This is the **method of least squares** (section 12.3). Adrien-Marie Legendre was the first to publish it
clearly, in 1805, and the American Robert Adrain found it on his own in 1808. When Gauss published his method for
orbits in 1809, he said he had been using least squares since 1795, which started a quarrel over who came first. Gauss
went further than the others, though: he tied the method to the laws of chance and to the bell-shaped curve of errors
now called the normal distribution.

??? note "Sources"
    - Piazzi's discovery at Palermo on 1 January 1801, the 24-year-old Gauss's new method of orbit determination, von
      Zach, and the recovery by von Zach and Olbers on 31 December 1801 near the predicted position: Wikipedia,
      [Ceres (dwarf planet)](https://en.wikipedia.org/wiki/Ceres_(dwarf_planet)) (weaker).
    - Piazzi following Ceres for 40 days until it was lost in the Sun's glare, only Gauss's predictions succeeding,
      Legendre in 1805, Adrain in 1808, Gauss in 1809 and his claim to have used the method since 1795, the priority
      dispute, and the link to probability and the normal distribution: Wikipedia,
      [Least squares](https://en.wikipedia.org/wiki/Least_squares) (weaker).
    - Ceres's period: Kepler's third law with $a = 2.77$ AU (history book, section 17.4) gives 4.6 years, our
      arithmetic.

## 12.3 The best fit { #fit }

Every measurement is a little wrong. The air shimmers, clocks drift and telescopes shake. So a hundred measurements of
a planet never fit any one orbit exactly. Which orbit is best?

Gauss's answer: for any trial orbit, work out how far each measurement misses it. Square each miss, so that misses on
either side count the same and a big miss counts much more than a small one, and add up the squares. The **best**
orbit is the one that makes this total as small as possible. In practice you start from a rough orbit, find which
small changes to its six numbers shrink the total, make them, and repeat until the total stops shrinking.

- **More is better.** Random errors partly cancel. If each measurement is good to 1 km, a fit to 100 of them is good
  to roughly $1/\sqrt{100}$ of that, about 100 m (section 12.10). That is why modern orbits use thousands of
  measurements.
- **Bad measurements stand out.** One that misses by far more than the rest is usually a mistake, and can be checked
  or left out.

Today anyone in the world who sees an asteroid or a comet can send its position to the **Minor Planet Center**, which
collects these reports for the International Astronomical Union, works out the orbits and publishes them. It was set
up in 1947 at the University of Cincinnati under Paul Herget, and moved to the Smithsonian Astrophysical Observatory
in 1978. One of its jobs is to check whether a "new" asteroid is really an old one, by seeing whether it fits an orbit
already known.

??? note "Sources"
    - Least squares as making the sum of the squared misses as small as possible: Wikipedia, Least squares (above).
      Repeating small corrections, errors shrinking roughly as $1/\sqrt{N}$, and spotting bad measurements: standard.
    - The Minor Planet Center collecting observations from around the world, computing and publishing orbits under the
      IAU, set up at the University of Cincinnati in 1947 under Paul Herget and moved to the Smithsonian Astrophysical
      Observatory in 1978: Wikipedia, [Minor Planet Center](https://en.wikipedia.org/wiki/Minor_Planet_Center)
      (weaker).
    - Orbits used to check that a newly seen asteroid has not been found before: Wikipedia, Orbit determination
      (above).

## 12.4 Echoes { #radar }

A telescope gives direction. **Radar** gives distance. Send out a radio pulse, wait for the echo, and time the round
trip $t$. The pulse went there and back at the speed of light $c$, so the distance is

$$d = \frac{c\,t}{2}.$$

Because light is so fast, the timing has to be very good: a round trip timed wrongly by a millionth of a second puts
the distance out by 150 m (section 12.9). The physics lesson
[Ranging to Mars](https://physics.akadian.ca/topics/spacetime/level-6/06-ranging-to-mars.html) works through more
examples.

**Venus, 1961.** The size of the solar system in kilometres had always been the hard part (history book,
[section 16.4](../history/16-Newton-Halley-and-Romer.md#distance)). Kepler's laws give every distance in units of the
Earth's distance from the Sun, the **astronomical unit** (AU), but not the AU itself. Radar could measure it directly
by timing an echo from Venus. The first claims of Venus echoes, from Lincoln Laboratory and Jodrell Bank and from
Vladimir Kotelnikov of the Soviet Union, all agreed with the value then accepted, 149,467,000 km. They had been dug out
of weak, noisy signals by looking where the answer was expected, and they were wrong. The first certain echo was
caught by NASA's Jet Propulsion Laboratory (JPL) on **10 March 1961**. Two months of echoes gave an AU of
**149,598,500 ± 500 km**, 131,000 km more than the old value. Once the right answer was known, other groups found
matching echoes in their old recordings.

**Asteroids.** A telescope measures where an asteroid is on the sky; radar measures how far away it is and how fast
that distance is changing. Together they can often predict an asteroid's orbit decades, and sometimes centuries,
ahead, which is how astronomers check whether an asteroid such as 99942 Apophis could hit the Earth. Planetary radars
are rare. After the Arecibo dish collapsed in 2020, two were in regular use as of 2023: Goldstone in California and
Evpatoria on the Black Sea (book 2, [section 17.7](../light-and-telescopes/17-Radio-Telescopes.md#radar)).

??? note "Sources"
    - The early claims from Lincoln Laboratory, Jodrell Bank and Kotelnikov, all agreeing with the old value of
      149,467,000 km after heavy processing that used the expected value, and now known to be wrong; JPL's first
      certain detection on 10 March 1961, contact until 10 May 1961, the new value of 149,598,500 ± 500 km, and other
      groups then finding echoes in their archived data; optical and radar together predicting orbits decades or
      centuries ahead, Apophis; Arecibo's collapse in December 2020; Goldstone and Evpatoria in regular use as of 2023:
      Wikipedia, [Radar astronomy](https://en.wikipedia.org/wiki/Radar_astronomy) (weaker).
    - $d = ct/2$ and 150 m for a microsecond: standard, and the physics lesson above. The 131,000 km: our arithmetic,
      section 12.9.

## 12.5 Following a spacecraft { #tracking }

A spacecraft is easier to measure than a planet, because it answers back. It picks up a radio signal from Earth and
sends one straight back, much stronger than any echo. Three kinds of measurement are made.

- **Range.** Time the round trip, as with radar, to get the distance.
- **Doppler.** As the spacecraft moves towards or away from us, the frequency of the returned signal shifts (book 2,
  [chapter 8](../light-and-telescopes/08-The-Doppler-Shift.md)). The shift gives its speed along the line of sight.
- **Direction.** Two dishes far apart, on different continents, listen to the spacecraft at the same time. The
  difference between the moments the signal reaches each dish gives its direction. To take out the delays caused by
  the air, the same two dishes also measure a quasar, a far-off galaxy whose place in the sky is known very well,
  ideally within 10° of the spacecraft. This is **delta-DOR**, short for delta differential one-way ranging, and it
  uses the same idea as VLBI (book 2, [section 17.6](../light-and-telescopes/17-Radio-Telescopes.md#vlbi)). ESA calls
  it the most precise way now in use to find a spacecraft in deep space.

**Dishes round the world.** As the Earth turns, any one dish loses sight of a spacecraft for part of every day. So the
big networks place three stations about 120° apart in longitude, and one of them can always see it.

- **NASA's Deep Space Network:** Goldstone in California, near Madrid in Spain and near Canberra in Australia (book
  2, [section 2.9](../light-and-telescopes/02-The-Speed-of-Light.md#mars)).
- **The European Space Agency (ESA):** three dishes 35 m across, at New Norcia in Western Australia, Cebreros in
  Spain and Malargüe in Argentina, built in the 2000s; Malargüe opened in December 2012.
- **China's** network, first needed for the Chang'e 1 Moon mission, with stations at Kashgar and Jiamusi in China and
  in Neuquén Province, Argentina. It followed Tianwen-1 to Mars.
- **India's** Deep Space Network, at Byalalu near Bengaluru, whose 32 m dish served Chandrayaan-1 and the Mars Orbiter
  Mission.

The agencies lend each other time. NASA's dishes track Europe's Mars Express, and ESA's stations have supported
Japan's Hayabusa2 and India's Chandrayaan-3.

??? note "Sources"
    - Delta-DOR: two widely separated stations, the difference in arrival times giving the direction, Doppler giving
      the speed, a well-known quasar preferably within 10° tracked to correct for the air, and its use by NASA, ESA,
      China and India: Wikipedia, [Delta-DOR](https://en.wikipedia.org/wiki/Delta-DOR) (weaker).
    - ESA's plan of 1998 for three stations about 120° apart for continuous coverage, the three 35 m Deep Space
      Antennas at New Norcia, Cebreros and Malargüe built in the 2000s, Malargüe opened in December 2012, delta-DOR as
      the most precise technique now in use, NASA's support of Mars Express and ESA's of Hayabusa2 and Chandrayaan-3:
      ESA,
      [Estrack: ESA's global ground station network](https://www.esa.int/Enabling_Support/Operations/ESA_Ground_Stations/Estrack_ESA_s_global_ground_station_network).
    - NASA's three complexes: Wikipedia,
      [NASA Deep Space Network](https://en.wikipedia.org/wiki/NASA_Deep_Space_Network) (weaker).
    - China's network built for Chang'e 1, Kashgar, Jiamusi, the station in Neuquén Province and Tianwen-1: Wikipedia,
      [Chinese Deep Space Network](https://en.wikipedia.org/wiki/Chinese_Deep_Space_Network) (weaker).
    - India's network near Bengaluru, its 32 m antenna, Chandrayaan-1 and the Mars Orbiter Mission: Wikipedia,
      [Indian Deep Space Network](https://en.wikipedia.org/wiki/Indian_Deep_Space_Network) (weaker).
    - Quasars as fixed markers and the Doppler shift: this site's book 2, chapters 8 and 17.

## 12.6 A unit fixed by agreement { #au }

The AU took more than three hundred years to pin down.

| Year | How | Distance from the Earth to the Sun |
| --- | --- | --- |
| 1672 | Mars seen from Paris and Cayenne at once | about 138 million km |
| 1961 | radar echoes from Venus | 149,598,500 ± 500 km |
| 2009 | planet tables from JPL and Russia's IAA | 149,597,870.700 km, give or take 3 m |
| 2012 | fixed by the International Astronomical Union | exactly 149,597,870.700 km |

The steps in between included the transits of Venus of 1761 and 1769, watched by Tupaia and Cook at Tahiti among
many others (history book, [section 12.4](../history/12-Oceania-and-Australia.md#tupaia)), and the asteroid 433 Eros,
whose close passes in 1900–1901 and 1930–1931 gave better measurements than ever before.

From 1976 the AU had been defined through the Sun's gravity: the size of orbit in which a tiny body would go round the
Sun at a rate set by a number called the Gaussian gravitational constant, $k = 0.01720209895$. At the precision now
reached, that definition got tangled up in the corrections that Einstein's theory needs (chapter 18). So in 2012 the
IAU took the 2009 value and made it exact: **1 AU = 149,597,870,700 m**, just as the metre is fixed by the speed of
light. Light crosses one AU in 499.005 seconds, a little over 8 minutes 19 seconds.

??? note "Sources"
    - The 1976 definition through the Gaussian constant $k = 0.01720209895$, the best 2009 estimate of
      149,597,870,700 ± 3 m from JPL and IAA–RAS ephemerides, the light time of 499.0047838061 s, the 2012
      redefinition because building in relativity would have made the old one too complex, and Eros's passes of
      1900–1901 and 1930–1931: Wikipedia, [Astronomical unit](https://en.wikipedia.org/wiki/Astronomical_unit)
      (weaker).
    - 1672 and 138 million km: history book, section 16.4. The transits and Tupaia: history book, section 12.4. 1961:
      section 12.4 above.

## 12.7 The whole solar system in one fit { #ephemeris }

A table of where the planets will be is called an **ephemeris**. The best ones today come from fitting the whole
solar system at once. Start with the positions, speeds and masses of the Sun, the Moon and the planets at one moment.
Let a computer move them all forward in small steps, each pulling on all the others, with Einstein's small corrections
(chapter 18) and the pulls of hundreds of asteroids. Compare the result with every good measurement ever made, and
adjust the starting numbers by least squares until the misses are as small as they can be.

Three groups make such tables: NASA's JPL, whose DE tables have been revised almost every year since 1981; the
Institute of Applied Astronomy of the Russian Academy of Sciences, with its EPM tables; and the IMCCE at the Paris
Observatory, with INPOP.

JPL's report on its DE430 table, from 2014, lists what went in.

- **The Moon:** 18,369 laser ranges from 1969 to 2012, from observatories in Texas, Hawaii, the south of France,
  Italy and New Mexico (chapter 8, [section 8.5](08-Tides.md#slowing)). The earliest are good to about 25 cm, the
  latest to about 2 cm.
- **Mercury and Venus:** radar ranges from Arecibo, Goldstone, Haystack and Evpatoria, Evpatoria's going back to
  1962, and radio ranges to MESSENGER and Venus Express.
- **Mars:** 17,220 radio ranges to landers and orbiters, and VLBI fixes on its orbiters (section 12.8).
- **Jupiter and beyond:** a few passing spacecraft, and thousands of telescope positions from observatories
  such as Washington, Flagstaff, La Palma, Bordeaux and Nikolaev, some going back to 1908.
- **Asteroids:** the pulls of 343 of them.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="How well each orbit is known, on a scale where each step is ten times the last, from JPL's report on its planet tables DE430 and DE431. The Moon's orbit is known to under a metre, from lasers fired at mirrors on the Moon. The orbits of Mercury, Venus, the Earth and Mars are known to a few hundred metres, from radio ranging to spacecraft in orbit round them, tied to distant quasars. Jupiter and Saturn are known to tens of kilometres, from tracking the few spacecraft that went there. Uranus, Neptune and Pluto are known only to several thousand kilometres, from telescope positions blurred by the Earth's air.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">How well we know each orbit</text>
    <text x="6" y="42">the Moon</text>
    <rect x="112" y="34" width="15.2" height="11" fill="#5aa0d8"/>
    <text x="131.2" y="42">under a metre</text>
    <text x="112" y="56" fill="#555">lasers fired at mirrors on the Moon</text>
    <text x="6" y="84">Mercury, Venus,</text>
    <text x="6" y="93">Earth, Mars</text>
    <rect x="112" y="76" width="86.9" height="11" fill="#c1440e"/>
    <text x="202.9" y="84">a few hundred metres</text>
    <text x="112" y="98" fill="#555">radio ranging to orbiters, tied to quasars</text>
    <text x="6" y="126">Jupiter, Saturn</text>
    <rect x="112" y="118" width="144.9" height="11" fill="#5aa0d8"/>
    <text x="260.9" y="126">tens of kilometres</text>
    <text x="112" y="140" fill="#555">radio from the few craft that went there</text>
    <text x="6" y="168">Uranus, Neptune,</text>
    <text x="6" y="177">Pluto</text>
    <rect x="112" y="160" width="202.8" height="11" fill="#5aa0d8"/>
    <text x="310.8" y="168" text-anchor="end" fill="#fff">several thousand km</text>
    <text x="112" y="182" fill="#555">telescope positions, blurred by the air</text>
    <line x1="112" y1="202" x2="330" y2="202" stroke="currentColor" stroke-width="0.6"/>
    <line x1="127.2" y1="202" x2="127.2" y2="205" stroke="currentColor" stroke-width="0.6"/>
    <text x="127.2" y="213" text-anchor="middle">1 m</text>
    <line x1="156.1" y1="202" x2="156.1" y2="205" stroke="currentColor" stroke-width="0.6"/>
    <line x1="185.1" y1="202" x2="185.1" y2="205" stroke="currentColor" stroke-width="0.6"/>
    <text x="185.1" y="213" text-anchor="middle">100 m</text>
    <line x1="214.1" y1="202" x2="214.1" y2="205" stroke="currentColor" stroke-width="0.6"/>
    <line x1="243.1" y1="202" x2="243.1" y2="205" stroke="currentColor" stroke-width="0.6"/>
    <text x="243.1" y="213" text-anchor="middle">10 km</text>
    <line x1="272.0" y1="202" x2="272.0" y2="205" stroke="currentColor" stroke-width="0.6"/>
    <line x1="301.0" y1="202" x2="301.0" y2="205" stroke="currentColor" stroke-width="0.6"/>
    <text x="301.0" y="213" text-anchor="middle">1,000 km</text>
    <line x1="330.0" y1="202" x2="330.0" y2="205" stroke="currentColor" stroke-width="0.6"/>
    <text x="6" y="226">Each step along the bottom is ten times the last. The bar lengths stand for the words in</text>
    <text x="6" y="235">JPL's 2014 report on its planet tables, so their ends are rough. Red: Mars and the other inner</text>
    <text x="6" y="244">planets, pinned down by radio from spacecraft orbiting them.</text>
  </g>
</svg>
</div>

How good is the result? Figure A shows it. The Moon's orbit is known to under a metre. The orbits of the four inner
planets are known to a few hundred metres, from radio contact with spacecraft orbiting them. Jupiter and Saturn,
visited by fewer spacecraft, are known to tens of kilometres. Uranus, Neptune and Pluto have to rely mostly on
telescopes looking through the air, and are known only to several thousand kilometres. The next table, DE440 of 2021,
improved Jupiter, Saturn and Pluto with newer spacecraft data.

??? note "Sources"
    - JPL's DE ephemerides revised nearly every year since 1981, EPM from the Institute of Applied Astronomy of the
      Russian Academy of Sciences, and INPOP from the IMCCE: Wikipedia,
      [Ephemeris](https://en.wikipedia.org/wiki/Ephemeris) (weaker).
    - Numerical integration of all the bodies from starting conditions, relativistic corrections, and a least-squares
      fit to the observations; DE440 of 2021 improving Jupiter, Saturn and Pluto: Wikipedia,
      [Jet Propulsion Laboratory Development Ephemeris](https://en.wikipedia.org/wiki/Jet_Propulsion_Laboratory_Development_Ephemeris)
      (weaker).
    - The accuracies (the Moon to under a metre, the inner planets to under a kilometre and limited to a few hundred
      metres by the tie to the quasars, Jupiter and Saturn to tens of kilometres, Uranus, Neptune and Pluto to several
      thousand kilometres), the data in its tables 1 to 3, laser residuals of about 25 cm early and 2 cm lately, and the
      343 asteroids: W. M. Folkner, J. G. Williams, D. H. Boggs, R. S. Park and P. Kuchynka,
      [The Planetary and Lunar Ephemerides DE430 and DE431](https://ipnpr.jpl.nasa.gov/progress_report/42-196/196C.pdf),
      IPN Progress Report 42-196, NASA JPL, 2014. The totals of 18,369 and 17,220 are our sums from its tables. Where
      the observatories are: standard.

## 12.8 Measuring Mars { #mars }

In DE430 Mars has far more spacecraft ranges than any other planet: 17,220, against about 2,200 for Venus and under
250 for Mercury. Figure B shows where they came from.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The radio ranges to spacecraft at Mars that went into JPL's planet table DE430, mission by mission, from 1976 to 2013. Viking Lander 1, 1976 to 1982, 1,178 ranges. Viking Lander 2, 1976 to 1977, 80. Mars Pathfinder, 1997, 90. Mars Global Surveyor, 1999 to 2006, 3,067. Mars Odyssey, 2002 to 2012, 6,009. Mars Express, 2005 to 2013, 5,321. Mars Reconnaissance Orbiter, 2006 to 2012, 1,475. In all 17,220 ranges. Landers are drawn in red and orbiters in blue. After the Vikings there is a gap of fifteen years with no ranges in the table.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">Timing radio echoes from Mars, 1976 to 2013</text>
    <text x="6" y="38">Viking Lander 1</text>
    <rect x="116.7" y="30" width="32.9" height="10" fill="#c1440e"/>
    <text x="153.6" y="38">1,178</text>
    <text x="6" y="60">Viking Lander 2</text>
    <rect x="116.7" y="52" width="9.4" height="10" fill="#c1440e"/>
    <text x="130.1" y="60">80</text>
    <text x="6" y="82">Mars Pathfinder</text>
    <rect x="215.4" y="74" width="4.7" height="10" fill="#c1440e"/>
    <text x="224.1" y="82">90</text>
    <text x="6" y="104">Mars Global Surveyor</text>
    <rect x="224.8" y="96" width="37.6" height="10" fill="#5aa0d8"/>
    <text x="266.4" y="104">3,067</text>
    <text x="6" y="126">Mars Odyssey</text>
    <rect x="238.9" y="118" width="51.7" height="10" fill="#5aa0d8"/>
    <text x="294.6" y="126">6,009</text>
    <text x="6" y="148">Mars Express</text>
    <rect x="253.0" y="140" width="42.3" height="10" fill="#5aa0d8"/>
    <text x="299.3" y="148">5,321</text>
    <text x="6" y="170">Mars Reconnaissance Orb.</text>
    <rect x="257.7" y="162" width="32.9" height="10" fill="#5aa0d8"/>
    <text x="294.6" y="170">1,475</text>
    <line x1="112" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="0.6"/>
    <line x1="112.0" y1="190" x2="112.0" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="112.0" y="201" text-anchor="middle">1975</text>
    <line x1="135.5" y1="190" x2="135.5" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <line x1="159.0" y1="190" x2="159.0" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="159.0" y="201" text-anchor="middle">1985</text>
    <line x1="182.5" y1="190" x2="182.5" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <line x1="206.0" y1="190" x2="206.0" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="206.0" y="201" text-anchor="middle">1995</text>
    <line x1="229.5" y1="190" x2="229.5" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <line x1="253.0" y1="190" x2="253.0" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="253.0" y="201" text-anchor="middle">2005</text>
    <line x1="276.5" y1="190" x2="276.5" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <line x1="300.0" y1="190" x2="300.0" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="300.0" y="201" text-anchor="middle">2015</text>
    <text x="182.5" y="60.0" text-anchor="middle" fill="#555">no ranges in the table</text>
    <text x="6" y="226">Number of radio ranges to each spacecraft used in JPL's planet table DE430: 17,220 in all.</text>
    <text x="6" y="235">Red: landers, fixed to the ground; blue: orbiters. After the Vikings fell silent, the table has</text>
    <text x="6" y="244">no ranges from Mars for fifteen years.</text>
  </g>
</svg>
</div>

**Landers.** A lander sits still on the ground. Once its place on Mars is known, every range to it measures the
distance between two planets. Viking Lander 1 answered from 1976 to 1982, giving 1,178 ranges. They were so precise
that, when Mars was behind the Sun in 1976, they showed the signals arriving late, by up to about 250 millionths of a
second, because they had passed close to the Sun, just as Einstein's theory predicts (chapter 18).

**Orbiters.** Since 1999 orbiters have done most of the work: NASA's Mars Global Surveyor, Mars Odyssey and Mars
Reconnaissance Orbiter, and Europe's Mars Express. To use them, the orbiter's own path round Mars has to be worked out
too, from its Doppler tracking (section 12.5).

**The anchor.** VLBI fixes on three of these orbiters tie the whole JPL table to the distant quasars to within
0.0002″, two ten-thousandths of a second of arc. That small tilt is the biggest error left in the orbits of the
Earth, Venus, Mercury and Mars themselves, and it amounts to a few hundred metres (section 12.9). So spacecraft at
Mars do more than measure Mars: they hold the map of the inner solar system steady.

**Getting there.** Better tables mean safer arrivals. JPL's DE410 of 2003 was used to steer the Mars Exploration
Rovers, and DE414 added ranges to Mars Global Surveyor and Mars Odyssey up to 2003. Delta-DOR has been used for India's
Mars Orbiter Mission, and to guide Europe's ExoMars Trace Gas Orbiter on its way to Mars in 2016.

**Inside Mars.** The same radio tracking from landers shows how Mars spins and wobbles, and from that the size of its
core (book 2, [section 8.8](../light-and-telescopes/08-The-Doppler-Shift.md#mars)).

??? note "Sources"
    - The ranges to each spacecraft at Mars (Viking Lander 1, 1976 to 1982, 1,178; Viking Lander 2, 1976 to 1977, 80;
      Mars Pathfinder, 1997, 90; Mars Global Surveyor, 1999 to 2006, 3,067; Mars Odyssey, 2002 to 2012, 6,009; Mars
      Reconnaissance Orbiter, 2006 to 2012, 1,475; Mars Express, 2005 to 2013, 5,321), the VLBI on three orbiters, the
      ranges to Venus Express (2,158) and to Mariner 10 and MESSENGER (244), and the tie to the quasars at 0.0002″ as
      the limiting error for the inner planets: Folkner and others, DE430 (above).
    - The Viking ranging near the 1976 conjunction and the delay of up to about 250 microseconds: this site's physics
      lesson Ranging to Mars (above), which cites Shapiro and others, *The Viking relativity experiment*.
    - DE410 used for Mars Exploration Rover navigation, and DE414 fit to ranging from Mars Global Surveyor and Odyssey
      through 2003: NASA JPL, [Planetary and Lunar Ephemerides](https://ssd.jpl.nasa.gov/planets/eph_export.html).
    - Delta-DOR for the Mars Orbiter Mission and the ExoMars Trace Gas Orbiter: Wikipedia, Delta-DOR (above).
    - Mars's spin, wobble and core: this site's book 2, section 8.8, and its sources.

## 12.9 Working it out { #working }

**Ranging.** $d = ct/2$, with $c = 299{,}792$ km/s.

- A round trip of 20 minutes, 1,200 s: $d = 299{,}792 \times 1{,}200 / 2 = 180$ million km.
- A timing error of one microsecond: $299{,}792 \times 0.000001 / 2 = 0.15$ km, 150 m.
- For 1 m, the round trip must be timed to $2 \times 1 / 299{,}792{,}458 = 6.7$ billionths of a second.

**Mars.** At its nearest, 54.6 million km, a radio signal takes $54.6 \times 10^6 / 299{,}792 = 182$ s, about 3.0
minutes, one way; a round trip takes 6.1 minutes. At its farthest, 401.4 million km, it takes 22.3 minutes one way and
44.6 for the round trip.

**Doppler.** A signal sent out and back picks up the shift twice, so $\Delta f = 2 f v / c$. At $f = 8.4$ GHz, a
speed along the line of sight of 1 m/s gives $\Delta f = 2 \times 8.4 \times 10^9 \times 1 / 299{,}792{,}458 = 56$ Hz.

**The AU.** $149{,}597{,}870{,}700 / 299{,}792{,}458 = 499.005$ s, or 8 minutes 19.0 seconds.

**Venus, 1961.** $149{,}598{,}500 - 149{,}597{,}870.7 = 629$ km, a little more than the stated ±500 km. The old value
was $149{,}597{,}871 - 149{,}467{,}000 = 130{,}871$ km too small, about 1 part in 1,100.

**The tie to the quasars.** One second of arc is $1/206{,}265$ of a radian, so at Mars's distance of 1.524 AU,
$0.0002″$ is $0.0002 / 206{,}265 \times 1.524 \times 1.496 \times 10^{11} = 221$ m. That is the "few hundred metres"
of Figure A.

| | Mars | Earth |
| --- | --- | --- |
| Mean distance from the Sun | 1.524 AU | 1.000 AU |
| Sunlight takes | 12.7 minutes | 8.3 minutes |
| Orbit known to (DE430) | a few hundred metres | a few hundred metres |
| Ranges in DE430 | 17,220 radio ranges to spacecraft at Mars, 1976–2013 | 18,369 laser ranges to the Moon, 1969–2012 |
| Radio round trip | 6 to 45 minutes from the Earth | 2.6 seconds to the Moon |

??? note "Sources"
    - The nearest and farthest distances of 54.6 and 401.4 million km, and Mars's mean distance: NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - The X band near 8.4 GHz: this site's book 2, section 17.8. The Moon's mean distance of 384,400 km, used for the
      round trip: standard. The rest are from sections 12.4 to 12.8; the arithmetic is ours.

## 12.10 Fitting a straight line { #squares }

Here is least squares worked out for the simplest case. We have $N$ measurements $y_i$ at times $t_i$ and want the
line $y = a + bt$ that fits them best. The misses are $r_i = y_i - a - b\,t_i$, and we want to make

$$Q = \sum_i r_i^2$$

as small as possible. At the lowest point, changing $a$ or $b$ a little does not change $Q$, so both derivatives are
zero:

$$\frac{\partial Q}{\partial a} = -2\sum_i r_i = 0, \qquad \frac{\partial Q}{\partial b} = -2\sum_i t_i\,r_i = 0.$$

The first says the misses add up to zero, so the line passes through the average point $(\bar t, \bar y)$. Putting
$a = \bar y - b\,\bar t$ into the second gives

$$b = \frac{\sum_i (t_i - \bar t)(y_i - \bar y)}{\sum_i (t_i - \bar t)^2}.$$

**An example.** Four measurements: $y = 2.0, 2.9, 4.2, 4.9$ at $t = 0, 1, 2, 3$. Then $\bar t = 1.5$ and
$\bar y = 3.5$. The top of the fraction is
$(-1.5)(-1.5) + (-0.5)(-0.6) + (0.5)(0.7) + (1.5)(1.4) = 5.0$ and the bottom is $2.25 + 0.25 + 0.25 + 2.25 = 5.0$, so
$b = 1.0$ and $a = 3.5 - 1.5 = 2.0$. The misses are $0, -0.1, +0.2, -0.1$, which add up to zero.

**Why more measurements help.** If each measurement has a random error of about $\sigma$, an average of $N$ of them
has an error of about $\sigma/\sqrt{N}$, and the fitted $a$ and $b$ behave the same way. A hundred times as many
measurements give an answer ten times better.

**From a line to an orbit.** An orbit is not a straight line, but near a good guess, a small change in any of its six
elements moves each predicted position almost in proportion. So near the guess the problem looks just like this one,
with six unknowns instead of two. Solve it, correct the guess, and repeat. This is Gauss's method in modern form, and
it is how DE430 was fitted, with many more unknowns: the starting positions and speeds of every planet and the Moon,
and many masses.

??? note "Sources"
    - The derivation, the $\sigma/\sqrt{N}$ rule and correcting a guess step by step: standard. That the JPL tables
      fit starting positions, speeds and masses by least squares: Wikipedia, Jet Propulsion Laboratory Development
      Ephemeris (above). The example is ours.

## Check yourself { #check }

**1.** (beginner) Why can one sighting through a telescope never tell you a planet's orbit?

??? note "Answer"
    It gives only the direction, two angles on the sky, not the distance. An orbit needs six numbers, so you need at
    least three sightings.

**2.** (beginner) How was Ceres lost in 1801, and how was it found again?

??? note "Answer"
    Piazzi followed it for 40 days before it went into the Sun's glare. Gauss worked out its orbit from three
    observations with a new method, and von Zach and Olbers found it near his prediction on 31 December 1801.

**3.** (beginner) In the method of least squares, what is made as small as possible?

??? note "Answer"
    The sum of the squares of the misses between the measurements and the orbit (or line) being fitted.

**4.** (intermediate) A radar echo from Venus comes back after 5 minutes. How far away is Venus?

??? note "Answer"
    $d = 299{,}792 \times 300 / 2 = 45$ million km.

**5.** (intermediate) Name three ways of measuring a spacecraft by radio, and what each one tells you.

??? note "Answer"
    Range, from the round-trip time, gives its distance. Doppler, from the shift in frequency, gives its speed along
    the line of sight. Delta-DOR, from the difference in arrival times at two far-apart dishes checked against a
    quasar, gives its direction.

**6.** (intermediate) Why are ESA's three deep-space dishes in Australia, Spain and Argentina?

??? note "Answer"
    They are about 120° apart in longitude, so as the Earth turns, at least one of them can always see a spacecraft.

**7.** (advanced) Mars is 225 million km away. How long does a radio round trip take, and how well must it be timed
to get the distance right to 1 m?

??? note "Answer"
    $2 \times 225 \times 10^9 / 299{,}792{,}458 = 1{,}501$ s, about 25 minutes. For 1 m, the timing must be good to
    $2 / 299{,}792{,}458 = 6.7$ billionths of a second, out of 1,501 s.

**8.** (expert) Fit the line $y = a + bt$ to the points $(0, 1.0)$, $(1, 2.9)$ and $(2, 5.2)$ by least squares.

??? note "Answer"
    $\bar t = 1$ and $\bar y = 9.1/3 = 3.033$. The top of the fraction is $(-1)(-2.033) + 0 + (1)(2.167) = 4.2$ and
    the bottom is $1 + 0 + 1 = 2$, so $b = 2.1$ and $a = 3.033 - 2.1 = 0.933$. The misses are $+0.067$, $-0.133$ and
    $+0.067$, which add up to zero.

## Summary

- A telescope gives a planet's direction but not its distance; three sightings give the six numbers an orbit needs.
- Gauss found the lost Ceres in 1801 and used least squares, which picks the orbit that makes the sum of the squared
  misses smallest. Legendre published the method first, in 1805.
- Radar measures distance as $d = ct/2$. Echoes from Venus in 1961 gave the AU as 149,598,500 ± 500 km, 131,000 km
  more than the old value.
- Spacecraft are measured by range, Doppler and delta-DOR, from networks of dishes in the United States, Spain,
  Australia, Argentina, China and India.
- Since 2012 the AU has been exactly 149,597,870,700 m.
- Planet tables such as JPL's DE, Russia's EPM and France's INPOP fit the whole solar system at once. The Moon is
  known to under a metre, the inner planets to a few hundred metres and the outermost planets to thousands of
  kilometres.
- Ranges and VLBI from landers and orbiters at Mars hold the whole inner solar system in place.

**Next:** chapter 13, Rockets and getting to orbit, where we leave the planets to themselves and work out what it
takes to launch something into orbit.

## Further reading

- Kitty Ferguson, *Measuring the Universe: Our Historic Quest to Chart the Horizons of Space and Time*, Walker and
  Company, 1999.
