# 16. Gravity assists

*A spacecraft that flies close past a planet can come away faster or slower than it arrived, and pointing in a new
direction, without burning any fuel. This trick, the gravity assist or slingshot, took the Voyagers to the outer
planets, sends probes inwards to Mercury and the Sun, and is being used at the Earth and Mars right now. This chapter
explains how a planet can give speed away, who worked it out, how much each planet can give, and why Mars, small as it
is, has become a popular place to swing past.*

!!! abstract "In this chapter"
    **You will learn:**

    - how a flyby can change a spacecraft's speed without breaking any law of physics
    - who worked out the idea, from Kondratyuk and Zander to Minovitch and Flandro
    - how the Voyagers used Jupiter and Saturn to reach Uranus and Neptune
    - why heavy planets give more, and why a flyby can never give more than twice the approach speed
    - how flybys of Venus and Mercury let spacecraft fall in towards the Sun
    - how spacecraft come back to swing past the Earth
    - why so many missions now swing past Mars, and what a Mars cycler is
    - how to work out the turn and the speed change of a flyby

    **You need:** chapters 7 and 15.

    **Levels:** 16.1 to 16.3 are beginner; 16.4 to 16.7 are intermediate; 16.8 is advanced; 16.9 is expert.

## 16.1 Something for nothing? { #idea }

Throw a tennis ball at 30 km/h at the front of a train coming towards you at 50 km/h. The driver sees the ball coming
at 80 km/h, and after a perfect bounce, going away at 80 km/h. But the train is still moving, so you see the ball go
off at 80 + 50 = **130 km/h**. The ball has picked up twice the train's speed.

A planet does the same thing to a spacecraft, without touching it. Figure A shows both points of view.

- **Seen from the planet**, the spacecraft falls in, swings round and climbs out again. Gravity gives back on the way
  out exactly the speed it gave on the way in, so the spacecraft leaves **as fast as it came**. Only its direction has
  changed.
- **Seen from the Sun**, the planet is itself moving, at tens of kilometres a second. Add the planet's speed to the
  spacecraft's speed past the planet, before and after. The turned arrow now points more along the planet's path, so
  the total is bigger.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Two views of one flyby. On the left, seen from the planet, the spacecraft comes in from below going straight up, swings round the back of the planet, and leaves turned 60 degrees towards the right. Its arrows in and out are the same length: seen from the planet it leaves exactly as fast as it came. On the right, seen from the Sun, the planet's own speed is drawn as a long arrow to the right, and the spacecraft's speed past the planet is added to its tip, once before and once after the turn. The arrow for after the flyby is clearly longer than the one for before, so seen from the Sun the spacecraft has sped up.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">One flyby, two points of view</text>
    <text x="10" y="28">Seen from the planet</text>
    <text x="186" y="28">Seen from the Sun</text>
    <circle cx="95" cy="120" r="8" fill="#c1440e" fill-opacity="0.8"/>
    <text x="109" y="123" fill="#c1440e">planet</text>
    <path d="M74.0,182.2 L74.2,178.0 L74.3,174.2 L74.4,170.8 L74.5,167.7 L74.6,165.0 L74.7,162.4 L74.8,160.1 L74.9,157.9 L75.0,155.9 L75.1,154.1 L75.2,152.4 L75.3,150.8 L75.4,149.3 L75.5,147.9 L75.6,146.6 L75.7,145.4 L75.8,144.2 L75.9,143.1 L76.0,142.0 L76.1,141.0 L76.2,140.1 L76.3,139.2 L76.4,138.3 L76.5,137.5 L76.6,136.7 L76.8,135.9 L76.9,135.2 L77.0,134.5 L77.1,133.8 L77.2,133.2 L77.3,132.6 L77.4,132.0 L77.5,131.4 L77.6,130.8 L77.7,130.3 L77.8,129.8 L77.9,129.2 L78.0,128.7 L78.1,128.3 L78.2,127.8 L78.3,127.3 L78.4,126.9 L78.5,126.5 L78.6,126.0 L78.7,125.6 L78.8,125.2 L78.9,124.8 L79.0,124.5 L79.1,124.1 L79.2,123.7 L79.3,123.3 L79.4,123.0 L79.5,122.7 L79.6,122.3 L79.7,122.0 L79.8,121.7 L79.9,121.3 L80.0,121.0 L80.1,120.7 L80.2,120.4 L80.3,120.1 L80.4,119.8 L80.6,119.5 L80.7,119.2 L80.8,118.9 L80.9,118.7 L81.0,118.4 L81.1,118.1 L81.2,117.8 L81.3,117.6 L81.5,117.3 L81.6,117.0 L81.7,116.8 L81.8,116.5 L81.9,116.3 L82.0,116.0 L82.2,115.8 L82.3,115.5 L82.4,115.3 L82.5,115.0 L82.7,114.8 L82.8,114.5 L82.9,114.3 L83.0,114.1 L83.2,113.8 L83.3,113.6 L83.4,113.4 L83.6,113.1 L83.7,112.9 L83.9,112.7 L84.0,112.4 L84.1,112.2 L84.3,112.0 L84.4,111.7 L84.6,111.5 L84.7,111.3 L84.9,111.0 L85.0,110.8 L85.2,110.6 L85.4,110.3 L85.5,110.1 L85.7,109.9 L85.8,109.7 L86.0,109.4 L86.2,109.2 L86.4,109.0 L86.5,108.7 L86.7,108.5 L86.9,108.2 L87.1,108.0 L87.3,107.8 L87.5,107.5 L87.7,107.3 L87.9,107.0 L88.1,106.8 L88.3,106.5 L88.5,106.3 L88.8,106.0 L89.0,105.8 L89.2,105.5 L89.5,105.3 L89.7,105.0 L90.0,104.7 L90.2,104.5 L90.5,104.2 L90.8,103.9 L91.1,103.6 L91.3,103.3 L91.6,103.1 L91.9,102.8 L92.3,102.5 L92.6,102.2 L92.9,101.8 L93.2,101.5 L93.6,101.2 L94.0,100.9 L94.3,100.5 L94.7,100.2 L95.1,99.8 L95.6,99.5 L96.0,99.1 L96.4,98.7 L96.9,98.3 L97.4,97.9 L97.9,97.5 L98.4,97.1 L99.0,96.7 L99.6,96.2 L100.2,95.7 L100.8,95.3 L101.5,94.8 L102.2,94.2 L102.9,93.7 L103.7,93.1 L104.5,92.5 L105.3,91.9 L106.2,91.3 L107.2,90.6 L108.2,89.9 L109.3,89.1 L110.5,88.3 L111.7,87.5 L113.0,86.6 L114.4,85.6 L116.0,84.6 L117.6,83.5 L119.4,82.4 L121.4,81.1 L123.6,79.7 L125.9,78.2 L128.5,76.6 L131.4,74.8 L134.6,72.8 L138.2,70.6 L142.3,68.1 L146.9,65.2 L152.3,62.0 L158.5,58.2 L165.9,53.8" fill="none" stroke="#5aa0d8" stroke-width="1.3"/>
    <defs><marker id="o16ah" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="currentColor"/></marker></defs>
    <line x1="74.0" y1="182.2" x2="74.0" y2="152.2" stroke="currentColor" stroke-width="1" marker-end="url(#o16ah)"/>
    <text x="78.0" y="174.2">in</text>
    <line x1="139.9" y1="68.8" x2="165.9" y2="53.8" stroke="currentColor" stroke-width="1" marker-end="url(#o16ah)"/>
    <text x="145.9" y="45.8" text-anchor="end">out</text>
    <text x="10" y="200">Same speed out as in.</text>
    <text x="10" y="209">Only the direction turns.</text>
    <line x1="186.0" y1="175.0" x2="266.0" y2="175.0" stroke="currentColor" stroke-width="1.1" marker-end="url(#o16ah)"/>
    <text x="188" y="186">the planet's speed round the Sun</text>
    <path d="M266.0,125.0 L268.6,125.1 L271.2,125.3 L273.8,125.6 L276.4,126.1 L278.9,126.7 L281.5,127.4 L283.9,128.3 L286.3,129.3 L288.7,130.4 L291.0,131.7 L293.2,133.1 L295.4,134.5 L297.5,136.1 L299.5,137.8 L301.4,139.6 L303.2,141.5 L304.9,143.5 L306.5,145.6 L307.9,147.8 L309.3,150.0" fill="none" stroke="#555" stroke-width="0.5" stroke-dasharray="2 2"/>
    <line x1="266.0" y1="175.0" x2="266.0" y2="125.0" stroke="#555" stroke-width="0.8" marker-end="url(#o16ah)"/>
    <line x1="266.0" y1="175.0" x2="309.3" y2="150.0" stroke="#555" stroke-width="0.8" marker-end="url(#o16ah)"/>
    <text x="263.0" y="147.0" text-anchor="end" fill="#555">in</text>
    <text x="295.3" y="174.0" fill="#555">out</text>
    <line x1="186.0" y1="175.0" x2="266.0" y2="125.0" stroke="#5aa0d8" stroke-width="1.4" marker-end="url(#o16ah)"/>
    <line x1="186.0" y1="175.0" x2="309.3" y2="150.0" stroke="#c1440e" stroke-width="1.4" marker-end="url(#o16ah)"/>
    <text x="200.0" y="141.0" fill="#5aa0d8">before</text>
    <text x="313.3" y="153.0" fill="#c1440e">after</text>
    <text x="6" y="226">Left: the planet sees the spacecraft arrive and leave at the same speed. Right: add the</text>
    <text x="6" y="235">planet's own motion to both. The turned arrow now points more along the planet's path, so the</text>
    <text x="6" y="244">"after" arrow is longer: seen from the Sun, the spacecraft has sped up, here by a third.</text>
  </g>
</svg>
</div>

Nothing is free. The spacecraft's gain is the planet's loss: the planet is pulled back very slightly. But a planet is
so heavy that the change is far too small ever to notice. If an 800 kg spacecraft gains 10 km/s at Jupiter, Jupiter
slows by about 4 × 10⁻²¹ m/s.

Pass **in front of** the planet instead of behind it, and the turn goes the other way: the spacecraft comes away
**slower**, seen from the Sun. Both are useful.

??? note "Sources"
    - The train and tennis ball, 30 and 50 km/h, 80 and 130 km/h, and the planet's frame and the Sun's frame:
      Wikipedia, [Gravity assist](https://en.wikipedia.org/wiki/Gravity_assist) (weaker).
    - The planet's loss: momentum is shared, standard. Jupiter's mass of 1.898 × 10²⁷ kg: NASA,
      [Jupiter Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html). The 4 × 10⁻²¹ m/s is our
      arithmetic, $800 \times 10{,}000 / 1.898 \times 10^{27}$.
    - Passing ahead of or behind the planet to lose or gain speed: standard, and the same Wikipedia article.

## 16.2 Who worked it out { #history }

The idea grew in several countries over forty years.

- **Yuri Kondratyuk**, born Aleksandr Shargei in 1897 in Poltava, then in the Russian Empire and now in Ukraine, wrote
  in 1918–1919 that a spacecraft travelling between two planets could be sped up at the start and the end by the pull
  of the two planets' moons. His notes, *To Those Who Will Be Reading in Order to Build*, were published in 1938, and
  the part on gravity assists only in the 1960s. He also
  worked out how to land on the Moon by leaving the main ship in orbit, the plan that Apollo later used.
- **Friedrich Zander**, born in Riga in 1887 into a Baltic German family, a Russian and Soviet pioneer of rocketry,
  showed a deep understanding of gravity assists in a paper on interplanetary flight in 1925.
- **Gaetano Crocco**, an Italian scientist and the founder of the Italian Rocket Society, was nearly 80 when in 1956 he
  worked out a one-year trip from the Earth past Mars and Venus and home again, using several flybys. This is the
  Crocco grand tour of chapter 15.
- **The first use** was in 1959. The Soviet probe **Luna 3** swung round the Moon on 6 October, passing about
  6,200 km from it, took the first photographs of the Moon's far side, and headed back towards the Earth to send them.
- **Michael Minovitch**, an American mathematician, worked out a general method in 1961 as a graduate student at UCLA
  working summers at NASA's Jet Propulsion Laboratory. He used the IBM 7090, the fastest computer of the day, to solve
  the paths of a spacecraft, the Sun and a planet together.

??? note "Sources"
    - Kondratyuk's paper, published in 1938 but dated 1918–1919, the use of the two planets' moons, and the gravity
      assist part unpublished until the 1960s:
      Wikipedia, Gravity assist (above). Born Aleksandr Ignatyevich Shargei in 1897 in Poltava, Russian Empire (now
      Ukraine), died February 1942; lunar orbit rendezvous later adopted by Apollo: Wikipedia,
      [Yuri Kondratyuk](https://en.wikipedia.org/wiki/Yuri_Kondratyuk) (weaker).
    - Zander's 1925 paper: Wikipedia, Gravity assist (above). Born in Riga in 1887 into a Baltic German family, "a
      Russian and Soviet pioneer of rocketry and spaceflight": Wikipedia,
      [Friedrich Zander](https://en.wikipedia.org/wiki/Friedrich_Zander) (weaker).
    - Crocco, "an Italian scientist and aeronautics pioneer", founder of the Italian Rocket Society, his 1956
      "One-Year Exploration-Trip Earth-Mars-Venus-Earth", nearly 80 years old: Wikipedia,
      [Gaetano Crocco](https://en.wikipedia.org/wiki/Gaetano_Crocco) (weaker). Multiple gravity assists in 1956:
      Wikipedia, Gravity assist (above).
    - Luna 3: first gravity assist in 1959, the first photographs of the far side, closest approach about 6,200 km on
      6 October 1959: Wikipedia, [Luna 3](https://en.wikipedia.org/wiki/Luna_3) (weaker).
    - Minovitch: American mathematician, a UCLA graduate student working summers at JPL, 1961, the IBM 7090:
      Wikipedia, [Michael Minovitch](https://en.wikipedia.org/wiki/Michael_Minovitch) (weaker), and Gravity assist
      (above).

## 16.3 The Grand Tour { #tour }

In 1964 **Gary Flandro**, a summer student at the Jet Propulsion Laboratory, was asked to look at paths to the outer
planets. He noticed that in the late 1970s Jupiter, Saturn, Uranus and Neptune would be lined up so that one
spacecraft could swing from each to the next. The line-up comes only once every **175 years**, and the best launch
year was 1977. He called it the **Grand Tour**.

NASA launched **Voyager 2** on 20 August 1977 and **Voyager 1** on 5 September. Voyager 2 took the full tour:

| Planet | Voyager 2 flew past in |
| --- | --- |
| Jupiter | 1979 |
| Saturn | 1981 |
| Uranus | January 1986 |
| Neptune | August 1989 |

It is still the only spacecraft to have visited Uranus or Neptune. On the cheapest path with no flybys, a trip to
Neptune would have taken about 31 years; Voyager 2 took 12. Each flyby both bent its path towards the next planet and
sped it up, until it was going fast enough to leave the solar system for ever. Voyager 1, after Jupiter and Saturn, is
now moving away from the Sun at about **17 km/s**, faster than any other spacecraft.

??? note "Sources"
    - Flandro in 1964 as a summer student at JPL, the Grand Tour, the alignment every 175 years and 1977 as the best
      launch year: Wikipedia, [Gary Flandro](https://en.wikipedia.org/wiki/Gary_Flandro) (weaker).
    - Voyager 2 launched on 20 August 1977; Jupiter in 1979, Saturn in 1981, Uranus on 24 January 1986, Neptune on
      25 August 1989; the only spacecraft to visit the ice giants; reaching solar escape speed: Wikipedia,
      [Voyager 2](https://en.wikipedia.org/wiki/Voyager_2) (weaker). Voyager 1 launched on 5 September 1977 and moving
      at about 17 km/s, the fastest of any spacecraft away from the Sun: Wikipedia,
      [Voyager 1](https://en.wikipedia.org/wiki/Voyager_1) (weaker).
    - About 31 years: a Hohmann path to Neptune at 30.1 AU takes $\tfrac12 (15.55)^{1.5} = 30.7$ years; our
      arithmetic. Neptune's distance: NASA,
      [Neptune Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/neptunefact.html).

## 16.4 How much can a planet give? { #turn }

A flyby turns the spacecraft's path round the planet. Two things set how far:

- **How heavy the planet is.** A heavier planet pulls harder and bends the path more.
- **How close and how fast the spacecraft passes.** A slow, close pass bends a lot; a fast, distant pass hardly bends
  at all.

The change in speed seen from the Sun depends on the turn. The most it can ever be is **twice the approach speed**,
when the spacecraft is turned right round, like the tennis ball. Figure B shows what each planet can do for a
spacecraft passing 300 km above it at 6 km/s.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="A bar chart of the biggest change in speed a spacecraft can get from one flyby, passing 300 km above the surface or cloud tops at 6 km/s relative to the planet. The Moon gives about 0.8 km/s, Mars about 2.9 km/s, Venus about 7.0, the Earth about 7.5, and Jupiter about 11.8, almost the limit of 12 km/s, twice the speed of the approach. The turn angles are also given: 7 degrees at the Moon, 28 at Mars, 72 at Venus, 77 at the Earth and 157 at Jupiter.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">The most one flyby can change your speed</text>
    <text x="6" y="24" fill="#555">passing 300 km up, at 6 km/s relative to the planet</text>
    <line x1="70" y1="34" x2="70" y2="176" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="70" y="186" text-anchor="middle">0</text>
    <line x1="110" y1="34" x2="110" y2="176" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="110" y="186" text-anchor="middle">2</text>
    <line x1="150" y1="34" x2="150" y2="176" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="150" y="186" text-anchor="middle">4</text>
    <line x1="190" y1="34" x2="190" y2="176" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="190" y="186" text-anchor="middle">6</text>
    <line x1="230" y1="34" x2="230" y2="176" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="230" y="186" text-anchor="middle">8</text>
    <line x1="270" y1="34" x2="270" y2="176" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="270" y="186" text-anchor="middle">10</text>
    <line x1="310" y1="34" x2="310" y2="176" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="310" y="186" text-anchor="middle">12</text>
    <text x="190" y="196" text-anchor="middle">change in speed, km/s</text>
    <line x1="310" y1="34" x2="310" y2="176" stroke="currentColor" stroke-width="0.8" stroke-dasharray="3 2"/>
    <text x="307" y="42" text-anchor="end">the limit: twice 6 km/s</text>
    <text x="66" y="58" text-anchor="end">Moon</text>
    <rect x="70" y="48" width="15.0" height="12" fill="#cfc8bf"/>
    <text x="89.0" y="57">0.8 km/s, turned 7°</text>
    <text x="66" y="84" text-anchor="end">Mars</text>
    <rect x="70" y="74" width="58.4" height="12" fill="#c1440e"/>
    <text x="132.4" y="83">2.9 km/s, turned 28°</text>
    <text x="66" y="110" text-anchor="end">Venus</text>
    <rect x="70" y="100" width="140.9" height="12" fill="#eea66f"/>
    <text x="214.9" y="109">7.0 km/s, turned 72°</text>
    <text x="66" y="136" text-anchor="end">Earth</text>
    <rect x="70" y="126" width="149.7" height="12" fill="#5aa0d8"/>
    <text x="223.7" y="135">7.5 km/s, turned 77°</text>
    <text x="66" y="162" text-anchor="end">Jupiter</text>
    <rect x="70" y="152" width="235.2" height="12" fill="#eea66f"/>
    <text x="301.2" y="161" text-anchor="end">11.8 km/s, turned 157°</text>
    <text x="6" y="226">The heavier the planet, the more it bends the path and the more speed it can give. Mars is</text>
    <text x="6" y="235">light, so it turns a spacecraft only about 30°; Jupiter can turn it almost right round.</text>
    <text x="6" y="244">Slower approaches turn more, but the change can never be more than twice the approach speed.</text>
  </g>
</svg>
</div>

Jupiter, 318 times as heavy as the Earth, can turn a spacecraft almost right round. The Moon hardly bends it. Mars,
about a tenth of the Earth's mass, turns it about 30°, so a Mars flyby gives a useful push, but not a big one.

The flyby also has to be aimed very precisely. A few kilometres off at the planet means thousands of kilometres off at
the next stop, so teams track the spacecraft closely (chapter 12) and correct its course on the way in.

??? note "Sources"
    - The turn and speed change, the factor of two: our arithmetic, section 16.9, and Wikipedia, Gravity assist
      (above).
    - Masses, $GM$ and radii: the NASA fact sheets for each planet, as in the Jupiter Fact Sheet (above) and the
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html). Jupiter 317.8 Earth masses and
      Mars 0.107: the same sheets.
    - Aiming errors growing with distance and close tracking before flybys: standard.

## 16.5 Falling towards the Sun { #inner }

To reach Mercury or the Sun, a spacecraft has to **lose** most of the Earth's 29.8 km/s round the Sun. That costs even
more than going outwards. So it passes in front of planets, coming away slower each time.

- **Mariner 10**, launched by NASA on 3 November 1973, passed 5,768 km from Venus on 5 February 1974, the first
  spacecraft to use a flyby to reach another planet. It went on to Mercury on 29 March 1974. The Italian scientist
  **Giuseppe "Bepi" Colombo** of the University of Padua saw that Mariner 10's orbit round the Sun could be made
  almost exactly twice Mercury's year, so it would meet Mercury again and again. It made three passes, the last on
  16 March 1975.
- **MESSENGER** flew past the Earth once, Venus twice and Mercury three times before going into orbit round Mercury,
  where it worked from 2011 to 2015.
- **BepiColombo**, a joint mission of Europe's ESA and Japan's JAXA named after Colombo, was launched on 20 October
  2018. It has used nine flybys: the Earth and Moon in April 2020, Venus in 2020 and 2021, and Mercury six times from
  2021 to 2025. A problem with its electric thrusters delayed its arrival, and it is due to go into orbit round Mercury
  on **21 November 2026**, two weeks after this chapter was written.
- **NASA's Parker Solar Probe** used seven flybys of Venus over nearly seven years to shrink its orbit, until it
  passed within 6.9 million km of the Sun's centre. At its closest, in 2024, it moved at **191 km/s**, the fastest
  object people have ever built.

??? note "Sources"
    - Mariner 10: launched on 3 November 1973; Venus on 5 February 1974 at 5,768 km; Mercury on 29 March 1974 and 16
      March 1975; Colombo's calculations giving repeated encounters: Wikipedia,
      [Mariner 10](https://en.wikipedia.org/wiki/Mariner_10) (weaker). The first spacecraft to use the slingshot to
      reach another planet: Wikipedia, Gravity assist (above). Colombo, "an Italian scientist, mathematician and
      engineer at the University of Padua", and three Mercury flybys instead of one: Wikipedia,
      [Giuseppe Colombo](https://en.wikipedia.org/wiki/Giuseppe_Colombo) (weaker). An orbital period almost exactly
      twice Mercury's: Wikipedia, Mariner 10 (above).
    - MESSENGER's flybys and its orbit from 2011 to 2015: Wikipedia,
      [MESSENGER](https://en.wikipedia.org/wiki/MESSENGER) (weaker).
    - BepiColombo: ESA and JAXA, named after Colombo, launched on 20 October 2018, nine gravity assists, the thruster
      problem found in 2024, and Mercury orbit insertion planned for 21 November 2026: Wikipedia,
      [BepiColombo](https://en.wikipedia.org/wiki/BepiColombo) (weaker).
    - Parker Solar Probe: seven Venus flybys over nearly seven years, 9.86 solar radii or 6.9 million km from the
      centre, 191 km/s at closest approach in 2024, the fastest object built: Wikipedia,
      [Parker Solar Probe](https://en.wikipedia.org/wiki/Parker_Solar_Probe) (weaker).

## 16.6 Back to the Earth { #earth }

The Earth is the heaviest of the inner planets, and every spacecraft starts there. A craft launched onto an orbit round
the Sun that brings it back a year or two later can swing past the Earth and leave with a new speed and direction.

- **Giotto**, ESA's probe to Halley's Comet, was woken on 2 July 1990 to swing past the Earth on its way to a second
  comet, Grigg–Skjellerup.
- **Hiten**, Japan's first Moon probe, launched by ISAS on 24 January 1990, made a series of swings past the Moon.
  After the eighth, on 19 March 1991, it dipped to 125.5 km above the Pacific at 11.0 km/s to test slowing down in the
  top of the air, a trick for chapter 17.
- **ESCAPADE**'s two spacecraft dived to within 600 km of the Earth in November 2026 for a pair of gravity assists,
  firing their engines at the same time, to set off for Mars (chapter 15).
- **NASA's Europa Clipper**, launched on 14 October 2024 for Jupiter's moon Europa, swung past Mars on 1 March 2025 and
  is due to swing past the Earth on **3 December 2026**. It should reach Jupiter in April 2030.

??? note "Sources"
    - Giotto woken on 2 July 1990 for an Earth flyby to slingshot to its next comet, Grigg–Skjellerup: Wikipedia,
      [Giotto (spacecraft)](https://en.wikipedia.org/wiki/Giotto_(spacecraft)) (weaker).
    - Hiten: built by ISAS, launched on 24 January 1990, Japan's first lunar probe, lunar swing-bys, and after the
      eighth the aerobraking test on 19 March 1991 at 125.5 km over the Pacific and 11.0 km/s: Wikipedia,
      [Hiten (spacecraft)](https://en.wikipedia.org/wiki/Hiten_(spacecraft)) (weaker).
    - ESCAPADE within 600 km of the Earth for a pair of gravity assists and its escape burns: Wikipedia,
      [ESCAPADE](https://en.wikipedia.org/wiki/ESCAPADE) (weaker).
    - Europa Clipper: launched on 14 October 2024, Mars on 1 March 2025, the Earth on 3 December 2026, Jupiter orbit in
      April 2030: Wikipedia, [Europa Clipper](https://en.wikipedia.org/wiki/Europa_Clipper) (weaker).

## 16.7 Swinging past Mars { #mars }

Mars lies on the way out from the Earth to the asteroid belt and Jupiter, so it is a handy stepping stone. Its push is
modest (figure B), but often enough. Recent missions that have swung past it:

| Spacecraft | Flew past Mars | Going to |
| --- | --- | --- |
| ESA's Rosetta | 25 February 2007 | the comet Churyumov–Gerasimenko |
| NASA's Dawn | February 2009 | the asteroids Vesta and Ceres |
| NASA's Europa Clipper | 1 March 2025 | Jupiter's moon Europa |
| ESA's Hera | 12 March 2025, 5,000 km up | the double asteroid Didymos |
| NASA's Psyche | 15 May 2026, 4,609 km up | the metal asteroid Psyche |

Hera used its pass to photograph Mars's small moon **Deimos**. It reached Didymos in November 2026. Psyche is due at
its asteroid in August 2029.

How much did Mars give? We do not know the speeds these craft passed at, but suppose a spacecraft passes 4,609 km up
at 5 km/s. Then Mars turns it about 20° and changes its speed by up to about 1.8 km/s, more than most spacecraft
could manage with their own fuel.

**Cyclers.** In 1985 the Apollo 11 astronaut Buzz Aldrin described a **Mars cycler**: a spaceship that never stops,
on an orbit round the Sun that swings past the Earth and Mars again and again, using each flyby to stay on track. His
cycler goes from the Earth to Mars in 146 days, spends 16 months out beyond Mars, and comes back, repeating every
synodic period of about 2.135 years. Crews would ride small craft called taxis out to it and back, while the big ship,
with heavy shielding against radiation, stays on its loop.

??? note "Sources"
    - Rosetta's low flyby of Mars on 25 February 2007 to correct its path, and its comet: Wikipedia,
      [Rosetta (spacecraft)](https://en.wikipedia.org/wiki/Rosetta_(spacecraft)) (weaker).
    - Dawn's Mars gravity assist in February 2009, to Vesta and Ceres: Wikipedia,
      [Dawn (spacecraft)](https://en.wikipedia.org/wiki/Dawn_(spacecraft)) (weaker).
    - Europa Clipper: section 16.6.
    - Hera's Mars gravity assist on 12 March 2025 at 5,000 km, observations of Deimos, and arrival at the double
      asteroid in November 2026: Wikipedia, [Hera (space mission)](https://en.wikipedia.org/wiki/Hera_(space_mission))
      (weaker).
    - Psyche's Mars gravity assist on 15 May 2026 at 4,609 km, arrival in August 2029: Wikipedia,
      [Psyche (spacecraft)](https://en.wikipedia.org/wiki/Psyche_(spacecraft)) (weaker).
    - The 20° and 1.8 km/s for an assumed 5 km/s: our arithmetic, section 16.9.
    - Aldrin's Mars cycler of 1985, 146 days out, 16 months beyond Mars, the synodic period of about 2.135 years:
      Wikipedia, [Mars cycler](https://en.wikipedia.org/wiki/Mars_cycler) (weaker). The taxis and the heavy radiation
      shielding: the same article.

## 16.8 Working it out { #working }

**The ball and the train.** In the train's frame the ball arrives at $30 + 50 = 80$ km/h and leaves at 80 km/h. Back in
the platform's frame, add the train's 50: $80 + 50 = 130$ km/h. Gain: $2 \times 50 = 100$ km/h.

**Figure A.** Let the planet move at $V$ and the spacecraft pass it at $v$, coming in at right angles to the planet's
path and turned 60° towards it. Before, seen from the Sun, the speed is $\sqrt{V^2 + v^2}$. After, the spacecraft's
velocity past the planet is $v$ at 30° above the planet's direction, so the speed is

$$\sqrt{(V + v\cos 30°)^2 + (v \sin 30°)^2}.$$

With $V = 80$ and $v = 50$ in the drawing's units: before $94.3$, after $125.8$, a gain of a third.

**How much speed one flyby changes.** For a pass at distance $r_p$ from the planet's centre, at speed $v_\infty$ far
from it,

$$e = 1 + \frac{r_p v_\infty^2}{GM}, \qquad \sin\frac{\delta}{2} = \frac{1}{e}, \qquad
\Delta v_{\max} = 2 v_\infty \sin\frac{\delta}{2} = \frac{2 v_\infty}{e},$$

where $\delta$ is the turn and $\Delta v_{\max}$ the biggest possible change in speed seen from the Sun.

- **Mars**, 300 km up ($r_p = 3{,}696$ km), $v_\infty = 6$ km/s: $e = 1 + 3{,}696 \times 36 / 42{,}828 = 4.11$, so
  $\delta = 28°$ and $\Delta v_{\max} = 12 / 4.11 = 2.9$ km/s.
- **Earth**, 300 km up ($r_p = 6{,}678$ km): $e = 1 + 6{,}678 \times 36 / 398{,}600 = 1.60$, so $\delta = 77°$ and
  $\Delta v_{\max} = 7.5$ km/s.

| Flyby 300 km up | Mars | Earth |
| --- | --- | --- |
| Turn at 3 km/s | 69° | 121° |
| Turn at 6 km/s | 28° | 77° |
| Most speed change at 3 km/s | 3.4 km/s | 5.2 km/s |
| Most speed change at 6 km/s | 2.9 km/s | 7.5 km/s |
| Most speed change at 8 km/s | 2.5 km/s | 7.7 km/s |

??? note "Sources"
    - $GM$ and radii: the NASA fact sheets (above). The formulas: section 16.9. The numbers: our arithmetic.

## 16.9 The turn, worked out { #derive }

Seen from the planet, a flyby is a hyperbola (chapter 7, [section 7.5](07-Speed-Energy-and-Escape.md#bound)), with the
planet at one focus.

**Energy.** Far away the speed is $v_\infty$, so the energy per kilogram is $\varepsilon = v_\infty^2/2$. For a
hyperbola $\varepsilon = GM/(2a)$ with $a > 0$ the semi-major axis, so $a = GM/v_\infty^2$.

**Closest pass.** For a hyperbola, $r_p = a(e - 1)$, so

$$e = 1 + \frac{r_p}{a} = 1 + \frac{r_p v_\infty^2}{GM}.$$

**The turn.** The path follows $r = a(e^2 - 1)/(1 + e\cos\nu)$, which runs off to infinity when $1 + e\cos\nu = 0$.
So the two arms point at $\nu = \pm\arccos(-1/e)$. The angle between the incoming and outgoing directions is
$\delta = 2\arccos(-1/e) - 180°$, which simplifies to

$$\sin\frac{\delta}{2} = \frac{1}{e}.$$

**The speed change.** The velocity past the planet keeps its size $v_\infty$ and turns by $\delta$. Two arrows of
length $v_\infty$ with angle $\delta$ between them differ by $2v_\infty\sin(\delta/2)$. Seen from the Sun, the
spacecraft's velocity is the planet's velocity plus this, so its change is the same vector, of size
$2 v_\infty / e$. How much of that becomes extra speed depends on the direction: all of it when the change points
along the spacecraft's path.

**Energy gained.** Per kilogram, the change in energy seen from the Sun is $\vec V \cdot \Delta \vec v$, the planet's
velocity times the part of the change that lies along it. Passing behind the planet makes this positive.

**Check: the tennis ball.** A complete turn, $\delta = 180°$, needs $e = 1$, a head-on bounce. Then the change is
$2 v_\infty$, and if it lies along the planet's motion with the ball arriving head-on, the gain is twice the planet's
speed, as on the platform.

??? note "Sources"
    - The hyperbola, $a = GM/v_\infty^2$, $r_p = a(e - 1)$ and the asymptotes: standard orbital mechanics, chapter 7,
      and Wikipedia, [Hyperbolic trajectory](https://en.wikipedia.org/wiki/Hyperbolic_trajectory) (weaker).
    - The energy change $\vec V \cdot \Delta\vec v$: from the sum of velocities, our arithmetic.

## Check yourself { #check }

**1.** (beginner) Seen from the planet, does a spacecraft leave a flyby faster than it arrived?

??? note "Answer"
    No. Seen from the planet it leaves exactly as fast as it came; only its direction changes. The gain or loss shows
    up only when you add the planet's own motion round the Sun.

**2.** (beginner) Which spacecraft first used a gravity assist, and when?

??? note "Answer"
    The Soviet Luna 3, in October 1959, which swung round the Moon, photographed its far side, and came back towards
    the Earth.

**3.** (beginner) Why was 1977 a special year to launch to the outer planets?

??? note "Answer"
    Jupiter, Saturn, Uranus and Neptune were lined up so that one spacecraft could swing from each to the next, a
    line-up that comes once every 175 years. Voyager 2 used it.

**4.** (intermediate) Why does a flyby of Jupiter give much more than a flyby of Mars?

??? note "Answer"
    Jupiter is about 3,000 times as heavy as Mars, so it bends the path much more. A bigger turn means a bigger change
    in velocity, up to twice the approach speed.

**5.** (intermediate) Why did Mariner 10, MESSENGER and Parker Solar Probe pass in front of planets, not behind?

??? note "Answer"
    They needed to lose speed round the Sun to fall inwards, towards Mercury or the Sun. Passing in front of a planet
    makes the spacecraft slower afterwards, seen from the Sun.

**6.** (intermediate) Name two spacecraft that swung past Mars on their way somewhere else.

??? note "Answer"
    Any two of Rosetta (2007), Dawn (2009), Europa Clipper (2025), Hera (2025) and Psyche (2026).

**7.** (advanced) A spacecraft passes 300 km above Venus ($GM = 324{,}859$ km³/s², radius 6,052 km) at 5 km/s.
Find the turn and the biggest change in speed.

??? note "Answer"
    $e = 1 + 6{,}352 \times 25 / 324{,}859 = 1.489$, so $\sin(\delta/2) = 0.672$, $\delta = 84°$, and
    $\Delta v_{\max} = 10/1.489 = 6.7$ km/s.

**8.** (expert) Show that a flyby can never change the speed past the planet, but can change the speed seen from the
Sun by up to $2v_\infty$.

??? note "Answer"
    In the planet's frame gravity is the only force and the planet is (almost) fixed, so energy per kilogram,
    $v^2/2 - GM/r$, is the same far away on the way in and on the way out: the speed is $v_\infty$ both times. Seen
    from the Sun, both velocities have the planet's velocity added, so their difference is the difference of two
    vectors of size $v_\infty$, which is at most $2v_\infty$, reached when one points opposite to the other.

## Summary

- A flyby leaves a spacecraft's speed past the planet unchanged but turns it; adding the planet's motion, the speed
  round the Sun goes up or down.
- Passing behind a planet speeds a spacecraft up; passing in front slows it down. The planet's own change is far too
  small to measure.
- Kondratyuk, Zander, Crocco and Minovitch worked out the idea; Luna 3 used it first, in 1959.
- Voyager 2 used a line-up that comes once in 175 years to visit Jupiter, Saturn, Uranus and Neptune.
- Heavy planets bend paths more; the most any flyby can give is twice the approach speed.
- Mariner 10, MESSENGER, BepiColombo and Parker Solar Probe used flybys to fall in towards Mercury and the Sun.
- Rosetta, Dawn, Europa Clipper, Hera and Psyche have swung past Mars, and Mars cyclers could carry crews there and
  back again and again.

**Next:** chapter 17, Arriving, where a spacecraft reaches Mars and has to slow down: braking with its engine, dipping
into the air again and again, or diving straight in to land.

## Further reading

- Jim Bell, *The Interstellar Age: Inside the Forty-Year Voyager Mission*, Dutton, 2015.
