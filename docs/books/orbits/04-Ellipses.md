# 4. Ellipses: the shape of an orbit

*Kepler said orbits are ellipses. This chapter looks at that shape closely: how to draw one with two pins and a loop
of string, how to measure how stretched it is, and how the ellipse belongs to a family of curves, with the parabola
and the hyperbola, that the Greeks studied two thousand years before anyone knew planets moved on them. Then it
answers the question every astronomer and every mission planner has to ask: given an orbit, where is the planet
today? It ends with Mars's own ellipse, which brings Mars half as much sunlight again at its nearest as at its
farthest.*

!!! abstract "In this chapter"
    **You will learn:**

    - how to draw an ellipse, and what its foci, axes and eccentricity are
    - how stretched the orbits of planets, moons, comets and spacecraft are
    - how circles, ellipses, parabolas and hyperbolas make one family, and which visitors from other stars have
      followed hyperbolas through the solar system
    - the names for the nearest and farthest points of an orbit
    - how Kepler's equation tells you where a planet is on any date
    - the six numbers that pin down any orbit in space
    - how Mars's ellipse shapes its seasons and its dust storms
    - why Kepler's equation follows from equal areas

    **You need:** chapter 3.

    **Levels:** 4.1 to 4.3 are beginner; 4.4 to 4.7 are intermediate; 4.8 is advanced; 4.9 is expert.

## 4.1 Two pins and a loop of string { #string }

Push two pins into a board, drop a loop of string over them, pull it tight with a pencil and draw all the way round.
The curve is an ellipse.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Drawing an ellipse with two pins and a loop of string. Two pins stand at the foci, F and F prime, either side of the centre. A string from one pin to the pencil point P and back to the other pin keeps the two distances adding up to the same total, the long width of the ellipse, two a. Labels show the semi-major axis a from the centre to the end of the long axis, the semi-minor axis b from the centre to the top, and the distance c from the centre to each focus, equal to a times e.">
  <g font-size="8" fill="currentColor">
    <ellipse cx="170" cy="112" rx="120" ry="96.0" fill="none" stroke="#c1440e" stroke-width="1"/>
    <line x1="50" y1="112" x2="290" y2="112" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <line x1="170" y1="16.0" x2="170" y2="208.0" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <polyline points="98.0,112 113.7,27.2 242.0,112" fill="none" stroke="#5aa0d8" stroke-width="1.1"/>
    <circle cx="98.0" cy="112" r="2.5" fill="currentColor"/>
    <text x="98.0" y="123" text-anchor="middle">F</text>
    <circle cx="242.0" cy="112" r="2.5" fill="currentColor"/>
    <text x="242.0" y="123" text-anchor="middle">F′</text>
    <circle cx="113.7" cy="27.2" r="2.5" fill="#c1440e"/>
    <text x="109.7" y="21.2" text-anchor="middle">P (pencil)</text>
    <text x="99.8" y="69.6" text-anchor="end" fill="#5aa0d8">r₁</text>
    <text x="183.8" y="69.6" fill="#5aa0d8">r₂</text>
    <text x="230.0" y="134" text-anchor="middle">a</text>
    <line x1="170" y1="128" x2="290" y2="128" stroke="currentColor" stroke-width="0.5"/>
    <text x="174" y="163.0">b</text>
    <text x="134.0" y="108" text-anchor="middle">c = ae</text>
    <circle cx="170" cy="112" r="1.3" fill="currentColor"/>
    <text x="6" y="12">Two pins and a loop of string</text>
    <text x="6" y="226">Wherever the pencil goes, r₁ + r₂ stays the same: the length 2a. The pins are the foci;</text>
    <text x="6" y="235">a is the semi-major axis, b the semi-minor axis, and c = ae the distance from the centre</text>
    <text x="6" y="244">to each focus. Here e = 0.6. Push the pins together and you get a circle.</text>
  </g>
</svg>
</div>

*Figure A. Drawing an ellipse.*

The string keeps the distance from the pencil to one pin plus the distance to the other pin always the same. That is
the definition of an ellipse: the points whose distances from two fixed points, the **foci**, add up to the same
total. Gardeners use two pegs and a rope the same way to mark out oval flower beds.

The size and shape need three lengths, related by $a^2 = b^2 + c^2$:

- the **semi-major axis** $a$, half the longest width; the string's two parts always add up to $2a$;
- the **semi-minor axis** $b$, half the shortest width;
- the distance $c$ from the centre to each focus.

In an orbit, the Sun (or the planet being orbited) sits at one focus. The other focus is empty, a point in space with
nothing there. The physics lesson [Ellipses](https://physics.akadian.ca/topics/gravity/level-7/03-ellipses.html)
works through the same ideas.

??? note "Sources"
    - The definition by the sum of distances to the foci, the pins-and-string method, and the gardener's ellipse:
      Wikipedia, [Ellipse](https://en.wikipedia.org/wiki/Ellipse) (weaker).
    - $a^2 = b^2 + c^2$: when the pencil is at the end of the short axis, each part of the string has length $a$ and
      makes a right-angled triangle with $b$ and $c$; standard.

## 4.2 How stretched? { #eccentricity }

The **eccentricity** $e$ is how far the focus is from the centre, as a fraction of $a$: $e = c / a$. A circle, with
both pins in one hole, has $e = 0$. The closer $e$ gets to 1, the longer and thinner the ellipse.

| Orbit | Eccentricity |
| --- | --- |
| Venus round the Sun | 0.007 |
| Neptune | 0.010 |
| Phobos round Mars | 0.015 |
| Earth | 0.017 |
| the Moon round the Earth | 0.055 |
| Mars | 0.093 |
| Mercury | 0.206 |
| Pluto | 0.244 |
| MAVEN round Mars | 0.46 |
| Halley's comet | 0.967 |

Two simple rules follow. The nearest distance from the focus is $a(1 - e)$ and the farthest is $a(1 + e)$. And the
ellipse is narrower than a circle by a factor $\sqrt{1 - e^2}$, which is tiny for small $e$. Mars's orbit is only 0.44%
narrower than a circle, but its Sun is off-centre by 9.3% of $a$, 21.3 million km. For orbits like the planets', the
shift of the Sun off the centre is what matters, not the squashing.

Pluto shows how much even a modest eccentricity can do. Its average distance is 39.2 AU, but at its nearest it comes
to 29.65 AU, closer to the Sun than Neptune ever gets (29.89 AU). Chapter 11 explains why the two never meet.

??? note "Sources"
    - Eccentricities of Venus (0.0068), Neptune (0.0097), the Earth (0.0167), Mars (0.0935), Mercury (0.2056) and Pluto
      (0.2444), and the perihelion distances of Pluto (4,434.987 million km) and Neptune (4,471.050 million km): NASA
      fact sheets for [Venus](https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html),
      [Neptune](https://nssdc.gsfc.nasa.gov/planetary/factsheet/neptunefact.html),
      [Earth](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html),
      [Mars](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html),
      [Mercury](https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html) and
      [Pluto](https://nssdc.gsfc.nasa.gov/planetary/factsheet/plutofact.html).
    - The Moon (0.0554) and Phobos (0.015): NASA JPL,
      [planetary satellite mean elements](https://ssd.jpl.nasa.gov/sats/elem/). MAVEN: chapter 3, section 3.9.
      Halley's comet (0.96658): Wikipedia, [Halley's Comet](https://en.wikipedia.org/wiki/Halley%27s_Comet) (weaker).
    - Mars's narrowing and off-centre Sun: the history book, chapter 14, section 14.10; our arithmetic in section 4.8.

## 4.3 Circles, ellipses, parabolas and hyperbolas { #conics }

Slice a cone with a flat cut and the edge of the cut is a curve. Slice straight across and you get a circle; tilt the
cut and you get an ellipse; tilt it until it is parallel to the side of the cone and the curve never closes, a
**parabola**; tilt it further and you get a **hyperbola**. These are the **conic sections**.

Greek mathematicians studied them long before anyone connected them with the sky. Menaechmus, who died around 320 BC,
gave the first known definition, and around 200 BC Apollonius of Perga wrote the great work on them; his names
ellipse, parabola and hyperbola are the ones we still use. The family is ordered by eccentricity:

| Curve | Eccentricity | As an orbit |
| --- | --- | --- |
| circle | 0 | goes round for ever at one distance |
| ellipse | between 0 and 1 | goes round for ever, nearer and farther |
| parabola | exactly 1 | comes in once, swings round, leaves for ever |
| hyperbola | more than 1 | the same, but with speed to spare |

Newton's cannon showed all four (chapter 1, [section 1.2](01-Falling-Round-the-Earth.md#cannon)): fire at orbital speed
and the ball circles; faster and it follows an ellipse; at escape speed a parabola; faster still a hyperbola.

**Visitors on hyperbolas.** On 19 October 2017 the Canadian physicist Robert Weryk, using the Pan-STARRS telescope on
Haleakalā in Hawaii, found an object already heading out of the solar system. Its orbit had an eccentricity of 1.20: it
was not bound to the Sun at all, and had come from between the stars. It was named **ʻOumuamua**, the first
interstellar object ever confirmed. Two years later, on 30 August 2019, the amateur astronomer Gennadiy Borisov found a
second with a telescope he had built himself, at his observatory in Nauchnij, Crimea. **2I/Borisov** was a comet, with
an eccentricity of 3.36, and it was leaving at 32 km/s even when far from the Sun.

??? note "Sources"
    - The three conic sections, the circle as a special case of the ellipse, Menaechmus (died 320 BC) giving the first
      definition, Apollonius of Perga's systematic work around 200 BC, and the type of conic set by the eccentricity:
      Wikipedia, [Conic section](https://en.wikipedia.org/wiki/Conic_section) (weaker).
    - Apollonius's definitions of the terms ellipse, parabola and hyperbola being the ones in use today: Wikipedia,
      [Apollonius of Perga](https://en.wikipedia.org/wiki/Apollonius_of_Perga) (weaker).
    - ʻOumuamua, 1I/2017 U1, the first confirmed interstellar object, found by Robert Weryk with Pan-STARRS at
      Haleakalā Observatory on 19 October 2017, with an eccentricity of 1.20: Wikipedia,
      [ʻOumuamua](https://en.wikipedia.org/wiki/%CA%BBOumuamua) (weaker).
    - 2I/Borisov, found on 30 August 2019 by Gennadiy Borisov at his observatory MARGO in Nauchnij, Crimea, with a
      0.65 m telescope he designed and built, eccentricity 3.36, hyperbolic excess speed 32 km/s, the first observed
      rogue comet: Wikipedia, [2I/Borisov](https://en.wikipedia.org/wiki/2I/Borisov) (weaker).
    - The cannon: chapter 1, section 1.2.

## 4.4 Nearest and farthest { #apsides }

The two ends of the long axis are the **apsides**: the nearest point and the farthest. Their names depend on what is
being orbited.

| Orbiting | Nearest | Farthest |
| --- | --- | --- |
| the Sun | perihelion | aphelion |
| the Earth | perigee | apogee |
| anything | periapsis | apoapsis |

For Mars round the Sun, perihelion is $1.5237 \times (1 - 0.0934) = 1.381$ AU, 206.7 million km, and aphelion is
$1.5237 \times (1 + 0.0934) = 1.666$ AU, 249.3 million km. Mars was last at perihelion in late March 2026 and will be at
aphelion in early March 2027, half of 687 days later.

The line joining the apsides does not stay fixed for ever. The pulls of the other planets turn it slowly round, and
for Mercury there is a small extra turning that only Einstein could explain (chapter 18).

??? note "Sources"
    - Perihelion and aphelion, perigee and apogee, periapsis and apoapsis: Wikipedia,
      [Apsis](https://en.wikipedia.org/wiki/Apsis) (weaker).
    - Mars's semi-major axis (1.52371 AU) and eccentricity (0.09339): NASA JPL,
      [approximate orbital elements](https://ssd.jpl.nasa.gov/planets/approx_pos.html). The perihelion of about
      26 March 2026 and aphelion of about 4 March 2027 are worked out by us from those elements and their rates of
      change.
    - The turning of the apsides and Mercury's extra turning: chapters 10 and 18.

## 4.5 Where is the planet now? { #where }

Kepler's second law says how fast a planet moves, but not directly where it is on a given date. To find that, Kepler
used three angles, each measured from perihelion.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The eccentric anomaly. A circle of radius a is drawn round the ellipse, touching it at both ends of the long axis. The planet P is on the ellipse. Straight above it, on the circle, is the point Q. The angle E at the centre, between the long axis and the line to Q, is the eccentric anomaly. The angle nu at the focus, where the Sun is, between the long axis and the line to the planet, is the true anomaly, the planet's real direction from the Sun. The mean anomaly M is the angle a planet moving at a steady rate would have reached; Kepler's equation, M equals E minus e sine E, links it to E.">
  <g font-size="8" fill="currentColor">
    <circle cx="170" cy="112" r="92" fill="none" stroke="#555" stroke-width="0.6" stroke-dasharray="3 3"/>
    <ellipse cx="170" cy="112" rx="92" ry="73.6" fill="none" stroke="#c1440e" stroke-width="1"/>
    <line x1="78" y1="112" x2="262" y2="112" stroke="#555" stroke-width="0.5"/>
    <line x1="170" y1="112" x2="208.9" y2="28.6" stroke="currentColor" stroke-width="0.8"/>
    <line x1="208.9" y1="28.6" x2="208.9" y2="112" stroke="#555" stroke-width="0.5" stroke-dasharray="2 2"/>
    <line x1="225.2" y1="112" x2="208.9" y2="45.3" stroke="#c1440e" stroke-width="0.9"/>
    <path d="M188,112 A18,18 0 0 0 177.6,95.7" fill="none" stroke="currentColor" stroke-width="0.6"/>
    <text x="190.2" y="102.1">E</text>
    <path d="M237.2,112 A12,12 0 0 0 222.3,100.3" fill="none" stroke="#c1440e" stroke-width="0.6"/>
    <text x="237.7" y="101.6" fill="#c1440e">ν</text>
    <circle cx="225.2" cy="112" r="4.5" fill="#eea66f"/>
    <text x="225.2" y="126" text-anchor="middle">Sun (focus)</text>
    <circle cx="170" cy="112" r="1.3" fill="currentColor"/>
    <text x="170" y="122" text-anchor="middle">centre</text>
    <circle cx="208.9" cy="28.6" r="2.5" fill="currentColor"/>
    <text x="213.9" y="25.6">Q, on the circle</text>
    <circle cx="208.9" cy="45.3" r="3" fill="#c1440e"/>
    <text x="214.9" y="48.3">P, the planet</text>
    <text x="265" y="109">perihelion</text>
    <text x="6" y="12">Three angles for one planet</text>
    <text x="6" y="226">ν (true anomaly): the planet's real direction from the Sun. E (eccentric anomaly): the angle</text>
    <text x="6" y="235">at the centre to Q, straight above P on the circle. M (mean anomaly): where a steady planet</text>
    <text x="6" y="244">would be. Kepler's equation links them: M = E − e sin E.</text>
  </g>
</svg>
</div>

*Figure B. Three angles. The circle round the ellipse has radius $a$.*

- The **mean anomaly** $M$ is where the planet would be if it went round at a steady rate: it grows by 360° every
  orbit, so after time $t$ since perihelion, $M = 360^\circ \times t / P$.
- The **eccentric anomaly** $E$ is a helper angle. Draw a circle of radius $a$ round the ellipse, find the point on the
  circle straight above the planet, and measure its angle at the centre.
- The **true anomaly** $\nu$ is the real direction of the planet as seen from the Sun.

They are tied together by **Kepler's equation**,

$$M = E - e \sin E,$$

and the distance from the Sun is $r = a(1 - e\cos E)$. Given the date you know $M$, but the equation runs the wrong way:
it gives $M$ from $E$, not $E$ from $M$. There is no formula that turns it round. Kepler, in 1621, suggested guessing
$E$ and improving the guess again and again, and that is still how it is done: start with $E = M$, then keep
replacing $E$ by $M + e\sin E$. For planets, with small $e$, a few rounds are enough (section 4.8).

??? note "Sources"
    - Kepler's equation, derived in chapter 60 of *Astronomia nova* in 1609, with an iterative solution proposed in book
      V of the *Epitome* in 1621, and its being transcendental, with no algebraic solution: Wikipedia,
      [Kepler's equation](https://en.wikipedia.org/wiki/Kepler%27s_equation) (weaker).
    - The eccentric anomaly as the angle to the point on the circle of radius $a$: Wikipedia,
      [Eccentric anomaly](https://en.wikipedia.org/wiki/Eccentric_anomaly) (weaker). The true anomaly: Wikipedia,
      [True anomaly](https://en.wikipedia.org/wiki/True_anomaly) (weaker).
    - $r = a(1 - e\cos E)$ and Kepler's equation are derived in section 4.9.

## 4.6 Six numbers for an orbit { #elements }

An ellipse in a flat drawing needs two numbers, $a$ and $e$. A real orbit also has to be placed in space and in time,
and that takes six numbers in all, the **orbital elements**:

1. **$a$**, the size;
2. **$e$**, the shape;
3. **$i$**, the **inclination**: how far the orbit's plane is tilted to a reference plane, for planets the plane of the
   Earth's orbit;
4. **$\Omega$**, the **longitude of the ascending node**: the direction in which the orbit climbs up through the
   reference plane;
5. **$\omega$**, the **argument of periapsis**: where in its own plane the nearest point lies;
6. **$M_0$**, the mean anomaly at a chosen moment, the **epoch**: where the body was then.

For Mars, at noon on 1 January 2000, NASA's tables give $a = 1.5237$ AU, $e = 0.0934$, $i = 1.850^\circ$,
$\Omega = 49.56^\circ$, $\omega = 286.50^\circ$ and $M_0 = 19.39^\circ$. With these, Kepler's equation and the rates at
which the numbers slowly change, anyone can work out where Mars is on any date for centuries; that is how Figure A of
chapter 2 was made.

Every tracked satellite has its six numbers too. Since the 1970s they have been shared in a format called the
**two-line element set**, which grew out of the models used by NORAD, the North American air defence command, to
follow everything in orbit. A phone app that
shows you where the space station is uses them.

??? note "Sources"
    - Six orbital elements needed to define a Keplerian orbit, the longitude of the ascending node, the argument of
      periapsis, and the epoch: Wikipedia, [Orbital elements](https://en.wikipedia.org/wiki/Orbital_elements) (weaker).
    - Mars's elements for J2000: NASA JPL, approximate orbital elements (above), table 1: $a = 1.52371034$,
      $e = 0.09339410$, $i = 1.84969142^\circ$, mean longitude $-4.55343205^\circ$, longitude of perihelion
      $-23.94362959^\circ$ (so $336.06^\circ$), $\Omega = 49.55953891^\circ$. Then
      $\omega = 336.06 - 49.56 = 286.50^\circ$ and $M_0 = -4.553 - (-23.944) = 19.39^\circ$: our arithmetic.
    - Max Lane's prediction models of the early 1960s, the model that became NORAD's standard in the early 1970s, and
      the two-line element format that grew from it: Wikipedia,
      [Two-line element set](https://en.wikipedia.org/wiki/Two-line_element_set) (weaker). That tracking apps use them
      is standard.

## 4.7 Mars's ellipse { #mars }

Mars's eccentricity, 0.093, is more than five times the Earth's, and it changes life on Mars.

**Sunlight.** Sunlight weakens with the square of the distance. At perihelion Mars is 206.7 million km from the Sun and
at aphelion 249.3 million km, so it gets $(249.3 / 206.7)^2 = 1.45$ times as much sunlight at its nearest as at its
farthest: 45% more. The Earth's difference is only 7%.

**Seasons and storms.** Because Mars moves fastest near perihelion, the season spent on that part of the orbit is the
shortest: northern autumn, which is southern spring, lasts 142 sols, against 194 for northern spring (history book,
[section 14.9](../history/14-Tycho-and-Kepler.md#onmars)). The strong sunshine near perihelion stirs up the
atmosphere. Dust storms are most common then, and the great storms that wrap the whole planet are often set off by
it. The Opportunity rover sent its last message on 10 June 2018, as the storm of that year darkened its sky (book 2,
[section 20.7](../light-and-telescopes/20-Cameras-and-Telescopes-at-Mars.md#sky)).

**Counting Mars years.** Scientists who study Mars's climate number its years from the northern spring equinox of
11 April 1955, which began Mars Year 1. By that count, Mars Year 38 began in November 2024 and Mars Year 39 at the end
of September 2026.

??? note "Sources"
    - Mars's perihelion and aphelion distances (206.650 and 249.261 million km) and the Earth's (147.095 and
      152.100 million km): NASA fact sheets (above). The sunlight ratios are our arithmetic.
    - Season lengths of 194 and 142 sols: Wikipedia,
      [Timekeeping on Mars](https://en.wikipedia.org/wiki/Timekeeping_on_Mars) (weaker), and the history book,
      chapter 14, section 14.9.
    - Dust storms most common near perihelion, global storms often triggered by solar heating near perihelion, and the
      storm of 2018 that covered the whole planet by 20 June: Wikipedia,
      [Climate of Mars](https://en.wikipedia.org/wiki/Climate_of_Mars) (weaker). Opportunity's last message on 10 June
      2018: book 2, chapter 20, section 20.7, and its sources.
    - Mars years numbered from the equinox of 11 April 1955: Wikipedia, Timekeeping on Mars (above). The starting dates
      of Mars Years 38 and 39 are our arithmetic, adding Mars years of 686.97 days.

## 4.8 Working it out { #working }

**Where is Mars 100 days after perihelion?** Mars's year is 686.98 days, so

$$M = 360^\circ \times \frac{100}{686.98} = 52.40^\circ = 0.9146 \text{ radians}.$$

Solve $E = M + e\sin E$ with $e = 0.0934$, starting from $E = M$:

| Round | $E$ (radians) |
| --- | --- |
| start | 0.9146 |
| 1 | 0.9886 |
| 2 | 0.9926 |
| 3 | 0.9928 |
| 4 | 0.9928 |

So $E = 0.9928$ radians, or 56.89°. Then

$$r = a(1 - e\cos E) = 1.5237 \times (1 - 0.0934 \times 0.5462) = 1.446 \text{ AU} = 216.3 \text{ million km},$$

and the true anomaly, from $\tan\frac{\nu}{2} = \sqrt{\frac{1+e}{1-e}}\tan\frac{E}{2}$, is $\nu = 61.49^\circ$. After
100 days Mars is 61.5° round from perihelion, 9.1° ahead of where a steady planet would be.

The same steps in a few lines of Python:

```python
from math import sin, cos, tan, atan, sqrt, pi
a, e, P, t = 1.5237, 0.0934, 686.98, 100
M = 2 * pi * t / P
E = M
for _ in range(10):
    E = M + e * sin(E)
r = a * (1 - e * cos(E))
nu = 2 * atan(sqrt((1 + e) / (1 - e)) * tan(E / 2))
print(round(E, 4), round(r, 4), round(nu * 180 / pi, 2))
```

| | Mars | Earth |
| --- | --- | --- |
| Semi-major axis $a$ | 1.5237 AU | 1.0000 AU |
| Eccentricity $e$ | 0.0934 | 0.0167 |
| Sun's distance from the centre, $ae$ | 21.3 million km | 2.5 million km |
| Narrowest width ÷ widest, $\sqrt{1 - e^2}$ | 0.9956 | 0.9999 |
| Perihelion, $a(1-e)$ | 1.381 AU | 0.983 AU |
| Aphelion, $a(1+e)$ | 1.666 AU | 1.017 AU |
| Sunlight at perihelion ÷ at aphelion | 1.45 | 1.07 |
| Most the planet runs ahead of or behind a steady pace | 10.7° | 1.9° |

??? note "Sources"
    - Mars's and the Earth's elements: NASA JPL, approximate orbital elements (above), and the NASA fact sheets
      (above). Mars's year of 686.98 days: NASA, Mars fact sheet.
    - The formula for $\nu$ from $E$: Wikipedia, True anomaly (above). The last row: chapter 2, section 2.9.
    - The arithmetic and the program are ours.

## 4.9 Kepler's equation from equal areas { #proof }

Put the centre of the ellipse at the origin, with the long axis along $x$. A point on the circle of radius $a$ at angle
$E$ is $(a\cos E,\ a\sin E)$. Squash the circle by the factor $b/a$ in the $y$ direction and it becomes the ellipse, so
the planet, straight below that point, is at

$$(a\cos E,\ b\sin E).$$

**The distance.** The Sun is at the focus $(ae, 0)$, and $b^2 = a^2(1 - e^2)$. So

$$r^2 = a^2(\cos E - e)^2 + a^2(1 - e^2)\sin^2 E = a^2(1 - 2e\cos E + e^2\cos^2 E) = a^2(1 - e\cos E)^2,$$

which gives $r = a(1 - e\cos E)$.

**The area.** By the second law, the time since perihelion is proportional to the area swept by the line from the Sun
to the planet. Find that area on the circle first. The region of the circle from perihelion, bounded by the line from
the focus to the point at angle $E$, is a sector of the circle minus a triangle:

$$\tfrac12 a^2 E - \tfrac12 (ae)(a\sin E) = \tfrac12 a^2 (E - e\sin E).$$

Squashing by $b/a$ shrinks every area by the same factor, so the area swept on the ellipse is
$\tfrac12 ab\,(E - e\sin E)$. The whole ellipse has area $\pi ab$ and takes one period $P$. Equal areas in equal times
then give

$$\frac{t}{P} = \frac{\tfrac12 ab\,(E - e\sin E)}{\pi ab} = \frac{E - e\sin E}{2\pi}.$$

The left side is $M / 2\pi$, so $M = E - e\sin E$: Kepler's equation. Kepler found it the same way, by areas, in 1609.

??? note "Sources"
    - The derivation is standard; this form follows the auxiliary circle described in Wikipedia, Eccentric anomaly
      (above). Kepler's derivation in *Astronomia nova*, chapter 60: Wikipedia, Kepler's equation (above).

## Check yourself { #check }

**1.** (beginner) You draw an ellipse with two pins 6 cm apart and a loop of string that gives $2a = 10$ cm. What are
$a$, $c$ and $e$?

??? note "Answer"
    $a = 5$ cm. The pins are $2c = 6$ cm apart, so $c = 3$ cm, and $e = c / a = 0.6$. (And $b = \sqrt{25 - 9} = 4$ cm.)

**2.** (beginner) Which orbit is more stretched, the Moon's round the Earth or Mars's round the Sun?

??? note "Answer"
    Mars's: 0.093 against 0.055.

**3.** (beginner) What kind of curve did ʻOumuamua follow, and how do we know it came from outside the solar system?

??? note "Answer"
    A hyperbola. Its eccentricity was 1.20, more than 1, so it was moving too fast to be held by the Sun: it could not
    have been going round the Sun before, and it will not come back.

**4.** (intermediate) Halley's comet has $a = 17.74$ AU and $e = 0.967$. Find its perihelion and aphelion distances.

??? note "Answer"
    Perihelion $17.74 \times 0.033 = 0.59$ AU; aphelion $17.74 \times 1.967 = 34.9$ AU.

**5.** (intermediate) Why does Mars get 45% more sunlight at perihelion, but the Earth only 7%?

??? note "Answer"
    Sunlight goes as one over the distance squared, and the ratio of farthest to nearest distance is
    $(1 + e)/(1 - e)$. For Mars that is 1.206, squared 1.45; for the Earth 1.034, squared 1.07. Mars's orbit is more
    than five times as eccentric.

**6.** (intermediate) Name the six orbital elements and say in a few words what each one fixes.

??? note "Answer"
    $a$: the size. $e$: the shape. $i$: the tilt of the orbit's plane. $\Omega$: the direction in which the orbit
    crosses up through the reference plane. $\omega$: where the nearest point lies within the orbit's plane. $M_0$:
    where the body was at the epoch.

**7.** (advanced) Where is Mars, as seen from the Sun, 200 days after perihelion? Find $M$, $E$ and $r$.

??? note "Answer"
    $M = 360^\circ \times 200 / 686.98 = 104.81^\circ = 1.8292$ rad. Iterating $E = M + 0.0934\sin E$: 1.9195, 1.9170,
    1.9171, so $E = 1.9171$ rad, 109.84°. Then $r = 1.5237 \times (1 + 0.0934 \times 0.3396) = 1.572$ AU, about
    235 million km.

**8.** (expert) Show that at the ends of the short axis, $E = 90^\circ$, the planet is exactly $a$ from the Sun, and
that it reaches that point a fraction $\tfrac14 - \tfrac{e}{2\pi}$ of its period after perihelion. How many days is
that for Mars?

??? note "Answer"
    With $E = 90^\circ$, $r = a(1 - e\cos 90^\circ) = a$. And $M = \tfrac{\pi}{2} - e$, so $t / P = M / 2\pi =
    \tfrac14 - \tfrac{e}{2\pi}$. For Mars, $\tfrac14 - 0.0934 / 6.2832 = 0.2351$, and $0.2351 \times 686.98 = 161.5$
    days, about ten days sooner than a quarter of its year.

## Summary

- An ellipse is the set of points whose distances from two foci add to $2a$; draw one with two pins and a loop of
  string.
- The eccentricity $e = c/a$ measures how stretched it is: 0.017 for the Earth, 0.093 for Mars, 0.967 for Halley's
  comet.
- Nearest and farthest distances are $a(1-e)$ and $a(1+e)$: perihelion and aphelion round the Sun, perigee and apogee
  round the Earth.
- Circles, ellipses, parabolas and hyperbolas are the conic sections, named by Apollonius; ʻOumuamua and 2I/Borisov came
  in on hyperbolas from between the stars.
- Kepler's equation $M = E - e\sin E$ gives where a planet is on any date, solved by repeated guessing.
- Six numbers, the orbital elements, fix any orbit in space and time.
- Mars gets 45% more sunlight at perihelion than at aphelion; its dust storms are most common then.
- Kepler's equation follows from equal areas and a circle squashed into an ellipse.

**Next:** chapter 5, Newton's law of gravity, where one law of force explains all three of Kepler's laws, the fall of
an apple and the orbit of the Moon.

## Further reading

- Roger R. Bate, Donald D. Mueller and Jerry E. White, *Fundamentals of Astrodynamics*, Dover, 1971.
