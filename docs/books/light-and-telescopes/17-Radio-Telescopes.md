# 17. Radio telescopes

*The history book told how radio astronomy began, with static on a telephone line and a dish in a back yard (history
book, [chapter 20](../history/20-Radio-Astronomy.md#jansky)). This chapter is about the instruments themselves. It
explains what a radio telescope is, why its dish can be made of wire, and why a single dish sees such a blurred sky.
It visits the giant dishes of Germany, the United States, China, Russia and India, then shows how dishes kilometres
or continents apart can be joined into one telescope as wide as the Earth. It ends with radar, and with the faint
radio voice that brings every picture home from Mars.*

!!! abstract "In this chapter"
    **You will learn:**

    - the parts of a radio telescope and what each does
    - which radio waves get through the air, and why some dishes are made of wire
    - why a single dish sees a blurred sky
    - how radio astronomers measure faint signals and protect their quiet
    - how the largest dishes keep their shape
    - how many dishes are combined into one telescope, up to the size of the Earth
    - how radar bounces radio off the planets
    - how the radio signal from a Mars orbiter reaches Earth, and how faint it is

    **You need:** chapter 4 on the bands of the spectrum, chapter 11 on mirrors, and chapter 12 on diffraction. The
    history book, [chapter 20](../history/20-Radio-Astronomy.md#jansky), tells the story of radio astronomy.

    **Levels:** 17.1 to 17.3 are beginner; 17.4 to 17.8 are intermediate; 17.9 is advanced; 17.10 is expert.

## 17.1 A dish, a horn and a receiver { #parts }

A radio telescope is an antenna and a radio receiver, built to pick up radio waves from space. Most are curved dishes,
like the dishes used to talk to satellites and spacecraft, only larger.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The parts of a radio telescope. Radio waves from a distant source arrive as parallel rays from straight above. They strike a curved dish, which reflects every ray to one point, the focus, held above the dish by struts. At the focus a feed horn collects the waves and passes them to the receiver, which amplifies the faint signal. A cable carries it down the mount, which turns the dish to follow the sky, to a computer that records and analyses it. The dish can be solid metal, or wire mesh for long waves.">
  <g font-size="8" fill="currentColor">
    <polyline points="50,168.8 55,171.8 60,174.7 65,177.4 70,180.0 75,182.4 80,184.7 85,186.8 90,188.8 95,190.5 100,192.2 105,193.7 110,195.0 115,196.2 120,197.2 125,198.0 130,198.8 135,199.3 140,199.7 145,199.9 150,200.0 155,199.9 160,199.7 165,199.3 170,198.8 175,198.0 180,197.2 185,196.2 190,195.0 195,193.7 200,192.2 205,190.5 210,188.8 215,186.8 220,184.7 225,182.4 230,180.0 235,177.4 240,174.7 245,171.8 250,168.8" fill="none" stroke="currentColor" stroke-width="2.5"/>
    <line x1="50" y1="168.8" x2="150" y2="120" stroke="#555" stroke-width="0.8"/>
    <line x1="250" y1="168.8" x2="150" y2="120" stroke="#555" stroke-width="0.8"/>
    <polyline points="90,30 90,188.8 150,120" fill="none" stroke="#5aa0d8" stroke-width="1"/>
    <polyline points="120,30 120,197.2 150,120" fill="none" stroke="#5aa0d8" stroke-width="1"/>
    <polyline points="180,30 180,197.2 150,120" fill="none" stroke="#5aa0d8" stroke-width="1"/>
    <polyline points="210,30 210,188.8 150,120" fill="none" stroke="#5aa0d8" stroke-width="1"/>
    <polygon points="144,112 156,112 153,122 147,122" fill="#eea66f" stroke="currentColor" stroke-width="0.8"/>
    <rect x="141" y="98" width="18" height="14" fill="#cfc8bf" stroke="currentColor" stroke-width="0.8"/>
    <line x1="150" y1="200" x2="150" y2="232" stroke="currentColor" stroke-width="3"/>
    <rect x="128" y="232" width="44" height="6" fill="currentColor"/>
    <rect x="250" y="200" width="70" height="22" fill="none" stroke="currentColor" stroke-width="1"/>
    <text x="285" y="214" text-anchor="middle">computer</text>
    <path d="M172,235 L285,235 L285,222" fill="none" stroke="currentColor" stroke-width="0.8" stroke-dasharray="3 2"/>
    <text x="150" y="24" text-anchor="middle">radio waves from a distant source</text>
    <line x1="222" y1="102" x2="161" y2="106" stroke="currentColor" stroke-width="0.5"/>
    <text x="224" y="98">feed horn and</text>
    <text x="224" y="107">receiver at the focus</text>
    <text x="258" y="162">dish: metal, or</text>
    <text x="258" y="171">wire mesh for</text>
    <text x="258" y="180">long waves</text>
    <text x="6" y="70">the dish reflects</text>
    <text x="6" y="79">every ray to</text>
    <text x="6" y="88">one point</text>
    <text x="6" y="216">the mount turns</text>
    <text x="6" y="225">the dish to</text>
    <text x="6" y="234">follow the sky</text>
    <text x="285" y="246" text-anchor="middle">records, analyses</text>
    <text x="6" y="12">A radio telescope</text>
  </g>
</svg>
</div>

*Figure A. The parts of a radio telescope.*

- **The dish** is a curved reflector, shaped like the mirror of a reflecting telescope (chapter 13). It sends every
  ray arriving straight on to one point, the focus.
- **The feed horn** at the focus is a small horn-shaped antenna that collects the waves and guides them into the
  receiver.
- **The receiver** amplifies the very weak signal.
- **A computer** records it and works out how bright the source is, or splits it into a spectrum.

A simple radio telescope has, in effect, only one pixel. It measures how much radio comes from the patch of sky it is
pointing at. To make a map, it points at one patch after another.

??? note "Sources"
    - A radio telescope as a specialised antenna and receiver, typically a large parabolic dish like those for tracking
      and talking to satellites and space probes: Wikipedia,
      [Radio telescope](https://en.wikipedia.org/wiki/Radio_telescope) (weaker).
    - A feed horn as a small horn antenna that couples a dish to the receiver: Wikipedia,
      [Feed horn](https://en.wikipedia.org/wiki/Feed_horn) (weaker).
    - A single dish mapping by pointing at one spot after another is standard practice.

## 17.2 Long waves: wire dishes and blurry views { #long }

**What gets through.** The air lets radio through from waves about 30 m long down to about 0.3 mm (chapter 4,
[section 4.5](04-Beyond-the-Rainbow.md#air)). Longer waves, below about 10 MHz, are reflected back into space by the
**ionosphere**, a layer of charged gas high in the air. At the short end, water vapour absorbs strongly at 1.32 cm,
1.64 mm and 0.93 mm, so millimetre telescopes go high and dry.

**Wire is enough.** A mirror only needs to be smooth compared with the waves it reflects. Radio waves are so long
that a dish for metre waves can be made of coarse wire mesh, even chicken wire. India's Ooty Radio Telescope reflects
with 1,100 thin stainless-steel wires.

**But the view is blurred.** The finest detail a telescope can show is about the wavelength divided by its width
(chapter 12). Radio waves are hundreds of thousands of times longer than light, so even a huge dish is blurry. A
100 m dish working at 21 cm, the wavelength of hydrogen (history book,
[section 20.4](../history/20-Radio-Astronomy.md#hydrogen)), sees nothing smaller than about 9 minutes of arc, more than
a quarter of the width of the full Moon. Your eye does better than that.

??? note "Sources"
    - The radio window from about 10 MHz (30 m) to about 1 THz (0.3 mm) at the best sites, reflection below 10 MHz by
      the ionosphere, and the water vapour bands at 22.3 GHz (1.32 cm), 183.3 GHz (1.64 mm) and 323.8 GHz (0.93 mm):
      Wikipedia, [Radio window](https://en.wikipedia.org/wiki/Radio_window) (weaker).
    - Reflectors of coarse wire mesh such as chicken wire for long waves: Wikipedia, Radio telescope (above).
    - Ooty's 1,100 stainless-steel wires: Wikipedia,
      [Ooty Radio Telescope](https://en.wikipedia.org/wiki/Ooty_Radio_Telescope) (weaker).
    - The 9 minutes of arc is worked out in section 17.9. The full Moon is about half a degree, 30 minutes of arc,
      across.

## 17.3 Whispers from space { #faint }

**What sends out radio.** The Sun and Jupiter; the centre of the Milky Way, where a giant black hole lies;
**pulsars**, **quasars** and radio galaxies, whose jets of fast charged particles give out radio; clouds of gas that
glow in the hydrogen line; and natural **masers**, the radio cousins of lasers (history book,
[section 20.6](../history/20-Radio-Astronomy.md#quasars)).

**How faint.** Radio astronomers measure brightness in **janskys**, named after Karl Jansky. One jansky is
$10^{-26}$ watts falling on each square metre, in each hertz of the radio band.

**Keeping quiet.** Radio, television, radar, cars and other electronics all drown these whispers, so radio
observatories are built far from towns.

- **USA, 1958.** The National Radio Quiet Zone, about 34,000 km², mostly in Virginia and West Virginia, protects the
  Green Bank telescopes. The observatory even checks for microwave ovens and Wi-Fi in the area, and asks people to
  stop using them.
- **China.** To make a radio-quiet area round the FAST dish (section 17.4), a village of 65 people was moved,
  along with 9,110 more people living within 5 km.

??? note "Sources"
    - The Sun, Jupiter, Sagittarius A*, active galactic nuclei and pulsars with jets giving synchrotron radiation, and
      masers: Wikipedia, [Radio astronomy](https://en.wikipedia.org/wiki/Radio_astronomy) (weaker).
    - The jansky, $10^{-26}$ watts per square metre per hertz, named after Karl Jansky: Wikipedia,
      [Jansky](https://en.wikipedia.org/wiki/Jansky) (weaker).
    - Radio observatories far from population to avoid interference from radio, television, radar and motor vehicles:
      Wikipedia, Radio telescope (above).
    - The Quiet Zone created by the FCC in 1958, about 34,000 km², Green Bank and Sugar Grove, and the policing of
      microwave ovens and Wi-Fi: Wikipedia,
      [National Radio Quiet Zone](https://en.wikipedia.org/wiki/National_Radio_Quiet_Zone) (weaker).
    - The village of 65 and the 9,110 people within 5 km: Wikipedia,
      [FAST](https://en.wikipedia.org/wiki/Five-hundred-meter_Aperture_Spherical_Telescope) (weaker). FAST's first light
      in 2016: this site's history book, chapter 20.

## 17.4 Giant dishes { #dishes }

A big dish has the same problem as a big mirror (chapter 16): as it tilts, it sags. Each of the giants below has its
own answer. Jodrell Bank, Parkes and Arecibo, the first giants, have their stories in the history book,
[section 20.5](../history/20-Radio-Astronomy.md#dishes).

- **Effelsberg, Germany, 1972.** The 100 m dish of the Max Planck Institute for Radio Astronomy has a support
  structure designed by computer so that, as it bends, the dish always keeps a true focusing
  shape. For 29 years it was the largest fully steerable radio telescope on Earth.
- **Green Bank, USA, 2000.** The earlier 90 m dish at Green Bank collapsed on 15 November 1988 when one steel plate in
  its frame failed. Its replacement, the **Green Bank Telescope**, measures 100 by 110 m. Its surface is made of 2,004
  panels moved by 2,209 small motors, and its receivers hang to one side on a 61 m arm so that nothing blocks the dish.
  It is the largest fully steerable radio telescope in the world.
- **Guizhou, China, 2016.** **FAST**, 500 m across, lies in a natural hollow and cannot move. Instead its surface,
  4,450 triangular panels each 11 m on a side, is pulled into a moving curved shape wherever it needs to look, using
  300 m of the dish at a time. The receiver hangs above in a cabin moved by cables and winches. By November 2024 it had
  discovered more than 1,000 new pulsars.
- **Caucasus, Russia, 1974.** **RATAN-600**, next to the BTA-6 of chapter 16, is not a dish at all but a ring 576 m
  across of 895 tilting panels, each 2 by 7.4 m, that reflect radio onto receivers.
- **Ooty, India, 1970.** The **Ooty Radio Telescope** is a cylinder 530 m long and 30 m tall, lying on a natural
  slope of 11°, the same as the latitude of the place, so its long axis points along the Earth's axis.

??? note "Sources"
    - Effelsberg: 100 m, the Max Planck Institute for Radio Astronomy, inaugurated in 1972, the computer-designed
      support that keeps the deformed mirror parabolic, the largest fully steerable for 29 years: Wikipedia,
      [Effelsberg 100-m Radio Telescope](https://en.wikipedia.org/wiki/Effelsberg_100-m_Radio_Telescope) (weaker).
    - The 300-foot (90.44 m) telescope's collapse on 15 November 1988 from a failed gusset plate, the GBT's 100 by
      110 m surface, 2,004 panels and 2,209 actuators, the 61 m offset arm and unblocked aperture, and the largest
      fully steerable radio telescope: Wikipedia,
      [Green Bank Telescope](https://en.wikipedia.org/wiki/Green_Bank_Telescope) (weaker). 2000 as the year it overtook
      Effelsberg: Wikipedia, Effelsberg 100-m Radio Telescope (above).
    - FAST: 4,450 triangular panels 11 m on a side, the active surface forming a moving parabola, 300 m used without
      loss, the feed cabin on cables moved by winches, and more than 1,000 pulsars by November 2024: Wikipedia, FAST
      (above).
    - RATAN-600: a 576 m circle of 895 reflectors each 2 m by 7.4 m, at 970 m, working since mid-1974, beside BTA-6:
      Wikipedia, [RATAN-600](https://en.wikipedia.org/wiki/RATAN-600) (weaker).
    - Ooty: 530 m by 30 m, an 11° slope matching the latitude, completed in 1970: Wikipedia, Ooty Radio Telescope
      (above). That the axis is then parallel to the Earth's axis follows from the geometry (chapter 13).

## 17.5 Many dishes as one { #arrays }

Two dishes some distance apart receive the same radio wave, but one gets it a little later than the other. Feed both
signals into a **correlator**, which multiplies them together and adds up the result. As the Earth turns and the source
moves across the sky, the difference in path changes, and the combined signal rises and falls in **fringes**, like the
bright and dark bands of Young's experiment (chapter 1).

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Two radio dishes working as one. Two dishes stand on the ground a distance B apart, the baseline. Radio waves from a distant source arrive from the upper right, tilted at an angle theta from straight up. The wave fronts, drawn as dashed lines across the rays, reach the right-hand dish first. The left-hand dish receives the same wave front later, after it has travelled an extra distance B times sine theta, shown in orange. Cables carry both signals to a correlator; the signal from the right-hand dish passes through a delay so that the two match. The correlator multiplies and adds them. As the source moves across the sky the extra path changes, and the combined signal rises and falls in fringes.">
  <g font-size="8" fill="currentColor">
    <line x1="10" y1="190" x2="330" y2="190" stroke="#555" stroke-width="0.8"/>
    <line x1="155.0" y1="60.1" x2="80" y2="182" stroke="#5aa0d8" stroke-width="1"/>
    <path d="M69.6,176.0 Q78.0,187.2 90.4,188.0" fill="none" stroke="currentColor" stroke-width="2"/>
    <line x1="80" y1="186" x2="80" y2="190" stroke="currentColor" stroke-width="2"/>
    <line x1="335.0" y1="60.1" x2="260" y2="182" stroke="#5aa0d8" stroke-width="1"/>
    <path d="M249.6,176.0 Q258.0,187.2 270.4,188.0" fill="none" stroke="currentColor" stroke-width="2"/>
    <line x1="260" y1="186" x2="260" y2="190" stroke="currentColor" stroke-width="2"/>
    <line x1="266.9" y1="186.0" x2="99.0" y2="89.1" stroke="currentColor" stroke-width="0.8" stroke-dasharray="4 2"/>
    <line x1="286.9" y1="151.4" x2="119.0" y2="54.4" stroke="currentColor" stroke-width="0.8" stroke-dasharray="4 2"/>
    <line x1="125.0" y1="104.1" x2="80" y2="182" stroke="#c1440e" stroke-width="2.5"/>
    <text x="64" y="122" text-anchor="end" fill="#c1440e">extra path</text>
    <text x="64" y="131" text-anchor="end" fill="#c1440e">B sin θ</text>
    <line x1="80" y1="182" x2="80" y2="130" stroke="#555" stroke-width="0.5" stroke-dasharray="2 2"/>
    <path d="M80,142 A40,40 0 0 1 100.0,147.4" fill="none" stroke="currentColor" stroke-width="0.6"/>
    <text x="89" y="138">θ</text>
    <path d="M80,200 L260,200 M84,197 L80,200 L84,203 M256,197 L260,200 L256,203" fill="none" stroke="currentColor" stroke-width="0.8"/>
    <text x="170" y="198" text-anchor="middle">baseline B</text>
    <path d="M80,190 L80,220 L150,220" fill="none" stroke="currentColor" stroke-width="0.8"/>
    <path d="M260,190 L260,220 L246,220" fill="none" stroke="currentColor" stroke-width="0.8"/>
    <rect x="222" y="214" width="24" height="12" fill="none" stroke="currentColor" stroke-width="0.8"/>
    <text x="234" y="223" text-anchor="middle">delay</text>
    <path d="M222,220 L200,220" fill="none" stroke="currentColor" stroke-width="0.8"/>
    <rect x="150" y="212" width="50" height="16" fill="#cfc8bf" fill-opacity="0.5" stroke="currentColor" stroke-width="0.8"/>
    <text x="175" y="223" text-anchor="middle">correlator</text>
    <text x="175" y="240" text-anchor="middle">multiplies and adds the two signals</text>
    <text x="334" y="40" text-anchor="end">waves from a</text>
    <text x="334" y="49" text-anchor="end">distant source</text>
    <text x="112" y="50" text-anchor="end">wave fronts</text>
    <text x="6" y="12">Two dishes working as one</text>
  </g>
</svg>
</div>

*Figure B. Two dishes working as one.*

The sharpness now depends on the distance between the dishes, the **baseline** $B$, not on their size: the finest
detail is about $\lambda/B$. Each pair of dishes measures one ingredient of the picture. With many pairs, and the
turning of the Earth to swing each pair round, a computer can build up a full picture. This is **aperture synthesis**,
developed by Martin Ryle and his group at Cambridge (history book,
[section 20.5](../history/20-Radio-Astronomy.md#dishes)).

- **The Very Large Array, New Mexico, 1980.** 28 dishes, each 25 m across (27 in use at a time, one always being
  serviced), stand along the three arms of a Y, each arm 21 km long. They move along double railway tracks: in the
  tightest layout all are within 600 m of the centre, and in the widest they are spread out along the arms.
- **ALMA, Chile, 2013.** 66 antennas on the Chajnantor plateau, 5,000 m up in the Atacama, work at waves from 3.6 to
  0.32 mm. The United States and Europe gave 25 antennas each, 12 m across, and East Asia 16 more. Giant trucks carry
  them to new positions from 150 m to 16 km apart; the drivers' seats are made to fit an oxygen tank for the thin air.
- **India, South Africa and Australia.** The GMRT near Pune, MeerKAT in the Karoo, and the Square Kilometre Array now
  being built, appear in the history book, [sections 20.8](../history/20-Radio-Astronomy.md#world) and
  [20.9](../history/20-Radio-Astronomy.md#arrays).

??? note "Sources"
    - Aperture synthesis: each separation and orientation giving one component of the Fourier transform of the
      brightness, the use of the Earth's rotation to add baselines, and its development by Ryle and coworkers at
      Cambridge: Wikipedia, [Aperture synthesis](https://en.wikipedia.org/wiki/Aperture_synthesis) (weaker).
    - The VLA: 28 dishes of 25 m with 27 in use, the Y with 21 km arms, double railroad tracks, configurations A to D
      with D within 600 m, the first antenna in 1975 and the inauguration in 1980: Wikipedia,
      [Very Large Array](https://en.wikipedia.org/wiki/Very_Large_Array) (weaker).
    - ALMA: 66 antennas, 3.6 to 0.32 mm, the 5,000 m Chajnantor plateau, 25 + 25 antennas of 12 m from America and
      Europe, 16 from East Asia, transporters moving them from 150 m to 16 km apart with seats for an oxygen tank, fully
      operational since March 2013: Wikipedia,
      [ALMA](https://en.wikipedia.org/wiki/Atacama_Large_Millimeter_Array) (weaker).

## 17.6 A telescope as wide as the Earth { #vlbi }

When the dishes are on different continents, no cable can join them. Instead, in **very long baseline
interferometry** (VLBI), each dish records its signal along with the exact time from its own **atomic clock**, such
as a hydrogen maser. Later, the recordings are brought together and combined. Some are now sent along fast fibre-optic
links instead.

- The **Very Long Baseline Array** has ten 25 m dishes spread 8,600 km across the United States.
- **RadioAstron**, a Russian 10 m radio telescope launched into orbit in 2011, which stopped answering in 2019, swung
  as far as 338,541 km from Earth and worked with dishes on the ground, making the largest radio interferometer yet.
- The **Event Horizon Telescope** joined dishes from Hawaiʻi and Chile to Greenland and the South Pole, and in 2019
  showed the first picture of a black hole (history book, [section 20.9](../history/20-Radio-Astronomy.md#arrays)).

VLBI also works in reverse. Distant quasars serve as fixed markers in the sky, so the tiny differences in arrival time
show how the dishes themselves move. This measures the drift of the Earth's plates to within millimetres, and the
wobbles of the Earth's spin.

??? note "Sources"
    - Each antenna's data timed by a local atomic clock such as a hydrogen maser and correlated later, e-VLBI over
      fibre, the VLBA's ten 25 m dishes spanning 5,351 miles (8,612 km), RadioAstron's apogee of 338,541 km making it
      the biggest radio interferometer, and VLBI used in reverse for Earth rotation and tectonic plates to within
      millimetres: Wikipedia,
      [Very-long-baseline interferometry](https://en.wikipedia.org/wiki/Very-long-baseline_interferometry) (weaker).
    - RadioAstron's 10 m telescope, its launch on 18 July 2011, and the loss of contact on 11 January 2019: Wikipedia,
      [Spektr-R](https://en.wikipedia.org/wiki/Spektr-R) (weaker).
    - The Event Horizon Telescope: this site's history book, chapter 20, section 20.9.

## 17.7 Radar: radio that comes back { #radar }

A radio telescope can also send. **Radar** sends out a pulse and listens for the echo.

- **The Moon** was detected by radar soon after the technique was invented, in 1946.
- **Venus** was first detected in 1961. Timing the echo gave a direct measurement of the size of the Earth's orbit,
  needed to steer the first spacecraft to the planets.
- **Mars.** The Arecibo dish mapped how rough Mars's surface is.

Arecibo collapsed in December 2020 (history book, [section 20.5](../history/20-Radio-Astronomy.md#dishes)). As of
2023 two planetary radars were in regular use: the Goldstone Solar System Radar in California and the Evpatoria
Planetary Radar on the Black Sea.

Radar also works from orbit round Mars. **SHARAD**, on NASA's Mars Reconnaissance Orbiter, sends radio waves of 15 to
25 MHz into the ground and can pick out layers as thin as 7 m down to 3 km deep. **MARSIS**, on Europe's Mars Express,
sees coarser detail but goes deeper. Both were made by the Italian Space Agency (chapter 4,
[section 4.7](04-Beyond-the-Rainbow.md#mars); history book, [section 20.10](../history/20-Radio-Astronomy.md#mars)).

??? note "Sources"
    - The Moon detected by radar soon after 1946, Venus first detected in 1961 and its use for the astronomical unit,
      Arecibo's mapping of Mars's surface roughness, the collapse of Arecibo, and Goldstone and Evpatoria in regular use
      as of 2023: Wikipedia, [Radar astronomy](https://en.wikipedia.org/wiki/Radar_astronomy) (weaker).
    - SHARAD: 15 to 25 MHz, layers as thin as 7 m to 3 km deep, MARSIS coarser and deeper, both made by the Italian
      Space Agency: Wikipedia,
      [Mars Reconnaissance Orbiter](https://en.wikipedia.org/wiki/Mars_Reconnaissance_Orbiter) (weaker).

## 17.8 Hearing Mars { #mars }

Every picture from Mars comes home by radio, picked up by the big dishes of NASA's Deep Space Network in California,
Spain and Australia (history book, [section 20.10](../history/20-Radio-Astronomy.md#mars)). Take the Mars
Reconnaissance Orbiter, which reached Mars on 10 March 2006.

- **Its voice.** A dish 3 m across sends to Earth at 8.41 GHz, a wavelength of 3.6 cm, powered by an amplifier of
  100 watts, about as much as a bright old-fashioned light bulb. There is a second amplifier as a spare.
- **Its ears.** The Deep Space Network listens with dishes 34 m and 70 m across. Because the 8.41 GHz band is crowded,
  its 34 m dishes were given receivers for a higher band, at 32 GHz.
- **A relay.** The orbiter also carries Electra, a radio that talks to the rovers on the ground at 1 thousand to
  2 million bits a second, and passes their data on to Earth (chapter 4).
- **How much.** The orbiter has sent back more than three times as much data as all of NASA JPL's other missions of
  the previous ten years together.

By the time the orbiter's 100 watts reach a 70 m dish on Earth, only about a fifth of a million-millionth of a watt is
left, and when Mars is on the far side of the Sun, fifty times less (section 17.9). Radio is also used to measure Mars
itself: tracking the radio from a lander showed how Mars wobbles, and so the size of its core (chapter 8,
[section 8.8](08-The-Doppler-Shift.md#mars)).

??? note "Sources"
    - MRO's arrival on 10 March 2006, its 3 m high-gain antenna at 8.41 GHz in the X band, the two 100-watt amplifiers
      (one a backup), the Deep Space Network's Ka-band (32 GHz) receivers on its 34 m antennas because of the lack of
      room at 8.41 GHz, the Electra UHF radio with links of 1 kbit/s to 2 Mbit/s, and the data returned compared with
      JPL's other missions: Wikipedia, Mars Reconnaissance Orbiter (above).
    - The 34 m and 70 m dishes of the Deep Space Network: this site's history book, chapter 20, section 20.10.
    - The received power is our rough estimate in section 17.9. A bright incandescent bulb of 100 W is our comparison.

## 17.9 Working it out { #working }

**Sharpness.** The finest detail is about $1.22\lambda/D$ for a single dish, and about $\lambda/B$ for an array.

| Telescope | Wavelength | Width or baseline | Finest detail |
| --- | --- | --- | --- |
| A 100 m dish | 21 cm | 100 m | 8.8 minutes of arc |
| Green Bank, at its shortest wave | 2.6 mm (116 GHz) | 100 m | 6.5 seconds of arc |
| VLA, widest layout | 21 cm | about 36 km | 1.2 seconds of arc |
| ALMA, widest layout | 0.32 mm | 16 km | 0.004 seconds of arc |
| Event Horizon Telescope | 1.3 mm | about the Earth | 0.000025 seconds of arc |

The VLA's arms are 21 km long and 120° apart, so the ends of two arms are $21 \times \sqrt{3} \approx 36$ km apart.

**Pairs.** $N$ dishes make $N(N-1)/2$ pairs: 351 for the VLA's 27, 2,016 for MeerKAT's 64 and 2,145 for ALMA's 66.

**An Event Horizon Telescope on each planet.** The longest baseline on a planet is its diameter.

| | Mars | Earth |
| --- | --- | --- |
| Diameter, the longest baseline | 6,792 km | 12,756 km |
| Finest detail at 1.3 mm, $\lambda/B$ | 0.000039 seconds of arc | 0.000021 seconds of arc |
| Radio time across the planet | 23 ms | 43 ms |
| Time to turn once, swinging each baseline round | 24.6 hours | 23.9 hours |

A dish on Earth and a dish on Mars, 54.6 million km apart at closest, would make a baseline 4,300 times longer than the
Earth, and could in principle see detail of 5 billionths of a second of arc.

**The whisper from Mars.** A dish of width $D$ concentrates its power into a narrow beam, by a factor called the
**gain**, roughly $0.55(\pi D/\lambda)^2$. For the orbiter's 3 m dish at 3.6 cm, that is about 38,000. A dish on Earth
with a collecting area $A$ catches

$$P = \frac{P_t\, G\, A}{4\pi d^2}.$$

With $P_t = 100$ W, $G = 38{,}000$, a 70 m dish catching on about 60% of its area, $A \approx 2{,}300$ m², and Mars at
its closest, $d = 54.6$ million km:
$P = 100 \times 38{,}000 \times 2{,}300 / (4\pi \times (5.46\times10^{10})^2) \approx 2\times10^{-13}$ W. At its
farthest, 401.3 million km, the power is $(401.3/54.6)^2 = 54$ times less, about $4\times10^{-15}$ W.

??? note "Sources"
    - Mars and Earth diameters, rotation periods and distances: NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - The VLA's 21 km arms and ALMA's 16 km: sections 17.5 and above. The GBT's top frequency of 116 GHz: Wikipedia,
      Green Bank Telescope (above). The EHT's 1.3 mm: this site's history book, chapter 20.
    - The 55% and 60% efficiencies are typical values we have assumed; the arithmetic is ours.

## 17.10 How two dishes make a picture { #fourier }

**Fringes.** Let a point source at angle $\theta$ send a wave of frequency $\nu$. The far dish receives it later by
$\tau = B\sin\theta / c$. The correlator multiplies the two signals and averages:

$$\langle \cos(2\pi\nu t)\cos(2\pi\nu(t-\tau)) \rangle = \tfrac12\cos(2\pi\nu\tau)
= \tfrac12\cos\!\left(\frac{2\pi B\sin\theta}{\lambda}\right).$$

As $\theta$ changes, the output swings between high and low. One full swing happens when $B\sin\theta$ changes by one
wavelength, so neighbouring fringes are about $\lambda/(B\cos\theta)$ apart: the sharpness of an array is set by
$\lambda/B$.

**Pictures from fringes.** A source that is spread out is the sum of many points, each making its own fringes. What the
correlator then measures is one **Fourier component** of the brightness of the sky, the one with a spatial frequency
$u = B/\lambda$ along the direction of the baseline. Short baselines measure the broad shape, long ones the fine
detail. To rebuild the picture by an inverse Fourier transform you need many different $u$: hence many dishes, giving
$N(N-1)/2$ pairs, moved into new layouts, and swung round by the turning Earth.

**How faint can you go?** The receiver adds its own noise, described by a "system temperature" $T_{sys}$. Averaging
over a band $\Delta\nu$ for a time $t$ gives about $\Delta\nu\, t$ independent samples, and the noise falls as their
square root (chapter 14):

$$\Delta T = \frac{T_{sys}}{\sqrt{\Delta\nu\, t}}.$$

With $T_{sys} = 20$ K, a band of 1 MHz and one hour, $\Delta T = 20/\sqrt{10^6 \times 3{,}600} \approx 0.0003$ K: a
signal 60,000 times weaker than the receiver's own noise can still be seen.

??? note "Sources"
    - Each baseline giving one Fourier component of the brightness, and the Earth's rotation adding baselines:
      Wikipedia, Aperture synthesis (above).
    - That quasars serve as fixed reference points for VLBI is standard.
    - The fringe formula, the noise formula and the example are ours, using standard wave and counting arguments; the
      20 K system temperature is an assumed value.

## Check yourself { #check }

**1.** (beginner) Name the main parts of a radio telescope.

??? note "Answer"
    The dish, which reflects the waves to a focus; the feed horn at the focus; the receiver, which amplifies the
    signal; and a computer that records and analyses it. A mount turns the dish.

**2.** (beginner) Why can a radio dish for long waves be made of wire mesh?

??? note "Answer"
    A reflector only needs to be smooth compared with the wavelength. Radio waves metres long see a coarse mesh as a
    solid surface.

**3.** (beginner) Why are radio observatories built far from towns?

??? note "Answer"
    Radio, television, radar, cars and other electronics give out radio that would drown the faint signals from space.

**4.** (intermediate) How does the Effelsberg dish keep its shape as it tilts?

??? note "Answer"
    Its support structure was designed by computer so that, as the dish sags, it bends into another perfect focusing
    shape.

**5.** (intermediate) Why do the VLA's dishes sit on railway tracks?

??? note "Answer"
    So they can be moved into different layouts: spread wide for fine detail, or close together to pick up broad,
    faint features.

**6.** (intermediate) How can dishes on different continents work together?

??? note "Answer"
    Each records its signal with the exact time from an atomic clock, such as a hydrogen maser. The recordings are
    combined later in a correlator. This is very long baseline interferometry.

**7.** (advanced) ALMA works at 1.3 mm with dishes up to 16 km apart. What is the finest detail, in seconds of arc?

??? note "Answer"
    $\lambda/B = 1.3\times10^{-3}/1.6\times10^4 = 8.1\times10^{-8}$ radians $\times 206{,}265 \approx 0.017$ seconds of
    arc.

**8.** (expert) An array has 40 dishes. How many baselines does it have, and why does the turning of the Earth help?

??? note "Answer"
    $40 \times 39 / 2 = 780$ baselines. As the Earth turns, each baseline, seen from the source, changes its length and
    direction, so it measures many different Fourier components of the picture instead of one.

## Summary

- A radio telescope is a dish, a feed horn at its focus, a receiver and a computer.
- Radio gets through the air from about 30 m to 0.3 mm; the ionosphere blocks longer waves, water vapour shorter ones.
- Long waves let dishes be made of wire, but even a 100 m dish sees a blurred sky.
- Radio sources are measured in janskys, and observatories hide in radio-quiet zones.
- Effelsberg, Green Bank, FAST, RATAN-600 and Ooty each found a different way to build big.
- Arrays such as the VLA and ALMA combine many dishes; their sharpness is set by the baseline.
- VLBI joins dishes across the world with atomic clocks, and also measures the moving Earth.
- Radar bounces radio off the Moon and planets, and orbiting radars look under the ground of Mars.
- A Mars orbiter's 100 W reaches Earth as about $10^{-13}$ W, enough to carry every picture home.

**Next:**
[chapter 18, Infrared, ultraviolet, X-ray and gamma-ray astronomy](18-Infrared-Ultraviolet-X-ray-and-Gamma-ray-Astronomy.md),
where we look at the rest of the invisible sky.

## Further reading

- Gerrit L. Verschuur, *The Invisible Universe: The Story of Radio Astronomy*, 2nd edition, Springer, 2007.
