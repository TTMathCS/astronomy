# 7. Orbital speed, energy and escape

*How fast does an orbit go, and what does it cost to get there? This chapter finds the speed of any circular orbit,
meets the strange rule that a satellite slowed by air ends up going faster, and counts the energy needed to climb out
of a planet's gravity. It finds the escape speed of every planet, follows the spacecraft that have left the Earth and
the one that is leaving the Sun, and ends with the rocks that left Mars by themselves and landed on the Earth.*

!!! abstract "In this chapter"
    **You will learn:**

    - how fast a circular orbit goes at any distance
    - why drag makes a satellite speed up, and why you slow down to catch up in orbit
    - how much energy an orbit holds, and why getting to low orbit is more than half the way to escaping
    - the escape speed of the Earth, Mars and other worlds, and why it is a speed and not a velocity
    - which spacecraft are bound to the Sun and which are leaving it for good
    - how to find the speed anywhere on an ellipse
    - how rocks and air leave Mars
    - where the formulas for energy, escape speed and speed on an ellipse come from

    **You need:** chapters 4 and 5.

    **Levels:** 7.1, 7.2 and 7.4 are beginner; 7.3 and 7.5 to 7.7 are intermediate; 7.8 is advanced; 7.9 is expert.

## 7.1 How fast is an orbit? { #speed }

For a circular orbit of radius $r$ round a body with $GM$, the pull of gravity must be just enough to bend the path
into a circle (chapter 5, [section 5.8](05-Newtons-Law-of-Gravity.md#working)): $v^2 / r = GM / r^2$. So

$$v = \sqrt{\frac{GM}{r}}.$$

Four times farther out, half the speed.

| Orbit | Distance from the centre | Speed (km/s) |
| --- | --- | --- |
| the space station, round the Earth | 6,771 km | 7.67 |
| GPS satellites | 26,600 km | 3.87 |
| geostationary satellites | 42,164 km | 3.07 |
| the Moon | 384,400 km | 1.02 |
| Phobos, round Mars | 9,378 km | 2.14 |
| Deimos, round Mars | 23,459 km | 1.35 |
| Mercury, round the Sun | 0.39 AU | 47.4 |
| the Earth | 1.00 AU | 29.8 |
| Mars | 1.52 AU | 24.1 |
| Jupiter | 5.20 AU | 13.1 |
| Neptune | 30.1 AU | 5.4 |

The physics lesson
[Orbital speed](https://physics.akadian.ca/topics/gravity/level-6/03-orbital-speed.html) has more examples.

??? note "Sources"
    - Mean orbital speeds of Mercury (47.36), the Earth (29.78), Mars (24.08), Jupiter (13.06) and Neptune
      (5.45 km/s), and of the Moon (1.022): NASA fact sheets for
      [Mercury](https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html),
      [Earth](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html),
      [Mars](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html),
      [Jupiter](https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html),
      [Neptune](https://nssdc.gsfc.nasa.gov/planetary/factsheet/neptunefact.html) and
      [Moon](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html).
    - The space station's 7.67 km/s: book 1, chapter 16, section 16.3, as in chapter 1. GPS and geostationary
      distances: chapter 3, section 3.6. Phobos and Deimos: NASA, Mars fact sheet. The other speeds are our arithmetic
      from $\sqrt{GM/r}$, with $GM$ from chapter 6.

## 7.2 Faster by slowing down { #paradox }

Orbits have a habit of doing the opposite of what you expect.

**Drag speeds a satellite up.** The space station brushes through a trace of air 400 km up, and the drag slowly takes
away its energy, so it sinks, about 2 km a month (chapter 1, [section 1.6](01-Falling-Round-the-Earth.md#decay)). But a
lower orbit is a faster one. So the drag, which pushes backwards on the station, ends up making it go faster: about
1 m/s faster for every 2 km it sinks.

**To catch up, slow down.** Suppose a supply ship is in the same orbit as the station but some way behind. Firing the
engine forwards, to go faster, would lift the ship into a higher, slower orbit, and it would fall further behind.
Instead the ship fires backwards. It drops into a lower, faster orbit, gains on the station, and then fires forwards at
the right moment to rise back up to meet it.

The reason for both is the same. In a lower circle the ship has less energy in all, but more of it is in its motion
(section 7.3).

??? note "Sources"
    - The station's height, speed and loss of height: chapter 1, sections 1.3 and 1.6, and their sources.
    - The speed gained for 2 km of sinking, $\sqrt{GM/6{,}769} - \sqrt{GM/6{,}771}$ with $GM = 398{,}600$ km³/s², is
      about 1.1 m/s: our arithmetic. That drag speeds a satellite up, and the method of catching up: standard.

## 7.3 The energy of an orbit { #energy }

Lifting something takes energy. Near the ground the energy needed is $mgh$, but gravity weakens with height, so for
big climbs the right formula is the **gravitational potential energy**

$$U = -\frac{GMm}{r}.$$

It is negative because the zero is put far away, where the pull has faded to nothing; everything closer is lower than
that, down in the planet's "gravity well". Climbing from radius $r_1$ to $r_2$ costs $GMm\,(1/r_1 - 1/r_2)$.

A body in a circular orbit also has motion energy, $\tfrac12 mv^2 = GMm / 2r$. Adding the two gives the total

$$E = -\frac{GMm}{2r},$$

and for an ellipse, $E = -GMm / 2a$ (section 7.9). So the total energy depends only on the size of the orbit, and a
higher orbit has more energy, even though it is slower.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Energy needed to lift each kilogram from the ground, ignoring the spin of the planet, in megajoules. From the Earth: to a low orbit 400 kilometres up, 33.1; to the GPS orbit, 55.1; to geostationary orbit, 57.8; to escape the Earth completely, 62.6. From Mars: to a low orbit 200 kilometres up, 6.7; to areostationary orbit, 11.6; to escape Mars, 12.6. Reaching low Earth orbit takes more than half the energy of escaping, and escaping Mars takes about a fifth of the energy of escaping the Earth.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="24" font-weight="bold">From the Earth</text>
    <rect x="112" y="30" width="96.8" height="12" fill="#5aa0d8"/>
    <text x="108" y="39" text-anchor="end">low orbit, 400 km up</text>
    <text x="212.8" y="39">33.1</text>
    <rect x="112" y="48" width="161.0" height="12" fill="#5aa0d8"/>
    <text x="108" y="57" text-anchor="end">GPS orbit</text>
    <text x="277.0" y="57">55.1</text>
    <rect x="112" y="66" width="169.1" height="12" fill="#5aa0d8"/>
    <text x="108" y="75" text-anchor="end">geostationary orbit</text>
    <text x="285.1" y="75">57.8</text>
    <rect x="112" y="84" width="182.9" height="12" fill="#5aa0d8"/>
    <text x="108" y="93" text-anchor="end">escape</text>
    <text x="298.9" y="93">62.6</text>
    <text x="6" y="116" font-weight="bold">From Mars</text>
    <rect x="112" y="122" width="19.5" height="12" fill="#c1440e"/>
    <text x="108" y="131" text-anchor="end">low orbit, 200 km up</text>
    <text x="135.5" y="131">6.7</text>
    <rect x="112" y="140" width="33.9" height="12" fill="#c1440e"/>
    <text x="108" y="149" text-anchor="end">areostationary orbit</text>
    <text x="149.9" y="149">11.6</text>
    <rect x="112" y="158" width="36.9" height="12" fill="#c1440e"/>
    <text x="108" y="167" text-anchor="end">escape</text>
    <text x="152.9" y="167">12.6</text>
    <line x1="112" y1="180" x2="302" y2="180" stroke="#555" stroke-width="0.6"/>
    <line x1="112.0" y1="180" x2="112.0" y2="183" stroke="#555" stroke-width="0.6"/>
    <text x="112.0" y="191" text-anchor="middle">0</text>
    <line x1="170.5" y1="180" x2="170.5" y2="183" stroke="#555" stroke-width="0.6"/>
    <text x="170.5" y="191" text-anchor="middle">20</text>
    <line x1="228.9" y1="180" x2="228.9" y2="183" stroke="#555" stroke-width="0.6"/>
    <text x="228.9" y="191" text-anchor="middle">40</text>
    <line x1="287.4" y1="180" x2="287.4" y2="183" stroke="#555" stroke-width="0.6"/>
    <text x="287.4" y="191" text-anchor="middle">60</text>
    <text x="207.0" y="201" text-anchor="middle">megajoules per kilogram</text>
    <text x="6" y="12">The climb out: energy for each kilogram, from the ground</text>
    <text x="6" y="235">Reaching a low orbit round the Earth already takes more than half the energy of escaping.</text>
    <text x="6" y="244">Leaving Mars takes about a fifth of the energy of leaving the Earth. (Planet spin left out.)</text>
  </g>
</svg>
</div>

*Figure A. The energy to climb from the ground.*

Per kilogram, the Earth's well is 62.6 megajoules deep. Reaching a low orbit takes 33.1 MJ, more than half of that,
because a low orbit needs both the climb and the high speed. Once there, all the far places, geostationary orbit, the
Moon, the open solar system, are nearer in energy than the ground you left. Mars's well is only 12.6 MJ deep, a fifth
of the Earth's.

The physics lesson
[Gravitational energy](https://physics.akadian.ca/topics/gravity/level-7/01-gravitational-energy.html) goes further.

??? note "Sources"
    - $U = -GMm/r$, the motion energy of a circular orbit, and the total $-GMm/2r$: standard, as in the physics lesson
      above. For an ellipse, $-GMm/2a$: Wikipedia,
      [Specific orbital energy](https://en.wikipedia.org/wiki/Specific_orbital_energy) (weaker).
    - The energies per kilogram are our arithmetic from $GM$ and the radii (NASA, Earth and Mars fact sheets), leaving
      out the spin of the planet.

## 7.4 Escape speed { #escape }

Throw a ball up and it comes back. Throw it faster and it goes higher. Fast enough, and it never comes back: its
motion energy is enough to climb all the way out of the well. Setting $\tfrac12 mv^2 = GMm / R$ gives the **escape
speed**

$$v_\text{esc} = \sqrt{\frac{2GM}{R}},$$

exactly $\sqrt2 = 1.414$ times the speed of a circular orbit at the same place.

| World | Escape speed from the surface (km/s) |
| --- | --- |
| the Sun | 617.6 |
| Jupiter | 59.5 |
| the Earth | 11.19 |
| Venus | 10.36 |
| Mars | 5.03 |
| Mercury | 4.3 |
| the Moon | 2.38 |
| Pluto | 1.21 |
| Phobos | 0.011 |

Escape speed is really a speed, not a velocity, because the direction does not matter: going straight up or sideways,
as long as you miss the planet, you need the same speed. Direction does matter in one way. The Earth's surface at the
equator is already moving east at 465 m/s, so a rocket launched eastwards there needs only about 10.74 km/s relative
to the ground.

Nor does a rocket have to reach escape speed in one go. It can keep firing and climb at any speed; the energy needed
is the same in the end. The first spacecraft to escape the Earth was the Soviet Luna 1, launched on 2 January 1959. It
was meant to hit the Moon, missed it by about 6,000 km, and went on into orbit round the Sun, the first spacecraft to
do so.

??? note "Sources"
    - Escape speeds of the Sun (617.6), Jupiter (59.5), the Earth (11.186), Venus (10.36), Mars (5.03), Mercury (4.3),
      the Moon (2.38) and Pluto (1.21 km/s): NASA fact sheets (above), and for the
      [Sun](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html),
      [Venus](https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html) and
      [Pluto](https://nssdc.gsfc.nasa.gov/planetary/factsheet/plutofact.html). Phobos, 11.39 m/s: Wikipedia,
      [Phobos (moon)](https://en.wikipedia.org/wiki/Phobos_(moon)) (weaker).
    - Escape velocity being independent of direction, the 465 m/s of the equator and the 10.735 km/s eastwards, and a
      rocket under thrust escaping at any speed with the same minimum energy: Wikipedia,
      [Escape velocity](https://en.wikipedia.org/wiki/Escape_velocity) (weaker).
    - Luna 1, launched on 2 January 1959, meant to hit the Moon, missing it by 5,995 km, the first spacecraft to leave
      the Earth's orbit and the first in orbit round the Sun: Wikipedia,
      [Luna 1](https://en.wikipedia.org/wiki/Luna_1) (weaker).

## 7.5 Bound or free { #bound }

The same rule works round the Sun. At the Earth's distance, a circular orbit goes at 29.8 km/s and escape speed is
42.1 km/s. A body there moving slower than 42.1 km/s is **bound**: it is on an ellipse and will come back. One moving
faster is **free**, on a hyperbola, and will leave the solar system for good.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Bound or free round the Sun. A log-log chart of speed against distance from the Sun, from 0.01 to 1,000 astronomical units. A lower line shows the speed of a circular orbit, 29.8 kilometres per second at the Earth's distance and falling with the square root of the distance; the planets from Mercury to Neptune lie on it. An upper line, 1.41 times higher, shows escape speed, 42.1 kilometres per second at the Earth's distance. Below the upper line an object is bound to the Sun; above it, it is free. The Parker Solar Probe, at 191 kilometres per second only 6.9 million kilometres from the Sun, is just below the escape line, still bound. Voyager 1, at 17 kilometres per second and 172 astronomical units, is far above it, leaving the Sun for good.">
  <g font-size="8" fill="currentColor">
    <polygon points="46,22 46.0,43.8 326.0,188.8 326,22" fill="#5aa0d8" fill-opacity="0.12"/>
    <rect x="46" y="22" width="280" height="174" fill="none" stroke="#555" stroke-width="0.6"/>
    <line x1="46.0" y1="196" x2="46.0" y2="199" stroke="#555" stroke-width="0.6"/>
    <text x="46.0" y="207" text-anchor="middle">0.01</text>
    <line x1="102.0" y1="196" x2="102.0" y2="199" stroke="#555" stroke-width="0.6"/>
    <text x="102.0" y="207" text-anchor="middle">0.1</text>
    <line x1="158.0" y1="196" x2="158.0" y2="199" stroke="#555" stroke-width="0.6"/>
    <text x="158.0" y="207" text-anchor="middle">1</text>
    <line x1="214.0" y1="196" x2="214.0" y2="199" stroke="#555" stroke-width="0.6"/>
    <text x="214.0" y="207" text-anchor="middle">10</text>
    <line x1="270.0" y1="196" x2="270.0" y2="199" stroke="#555" stroke-width="0.6"/>
    <text x="270.0" y="207" text-anchor="middle">100</text>
    <line x1="326.0" y1="196" x2="326.0" y2="199" stroke="#555" stroke-width="0.6"/>
    <text x="326.0" y="207" text-anchor="middle">1,000</text>
    <line x1="43" y1="196.0" x2="46" y2="196.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="199.0" text-anchor="end">1</text>
    <line x1="43" y1="138.0" x2="46" y2="138.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="141.0" text-anchor="end">10</text>
    <line x1="43" y1="80.0" x2="46" y2="80.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="83.0" text-anchor="end">100</text>
    <line x1="43" y1="22.0" x2="46" y2="22.0" stroke="#555" stroke-width="0.6"/>
    <text x="41" y="25.0" text-anchor="end">1,000</text>
    <line x1="46.0" y1="52.5" x2="326.0" y2="197.5" stroke="currentColor" stroke-width="1"/>
    <line x1="46.0" y1="43.8" x2="326.0" y2="188.8" stroke="#5aa0d8" stroke-width="1"/>
    <circle cx="134.9" cy="98.8" r="2.2" fill="#c1440e"/>
    <text x="129.9" y="110.8" text-anchor="end">Mercury</text>
    <circle cx="150.1" cy="106.4" r="2.2" fill="#c1440e"/>
    <circle cx="158.0" cy="110.5" r="2.2" fill="#c1440e"/>
    <text x="158.0" y="121.5" text-anchor="middle">Earth</text>
    <circle cx="168.2" cy="115.9" r="2.2" fill="#c1440e"/>
    <text x="168.2" y="136.9" text-anchor="middle">Mars</text>
    <circle cx="198.1" cy="131.3" r="2.2" fill="#c1440e"/>
    <text x="198.1" y="142.3" text-anchor="middle">Jupiter</text>
    <circle cx="212.8" cy="138.8" r="2.2" fill="#c1440e"/>
    <circle cx="229.9" cy="147.8" r="2.2" fill="#c1440e"/>
    <circle cx="240.8" cy="153.3" r="2.2" fill="#c1440e"/>
    <text x="240.8" y="164.3" text-anchor="middle">Neptune</text>
    <line x1="168.2" y1="118.9" x2="168.2" y2="128.9" stroke="currentColor" stroke-width="0.4"/>
    <circle cx="83.2" cy="63.7" r="3" fill="#eea66f" stroke="currentColor" stroke-width="0.5"/>
    <text x="89.2" y="66.7">Parker Solar Probe</text>
    <circle cx="283.3" cy="124.6" r="3" fill="#eea66f" stroke="currentColor" stroke-width="0.5"/>
    <text x="283.3" y="118.6" text-anchor="middle">Voyager 1</text>
    <text x="96.6" y="138.0" text-anchor="middle">bound</text>
    <text x="184.7" y="52.3" text-anchor="middle" fill="#5aa0d8">free</text>
    <text x="274.4" y="157.1" fill="#5aa0d8" text-anchor="middle" transform="rotate(27.4 274.4 157.1)">escape speed</text>
    <text x="274.4" y="180.8" text-anchor="middle" transform="rotate(27.4 274.4 180.8)">circular orbit</text>
    <text x="186.0" y="218" text-anchor="middle">distance from the Sun (AU)</text>
    <text x="12" y="109.0" text-anchor="middle" transform="rotate(-90 12 109.0)">speed (km/s)</text>
    <text x="6" y="12">Bound or free round the Sun</text>
    <text x="6" y="244">Above the blue line, faster than escape speed: free. Below it: bound, on an ellipse.</text>
  </g>
</svg>
</div>

*Figure B. Bound or free round the Sun.*

Two spacecraft show the two sides of the line.

- **Parker Solar Probe**, in December 2024, swept within 6.9 million km of the Sun's centre at 191 km/s, the fastest
  speed of anything ever built. Escape speed at that distance is 196 km/s, so even Parker is bound. It swings back out
  and returns again and again.
- **Voyager 1**, launched on 5 September 1977, is moving away from the Sun at about 17 km/s. In October 2026 it was
  172.5 AU away, where escape speed is only 3.2 km/s. It is free. On 25 August 2012 it became the first spacecraft to
  enter interstellar space. Its speed came largely from swinging past Jupiter and Saturn (chapter 16).

Leaving the Sun from the Earth is easier than 42.1 km/s sounds, because the Earth already carries you at 29.8 km/s.
Launched in the direction the Earth is moving, a spacecraft needs about 12.3 km/s more, once it has climbed out of the
Earth's own well.

??? note "Sources"
    - Parker Solar Probe: closest approach in December 2024 at 9.86 solar radii (6.9 million km) from the Sun's
      centre, 191 km/s, the fastest object ever built: Wikipedia,
      [Parker Solar Probe](https://en.wikipedia.org/wiki/Parker_Solar_Probe) (weaker).
    - Voyager 1: launched on 5 September 1977, about 17 km/s, 172.52 AU as of October 2026, interstellar space on
      25 August 2012: Wikipedia, [Voyager 1](https://en.wikipedia.org/wiki/Voyager_1) (weaker). Its speed from Jupiter
      and Saturn: standard; chapter 16.
    - The 12.3 km/s, $42.1 - 29.8$, and the circular and escape speeds at each distance are our arithmetic, with the
      Sun's $GM$ of $1.32712 \times 10^{11}$ km³/s² (chapter 6).

## 7.6 Speed anywhere on an ellipse { #visviva }

On an ellipse the speed keeps changing. Energy is shared between motion and height, and the total, $-GMm/2a$, stays
the same. Writing that out gives the **vis-viva equation**, "living force" in Latin:

$$v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right),$$

where $r$ is where the body is now and $a$ is the size of its orbit. It contains all the others. On a circle, $r = a$,
and it gives $v^2 = GM/a$. Make the ellipse longer and longer, $a$ very large, and it gives $v^2 = 2GM/r$, escape speed.

**Halley's comet.** With $a = 17.74$ AU, at perihelion, 0.593 AU from the Sun, it moves at 54.3 km/s; at aphelion,
34.9 AU out, at only 0.92 km/s, 59 times slower, as chapter 3 found from the second law. As it crosses the Earth's
distance it moves at 41.5 km/s, just under the escape speed there. Long, thin ellipses are close to the edge.

The physics lesson [The vis-viva equation](https://physics.akadian.ca/topics/gravity/level-7/04-vis-viva.html) works
through the transfer orbit to Mars.

??? note "Sources"
    - The vis-viva equation: Wikipedia, [Vis-viva equation](https://en.wikipedia.org/wiki/Vis-viva_equation)
      (weaker); derived in section 7.9.
    - Halley's semi-major axis (17.737 AU) and eccentricity (0.96658): chapter 3, section 3.2, and its sources. The
      speeds are our arithmetic.

## 7.7 Leaving Mars { #mars }

Mars's escape speed, 5.03 km/s, is less than half the Earth's, and its well is a fifth as deep. That is good news for
any future rocket that has to bring samples or people home. It also means that Mars loses things more easily.

**Rocks.** When a large asteroid hits Mars, some of the rock is thrown off faster than 5 km/s. It goes into orbit round
the Sun, and a few pieces, after millions of years, fall on the Earth. As of September 2020, 277 meteorites had been
identified as Martian, less than half a percent of the 72,000 classified. They have been found or seen to fall all
over the world: at Chassigny in France in 1815, at Sherghati in India in 1865, at El-Nakhla in Egypt in 1911, at Tissint
in Morocco in 2011, and in the Sahara, where "Black Beauty" turned up in 2011 with pieces 4.4 billion years old. One
found by Roberta Score in the Allan Hills of Antarctica on 27 December 1984, ALH84001, was thrown off Mars about
17 million years ago and landed about 13,000 years ago. One clue that these rocks came from Mars was gas trapped inside
one of them, which matched the air of Mars as measured by the Viking landers.

**Air.** In any gas, a few molecules move much faster than the average. High in a planet's air, where collisions are
rare, the fastest of them can exceed the escape speed and fly off into space. Light gases such as hydrogen move faster
than heavy ones at the same temperature, so they leak first; the Earth loses about 3 kg of hydrogen every second. Mars,
with its low escape speed, has lost much more. NASA's MAVEN orbiter studied how the solar wind strips away Mars's air,
and its measurements suggest that two thirds of the argon-36 in the Martian atmosphere has been lost over the last
4 billion years. MAVEN fell silent on 6 December 2025, and in February 2026 a review board judged that it could
probably not be recovered.

??? note "Sources"
    - Escape speed of Mars: NASA, Mars fact sheet (above). The well depths: section 7.3.
    - Martian meteorites thrown off by impacts, 277 classified as Martian out of 72,000 as of September 2020,
      Chassigny (France, 1815), Shergotty (Sherghati, India, 1865), Nakhla (El-Nakhla, Egypt, 1911), Tissint
      (Morocco, 2011), NWA 7034 "Black Beauty" (Sahara, 2011, components 4.42 billion years old), and gases trapped in
      EET79001 matching the Martian atmosphere measured by Viking: Wikipedia,
      [Martian meteorite](https://en.wikipedia.org/wiki/Martian_meteorite) (weaker).
    - ALH84001, found on 27 December 1984 in the Allan Hills of Antarctica by Roberta Score of an ANSMET team, thrown
      off Mars about 17 million years ago and landing about 13,000 years ago: Wikipedia,
      [Allan Hills 84001](https://en.wikipedia.org/wiki/Allan_Hills_84001) (weaker).
    - Molecules in the fast tail of the speed distribution escaping from the exosphere, and heavier molecules moving
      slower: Wikipedia, [Jeans escape](https://en.wikipedia.org/wiki/Jeans_escape) (weaker). Hydrogen escaping more
      easily than carbon dioxide, the Earth losing about 3 kg/s of hydrogen, and MAVEN results on 66% of argon-36 lost
      over 4 billion years: Wikipedia, [Atmospheric escape](https://en.wikipedia.org/wiki/Atmospheric_escape) (weaker).
    - MAVEN studying how the solar wind strips the upper atmosphere, losing contact on 6 December 2025, and the review
      board of February 2026 finding it likely not recoverable: Wikipedia,
      [MAVEN](https://en.wikipedia.org/wiki/MAVEN) (weaker).

## 7.8 Working it out { #working }

Using $GM$ in km³/s² and distances in km gives speeds in km/s and energies in km²/s², which are the same as MJ/kg.

**The space station.** $v = \sqrt{398{,}600 / 6{,}771} = \sqrt{58.87} = 7.67$ km/s. Escape speed at that height is
$7.67 \times 1.414 = 10.85$ km/s.

**Escape from Mars.** $v_\text{esc} = \sqrt{2 \times 42{,}828 / 3{,}389.5} = \sqrt{25.27} = 5.03$ km/s.

**Energy to a low orbit.** From the ground (ignoring spin) to a 400 km orbit round the Earth:
$398{,}600 / 6{,}371 - 398{,}600 / (2 \times 6{,}771) = 62.56 - 29.43 = 33.1$ MJ/kg.

**Halley at the Earth's distance.** $v^2 = 1.32712 \times 10^{11} \times (2 / 1.496 \times 10^8 - 1 / 2.6534 \times
10^9) = 1.32712 \times 10^{11} \times 1.2992 \times 10^{-8} = 1{,}724$, so $v = 41.5$ km/s.

| | Mars | Earth |
| --- | --- | --- |
| Speed of an orbit skimming the surface | 3.55 km/s | 7.91 km/s |
| Escape speed from the surface | 5.03 km/s | 11.19 km/s |
| Depth of the well, $GM/R$ | 12.6 MJ/kg | 62.6 MJ/kg |
| Energy to a low orbit | 6.7 MJ/kg (200 km up) | 33.1 MJ/kg (400 km up) |
| Speed in its stationary orbit | 1.45 km/s | 3.07 km/s |
| Speed round the Sun | 24.1 km/s | 29.8 km/s |
| Escape speed from the Sun at its distance | 34.1 km/s | 42.1 km/s |

??? note "Sources"
    - $GM$ and radii: chapter 6, and NASA fact sheets (above). Stationary orbits: chapter 3, section 3.6. All values
      are our arithmetic.

## 7.9 Where the formulas come from { #derive }

**Escape speed.** Energy is conserved: motion energy plus potential energy stays the same. Starting at the surface with
speed $v$ and just reaching infinity with nothing to spare,

$$\tfrac12 mv^2 - \frac{GMm}{R} = 0 + 0 \qquad\Rightarrow\qquad v = \sqrt{\frac{2GM}{R}}.$$

The mass $m$ cancels: a pebble and a spaceship need the same escape speed.

**Energy on an ellipse.** Per kilogram, at perihelion ($r_p = a(1-e)$, speed $v_p$) and aphelion ($r_a = a(1+e)$,
speed $v_a$), two things are conserved. The second law says $r_p v_p = r_a v_a$, since at the ends of the axis the speed
is at right angles to the radius. Energy says

$$\tfrac12 v_p^2 - \frac{GM}{r_p} = \tfrac12 v_a^2 - \frac{GM}{r_a}.$$

Put $v_a = v_p r_p / r_a$ into it:

$$\tfrac12 v_p^2\left(1 - \frac{r_p^2}{r_a^2}\right) = GM\,\frac{r_a - r_p}{r_p r_a}
\qquad\Rightarrow\qquad v_p^2 = \frac{2GM\,r_a}{r_p\,(r_a + r_p)} = \frac{GM}{a}\cdot\frac{r_a}{r_p},$$

using $r_a + r_p = 2a$. The energy per kilogram is then

$$\tfrac12 v_p^2 - \frac{GM}{r_p} = \frac{GM}{r_p}\left(\frac{r_a}{2a} - 1\right)
= \frac{GM}{r_p}\cdot\frac{r_a - 2a}{2a}
= -\frac{GM}{2a},$$

since $r_a - 2a = -r_p$.

**Vis-viva.** The energy is the same at every point of the orbit, so anywhere

$$\tfrac12 v^2 - \frac{GM}{r} = -\frac{GM}{2a} \qquad\Rightarrow\qquad v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right).$$

??? note "Sources"
    - The derivations are standard; the vis-viva equation and its derivation from conservation of energy and angular
      momentum are given in Wikipedia, Vis-viva equation (above).

## Check yourself { #check }

**1.** (beginner) Which moves faster, a GPS satellite or a geostationary one? Why?

??? note "Answer"
    The GPS satellite, 3.87 km/s against 3.07 km/s. It is closer to the Earth, where the pull is stronger, so it must
    go faster to stay up.

**2.** (beginner) Why is it more accurate to say escape *speed* than escape *velocity*?

??? note "Answer"
    Because the direction does not matter. Any direction that misses the planet needs the same speed.

**3.** (beginner) What had to happen for a rock from Mars to land on the Earth?

??? note "Answer"
    An impact on Mars threw it off faster than Mars's escape speed, 5 km/s. It then went round the Sun, often for
    millions of years, until its orbit crossed the Earth's and it fell.

**4.** (intermediate) The Moon's $GM$ is 4,903 km³/s² and its radius 1,737.4 km. Find its escape speed.

??? note "Answer"
    $\sqrt{2 \times 4{,}903 / 1{,}737.4} = \sqrt{5.644} = 2.38$ km/s.

**5.** (intermediate) Air drag pushes backwards on a satellite. Why does the satellite end up going faster?

??? note "Answer"
    Drag takes away energy, so the satellite sinks into a lower orbit. A lower circular orbit is faster,
    $v = \sqrt{GM/r}$. The potential energy falls by twice as much as the motion energy rises.

**6.** (intermediate) Parker Solar Probe moved at 191 km/s at 6.9 million km from the Sun's centre. Show that it was
still bound to the Sun.

??? note "Answer"
    Escape speed there is $\sqrt{2 \times 1.32712 \times 10^{11} / 6.9 \times 10^6} = \sqrt{38{,}467} = 196$ km/s.
    191 km/s is less, so the probe is bound.

**7.** (advanced) Mars has $a = 1.5237$ AU. Use the vis-viva equation to find its speed at perihelion, 206.65 million km
from the Sun.

??? note "Answer"
    $a = 1.5237 \times 1.496 \times 10^8 = 2.2795 \times 10^8$ km. $v^2 = 1.32712 \times 10^{11} \times (2 / 2.0665
    \times 10^8 - 1 / 2.2795 \times 10^8) = 1.32712 \times 10^{11} \times 5.292 \times 10^{-9} = 702.3$, so
    $v = 26.5$ km/s, as chapter 3 found.

**8.** (expert) Show that for a circular orbit the motion energy equals minus the total energy, and the potential
energy is twice the total. Use this to find how much energy each kilogram of the space station loses when it sinks
from 6,771 km to 6,769 km, and how much faster it goes.

??? note "Answer"
    With $E = -GM/2r$, motion energy $GM/2r = -E$ and potential energy $-GM/r = 2E$. The energy lost is
    $398{,}600/(2 \times 6{,}769) - 398{,}600/(2 \times 6{,}771) = 0.0087$ MJ/kg, 8.7 kJ for each kilogram. The motion
    energy rises by the same 8.7 kJ/kg: the speed goes from $\sqrt{398{,}600/6{,}771} = 7.6726$ to
    $\sqrt{398{,}600/6{,}769} = 7.6737$ km/s, about 1.1 m/s faster.

## Summary

- A circular orbit goes at $\sqrt{GM/r}$: 7.67 km/s for the space station, 29.8 km/s for the Earth round the Sun.
- Drag makes a satellite sink and speed up; to catch something ahead in orbit, you slow down first.
- An orbit's total energy is $-GMm/2a$; reaching low Earth orbit takes more than half the energy of escaping.
- Escape speed is $\sqrt{2GM/R}$, $\sqrt2$ times orbital speed: 11.19 km/s from the Earth, 5.03 km/s from Mars.
- Below escape speed a body is bound on an ellipse; above, it is free. Parker Solar Probe is bound; Voyager 1 is
  leaving.
- The vis-viva equation $v^2 = GM(2/r - 1/a)$ gives the speed anywhere on an orbit.
- Rocks thrown off Mars by impacts have landed all over the Earth, and Mars has lost much of its air to space.

**Next:** chapter 8, Tides, where the Moon and the Sun stretch the Earth, and Mars stretches Phobos towards its end.

## Further reading

- Howard D. Curtis, *Orbital Mechanics for Engineering Students*, fourth edition, Butterworth-Heinemann, 2020.
