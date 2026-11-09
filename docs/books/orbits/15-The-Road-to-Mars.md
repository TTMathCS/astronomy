# 15. The road to Mars

*You cannot just point a rocket at Mars and fire. The Earth, Mars and the spacecraft are all going round the Sun, and
the Sun's pull bends every path. This chapter finds the cheapest road, half an ellipse described by Walter
Hohmann a hundred years ago. It shows why the trip takes most of a year, why the chance to go comes once every
26 months, how to leave the Earth with the least fuel, and why a crew who got there would have to wait well over a
year before they could come home.*

!!! abstract "In this chapter"
    **You will learn:**

    - why a spacecraft for Mars sets off along the Earth's own path, not straight towards Mars
    - who Walter Hohmann was, and what his half-ellipse is
    - why launch windows to Mars come once every 26 months, and what happened in the window of 2026
    - why the best place to fire the engine is low down, close to the Earth
    - how a little extra speed cuts weeks off the trip, and what a porkchop plot shows
    - how spacecraft are steered on the way
    - why a round trip to Mars takes years
    - what it takes to leave Mars for home
    - how to work out the speeds, the angles and the waiting times yourself

    **You need:** chapters 3, 7 and 13.

    **Levels:** 15.1 to 15.3 are beginner; 15.4 to 15.8 are intermediate; 15.9 is advanced; 15.10 is expert.

## 15.1 Why not aim straight at Mars? { #aim }

When Mars shines bright in the night sky it seems simple: point the rocket at it and go. It does not work, for three
reasons.

- **Everything moves.** The Earth goes round the Sun at about 29.8 km/s and Mars at about 24.1 km/s. Mars will not be
  where you aimed by the time you get there, months later.
- **You already have the Earth's speed.** A rocket leaving the Earth keeps the Earth's 29.8 km/s round the Sun. To
  fly straight out across the gap, it would first have to cancel most of that sideways speed, far more than any rocket
  can do.
- **The Sun pulls.** Every path through the solar system bends round the Sun. There are no straight lines.

So the trick is to go with the flow. The spacecraft leaves the Earth going a little **faster than the Earth, in the
same direction**. It is now too fast for a circle at the Earth's distance, so it swings outwards onto an ellipse
(chapter 7). Give it just enough extra speed and the far end of that ellipse reaches out to Mars's orbit. The Sun's
pull does the steering for free.

The physics lesson [The trip to Mars](https://physics.akadian.ca/topics/rockets/level-4/03-the-trip-to-mars.html)
tells the same story with less arithmetic.

??? note "Sources"
    - The mean orbital speeds of 29.78 km/s for the Earth and 24.08 km/s for Mars: NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html), which gives both side by side.
      Our circular-orbit value for Mars, 24.13 km/s, is in section 15.9.
    - Going faster along your path raises the far side of the orbit: section 7.6 and standard.

## 15.2 Hohmann's half-ellipse { #hohmann }

**Walter Hohmann** (1880–1945) was a German engineer. Born in Hardheim, the son of a
doctor, he lived for a time as a boy in Port Elizabeth, South Africa, where his father showed him the stars of the
southern sky. Reading the stories of the French writer Jules Verne and the German writer Kurd Lasswitz, he started to
wonder how you would get up there. He studied civil engineering in Munich, finishing in 1904, worked for the cities of
Vienna, Hanover and Breslau (now Wrocław), and settled in Essen, where he became the city's chief architect. In his
spare time he worked out how to travel between the planets, and in 1925 he published it in a book,
*Die Erreichbarkeit der Himmelskörper*, "The Reachability of the Heavenly Bodies".

Chapter 3 ([section 3.7](03-Keplers-Three-Laws.md#transfer)) met his idea: an ellipse round the Sun whose
**perihelion touches the Earth's orbit** and whose **aphelion touches Mars's orbit**. The spacecraft rides half of it,
from one end to the other. Figure A draws it to scale.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The cheapest path from the Earth to Mars, drawn to scale and seen from above, with the Sun in the middle. The Earth's orbit is a circle 1 AU across from the Sun and Mars's orbit a larger circle 1.52 AU out. The path is half an ellipse that touches the Earth's orbit where the spacecraft leaves, at the bottom, and touches Mars's orbit on the far side of the Sun, at the top, where it arrives 259 days later. At launch Mars is 44 degrees ahead of the Earth. During the trip Mars moves 136 degrees round to meet the spacecraft, while the Earth moves 255 degrees and ends up 75 degrees ahead of Mars.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">The cheapest way to Mars, to scale, seen from above</text>
    <circle cx="112" cy="116" r="60.0" fill="none" stroke="#5aa0d8" stroke-width="0.7" stroke-dasharray="2 2"/>
    <circle cx="112" cy="116" r="91.4" fill="none" stroke="#c1440e" stroke-width="0.7" stroke-dasharray="2 2"/>
    <path d="M112.0,176.0 L114.4,176.0 L116.9,175.8 L119.3,175.6 L121.8,175.3 L124.2,175.0 L126.6,174.5 L128.9,174.0 L131.3,173.4 L133.6,172.7 L135.9,171.9 L138.2,171.1 L140.4,170.2 L142.6,169.2 L144.8,168.2 L146.9,167.1 L149.0,165.9 L151.0,164.7 L153.0,163.4 L154.9,162.0 L156.8,160.6 L158.6,159.1 L160.4,157.6 L162.1,156.1 L163.7,154.5 L165.3,152.8 L166.9,151.1 L168.4,149.4 L169.8,147.7 L171.1,145.9 L172.4,144.0 L173.7,142.2 L174.9,140.3 L176.0,138.4 L177.1,136.5 L178.1,134.5 L179.0,132.6 L179.9,130.6 L180.7,128.6 L181.4,126.6 L182.1,124.6 L182.8,122.6 L183.4,120.6 L183.9,118.6 L184.3,116.5 L184.7,114.5 L185.1,112.5 L185.4,110.5 L185.6,108.4 L185.8,106.4 L186.0,104.4 L186.0,102.4 L186.1,100.4 L186.0,98.5 L186.0,96.5 L185.8,94.5 L185.7,92.6 L185.5,90.7 L185.2,88.8 L184.9,86.9 L184.5,85.0 L184.1,83.2 L183.7,81.3 L183.2,79.5 L182.7,77.7 L182.1,75.9 L181.5,74.2 L180.9,72.5 L180.2,70.8 L179.5,69.1 L178.7,67.4 L177.9,65.8 L177.1,64.2 L176.3,62.6 L175.4,61.1 L174.4,59.6 L173.5,58.1 L172.5,56.6 L171.5,55.2 L170.5,53.8 L169.4,52.4 L168.3,51.1 L167.2,49.8 L166.0,48.5 L164.8,47.2 L163.6,46.0 L162.4,44.8 L161.2,43.7 L159.9,42.6 L158.6,41.5 L157.3,40.4 L156.0,39.4 L154.6,38.4 L153.3,37.4 L151.9,36.5 L150.5,35.6 L149.1,34.8 L147.7,33.9 L146.2,33.1 L144.7,32.4 L143.3,31.7 L141.8,31.0 L140.3,30.3 L138.8,29.7 L137.3,29.1 L135.7,28.6 L134.2,28.1 L132.6,27.6 L131.1,27.1 L129.5,26.7 L128.0,26.4 L126.4,26.0 L124.8,25.7 L123.2,25.4 L121.6,25.2 L120.0,25.0 L118.4,24.9 L116.8,24.7 L115.2,24.6 L113.6,24.6 L112.0,24.6" fill="none" stroke="currentColor" stroke-width="1.3"/>
    <circle cx="162.4" cy="155.8" r="1.4" fill="currentColor"/>
    <circle cx="185.2" cy="111.8" r="1.4" fill="currentColor"/>
    <circle cx="179.1" cy="68.2" r="1.4" fill="currentColor"/>
    <circle cx="153.7" cy="37.7" r="1.4" fill="currentColor"/>
    <circle cx="118.6" cy="24.9" r="1.4" fill="currentColor"/>
    <circle cx="112" cy="116" r="5" fill="#eea66f"/>
    <text x="119" y="119">Sun</text>
    <line x1="112" y1="116" x2="112.0" y2="176.0" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <line x1="112" y1="116" x2="175.9" y2="181.4" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <path d="M112.0,141.2 L113.0,141.2 L113.9,141.1 L114.9,141.0 L115.9,140.9 L116.8,140.7 L117.8,140.5 L118.7,140.3 L119.7,140.0 L120.6,139.7 L121.5,139.3 L122.4,139.0 L123.3,138.5 L124.1,138.1 L125.0,137.6 L125.8,137.1 L126.6,136.5 L127.4,135.9 L128.2,135.3 L128.9,134.7 L129.6,134.0" fill="none" stroke="#555" stroke-width="0.6"/>
    <text x="124.5" y="149.6" fill="#555">44°</text>
    <circle cx="112.0" cy="176.0" r="3.2" fill="#5aa0d8"/>
    <text x="106.0" y="188.0" text-anchor="end" fill="#5aa0d8">Earth at launch</text>
    <circle cx="175.9" cy="181.4" r="3.2" fill="none" stroke="#c1440e" stroke-width="1"/>
    <text x="181.9" y="187.4" fill="#c1440e">Mars at launch</text>
    <circle cx="112.0" cy="24.6" r="3.2" fill="#c1440e"/>
    <text x="118.0" y="22.6" fill="#c1440e">Mars at arrival</text>
    <circle cx="54.0" cy="100.6" r="3.2" fill="none" stroke="#5aa0d8" stroke-width="1"/>
    <text x="60.0" y="95.6" fill="#5aa0d8">Earth at arrival</text>
    <text x="214" y="96">The path: half an ellipse,</text>
    <text x="214" y="105">from 1 AU out to 1.52 AU.</text>
    <text x="214" y="114">Dots: every 50 days.</text>
    <text x="214" y="132" fill="#555">Everything goes round</text>
    <text x="214" y="141" fill="#555">anticlockwise.</text>
    <text x="6" y="226">At launch Mars must be 44° ahead of the Earth. The trip takes 259 days, and Mars moves 136°</text>
    <text x="6" y="235">to meet the spacecraft at the far side of the Sun. The Earth moves 255° in the same time,</text>
    <text x="6" y="244">so when we arrive it is 75° ahead of Mars, the wrong place to come straight home.</text>
  </g>
</svg>
</div>

**Two pushes.** On circles round the Sun, the Earth moves at 29.78 km/s and Mars at 24.13 km/s. Using the speed rule
of chapter 7 ([section 7.6](07-Speed-Energy-and-Escape.md#visviva)):

- At the start, the half-ellipse needs **32.73 km/s**. The spacecraft must leave the Earth's neighbourhood going
  **2.94 km/s faster** than the Earth.
- At the far end it has slowed to **21.48 km/s**, while Mars is doing 24.13. Mars comes up from behind at
  **2.65 km/s**. To stay with Mars, the spacecraft must gain 2.65 km/s, or let Mars's pull and air help (chapter 17).

**Why it is the cheapest.** Both pushes point exactly along the way the spacecraft is already going, and the path
just touches each orbit, so no speed is wasted turning. Between circular orbits in the same plane it is the cheapest
path with two pushes. A path with three pushes can do better only when one orbit is about 12 times the size of the
other or more, far beyond Mars's 1.5.

**The time.** Kepler's third law gives half of the ellipse's period: **259 days**, about 8½ months. The spacecraft
travels about 590 million km to cover a gap that, at its narrowest, is only about 55 million km.

The physics lesson [Hohmann transfer](https://physics.akadian.ca/topics/gravity/level-7/05-hohmann-transfer.html)
works through the same pushes.

??? note "Sources"
    - Hohmann's dates, 18 March 1880 to 11 March 1945, a German engineer; born in Hardheim, son of a doctor; boyhood in
      Port Elizabeth, his father showing him the southern constellations; Verne and Lasswitz and "How do you get up
      there?"; civil engineering at the Technical University of Munich, 1904; Vienna, Hanover, Breslau and chief
      architect in Essen; the 1925 book: Wikipedia, [Walter Hohmann](https://en.wikipedia.org/wiki/Walter_Hohmann)
      (weaker). The title in English is our translation.
    - The half-ellipse touching both orbits and the 1925 book: Wikipedia,
      [Hohmann transfer orbit](https://en.wikipedia.org/wiki/Hohmann_transfer_orbit) (weaker).
    - The Hohmann path as the cheapest two-push transfer between circular orbits in a plane: standard. A three-push,
      bi-elliptic path beating it only when the ratio is 11.94 or more: the same Wikipedia article.
    - The speeds, 259 days and 590 million km: our arithmetic, section 15.9. The narrowest gap, about 55 million km:
      Mars's perihelion of 206.65 million km less the Earth's aphelion of 152.10 million km, from the NASA Mars Fact
      Sheet (above), our arithmetic.

## 15.3 Once every 26 months { #windows }

Figure A shows a catch. The spacecraft takes 259 days to reach Mars's orbit, and Mars has to be there when it arrives.
In 259 days Mars goes 136° round the Sun, so at launch Mars must already be **44° ahead of the Earth**.

The Earth goes round faster than Mars and gains on it by about 0.46° a day. To gain a whole lap, 360°, and get back to
the same line-up takes about **780 days**, close to 26 months. NASA gives Mars's synodic period as 779.94 days. So the
**launch window** to Mars opens once every 26 months, and stays open a few weeks. Miss it, and you wait for the next
one. The history book's chart of Mars launches
([section 21.7](../history/21-The-Space-Age-at-Mars.md#hard)) shows them coming in two-year steps since 1960.

**July 2020.** Three countries used the same window within ten days: the Emirates' **Hope** on 20 July, China's
**Tianwen-1** on 23 July and NASA's **Perseverance** on 30 July. All three reached Mars in February 2021, within ten
days of each other.

**The window of 2026.** As this chapter was written, in November 2026, the window was open again.

- Japan's **MMX** was launched on an H3 rocket on 19 October 2026, in that year's window. It is due to reach Mars orbit
  in August 2027 and go on to Mars's moon Phobos.
- NASA's twin **ESCAPADE** spacecraft, Blue and Gold, were launched on 13 November 2025, a year before the window. They
  could not leave for Mars then, so they waited in a loop about 1.5 million km from the Earth,
  near the point L2 (chapter 9), until the window opened. Then they dived back to pass within 600 km of the Earth and
  fire their engines for Mars. Blue made its pass on 7 November 2026, and Gold's was planned for 9 November. Both are
  due to reach Mars orbit by September 2027.

Because the real orbits are ellipses, not circles, the best dates drift by weeks from one window to the next, and some
windows cost more than others. The physics lesson
[Launch windows](https://physics.akadian.ca/topics/gravity/level-7/06-launch-windows.html) works out the timing.

??? note "Sources"
    - The 44° lead, 136° and 0.46° a day: our arithmetic, section 15.10. Mars's synodic period of 779.94 days: NASA,
      Mars Fact Sheet (above).
    - Hope launched on 20 July 2020 and in Mars orbit on 9 February 2021: Wikipedia,
      [Emirates Mars Mission](https://en.wikipedia.org/wiki/Emirates_Mars_Mission) (weaker). Tianwen-1 launched on
      23 July 2020 and in orbit on 10 February 2021: Wikipedia, [Tianwen-1](https://en.wikipedia.org/wiki/Tianwen-1)
      (weaker). Perseverance launched on 30 July 2020 and landed on 18 February 2021: Wikipedia,
      [Perseverance (rover)](https://en.wikipedia.org/wiki/Perseverance_(rover)) (weaker).
    - MMX launched on an H3-24L on 19 October 2026 "during the year's launch window", Mars orbit in August 2027, then
      Phobos: Wikipedia, [Martian Moons eXploration](https://en.wikipedia.org/wiki/Martian_Moons_Exploration)
      (weaker).
    - ESCAPADE launched on 13 November 2025 to a staging orbit "about a million miles away" round the Sun–Earth L2
      point, loitering until the Mars window opened, then diving within 600 km of the Earth for its escape burns, Blue
      on 7 November 2026 and Gold planned for 9 November, Mars orbit by September 2027: Wikipedia,
      [ESCAPADE](https://en.wikipedia.org/wiki/ESCAPADE) (weaker). A million miles is 1.6 million km; we round to
      about 1.5 million km, the distance of L2 (chapter 9).
    - The best dates drifting and windows differing in cost because the orbits are not circles: standard.

## 15.4 Leaving the Earth: fire low down { #leaving }

The spacecraft needs to be 2.94 km/s faster than the Earth once it is clear of the Earth's pull. How much must its
engine give it? Not what you might guess.

Picture a spacecraft in a low orbit 300 km up, moving at 7.73 km/s. Escape speed there is 10.93 km/s (chapter 7,
[section 7.4](07-Speed-Energy-and-Escape.md#escape)).

- **The slow way.** Burn 3.20 km/s to reach escape speed and coast away from the Earth with nothing left over. Then,
  far away, burn another 2.94 km/s. Total: **6.14 km/s**.
- **The smart way.** Do it all in one burn, in low orbit. Speed up to 11.32 km/s, a burn of **3.59 km/s**. The
  spacecraft climbs out of the Earth's pull and is left with exactly 2.94 km/s to spare.

The one low burn saves 2.5 km/s. The reason is energy. A push of a given size adds more energy to something that is
already moving fast: kinetic energy grows with the **square** of the speed, so going from 7.73 to 11.32 km/s adds far
more energy than going from 0 to 3.59. The deeper in a gravity well you fire, the faster you are moving and the more
each kilogram of fuel is worth. This is the **Oberth effect**, named after Hermann Oberth, an Austro-Hungarian-born
German physicist and a founder of rocketry, who described it in 1927.

**Mangalyaan used it.** India's Mars Orbiter Mission was launched on 5 November 2013 on a PSLV rocket, which was not
strong enough to send it straight to Mars. So it went first into a long ellipse round the Earth. Over the next
month it fired its own 440-newton engine as it swept through its low point, where it was fastest, raising the far
end of its orbit seven times. The first burn, on 6 November, lasted 416 seconds. Then, on 30 November 2013, one more
burn sent it off to Mars.

ESCAPADE did the same thing in November 2026: it dived to within 600 km of the Earth so that its engine burns would
happen where it was moving fastest.

Add the 9.4 km/s needed to reach low orbit in the first place (chapter 13,
[section 13.6](13-Rockets-and-Getting-to-Orbit.md#budget)), and leaving the ground for Mars takes about **13 km/s**.

??? note "Sources"
    - Escape speed, orbit speed and the 3.59 and 6.14 km/s: our arithmetic, section 15.9, with $GM$ and the radius
      from the NASA fact sheets (above).
    - The Oberth effect, named after Hermann Oberth, "an Austro-Hungarian-born German physicist and a founder of modern
      rocketry", described in 1927; burning at the lowest point, where speed and kinetic energy are greatest, is most
      efficient: Wikipedia, [Oberth effect](https://en.wikipedia.org/wiki/Oberth_effect) (weaker).
    - The Mars Orbiter Mission launched on PSLV-C25 on 5 November 2013; not powerful enough to go straight to Mars;
      perigee burns using the Oberth effect; seven apogee-raising manoeuvres; the first on 6 November, 440 N for
      416 s; trans-Mars injection on 30 November 2013: Wikipedia,
      [Mars Orbiter Mission](https://en.wikipedia.org/wiki/Mars_Orbiter_Mission) (weaker).
    - ESCAPADE within 600 km for its escape burns: Wikipedia, ESCAPADE (above). That this uses the Oberth effect: our
      reading.
    - 9.4 km/s to low orbit: chapter 13 (above). The total of about 13 km/s: our arithmetic.

## 15.5 Faster roads, and porkchop plots { #paths }

Look at figure A again. Near its far end the half-ellipse runs almost alongside Mars's orbit, and the spacecraft is at
its slowest there. The last few weeks are a slow creep up to Mars's orbit. Leave a little faster, and the ellipse
reaches past Mars's orbit, so the spacecraft crosses it sooner, before reaching its own far end.

| Speed beyond the Earth's | Days to Mars's orbit | Burn from 300 km up | Mars comes past at |
| --- | --- | --- | --- |
| 2.94 km/s (Hohmann) | 259 | 3.59 km/s | 2.65 km/s |
| 3.0 km/s | 229 | 3.60 km/s | 3.0 km/s |
| 3.2 km/s | 200 | 3.66 km/s | 4.0 km/s |
| 3.5 km/s | 178 | 3.75 km/s | 5.1 km/s |
| 4.0 km/s | 155 | 3.91 km/s | 6.6 km/s |

Seven hundredths of a km/s more at launch, from 3.59 to 3.66, cuts the trip by two months. The price comes at the
other end: the spacecraft meets Mars at a steeper angle and much faster, so it has more speed to lose when it gets
there. A lander that slows down in Mars's air can cope; an orbiter that has to brake with its engine pays more
(chapter 17).

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="A bar chart of how long eleven spacecraft took to get from launch to Mars, from Mariner 4 in 1964 to Perseverance in 2020, with a line at 259 days for the half-ellipse path of figure A. Most took between 168 and 254 days, so most were faster than 259 days. Viking 1 took 304 days. India's Mars Orbiter Mission took 323 days from launch, of which the first 25 were spent raising its orbit around the Earth and 298 on the way to Mars.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">Days from launch to reaching Mars</text>
    <line x1="104.0" y1="22" x2="104.0" y2="197.6" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="104.0" y="206.6" text-anchor="middle">0</text>
    <line x1="164.0" y1="22" x2="164.0" y2="197.6" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="164.0" y="206.6" text-anchor="middle">100</text>
    <line x1="224.0" y1="22" x2="224.0" y2="197.6" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="224.0" y="206.6" text-anchor="middle">200</text>
    <line x1="284.0" y1="22" x2="284.0" y2="197.6" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="284.0" y="206.6" text-anchor="middle">300</text>
    <text x="100" y="33.0" text-anchor="end">Mariner 4, flyby, 1964</text>
    <rect x="104.0" y="26.0" width="137.4" height="8" fill="#c1440e"/>
    <text x="244.4" y="33.0">229</text>
    <text x="100" y="48.6" text-anchor="end">Mars 3, orbit, 1971</text>
    <rect x="104.0" y="41.6" width="112.8" height="8" fill="#c1440e"/>
    <text x="219.8" y="48.6">188</text>
    <text x="100" y="64.2" text-anchor="end">Mariner 9, orbit, 1971</text>
    <rect x="104.0" y="57.2" width="100.8" height="8" fill="#c1440e"/>
    <text x="207.8" y="64.2">168</text>
    <text x="100" y="79.8" text-anchor="end">Viking 1, orbit, 1975</text>
    <rect x="104.0" y="72.8" width="182.4" height="8" fill="#c1440e"/>
    <text x="289.4" y="79.8">304</text>
    <text x="100" y="95.4" text-anchor="end">Pathfinder, landing, 1996</text>
    <rect x="104.0" y="88.4" width="127.2" height="8" fill="#c1440e"/>
    <text x="234.2" y="95.4">212</text>
    <text x="100" y="111.0" text-anchor="end">Mars Express, orbit, 2003</text>
    <rect x="104.0" y="104.0" width="123.6" height="8" fill="#c1440e"/>
    <text x="230.6" y="111.0">206</text>
    <text x="100" y="126.6" text-anchor="end">Curiosity, landing, 2011</text>
    <rect x="104.0" y="119.6" width="152.4" height="8" fill="#c1440e"/>
    <text x="262.3" y="126.6">254</text>
    <text x="100" y="142.2" text-anchor="end">MOM, orbit, 2013</text>
    <rect x="104" y="135.2" width="15.0" height="8" fill="#cfc8bf"/>
    <rect x="119.0" y="135.2" width="178.8" height="8" fill="#c1440e"/>
    <text x="300.8" y="142.2">323</text>
    <text x="100" y="157.8" text-anchor="end">Hope, orbit, 2020</text>
    <rect x="104.0" y="150.8" width="122.4" height="8" fill="#c1440e"/>
    <text x="229.4" y="157.8">204</text>
    <text x="100" y="173.4" text-anchor="end">Tianwen-1, orbit, 2020</text>
    <rect x="104.0" y="166.4" width="121.2" height="8" fill="#c1440e"/>
    <text x="228.2" y="173.4">202</text>
    <text x="100" y="189.0" text-anchor="end">Perseverance, landing, 2020</text>
    <rect x="104.0" y="182.0" width="121.8" height="8" fill="#c1440e"/>
    <text x="228.8" y="189.0">203</text>
    <line x1="259.3" y1="20" x2="259.3" y2="197.6" stroke="currentColor" stroke-width="0.9" stroke-dasharray="3 2"/>
    <text x="256.3" y="18" text-anchor="end">figure A: 259 days</text>
    <text x="6" y="226">Most trips took 6 to 8 months, and most beat the 259 days of figure A: real orbits are not</text>
    <text x="6" y="235">perfect circles, and a little extra speed cuts weeks off the trip. Grey: the 25 days India's</text>
    <text x="6" y="244">Mars Orbiter Mission spent going round the Earth, raising its orbit, before it left.</text>
  </g>
</svg>
</div>

**Real orbits are not circles.** Mars's distance from the Sun swings from 1.38 to 1.67 AU. A Hohmann trip to Mars at
its nearest to the Sun would take 237 days; to Mars at its farthest, 281. In 2003 the Earth and Mars came closer than
they had for about 60,000 years. ESA's **Mars Express** used that window, and its name partly comes from the short
trip: 206 days.

**Real orbits are tilted.** Mars's orbit is tilted 1.85° to the Earth's. A trip of exactly half a lap would arrive at
a point where turning into Mars's plane costs a great deal, so real trips go a little less than halfway round the Sun,
or a little more.

**Porkchop plots.** To choose, planners draw a chart with the launch date across and the arrival date up. Over it they
draw contour lines of the launch energy needed, called **C3**, the square of the speed left over after escaping the
Earth. Each contour is a closed loop, and the shape often looks like a pork chop. The cheapest launch is in its centre;
the planners pick a date near it that gives a good arrival date too.

??? note "Sources"
    - The table: our arithmetic, section 15.10, for a spacecraft leaving along the Earth's path from a circular orbit
      at 1 AU to a circular Mars orbit, with the burn from 300 km up worked as in section 15.4.
    - Mars's perihelion of 206.650 million km and aphelion of 249.261 million km, and its orbit tilted 1.85061°: NASA,
      Mars Fact Sheet (above). 237 and 281 days: our arithmetic.
    - Mars Express launched on 2 June 2003 and in orbit on 25 December 2003; "Express" partly from the short voyage
      when the Earth and Mars were closer than they had been in about 60,000 years: Wikipedia,
      [Mars Express](https://en.wikipedia.org/wiki/Mars_Express) (weaker). 206 days: our arithmetic.
    - Avoiding exactly half a lap because of the plane change: standard.
    - Porkchop plots, with contours of equal characteristic energy, C3, against launch and arrival dates, and the
      minimum in the centre: Wikipedia, [Porkchop plot](https://en.wikipedia.org/wiki/Porkchop_plot) (weaker).
    - Figure B's dates. Mariner 4: launched on 28 November 1964, past Mars on 15 July 1965, Wikipedia,
      [Mariner 4](https://en.wikipedia.org/wiki/Mariner_4) (weaker). Mars 3: 28 May 1971 to 2 December 1971,
      Wikipedia, [Mars 3](https://en.wikipedia.org/wiki/Mars_3) (weaker). Mariner 9: 30 May 1971 to 14 November 1971,
      Wikipedia, [Mariner 9](https://en.wikipedia.org/wiki/Mariner_9) (weaker). Viking 1: 20 August 1975 to orbit on
      19 June 1976, Wikipedia, [Viking 1](https://en.wikipedia.org/wiki/Viking_1) (weaker). Mars Pathfinder:
      4 December 1996 to 4 July 1997, Wikipedia, [Mars Pathfinder](https://en.wikipedia.org/wiki/Mars_Pathfinder)
      (weaker). Curiosity: 26 November 2011 to 6 August 2012, Wikipedia,
      [Curiosity (rover)](https://en.wikipedia.org/wiki/Curiosity_(rover)) (weaker). The Mars Orbiter Mission: section
      15.4 and its orbit on 24 September 2014 after a 298-day transit. Hope, Tianwen-1 and Perseverance: section 15.3.
      The day counts: our arithmetic.

## 15.6 Steering on the way { #cruise }

No launch is perfect. A spacecraft leaves the Earth a little too fast or too slow, or a little off line, and over
hundreds of millions of kilometres a tiny error grows into a miss. So mission teams track it the whole way, by timing
radio signals and measuring their Doppler shift (chapter 12,
[section 12.5](12-Measuring-Orbits.md#tracking)), and every few weeks or months they fire small thrusters to correct
its course.

- India's Mars Orbiter Mission made its first **trajectory correction manoeuvre** on 11 December 2013, firing its
  22-newton thrusters for 40.5 seconds.
- NASA's Curiosity rover landed less than **2.4 km** from the centre of its target after a journey of 560 million km,
  about four parts in a billion.

Getting the steering wrong is fatal. In 1999 NASA's **Mars Climate Orbiter** was steered using numbers in the wrong
units, so its course drifted. It was aimed to pass 226 km above Mars and went in at about 57 km, and was lost (history
book, [section 21.7](../history/21-The-Space-Age-at-Mars.md#hard)). Chapter 17 looks at what happens on arrival.

??? note "Sources"
    - The first trajectory correction on 11 December 2013, 22 N thrusters for 40.5 s: Wikipedia, Mars Orbiter Mission
      (above).
    - Curiosity's landing less than 2.4 km from the centre of its target after a 560 million km journey: Wikipedia,
      Curiosity (rover) (above). Four parts in a billion: our arithmetic.
    - Mars Climate Orbiter, the pound-force seconds and newton-seconds, 226 km and about 57 km, lost on 23 September
      1999: history book, section 21.7 (above), and Wikipedia,
      [Mars Climate Orbiter](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) (weaker).
    - Tracking and regular course corrections in cruise: standard.

## 15.7 The way home { #home }

Look at the end of figure A. When the spacecraft reaches Mars, the Earth has run 255° round the Sun and is **75° ahead
of Mars**. To come home on a half-ellipse, the Earth must be in the right place in 259 days' time, which means it has
to be **75° behind** Mars at departure.

So the crew wait. The Earth gains on Mars by 0.46° a day, and it has to gain 210° more before the line-up is right.
That takes about **454 days**, or 15 months. The whole trip, out, waiting and back, takes
$259 + 454 + 259 = 972$ days: **about 2.7 years**.

Planners of human missions call this a **conjunction-class** mission. With real orbits, it is about nine months each
way and about 500 days on Mars.

The other choice is an **opposition-class** mission: a short stay and a round trip of 400 to 450 days, under 15
months. But at least one leg then has to cut across the solar system on a fast, expensive path. A third plan, the
Crocco grand tour, would not stop at all: the crew would fly past Mars and Venus and be home in under a year. Flying
past planets to change course is the subject of the next chapter.

??? note "Sources"
    - 255°, 75°, 210° and 454 days: our arithmetic, section 15.10, for circular orbits.
    - A conjunction-class mission of about nine months each way and about 500 days at Mars, and an opposition-class
      round trip of 400 to 450 days, under 15 months, needing much more energy: Wikipedia,
      [Human mission to Mars](https://en.wikipedia.org/wiki/Human_mission_to_Mars) (weaker). The Crocco grand tour, a
      flyby of Mars and Venus in under a year: the same article.

## 15.8 Leaving Mars { #mars }

The trip home starts at the bottom of Mars's gravity well, and that well is much shallower than the Earth's.

| From a circular orbit 300 km up | Mars | Earth |
| --- | --- | --- |
| Orbit speed | 3.41 km/s | 7.73 km/s |
| Escape speed | 4.82 km/s | 10.93 km/s |
| Speed needed beyond escape | 2.65 km/s | 2.94 km/s |
| One burn, low down | **2.09 km/s** | **3.59 km/s** |
| Escape first, then burn | 4.06 km/s | 6.14 km/s |

Leaving Mars orbit for home takes about 2.1 km/s, against 3.6 km/s to leave the Earth for Mars. Firing low still
helps, saving almost 2 km/s. Getting from the ground to low Mars orbit takes about 4.1 km/s (chapter 13,
[section 13.7](13-Rockets-and-Getting-to-Orbit.md#mars)).

No spacecraft has yet made the trip home from Mars. Two are planned. Japan's **MMX**, launched in October 2026,
is due to collect samples from Phobos, fly past Deimos, and bring the samples to the Earth in 2031. China's
**Tianwen-3** plans to bring about 500 g of Mars itself back by 2031. Both will have to leave Mars in a window, which
comes, like the outward one, once every 26 months.

??? note "Sources"
    - The table: our arithmetic, section 15.9, with $GM$ and radii from the NASA fact sheets (above).
    - 4.1 km/s from the surface: chapter 13, section 13.7.
    - MMX: samples from Phobos, flybys of Deimos and samples back in 2031: Wikipedia, Martian Moons eXploration
      (above). Tianwen-3: chapter 13, section 13.7.
    - No spacecraft yet back from Mars, as of 2026: standard; see the history book, section 21.9.
    - Windows home every 26 months: the same line-up argument as section 15.3.

## 15.9 Working it out { #working }

Take circular orbits: the Earth's at $r_1 = 1$ AU and Mars's at $r_2 = 1.5237$ AU, with the Sun's
$GM = 1.3271 \times 10^{11}$ km³/s² and 1 AU $= 1.4960 \times 10^8$ km.

**Speeds on the circles.** $v = \sqrt{GM/r}$ gives **29.78 km/s** for the Earth and **24.13 km/s** for Mars.

**The half-ellipse.** Its semi-major axis is $a = (1 + 1.5237)/2 = 1.2618$ AU. By the speed rule of chapter 7,
$v^2 = GM\,(2/r - 1/a)$:

- at 1 AU, $v = 29.78 \times \sqrt{2 \times 1.5237 / 2.5237} = 32.73$ km/s, so the first push is
  $32.73 - 29.78 = 2.94$ km/s;
- at 1.5237 AU, $v = 24.13 \times \sqrt{2 / 2.5237} = 21.48$ km/s, so the second is $24.13 - 21.48 = 2.65$ km/s.

**The time.** A full ellipse with $a = 1.2618$ AU takes $1.2618^{1.5} = 1.417$ years. Half is 0.709 years,
**259 days**.

**Leaving a planet.** From a circular orbit of radius $r$, with $v_c = \sqrt{GM/r}$ and escape speed
$v_e = \sqrt{2GM/r}$, the burn that leaves you with speed $v_\infty$ far away is

$$\Delta v = \sqrt{v_\infty^2 + v_e^2} - v_c .$$

- **Earth**, 300 km up: $r = 6{,}678$ km, $v_c = 7.73$, $v_e = 10.93$, $v_\infty = 2.94$:
  $\Delta v = \sqrt{2.94^2 + 10.93^2} - 7.73 = 11.32 - 7.73 = 3.59$ km/s.
- **Mars**, 300 km up: $r = 3{,}690$ km, $v_c = 3.41$, $v_e = 4.82$, $v_\infty = 2.65$:
  $\Delta v = \sqrt{2.65^2 + 4.82^2} - 3.41 = 5.50 - 3.41 = 2.09$ km/s.

| | Mars | Earth |
| --- | --- | --- |
| Speed round the Sun (circular) | 24.13 km/s | 29.78 km/s |
| Year | 687 days | 365 days |
| Hohmann push at this end | 2.65 km/s | 2.94 km/s |
| Burn to leave from 300 km up | 2.09 km/s | 3.59 km/s |
| Escape speed from the surface | 5.03 km/s | 11.19 km/s |
| Low orbit from the ground | about 4.1 km/s | about 9.4 km/s |

??? note "Sources"
    - $GM$ of the Sun, the AU, Mars's 1.5237 AU, the year lengths of 365.256 and 686.98 days, the planets' $GM$, radii
      and escape speeds: NASA fact sheets, as in the Mars Fact Sheet (above).
    - The speed rule: chapter 7, section 7.6. The rest is our arithmetic. Low orbit from the ground: chapter 13.

## 15.10 Angles and waits, worked out { #derive }

**The general pushes.** For a Hohmann transfer between circles of radius $r_1$ and $r_2$ round a body with $GM$:

$$\Delta v_1 = \sqrt{\frac{GM}{r_1}}\left(\sqrt{\frac{2r_2}{r_1 + r_2}} - 1\right), \qquad
\Delta v_2 = \sqrt{\frac{GM}{r_2}}\left(1 - \sqrt{\frac{2r_1}{r_1 + r_2}}\right), \qquad
t = \pi\sqrt{\frac{a^3}{GM}} .$$

**The lead angle.** Mars goes round at $360°/T_M$ per day, $T_M = 686.98$ days. In the trip time $t$ it moves
$360° \times t/T_M$, and it must end up 180° from where the Earth started, so at launch it must be ahead by

$$\theta = 180° - 360°\,\frac{t}{T_M} = 180° - 360° \times \frac{258.9}{686.98} = 180° - 135.7° = 44.3° .$$

Since $t/T_M = \tfrac{1}{2}(a/r_2)^{1.5}$, this is also
$\theta = 180°\,\bigl(1 - (a/r_2)^{1.5}\bigr) = 180° \times (1 - 0.8282^{1.5}) = 44.3°$.

**The line-up repeats.** The Earth gains on Mars at $360/365.256 - 360/686.98 = 0.98561 - 0.52403 = 0.46158°$ a day,
so the same line-up comes back every $360 / 0.46158 = 779.9$ days.

**Where the Earth is on arrival.** In 258.9 days the Earth moves $360° \times 258.9/365.256 = 255.1°$. Mars has reached
180°, so the Earth is $\varphi = 75.1°$ ahead.

**The wait.** By the same argument as the lead angle, the trip home needs the Earth $75.1°$ **behind** Mars at
departure, that is at $360° - 75.1° = 284.9°$ ahead. The Earth must gain $284.9° - 75.1° = 209.8°$, which takes

$$\frac{360° - 2\varphi}{0.46158°\text{ a day}} = \frac{209.8}{0.46158} \approx 454 \text{ days}.$$

**Faster roads.** Leaving 1 AU along the Earth's path at $29.78 + v_\infty$ gives an ellipse with
$1/a = 2/r_1 - v^2/GM$. The point where it crosses $r_2$ is found from $r = a(1 - e^2)/(1 + e\cos\nu)$, and the time
from Kepler's equation (chapter 4). With $v_\infty = 3.2$ km/s: $a = 1.296$ AU, $e = 0.228$, and the orbit crosses
$r_2$ at $\nu = 150°$ after 200 days, the row in section 15.5.

??? note "Sources"
    - The Hohmann formulas: Wikipedia, Hohmann transfer orbit (above). The angles, the 779.9 days, the 454-day wait and
      the faster road: our arithmetic. NASA's synodic period of 779.94 days agrees.

## Check yourself { #check }

**1.** (beginner) Why does a spacecraft for Mars set off in the same direction the Earth is moving, not straight at
Mars?

??? note "Answer"
    It already has the Earth's 29.8 km/s round the Sun. Adding a little more speed along that path swings it out on an
    ellipse to Mars's orbit. Flying straight across would mean cancelling most of the Earth's speed, which no rocket
    can do.

**2.** (beginner) Who was Walter Hohmann, and what did he describe in 1925?

??? note "Answer"
    A German engineer, the chief architect of Essen, who described the cheapest path between two orbits: half an
    ellipse touching both.

**3.** (beginner) Why do launches to Mars come in groups about 26 months apart?

??? note "Answer"
    At launch Mars must be about 44° ahead of the Earth. The Earth gains on Mars by about 0.46° a day, so that line-up
    comes back every 780 days, about 26 months.

**4.** (intermediate) Why did India's Mars Orbiter Mission fire its engine at the low point of its orbit round the
Earth, again and again?

??? note "Answer"
    Its rocket could not send it straight to Mars. Firing where it moved fastest, deep in the Earth's well, gave each
    kilogram of fuel the most energy: the Oberth effect.

**5.** (intermediate) Most trips to Mars took less than 259 days. How?

??? note "Answer"
    They left a little faster than a Hohmann path needs, so they crossed Mars's orbit before reaching the slow far end
    of their ellipse. A few hundredths of a km/s more at launch can save weeks. Mars's orbit is also oval, and in some
    years Mars is nearer.

**6.** (intermediate) Why would a crew on a cheap trip have to wait about 15 months at Mars?

??? note "Answer"
    When they arrive, the Earth is about 75° ahead of Mars. For a cheap trip home it must be 75° behind. The Earth
    needs about 454 days to gain the 210° that takes.

**7.** (advanced) Find the Hohmann trip time from the Earth to Venus, at 0.723 AU.

??? note "Answer"
    $a = (1 + 0.723)/2 = 0.8615$ AU. Half of $0.8615^{1.5} = 0.800$ years is 0.400 years, about **146 days**.

**8.** (expert) Leaving from 200 km above the Earth ($v_c = 7.78$ km/s, $v_e = 11.01$ km/s) on a Hohmann path to
Mars, how big is the burn?

??? note "Answer"
    $\sqrt{2.94^2 + 11.01^2} - 7.78 = 11.40 - 7.78 = 3.62$ km/s, about the same as from 300 km.

## Summary

- A spacecraft leaves for Mars going a little faster than the Earth, in the same direction, and the Sun's pull curves
  it outwards.
- Walter Hohmann's half-ellipse of 1925 is the cheapest path: 2.94 km/s extra at the Earth, 2.65 km/s at Mars, and
  259 days.
- Mars must be 44° ahead at launch, so windows come every 780 days, about 26 months. In 2026, MMX and ESCAPADE left in
  the same window.
- Firing low, where the spacecraft moves fastest, saves fuel: 3.6 km/s from low orbit instead of 6.1. This is the
  Oberth effect.
- A little extra speed cuts months off the trip but means arriving faster. Porkchop plots show the trade.
- Spacecraft are tracked and steered all the way; Curiosity landed within 2.4 km of its target.
- A cheap round trip means about 15 months waiting at Mars and about 2.7 years in all.
- Leaving Mars orbit for home takes only about 2.1 km/s, but no spacecraft has yet done it.

**Next:** chapter 16, Gravity assists, where a spacecraft steals speed from a planet it flies past, the trick that
took the Voyagers to the outer planets and that ESCAPADE is using at the Earth right now.

## Further reading

- Walter Hohmann, *The Attainability of Heavenly Bodies*, NASA Technical Translation F-44, 1960, the English version of
  his 1925 book, free from [NASA's Technical Reports Server](https://ntrs.nasa.gov/citations/19980230631).
