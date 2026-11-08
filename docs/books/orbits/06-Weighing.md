# 6. Weighing the Sun, the planets and their moons

*Nobody has ever put the Sun on a scale, yet we know its mass to better than one part in ten thousand. The trick is
Newton's version of Kepler's third law: anything in orbit carries a record of the mass it goes round. This chapter
weighs the Sun, the planets and their moons from their orbits, follows the long effort to weigh the Earth itself, from
a volcano in the Andes to a shed in England, and finds out what the masses tell us about what these worlds are made
of.*

!!! abstract "In this chapter"
    **You will learn:**

    - how the size and period of an orbit give the mass of the body in the middle
    - how the Earth was weighed, with mountains and then with lead balls in a shed
    - why the constant $G$ is the hardest number in physics to pin down, and why astronomers work around it
    - how worlds with no moons, and small moons themselves, are weighed by spacecraft
    - how the wobble of a star gives the mass of a planet going round it
    - what density tells us about what a world is made of
    - how Mars, Phobos and Deimos have been weighed
    - how a twisting wire measures $G$

    **You need:** chapter 5.

    **Levels:** 6.1 and 6.2 are beginner; 6.3 to 6.7 are intermediate; 6.8 is advanced; 6.9 is expert.

## 6.1 Orbits weigh what they go round { #gm }

Chapter 5 gave Newton's form of the third law. Turned round, it reads

$$G\,(M + m) = \frac{4\pi^2 a^3}{P^2}.$$

Measure the size $a$ and period $P$ of any orbit, and you have $G(M + m)$, the pull of the pair. When the orbiting body
is much lighter, as a planet is beside the Sun, that is simply $GM$ for the body in the middle. Divide by $G$ and you
have its mass in kilograms.

| Weighed | Using the orbit of | Distance (km) | Period | $GM$ worked out (km³/s²) | Mass (kg) |
| --- | --- | --- | --- | --- | --- |
| the Sun | the Earth | 149,598,000 | 365.256 days | $1.327 \times 10^{11}$ | $1.989 \times 10^{30}$ |
| the Earth and Moon together | the Moon | 384,400 | 27.32 days | $4.02 \times 10^{5}$ | $6.03 \times 10^{24}$ |
| Mars | Phobos | 9,378 | 7.65 hours | 42,890 | $6.43 \times 10^{23}$ |
| Jupiter | Callisto | 1,882,700 | 16.69 days | $1.267 \times 10^{8}$ | $1.898 \times 10^{27}$ |
| Saturn | Titan | 1,221,900 | 15.95 days | $3.795 \times 10^{7}$ | $5.69 \times 10^{26}$ |
| Pluto and Charon together | Charon | 19,596 | 6.387 days | 975 | $1.46 \times 10^{22}$ |

Each of these is within 0.3% of NASA's figures, and most are far closer. The Sun comes out at 333,000 times the mass of
the Earth. The physics lesson
[Weighing planets](https://physics.akadian.ca/topics/gravity/level-6/06-weighing-planets.html) works through Mars in
detail.

??? note "Sources"
    - Orbits of the Moon, Callisto, Titan and Charon: NASA JPL,
      [planetary satellite mean elements](https://ssd.jpl.nasa.gov/sats/elem/) (Moon 384,400 km and 27.322 days;
      Callisto 1,882,700 km and 16.690440 days; Titan 1,221,900 km and 15.945448 days). Charon at 19,596 km and
      6.3872 days, Phobos at 9,378 km and 0.31891 days: NASA fact sheets for
      [Pluto](https://nssdc.gsfc.nasa.gov/planetary/factsheet/plutofact.html) and
      [Mars](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - NASA's masses and $GM$ values for comparison: fact sheets for the
      [Sun](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html),
      [Moon](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html),
      [Jupiter](https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html),
      [Saturn](https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturnfact.html), Mars and Pluto (above).
    - The worked values are our arithmetic, with $G = 6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻². The Moon's 0.3% gap is the
      Sun's pull, explained in chapter 5, section 5.9.

## 6.2 Weighing the Earth { #earth }

There is one catch. Orbits give $GM$, and to get $M$ you need $G$. To find $G$ you must measure the pull between two
masses that you have weighed in the ordinary way, and gravity between ordinary things is extremely weak. Newton
himself only guessed that the Earth's average density "might be five or six times as great as the density of water".

**A volcano in the Andes, 1738.** The French astronomers Pierre Bouguer and Charles Marie de La Condamine were near the
equator, in what is now Ecuador, to measure the length of a degree of latitude. They tried to see whether the
6,268 m volcano Chimborazo pulled a plumb line, a weight on a string, a little to one side. The effect was too small
for a clear result, but Bouguer argued that it did at least prove the Earth was not a hollow shell, as some, Edmond
Halley among them, had suggested.

**A Scottish mountain, 1774.** The Astronomer Royal, Nevil Maskelyne, chose Schiehallion in Perthshire, an isolated and
almost symmetrical mountain, and measured how much it pulled plumb lines on its north and south sides: 11.6 seconds of
arc in all. The mathematician Charles Hutton worked out the mountain's volume, drawing lines of equal height on the
map to do it, the **contour lines** now found on every hiking map. He concluded that the Earth's density was about
4,500 kg/m³, less than 20% from the true value.

**A shed in England, 1797–98.** The cleanest answer came from Henry Cavendish, using an apparatus designed by the
geologist John Michell before 1783. A 1.8 m wooden rod, with a small lead ball at each end, hung from a thin wire. Two
large lead balls of 158 kg were brought close to the small ones, and their pull twisted the wire.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Cavendish's torsion balance, seen from above. A wooden rod 1.8 metres long hangs at its middle from a thin wire. A small lead ball of 0.73 kilograms is fixed at each end. Two large lead balls of 158 kilograms stand nearby, one beside each small ball but on opposite sides, so both pull the rod round the same way. The pull twists the wire through a small angle, drawn here much larger than the real 0.16 degrees. Cavendish watched the rod through telescopes from outside the shed.">
  <g font-size="8" fill="currentColor">
    <line x1="70" y1="112" x2="270" y2="112" stroke="#555" stroke-width="1" stroke-dasharray="3 2"/>
    <line x1="70.7" y1="99.8" x2="269.3" y2="124.2" stroke="currentColor" stroke-width="2"/>
    <circle cx="70.7" cy="99.8" r="5" fill="#555"/>
    <circle cx="269.3" cy="124.2" r="5" fill="#555"/>
    <circle cx="74" cy="76" r="22" fill="#cfc8bf" stroke="#555" stroke-width="0.8"/>
    <circle cx="266" cy="148" r="22" fill="#cfc8bf" stroke="#555" stroke-width="0.8"/>
    <circle cx="170" cy="112" r="3" fill="#c1440e"/>
    <text x="170" y="104" text-anchor="middle">wire (seen from above)</text>
    <path d="M124,112 A46,46 0 0 1 124.3,106.4" fill="none" stroke="#c1440e" stroke-width="0.9"/>
    <path d="M216,112 A46,46 0 0 1 215.7,117.6" fill="none" stroke="#c1440e" stroke-width="0.9"/>
    <text x="136" y="126" fill="#c1440e" text-anchor="middle">twist</text>
    <text x="74" y="48" text-anchor="middle">large ball, 158 kg</text>
    <text x="266" y="182" text-anchor="middle">large ball, 158 kg</text>
    <text x="40" y="128" text-anchor="middle">small ball, 0.73 kg</text>
    <text x="300" y="102" text-anchor="middle">small ball, 0.73 kg</text>
    <line x1="70" y1="142" x2="200" y2="142" stroke="currentColor" stroke-width="0.5"/>
    <text x="135" y="152" text-anchor="middle">rod, 1.8 m end to end</text>
    <text x="6" y="12">Weighing the world in a shed</text>
    <text x="6" y="226">Seen from above. Each large ball pulls the small ball beside it, and the wire twists. The twist,</text>
    <text x="6" y="235">about 0.16°, is drawn here far larger. The pull on each small ball was about 1.7 × 10⁻⁷ N,</text>
    <text x="6" y="244">the weight of less than a fiftieth of a milligram.</text>
  </g>
</svg>
</div>

*Figure A. Cavendish's torsion balance.*

The pull on each small ball was about $1.74 \times 10^{-7}$ N, the weight of 0.0177 milligrams. Cavendish shut the
apparatus in a closed shed to keep out draughts and changes of temperature, and watched it through telescopes set in
holes in the wall. The rod turned by only about 0.16°, which he measured to better than 0.25 mm. He found the Earth's
density to be 5.448 times that of water. (An arithmetic slip, found in 1821 by Francis Baily, put 5.480 in his paper.)
The modern value is 5.513. In his letters he called the experiment "weighing the world".

??? note "Sources"
    - Newton's guess of five or six times the density of water, and Bouguer's view that Chimborazo at least proved the
      Earth was not hollow, as Halley had suggested: Wikipedia,
      [Gravitational constant](https://en.wikipedia.org/wiki/Gravitational_constant) (weaker).
    - Bouguer and La Condamine at Chimborazo (6,268 m) in 1738, then in the Viceroyalty of Peru and now in Ecuador,
      on an expedition to measure a degree of latitude near the equator; Schiehallion chosen for its isolation and
      symmetry; Maskelyne, Hutton and the summer of 1774; the 11.6″; Hutton's contour lines; his density of
      4,500 kg/m³, less than 20% from the modern 5,515: Wikipedia,
      [Schiehallion experiment](https://en.wikipedia.org/wiki/Schiehallion_experiment) (weaker).
    - Cavendish's experiment of 1797–1798, Michell's design before 1783, the 1.8 m rod, 0.73 kg and 158 kg balls, the
      force of $1.74 \times 10^{-7}$ N (0.0177 mg), the closed shed and telescopes, the deflection of about 0.16°, the
      0.25 mm accuracy, the density 5.448, Baily's correction of 1821, and "weighing the world": Wikipedia,
      [Cavendish experiment](https://en.wikipedia.org/wiki/Cavendish_experiment) (weaker).
    - The modern mean density of the Earth, 5,513 kg/m³: NASA, Mars fact sheet (Earth column, above).

## 6.3 The hardest number in physics { #g }

Today's best value of the constant is

$$G = 6.67430 \times 10^{-11} \text{ m}^3\,\text{kg}^{-1}\,\text{s}^{-2},$$

with an uncertainty of 2.2 parts in 100,000, about 1 in 45,000. That sounds precise, but most constants of physics are
known thousands of times better. Gravity is so weak that the pull of a laboratory mass is easily swamped by vibration,
temperature changes and the pull of everything else nearby.

Orbits, on the other hand, can be measured superbly well. The Sun's $GM$ is known to about 1 part in 13 billion:
$1.32712440042 \times 10^{20}$ m³/s². So astronomers and spacecraft engineers work with $GM$ directly, and never need
$G$ on its own to fly a mission. A mass in kilograms is only as good as $G$; a $GM$ is as good as the orbit.

??? note "Sources"
    - $G = 6.67430(15) \times 10^{-11}$ m³ kg⁻¹ s⁻², relative standard uncertainty $2.2 \times 10^{-5}$, and $G$ being
      difficult to measure with high accuracy: Wikipedia, Gravitational constant (above).
    - The Sun's $GM$, $(1.32712440042 \pm 0.0000000001) \times 10^{20}$ m³/s², and orbits being measured with great
      precision while $G$ is not: Wikipedia,
      [Standard gravitational parameter](https://en.wikipedia.org/wiki/Standard_gravitational_parameter) (weaker).
    - 1 in 45,000 and 1 in 13 billion are our arithmetic.

## 6.4 Weighing without a moon { #nomoon }

Mercury and Venus have no moons, so for centuries their masses could only be guessed from their small pulls on other
planets. Spacecraft changed that. A probe flying past a planet, or going round it, is bent by its gravity exactly as a
moon would be, and tracking its radio signal shows how much. The MESSENGER spacecraft did this at Mercury, and the
Voyager probes at the outer planets.

**Pluto.** Between 1931 and 1948, faulty calculations gave Pluto far too much mass. Only in 1978, when Charon was found,
could Pluto be weighed properly for the first time: about 0.2% of the Earth's mass, much too small to have disturbed
the orbit of Uranus, which was why people had searched for it in the first place. Even then, the orbit gave the mass of
Pluto and Charon together (section 6.1); splitting it between them needs the barycentre (chapter 5,
[section 5.6](05-Newtons-Law-of-Gravity.md#barycentre)).

**A moon for an asteroid.** On 28 August 1993 the Galileo spacecraft, on its way to Jupiter, flew past the asteroid
Ida, about 31 km across. Months later, on 17 February 1994, Ann Harch of the mission team spotted in the images a tiny
moon, 1.2 to 1.6 km across, now called **Dactyl**. Ida was the first asteroid found to have a moon. Dactyl's orbit could
not be fixed exactly, but the only orbits that would last showed that Ida's density is less than 3,200 kg/m³, too low
for much metal inside.

??? note "Sources"
    - Masses of moonless planets once estimated from their pulls on other planets: standard.
    - Masses from the influence on spacecraft, including the Voyager probes at the outer planets and MESSENGER at
      Mercury, and the flawed calculations of Pluto's mass in 1931–1948: Wikipedia,
      [Planetary mass](https://en.wikipedia.org/wiki/Planetary_mass) (weaker).
    - Charon's discovery in 1978 allowing Pluto's mass to be measured for the first time, about 0.2% of the Earth's,
      far too small to explain the discrepancies in Uranus's orbit: Wikipedia,
      [Pluto](https://en.wikipedia.org/wiki/Pluto) (weaker).
    - Galileo at Ida on 28 August 1993, Ida's mean diameter of 31.4 km, its being the first asteroid found to have a
      natural satellite, the density limit of 3.2 g/cm³ from the stability of Dactyl's orbit, and Ida being depleted of
      metallic minerals: Wikipedia, [243 Ida](https://en.wikipedia.org/wiki/243_Ida) (weaker).
    - Dactyl's discovery by Ann Harch on 17 February 1994 in delayed image downloads, and its size of
      1,200 × 1,400 × 1,600 m: Wikipedia, [Dactyl (moon)](https://en.wikipedia.org/wiki/Dactyl_(moon)) (weaker).

## 6.5 Weighing by the wobble { #wobble }

Chapter 5 showed that the Sun goes round the balance point it shares with Jupiter. The two move in step on opposite
sides of that point, so their speeds are in the ratio of their masses, heavier body slower:

$$\frac{m_\text{planet}}{M_\text{star}} = \frac{v_\text{star}}{v_\text{planet}}.$$

Jupiter moves at 13.06 km/s and makes the Sun move at about 12.5 m/s, so Jupiter has about $12.5 / 13{,}060$, roughly
1/1,000, of the Sun's mass. The Earth makes the Sun move at only about 0.1 m/s.

That is how many planets round other stars have been weighed. Their stars' speeds towards and away from us are
measured from the Doppler shift of their light (book 2,
[section 8.6](../light-and-telescopes/08-The-Doppler-Shift.md#planets)). The planet's speed follows from its period
and the star's mass, by the third law. One thing is lost: we usually do not know how the orbit is tilted to our line of
sight, and only the part of the wobble along that line shows up. So the method gives a **minimum mass**. The first
planet found round a star like the Sun, 51 Pegasi b in 1995, moves at 136 km/s and has a minimum mass about half
Jupiter's.

??? note "Sources"
    - Jupiter changing the Sun's velocity by about 12.4 m/s over about 12 years and the Earth by only 0.1 m/s:
      Wikipedia, [Doppler spectroscopy](https://en.wikipedia.org/wiki/Doppler_spectroscopy) (weaker). Our 12.5 m/s is
      from chapter 5, section 5.6.
    - Jupiter's orbital speed, 13.06 km/s: NASA, Jupiter fact sheet (above).
    - 51 Pegasi b, discovered in 1995, the first exoplanet found round a main-sequence star, its orbital speed of
      136 km/s and minimum mass about half Jupiter's: Wikipedia,
      [51 Pegasi b](https://en.wikipedia.org/wiki/51_Pegasi_b) (weaker).
    - The ratio of speeds, and the tilt giving only a minimum mass: standard.

## 6.6 What the masses tell us { #density }

A mass on its own says little. Divide it by the volume, which comes from the size, and you get the **density**, and
that says what a world is made of.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Densities of bodies weighed by their orbits, in kilograms per cubic metre, as horizontal bars. Rock and iron: the Earth 5,513, Mars 3,934, the Moon 3,344. Rubble: the asteroid Ida less than 3,200, Phobos 1,853. Ice and rock: Pluto 1,854, Charon 1,700. Gas: the Sun 1,408, Jupiter 1,326, Saturn 687, less dense than water, which is 1,000, marked by a dashed line.">
  <g font-size="8" fill="currentColor">
    <rect x="70" y="26" width="198.5" height="11" fill="#c1440e" stroke="#c1440e" stroke-width="0.6"/>
    <text x="66" y="34" text-anchor="end">Earth</text>
    <text x="272.5" y="34">5,513</text>
    <rect x="70" y="43" width="141.6" height="11" fill="#c1440e" stroke="#c1440e" stroke-width="0.6"/>
    <text x="66" y="51" text-anchor="end">Mars</text>
    <text x="215.6" y="51">3,934</text>
    <rect x="70" y="60" width="120.4" height="11" fill="#c1440e" stroke="#c1440e" stroke-width="0.6"/>
    <text x="66" y="68" text-anchor="end">the Moon</text>
    <text x="194.4" y="68">3,344</text>
    <rect x="70" y="77" width="115.2" height="11" fill="#cfc8bf" stroke="#cfc8bf" stroke-width="0.6" stroke-dasharray="3 2" fill-opacity="0.35"/>
    <text x="66" y="85" text-anchor="end">Ida</text>
    <text x="189.2" y="85">less than 3,200</text>
    <rect x="70" y="94" width="66.7" height="11" fill="#5aa0d8" stroke="#5aa0d8" stroke-width="0.6"/>
    <text x="66" y="102" text-anchor="end">Pluto</text>
    <text x="140.7" y="102">1,854</text>
    <rect x="70" y="111" width="66.7" height="11" fill="#cfc8bf" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="66" y="119" text-anchor="end">Phobos</text>
    <text x="140.7" y="119">1,853</text>
    <rect x="70" y="128" width="61.2" height="11" fill="#5aa0d8" stroke="#5aa0d8" stroke-width="0.6"/>
    <text x="66" y="136" text-anchor="end">Charon</text>
    <text x="135.2" y="136">1,700</text>
    <rect x="70" y="145" width="50.7" height="11" fill="#eea66f" stroke="#eea66f" stroke-width="0.6"/>
    <text x="66" y="153" text-anchor="end">Sun</text>
    <text x="124.7" y="153">1,408</text>
    <rect x="70" y="162" width="47.7" height="11" fill="#eea66f" stroke="#eea66f" stroke-width="0.6"/>
    <text x="66" y="170" text-anchor="end">Jupiter</text>
    <text x="121.7" y="170">1,326</text>
    <rect x="70" y="179" width="24.7" height="11" fill="#eea66f" stroke="#eea66f" stroke-width="0.6"/>
    <text x="66" y="187" text-anchor="end">Saturn</text>
    <text x="110.0" y="187">687</text>
    <line x1="106.0" y1="20" x2="106.0" y2="199" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 2"/>
    <text x="106.0" y="208" text-anchor="middle">water</text>
    <line x1="70.0" y1="199" x2="70.0" y2="202" stroke="#555" stroke-width="0.6"/>
    <line x1="142.0" y1="199" x2="142.0" y2="202" stroke="#555" stroke-width="0.6"/>
    <text x="142.0" y="210" text-anchor="middle">2,000</text>
    <line x1="214.0" y1="199" x2="214.0" y2="202" stroke="#555" stroke-width="0.6"/>
    <text x="214.0" y="210" text-anchor="middle">4,000</text>
    <line x1="286.0" y1="199" x2="286.0" y2="202" stroke="#555" stroke-width="0.6"/>
    <text x="286.0" y="210" text-anchor="middle">6,000</text>
    <line x1="70" y1="199" x2="286" y2="199" stroke="#555" stroke-width="0.6"/>
    <text x="6" y="12">How dense? Mass from orbits, divided by volume (kg/m³)</text>
    <rect x="6" y="222" width="8" height="8" fill="#c1440e"/>
    <text x="17" y="229">rock and iron</text>
    <rect x="85.6" y="222" width="8" height="8" fill="#5aa0d8"/>
    <text x="96.6" y="229">ice and rock</text>
    <rect x="161.0" y="222" width="8" height="8" fill="#cfc8bf"/>
    <text x="172.0" y="229">rubble</text>
    <rect x="211.2" y="222" width="8" height="8" fill="#eea66f"/>
    <text x="222.2" y="229">gas</text>
    <text x="6" y="243">Ida's bar is an upper limit, from the orbit of its little moon Dactyl.</text>
  </g>
</svg>
</div>

*Figure B. Densities from weighing.*

- **Rock and iron.** The Earth, at 5,513 kg/m³, is much denser than the rocks at its surface, which are mostly between
  2,500 and 3,000. It must have something heavier inside: an iron core. Mars, at 3,934, and the Moon, at 3,344, have
  less of it.
- **Ice and rock.** Pluto and Charon, around 1,700 to 1,850, must be a mixture of rock and ice.
- **Gas.** The Sun, Jupiter and Saturn are mostly hydrogen and helium. Saturn, at 687, is less dense than water.
- **Rubble.** Phobos, at 1,853, is too light to be solid rock. Measurements suggest that between a quarter and a
  third of it is empty space: it may be a pile of loose rubble held together by a thin crust.

??? note "Sources"
    - Densities of the Earth, Mars, the Moon, Pluto, Charon, the Sun, Jupiter and Saturn: NASA fact sheets (above).
      Ida: section 6.4.
    - Phobos's density, 1.853 g/cm³, its porosity of 30% ± 5%, "a quarter to a third being empty", and its possibly
      being a rubble pile held together by a thin crust: Wikipedia,
      [Phobos (moon)](https://en.wikipedia.org/wiki/Phobos_(moon)) (weaker).
    - Surface rocks of 2,500 to 3,000 kg/m³, the Earth's iron core, the Moon's small share of iron, rock and ice in
      Pluto and Charon, and hydrogen and helium in the Sun and the giant planets: standard.

## 6.7 Weighing Mars and its moons { #mars }

**Mars.** Once Asaph Hall found Phobos and Deimos in 1877 (history book,
[section 17.5](../history/17-Herschel-and-the-Canals-of-Mars.md#moons)), Mars could be weighed from their orbits.
Phobos gives a $GM$ of 42,890 km³/s² and Deimos 42,840, both very close to the modern 42,828. Phobos is a little off
because it is so close to Mars that the planet's bulge at the equator pulls on it extra. Today the orbiters tracked
from the Earth (chapter 5, [section 5.7](05-Newtons-Law-of-Gravity.md#mars)) give Mars's $GM$ to far more digits,
along with a map of how its gravity changes from place to place.

**The moons.** A moon's own mass is much harder to find: something has to pass close by and feel its pull. The
European Space Agency's Mars Express made a flyby of Phobos on 5 March 2010 planned to measure its gravity. In 2026 a
team of researchers, using the tracking of two Mars Express flybys, gave Phobos's $GM$ as 709,962 m³/s², a mass of
$1.0637 \times 10^{16}$ kg, about one sixty-millionth of Mars. Deimos, at about $2.4 \times 10^{15}$ kg, is lighter
still.

Mars Express has also passed messages for China's Zhurong rover, and is planned to do the same for Japan's Martian
Moons eXploration mission, which aims to bring a sample of Phobos back to the Earth.

??? note "Sources"
    - Asaph Hall's discovery of the moons in August 1877: the history book, chapter 17, section 17.5.
    - Mars's $GM$, 42,828 km³/s², and Deimos's mass, $2.4 \times 10^{15}$ kg: NASA, Mars fact sheet (above). Phobos's
      orbit pulled by Mars's bulge: standard; the physics lesson Weighing planets (above) notes it.
    - The flyby of Phobos on 5 March 2010 to measure its gravity, Mars Express relaying for China's Zhurong rover, and
      plans to relay for Japan's Martian Moons eXploration sample return: Wikipedia,
      [Mars Express](https://en.wikipedia.org/wiki/Mars_Express) (weaker).
    - Phobos's mass $1.0637 \times 10^{16}$ kg from $GM = 709{,}962$ m³/s², from Xi Guo, Jianguo Yan and others,
      "Phobos' degree-1 ellipsoidal harmonic gravity field recovery from two Mars Express flybys", *Monthly Notices of
      the Royal Astronomical Society*, 11 April 2026, as cited by Wikipedia, Phobos (moon) (above).

## 6.8 Working it out { #working }

**The Sun from the Earth's orbit.** With $a = 1.49598 \times 10^{11}$ m and $P = 365.256$ days
$= 3.15581 \times 10^{7}$ s,

$$GM = \frac{4\pi^2 a^3}{P^2} = \frac{39.478 \times 3.3479 \times 10^{33}}{9.9592 \times 10^{14}} = 1.3271 \times
10^{20} \text{ m}^3/\text{s}^2,$$

and $M = 1.3271 \times 10^{20} / 6.674 \times 10^{-11} = 1.989 \times 10^{30}$ kg.

**Mars from Deimos.** With $a = 2.3459 \times 10^{7}$ m and $P = 1.26244$ days $= 109{,}075$ s,

$$GM = \frac{39.478 \times 1.2910 \times 10^{22}}{1.1897 \times 10^{10}}
= 4.284 \times 10^{13} \text{ m}^3/\text{s}^2,$$

so Mars's mass is $4.284 \times 10^{13} / 6.674 \times 10^{-11} = 6.42 \times 10^{23}$ kg.

**The Earth from its own gravity.** $M = gR^2 / G = 9.82 \times (6.371 \times 10^6)^2 / 6.674 \times 10^{-11} =
5.97 \times 10^{24}$ kg. Its volume is $\tfrac43\pi R^3 = 1.083 \times 10^{21}$ m³, so its density is 5,514 kg/m³.

| | Mars | Earth |
| --- | --- | --- |
| $GM$ | 42,828 km³/s² | 398,600 km³/s² |
| Mass | $6.42 \times 10^{23}$ kg | $5.97 \times 10^{24}$ kg |
| Mean density | 3,934 kg/m³ | 5,513 kg/m³ |
| Radius of the core | about 1,830 km | about 3,485 km |
| $GM$ measured from | Phobos, Deimos and orbiting spacecraft | the Moon and satellites |
| Mass of its moons, as a fraction of the planet | 1/49 million | 1/81 |

??? note "Sources"
    - Masses, $GM$, densities and core radii: NASA, Mars fact sheet (above), which gives the Earth's values beside
      Mars's. Phobos and Deimos masses: section 6.7. The rest is our arithmetic.

## 6.9 How a twisting wire weighs the Earth { #torsion }

Here is the physics behind Figure A. Let the rod have length $L$, a small ball of mass $m$ at each end, and a large
ball of mass $M$ a distance $r$ from each small ball.

**The twist.** Each large ball pulls its small ball with $F = GMm/r^2$, at a lever arm of $L/2$ from the wire. The two
pulls together make a turning effect, a torque, of $2F \cdot \tfrac{L}{2} = GMmL/r^2$. The wire resists twisting with a
torque $\kappa\theta$, where $\theta$ is the angle turned and $\kappa$ is the wire's stiffness. At balance,

$$\kappa\theta = \frac{GMmL}{r^2}.$$

**The stiffness.** Nobody can measure $\kappa$ directly, but it can be timed. Let the rod swing freely to and fro; a
twisting pendulum has period $T = 2\pi\sqrt{I/\kappa}$, where $I = 2m(L/2)^2 = mL^2/2$ is how hard the rod is to turn,
leaving out the rod itself. So

$$\kappa = \frac{4\pi^2 I}{T^2} = \frac{2\pi^2 m L^2}{T^2}.$$

**Put together.** Substituting,

$$\frac{2\pi^2 m L^2}{T^2}\,\theta = \frac{GMmL}{r^2}
\qquad\Rightarrow\qquad G = \frac{2\pi^2 L\, r^2\, \theta}{M\,T^2}.$$

The small mass $m$ cancels. Everything left is a length, an angle, a time or the mass of the large ball, all things
that can be measured on the Earth.

**From $G$ to the Earth.** At the surface $g = GM_E / R^2$ and $M_E = \tfrac43\pi R^3\rho$, so $g = \tfrac43\pi G\rho R$
and

$$G = \frac{3g}{4\pi R\rho}.$$

Cavendish's density, $\rho = 5{,}448$ kg/m³, with $g = 9.80$ m/s² and $R = 6{,}371$ km, gives
$G = 6.74 \times 10^{-11}$, only 1% from the modern value. Hutton's 4,500 would have given $8.16 \times 10^{-11}$.

??? note "Sources"
    - The torque $\kappa\theta$, timing the swing to find $\kappa$, $I = mL^2/2$ for point masses, the formula
      $G = 2\pi^2 L r^2 \theta / (M T^2)$, and $G = 3g / (4\pi R \rho)$, and Cavendish's
      density giving $G = 6.74 \times 10^{-11}$, 1% from the CODATA 2014 value: Wikipedia, Cavendish experiment
      (above). Hutton's value is our arithmetic.

## Check yourself { #check }

**1.** (beginner) Nobody can put Mars on a scale. What is measured instead to find its mass?

??? note "Answer"
    The size and period of an orbit round it, of a moon such as Phobos or of a spacecraft. Together they give $GM$,
    and dividing by $G$ gives the mass.

**2.** (beginner) What did Cavendish actually measure, and why did he call it "weighing the world"?

??? note "Answer"
    He measured the tiny pull between large and small lead balls. Comparing it with the Earth's pull on the same balls
    gave the Earth's density, and with its size, the Earth's mass.

**3.** (beginner) Saturn's average density is 687 kg/m³. What does that mean, compared with water?

??? note "Answer"
    Saturn is less dense than water, 1,000 kg/m³. On average a cubic metre of Saturn has less mass than a cubic metre
    of water.

**4.** (intermediate) MAVEN goes round Mars on an orbit with $a = 6{,}565$ km and a period of 4.49 hours. Weigh Mars.

??? note "Answer"
    $P = 4.49 \times 3{,}600 = 16{,}164$ s. $GM = 4\pi^2 \times (6.565 \times 10^6)^3 / 16{,}164^2 = 4.27 \times
    10^{13}$ m³/s², and $M = 4.27 \times 10^{13} / 6.674 \times 10^{-11} = 6.40 \times 10^{23}$ kg, within 0.2% of the
    true value; the period was rounded.

**5.** (intermediate) Why do spacecraft engineers work with $GM$ and not with the mass $M$?

??? note "Answer"
    Orbits give $GM$ directly and very precisely: the Sun's to about 1 part in 13 billion. $G$ is known only to about
    1 part in 45,000, so dividing by it makes $M$ much less certain. The motion of a spacecraft depends only on $GM$.

**6.** (intermediate) Jupiter moves at 13.06 km/s and makes the Sun move at 12.5 m/s. Roughly what fraction of the
Sun's mass is Jupiter?

??? note "Answer"
    $12.5 / 13{,}060 = 1/1{,}045$, close to the true 1/1,048.

**7.** (advanced) Phobos's $GM$ is 709,962 m³/s² and its volume is 5,740 km³. Find its mass and density.

??? note "Answer"
    $M = 709{,}962 / 6.6743 \times 10^{-11} = 1.064 \times 10^{16}$ kg. The volume is $5.740 \times 10^{12}$ m³, so the
    density is $1.064 \times 10^{16} / 5.740 \times 10^{12} = 1{,}853$ kg/m³.

**8.** (expert) Charon goes round Pluto at 19,596 km every 6.3872 days, and the barycentre is 2,126 km from Pluto's
centre. Find the masses of Pluto and of Charon.

??? note "Answer"
    The orbit gives $G(M_P + M_C) = 4\pi^2 \times (1.9596 \times 10^7)^3 / (551{,}854)^2 = 9.755 \times 10^{11}$ m³/s²,
    so $M_P + M_C = 1.462 \times 10^{22}$ kg. The barycentre is a fraction $M_C / (M_P + M_C) = 2{,}126 / 19{,}596 =
    0.1085$ of the way from Pluto to Charon. So $M_C = 0.1085 \times 1.462 \times 10^{22} = 1.59 \times 10^{21}$ kg and
    $M_P = 1.30 \times 10^{22}$ kg, matching NASA's values.

## Summary

- An orbit's size and period give $G(M + m)$, the pull of the pair; that weighs the Sun, the planets and their moons.
- The Earth was weighed against mountains, Chimborazo in 1738 and Schiehallion in 1774, and then with Cavendish's
  torsion balance in 1797–98, which gave its density as 5.448 times water's.
- $G$ is known only to about 1 part in 45,000, while orbits give $GM$ far more precisely, so astronomers use $GM$.
- Worlds without moons, and small moons themselves, are weighed by the spacecraft that pass them.
- A star's wobble gives the mass of its planet, or at least a minimum mass.
- Density shows what a world is made of: rock and iron, ice and rock, gas, or rubble.
- Mars was weighed with Phobos and Deimos; Phobos itself has been weighed by Mars Express flybys, and is about a
  third empty space.

**Next:** chapter 7, Orbital speed, energy and escape, where we find how fast an orbit goes, what it costs to climb
higher, and how fast you must go to leave a planet for good.

## Further reading

- Edwin Danson, *Weighing the World: The Quest to Measure the Earth*, Oxford University Press, 2006.
