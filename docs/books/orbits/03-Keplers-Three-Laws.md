# 3. Kepler's three laws

*Johannes Kepler spent ten years fighting the orbit of Mars and came out with three short rules. They were meant for
the planets, but they turned out to work for everything that orbits anything: comets round the Sun, moons round
Jupiter, satellites round the Earth, spacecraft round Mars. This chapter states the three laws, shows each one at
work, and uses them to find the height of a satellite that hangs over one spot, the shape of the path to Mars, and how
long a comet spends near the Sun. It ends with Newton's short proof of why equal areas must be swept in equal times.*

!!! abstract "In this chapter"
    **You will learn:**

    - Kepler's three laws, in plain words
    - why comets travel on long, thin ellipses, and how little of its time Halley's comet spends near the Sun
    - why a planet moves fastest when it is nearest the Sun
    - how the squares of the years and the cubes of the distances line up, for every planet
    - that the same law works for moons and satellites, with a different number for each central body
    - how to find the height of a geostationary satellite from the Moon alone
    - why the path from the Earth to Mars takes about 259 days
    - how Kepler's laws shape the orbits of spacecraft at Mars
    - Newton's proof that any pull towards a fixed centre gives equal areas in equal times

    **You need:** chapters 1 and 2. The story of how Kepler found the laws is in the history book,
    [chapter 14](../history/14-Tycho-and-Kepler.md#mars).

    **Levels:** 3.1 to 3.3 are beginner; 3.4 to 3.8 are intermediate; 3.9 is advanced; 3.10 is expert.

## 3.1 Three rules { #rules }

Kepler published his laws between 1609 and 1621, after working through Tycho Brahe's measurements of Mars (history
book, [sections 14.7 and 14.8](../history/14-Tycho-and-Kepler.md#mars)).

1. **Ellipses.** Each planet moves on an ellipse, with the Sun at one focus. An ellipse is a stretched circle; the two
   foci are points inside it, on its long axis, equally far from the centre. The Sun sits at one of them. The other
   is empty.
2. **Equal areas.** The line from the Sun to the planet sweeps out equal areas in equal times. Near the Sun the line is
   short, so the planet has to move fast to sweep its share; far away the line is long, and it moves slowly.
3. **Squares and cubes.** The square of a planet's year is proportional to the cube of the size of its orbit. Measure
   years in Earth years and sizes in units of the Earth's distance from the Sun, and the rule becomes
   $P^2 = a^3$.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Kepler's first two laws on an ellipse stretched far more than any planet's orbit. The Sun sits at one focus, off to the right of the centre. Sixteen dots mark where the planet is at equal steps of time. Near the Sun, on the right, the dots are far apart because the planet moves fast; far from the Sun, on the left, they bunch together because it moves slowly. Two shaded wedges, each covering one step of time, one short and wide near the Sun and one long and thin far away, have the same area.">
  <g font-size="8" fill="currentColor">
    <ellipse cx="170" cy="112" rx="120" ry="96.0" fill="none" stroke="#c1440e" stroke-width="0.9"/>
    <path d="M242.0,112 L290.0,112.0 L289.4,102.6 L287.7,93.4 L285.0,84.7 L281.5,76.5 L277.2,68.9 L272.4,62.0 L267.2,55.7 L261.7,50.1 L256.0,45.0 L250.2,40.6 Z" fill="#eea66f" fill-opacity="0.55" stroke="#eea66f" stroke-width="0.6"/>
    <path d="M242.0,112 L50.0,112.0 L50.0,114.4 L50.1,116.7 L50.3,119.1 L50.6,121.4 L50.9,123.8 L51.3,126.1 L51.8,128.4 L52.3,130.8 L52.9,133.1 L53.6,135.4 Z" fill="#5aa0d8" fill-opacity="0.55" stroke="#5aa0d8" stroke-width="0.6"/>
    <circle cx="290.0" cy="112.0" r="2.2" fill="#c1440e"/>
    <circle cx="250.2" cy="40.6" r="2.2" fill="#c1440e"/>
    <circle cx="193.5" cy="17.9" r="2.2" fill="#c1440e"/>
    <circle cx="146.7" cy="17.8" r="2.2" fill="#c1440e"/>
    <circle cx="110.3" cy="28.7" r="2.2" fill="#c1440e"/>
    <circle cx="83.3" cy="45.6" r="2.2" fill="#c1440e"/>
    <circle cx="64.6" cy="66.1" r="2.2" fill="#c1440e"/>
    <circle cx="53.6" cy="88.6" r="2.2" fill="#c1440e"/>
    <circle cx="50.0" cy="112.0" r="2.2" fill="#c1440e"/>
    <circle cx="53.6" cy="135.4" r="2.2" fill="#c1440e"/>
    <circle cx="64.6" cy="157.9" r="2.2" fill="#c1440e"/>
    <circle cx="83.3" cy="178.4" r="2.2" fill="#c1440e"/>
    <circle cx="110.3" cy="195.3" r="2.2" fill="#c1440e"/>
    <circle cx="146.7" cy="206.2" r="2.2" fill="#c1440e"/>
    <circle cx="193.5" cy="206.1" r="2.2" fill="#c1440e"/>
    <circle cx="250.2" cy="183.4" r="2.2" fill="#c1440e"/>
    <circle cx="242.0" cy="112" r="5" fill="#eea66f"/>
    <text x="242.0" y="127" text-anchor="middle">Sun</text>
    <circle cx="170" cy="112" r="1.3" fill="currentColor"/>
    <text x="170" y="107" text-anchor="middle">centre</text>
    <circle cx="98.0" cy="112" r="1.3" fill="currentColor"/>
    <text x="98.0" y="107" text-anchor="middle">other focus</text>
    <text x="294" y="108">perihelion</text>
    <text x="46" y="108" text-anchor="end">aphelion</text>
    <text x="6" y="12">Equal times, equal areas</text>
    <text x="6" y="226">Dots: the planet's place at 16 equal steps of time. The two shaded wedges each</text>
    <text x="6" y="235">take one step and have the same area. Eccentricity 0.6, far more stretched</text>
    <text x="6" y="244">than any planet; Mars's orbit is 0.093 and would look like a circle.</text>
  </g>
</svg>
</div>

*Figure A. The first two laws on an orbit stretched far more than any planet's.*

The near end of an orbit round the Sun is its **perihelion** and the far end its **aphelion**. The size $a$ in the
third law is the **semi-major axis**, half the longest width of the ellipse, which is also the planet's average of its
nearest and farthest distances. Chapter 4 looks at ellipses in detail, and the physics lesson
[Ellipses](https://physics.akadian.ca/topics/gravity/level-7/03-ellipses.html) works through the first two laws with
Mars's numbers.

??? note "Sources"
    - The three laws, the wording of the second ("a line segment joining a planet and the Sun sweeps out equal areas
      during equal intervals of time"), the Sun at one focus, and publication from 1609 to 1621 in *Astronomia nova*,
      *Harmonices Mundi* and *Epitome Astronomiae Copernicanae*: Wikipedia,
      [Kepler's laws of planetary motion](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion) (weaker).
    - The story: the history book, chapter 14, sections 14.7 and 14.8.
    - Figure A: positions at 16 equal steps of time, worked out by us from Kepler's equation (chapter 4) for an
      eccentricity of 0.6.

## 3.2 Nearly round, and very long { #first }

The planets' ellipses are so nearly round that you could not tell them from circles in a drawing. Mars's is only
0.44% narrower than a circle; what gives it away is that the Sun is 21 million km off its centre (history book,
[section 14.10](../history/14-Tycho-and-Kepler.md#working)).

Comets are another matter. **Halley's comet** travels on an ellipse with an eccentricity of 0.967, close to the 1 of a
parabola. At perihelion it is 0.59 AU from the Sun, 88 million km, between the orbits of Mercury and Venus. At
aphelion it is 35 AU away, 5.2 billion km, roughly as far as Pluto. It goes round once every 74.7 years on average,
though the pulls of the planets make each trip a little different, anywhere from 74 to 79 years.

Edmond Halley worked out that the comets of 1531, 1607 and 1682 were one object on one orbit, and predicted that it
would return in 1758. He died in 1742; the comet came back on time (history book,
[chapter 16, section 16.5](../history/16-Newton-Halley-and-Romer.md#halley)). It last came in 1986 and will be back in
mid-2061.

??? note "Sources"
    - Mars's ellipse: the history book, chapter 14, section 14.10, and its sources.
    - Halley's comet: eccentricity 0.967 (0.96658), perihelion 0.59 AU (88 million km) between the orbits of Mercury
      and Venus, aphelion 35 AU (5.2 billion km), roughly Pluto's distance, semi-major axis 17.737 AU, period
      74.7 years, returns every 74 to 79 years, Halley's prediction of a return in 1758 and his death in 1742, the
      returns of 1986 and mid-2061: Wikipedia, [Halley's Comet](https://en.wikipedia.org/wiki/Halley%27s_Comet)
      (weaker).
    - The comets of 1531, 1607 and 1682: the history book, chapter 16, section 16.5, and its sources.

## 3.3 Fast near, slow far { #second }

The second law says a planet speeds up as it falls towards the Sun and slows down as it climbs away.

- **The Earth** is closest to the Sun in early January and moves fastest then, 30.29 km/s, against 29.29 km/s in early
  July. That is why northern winter is the shortest season (book 1,
  [section 8.9](../night-sky/08-The-Suns-Path-and-the-Seasons.md#kepler)).
- **Mars** changes more: 26.50 km/s at perihelion, 21.97 km/s at aphelion.
- **Halley's comet** changes enormously. At perihelion and aphelion it is moving straight across the line to the Sun,
  and there the equal-areas rule makes speed times distance the same at both ends. Its farthest distance is 59 times
  its nearest, so it moves 59 times faster at perihelion than at aphelion.

The rule also says where the time goes. Halley's comet spends only about **2.2 years** of each 75-year trip inside
the orbit of Jupiter, and only about **78 days** inside the Earth's orbit, where it is easy to see. The rest of the
time it creeps along the far end of its orbit (section 3.9).

??? note "Sources"
    - The Earth's maximum and minimum orbital speeds (30.29 and 29.29 km/s) and Mars's (26.50 and 21.97 km/s): NASA,
      [Earth fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html) and
      [Mars fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - The Earth closest in early January and the short northern winter: book 1, chapter 8, section 8.9.
    - Halley's perihelion of 0.59278 AU and aphelion of 35.14 AU: Wikipedia, Halley's Comet (above). The speed ratio
      and the times inside Jupiter's and the Earth's orbits are our arithmetic, section 3.9.

## 3.4 Squares and cubes { #third }

Kepler found his third law in 1618. Here it is for every planet, with two more bodies he never knew: the dwarf planet
Ceres, found in 1801, and Halley's comet.

| Body | Size of orbit $a$ (AU) | $a^3$ | $\sqrt{a^3}$ (years) | Measured year |
| --- | --- | --- | --- | --- |
| Mercury | 0.387 | 0.058 | 0.241 | 0.241 |
| Venus | 0.723 | 0.378 | 0.615 | 0.615 |
| Earth | 1.000 | 1.000 | 1.000 | 1.000 |
| Mars | 1.524 | 3.538 | 1.881 | 1.881 |
| Ceres | 2.766 | 21.16 | 4.600 | 4.600 |
| Jupiter | 5.203 | 140.8 | 11.87 | 11.86 |
| Saturn | 9.537 | 867.3 | 29.45 | 29.45 |
| Halley's comet | 17.74 | 5,580 | 74.70 | 74.7 |
| Uranus | 19.19 | 7,066 | 84.06 | 84.01 |
| Neptune | 30.07 | 27,189 | 164.9 | 164.8 |

Everything agrees to better than 0.1%, from Mercury, which goes round in 88 days, to Neptune, which takes 165 years.
Uranus was found in 1781 and Neptune in 1846, long after Kepler died, and they obey his rule just the same. The
physics lesson [Kepler's third law](https://physics.akadian.ca/topics/gravity/level-6/04-keplers-third-law.html) shows
where the squares and cubes come from.

??? note "Sources"
    - Semi-major axes: NASA JPL,
      [approximate orbital elements](https://ssd.jpl.nasa.gov/planets/approx_pos.html), table 1 (for 2000). NASA's fact
      sheets give a slightly larger long-term value for Saturn, 9.57 AU, used in chapter 2.
    - Orbital periods (87.969, 224.701, 365.256, 686.980, 4,332.589, 10,755.699, 30,685.4 and 60,189.018 days): NASA
      fact sheets for [Mercury](https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html),
      [Venus](https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html), the Earth, Mars,
      [Jupiter](https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html),
      [Saturn](https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturnfact.html),
      [Uranus](https://nssdc.gsfc.nasa.gov/planetary/factsheet/uranusfact.html) and
      [Neptune](https://nssdc.gsfc.nasa.gov/planetary/factsheet/neptunefact.html).
    - Ceres: semi-major axis 2.766 AU, period 4.600 years, discovered on 1 January 1801 by Giuseppe Piazzi: Wikipedia,
      [Ceres](https://en.wikipedia.org/wiki/Ceres_(dwarf_planet)) (weaker). Halley's comet: as in section 3.2.
    - Kepler finding the third law in 1618: the history book, chapter 14, section 14.8. The discovery dates of Uranus
      (1781) and Neptune (1846) are standard; chapter 10 tells Neptune's story.

## 3.5 The same law for moons { #moons }

In 1610 telescopes revealed four moons going round Jupiter. Kepler noticed, in 1621, that his third law worked for
them too, using the observations Simon Marius had published in 1614. It was a big step: the rules that move the
planets round the Sun also move moons round a planet.

But the number in the law is different. For the planets, $a^3 / P^2$ is the same for all of them; for Jupiter's moons
it is the same for all four, but a different value. Every family of orbits has its own constant.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Kepler's third law on a log-log chart: the distance of each orbit across the bottom, from a thousand kilometres to ten billion, and the time for one orbit up the side, from a hundredth of a day to a hundred thousand days. Four groups of dots each fall on a straight line, and the four lines are parallel. The planets, Ceres and Halley's comet round the Sun lie on the lowest line. The four big moons of Jupiter lie on the next. The space station, GPS satellites, geostationary satellites and the Moon round the Earth lie on the next, and Phobos, the areostationary orbit and Deimos round Mars on the top line. The slope is the same for all: the period squared goes with the distance cubed. Only the constant differs, because each central body has a different mass.">
  <g font-size="8" fill="currentColor">
    <rect x="46" y="22" width="272" height="182" fill="none" stroke="#555" stroke-width="0.6"/>
    <line x1="46.0" y1="204" x2="46.0" y2="207" stroke="#555" stroke-width="0.6"/>
    <text x="46.0" y="215" text-anchor="middle">10<tspan dy="-3" font-size="6">3</tspan></text>
    <line x1="84.9" y1="204" x2="84.9" y2="207" stroke="#555" stroke-width="0.6"/>
    <text x="84.9" y="215" text-anchor="middle">10<tspan dy="-3" font-size="6">4</tspan></text>
    <line x1="123.7" y1="204" x2="123.7" y2="207" stroke="#555" stroke-width="0.6"/>
    <text x="123.7" y="215" text-anchor="middle">10<tspan dy="-3" font-size="6">5</tspan></text>
    <line x1="162.6" y1="204" x2="162.6" y2="207" stroke="#555" stroke-width="0.6"/>
    <text x="162.6" y="215" text-anchor="middle">10<tspan dy="-3" font-size="6">6</tspan></text>
    <line x1="201.4" y1="204" x2="201.4" y2="207" stroke="#555" stroke-width="0.6"/>
    <text x="201.4" y="215" text-anchor="middle">10<tspan dy="-3" font-size="6">7</tspan></text>
    <line x1="240.3" y1="204" x2="240.3" y2="207" stroke="#555" stroke-width="0.6"/>
    <text x="240.3" y="215" text-anchor="middle">10<tspan dy="-3" font-size="6">8</tspan></text>
    <line x1="279.1" y1="204" x2="279.1" y2="207" stroke="#555" stroke-width="0.6"/>
    <text x="279.1" y="215" text-anchor="middle">10<tspan dy="-3" font-size="6">9</tspan></text>
    <line x1="318.0" y1="204" x2="318.0" y2="207" stroke="#555" stroke-width="0.6"/>
    <text x="318.0" y="215" text-anchor="middle">10<tspan dy="-3" font-size="6">10</tspan></text>
    <line x1="43" y1="204.0" x2="46" y2="204.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="207.0" text-anchor="end">10<tspan dy="-3" font-size="6">-2</tspan></text>
    <line x1="43" y1="178.0" x2="46" y2="178.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="181.0" text-anchor="end">10<tspan dy="-3" font-size="6">-1</tspan></text>
    <line x1="43" y1="152.0" x2="46" y2="152.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="155.0" text-anchor="end">10<tspan dy="-3" font-size="6">0</tspan></text>
    <line x1="43" y1="126.0" x2="46" y2="126.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="129.0" text-anchor="end">10<tspan dy="-3" font-size="6">1</tspan></text>
    <line x1="43" y1="100.0" x2="46" y2="100.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="103.0" text-anchor="end">10<tspan dy="-3" font-size="6">2</tspan></text>
    <line x1="43" y1="74.0" x2="46" y2="74.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="77.0" text-anchor="end">10<tspan dy="-3" font-size="6">3</tspan></text>
    <line x1="43" y1="48.0" x2="46" y2="48.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="51.0" text-anchor="end">10<tspan dy="-3" font-size="6">4</tspan></text>
    <line x1="43" y1="22.0" x2="46" y2="22.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="25.0" text-anchor="end">10<tspan dy="-3" font-size="6">5</tspan></text>
    <text x="182.0" y="225" text-anchor="middle">size of orbit (semi-major axis, km)</text>
    <text x="10" y="113.0" text-anchor="middle" transform="rotate(-90 10 113.0)">time for one orbit (days)</text>
    <line x1="215.6" y1="117.0" x2="310.2" y2="22.0" stroke="#eea66f" stroke-width="0.8"/>
    <circle cx="231.1" cy="101.4" r="2.2" fill="#eea66f" stroke="#555" stroke-width="0.3"/>
    <circle cx="241.6" cy="90.9" r="2.2" fill="#eea66f" stroke="#555" stroke-width="0.3"/>
    <circle cx="247.1" cy="85.4" r="2.2" fill="#eea66f" stroke="#555" stroke-width="0.3"/>
    <circle cx="254.2" cy="78.2" r="2.2" fill="#eea66f" stroke="#555" stroke-width="0.3"/>
    <circle cx="264.3" cy="68.1" r="2.2" fill="#eea66f" stroke="#555" stroke-width="0.3"/>
    <circle cx="274.9" cy="57.4" r="2.2" fill="#eea66f" stroke="#555" stroke-width="0.3"/>
    <circle cx="285.2" cy="47.2" r="2.2" fill="#eea66f" stroke="#555" stroke-width="0.3"/>
    <circle cx="296.9" cy="35.3" r="2.2" fill="#eea66f" stroke="#555" stroke-width="0.3"/>
    <circle cx="295.6" cy="36.7" r="2.2" fill="#eea66f" stroke="#555" stroke-width="0.3"/>
    <circle cx="304.6" cy="27.7" r="2.2" fill="#eea66f" stroke="#555" stroke-width="0.3"/>
    <text x="256.3" y="71.1" text-anchor="end">round the Sun</text>
    <line x1="132.5" y1="161.1" x2="188.7" y2="104.7" stroke="#cfc8bf" stroke-width="0.8"/>
    <circle cx="148.0" cy="145.6" r="2.2" fill="#cfc8bf" stroke="#555" stroke-width="0.3"/>
    <circle cx="155.8" cy="137.7" r="2.2" fill="#cfc8bf" stroke="#555" stroke-width="0.3"/>
    <circle cx="163.7" cy="129.8" r="2.2" fill="#cfc8bf" stroke="#555" stroke-width="0.3"/>
    <circle cx="173.2" cy="120.2" r="2.2" fill="#cfc8bf" stroke="#555" stroke-width="0.3"/>
    <text x="180.2" y="123.2" text-anchor="start">round Jupiter</text>
    <line x1="62.8" y1="198.5" x2="161.9" y2="99.1" stroke="#5aa0d8" stroke-width="0.8"/>
    <circle cx="78.3" cy="183.0" r="2.2" fill="#5aa0d8" stroke="#555" stroke-width="0.3"/>
    <circle cx="101.4" cy="159.9" r="2.2" fill="#5aa0d8" stroke="#555" stroke-width="0.3"/>
    <circle cx="109.1" cy="152.0" r="2.2" fill="#5aa0d8" stroke="#555" stroke-width="0.3"/>
    <circle cx="146.4" cy="114.7" r="2.2" fill="#5aa0d8" stroke="#555" stroke-width="0.3"/>
    <text x="138.4" y="117.7" text-anchor="end">round the Earth</text>
    <line x1="68.3" y1="180.4" x2="114.7" y2="133.9" stroke="#c1440e" stroke-width="0.8"/>
    <circle cx="83.8" cy="164.9" r="2.2" fill="#c1440e" stroke="#555" stroke-width="0.3"/>
    <circle cx="96.9" cy="151.7" r="2.2" fill="#c1440e" stroke="#555" stroke-width="0.3"/>
    <circle cx="99.2" cy="149.4" r="2.2" fill="#c1440e" stroke="#555" stroke-width="0.3"/>
    <text x="91.2" y="140.4" text-anchor="end">round Mars</text>
    <text x="6" y="12">Squares and cubes</text>
    <text x="6" y="244">Four families of orbits, four parallel lines: the same law with different constants.</text>
  </g>
</svg>
</div>

*Figure B. Orbits round four different bodies. On these scales, squares and cubes give straight lines of the same
slope; each body gets its own line.*

Each line in Figure B is a family: the planets round the Sun; Io, Europa, Ganymede and Callisto round Jupiter; the
space station, GPS satellites, geostationary satellites and the Moon round the Earth; and Phobos, Deimos and the
areostationary orbit round Mars. The lines are parallel because the law is the same. They are shifted because the
constant depends on how massive the central body is. Newton explained why (chapter 5), and chapter 6 uses the shift
to weigh the Sun and the planets.

??? note "Sources"
    - Kepler noting in 1621 that his third law applies to the four brightest moons of Jupiter: Wikipedia, Kepler's
      laws of planetary motion (above). His use of Simon Marius's 1614 *Mundus Iovialis*, and the idea that the same
      laws govern moons round planets: Wikipedia,
      [Epitome Astronomiae Copernicanae](https://en.wikipedia.org/wiki/Epitome_Astronomiae_Copernicanae) (weaker).
    - The moons found in 1610, and their distances and periods (Io 421,800 km and 1.769 days, Europa 671,100 km and
      3.551, Ganymede 1,070,400 km and 7.155, Callisto 1,882,700 km and 16.689): Wikipedia,
      [Galilean moons](https://en.wikipedia.org/wiki/Galilean_moons) (weaker).
    - The Moon (384,400 km, 27.322 days), Phobos (9,375 km, 0.3187 days) and Deimos (23,457 km, 1.2625 days): NASA
      JPL, [planetary satellite mean elements](https://ssd.jpl.nasa.gov/sats/elem/).
    - The space station: book 1, chapter 16, section 16.3. GPS, geostationary and areostationary orbits: as in
      sections 3.6 and 3.8.

## 3.6 From the Moon to a fixed satellite { #geo }

A satellite that goes round once in exactly the time the Earth takes to turn, one sidereal day of 23 hours 56 minutes,
stays over the same spot on the equator. Where must it be?

The Moon answers it. The Moon goes round in 27.322 days at 384,400 km. By the third law, a satellite with a period
$27.322 / 0.99727 = 27.40$ times shorter must have an orbit $27.40^{2/3} = 9.09$ times smaller:

$$384{,}400 \text{ km} / 9.09 = 42{,}300 \text{ km}.$$

The real geostationary orbit is 42,164 km from the Earth's centre, 35,786 km above the equator. The idea was made famous
by the writer Arthur C. Clarke in the 1940s, and the first satellite reached such an orbit in 1963 (book 1,
[section 16.6](../night-sky/16-Satellites-and-the-Space-Station.md#heights)). The small difference from 42,300 km
is real, and section 3.9 explains it.

The same trick gives the **GPS** satellites, which go round twice a day, in 11 hours 58 minutes. Their orbits come out
at about 26,600 km from the Earth's centre, about 20,200 km up, just where they are.

??? note "Sources"
    - The geostationary orbit, 42,164 km from the Earth's centre and 35,786 km above the equator, with a period of one
      sidereal day, Clarke in the 1940s, and the first satellite in such an orbit in 1963: Wikipedia,
      [Geostationary orbit](https://en.wikipedia.org/wiki/Geostationary_orbit) (weaker).
    - GPS satellites at about 20,200 km up, orbital radius about 26,600 km, with a period of half a sidereal day,
      11 hours 58 minutes: Wikipedia,
      [Global Positioning System](https://en.wikipedia.org/wiki/Global_Positioning_System) (weaker).
    - The Moon: NASA JPL, satellite mean elements (above). The sidereal day of 23.9345 hours (0.99727 days): NASA,
      Earth fact sheet (above). The arithmetic is ours.

## 3.7 Half an ellipse to Mars { #transfer }

The cheapest common way to fly from the Earth to Mars is on an ellipse that just touches both orbits: perihelion at
the Earth's orbit, aphelion at Mars's. A spacecraft launched onto it coasts halfway round and meets Mars at the far
end. It is called a **Hohmann transfer**, after the German engineer Walter Hohmann, who described it in 1925.

The third law gives the travel time without any physics beyond this chapter. The ellipse stretches from 1 AU to
1.524 AU, so its semi-major axis is $(1 + 1.524) / 2 = 1.262$ AU. A full trip round it would take
$\sqrt{1.262^3} = 1.418$ years, and the spacecraft does half of it: **0.709 years, or about 259 days.**

The second law adds the speeds. The spacecraft leaves at its perihelion, moving fast, and arrives at its aphelion
moving 1.524 times more slowly, because the far end is 1.524 times farther from the Sun. Chapter 15 works out what
that means for launching and arriving, and the physics lesson
[Hohmann transfer](https://physics.akadian.ca/topics/gravity/level-7/05-hohmann-transfer.html) does the speeds.

??? note "Sources"
    - The Hohmann transfer, named after Walter Hohmann, who described it in his 1925 book *Die Erreichbarkeit der
      Himmelskörper*: Wikipedia, [Hohmann transfer orbit](https://en.wikipedia.org/wiki/Hohmann_transfer_orbit)
      (weaker).
    - Mars's semi-major axis of 1.524 AU: NASA JPL, approximate orbital elements (above). The travel time and speed
      ratio are our arithmetic, for circular orbits; the physics lesson
      [Kepler's third law](https://physics.akadian.ca/topics/gravity/level-6/04-keplers-third-law.html) gets the same
      259 days.

## 3.8 Kepler's laws at Mars { #mars }

Mars has its own families of orbits, and Kepler's laws run them all.

**Phobos and Deimos.** Deimos is 2.50 times farther from Mars than Phobos, so by the third law its month should be
$2.50^{1.5} = 3.96$ times longer. Phobos goes round in 7 hours 39 minutes and Deimos in 30 hours 18 minutes: the ratio
is 3.96.

**A Mars-stationary orbit.** A satellite that keeps pace with Mars's turning, once every 24 hours 37 minutes, would
hang over one spot on Mars's equator. Phobos and Deimos each give its height by the trick of section 3.6: about
20,430 km from Mars's centre, 17,032 km above the ground. Deimos orbits just outside it (book 1,
[section 16.8](../night-sky/16-Satellites-and-the-Space-Station.md#mars)). No spacecraft has been put there yet; it is
hard to reach and to stay in.

**Equal areas for an orbiter.** NASA's MAVEN reached Mars on 22 September 2014 and went into an ellipse from about 150
km to 6,200 km above the ground, to sample the upper air at its low point. The third law gives its period, about **4.5
hours**. The second law decides how the time is shared out. MAVEN skims past its low point at about 4.2 km/s and
crawls through its high point at about 1.6 km/s. It covers the low half of each circuit, from one side of Mars round
past the low point to the other side, in under **an hour**, and spends the other three and a half hours on the high
side.

**Mars's own orbit.** Mars obeys the laws round the Sun as well: its unequal seasons are the second law at work
(history book, [section 14.9](../history/14-Tycho-and-Kepler.md#onmars)).

??? note "Sources"
    - Phobos and Deimos: distances and periods from NASA JPL, satellite mean elements (above). Mars's sidereal day of
      24.6229 hours: NASA, Mars fact sheet (above).
    - The areostationary orbit, about 17,032 km above Mars's equator and 20,428 km from its centre: Wikipedia,
      [Areostationary orbit](https://en.wikipedia.org/wiki/Areostationary_orbit) (weaker), which also says no
      artificial satellite has been placed in it because it is technically hard to reach and keep. Deimos just outside
      it: book 1, chapter 16, section 16.8.
    - MAVEN's arrival on 22 September 2014 and its elliptic orbit of about 6,200 km by 150 km above the surface:
      Wikipedia, [MAVEN](https://en.wikipedia.org/wiki/MAVEN) (weaker), which calls it the first NASA mission to study
      the Mars atmosphere.
    - MAVEN's period, speeds and the time on the low half are our arithmetic, section 3.9, using Mars's $GM$ of
      42,828 km³/s² and radius of 3,389.5 km from the NASA Mars fact sheet.
    - Mars's seasons: the history book, chapter 14, section 14.9.

## 3.9 Working it out { #working }

**Halley's speeds.** At perihelion and aphelion the comet moves at right angles to the line to the Sun, so the area
swept in a short time $t$ is a thin triangle of area $\tfrac12 r v t$. Equal areas means $r_p v_p = r_a v_a$, so

$$\frac{v_p}{v_a} = \frac{r_a}{r_p} = \frac{35.14}{0.593} = 59.3.$$

The same rule checks Mars: $206.650 \times 26.50 = 5{,}476$ and $249.261 \times 21.97 = 5{,}476$ (million km times
km/s).

**Halley's time near the Sun.** For a body on an ellipse with semi-major axis $a$ and eccentricity $e$, use an angle
$E$ (the **eccentric anomaly**, chapter 4) with distance $r = a(1 - e\cos E)$; the time since perihelion, as a fraction
of the period, is $(E - e\sin E) / 2\pi$. For Halley's comet, $a = 17.737$ AU and $e = 0.96658$. Inside Jupiter's
orbit, $r < 5.2$ AU:

$$\cos E = \frac{1 - 5.2/17.737}{0.96658} = 0.7313, \quad E = 0.7513, \quad E - e\sin E = 0.0920.$$

That is the time from perihelion out to 5.2 AU; the trip in takes the same, so the fraction of the orbit spent inside
is $2 \times 0.0920 / 2\pi = 0.0293$, which is $0.0293 \times 74.7 = 2.2$ years. The same steps for 1 AU give 78 days.

**The geostationary orbit from the Moon.** $a = 384{,}400 \times (0.99727 / 27.322)^{2/3} = 42{,}300$ km, 0.3% more
than the true 42,164 km. The reason is that the Moon is not tiny: it has 1.2% of the Earth's mass, and the third law's
constant depends on the masses of both bodies together (chapter 6). Allowing for it gives 42,126 km, within 0.1%.

**MAVEN.** Its low and high points are $r_p = 3{,}389.5 + 150 = 3{,}539.5$ km and $r_a = 3{,}389.5 + 6{,}200 =
9{,}589.5$ km from Mars's centre, so $a = 6{,}564.5$ km and $e = (r_a - r_p) / (r_a + r_p) = 0.461$. Its period is

$$P = 2\pi\sqrt{\frac{a^3}{GM}} = 2\pi\sqrt{\frac{6{,}564.5^3}{42{,}828}} = 16{,}150 \text{ s} = 4.49 \text{ hours}.$$

The speed at the low point is 4.20 km/s (from the energy rule of chapter 7), and at the high point
$4.20 / 2.709 = 1.55$ km/s. The low half runs from the point level with Mars's centre on one side, at right angles to
the long axis, round through the low point to the same point on the other side. At its ends $\cos E = e$, so
$E = 1.092$ and $E - e\sin E = 0.683$: a fraction $0.683 / \pi = 0.217$ of the orbit, 59 minutes.

| | Mars | Earth |
| --- | --- | --- |
| Third-law constant $a^3/P^2$ for its moons and satellites | $8.1 \times 10^{12}$ km³/day² | $7.5 \times 10^{13}$ km³/day² |
| Orbit that keeps pace with the turning planet | 20,428 km from the centre | 42,164 km from the centre |
| Height of that orbit above the equator | 17,032 km | 35,786 km |
| Period of an orbit 200 km up | 109 minutes | 88 minutes |
| Fastest ÷ slowest speed round the Sun | 26.50 ÷ 21.97 = 1.21 | 30.29 ÷ 29.29 = 1.03 |

The Earth's constant is about nine times Mars's: that factor is the ratio of their masses, as chapter 6 shows.

??? note "Sources"
    - Halley's orbit: Wikipedia, Halley's Comet (above). Mars's perihelion and aphelion distances (206.650 and 249.261
      million km) and speeds: NASA, Mars fact sheet (above).
    - The relations $r = a(1 - e\cos E)$ and $M = E - e\sin E$ are Kepler's; chapter 4 derives them.
    - The Moon's mass, 1.23% of the Earth's: NASA,
      [Moon fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html) (0.0123 of the Earth's).
    - Mars's $GM$ (42,828 km³/s²) and radius: NASA, Mars fact sheet. The Earth's $GM$ (398,600 km³/s²): NASA, Earth
      fact sheet. The constants are from the moons and satellites in Figure B. The rest is our arithmetic.

## 3.10 Newton's proof of equal areas { #newton }

Kepler found the second law by measurement. Newton proved it, near the start of the *Principia*, with nothing but
triangles, and the proof shows something Kepler could not: the law has nothing to do with how strong the pull is. Any
pull aimed at a fixed centre gives equal areas.

Let time pass in equal ticks. In the first tick the body moves from A to B. If nothing pulled on it, in the next tick
it would go straight on the same distance, to c. Instead, at B, it gets a sudden kick straight towards the centre S,
and ends up at C.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Newton's proof of equal areas. A body moves from A to B in one tick of time. With no force it would go on the same distance again to a point c. Instead, at B it gets a kick straight towards the Sun, S, and ends up at C. The triangles S A B and S B c have equal bases and the same height, so they have equal areas. The triangles S B c and S B C share the base S B, and c and C lie on a line parallel to S B, so they also have equal areas. So the area swept from A to B equals the area swept from B to C. Making the ticks shorter and shorter turns the kicks into a smooth pull and the path into a curve, and the areas stay equal.">
  <g font-size="8" fill="currentColor">
    <path d="M70,196 L96,70 L200,52 Z" fill="#eea66f" fill-opacity="0.45" stroke="#eea66f" stroke-width="0.7"/>
    <path d="M70,196 L200,52 L261.1,81.5 Z" fill="#5aa0d8" fill-opacity="0.45" stroke="#5aa0d8" stroke-width="0.7"/>
    <path d="M70,196 L304,34" fill="none" stroke="#555" stroke-width="0.6" stroke-dasharray="3 2"/>
    <line x1="200" y1="52" x2="304" y2="34" stroke="#555" stroke-width="0.8" stroke-dasharray="3 2"/>
    <line x1="304" y1="34" x2="261.1" y2="81.5" stroke="#555" stroke-width="0.6" stroke-dasharray="1 2"/>
    <polyline points="96,70 200,52 261.1,81.5" fill="none" stroke="#c1440e" stroke-width="1.3"/>
    <circle cx="96.0" cy="70.0" r="2.5" fill="#c1440e"/>
    <text x="88.0" y="70.0" text-anchor="middle" font-size="9">A</text>
    <circle cx="200.0" cy="52.0" r="2.5" fill="#c1440e"/>
    <text x="200.0" y="46.0" text-anchor="middle" font-size="9">B</text>
    <circle cx="304.0" cy="34.0" r="2.5" fill="#c1440e"/>
    <text x="310.0" y="34.0" text-anchor="middle" font-size="9">c</text>
    <circle cx="261.1" cy="81.5" r="2.5" fill="#c1440e"/>
    <text x="268.1" y="85.5" text-anchor="middle" font-size="9">C</text>
    <circle cx="70" cy="196" r="6" fill="#eea66f"/>
    <text x="60" y="199" text-anchor="end" font-size="9">S</text>
    <text x="288.6" y="57.8">kick towards S</text>
    <text x="252.0" y="37.0" text-anchor="middle">straight on</text>
    <text x="6" y="12">Newton's proof of equal areas</text>
    <text x="6" y="226">Orange (SAB) = SBc: equal bases AB and Bc, same height. SBc = blue (SBC): same</text>
    <text x="6" y="235">base SB, and cC is parallel to SB. So each tick sweeps the same area. Shrink the</text>
    <text x="6" y="244">ticks and the kicks become a smooth pull towards S; the areas stay equal.</text>
  </g>
</svg>
</div>

*Figure C. Newton's construction.*

- Triangles SAB and SBc have equal bases, AB and Bc, along the same line, and the same apex S, so they have the same
  height and the same area.
- The kick is aimed at S, so it moves the body from c to C along a line parallel to SB. Triangles SBc and SBC share
  the base SB, and c and C are the same distance from it, so they have the same area too.

So SAB and SBC have equal areas: each tick sweeps the same area, kick or no kick. Now make the ticks shorter and
shorter, with smaller and smaller kicks. The broken path becomes a smooth curve, the kicks become a steady pull towards
S, and the areas stay equal at every step.

In modern words, the quantity kept fixed is $r v_\perp$, the distance times the speed across the line to the centre.
Physicists call it the **angular momentum** per unit mass. A pull towards the centre cannot change it, because it has
no sideways part. The first and third laws are different: they need the pull to weaken as the square of the distance,
and that is where chapter 5 begins.

??? note "Sources"
    - Newton's construction for equal areas under a central force is proposition 1 of book 1 of the *Principia*
      (1687); standard. The *Principia*: the history book, chapter 16, section 16.2.
    - That the first and third laws follow from an inverse-square force is standard; chapter 5.
    - Figure C: our drawing of the construction.

## Check yourself { #check }

**1.** (beginner) State Kepler's three laws in your own words.

??? note "Answer"
    Planets move on ellipses with the Sun at one focus. The line from the Sun to a planet sweeps out equal areas in
    equal times, so the planet is fastest when nearest the Sun. The square of the year is proportional to the cube of
    the size of the orbit.

**2.** (beginner) Where on its orbit does a planet move fastest, and why?

??? note "Answer"
    At perihelion, nearest the Sun. The line to the Sun is shortest there, so to sweep out the same area in the same
    time the planet has to cover more distance.

**3.** (beginner) Why is Halley's comet visible for only a short time every 75 years?

??? note "Answer"
    Its orbit is a long, thin ellipse. It comes close to the Sun, where it is bright and near the Earth, only briefly,
    moving fast; it spends most of its time crawling round the far end of its orbit, beyond Neptune's distance.

**4.** (intermediate) Ceres goes round the Sun at 2.766 AU. Use the third law to find its year.

??? note "Answer"
    $P = \sqrt{2.766^3} = \sqrt{21.16} = 4.60$ years.

**5.** (intermediate) Why can't you use $P^2 = a^3$, with years and AU, for the moons of Jupiter?

??? note "Answer"
    The constant in the law depends on the central body. With years and AU, the constant 1 is the Sun's. Jupiter's
    moons follow the same squares-and-cubes rule, but with Jupiter's own constant, about a thousand times smaller.

**6.** (intermediate) A spacecraft flies a Hohmann transfer from the Earth to Jupiter, at 5.2 AU. How long does the
trip take?

??? note "Answer"
    $a = (1 + 5.2) / 2 = 3.1$ AU. A full orbit takes $\sqrt{3.1^3} = 5.46$ years, so half takes 2.73 years, about 2
    years and 9 months.

**7.** (advanced) Use the Moon (384,400 km, 27.32 days) to find the radius of an orbit round the Earth with a period
of exactly one day of 24 hours. Is it inside or outside the geostationary orbit?

??? note "Answer"
    $a = 384{,}400 \times (1 / 27.32)^{2/3}$. Since $27.32^{2/3} = 9.07$, $a = 384{,}400 / 9.07 = 42{,}380$ km. That
    is slightly outside the geostationary orbit (42,300 km by the same method), because 24 hours is about 4 minutes
    longer than the sidereal day in which the Earth turns once. A satellite there would drift slowly westward.

**8.** (expert) In Figure C, the kick at B changes the body's speed. Show that $r v_\perp$, the distance from S times
the speed across the line to S, is the same before and after the kick.

??? note "Answer"
    The area swept in one tick is $\tfrac12 \times SB \times$ (the sideways distance moved across the line SB), which is
    $\tfrac12 r v_\perp t$. The kick is along SB, so it adds nothing across SB: the sideways part of the velocity is
    unchanged, and so is $r v_\perp$. That is the same statement as equal areas.

## Summary

- Planets move on ellipses with the Sun at one focus; the line to the Sun sweeps equal areas in equal times; the
  square of the year goes with the cube of the size of the orbit.
- The planets' ellipses are nearly circles; comets' are long and thin. Halley's comet goes from 0.59 to 35 AU.
- Near the Sun a body moves fast, far away slowly: speed times distance is the same at both ends of the orbit.
- Halley's comet spends only about 78 days of each 75-year trip inside the Earth's orbit.
- $P^2 = a^3$ fits every planet, Ceres and Halley's comet to better than 0.1%.
- Moons and satellites follow the same law, with a different constant for each central body.
- The Moon alone gives the height of geostationary orbit, and the GPS satellites' too.
- The half-ellipse from the Earth to Mars takes about 259 days.
- At Mars the laws give the Mars-stationary height, 17,032 km, and share out MAVEN's 4.5-hour orbit: under an hour low,
  three and a half hours high.
- Any pull aimed at a fixed centre gives equal areas; the ellipse and the squares and cubes need the inverse square.

**Next:** chapter 4, Ellipses: the shape of an orbit, where we draw ellipses with string and pins, measure how
stretched they are, and work out where a planet is on any date.

## Further reading

- James R. Voelkel, *Johannes Kepler and the New Astronomy*, Oxford University Press, 1999.
