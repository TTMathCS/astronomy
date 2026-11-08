# 5. Newton's law of gravity

*Kepler described how the planets move. Newton explained why. One rule, that every piece of matter pulls every other
piece, more strongly when it is heavier and more weakly when it is farther, accounts for a falling apple, the space
station, the Moon, and Kepler's three laws all at once. This chapter tests the rule from the ground to the Moon, uses it
to find your weight on other worlds, shows why a planet pulls as if all its mass were at its centre, and finds that the
Sun does not stand still while the planets go round it.*

!!! abstract "In this chapter"
    **You will learn:**

    - how one pull, weakening with the square of the distance, explains an apple's fall and every orbit round the Earth
    - Newton's law of gravity, and how small the constant $G$ is
    - why you would weigh less on Mars, and much less on Phobos
    - why a round planet pulls as if all its mass were at its centre, and what would happen in a tunnel through it
    - how Newton's law gives Kepler's laws, with a small correction to the third
    - why two bodies both go round a point between them, the barycentre
    - how Newton's law is used at Mars
    - how the inverse-square law follows from Kepler's third law

    **You need:** chapters 3 and 4. The story of how Newton came to write the law is in the history book,
    [section 16.2](../history/16-Newton-Halley-and-Romer.md#principia).

    **Levels:** 5.1 to 5.3 are beginner; 5.4 to 5.7 are intermediate; 5.8 is advanced; 5.9 is expert.

## 5.1 From the apple to the Moon { #moon }

A dropped apple falls with an acceleration of 9.82 m/s². The Moon, 60.3 Earth radii away, is falling too: chapter 1
showed that an orbit is a fall that never lands. Newton's idea was that the same pull reaches the Moon, weakened by
the square of the distance, $60.3^2 \approx 3{,}600$ times. The history book works through his test
([section 16.2](../history/16-Newton-Halley-and-Romer.md#principia)).

Today we can do the test at many distances, because we have put things in orbit in between. For anything going round
in a circle, the pull it feels can be worked out from its speed and its distance, or from its period and its distance
(section 5.8). Here are the results, beside the rule "9.82 m/s² divided by the distance squared":

| Where | Distance from the Earth's centre (Earth radii) | Pull worked out from the motion (m/s²) | 9.82 ÷ distance² (m/s²) |
| --- | --- | --- | --- |
| an apple, at the ground | 1 | 9.82 | 9.82 |
| the space station, 400 km up | 1.063 | 8.69 | 8.69 |
| GPS satellites | 4.18 | 0.566 | 0.563 |
| geostationary satellites | 6.62 | 0.224 | 0.224 |
| the Moon | 60.3 | 0.00272 | 0.00270 |

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Newton's Moon test, extended. A log-log chart of the pull of the Earth against distance from the Earth's centre, in Earth radii, from 1 to 100. A straight line shows the inverse-square law, starting at 9.82 metres per second squared at the surface and falling by a factor of four for every doubling of distance. Five measured points lie on the line: an apple falling at the surface; the space station, worked out from its speed and height; GPS satellites and geostationary satellites, from their periods and distances; and the Moon at 60 Earth radii, where the pull is 3,600 times weaker than at the ground, 2.7 millimetres per second squared.">
  <g font-size="8" fill="currentColor">
    <rect x="50" y="24" width="266" height="176" fill="none" stroke="#555" stroke-width="0.6"/>
    <line x1="50.0" y1="200" x2="50.0" y2="203" stroke="#555" stroke-width="0.6"/>
    <text x="50.0" y="211" text-anchor="middle">1</text>
    <line x1="183.0" y1="200" x2="183.0" y2="203" stroke="#555" stroke-width="0.6"/>
    <text x="183.0" y="211" text-anchor="middle">10</text>
    <line x1="316.0" y1="200" x2="316.0" y2="203" stroke="#555" stroke-width="0.6"/>
    <text x="316.0" y="211" text-anchor="middle">100</text>
    <line x1="47" y1="200.0" x2="50" y2="200.0" stroke="#555" stroke-width="0.6"/>
    <text x="45" y="203.0" text-anchor="end">0.001</text>
    <line x1="47" y1="156.0" x2="50" y2="156.0" stroke="#555" stroke-width="0.6"/>
    <text x="45" y="159.0" text-anchor="end">0.01</text>
    <line x1="47" y1="112.0" x2="50" y2="112.0" stroke="#555" stroke-width="0.6"/>
    <text x="45" y="115.0" text-anchor="end">0.1</text>
    <line x1="47" y1="68.0" x2="50" y2="68.0" stroke="#555" stroke-width="0.6"/>
    <text x="45" y="71.0" text-anchor="end">1</text>
    <line x1="47" y1="24.0" x2="50" y2="24.0" stroke="#555" stroke-width="0.6"/>
    <text x="45" y="27.0" text-anchor="end">10</text>
    <line x1="50.0" y1="24.3" x2="316.0" y2="200.3" stroke="#5aa0d8" stroke-width="1"/>
    <text x="176.9" y="100.3" fill="#5aa0d8" transform="rotate(32 176.9 100.3)">pull falls as 1 / distance²</text>
    <circle cx="50.0" cy="24.3" r="2.8" fill="#c1440e"/>
    <text x="57.0" y="39.3" text-anchor="start">apple, at the ground</text>
    <circle cx="53.5" cy="26.7" r="2.8" fill="#c1440e"/>
    <text x="60.5" y="21.7" text-anchor="start">space station, 400 km up</text>
    <circle cx="132.5" cy="78.9" r="2.8" fill="#c1440e"/>
    <text x="138.5" y="74.9" text-anchor="start">GPS</text>
    <circle cx="159.2" cy="96.6" r="2.8" fill="#c1440e"/>
    <text x="165.2" y="92.6" text-anchor="start">geostationary</text>
    <circle cx="286.8" cy="180.9" r="2.8" fill="#c1440e"/>
    <text x="280.8" y="174.9" text-anchor="end">Moon</text>
    <text x="183.0" y="222" text-anchor="middle">distance from the Earth's centre (Earth radii)</text>
    <text x="12" y="112.0" text-anchor="middle" transform="rotate(-90 12 112.0)">pull (m/s²)</text>
    <text x="6" y="12">One pull, from the ground to the Moon</text>
    <text x="6" y="244">Dots: pulls measured from an apple's fall and from each orbit. Line: 9.82 m/s² ÷ distance².</text>
  </g>
</svg>
</div>

*Figure A. One pull, from the ground to the Moon.*

The pull falls by a factor of 3,600 between the ground and the Moon, and at every step it matches the rule. The small
gap for the Moon, under 1%, has a reason that section 5.9 explains.

??? note "Sources"
    - The Earth's surface gravity, 9.82 m/s², and mean radius, 6,371 km: NASA,
      [Mars fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html) (Earth column) and
      [Earth fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html).
    - The Moon's distance (384,400 km) and period (27.3217 days): NASA,
      [Moon fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html).
    - The space station at about 400 km and 7.67 km/s: book 1, chapter 16, section 16.3, as in chapter 1. GPS at
      26,600 km with a period of 11 hours 58 minutes, and geostationary satellites at 42,164 km with a period of
      23 hours 56 minutes: chapter 3, section 3.6.
    - The table and the figure are our arithmetic (section 5.8).

## 5.2 One law for everything { #law }

Newton went further than the Earth. He said that **every** body pulls **every** other body, with a force

$$F = \frac{G\,m_1 m_2}{r^2},$$

where $m_1$ and $m_2$ are the two masses, $r$ is the distance between them, and $G$ is a fixed number, the same
everywhere. In words:

- double either mass and the pull doubles;
- double the distance and the pull drops to a quarter;
- the pull on each body is the same size, in opposite directions. The Earth pulls you down with 687 N if your mass is
  70 kg, and you pull the Earth up with exactly 687 N. The Earth is so heavy that this moves it by nothing you could
  ever measure.

The number $G$ is tiny: $6.674 \times 10^{-11}$ in metres, kilograms and seconds. Two people of 70 kg standing a metre
apart pull on each other with $6.674 \times 10^{-11} \times 70 \times 70 = 3.3 \times 10^{-7}$ N, about two billion
times weaker than the Earth's pull on either of them. Gravity only becomes strong when one of the masses is the size of
a moon or a planet. The first person to measure the pull between ordinary objects in a laboratory was the British
scientist Henry Cavendish, in 1798, 111 years after the *Principia*; chapter 6 tells how, and how it lets us weigh the
Earth.

The physics lesson [The law of gravity](https://physics.akadian.ca/topics/gravity/level-6/01-the-law-of-gravity.html)
covers the same law with more practice.

??? note "Sources"
    - The law $F = G m_1 m_2 / r^2$, $G = 6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻², publication of the *Principia* on 5 July
      1687, and the Cavendish experiment of 1798, 111 years after the *Principia*, as the first laboratory test:
      Wikipedia,
      [Newton's law of universal gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation)
      (weaker).
    - Equal and opposite pulls: Newton's third law; standard. The 687 N, the pull between two people and the ratio are
      our arithmetic.

## 5.3 Your weight on other worlds { #weight }

Put a planet of mass $M$ and radius $R$ into Newton's law, with you on its surface, and the pull on each kilogram of
you is

$$g = \frac{GM}{R^2}.$$

Your **mass**, the amount of you, is the same everywhere. Your **weight**, the pull on you, depends on where you are.

| World | Gravity at the surface (m/s²) | A 70 kg person on bathroom scales made for the Earth |
| --- | --- | --- |
| Earth | 9.82 | 70 kg |
| Mars | 3.73 | 26.6 kg |
| the Moon | 1.62 | 11.6 kg |
| Pluto | 0.62 | 4.4 kg |
| Charon | 0.29 | 2.1 kg |
| Phobos | 0.0057 | 41 grams |

Mars has only 11% of the Earth's mass, but its gravity is 38% of the Earth's. The reason is the $R^2$: Mars's radius is
53% of the Earth's, so you stand much closer to its centre, and $0.107 / 0.532^2 = 0.38$.

On Phobos, a lumpy moon about 22 km across, gravity is so weak that a ball thrown at 41 km/h, the speed of a car in
town, would never fall back (chapter 7 explains why). The physics lessons
[Weight on other worlds](https://physics.akadian.ca/topics/gravity/level-2/03-weight-on-other-worlds.html) and
[g from a planet's size and mass](https://physics.akadian.ca/topics/gravity/level-6/02-g-from-a-planet.html) go
further.

??? note "Sources"
    - Surface gravity of the Earth (9.82), Mars (3.73), the Moon (1.62), Pluto (0.62) and Charon (0.29), and the
      masses and radii of the Earth and Mars: NASA fact sheets for
      [Mars](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html),
      [the Moon](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html) and
      [Pluto](https://nssdc.gsfc.nasa.gov/planetary/factsheet/plutofact.html) (which includes Charon).
    - Phobos's surface gravity, 0.0057 m/s², escape speed 11.39 m/s (41 km/h), and size, 25.90 × 22.60 × 18.32 km:
      Wikipedia, [Phobos (moon)](https://en.wikipedia.org/wiki/Phobos_(moon)) (weaker).
    - The scale readings and the ratio 0.38 are our arithmetic.

## 5.4 Pulling from the centre { #shell }

A planet is not a point. Every rock in it pulls on you, the near ones strongly and the far ones weakly, from many
different directions. Newton proved a remarkable result, now called the **shell theorem**: a ball whose matter is
arranged in even layers pulls on anything outside it exactly as if all its mass were at the centre. That is why, all
through this book, distances are measured from the centre of the Earth, not from its surface.

The theorem has a second half: inside a hollow, even shell, the pulls from all sides cancel, and there is no pull at
all. So if you went down a deep mine, only the part of the Earth below you, the ball closer to the centre than you
are, would pull you down.

**A tunnel through the Earth.** In a letter to Newton, Robert Hooke raised the question of how something would move if
it could fall inside a planet. Picture a tunnel straight through the Earth. In an Earth of even density, the pull
inside grows in proportion to your distance from the centre: half-way down, it is half as strong. You would speed up
all the way to the centre, coast up the other side, arrive just as you stopped, and fall back again for ever. A trip
from one side to the other would take **42 minutes**, wherever the tunnel went, exactly half the time of an orbit
skimming the surface. The real Earth is densest at the centre, which makes the trip about 38 minutes. On Mars, if it
had even density all through, the trip would take 50 minutes.

??? note "Sources"
    - Newton proving the shell theorem, a ball acting as if its mass were at its centre, and no net force inside a
      hollow shell: Wikipedia, [Shell theorem](https://en.wikipedia.org/wiki/Shell_theorem) (weaker).
    - Hooke's letter to Newton, the 2,530 seconds (42.2 minutes) for a uniform Earth, the time being half that of a
      very low orbit, and 38 minutes with the real density: Wikipedia,
      [Gravity train](https://en.wikipedia.org/wiki/Gravity_train) (weaker).
    - Mars: our arithmetic in section 5.8, from the NASA Mars fact sheet.

## 5.5 Kepler's laws from Newton's { #kepler }

Newton showed that his law gives all three of Kepler's laws:

1. **Ellipses.** A force that weakens with the square of the distance makes a body move on a conic section with the
   Sun at a focus: an ellipse if it is bound, a parabola or hyperbola if it is not (chapter 4,
   [section 4.3](04-Ellipses.md#conics)). Another force law would give other shapes; most would not even close.
2. **Equal areas.** Any pull aimed straight at the Sun gives equal areas in equal times, whatever its strength
   (chapter 3, [section 3.10](03-Keplers-Three-Laws.md#newton)).
3. **Squares and cubes.** For a body of mass $m$ going round one of mass $M$,

    $$P^2 = \frac{4\pi^2 a^3}{G\,(M + m)}.$$

The third law gains something here. Kepler's version says $P^2 / a^3$ is the same for every planet. Newton's says it
depends very slightly on the planet's own mass. For most planets the difference is too small to notice, but Jupiter
has 1/1,048 of the Sun's mass. With $a = 5.2029$ AU, Kepler's rule gives a period of 11.868 years; Newton's,
including Jupiter's mass, gives 11.862 years, and the measured period is 11.862 years.

The formula also turns round. Measure the size and period of any orbit, and you can find $G(M + m)$, the combined mass
of the two bodies. That is how the Sun, the planets and their moons are weighed (chapter 6).

??? note "Sources"
    - Newton deriving Kepler's laws from an inverse-square force: the history book, chapter 16, section 16.2, and its
      sources.
    - The third law with $M + m$: standard; derived in section 5.9. That only an inverse-square pull, or one growing
      in step with distance, makes every bound orbit close on itself is Bertrand's theorem; standard.
    - Jupiter's semi-major axis, 5.20288700 AU: NASA JPL,
      [approximate orbital elements](https://ssd.jpl.nasa.gov/planets/approx_pos.html). Jupiter's period
      (4,332.589 days, 11.862 years) and mass (1,898.13 × 10²⁴ kg): NASA,
      [Jupiter fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html). The Sun's mass
      (1,988,400 × 10²⁴ kg): NASA, [Sun fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html).
      The ratio and both periods are our arithmetic.

## 5.6 Both bodies move { #barycentre }

If the Earth pulls the Moon, the Moon pulls the Earth just as hard, so the Earth must move too. It does: the Earth and
the Moon both go round a point between them, their **barycentre**, the balance point of the pair. The heavier body is
nearer to it, by the ratio of the masses.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Where two bodies really turn: three barycentres. Top, the Earth and the Moon: the point they both go round is inside the Earth, about three quarters of the way from the centre to the surface, on the side facing the Moon. Middle, the Sun and Jupiter: the point is just outside the Sun's surface, at 1.07 times the Sun's radius. Bottom, Pluto and Charon, drawn to scale: the point is well outside Pluto, in the space between the two, so both go round empty space.">
  <g font-size="8" fill="currentColor">
    <circle cx="46" cy="48" r="18" fill="#5aa0d8" fill-opacity="0.5" stroke="#5aa0d8" stroke-width="0.8"/>
    <line x1="55.2" y1="44" x2="63.2" y2="52" stroke="currentColor" stroke-width="1.2"/>
    <line x1="55.2" y1="52" x2="63.2" y2="44" stroke="currentColor" stroke-width="1.2"/>
    <text x="46" y="76" text-anchor="middle">Earth</text>
    <line x1="66.0" y1="48" x2="184" y2="48" stroke="#555" stroke-width="0.5" stroke-dasharray="2 2"/>
    <path d="M179,45 L184,48 L179,51" fill="none" stroke="#555" stroke-width="0.5"/>
    <text x="188" y="51">to the Moon</text>
    <text x="242" y="45">inside the Earth:</text>
    <text x="242" y="55">4,671 km from its centre</text>
    <circle cx="46" cy="118" r="18" fill="#eea66f" fill-opacity="0.5" stroke="#eea66f" stroke-width="0.8"/>
    <line x1="61.2" y1="114" x2="69.2" y2="122" stroke="currentColor" stroke-width="1.2"/>
    <line x1="61.2" y1="122" x2="69.2" y2="114" stroke="currentColor" stroke-width="1.2"/>
    <text x="46" y="146" text-anchor="middle">Sun</text>
    <line x1="66.0" y1="118" x2="184" y2="118" stroke="#555" stroke-width="0.5" stroke-dasharray="2 2"/>
    <path d="M179,115 L184,118 L179,121" fill="none" stroke="#555" stroke-width="0.5"/>
    <text x="188" y="121">to Jupiter</text>
    <text x="242" y="115">just outside the Sun:</text>
    <text x="242" y="125">1.07 Sun radii</text>
    <circle cx="46" cy="188" r="9" fill="#cfc8bf" fill-opacity="0.5" stroke="#cfc8bf" stroke-width="0.8"/>
    <line x1="58.1" y1="184" x2="66.1" y2="192" stroke="currentColor" stroke-width="1.2"/>
    <line x1="58.1" y1="192" x2="66.1" y2="184" stroke="currentColor" stroke-width="1.2"/>
    <text x="46" y="207" text-anchor="middle">Pluto</text>
    <line x1="55.0" y1="188" x2="194.5" y2="188" stroke="#555" stroke-width="0.5" stroke-dasharray="2 2"/>
    <circle cx="194.5" cy="188" r="4.6" fill="#cfc8bf" stroke="#555" stroke-width="0.5"/>
    <text x="194.5" y="207" text-anchor="middle">Charon</text>
    <text x="242" y="185">outside Pluto:</text>
    <text x="242" y="195">2,126 km from its centre</text>
    <text x="6" y="12">Where two bodies really turn</text>
    <text x="6" y="235">×: the barycentre, the point both bodies go round. Top two not to scale for distance;</text>
    <text x="6" y="244">Pluto and Charon drawn to scale.</text>
  </g>
</svg>
</div>

*Figure B. Three barycentres.*

- **The Earth and the Moon.** The Moon has 1/81 of the Earth's mass, so the balance point is 1/82 of the way from the
  Earth's centre to the Moon's: 4,671 km from the Earth's centre, still inside the Earth. The Earth wobbles round it
  once a month.
- **The Sun and Jupiter.** The Sun has 1,048 times Jupiter's mass, but Jupiter is 778 million km away. The balance
  point is 742,000 km from the Sun's centre, just outside its surface. The Sun goes round it every 11.9 years at about
  12.5 m/s, 45 km/h. Wobbles like this, seen in other stars, are one way planets round them are
  found.
- **Pluto and Charon.** Charon has 1/8 of Pluto's mass and is 16.5 Pluto radii away, so the balance point is 2,126 km
  from Pluto's centre, about 940 km above its surface. Pluto and Charon both go round empty space, every 6.387 days.
  Charon was found in 1978 by James Christy at the United States Naval Observatory.

??? note "Sources"
    - The barycentre as the centre of mass the bodies orbit, the Earth–Moon barycentre 4,671 km from the Earth's centre,
      the Sun–Jupiter barycentre just outside the Sun, and the Pluto–Charon barycentre outside Pluto: Wikipedia,
      [Barycenter (astronomy)](https://en.wikipedia.org/wiki/Barycenter_(astronomy)) (weaker).
    - Masses of the Earth and the Moon: NASA, Moon fact sheet (above). Jupiter's distance (778.479 million km) and
      speed (13.06 km/s) and the Sun's radius (695,700 km): NASA, Jupiter and Sun fact sheets (above). Pluto's and
      Charon's masses, Pluto's radius, Charon's distance (19,596 km) and period (6.3872 days): NASA, Pluto fact sheet
      (above). The distances and the Sun's speed are our arithmetic.
    - Charon's discovery in 1978 by James Christy at the United States Naval Observatory: Wikipedia,
      [Charon (moon)](https://en.wikipedia.org/wiki/Charon_(moon)) (weaker).
    - Finding planets of other stars by their wobble: standard.

## 5.7 Newton's law at Mars { #mars }

**The two moons.** Phobos and Deimos make a small version of Figure A. Phobos, 9,378 km from Mars's centre, goes round
in 7.65 hours; Deimos, at 23,459 km, in 30.3 hours. Working out the pull from each orbit gives 0.488 and 0.0778 m/s²,
and "3.73 m/s² divided by the distance squared, in Mars radii" gives 0.487 and 0.0779. The history book does the same
test with Phobos ([section 16.8](../history/16-Newton-Halley-and-Romer.md#working)).

**Mars wobbles too.** Phobos has about one sixty-millionth of Mars's mass, so the balance point of Mars and Phobos is
only about 16 cm from Mars's centre.

**Gravity is not quite the same everywhere.** A planet is not a perfect ball of even layers, so the shell theorem is
only nearly true. On Mars, gravity at the surface averages about 3.72 m/s² but varies by about 0.059 m/s², around
1.6%, from place to place. Volcanoes show up as spots of slightly stronger gravity, and deep basins as weaker.
Scientists map these differences by tracking the radio signals of orbiting spacecraft: a craft speeds up a little as
it passes over extra mass, and the tiny change in speed shows up in its signal. The most detailed map, made in 2016,
used 16 years of tracking of NASA's Mars Global Surveyor, Mars Odyssey and Mars Reconnaissance Orbiter, and shows
features down to about 115 km across.

??? note "Sources"
    - The orbits of Phobos (9,378 km, 0.31891 days) and Deimos (23,459 km, 1.26244 days), Phobos's mass
      (10.6 × 10¹⁵ kg) and Mars's mass and radius: NASA, Mars fact sheet (above). The pulls and the 16 cm are our
      arithmetic.
    - Mars's average surface gravity of 3.721 m/s² and its variation of about 0.059 m/s², the gravity highs of
      volcanic features and lows of deep depressions, tracking by Doppler with the Deep Space Network, and the Goddard
      Mars Model 3 of 2016 from 16 years of tracking of Mars Global Surveyor, Mars Odyssey and Mars Reconnaissance
      Orbiter, with a resolution of 115 km: Wikipedia,
      [Gravity of Mars](https://en.wikipedia.org/wiki/Gravity_of_Mars) (weaker).

## 5.8 Working it out { #working }

**The pull from an orbit.** Something moving at speed $v$ round a circle of radius $r$ is pulled towards the centre
with an acceleration $v^2 / r$. If you know the period $P$ instead, $v = 2\pi r / P$ and the acceleration is
$4\pi^2 r / P^2$.

- The space station: $v = 7{,}670$ m/s, $r = 6{,}771$ km, so $7{,}670^2 / 6.771 \times 10^6 = 8.69$ m/s².
  The rule gives $9.82 \times (6{,}371 / 6{,}771)^2 = 8.69$ m/s².
- GPS: $r = 2.66 \times 10^7$ m, $P = 43{,}080$ s, so $4\pi^2 \times 2.66 \times 10^7 / 43{,}080^2 = 0.566$ m/s².
- The Moon: $r = 3.844 \times 10^8$ m, $P = 27.3217$ days $= 2{,}360{,}600$ s, so
  $4\pi^2 \times 3.844 \times 10^8 / 2{,}360{,}600^2 = 0.00272$ m/s². The rule gives $9.82 / 60.34^2 = 0.00270$ m/s².

**A tunnel through Mars.** Half the period of an orbit skimming the surface is $\pi\sqrt{R/g}$. For Mars,
$\pi\sqrt{3{,}389{,}500 / 3.73} = 2{,}995$ s, 49.9 minutes. For the Earth, $\pi\sqrt{6{,}371{,}000 / 9.82} = 2{,}530$ s,
42.2 minutes.

| | Mars | Earth |
| --- | --- | --- |
| Mass | $0.642 \times 10^{24}$ kg | $5.972 \times 10^{24}$ kg |
| Mean radius | 3,389.5 km | 6,371.0 km |
| $GM$ | 42,828 km³/s² | 398,600 km³/s² |
| Gravity at the surface, $GM/R^2$ | 3.73 m/s² | 9.82 m/s² |
| Gravity 400 km up | 2.98 m/s² | 8.69 m/s² |
| A 70 kg person on Earth scales | 26.6 kg | 70 kg |
| Trip through a tunnel of even density | 50 minutes | 42 minutes |
| Balance point with its largest moon, from the centre | 16 cm | 4,671 km |

??? note "Sources"
    - Masses, radii, $GM$ and surface gravity: NASA, Mars fact sheet and Moon fact sheet (above). The rest is our
      arithmetic.

## 5.9 From the third law to the inverse square { #inverse }

Newton could run the argument either way. Here is the direction that tells you the force must be inverse-square,
using circular orbits.

For a circle, the pull per kilogram is $4\pi^2 r / P^2$ (section 5.8). Kepler's third law says $P^2 = k\,r^3$, with the
same $k$ for every planet. Put that in:

$$\text{pull} = \frac{4\pi^2 r}{k\,r^3} = \frac{4\pi^2}{k}\cdot\frac{1}{r^2}.$$

So if the third law holds, the pull must fall off as $1/r^2$. A pull falling as $1/r$ would instead give $P^2 \propto
r^2$, and one falling as $1/r^3$ would give $P^2 \propto r^4$. The planets choose $1/r^2$.

**Both bodies move.** Now let both bodies feel the pull. The planet, mass $m$, is pulled towards the Sun with
acceleration $GM/r^2$; the Sun, mass $M$, is pulled towards the planet with acceleration $Gm/r^2$. Their accelerations
point towards each other, so the line between them shrinks as if one body were fixed and the other had acceleration

$$\frac{GM}{r^2} + \frac{Gm}{r^2} = \frac{G(M + m)}{r^2}.$$

For a circular orbit this must equal $4\pi^2 r / P^2$, which gives

$$P^2 = \frac{4\pi^2 r^3}{G\,(M + m)}.$$

This also clears up the Moon's 1% in section 5.1. The Moon's mass is 1.23% of the Earth's, so the pull that shapes its
orbit is $0.00270 \times 1.0123 = 0.00273$ m/s², against the 0.00272 measured. What is left is due mostly to the Sun's
pull on the Moon (chapter 10).

??? note "Sources"
    - The derivation is standard. The Moon's mass as 0.0123 of the Earth's: NASA, Moon fact sheet (above). The
      leftover of about 0.3% from the Sun's pull: standard; the Sun's average outward tidal pull on the Moon is about
      half of $(1/13.37)^2$ of the Earth's, 0.28%, our estimate.

## Check yourself { #check }

**1.** (beginner) At 6,371 km above the ground, twice as far from the Earth's centre as the surface, how strong is the
Earth's gravity?

??? note "Answer"
    A quarter as strong: $9.82 / 4 = 2.46$ m/s².

**2.** (beginner) The Earth pulls you down with 687 N. How hard do you pull the Earth?

??? note "Answer"
    Exactly 687 N, upwards. The pulls are equal and opposite; the Earth just has far more mass, so its acceleration is
    tiny, about $10^{-22}$ m/s².

**3.** (beginner) An astronaut with a mass of 70 kg lands on Mars. What is their mass there, and what would bathroom
scales made for the Earth read?

??? note "Answer"
    The mass is still 70 kg. The scales would read about 26.6 kg, because Mars pulls with 3.73 m/s² instead of 9.82.

**4.** (intermediate) Pluto has 0.0022 times the Earth's mass and 0.186 times its radius. Work out the gravity at its
surface.

??? note "Answer"
    $9.82 \times 0.0022 / 0.186^2 = 9.82 \times 0.0022 / 0.0346 = 0.62$ m/s², as NASA lists.

**5.** (intermediate) Why is the balance point of Pluto and Charon outside Pluto, while the Earth and Moon's is inside
the Earth?

??? note "Answer"
    The balance point is a fraction $m / (M + m)$ of the way from the bigger body. Charon has 0.122 of Pluto's mass and
    is 16.5 Pluto radii away: $16.5 \times 0.122 / 1.122 = 1.79$ Pluto radii, outside. The Moon has 0.0123 of the
    Earth's mass and is 60.3 Earth radii away: $60.3 \times 0.0123 / 1.0123 = 0.73$ Earth radii, inside.

**6.** (intermediate) How long would it take to fall through a tunnel through the Moon, if the Moon had even density?
Use $R = 1{,}737$ km and $g = 1.62$ m/s².

??? note "Answer"
    $\pi\sqrt{1{,}737{,}000 / 1.62} = \pi \times 1{,}035 = 3{,}250$ s, about 54 minutes.

**7.** (advanced) Deimos is 23,459 km from Mars's centre and goes round in 1.26244 days. Work out the pull on it from
its orbit, and compare it with $3.73 \times (3{,}389.5 / 23{,}459)^2$.

??? note "Answer"
    $P = 1.26244 \times 86{,}400 = 109{,}075$ s. Pull $= 4\pi^2 \times 2.3459 \times 10^7 / 109{,}075^2 = 0.0778$ m/s².
    The rule gives $3.73 \times 0.1445^2 = 0.0779$ m/s². They agree.

**8.** (expert) Show that the time to fall through a tunnel in a planet of even density depends only on the density
$\rho$, and is $\pi\sqrt{3 / (4\pi G\rho)}$. Use it for Mars, $\rho = 3{,}934$ kg/m³.

??? note "Answer"
    The mass is $M = \tfrac43\pi R^3\rho$, so $g = GM/R^2 = \tfrac43\pi G\rho R$ and $R/g = 3/(4\pi G\rho)$: the
    radius cancels. Then the time is $\pi\sqrt{R/g} = \pi\sqrt{3/(4\pi G\rho)}$. For Mars,
    $4\pi \times 6.674 \times 10^{-11} \times 3{,}934 = 3.299 \times 10^{-6}$, so the time is
    $\pi\sqrt{3 / 3.299 \times 10^{-6}} = \pi \times 954 = 2{,}996$ s, 49.9 minutes, as in section 5.8.

## Summary

- The pull of the Earth falls with the square of the distance from its centre, from 9.82 m/s² at the ground to
  0.0027 m/s² at the Moon, and satellites in between confirm it.
- Newton's law: every two bodies pull each other with $F = Gm_1m_2/r^2$, equally and oppositely; $G$ is
  $6.674 \times 10^{-11}$.
- Gravity at a planet's surface is $GM/R^2$: 3.73 m/s² on Mars, 0.0057 m/s² on Phobos.
- A round planet pulls as if all its mass were at its centre; inside a hollow shell there is no pull at all.
- Newton's law gives Kepler's three laws, with the third corrected to $P^2 = 4\pi^2a^3 / G(M + m)$.
- Two bodies both go round their barycentre: inside the Earth for the Moon, just outside the Sun for Jupiter, and in
  empty space for Pluto and Charon.
- At Mars, Phobos and Deimos follow the same law, and tracking orbiters maps small changes in gravity across the planet.

**Next:** [chapter 6, Weighing the Sun, the planets and their moons](06-Weighing.md), where orbits give the masses of
the Sun, the planets and their moons, and a laboratory experiment gives the mass of the Earth.

## Further reading

- S. Chandrasekhar, *Newton's Principia for the Common Reader*, Clarendon Press, Oxford, 1995.
