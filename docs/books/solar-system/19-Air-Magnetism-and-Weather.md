# 19. Air, magnetism and weather on other worlds

*Each planet and moon in this book has had its own chapter. This one lines them up side by side. It asks how much air
each world has and why, which worlds make a magnetic field and how far out it holds off the solar wind, what the
weather is like from Venus to Neptune, and how a world loses its air to space. Mars runs through all of it: a planet
that once had a strong magnetic field and much thicker air, and now has neither.*

!!! abstract "In this chapter"
    **You will learn:**

    - how much air each world has, from 92 bars on Venus to almost nothing on the Moon and Mercury
    - why air thins as you go up, and what the scale height tells you
    - what a planet needs to make a magnetic field, and which worlds have one
    - how far out each magnetic shield reaches, and why Jupiter's is the biggest thing any planet makes
    - the weather of other worlds: Venus's racing clouds, Mars's dust storms, Titan's methane rain, Neptune's winds
    - the ways a world loses air to space, and how Mars lost most of its own
    - how people in al-Andalus, Italy, France, Russia, Japan and the Emirates found out about the air of other worlds
    - how to work out the size of a magnetic shield by balancing two pushes

    **You need:** chapter 5 for Venus, chapter 6 (section 6.4) for the Earth's magnetic field, chapter 8 for Mars, and
    chapter 18 (section 18.9) for the push of the solar wind. Powers and roots; for 19.9, sixth roots on a calculator.

    **Levels:** 19.1 to 19.3 are beginner; 19.4 to 19.7 are intermediate; 19.8 is advanced; 19.9 is expert.

## 19.1 How much air? { #air }

**From 92 bars to almost nothing.** Air pressure is the weight of the air above you pressing down on each square
metre. At sea level on the Earth it is about 1 bar. Other worlds cover a huge range:

| World | Pressure at the ground | Main gases | Scale height |
|---|---|---|---|
| Venus | 92 bar | carbon dioxide 96.5%, nitrogen 3.5% | 15.9 km |
| Titan | 1.5 bar | nitrogen 94.2%, methane 5.65% | 15 to 50 km |
| Earth | 1.014 bar | nitrogen 78.08%, oxygen 20.95% | 8.5 km |
| Mars | 0.00636 bar | carbon dioxide 95.1%, nitrogen 2.59% | 11.0 km |
| Pluto | about 0.000013 bar | nitrogen 99% | about 18 km |
| Mercury | under 5 × 10⁻¹⁵ bar | a few atoms | |
| Moon | 3 × 10⁻¹⁵ bar at night | a few atoms | |

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Surface air pressure of seven worlds on a scale where each step is a thousand times the last, from a millionth of a billionth of a bar on the left to a thousand bars on the right. Venus has 92 bars, Titan 1.5, the Earth 1.01, Mars 0.0064, Pluto about 13 millionths of a bar, Mercury less than 5 thousand-million-millionths and the Moon about 3 thousand-million-millionths. The thickest air, on Venus, is about 30 million billion times the thinnest, on the Moon.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">How much air: pressure at the ground, in bars</text>
    <line x1="92.0" y1="24.0" x2="92.0" y2="196.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="92.0" y="206.0" text-anchor="middle">10⁻¹⁵</text>
    <line x1="131.0" y1="24.0" x2="131.0" y2="196.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="131.0" y="206.0" text-anchor="middle">10⁻¹²</text>
    <line x1="170.0" y1="24.0" x2="170.0" y2="196.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="170.0" y="206.0" text-anchor="middle">10⁻⁹</text>
    <line x1="209.0" y1="24.0" x2="209.0" y2="196.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="209.0" y="206.0" text-anchor="middle">10⁻⁶</text>
    <line x1="248.0" y1="24.0" x2="248.0" y2="196.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="248.0" y="206.0" text-anchor="middle">0.001</text>
    <line x1="287.0" y1="24.0" x2="287.0" y2="196.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="287.0" y="206.0" text-anchor="middle">1</text>
    <line x1="326.0" y1="24.0" x2="326.0" y2="196.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="326.0" y="206.0" text-anchor="middle">1000</text>
    <text x="86.0" y="39.0" text-anchor="end">Venus</text>
    <rect x="92.0" y="31.0" width="220.5" height="10" fill="#eea66f" opacity="0.85"/>
    <text x="309.5" y="28.0" text-anchor="end">92</text>
    <text x="86.0" y="62.0" text-anchor="end">Titan</text>
    <rect x="92.0" y="54.0" width="197.3" height="10" fill="#cfc8bf" opacity="0.85"/>
    <text x="286.3" y="51.0" text-anchor="end">1.5</text>
    <text x="86.0" y="85.0" text-anchor="end">Earth</text>
    <rect x="92.0" y="77.0" width="195.1" height="10" fill="#5aa0d8" opacity="0.85"/>
    <text x="284.1" y="74.0" text-anchor="end">1.01</text>
    <text x="86.0" y="108.0" text-anchor="end">Mars</text>
    <rect x="92.0" y="100.0" width="166.4" height="10" fill="#c1440e" opacity="0.85"/>
    <text x="255.4" y="97.0" text-anchor="end">0.0064</text>
    <text x="86.0" y="131.0" text-anchor="end">Pluto</text>
    <rect x="92.0" y="123.0" width="131.5" height="10" fill="#cfc8bf" opacity="0.85"/>
    <text x="227.5" y="131.0">0.000013</text>
    <text x="86.0" y="154.0" text-anchor="end">Mercury</text>
    <rect x="92.0" y="146.0" width="9.1" height="10" fill="#555" opacity="0.85"/>
    <text x="105.1" y="154.0">&lt; 5 × 10⁻¹⁵</text>
    <text x="86.0" y="177.0" text-anchor="end">Moon</text>
    <rect x="92.0" y="169.0" width="6.2" height="10" fill="#555" opacity="0.85"/>
    <text x="102.2" y="177.0">3 × 10⁻¹⁵</text>
    <text x="6" y="226">Each grid line is 1,000 times the one to its left. Venus's air presses down 14,000 times as hard as</text>
    <text x="6" y="235">Mars's. The Moon and Mercury have almost none: a few atoms knocked or baked off their rocks.</text>
    <text x="6" y="244">The giant planets have no ground; their air just gets thicker and hotter all the way down.</text>
  </g>
</svg>
</div>

Venus's air presses down about **14,000 times** as hard as Mars's. **Titan**, a moon with only 14% of the Earth's
gravity, has half as much pressure again as the Earth, and its air weighs nearly twice as much as ours (chapter 15,
[section 15.4](15-Moons-of-the-Giants.md#titan)). At the bottom, Mercury's "air" is what NASA calls a surface-bounded
**exosphere**, essentially a vacuum. The giant planets are left out, because they have no ground: their air just gets
thicker and hotter all the way down, far past 1,000 bars (chapter 3,
[section 3.5](03-Rocky-Worlds-and-Giant-Worlds.md#gasgiants)).

**Why so different?** Several things decide how much air a world keeps:

- how much gas it got when it formed, and how much its volcanoes let out since;
- how much has escaped to space, which depends on gravity, heat and the solar wind (section 19.4);
- where the gas went: most of the Earth's carbon dioxide is locked up in limestone and other rocks (chapter 5,
  [section 5.4](05-Venus.md#greenhouse)), and on Mars so much carbon dioxide freezes onto the winter polar cap that
  the pressure swings from 4.0 to 8.7 thousandths of a bar during the year.

**Thinner as you go up.** Climb, and there is less air above you, so the pressure falls. In air at one temperature it
falls by the same fraction for every equal step up. The step that cuts it to $1/e$, about 37%, is the **scale
height** $H$. It is set by the temperature $T$, the mass of one mole of the gas $M$ and the gravity $g$:

$$H = \frac{RT}{Mg}$$

where $R = 8.314$ J per mole per kelvin. Mars's air is colder and heavier than ours, which would make $H$ smaller,
but its gravity is only 38% of ours, so in the end its air is more spread out: 11.0 km against 8.5 km. Titan, with
weak gravity, has scale heights of 15 to 50 km.

??? note "Sources"
    - Pressures, main gases, scale heights and Mars's seasonal 4.0 to 8.7 mb: NASA fact sheets for
      [Venus](https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html),
      [Earth](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html),
      [Mars](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html),
      [Pluto](https://nssdc.gsfc.nasa.gov/planetary/factsheet/plutofact.html),
      [Mercury](https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html) and the
      [Moon](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html). Mercury's "surface bounded exosphere,
      essentially a vacuum": NASA, Mercury fact sheet (above).
    - Titan's 1.5 bar, its 94.2% nitrogen and 5.65% methane, its air's mass of 9.1 × 10¹⁸ kg, nearly twice the
      Earth's, and scale heights of 15 to 50 km: Wikipedia,
      [Atmosphere of Titan](https://en.wikipedia.org/wiki/Atmosphere_of_Titan) (weaker). Titan's 14% gravity: chapter
      15.
    - Carbon dioxide in limestone: chapter 5. Carbon dioxide freezing onto the cap as the reason for the swing:
      standard. The 14,000 times: our arithmetic, $92/0.00636$.
    - The scale height formula: standard; section 19.8 checks it against the fact sheets.

## 19.2 Magnetic shields { #magnetic }

**What makes a field.** A planet makes a magnetic field with a **dynamo**, and a dynamo needs three things: a fluid
that carries electricity, the planet's spin to twist it, and a source of energy inside to keep the fluid moving. In
the Earth the fluid is the liquid iron of the outer core (chapter 6,
[section 6.4](06-The-Earth-as-a-Planet.md#magnetic)). In Jupiter it is thought to be hydrogen squeezed so hard that it
behaves like a liquid metal. In Uranus and Neptune it is probably a shallow layer of water and ammonia that carries
electricity (chapter 14, [section 14.5](14-Uranus-and-Neptune.md#inside)).

Out in space the field makes a bubble, the **magnetosphere**, that holds the solar wind off. Its front, the
**magnetopause**, is where the field's push and the wind's push balance. Here is how strong each field is at the
equator, in millionths of a tesla (µT), and how far out the front sits, in radii of the planet:

| World | Field at the equator | Front of the shield |
|---|---|---|
| Mercury | 0.14 to 0.4 µT | 1.5 radii |
| Earth | 31 µT | 10 radii |
| Mars | under 0.01 µT | no shield of its own |
| Jupiter | 428 µT | 70 radii |
| Ganymede | 0.72 µT | 1.6 radii |
| Saturn | 22 µT | 20 radii |
| Uranus | 23 µT | 18 radii |
| Neptune | 14 µT | 24 radii |

**Jupiter's giant.** Jupiter's field is about 14 times as strong as the Earth's at the cloud tops, and the front of
its shield is 70 Jupiter radii out, about **5 million km**, seven times the radius of the Sun. On the far side the
solar wind stretches the field into a tail that sometimes reaches beyond the orbit of Saturn. Jupiter's shield is
blown up from inside too: the volcanoes of Io throw out sulphur dioxide, which forms a ring of gas round Jupiter that
the field spins round with the planet. If you could see it, the shield would look wider than the full Moon in our sky
(section 19.8).

**Small fields.** **Mercury**'s field was found by Mariner 10 in 1974, and it is only about 1.1% as strong as the
Earth's. Its shield reaches only half a Mercury radius above the ground, about 1,200 km, on the side facing the Sun.
**Ganymede** is the only moon known to make its own field (chapter 15,
[section 15.3](15-Moons-of-the-Giants.md#oceans)), and it has a little magnetosphere inside Jupiter's.

**No field at all.** **Venus** seems to have no dynamo. The solar wind runs straight into its upper air, where
sunlight has knocked electrons off the atoms, and drapes round it; this makes a weak field that is called
**induced**. **Mars** has no dynamo today either, but its oldest crust, in the southern highlands, is still
magnetised: the record of a field that died long ago (section 19.7). The lander InSight measured about 2 µT
at the ground, about ten times what orbiters had suggested for that spot.

??? note "Sources"
    - The three things a dynamo needs: Wikipedia, [Dynamo theory](https://en.wikipedia.org/wiki/Dynamo_theory)
      (weaker). The Earth's core: chapter 6. Jupiter's liquid metallic hydrogen, Io's sulphur dioxide ring spun by the
      field, and the tail beyond Saturn's orbit: Wikipedia,
      [Magnetosphere of Jupiter](https://en.wikipedia.org/wiki/Magnetosphere_of_Jupiter) (weaker). Uranus and Neptune:
      chapter 14.
    - The table, the magnetopause as the balance of pushes, and Venus's induced field: Wikipedia,
      [Magnetosphere](https://en.wikipedia.org/wiki/Magnetosphere) (weaker), whose table is from Kivelson and Bagenal
      in the *Encyclopedia of the Solar System*. The 14 times, the 5 million km ($70 \times 71{,}492$ km) and the
      seven Sun radii: our arithmetic, with Jupiter's radius from NASA,
      [Jupiter fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html), and the Sun's radius,
      695,700 km: standard.
    - Mercury's field found by Mariner 10 in 1974, 1.1% of the Earth's: Wikipedia,
      [Magnetosphere of Mercury](https://en.wikipedia.org/wiki/Magnetosphere_of_Mercury) (weaker). The 1,200 km:
      our arithmetic, $0.5 \times 2{,}440$ km.
    - Ganymede: chapter 15; its own small magnetosphere inside Jupiter's: Wikipedia, Magnetosphere of Jupiter (above).
      The solar wind meeting Venus's charged upper air: standard.
    - Mars's magnetised southern crust and InSight's 2 µT against about 200 nT from orbit: Wikipedia,
      [Magnetic field of Mars](https://en.wikipedia.org/wiki/Magnetic_field_of_Mars) (weaker).

## 19.3 Weather on other worlds { #weather }

**Winds.** Here are the wind speeds NASA lists for each world:

| World | Winds |
|---|---|
| Venus | 0.3 to 1 m/s at the ground, about 100 m/s at the cloud tops |
| Earth | 0 to 100 m/s |
| Mars | 2 to 7 m/s in summer, 17 to 30 m/s in a dust storm (at the Viking landers) |
| Jupiter | up to 150 m/s |
| Saturn | up to 400 m/s |
| Uranus | up to 250 m/s |
| Neptune | up to 580 m/s |

The fastest winds in the solar system blow on **Neptune**, which gets only a nine-hundredth of the sunlight the Earth
gets. On the giants the winds run in bands round the planet, and a storm such as Jupiter's Great Red Spot can last for
well over a century (chapter 12, [section 12.3](12-Jupiter.md#spot)).

**Venus's racing clouds.** Venus turns once in 243 days, but its upper clouds go round the planet in about **4 Earth
days**, at 100 m/s or more. This is called **super-rotation**: the wind moves up to 60 times as fast as the ground
below it, while the Earth's fastest winds are only 10 to 20% of its spin speed (chapter 5,
[section 5.2](05-Venus.md#clouds)). Japan's Akatsuki saw something like a jet stream in the clouds 45 to 60 km up.

**Mars's dust storms.** Mars's winds are not strong by the Earth's standards, and in air so thin they push very
weakly: a 30 m/s gale on Mars pushes like a breeze of about 3 m/s on the Earth (section 19.8). Yet they lift fine
dust, and now and then a storm grows until it covers the planet. Since the 1950s the chance of a planet-wide storm in
any Martian year has been about **one in three**. When Mariner 9 arrived in 1971, it found the whole planet hidden
except the top of Olympus Mons, and the storm lasted a month. A storm that began in late May 2018 covered the planet
by 20 June and cut off the sunlight to the rover Opportunity (chapter 8,
[section 8.5](08-Mars-among-the-Planets.md#water)).

**Snow and rain.** Mars has thin clouds of water ice, and high up even of carbon dioxide ice. On 29 September 2008 the
Phoenix lander saw snow falling from clouds 4.5 km above it; it turned back into vapour before it reached the ground.
On **Titan**, the pressure is high enough for methane to be liquid at the surface as well as a gas in the air, so
methane does what water does here: it makes clouds, falls as rain and fills lakes and seas (chapter 15,
[section 15.4](15-Moons-of-the-Giants.md#titan)).

??? note "Sources"
    - The wind speeds: NASA fact sheets for Venus, Earth, Mars and Jupiter (above), and for
      [Saturn](https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturnfact.html),
      [Uranus](https://nssdc.gsfc.nasa.gov/planetary/factsheet/uranusfact.html) and
      [Neptune](https://nssdc.gsfc.nasa.gov/planetary/factsheet/neptunefact.html). Venus's 100 m/s cloud tops: below.
      The nine-hundredth: our arithmetic, $1/30.07^2$.
    - Super-rotation, 4 days, 100 m/s, 60 times, the Earth's 10 to 20%, and Akatsuki's jet stream at 45 to 60 km:
      Wikipedia, [Atmosphere of Venus](https://en.wikipedia.org/wiki/Atmosphere_of_Venus) (weaker).
    - One in three since the 1950s, Mariner 9 and Olympus Mons, the month-long storm, the 2018 storm covering the
      planet by 20 June, the ice clouds and Phoenix's snow: Wikipedia,
      [Climate of Mars](https://en.wikipedia.org/wiki/Climate_of_Mars) (weaker). Opportunity: chapter 8. The 3 m/s:
      our arithmetic, section 19.8.
    - Liquid methane at Titan's surface pressure: Wikipedia, Atmosphere of Titan (above). Rain, lakes and seas: chapter
      15.

## 19.4 Losing air to space { #loss }

**Ways out.** Every world with air leaks some of it to space. The main ways are:

- **Thermal escape.** High up, where the air is so thin that molecules rarely collide, the fastest ones can reach
  escape speed and fly off. It is named **Jeans escape** after the British astronomer James Jeans, who first
  described it. Light gases go first, because at the same temperature lighter molecules move faster.
- **Charge exchange.** A fast charged atom swaps its charge with a slow neutral one. The slow one, now charged, is
  held by the magnetic field; the fast one, now neutral, is free to escape.
- **Breaking apart.** Sunlight and chemistry split molecules, and the pieces fly apart fast enough to escape.
- **Sputtering.** Fast particles of the solar wind knock atoms right out of the air. This matters most on worlds with
  no magnetic shield.
- **Polar wind.** On a planet with a magnetic shield, the field lines near the poles open out into space, and charged
  atoms can flow out along them.

**How fast.** The Earth loses about **3 kg of hydrogen a second**, mostly by charge exchange, and about 50 g of helium
a second, mostly by the polar wind. Oxygen escapes too, in tiny amounts: in 2017 a Japanese team found a few oxygen
ions on the Moon that had come from the Earth. Mars, measured by MAVEN, loses 160 to 1,800 g of hydrogen a second and
about **1,500 g of oxygen** a second, mostly by molecules breaking apart (1,300 g), with charge exchange (130 g) and
sputtering (80 g). Dust storms carry water high up where sunlight can split it; one study suggests they caused about
10% of Mars's water loss. On Venus, the Venus Express orbiter found that escape went up by a factor of 1.9 when more
storms of solar matter (chapter 18, [section 18.4](18-Where-the-Suns-Wind-Ends.md#storms)) were hitting the planet.

**A shield is not everything.** The Earth, with a strong field, still loses hydrogen through its poles. Venus, with
no field, has kept 92 bars of air. A field mainly blocks sputtering and changes which ways out are open. What matters
as much is how hard the planet holds on: Venus's escape speed is 10.36 km/s and the Earth's 11.19 km/s, but Mars's is
only 5.03 km/s. Heavy carbon dioxide does not get out easily by itself, but sunlight can break it apart, and the solar
wind can strip the pieces from a small world with no shield.

??? note "Sources"
    - The ways out, Jeans as a British astronomer, sputtering being stronger without a magnetosphere, the polar wind
      on magnetised planets, the Earth's 3 kg/s and 50 g/s, the Japanese team in 2017, Mars's rates from MAVEN, and
      Venus Express's factor of 1.9: Wikipedia,
      [Atmospheric escape](https://en.wikipedia.org/wiki/Atmospheric_escape) (weaker). Lighter molecules moving faster:
      standard.
    - Dust storms and 10% of the water loss: Wikipedia, Climate of Mars (above).
    - Escape speeds: NASA fact sheets for Venus, Earth and Mars (above). A field changing which ways out are open, and
      how the pieces are stripped: our reasoning from the escape page.

## 19.5 Who found the air of other worlds { #history }

The compass and the Earth's own field have their history in chapter 6
([section 6.4](06-The-Earth-as-a-Planet.md#magnetic)). This is the story of how people measured air, and then found it
and magnetic fields on other worlds.

**Weighing our own air.**

- **Al-Andalus, 11th century.** A short book, *On twilight*, used how long twilight lasts to measure how thick the
  atmosphere is. It is now firmly credited to **Ibn Muʿādh al-Jayyānī** (989–1079), an Arab mathematician and judge
  from al-Andalus, in what is now Spain. For centuries it was put under Ibn al-Haytham's name, because of a note by
  Gerard of Cremona, who turned it into Latin; the Portuguese mathematician **Pedro Nunes** printed that Latin version
  in 1542.
- **Italy, 1640s.** **Evangelista Torricelli** is usually said to have made the first barometer in 1643, though 1644
  is more likely. The Italian **Gasparo Berti** built a rough water barometer between 1640 and 1644.
- **France, 1648.** **Blaise Pascal** asked **Florin Perier**, Pascal's brother-in-law, who lived near the mountain
  Puy de Dôme, to carry a barometer up it. In September 1648 the mercury stood lower the higher Perier climbed: the
  air thins as you go up, as in section 19.1.

**Air on other worlds.**

- **Russia, 1761.** During the transit of Venus, **Mikhail Lomonosov**, watching from a small observatory near
  home in Saint Petersburg, saw an arc of light round the part of Venus that was off the Sun's disc as it began to
  leave. Lomonosov concluded that Venus has an atmosphere.
- **Titan, 1903 to 1944.** Josep Comas i Solà saw hints of air on Titan, and Gerard Kuiper found
  methane there (chapter 15, [section 15.5](15-Moons-of-the-Giants.md#history)).
- **1962 and 1967.** NASA's Mariner 2 measured Venus's heat in 1962, and the Soviet Venera 4 confirmed in 1967 that
  its air is mostly carbon dioxide.
- **1971.** Mariner 9 reached Mars on 14 November 1971, into the great dust storm. The Soviet Mars 2 and Mars 3
  arrived about two weeks later. On 2 December 1971 the Mars 3 lander made the first soft landing on Mars, but it sent
  back only a grey image with no detail before it fell silent.

**Magnetic fields of other worlds.**

- **1955.** Bernard Burke and Kenneth Franklin heard radio bursts from Jupiter, the first sign of its field (chapter
  12, [section 12.4](12-Jupiter.md#history)).
- **1959 and 1963.** **Thomas Gold** named the magnetosphere in 1959. In 1963 Cahill and Amazeen, using data from
  Explorer 12, found the sudden drop in the field that marks its edge, the magnetopause.
- **1974.** Before Mariner 10 flew past, most people thought Mercury was too small, and too airless, to have a field.
  It did.
- **Mars.** Mars Global Surveyor and MAVEN mapped the magnetised old crust; InSight measured it from the ground.

??? note "Sources"
    - Ibn Muʿādh's dates, Cordova and Jaén, "Arab mathematician, Islamic scholar, and Qadi", *On twilight* and the
      thickness of the atmosphere, the mistaken credit to Ibn al-Haytham, Gerard of Cremona, and Pedro Nunes's 1542
      printing: Wikipedia,
      [Ibn Muʿādh al-Jayyānī](https://en.wikipedia.org/wiki/Ibn_Mu%CA%BFadh_al-Jayyani) (weaker).
    - Torricelli, 1643 or 1644, Berti, Pascal, Perier, the Puy de Dôme and September 1648: Wikipedia,
      [Barometer](https://en.wikipedia.org/wiki/Barometer) (weaker).
    - Lomonosov ("Russian polymath"), 1761, the arc of light and the observatory near the house, Mariner 2 in 1962
      and Venera 4 in 1967: Wikipedia, Atmosphere of Venus (above).
    - Titan: chapter 15. Mariner 9 on 14 November 1971, the dust storm, Mars 2 and Mars 3 two weeks later, and Mars 3's
      landing on 2 December 1971 with only a grey image: Wikipedia, [Mars 3](https://en.wikipedia.org/wiki/Mars_3)
      (weaker).
    - Burke and Franklin: chapter 12. Gold in 1959, and Cahill and Amazeen in 1963 with Explorer 12: Wikipedia,
      Magnetosphere (above). Mercury before 1974: Wikipedia, Magnetosphere of Mercury (above). Mars's crust: Wikipedia,
      Magnetic field of Mars (above).

## 19.6 Measuring air and shields today { #missions }

- **MAVEN** (NASA) went into orbit round Mars on 22 September 2014, the first NASA mission to study Mars's air. It
  measured how fast the solar wind strips gas away (section 19.4) and found the clues in section 19.7 to how much has
  gone. It fell silent on 6 December 2025, and NASA declared the mission over on 3 June 2026.
- **Hope**, the Emirates Mars Mission, was launched on 20 July 2020 on a Japanese rocket from Tanegashima, and
  reached Mars orbit on 9 February 2021. About 200 Emirati scientists and engineers worked on it. It watches Mars's
  weather through the day and the seasons, follows dust storms, and compares the weather in different regions.
- **ESCAPADE**, NASA's twin spacecraft Blue and Gold, were launched on 13 November 2025 and waited a year in a loop
  round the Earth–Sun L2 point, about a million miles (1.6 million km) away, watching space weather. In November 2026
  they swung past the Earth (Blue on 7 November, Gold due on 9 November) and set off on an 11-month trip to Mars, to
  study its magnetosphere and how the solar wind took away its air.
- **Mio**, Japan's Mercury Magnetospheric Orbiter, rides with Europe's orbiter on **BepiColombo**. The pair are due
  in orbit round Mercury on 21 November 2026, Mio is to be set free on 9 or 10 December 2026, and the science is to
  begin in April 2027. Mio will study Mercury's field and its small shield.
- **Akatsuki** (Japan) watched Venus's clouds and winds from 2015 to 2024 (chapter 5,
  [section 5.6](05-Venus.md#missions)), and **Juno** maps Jupiter's field (chapter 12,
  [section 12.6](12-Jupiter.md#missions)).
- **Dragonfly**, NASA's flying lander, is to be launched in July 2028 and reach Titan in 2034, the first aircraft on
  Titan.

??? note "Sources"
    - MAVEN's orbit on 22 September 2014, the first NASA mission to study Mars's air, the loss of contact on 6
      December 2025 and the end declared on 3 June 2026: Wikipedia, [MAVEN](https://en.wikipedia.org/wiki/MAVEN)
      (weaker).
    - Hope's launch on 20 July 2020 from Tanegashima on an H-IIA, Mars orbit on 9 February 2021, the 200 Emirati
      scientists and engineers, and its daily, seasonal and regional weather and dust storms: Wikipedia,
      [Emirates Mars Mission](https://en.wikipedia.org/wiki/Emirates_Mars_Mission) (weaker).
    - ESCAPADE, Blue and Gold, 13 November 2025, the staging orbit round the Earth–Sun L2 point, the flybys on 7 and 9
      November 2026, the 11-month cruise and its aims: Wikipedia, [ESCAPADE](https://en.wikipedia.org/wiki/ESCAPADE)
      (weaker).
    - BepiColombo, Mio, 21 November 2026, 9 to 10 December 2026 and April 2027: Wikipedia,
      [BepiColombo](https://en.wikipedia.org/wiki/BepiColombo) (weaker).
    - Akatsuki and Juno: chapters 5 and 12. Dragonfly's July 2028 launch, 2034 arrival and "first aircraft on Titan":
      Wikipedia, [Dragonfly](https://en.wikipedia.org/wiki/Dragonfly_(Titan_space_probe)) (weaker).

## 19.7 Mars beside Venus, the Earth and Titan { #mars }

| | Mars | Venus | Earth | Titan |
|---|---|---|---|---|
| Pressure at the ground | 0.0064 bar | 92 bar | 1.014 bar | 1.5 bar |
| Main gas | carbon dioxide 95% | carbon dioxide 96.5% | nitrogen 78% | nitrogen 94% |
| Mass of the air | 2.5 × 10¹⁶ kg | 4.8 × 10²⁰ kg | 5.1 × 10¹⁸ kg | 9.1 × 10¹⁸ kg |
| Average temperature | 214 K | 737 K | 288 K | 94 K |
| Gravity | 3.73 m/s² | 8.87 m/s² | 9.82 m/s² | 1.35 m/s² |
| Magnetic field | patches in old crust | none; induced | dynamo, 31 µT | none of its own |

**Mars's lost shield.** About 4 billion years ago Mars had a dynamo and a strong field, about as strong at the ground
as the Earth's is today. The old southern crust, 4.2 to 4.3 billion years old, still holds it. The big impact basins
made about 4.1 to 3.9 billion years ago carry no magnetism, so the dynamo had stopped before they formed, though a weak
one may have come back for a while, up to about 3.8 billion years ago.

**Mars's lost air.** With no shield and weak gravity, Mars lay open to the solar wind and the Sun's ultraviolet.
MAVEN's measurements suggest that about **66%** of Mars's argon-36, a gas that does not freeze or join rocks, has been
lost to space over 4 billion years, and with it **about half a bar or more** of carbon dioxide: about 80 times the air
Mars has now. Flowing water once carved river valleys on Mars (chapter 8,
[section 8.4](08-Mars-among-the-Planets.md#ages)), and in today's thin air it could not stay liquid for long.

**Living with thin air.** Mars's 0.0064 bar is close to the pressure at which liquid water can exist at all, 0.006
bar, so water at the ground tends to freeze or boil away. At the Viking 1 site the air went from 184 K at night to
242 K in the day. The thin air holds little heat, and with no shield, auroras can glow over the whole planet (book 1,
[section 21.7](../night-sky/21-The-Night-Sky-from-Mars.md#aurora)).

**Titan, the odd one.** Titan has no field of its own, and it spends about half of each orbit outside Saturn's shield,
open to the solar wind. Hydrogen escaping from it leaves a ring of gas round Saturn. Yet Titan keeps thicker air than
ours. Our guess at the reason is the cold: at 94 K a typical nitrogen molecule moves at about 240 m/s, less than a
tenth of Titan's escape speed of 2.64 km/s.

??? note "Sources"
    - Pressures, gases, masses of air, temperatures and gravities: NASA fact sheets (above), and for Titan Wikipedia,
      Atmosphere of Titan (above), with 94 K from chapter 15 and the gravity of 1.352 m/s² and escape speed of 2.641
      km/s from Wikipedia, [Titan](https://en.wikipedia.org/wiki/Titan_(moon)) (weaker). Fields: section 19.2.
    - The early dynamo "comparable to Earth's present surface field" 4 billion years ago, the crust of 4.2 to 4.3
      billion years, the basins of about 4.1 to 3.9 billion years and the late dynamo to about 3.8 billion years:
      Wikipedia, Magnetic field of Mars (above).
    - 66% of the argon-36 and 0.5 bar or more of carbon dioxide over 4 billion years: Wikipedia, Atmospheric escape
      (above). Argon not freezing or joining rocks: standard. The 80 times: our arithmetic, $0.5/0.00636 = 79$. The
      river valleys: chapter 8. Liquid water needing more pressure than Mars has now: standard, and below.
    - Water's triple point at 0.006 bar (611.657 Pa): standard. Viking 1's 184 to 242 K: NASA, Mars fact sheet
      (above). Auroras: book 1, chapter 21.
    - Titan half outside Saturn's bow shock and the hydrogen ring: Wikipedia, Atmospheric escape (above). The reason
      Titan keeps its air: our reasoning; the 240 m/s is our arithmetic, $\sqrt{2kT/m}$ for nitrogen at 94 K.

## 19.8 Working it out { #working }

**Mars's scale height.** $H = RT/(Mg) = 8.314 \times 214/(0.04349 \times 3.73) = 10{,}970$ m, 11.0 km, just what NASA
lists. The same sum gives 8.4 km for the Earth (288 K, 0.02897 kg per mole, 9.82 m/s²) and 15.9 km for Venus (737 K,
0.04345, 8.87).

**Up Olympus Mons.** About 22 km is two scale heights, so the pressure on top is $e^{-2} = 0.135$ of that at its
foot. Starting from 6.36 mb, that is about 0.86 mb.

**The mass of Mars's air.** The air's weight is the pressure times the area: $m = p \times 4\pi R^2/g = 636 \times
4\pi \times (3.3895 \times 10^6)^2/3.73 = 2.5 \times 10^{16}$ kg, as NASA lists. That is about a two-hundredth of the
Earth's $5.1 \times 10^{18}$ kg.

**A Martian gale.** The push of a wind on each square metre goes as $\tfrac12 \rho v^2$, where $\rho$ is the density.
On Mars $\rho$ is about 0.016 kg/m³, so a 30 m/s gale pushes with $0.5 \times 0.016 \times 30^2 = 7.2$ pascals. On
the Earth, with 1.217 kg/m³, the same push comes from $v = 30 \times \sqrt{0.016/1.217} = 3.4$ m/s, a light breeze.

**Venus's clouds.** Cloud tops 70 km up go round a circle of radius 6,122 km in 4 days: $2\pi \times 6.122 \times
10^6/(4 \times 86{,}400) = 111$ m/s. The ground at the equator moves at $2\pi \times 6.052 \times 10^6/(243 \times
86{,}400) = 1.8$ m/s. The clouds go about 60 times as fast.

**Mars's oxygen leak.** At 1.5 kg a second for 4 billion years, Mars would lose $1.5 \times 4 \times 10^9 \times 3.156
\times 10^7 = 1.9 \times 10^{17}$ kg of oxygen, about 7.6 times the mass of all its air today. Today's rate need not
hold over all that time, so this is only a rough guide, but it shows how much a small leak can add up to.

**Jupiter's shield in our sky.** The front is $70 \times 71{,}492 = 5.0$ million km from Jupiter, so the shield is at
least 10 million km across. When it is opposite the Sun in our sky, Jupiter is about $5.2 - 1 = 4.2$ AU, 628 million
km, away, so the shield would span $10/628 = 0.016$ radian, 0.91°: nearly twice the width of the full Moon, about
0.5°.

??? note "Sources"
    - Temperatures, molecular masses, gravities, radii, densities and masses of air: NASA fact sheets (above). Olympus
      Mons's 22 km: chapter 8. Venus's radius and spin: NASA, Venus fact sheet (above); cloud tops at 70 km: chapter
      5. MAVEN's 1.5 kg/s: section 19.4. Jupiter's radius: NASA, Jupiter fact sheet (above).
    - The push of a wind, $\tfrac12 \rho v^2$, and the Moon's width of about 0.5°: standard. All the sums: our
      arithmetic.

## 19.9 How big is a magnetic shield? { #derive }

The front of a magnetic shield is where two pushes balance: the solar wind pushing in and the planet's field pushing
out. Each push can be worked out.

**The wind's push.** Section 18.9 found that the solar wind pushes on each square metre with a pressure of about
$1.34 \times 10^{-9}$ pascals at 1 AU, falling as $1/a^2$ at $a$ AU from the Sun:

$$p = \frac{1.34 \times 10^{-9}}{a^2} \text{ Pa}$$

**The field's push.** A magnetic field of strength $B$ pushes like a pressure $B^2/(2\mu_0)$, where $\mu_0 = 4\pi
\times 10^{-7}$ in SI units. Over the planet's magnetic equator, a simple magnet's field falls as the cube of the
distance: if it is $B_0$ at the planet's radius $R$, at distance $r$ it is

$$B = B_0 \left(\frac{R}{r}\right)^3$$

Where the wind presses the field in, currents flow on the front of the shield, and they double the field just inside
it. So the field's push there is $(2B)^2/(2\mu_0) = 2B^2/\mu_0$.

**The balance.** Set the two equal:

$$\frac{2B_0^2}{\mu_0} \left(\frac{R}{r}\right)^6 = p
\quad\Longrightarrow\quad
\frac{r}{R} = \left(\frac{2B_0^2}{\mu_0 \, p}\right)^{1/6}$$

**The Earth.** $B_0 = 0.306$ gauss $= 3.06 \times 10^{-5}$ T, and $p = 1.34 \times 10^{-9}$ Pa. Then $2B_0^2 = 1.87
\times 10^{-9}$, $\mu_0 p = 1.68 \times 10^{-15}$, their ratio is $1.11 \times 10^6$, and its sixth root is **10.2**.
Spacecraft find the front about 10 Earth radii out.

**All six planets.** Using each planet's field from the NASA fact sheets and its distance from the Sun:

| Planet | Field $B_0$ | Distance | Worked out | Measured |
|---|---|---|---|---|
| Mercury | 0.002 gauss | 0.387 AU | 1.4 radii | 1.5 radii |
| Earth | 0.306 gauss | 1 AU | 10.2 | 10 |
| Jupiter | 4.30 gauss | 5.2 AU | 43 | 70 |
| Saturn | 0.215 gauss | 9.54 AU | 19 | 20 |
| Uranus | 0.228 gauss | 19.19 AU | 25 | 18 |
| Neptune | 0.142 gauss | 30.07 AU | 25 | 24 |

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="For six planets, how far the front of the magnetic shield sits from the planet's centre, in planet radii. Open circles are the answers from balancing the solar wind's push against the push of the planet's field, filled circles are measured. Mercury: 1.4 worked out, 1.5 measured. Earth: 10.2 and 10. Jupiter: 43 and 70. Saturn: 19 and 20. Uranus: 25 and 18. Neptune: 25 and 24. Four agree well; Jupiter's is much bigger because gas from its moon Io blows it up, and Uranus's field is tilted and off-centre.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">How far out the shield holds the wind (planet radii)</text>
    <line x1="92.0" y1="24.0" x2="92.0" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="92.0" y="200.0" text-anchor="middle">0</text>
    <line x1="122.1" y1="24.0" x2="122.1" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="122.1" y="200.0" text-anchor="middle">10</text>
    <line x1="152.3" y1="24.0" x2="152.3" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="152.3" y="200.0" text-anchor="middle">20</text>
    <line x1="182.4" y1="24.0" x2="182.4" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="182.4" y="200.0" text-anchor="middle">30</text>
    <line x1="212.5" y1="24.0" x2="212.5" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="212.5" y="200.0" text-anchor="middle">40</text>
    <line x1="242.7" y1="24.0" x2="242.7" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="242.7" y="200.0" text-anchor="middle">50</text>
    <line x1="272.8" y1="24.0" x2="272.8" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="272.8" y="200.0" text-anchor="middle">60</text>
    <line x1="302.9" y1="24.0" x2="302.9" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="302.9" y="200.0" text-anchor="middle">70</text>
    <text x="86.0" y="43.0" text-anchor="end">Mercury</text>
    <line x1="96.2" y1="40.0" x2="96.5" y2="40.0" stroke="#555" stroke-width="0.8"/>
    <circle cx="96.2" cy="40.0" r="3.4" fill="none" stroke="#eea66f" stroke-width="1.5"/>
    <circle cx="96.5" cy="40.0" r="3" fill="#5aa0d8"/>
    <text x="103.5" y="43.0">1.4 / 1.5</text>
    <text x="86.0" y="70.0" text-anchor="end">Earth</text>
    <line x1="122.7" y1="67.0" x2="122.1" y2="67.0" stroke="#555" stroke-width="0.8"/>
    <circle cx="122.7" cy="67.0" r="3.4" fill="none" stroke="#eea66f" stroke-width="1.5"/>
    <circle cx="122.1" cy="67.0" r="3" fill="#5aa0d8"/>
    <text x="129.7" y="70.0">10.2 / 10</text>
    <text x="86.0" y="97.0" text-anchor="end">Jupiter</text>
    <line x1="220.2" y1="94.0" x2="302.9" y2="94.0" stroke="#555" stroke-width="0.8"/>
    <circle cx="220.2" cy="94.0" r="3.4" fill="none" stroke="#eea66f" stroke-width="1.5"/>
    <circle cx="302.9" cy="94.0" r="3" fill="#5aa0d8"/>
    <text x="214.2" y="97.0" text-anchor="end">43 / 70</text>
    <text x="86.0" y="124.0" text-anchor="end">Saturn</text>
    <line x1="149.8" y1="121.0" x2="152.3" y2="121.0" stroke="#555" stroke-width="0.8"/>
    <circle cx="149.8" cy="121.0" r="3.4" fill="none" stroke="#eea66f" stroke-width="1.5"/>
    <circle cx="152.3" cy="121.0" r="3" fill="#5aa0d8"/>
    <text x="159.3" y="124.0">19 / 20</text>
    <text x="86.0" y="151.0" text-anchor="end">Uranus</text>
    <line x1="166.4" y1="148.0" x2="146.2" y2="148.0" stroke="#555" stroke-width="0.8"/>
    <circle cx="166.4" cy="148.0" r="3.4" fill="none" stroke="#eea66f" stroke-width="1.5"/>
    <circle cx="146.2" cy="148.0" r="3" fill="#5aa0d8"/>
    <text x="173.4" y="151.0">25 / 18</text>
    <text x="86.0" y="178.0" text-anchor="end">Neptune</text>
    <line x1="165.8" y1="175.0" x2="164.3" y2="175.0" stroke="#555" stroke-width="0.8"/>
    <circle cx="165.8" cy="175.0" r="3.4" fill="none" stroke="#eea66f" stroke-width="1.5"/>
    <circle cx="164.3" cy="175.0" r="3" fill="#5aa0d8"/>
    <text x="172.8" y="178.0">25 / 24</text>
    <circle cx="98.0" cy="209.0" r="3.4" fill="none" stroke="#eea66f" stroke-width="1.5"/>
    <text x="105.0" y="212.0">worked out (section 19.9)</text>
    <circle cx="220.0" cy="209.0" r="3" fill="#5aa0d8"/>
    <text x="227.0" y="212.0">measured</text>
    <text x="6" y="226">Worked out from each planet's field and the solar wind's push at its distance; measured values</text>
    <text x="6" y="235">from spacecraft. Jupiter's shield is puffed up by gas from Io, spun round by the planet; Uranus's</text>
    <text x="6" y="244">field is tipped 59° and set off-centre, so a simple magnet is a poor guide there.</text>
  </g>
</svg>
</div>

Four of the six agree well. **Jupiter**'s shield is much bigger than the sum says, because Jupiter is not a simple
magnet in an empty bubble: the gas from Io, spun round by the field, stretches it into a flat disc that pushes the
front out. **Uranus**'s field is tilted 59° and set off-centre, so a simple magnet is a poor guide there.

**A stiff shield.** Because of the sixth root, the shield hardly moves when the wind changes. If the wind pushes 8
times as hard as usual, the front comes in only by $8^{1/6} = 1.41$, from 10.2 to 7.2 Earth radii. To
push it in to 6.6 Earth radii, where satellites in geostationary orbit circle, takes $(10.2/6.6)^6 = 13$ times the
usual push. To halve it would take $2^6 = 64$ times.

**What the size depends on.** Since $(r/R)^6$ goes as $B_0^2/p$, and $p$ goes as $1/a^2$, the shield's size in
planet radii goes as $B_0^{1/3} a^{1/3}$: a planet twice as far from the Sun gets a shield $2^{1/3} = 1.26$ times
bigger, all else the same.

??? note "Sources"
    - The wind's push: chapter 18, section 18.9. Magnetic pressure $B^2/(2\mu_0)$, the cube law for a simple magnet,
      and the doubling of the field at the front: standard. Wikipedia's Magnetosphere page (above) gives the same
      formula without the doubling, which makes every answer 11% smaller ($2^{-1/6} = 0.89$).
    - The fields: NASA fact sheets for Mercury, Earth, Jupiter, Saturn, Uranus and Neptune (above), where the "dipole
      field strength" is in gauss times the planet's radius cubed. The distances: the same fact sheets. The measured
      sizes: Wikipedia, Magnetosphere (above).
    - Io's gas stretching Jupiter's field into a disc: Wikipedia, Magnetosphere of Jupiter (above). Uranus's 59° and
      the off-centre field: chapter 14. Geostationary orbit at 42,164 km, 6.6 Earth radii: standard.
    - All the sums: our arithmetic.

## Check yourself { #check }

**1.** (beginner) Put Venus, Titan, the Earth and Mars in order of the air pressure at the ground, thickest first.

??? note "Answer"
    Venus (92 bar), Titan (1.5 bar), the Earth (1.014 bar), Mars (0.0064 bar).

**2.** (beginner) What three things does a planet need to make a magnetic field? Name two rocky planets that have no
dynamo today.

??? note "Answer"
    A fluid that carries electricity, spin, and a source of energy inside to keep the fluid moving. Venus and Mars have
    no dynamo today.

**3.** (beginner) Why can a 30 m/s wind on Mars not knock you over, when a 30 m/s wind on the Earth is a storm?

??? note "Answer"
    Mars's air is about 76 times thinner, so the same wind pushes about 76 times less hard. A 30 m/s gale on Mars
    pushes like a breeze of about 3.4 m/s on the Earth.

**4.** (intermediate) Mars's scale height is 11 km. What fraction of the pressure at its foot would you expect at the
top of Olympus Mons, about 22 km higher?

??? note "Answer"
    22 km is two scale heights, so the pressure falls to $e^{-2} = 0.135$, about an eighth: about 0.86 mb if it is
    6.36 mb at the foot.

**5.** (intermediate) Name three ways a world's air escapes to space, and say which one a magnetic field weakens most.

??? note "Answer"
    Any three of: thermal (Jeans) escape, charge exchange, molecules breaking apart, sputtering, and the polar wind. A
    magnetic field mainly shuts off sputtering, by keeping the solar wind away from the air. (It also opens the polar
    wind, which only planets with a field have.)

**6.** (intermediate) Venus has no magnetic field but has kept 92 bars of air, while Mars has lost most of its air.
Give two reasons why a field is not the whole story.

??? note "Answer"
    Gravity: Venus's escape speed is 10.36 km/s, Mars's only 5.03 km/s, so gas finds it much harder to leave Venus.
    And the Earth, with a strong field, still loses hydrogen through the polar wind; a field changes which ways out
    are open rather than closing them all. (Mars also lost its field early, and its air was smaller to begin with.)

**7.** (advanced) Suppose the solar wind pushes 8 times as hard as usual. Where is the front of the Earth's
shield? Are satellites in geostationary orbit, 6.6 Earth radii out, still inside?

??? note "Answer"
    The front moves in by $8^{1/6} = 1.41$, from 10.2 to 7.2 Earth radii. That is still outside 6.6, so they are
    just inside the shield. It would take about 13 times the usual push to reach them.

**8.** (expert) Using the balance of section 19.9, show that a shield's size in planet radii goes as $B_0^{1/3}$.
How strong would Mercury's field have to be to hold the wind off at 10 Mercury radii, like the Earth's?

??? note "Answer"
    $(r/R)^6 = 2B_0^2/(\mu_0 p)$, so $r/R$ goes as $(B_0^2)^{1/6} = B_0^{1/3}$. To go from 1.39 to 10 radii, $B_0$
    must grow by $(10/1.39)^3 = 372$ times, to about $0.002 \times 372 = 0.74$ gauss: more than twice the Earth's
    0.306. Mercury needs a stronger field than ours because the solar wind pushes about 7 times as hard so close to
    the Sun.

## Summary

- Air pressure at the ground ranges from 92 bars on Venus through 1.5 on Titan, 1.014 on the Earth and 0.0064 on
  Mars to almost nothing on Mercury and the Moon.
- Air thins with height by the same fraction for each scale height, $H = RT/(Mg)$: 8.5 km on the Earth, 11 km on Mars.
- A dynamo needs a fluid that carries electricity, spin and an energy source. Mercury, the Earth, Ganymede and the
  four giants have one; Venus and Mars do not.
- The front of a magnetic shield ranges from 1.5 radii for Mercury and 10 for the Earth to 70 for Jupiter, whose
  shield is puffed up by gas from Io.
- Venus's clouds race round in 4 days, Mars has planet-wide dust storms about one year in three, Titan has methane
  rain, and Neptune has the fastest winds, up to 580 m/s.
- Air escapes by thermal escape, charge exchange, molecules breaking apart, sputtering and the polar wind; a shield
  blocks some of these, but gravity matters as much.
- Mars lost its dynamo about 4 billion years ago, and since then about 66% of its argon-36 and half a bar or more of
  carbon dioxide have gone to space.
- The shield's front is where the field's push balances the wind's; the sixth root in the answer makes shields stiff.

**Next:** chapter 20, Water and the search for life, where we follow water through the solar system, from Mars's dry
river valleys to the oceans under the ice of the giants' moons, and ask where life could be.

## Further reading

- F. W. Taylor, *Planetary Atmospheres*, Oxford University Press, Oxford, 2010. An Oxford physicist explains the air
  of the planets by comparing each one with the Earth's: its heat, clouds, winds and climate.
