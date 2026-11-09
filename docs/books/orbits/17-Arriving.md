# 17. Arriving

*After months in space, a spacecraft reaches Mars much too fast to stop. Mars's pull speeds it up as it falls in, and
unless it loses speed at just the right moment, it swings past and is gone for good. This chapter shows the three ways
to arrive: braking with the engine, dipping into the top of the air again and again, and diving straight in to land.
It tells how each has worked, how one orbiter was lost by a mix-up of units, and why Mars is the hardest of the three
nearby worlds to land on.*

!!! abstract "In this chapter"
    **You will learn:**

    - why a spacecraft arriving at Mars must lose speed, and how much
    - why being caught into a long ellipse costs much less than going straight into a low orbit
    - how aerobraking uses Mars's thin upper air to shrink an orbit over months
    - what aerocapture is, and why nobody has tried it at a planet yet
    - what happens in the seven minutes of a landing on Mars
    - how the Mars Climate Orbiter was lost in 1999
    - why landing on Mars is harder than landing on the Earth or the Moon
    - how to work out the braking needed to be caught into any orbit

    **You need:** chapters 7, 15 and 16.

    **Levels:** 17.1 to 17.3 are beginner; 17.4 to 17.7 are intermediate; 17.8 is advanced; 17.9 is expert.

## 17.1 Too fast to stop { #catch }

A spacecraft on the cheap road of chapter 15 reaches Mars's orbit going 2.65 km/s slower than Mars, so Mars comes up
from behind at **2.65 km/s**. Then Mars's pull takes over. As the spacecraft falls towards the planet it speeds up, and
300 km above the ground it is doing about **5.5 km/s**.

Escape speed there is 4.8 km/s (chapter 7). The spacecraft is going faster than that, so if nothing is done it simply
swings round Mars, like a flyby in chapter 16, and leaves. To stay, it must lose speed close to Mars, where it is
moving fastest. There are three ways to do it:

1. **Fire the engine** backwards, an **orbit insertion burn**.
2. **Dip into the air**, a little at a time, called **aerobraking**, after a first burn has caught it.
3. **Dive straight in** and land, letting the air take most of the speed.

??? note "Sources"
    - 2.65 km/s and the speed of 5.50 km/s at 300 km: chapter 15, sections 15.2 and 15.9, our arithmetic. Escape speed
      of 4.81 km/s at 300 km: our arithmetic with Mars's $GM$ from the NASA
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - A spacecraft that does not slow down leaving again: chapter 16, standard.

## 17.2 Braking with the engine { #engine }

The braking burn is the most nervous moment of an orbiter's mission. It has to start at the right second, point the
right way and stop at the right speed, and it happens so far away that radio takes several minutes to bring the news.
Nobody on the Earth can help; the spacecraft does it alone.

**Be caught loosely.** How much the burn must take off depends on the orbit you want. With 5.5 km/s at 300 km up:

| Orbit after the burn | Burn needed |
| --- | --- |
| Circle 300 km up | 2.09 km/s |
| 300 km by 45,000 km, about 35 hours | 0.86 km/s |
| Only just caught, the far point very far away | 0.68 km/s |

Going straight into a low circle costs more than twice as much as being caught into a long ellipse. This is the Oberth
effect of chapter 15 again: braking where the spacecraft is fastest is worth the most, and a long ellipse keeps its
low point close to Mars. So most orbiters are first caught into a long ellipse, and shrink it later.

Some arrivals:

- **Mariner 9** reached Mars on 14 November 1971 and became the **first spacecraft to orbit another planet**, narrowly
  beating the Soviet Mars 2 and Mars 3. Dust storms hid the ground for months before it could send back clear pictures.
- **India's Mars Orbiter Mission** had coasted for ten months since leaving the Earth. On 22 September 2014 the team
  test-fired its main engine for just under 4 seconds, about 41 hours before the real burn. It worked, and on 24
  September the craft was caught into the long ellipse of chapter 14.
- **NASA's Mars Reconnaissance Orbiter**, on 10 March 2006, was caught into an orbit 426 by 44,500 km above Mars,
  taking 35.5 hours. Its burn was so accurate that the speed change was only 0.01% short of the design.
- **The Emirates' Hope**, on 9 February 2021, fired its thrusters for about 27 minutes to be caught by Mars.

??? note "Sources"
    - The burns in the table: our arithmetic, section 17.9. The same 0.85 km/s and 2.09 km/s appear in this site's
      physics lesson
      [Aerobraking and aerocapture](https://physics.akadian.ca/topics/rockets/level-8/04-aerobraking-and-aerocapture.html).
    - Mariner 9 reaching Mars on 14 November 1971, the first spacecraft to orbit another planet, narrowly beating Mars 2
      and Mars 3, and the dust storms: Wikipedia, [Mariner 9](https://en.wikipedia.org/wiki/Mariner_9) (weaker).
    - The Mars Orbiter Mission's 440 N engine test-fired on 22 September 2014 for 3.968 s, about 41 hours before
      insertion, and in orbit on 24 September 2014: Wikipedia,
      [Mars Orbiter Mission](https://en.wikipedia.org/wiki/Mars_Orbiter_Mission) (weaker). Ten months: from
      30 November 2013 to September 2014, chapter 15.
    - MRO arriving on 10 March 2006; 426 by 44,500 km, about 35.5 hours; the change in speed only 0.01% short:
      Wikipedia, [Mars Reconnaissance Orbiter](https://en.wikipedia.org/wiki/Mars_Reconnaissance_Orbiter) (weaker).
    - Hope's insertion on 9 February 2021, about 27 minutes of thrust: Wikipedia,
      [Emirates Mars Mission](https://en.wikipedia.org/wiki/Emirates_Mars_Mission) (weaker).
    - Radio delays of several minutes: chapter 12 and standard.

## 17.3 Dipping into the air { #aerobraking }

Mars has a thin atmosphere, and its very top reaches out more than 100 km. An orbiter in a long ellipse can lower its
low point into that thin air. On each pass the air drags on it a little, so it leaves the low point a few metres a
second slower. That lowers the far point of the next orbit. Pass after pass, month after month, the long ellipse
shrinks towards a circle. At the end, a small burn lifts the low point back out of the air. This is **aerobraking**,
and figure A shows it for the Mars Reconnaissance Orbiter.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Mars Reconnaissance Orbiter's orbit shrinking by aerobraking, drawn to scale. Mars is a small disc at the right. The first orbit after arrival in March 2006 is a long thin ellipse reaching 44,500 km out to the left, taking 35.5 hours. Smaller ellipses inside it show the orbit as each dip into the top of Mars's air takes away a little speed: its low point stays near Mars while its far point comes in, through 20,000, 10,000 and 4,000 km, until the final nearly circular orbit about 250 to 316 km up, taking 112 minutes. The low point of every orbit is on the right, where the craft dips into the air.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">Aerobraking: the Mars Reconnaissance Orbiter, 2006, to scale</text>
    <ellipse cx="172.2" cy="112" rx="150.0" ry="78.5" fill="none" stroke="#5aa0d8" stroke-width="1.1"/>
    <text x="24.2" y="115" fill="#5aa0d8">far point</text>
    <ellipse cx="242.3" cy="112" rx="78.0" ry="52.5" fill="none" stroke="#555" stroke-width="0.6"/>
    <ellipse cx="271.3" cy="112" rx="49.0" ry="39.8" fill="none" stroke="#555" stroke-width="0.6"/>
    <ellipse cx="288.7" cy="112" rx="31.6" ry="29.5" fill="none" stroke="#555" stroke-width="0.6"/>
    <ellipse cx="300.0" cy="112" rx="21.3" ry="21.3" fill="none" stroke="#c1440e" stroke-width="1.3"/>
    <circle cx="300" cy="112" r="19.7" fill="#c1440e" fill-opacity="0.85"/>
    <text x="166.3" y="108" fill="#555">20,000</text>
    <text x="224.3" y="108" fill="#555">10,000</text>
    <text x="259.1" y="108" fill="#555">4,000</text>
    <text x="300" y="115" text-anchor="middle" fill="#fff">Mars</text>
    <text x="334" y="22" text-anchor="end">the low point, about 100 km up,</text>
    <text x="334" y="31" text-anchor="end">dips into the air on every orbit</text>
    <line x1="312" y1="34" x2="320" y2="106" stroke="currentColor" stroke-width="0.5"/>
    <text x="12" y="203" fill="#5aa0d8">First orbit: 426 by 44,500 km above Mars, 35.5 hours.</text>
    <text x="12" y="213" fill="#c1440e">Final orbit: about 250 to 316 km up, 112 minutes.</text>
    <text x="6" y="226">Each pass through the thin top of the air takes off a few metres a second. That lowers the far</text>
    <text x="6" y="235">point of the next orbit, so the ellipse shrinks towards a circle. More than 400 passes over</text>
    <text x="6" y="244">about five months did a job that would otherwise have needed over 1 km/s of braking by engine.</text>
  </g>
</svg>
</div>

To do the same with its engine, MRO would have needed about 1.24 km/s more, and with typical orbiter engines that is
about a third of the spacecraft's mass in extra fuel.

**How it began.** Japan's **Hiten** tested the idea at the Earth on 19 March 1991 (chapter 16). NASA's **Magellan** used
it at Venus in May 1993. The first spacecraft to use aerobraking as its main plan was **Mars Global Surveyor**.

**Mars Global Surveyor, 1997.** It arrived on 11 September 1997 in an orbit taking 45 hours, from 262 km to 54,026 km
above Mars, and lowered its low point to about 110 km. The plan was four months of aerobraking. But about a month in,
the team found that the push of the air was bending one of its two solar panels backwards. The panel had been damaged
slightly soon after launch. They had to brake much more gently, with a pause in the middle, and the far point did not
come down to 450 km until March 1999. The mapping began in April 1999, a year and a half after arrival.

The others learned from it:

| Orbiter | Aerobraking |
| --- | --- |
| Mars Global Surveyor | 1997 to 1999, with a pause |
| Mars Odyssey | about 76 days, ending in January 2002 |
| Mars Reconnaissance Orbiter | 2006, more than 400 passes, ending on 30 August |
| ESA's Trace Gas Orbiter | 11 months, March 2017 to February 2018 |

The Trace Gas Orbiter's aerobraking slowed it by 3,600 km/h and shrank its orbit from 98,000 by 200 km to 1,050 by
200 km. A few more burns made it a circle 400 km up, and its science began on 21 April 2018.

The danger is that Mars's upper air swells and shrinks from day to day with dust storms and sunshine. Dip too deep on
a day when it has swelled, and the spacecraft overheats. The team watches every pass and adjusts the low point with
small burns.

??? note "Sources"
    - Aerobraking: lowering the periapsis into the upper air, a little slowing on each pass, hundreds of passes over
      months, a final burn: Wikipedia, [Aerobraking](https://en.wikipedia.org/wiki/Aerobraking) (weaker), and this
      site's physics lesson Aerobraking and aerocapture (above), which also gives the 1.24 km/s, the third of the mass
      for engines with an exhaust speed of 3.1 km/s, more than 400 passes for MRO, and the swelling upper air.
    - Hiten on 19 March 1991, Magellan at Venus in May 1993, MGS in 1997 the first to use aerobraking as its main
      planned technique: Wikipedia, Aerobraking (above).
    - MGS: arrival on 11 September 1997; 45 hours, 262 by 54,026 km; about 110 km; four months planned; the bending
      solar panel, damaged soon after launch; aerobraking resumed from November 1998 to March 1999, down to 450 km;
      mapping from 1 April 1999: Wikipedia,
      [Mars Global Surveyor](https://en.wikipedia.org/wiki/Mars_Global_Surveyor) (weaker).
    - Mars Odyssey: about 76 days of aerobraking, ending in January 2002: Wikipedia,
      [2001 Mars Odyssey](https://en.wikipedia.org/wiki/2001_Mars_Odyssey) (weaker).
    - MRO lifting its periapsis out of the air on 30 August 2006 and its final orbit of 250 to 316 km and 112 minutes:
      Wikipedia, Mars Reconnaissance Orbiter (above).
    - TGO: in orbit on 19 October 2016; 11 months of aerobraking from March 2017 to February 2018; 3,600 km/h; 98,000 by
      200 km to 1,050 by 200 km; 400 km; science from 21 April 2018: Wikipedia,
      [Trace Gas Orbiter](https://en.wikipedia.org/wiki/Trace_Gas_Orbiter) (weaker).
    - Figure A: MRO's first and last orbits from Wikipedia (above); the in-between orbits are drawn to show the idea,
      not measured.

## 17.4 One deep dive: aerocapture { #aerocapture }

Why not let the air do the first braking too? In **aerocapture**, the spacecraft arrives behind a heat shield and
dives once, deep into the atmosphere, losing enough speed to be caught. It climbs out again into a long orbit, and a
small burn at the far point lifts its low point clear of the air. It would save most of the 0.86 km/s capture burn
and the months of aerobraking.

The catch is the **corridor**. Dive a little too shallow, and the spacecraft skips out and is not caught. Dive a
little too deep, and it burns up or hits the ground. So far, aerocapture has **not yet been tried at a planet**. The
nearest thing happened at the Earth: the Soviet Zond 6 and Zond 7, coming back from the Moon in 1968 and 1969, skipped
off the top of the air on their way in, which turned their open paths into closed ones before they came down.

??? note "Sources"
    - Aerocapture, the single pass, the small burn at the first apoapsis, never yet tried on a planetary mission, and
      Zond 6 and Zond 7 as aerocapture manoeuvres: Wikipedia,
      [Aerocapture](https://en.wikipedia.org/wiki/Aerocapture) (weaker). The years 1968 and 1969: standard.
    - The narrow corridor and the savings: the physics lesson Aerobraking and aerocapture (above).

## 17.5 Seven minutes { #landing }

A lander does not stop in orbit first. It comes straight in from its path across the solar system and hits the top of
the air, about 125 km up, at about **20,000 km/h**, 5.6 km/s. Seven minutes later it must be standing still on the
ground. Radio takes about 11 minutes to reach the Earth, so by the time anyone hears that the landing has begun, it
is already over, one way or the other. Figure B shows Perseverance's landing on 18 February 2021.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Perseverance's landing on 18 February 2021, plotted as speed against time on a scale where each step up is ten times faster. It entered the air 125 km up at about 20,000 km/h. Four minutes later the air and heat shield had slowed it to about 1,500 km/h, when the parachute opened 11 km up. At about 5 minutes 50 seconds, 2 km up and at about 320 km/h, it let go of the parachute and fired its engines. At 7 minutes it touched down at about 2.7 km/h, lowered on cables from a hovering sky crane.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">Perseverance's seven minutes, 18 February 2021</text>
    <line x1="52" y1="186.0" x2="320" y2="186.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="49" y="189.0" text-anchor="end">1</text>
    <line x1="52" y1="154.8" x2="320" y2="154.8" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="49" y="157.8" text-anchor="end">10</text>
    <line x1="52" y1="123.6" x2="320" y2="123.6" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="49" y="126.6" text-anchor="end">100</text>
    <line x1="52" y1="92.4" x2="320" y2="92.4" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="49" y="95.4" text-anchor="end">1,000</text>
    <line x1="52" y1="61.2" x2="320" y2="61.2" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="49" y="64.2" text-anchor="end">10,000</text>
    <line x1="52" y1="30.0" x2="320" y2="30.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="49" y="33.0" text-anchor="end">100,000</text>
    <text x="6" y="22">km/h</text>
    <line x1="52.0" y1="186" x2="52.0" y2="189" stroke="currentColor" stroke-width="0.6"/>
    <text x="52.0" y="197" text-anchor="middle">0</text>
    <line x1="90.3" y1="186" x2="90.3" y2="189" stroke="currentColor" stroke-width="0.6"/>
    <text x="90.3" y="197" text-anchor="middle">1</text>
    <line x1="128.6" y1="186" x2="128.6" y2="189" stroke="currentColor" stroke-width="0.6"/>
    <text x="128.6" y="197" text-anchor="middle">2</text>
    <line x1="166.9" y1="186" x2="166.9" y2="189" stroke="currentColor" stroke-width="0.6"/>
    <text x="166.9" y="197" text-anchor="middle">3</text>
    <line x1="205.1" y1="186" x2="205.1" y2="189" stroke="currentColor" stroke-width="0.6"/>
    <text x="205.1" y="197" text-anchor="middle">4</text>
    <line x1="243.4" y1="186" x2="243.4" y2="189" stroke="currentColor" stroke-width="0.6"/>
    <text x="243.4" y="197" text-anchor="middle">5</text>
    <line x1="281.7" y1="186" x2="281.7" y2="189" stroke="currentColor" stroke-width="0.6"/>
    <text x="281.7" y="197" text-anchor="middle">6</text>
    <line x1="320.0" y1="186" x2="320.0" y2="189" stroke="currentColor" stroke-width="0.6"/>
    <text x="320.0" y="197" text-anchor="middle">7</text>
    <text x="186.0" y="207" text-anchor="middle">minutes after entering the air</text>
    <rect x="52.0" y="180" width="153.1" height="6" fill="#eea66f"/>
    <rect x="205.1" y="180" width="70.2" height="6" fill="#5aa0d8"/>
    <rect x="275.3" y="180" width="44.7" height="6" fill="#c1440e"/>
    <text x="128.6" y="177" text-anchor="middle" fill="#555">heat shield and air</text>
    <text x="240.2" y="177" text-anchor="middle" fill="#555">parachute</text>
    <text x="297.7" y="177" text-anchor="middle" fill="#555">engines</text>
    <path d="M52.0,51.8 L205.1,86.9 L275.3,107.8 L320.0,172.5" fill="none" stroke="currentColor" stroke-width="0.8" stroke-dasharray="3 2"/>
    <circle cx="52.0" cy="51.8" r="2.6" fill="#c1440e"/>
    <text x="58.0" y="47.8" text-anchor="start">20,000 km/h: enters the air, 125 km up</text>
    <circle cx="205.1" cy="86.9" r="2.6" fill="#c1440e"/>
    <text x="211.1" y="82.9" text-anchor="start">1,500 km/h: parachute opens, 11 km up</text>
    <circle cx="275.3" cy="107.8" r="2.6" fill="#c1440e"/>
    <text x="269.3" y="119.8" text-anchor="end">320 km/h: backshell lets go, 2 km up</text>
    <circle cx="320.0" cy="172.5" r="2.6" fill="#c1440e"/>
    <text x="310.0" y="168.5" text-anchor="end">2.7 km/h: touchdown, lowered by a sky crane</text>
    <text x="6" y="226">Most of the speed went in the first four minutes, taken by the air and the heat shield, which</text>
    <text x="6" y="235">reached about 1,300 °C. The parachute took it from 1,500 to 320 km/h; rockets did the rest.</text>
    <text x="6" y="244">Dashes only join the four known points. Radio took 11 minutes to bring the news to Earth.</text>
  </g>
</svg>
</div>

- **Entry.** For four minutes the heat shield takes the heat, up to about 1,300 °C, while the air brakes the capsule.
  More than nine tenths of the speed is gone without a drop of fuel.
- **Parachute.** About 11 km up, at about 1,500 km/h, still faster than sound, a parachute 21.5 m across opens.
- **Rockets.** About 2 km up, at about 320 km/h, the lander drops the parachute and fires its engines.
- **Sky crane.** About 20 m up, the descent stage hovers and lowers the rover on cables. The cables are cut and the
  descent stage flies off to crash a safe distance away.

**Different ways down.** Every Mars landing has used a heat shield and a parachute. After that:

- **Legs and rockets**: Viking 1 in 1976, Phoenix, InSight on 26 November 2018, and China's **Zhurong** on 14 May 2021,
  which made China the second country to run a working spacecraft on Mars.
- **Airbags**: the lander bounces to a stop inside giant balloons, as Mars Pathfinder did in 1997 and the rovers Spirit
  and Opportunity in 2004.
- **Sky crane**: for rovers too heavy for airbags, Curiosity in 2012 and Perseverance in 2021.

The very first landing, by the Soviet **Mars 3** in December 1971, reached the ground safely but fell silent after
110 seconds.

**Aiming.** Landers are aimed at an oval on the map, the **landing ellipse**. For the rovers of 2004 it was about 80 km
long. Curiosity, steering its lift as it fell, cut it to about 20 by 7 km. Perseverance photographed the ground on the
way down, matched the pictures to a map, and steered to a safe spot, so it could be sent to Jezero crater, a site full
of cliffs and boulders that earlier landers could not have risked.

The physics lessons [Seven minutes](https://physics.akadian.ca/topics/rockets/level-4/04-seven-minutes.html) and
[Landing precision](https://physics.akadian.ca/topics/rockets/level-8/06-landing-precision.html) go through it step
by step.

??? note "Sources"
    - Perseverance's landing: 125 km and about 20,000 km/h; the heat shield near 1,300 °C; the parachute at about 11 km
      and 1,500 km/h, 21.5 m across; the backshell at about 2 km and 320 km/h; the sky crane at about 20 m; about
      seven minutes; 11 minutes of radio delay; more than nine tenths of the speed lost to the air: this site's
      physics lesson Seven minutes (above). 20,000 km/h is 5.6 km/s, our arithmetic, which matches a 2.65 km/s arrival
      (section 17.9).
    - All landings using an aeroshell and parachute, then airbags, legs or a sky crane; Mars 3 in 1971, the first
      successful landing, failing after 110 seconds; Zhurong landing on 14 May 2021: Wikipedia,
      [Mars landing](https://en.wikipedia.org/wiki/Mars_landing) (weaker). China the second country to operate a fully
      functional spacecraft on Mars: Wikipedia, [Zhurong (rover)](https://en.wikipedia.org/wiki/Zhurong_(rover))
      (weaker). InSight landed on 26 November 2018: Wikipedia, [InSight](https://en.wikipedia.org/wiki/InSight)
      (weaker). Which missions used which method: standard, and the history book, chapter 21.
    - Landing ellipses of about 80 km, 20 by 7 km and 7.7 by 6.6 km, guided entry and terrain-relative navigation,
      and Jezero's cliffs and boulders: this site's physics lesson Landing precision (above).

## 17.6 Arriving wrong: Mars Climate Orbiter { #mco }

Chapter 15 promised the full story. NASA's **Mars Climate Orbiter** was launched in December 1998. Like Mars Global
Surveyor, it was to be caught into a long orbit and then aerobrake for weeks, so its braking burn was planned for a
pass **226 km** above Mars on 23 September 1999.

On the way, small thruster firings nudged the spacecraft. Software from the builder, Lockheed Martin, reported the
size of each nudge in **pound-force seconds**. NASA's navigation software, which used those numbers to work out where
the spacecraft was, expected **newton-seconds**, 4.45 times bigger. So every nudge was counted as 4.45 times too
small, and the predicted path drifted away from the real one.

In the last week, the navigators saw that the pass might be lower than planned, perhaps 150 to 170 km. At least two of
them had noticed something wrong earlier, but their worries were dismissed because they had not filled in the right
form. The orbiter began its braking burn and was never heard from again. Working back afterwards, the team
found that it had passed only about **57 km** above the ground.

Why was 57 km fatal when 226 km was safe? Roughly, Mars's air gets thicker by a factor of about 2.7 for every 11 km
you go down. From 226 km down to 57 km is 169 km, about 15 of those steps, so the air was about **5 million times
thicker**. The spacecraft was destroyed, or perhaps skipped off back into orbit round the Sun.

NASA did not blame Lockheed Martin alone: its own checks and tests should have caught the mistake.

??? note "Sources"
    - Mars Climate Orbiter: weeks of aerobraking planned; insertion at 226 km on 23 September 1999; the thruster
      impulse in pound-force seconds and the trajectory software expecting newton-seconds, a factor of 4.45; the
      150–170 km estimate in the last week; two navigators' concerns dismissed for not following the rules about
      filling out a form; about 57 km; destroyed or back in orbit round the Sun; NASA's own failure to check: Wikipedia,
      [Mars Climate Orbiter](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) (weaker). The history book,
      [section 21.7](../history/21-The-Space-Age-at-Mars.md#hard), gives the outline. Launched in December 1998:
      standard.
    - Mars's scale height of 11.0 km: NASA, Mars Fact Sheet (above). The factor of 5 million: $e^{169/11} = 4.7$
      million, our arithmetic.

## 17.7 Mars, the Earth and the Moon { #mars }

Each of the three nearby worlds asks for a different way to land.

- **The Moon** has no air at all. There is nothing to slow you, but nothing to burn you either. Every bit of speed
  must be taken off by rockets.
- **The Earth** has thick air. A capsule coming home from the Moon is slowed by it from about 11 km/s, and parachutes
  alone can lower it gently into the sea.
- **Mars** has the worst of both. Its air is thick enough to heat a capsule like a meteor, so it needs a heat shield.
  But at the ground it is about sixty times thinner than the Earth's, so parachutes cannot slow a lander enough. Even
  Perseverance's huge parachute left it falling at about 320 km/h, and rockets had to do the rest.

**The tonne barrier.** Every Mars lander so far has weighed a tonne or less on the ground. A lander for people, carrying
their home or their rocket back, would weigh tens of tonnes. A heavier lander falls faster through the thin air, and a
40-tonne one would still be going faster than sound when it hit the ground. The answer planned is to light the landing
engines early, high up and still at two or three times the speed of sound: **supersonic retropropulsion**. Since 2014,
the first stages of SpaceX's Falcon 9 rockets, coming back down through the Earth's thin upper air, have done just
this, and NASA has studied those burns as practice for Mars.

The physics lessons
[Parachutes in thin air](https://physics.akadian.ca/topics/rockets/level-4/05-parachutes-in-thin-air.html) and
[Supersonic retropropulsion](https://physics.akadian.ca/topics/rockets/level-7/05-supersonic-retropropulsion.html)
work out the numbers.

??? note "Sources"
    - Mars's ground air about sixty times thinner than the Earth's; Perseverance's parachute leaving it at about
      320 km/h; parachutes unable to land a heavy lander: this site's physics lesson Parachutes in thin air (above).
    - Landers so far a tonne or less; a 40-tonne crew lander hitting the ground faster than sound; supersonic
      retropropulsion at Mach 2 to 3; Falcon 9 first stages since 2014, studied by NASA and SpaceX: this site's
      physics lesson Supersonic retropropulsion (above).
    - The Moon with no air and the Earth's parachute landings: standard. Coming back from the Moon at about 11 km/s:
      standard; a craft falling from far away reaches $\sqrt{2 \times 398{,}600 / 6{,}503} = 11.1$ km/s at the top of
      the air, our arithmetic.

## 17.8 Working it out { #working }

**Falling in.** A spacecraft that arrives with speed $v_\infty$ far from a planet has, at distance $r$ from its centre,

$$v = \sqrt{v_\infty^2 + \frac{2GM}{r}} .$$

For Mars, $GM = 42{,}828$ km³/s², and at 300 km up $r = 3{,}696$ km, so $2GM/r = 23.17$ km²/s². With
$v_\infty = 2.65$ km/s: $v = \sqrt{7.02 + 23.17} = 5.50$ km/s. Escape speed there is $\sqrt{23.17} = 4.81$ km/s, so
the spacecraft must lose at least $0.68$ km/s just to be caught.

**At the top of the air.** At 125 km up, $r = 3{,}521$ km and $v = \sqrt{7.02 + 24.33} = 5.60$ km/s, which is
20,200 km/h, as in figure B.

**Coming home to the Earth** from Mars, $v_\infty = 2.94$ km/s (chapter 15), and at 125 km up
$v = \sqrt{2.94^2 + 2 \times 398{,}600/6{,}503} = 11.5$ km/s.

**Thinner air.** With a scale height $H$, the air's density falls by a factor of $e$ for every $H$ you go up:
$\rho = \rho_0 e^{-h/H}$.

| | Mars | Earth |
| --- | --- | --- |
| Arriving from the other planet, speed at the top of the air | 5.6 km/s | 11.5 km/s |
| Escape speed at the ground | 5.03 km/s | 11.19 km/s |
| Air pressure at the ground | 6.4 millibars | 1,014 millibars |
| Scale height | 11.0 km | 8.5 km |
| Burn to be caught into a low orbit | 2.09 km/s | 3.59 km/s |

??? note "Sources"
    - $GM$, radii, escape speeds, surface pressures and scale heights: NASA, Mars Fact Sheet (above) and
      [Earth Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html). The speeds: our arithmetic.
      The Earth's low-orbit figure is chapter 15's leaving burn, which is the same as the braking burn for the same
      speed.

## 17.9 The capture burn, worked out { #derive }

Say the spacecraft arrives with $v_\infty$ and wants an orbit with its low point at $r_p$ and far point at $r_a$.

**Speed it has at $r_p$:** $\;v_1 = \sqrt{v_\infty^2 + 2GM/r_p}$.

**Speed the orbit needs at $r_p$**, from the speed rule of chapter 7 with $a = (r_p + r_a)/2$:

$$v_2 = \sqrt{GM\left(\frac{2}{r_p} - \frac{2}{r_p + r_a}\right)} = \sqrt{\frac{2GM\,r_a}{r_p(r_p + r_a)}} .$$

**The burn** is $\Delta v = v_1 - v_2$.

- **Circle**, $r_a = r_p = 3{,}696$ km: $v_2 = \sqrt{GM/r_p} = 3.40$ km/s, so $\Delta v = 5.50 - 3.40 = 2.09$ km/s.
- **300 by 45,000 km**, $r_a = 48{,}396$ km: $v_2 = \sqrt{2 \times 42{,}828 \times 48{,}396 / (3{,}696 \times 52{,}092)}
  = 4.64$ km/s, so $\Delta v = 0.86$ km/s.
- **Just caught**, $r_a \to \infty$: $v_2 \to \sqrt{2GM/r_p} = 4.81$ km/s, so $\Delta v = 0.68$ km/s.

**One aerobraking pass.** A small loss of speed $\delta v$ at the low point changes the orbit's energy by
$v_p\,\delta v$. Since $a = -GM/(2\varepsilon)$, a small change gives $\delta a = (2a^2/GM)\,v_p\,\delta v$, and with
the low point fixed, $r_a = 2a - r_p$ changes by twice that:

$$\delta r_a = \frac{4a^2 v_p}{GM}\,\delta v .$$

At the start of MRO's aerobraking, with the low point about 100 km up and the far point 44,500 km up,
$a = 25{,}696$ km and $v_p = 4.78$ km/s. A loss of 3 m/s on one pass drops the far point by

$$\frac{4 \times 25{,}696^2 \times 4.78}{42{,}828} \times 0.003 = 880 \text{ km}.$$

As the orbit shrinks, $a$ gets smaller and each pass does less, which is why the last part takes so long.

??? note "Sources"
    - The formulas: chapter 7 and standard. The numbers: our arithmetic with Mars's $GM$ and radius from the NASA Mars
      Fact Sheet (above). The 3 m/s a pass: the physics lesson Aerobraking and aerocapture (above).

## Check yourself { #check }

**1.** (beginner) Why can't a spacecraft that reaches Mars just switch off and stay?

??? note "Answer"
    Mars's pull speeds it up as it falls in, so close to Mars it is going faster than escape speed. Unless it loses
    speed, it swings round and leaves again.

**2.** (beginner) Which spacecraft was the first to orbit another planet?

??? note "Answer"
    Mariner 9, which reached Mars on 14 November 1971, just ahead of the Soviet Mars 2 and Mars 3.

**3.** (beginner) What is aerobraking?

??? note "Answer"
    Dipping the low point of an orbit into the thin top of a planet's air again and again, so each pass takes off a
    little speed and the orbit slowly shrinks, saving fuel.

**4.** (intermediate) Why do orbiters first get caught into a long ellipse rather than straight into a low circle?

??? note "Answer"
    It takes much less braking: about 0.86 km/s instead of 2.09 km/s for an arrival at 2.65 km/s. The rest of the
    shrinking can then be done by aerobraking, using air instead of fuel.

**5.** (intermediate) What went wrong with the Mars Climate Orbiter?

??? note "Answer"
    The sizes of its small thruster nudges were reported in pound-force seconds but read as newton-seconds, so the
    navigators' idea of its path drifted. It passed about 57 km above Mars instead of 226 km, in air millions of times
    thicker, and was lost.

**6.** (intermediate) Why can't a Mars lander use only parachutes, as capsules returning to the Earth do?

??? note "Answer"
    Mars's air at the ground is about sixty times thinner than the Earth's. Even the biggest parachute leaves a lander
    falling at about 300 km/h, so rockets, airbags or a sky crane must do the rest.

**7.** (advanced) A craft arrives at Mars with $v_\infty = 3.0$ km/s. How fast is it moving 300 km up, and how much
must it slow down there just to be caught?

??? note "Answer"
    $v = \sqrt{9.0 + 23.17} = 5.67$ km/s. Escape speed there is 4.81 km/s, so at least $0.86$ km/s.

**8.** (expert) Find the burn to be caught into an orbit 300 by 20,000 km above Mars, arriving at 2.65 km/s.

??? note "Answer"
    $r_p = 3{,}696$, $r_a = 23{,}396$ km. $v_2 = \sqrt{2 \times 42{,}828 \times 23{,}396 / (3{,}696 \times 27{,}092)}
    = \sqrt{20.01} = 4.47$ km/s. With $v_1 = 5.50$ km/s, $\Delta v = 1.03$ km/s.

## Summary

- A spacecraft reaching Mars is faster than escape speed when close in, and must lose speed to stay.
- Being caught into a long ellipse costs much less than going straight into a low circle; Mariner 9 was the first to
  orbit another planet, in 1971.
- Aerobraking shrinks the ellipse over months by dipping into the thin upper air; Mars Global Surveyor, Odyssey, MRO
  and the Trace Gas Orbiter all did it.
- Aerocapture, a single deep dive, has not yet been tried at a planet.
- A Mars landing takes about seven minutes: heat shield, parachute, then rockets, airbags or a sky crane.
- The Mars Climate Orbiter was lost in 1999 when a mix of units sent it 57 km above Mars instead of 226 km.
- Mars's air is too thick to ignore and too thin to rely on; landers of tens of tonnes will need rockets fired at
  supersonic speed.

**Next:** chapter 18, Einstein and orbits, where we find that Newton's laws are not quite the whole story: Mercury's
orbit turns a little too fast, radio signals passing the Sun are delayed, and the clocks on GPS satellites run fast.

## Further reading

- Rob Manning and William L. Simon, *Mars Rover Curiosity: An Inside Account from Curiosity's Chief Engineer*,
  Smithsonian Books, 2014.
