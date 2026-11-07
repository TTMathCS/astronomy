# 5. Brighter and fainter: the inverse square law

*Walk away from a lamp and it looks fainter. This chapter shows exactly how much fainter, and why: light spreads out
over a bigger and bigger area, so twice as far means a quarter as bright. It follows the rule from Kepler to the first
light meters, shows how Huygens used it to guess the distance of Sirius and how Henrietta Leavitt's stars turned it
into a ruler for the universe, and works out how much sunlight reaches each planet. On Mars it explains why solar
rovers die in dust storms, and why the newest rovers run on nuclear power. It ends by weighing the Sun's whole output
from a single number.*

!!! abstract "In this chapter"
    **You will learn:**

    - why light gets weaker with the square of the distance
    - how much sunlight reaches each planet
    - who found the rule, and the first measurements of brightness
    - how Huygens estimated the distance of a star with holes in a screen
    - what a standard candle is, and how Leavitt's stars measured the universe
    - what else follows the same rule
    - why sunlight at Mars changes so much through its year, and what that means for rovers
    - how to use the rule in calculations
    - how to work out the total power of the Sun

    **You need:** chapters 1 and 4. Book 1, [chapter 4](../night-sky/04-How-Bright-Is-a-Star.md), explains star
    magnitudes.

    **Levels:** 5.1 to 5.3 are beginner; 5.4 to 5.7 are intermediate; 5.8 is advanced; 5.9 is expert.

## 5.1 Light spreads out { #spread }

A small lamp sends its light out in straight lines in every direction. Think of the light that falls on one square
at a distance of 1 metre. Go twice as far, and the same light has spread over a square twice as wide and twice as
tall: four times the area. Three times as far, it covers nine times the area.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Light from a small lamp spreading out in straight lines. At distance 1 it covers one square; at distance 2 the same light covers a square twice as wide, which is 4 of the small squares; at distance 3 it covers a square three times as wide, 9 small squares. So each small square gets one quarter of the light at twice the distance and one ninth at three times the distance.">
  <circle cx="24" cy="80" r="5" fill="#eea66f"/>
  <line x1="90" y1="71.0" x2="90" y2="89.0" stroke="currentColor" stroke-width="2"/>
  <line x1="156" y1="62.0" x2="156" y2="98.0" stroke="currentColor" stroke-width="2"/>
  <line x1="222" y1="53.0" x2="222" y2="107.0" stroke="currentColor" stroke-width="2"/>
  <line x1="24" y1="80" x2="222" y2="53.0" stroke="#eea66f" stroke-width="0.8"/>
  <line x1="24" y1="80" x2="222" y2="107.0" stroke="#eea66f" stroke-width="0.8"/>
  <rect x="83.5" y="140.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.68" stroke="currentColor" stroke-width="0.5"/>
  <rect x="143.0" y="140.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.23" stroke="currentColor" stroke-width="0.5"/>
  <rect x="143.0" y="153.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.23" stroke="currentColor" stroke-width="0.5"/>
  <rect x="156.0" y="140.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.23" stroke="currentColor" stroke-width="0.5"/>
  <rect x="156.0" y="153.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.23" stroke="currentColor" stroke-width="0.5"/>
  <rect x="202.5" y="140.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="0.5"/>
  <rect x="202.5" y="153.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="0.5"/>
  <rect x="202.5" y="166.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="0.5"/>
  <rect x="215.5" y="140.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="0.5"/>
  <rect x="215.5" y="153.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="0.5"/>
  <rect x="215.5" y="166.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="0.5"/>
  <rect x="228.5" y="140.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="0.5"/>
  <rect x="228.5" y="153.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="0.5"/>
  <rect x="228.5" y="166.0" width="13" height="13" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="0.5"/>
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">The same light spreads over a bigger area</text>
    <text x="16" y="96">lamp</text>
    <text x="90" y="65.0" text-anchor="middle">distance 1</text>
    <text x="90" y="193" text-anchor="middle">1 square</text>
    <text x="90" y="205" text-anchor="middle">all of it</text>
    <text x="156" y="56.0" text-anchor="middle">distance 2</text>
    <text x="156" y="193" text-anchor="middle">4 squares</text>
    <text x="156" y="205" text-anchor="middle">1/4 each</text>
    <text x="222" y="47.0" text-anchor="middle">distance 3</text>
    <text x="222" y="193" text-anchor="middle">9 squares</text>
    <text x="222" y="205" text-anchor="middle">1/9 each</text>
    <text x="6" y="232">Twice as far: a quarter as bright. Three times as far: a ninth.</text>
  </g>
</svg>
</div>

*Figure A. The same light covers 1, 4 and 9 squares at distances 1, 2 and 3.*

So the brightness, the light falling on each square metre, goes down as one over the square of the distance:

$$\text{brightness} \propto \frac{1}{d^2}.$$

This is the **inverse square law**. Twice as far, a quarter as bright; ten times as far, a hundredth. To make
something half as bright you need to go only 1.4 times as far, since $1.4^2 \approx 2$.

The rule is exact for a small source that sends light equally in all directions, with nothing in the way. The Sun and
the stars are so far away that they count as small sources.

??? note "Sources"
    - The intensity of light from a point source inversely proportional to the square of the distance, doubling the
      distance giving one quarter, and the factor 1.4 to halve it: Wikipedia,
      [Inverse-square law](https://en.wikipedia.org/wiki/Inverse-square_law) (weaker).

## 5.2 Sunlight across the solar system { #planets }

At the Earth's average distance from the Sun, 1 astronomical unit (AU), sunlight brings **1,361 watts** to each square
metre facing it. Mars is 1.52 AU from the Sun, so it gets $1 / 1.52^2$ of that, about 43 per cent: 586 W. Jupiter,
5.2 AU away, gets only 50 W, and Neptune, 30 AU away, gets 1.5 W.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Bars showing how much sunlight falls on each square metre at each planet, on a scale where each step is ten times more: Mercury 9,083 watts, Venus 2,601, Earth 1,361, Mars 586, Jupiter 50, Saturn 15, Uranus 3.7 and Neptune 1.5 watts per square metre.">
  <g font-size="8" fill="currentColor">
    <rect x="64" y="34" width="197.9" height="14" fill="#cfc8bf"/>
    <text x="60" y="44" text-anchor="end">Mercury</text>
    <text x="265.9" y="44">9,083</text>
    <rect x="64" y="56" width="170.8" height="14" fill="#cfc8bf"/>
    <text x="60" y="66" text-anchor="end">Venus</text>
    <text x="238.8" y="66">2,601</text>
    <rect x="64" y="78" width="156.7" height="14" fill="#5aa0d8"/>
    <text x="60" y="88" text-anchor="end">Earth</text>
    <text x="224.7" y="88">1,361</text>
    <rect x="64" y="100" width="138.4" height="14" fill="#c1440e"/>
    <text x="60" y="110" text-anchor="end">Mars</text>
    <text x="206.4" y="110">586</text>
    <rect x="64" y="122" width="85.1" height="14" fill="#cfc8bf"/>
    <text x="60" y="132" text-anchor="end">Jupiter</text>
    <text x="153.1" y="132">50</text>
    <rect x="64" y="144" width="58.5" height="14" fill="#cfc8bf"/>
    <text x="60" y="154" text-anchor="end">Saturn</text>
    <text x="126.5" y="154">15</text>
    <rect x="64" y="166" width="28.4" height="14" fill="#cfc8bf"/>
    <text x="60" y="176" text-anchor="end">Uranus</text>
    <text x="96.4" y="176">3.7</text>
    <rect x="64" y="188" width="8.9" height="14" fill="#cfc8bf"/>
    <text x="60" y="198" text-anchor="end">Neptune</text>
    <text x="76.9" y="198">1.5</text>
    <line x1="64" y1="210" x2="64" y2="214" stroke="currentColor" stroke-width="0.7"/>
    <text x="64" y="224" text-anchor="middle">1</text>
    <line x1="114" y1="210" x2="114" y2="214" stroke="currentColor" stroke-width="0.7"/>
    <text x="114" y="224" text-anchor="middle">10</text>
    <line x1="164" y1="210" x2="164" y2="214" stroke="currentColor" stroke-width="0.7"/>
    <text x="164" y="224" text-anchor="middle">100</text>
    <line x1="214" y1="210" x2="214" y2="214" stroke="currentColor" stroke-width="0.7"/>
    <text x="214" y="224" text-anchor="middle">1,000</text>
    <line x1="264" y1="210" x2="264" y2="214" stroke="currentColor" stroke-width="0.7"/>
    <text x="264" y="224" text-anchor="middle">10,000</text>
    <line x1="64" y1="210" x2="264" y2="210" stroke="currentColor" stroke-width="0.7"/>
    <text x="6" y="12">Sunlight on each square metre, in watts</text>
    <text x="6" y="22">(each step is ten times more)</text>
    <text x="164" y="238" text-anchor="middle">watts per square metre</text>
  </g>
</svg>
</div>

*Figure B. Sunlight on each square metre at each planet. Each step on the scale is ten times more.*

??? note "Sources"
    - Solar irradiance at each planet, from 9,082.7 W/m² at Mercury to 1.508 W/m² at Neptune: NASA,
      [Mercury](https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html),
      [Venus](https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html),
      [Earth](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html),
      [Mars](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html),
      [Jupiter](https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html),
      [Saturn](https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturnfact.html),
      [Uranus](https://nssdc.gsfc.nasa.gov/planetary/factsheet/uranusfact.html) and
      [Neptune](https://nssdc.gsfc.nasa.gov/planetary/factsheet/neptunefact.html) fact sheets.
    - The distances in AU: the semi-major axes on the same fact sheets divided by the Earth's 149.598 million km.

## 5.3 Finding the rule { #history }

- **Kepler, 1604.** In his book on optics, Johannes Kepler argued that light spreading from a point source gets
  weaker with the square of the distance.
- **Bullialdus, 1645.** The French astronomer Ismaël Bullialdus suggested that gravity weakens with distance in the
  same way. Newton later made this his law of gravity (book 3).
- **Bouguer, 1729.** The French scientist Pierre Bouguer made some of the earliest measurements of brightness. He found
  sunlight to be 300,000 times as strong as moonlight, and he measured how much light is lost passing
  through the air.
- **Lambert, 1760.** In his book *Photometria*, Johann Heinrich Lambert, from Mulhouse in Alsace, set out the rules: the
  light falling on a surface goes up with the strength of the source and down with the square of its distance.

Measuring brightness is called **photometry**.

??? note "Sources"
    - Kepler's *Ad Vitellionem paralipomena* of 1604, proposition 9, and Bullialdus's suggestion of 1645 for
      gravitation: Wikipedia, [Inverse-square law](https://en.wikipedia.org/wiki/Inverse-square_law) (weaker).
    - Bouguer's *Essai d'optique sur la gradation de la lumière* of 1729, the loss of light through the atmosphere,
      and the Sun 300,000 times as intense as the Moon: Wikipedia,
      [Pierre Bouguer](https://en.wikipedia.org/wiki/Pierre_Bouguer) (weaker).
    - Lambert's *Photometria* of 1760: Wikipedia,
      [Johann Heinrich Lambert](https://en.wikipedia.org/wiki/Johann_Heinrich_Lambert) (weaker).

## 5.4 Huygens and the distance of Sirius { #huygens }

How far away are the stars? In the 1690s Christiaan Huygens had an idea. Suppose Sirius is really a sun, just as
bright as ours. Then it looks so faint only because it is so far away, and the inverse square law tells us how far.

To compare the two, he let sunlight through a hole in a screen and made the hole smaller and smaller, until the
light coming through looked as bright as Sirius. The hole then showed only 1/27,664 of the Sun's width. So Sirius, he
reasoned, must be roughly 28,000 times as far away as the Sun (section 5.9). He published this in his book
*Cosmotheoros*, in 1698.

His answer was about 20 times too small. Partly his guess was wrong: Sirius gives out about 24 times as much light as
the Sun. But the method was right, and the idea behind it, comparing how bright a thing looks with how bright it
really is, is still how astronomers measure the greatest distances.

??? note "Sources"
    - Huygens's holes in a screen, 1/27,664 of the Sun's diameter, the assumption that Sirius is as luminous as the
      Sun, the result of about 30,000 times as far, and *Cosmotheoros* of 1698: Wikipedia,
      [Christiaan Huygens](https://en.wikipedia.org/wiki/Christiaan_Huygens) (weaker).
    - Sirius at 2.64 parsecs, absolute magnitude 1.4 against the Sun's 4.83: book 1,
      [chapter 4, section 4.10](../night-sky/04-How-Bright-Is-a-Star.md#working), and its sources. "About 20 times" and
      "about 24 times" are worked out in section 5.9.

## 5.5 Standard candles { #candles }

If you know how much light something really gives out, its **luminosity**, then how bright it looks tells you how far
away it is. An object like that is called a **standard candle**.

The first good standard candles were found by **Henrietta Swan Leavitt**, who worked at Harvard College Observatory as
a "computer", measuring the brightness of stars on photographs. Many of the plates she studied were taken at Harvard's
station in Arequipa, Peru, and showed the Magellanic Clouds, two small neighbouring galaxies. She found 1,777 variable
stars.

Among them were **Cepheids**, stars that swell and shrink, brightening and fading in a regular rhythm. In 1908 she
noticed that the brighter ones had longer periods, and in 1912 she showed it clearly with 25 Cepheids in the Small
Magellanic Cloud. Her key insight: all the stars in that cloud are at roughly the same distance from us, so the ones
that look brighter really are brighter. So a Cepheid's period tells you its luminosity, and its luminosity and its
brightness tell you its distance.

In 1925 Edwin Hubble found Cepheids in the Andromeda "nebula" and showed that it lies far outside our Milky Way. It is
a separate galaxy, now known to be about 2.5 million light-years away. Leavitt's stars had shown that the universe is
full of galaxies.

??? note "Sources"
    - Leavitt at Harvard College Observatory as a computer, the plates from Arequipa, Peru, 1,777 variables, the
      brighter variables having longer periods in 1908, the 25 Cepheids of 1912, and the stars of the Small Magellanic
      Cloud at the same distance: Wikipedia,
      [Henrietta Swan Leavitt](https://en.wikipedia.org/wiki/Henrietta_Swan_Leavitt) (weaker).
    - Cepheids as standard candles: Wikipedia, [Cepheid variable](https://en.wikipedia.org/wiki/Cepheid_variable)
      (weaker).
    - Hubble's Cepheids in Andromeda in 1925, and its distance of about 2.5 million light-years: Wikipedia,
      [Andromeda Galaxy](https://en.wikipedia.org/wiki/Andromeda_Galaxy) (weaker).

## 5.6 Not only light { #other }

Anything that spreads out evenly from a point in all directions weakens in the same way:

- **Gravity.** Newton's law of gravity is an inverse square law (book 3).
- **Electric forces** between charges.
- **Sound** from a small source in open air.
- **Radio signals** from a spacecraft. When Mars is on the far side of the Sun, 401.4 million km away, its signals
  reaching the Earth are $(401.4/54.6)^2 = 54$ times weaker than at its closest, 54.6 million km away. Big dishes,
  like the Deep Space Network's 70 m ones, collect more of the faint signal (chapter 2, section 2.9).

A beam that does not spread, like a laser, does not follow the rule in the same simple way.

??? note "Sources"
    - Gravitation, electricity, light, sound and radiation following inverse square laws: Wikipedia,
      [Inverse-square law](https://en.wikipedia.org/wiki/Inverse-square_law) (weaker).
    - Mars's nearest and farthest distances: NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html). The 54 is our arithmetic.

## 5.7 Sunlight and power on Mars { #mars }

- **Less light.** On average Mars gets 586 W of sunlight on each square metre, 43 per cent of the Earth's 1,361 W.
- **A big swing through the year.** Mars's orbit is more oval than the Earth's. At its closest to the Sun it is
  206.7 million km away and gets about 713 W; at its farthest, 249.3 million km, about 490 W. That is 45 per cent
  more at the closest than at the farthest. The Earth's swing is only 7 per cent (section 5.8).
- **Dust on the panels.** Solar rovers and landers must also fight dust. **Opportunity**, planned to last 90 sols,
  kept going for 5,111. But in early June 2018 a dust storm covered the whole planet, and within a few days its panels
  could not make enough power to talk to the Earth. Its last contact was on 10 June 2018. The lander **InSight**
  depended on gusts of wind to clean its panels; as dust built up, it ran out of power, and its mission ended in
  December 2022.
- **Nuclear power.** Curiosity and Perseverance do not use solar panels. Each carries a generator that turns the heat
  of decaying plutonium-238 into electricity. It needs no sunlight, so it works day and night and through dust
  storms.

??? note "Sources"
    - Solar irradiance at Mars, 586.2 W/m², perihelion 206.650 and aphelion 249.261 million km: NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html). The 713 W and 490 W are worked
      out in section 5.8.
    - Opportunity's 90 planned sols and 5,111 sols, the planet-wide dust storm of June 2018, and the last contact on
      10 June 2018: Wikipedia, [Opportunity (rover)](https://en.wikipedia.org/wiki/Opportunity_(rover)) (weaker).
    - InSight's solar panels and "cleaning events", the dust, and the end of the mission declared on 21 December 2022:
      Wikipedia, [InSight](https://en.wikipedia.org/wiki/InSight) (weaker).
    - The generator on Curiosity and Perseverance, turning heat from plutonium-238 into electricity: Wikipedia,
      [Multi-mission radioisotope thermoelectric generator](https://en.wikipedia.org/wiki/Multi-mission_radioisotope_thermoelectric_generator)
      (weaker).

## 5.8 Working it out { #working }

**Comparing two distances.** If one place is $d$ times as far from a source as another, it gets $1/d^2$ as much light:

$$F = F_\text{Earth} \times \left(\frac{1 \text{ AU}}{d}\right)^2.$$

- Mars on average: $227.956 / 149.598 = 1.524$ AU, so $1361 / 1.524^2 = 586$ W/m², just what NASA gives.
- Mars at its closest: $1361 \times (149.598 / 206.650)^2 = 713$ W/m².
- Mars at its farthest: $1361 \times (149.598 / 249.261)^2 = 490$ W/m².
- Jupiter: $778.479 / 149.598 = 5.204$ AU, so $1361 / 5.204^2 = 50.3$ W/m².

**In magnitudes.** Bouguer's 300,000 between the Sun and the Moon is $2.5 \log_{10} 300{,}000 = 13.7$ magnitudes.
The modern figure for the full Moon is 14.0 magnitudes, about 400,000 times (book 1, chapter 4, section 4.10).

| | Mars | Earth |
| --- | --- | --- |
| Average distance from the Sun | 227.956 million km, 1.524 AU | 149.598 million km, 1 AU |
| Sunlight on average | 586 W/m² | 1,361 W/m² |
| Sunlight at the closest point of the orbit | 713 W/m² | 1,408 W/m² |
| Sunlight at the farthest point | 490 W/m² | 1,317 W/m² |
| Swing through the year | 45 per cent | 7 per cent |

??? note "Sources"
    - Distances: NASA, [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html),
      [Earth Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html) (perihelion 147.095 and
      aphelion 152.100 million km) and
      [Jupiter Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html).
    - The arithmetic is ours.

## 5.9 Weighing the Sun's light { #luminosity }

**The Sun's total power.** Imagine a huge sphere round the Sun, 1 AU in radius. All the Sun's light passes through it,
and every square metre of it gets 1,361 W. So the Sun's total output, its **luminosity**, is

$$L = 4\pi d^2 F = 4\pi \times (1.496 \times 10^{11})^2 \times 1361 = 3.83 \times 10^{26} \text{ W},$$

matching NASA's $382.8 \times 10^{24}$ W. Do the same at Mars, with $d = 2.280 \times 10^{11}$ m and $F = 586.2$
W/m², and you get the same $3.83 \times 10^{26}$ W, as you should.

**Distance from luminosity.** Turn the formula round:

$$d = \sqrt{\frac{L}{4\pi F}}.$$

Measure $F$, know $L$, and you have $d$. That is how a standard candle works.

**Huygens's sum.** The hole let through a disc of sunlight $1/27{,}664$ of the Sun's width, so its area, and its
light, was $1/27{,}664^2$ of the Sun's. A sun just like ours would look that faint at $27{,}664$ times the Sun's
distance, since $1/d^2 = 1/27{,}664^2$. That is 27,664 AU, or 0.44 light-years.

In fact Sirius is 2.64 parsecs away, $2.64 \times 206{,}265 = 545{,}000$ AU, which is $545{,}000 / 27{,}664 = 20$
times farther. Part of the reason is its luminosity. From book 1, Sirius's absolute magnitude is 1.4 and the Sun's
4.83, so Sirius is $10^{0.4 \times 3.43} = 24$ times as luminous. A star 24 times as bright must be $\sqrt{24} = 4.9$
times as far away to look the same. The rest of Huygens's error came from judging by eye when his hole matched Sirius.

??? note "Sources"
    - The Sun's luminosity, $382.8 \times 10^{24}$ J/s: NASA,
      [Sun Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html).
    - 1,361 W/m², 586.2 W/m² and the distances: NASA fact sheets, section 5.2.
    - Huygens's 1/27,664: section 5.4. Sirius's distance and magnitudes: book 1, chapter 4.
    - The arithmetic is ours.

## Check yourself { #check }

**1.** (beginner) You move three times as far from a lamp. How bright does it look now?

??? note "Answer"
    $1/3^2 = 1/9$ as bright.

**2.** (beginner) Why does Mars get less sunlight than the Earth?

??? note "Answer"
    It is about 1.52 times as far from the Sun, so the sunlight has spread over $1.52^2 = 2.3$ times the area.

**3.** (beginner) What did Henrietta Leavitt discover about Cepheids?

??? note "Answer"
    The brighter Cepheids have longer periods, so a Cepheid's period tells you how much light it really gives out.

**4.** (intermediate) What is a standard candle, and how does it give a distance?

??? note "Answer"
    Something whose true luminosity is known. Comparing that with how bright it looks, using the inverse square law,
    gives its distance.

**5.** (intermediate) Why did Opportunity stop working in 2018?

??? note "Answer"
    A planet-wide dust storm blocked the sunlight, and its solar panels could not make enough power to keep it in
    touch with the Earth.

**6.** (intermediate) Saturn is 9.57 AU from the Sun. How much sunlight falls on each square metre there?

??? note "Answer"
    $1361 / 9.57^2 = 14.9$ W/m², close to NASA's 14.82.

**7.** (advanced) A rover's solar panels make 900 watt-hours a day when Mars is at its farthest from the Sun. Ignoring
dust and seasons, about how much would they make at its closest?

??? note "Answer"
    $900 \times 1.455 = 1{,}310$ watt-hours, using $(249.261 / 206.650)^2 = 1.455$.

**8.** (expert) Neptune gets 1.508 W/m². Use this and the Sun's luminosity, $3.83 \times 10^{26}$ W, to find Neptune's
distance from the Sun in AU.

??? note "Answer"
    $d = \sqrt{3.83 \times 10^{26} / (4\pi \times 1.508)} = 4.50 \times 10^{12}$ m, which is
    $4.50 \times 10^{12} / 1.496 \times 10^{11} = 30.0$ AU.

## Summary

- Light from a small source spreads over an area that grows with the square of the distance, so brightness falls as
  $1/d^2$.
- Sunlight ranges from 9,083 W/m² at Mercury to 1.5 W/m² at Neptune; Mars gets 586 W/m², 43 per cent of the Earth's.
- Kepler stated the rule in 1604; Bouguer and Lambert began measuring brightness in the 1700s.
- Huygens used it in 1698 to estimate the distance of Sirius, assuming it was a sun like ours.
- Leavitt's Cepheids became standard candles, and in 1925 Hubble used them to show that Andromeda is a separate galaxy.
- Gravity, electric forces, sound and radio signals follow the same rule.
- Sunlight at Mars swings by 45 per cent through its year; dust ended Opportunity and InSight, and Curiosity and
  Perseverance run on nuclear power.
- The Sun's luminosity is $4\pi d^2 F = 3.83 \times 10^{26}$ W.

**Next:** chapter 6, Hot things glow, where we see how the colour of a star tells its temperature.

## Further reading

- Marcia Bartusiak, *The Day We Found the Universe*, Pantheon, 2009.
