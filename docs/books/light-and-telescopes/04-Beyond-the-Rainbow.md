# 4. Beyond the rainbow: radio to gamma rays

*The colours we see are a thin slice of a much bigger family of light. This chapter goes out past the red end, to
infrared, microwaves and radio, and past the violet end, to ultraviolet, X-rays and gamma rays. It tells how each was
found, in England, Germany, India and France, what each one shows us in the sky, and why most of them never reach the
ground. It visits the spacecraft that study Mars with radar, infrared and ultraviolet, and ends by counting the
photons in a beam of light.*

!!! abstract "In this chapter"
    **You will learn:**

    - that radio waves, light and X-rays are all the same kind of wave
    - how each kind of invisible light was discovered
    - the names and sizes of the bands, from radio to gamma rays
    - why ultraviolet, X-rays and gamma rays can harm living things
    - which kinds of light get through the Earth's air, and which need telescopes in space
    - what each band shows astronomers
    - how spacecraft use radio, radar, infrared and ultraviolet at Mars
    - how to change between frequency, wavelength and photon energy
    - how to count the photons in a beam

    **You need:** chapters 1 and 3. The physics lesson
    [The electromagnetic spectrum](https://physics.akadian.ca/topics/waves/level-6/02-the-electromagnetic-spectrum.html)
    helps.

    **Levels:** 4.1 to 4.4 are beginner; 4.5 to 4.7 are intermediate; 4.8 is advanced; 4.9 is expert.

## 4.1 One family of light { #family }

When Maxwell worked out that light is an electric and magnetic wave (chapter 1, section 1.6), his equations allowed
such waves to have any frequency at all, and all of them travel at the speed of light. The light we see is only a
small part of this range. The whole range is called the **electromagnetic spectrum**.

Every member of the family obeys the same rule (chapter 1):

$$\text{speed} = \text{frequency} \times \text{wavelength}, \qquad c = f\lambda.$$

Since $c$ is the same for all, a longer wave has a lower frequency. Frequency is measured in **hertz** (Hz), one wave
per second, named after Heinrich Hertz. The name was adopted in 1960, replacing "cycles per second".

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The electromagnetic spectrum as one long bar, with each step to the right ten times shorter in wavelength. From the left: radio waves, kilometres to a metre long; microwaves, a metre to a millimetre; infrared, a millimetre down to 750 nanometres; then a thin sliver of visible light from 740 to 380 nanometres, shown enlarged below as a band of colours from red to violet; then ultraviolet, down to 10 nanometres; X-rays, down to 10 picometres; and gamma rays, shorter still. Waves on the left are longer, with lower frequency and less energy in each photon; waves on the right are shorter, with higher frequency and more energy.">
  <defs><linearGradient id="l04vis" x1="0" x2="1" y1="0" y2="0">
    <stop offset="0" stop-color="#c0392b"/>
    <stop offset="0.25" stop-color="#e67e22"/>
    <stop offset="0.42" stop-color="#e6c619"/>
    <stop offset="0.6" stop-color="#3a9a46"/>
    <stop offset="0.8" stop-color="#2f6fc8"/>
    <stop offset="1" stop-color="#6b3fa0"/>
  </linearGradient></defs>
  <rect x="20.0" y="62" width="60.0" height="26" fill="#cfc8bf" fill-opacity="0.45" stroke="currentColor" stroke-width="0.5"/>
  <rect x="80.0" y="62" width="60.0" height="26" fill="#5aa0d8" fill-opacity="0.45" stroke="currentColor" stroke-width="0.5"/>
  <rect x="140.0" y="62" width="62.5" height="26" fill="#cfc8bf" fill-opacity="0.45" stroke="currentColor" stroke-width="0.5"/>
  <rect x="208.0" y="62" width="32.0" height="26" fill="#5aa0d8" fill-opacity="0.45" stroke="currentColor" stroke-width="0.5"/>
  <rect x="240.0" y="62" width="60.0" height="26" fill="#cfc8bf" fill-opacity="0.45" stroke="currentColor" stroke-width="0.5"/>
  <rect x="300.0" y="62" width="20.0" height="26" fill="#5aa0d8" fill-opacity="0.45" stroke="currentColor" stroke-width="0.5"/>
  <rect x="202.6" y="62" width="5.8" height="26" fill="url(#l04vis)"/>
  <g font-size="8" fill="currentColor">
    <text x="50.0" y="80" text-anchor="middle">radio</text>
    <text x="110.0" y="52" text-anchor="middle">microwave</text>
    <text x="171.2" y="80" text-anchor="middle">infrared</text>
    <text x="224.0" y="80" text-anchor="middle">UV</text>
    <text x="270.0" y="80" text-anchor="middle">X-ray</text>
    <text x="310.0" y="52" text-anchor="middle">gamma</text>
    <line x1="110.0" y1="55" x2="110.0" y2="62" stroke="currentColor" stroke-width="0.5"/>
    <line x1="310.0" y1="55" x2="310.0" y2="62" stroke="currentColor" stroke-width="0.5"/>
    <line x1="20.0" y1="88" x2="20.0" y2="93" stroke="currentColor" stroke-width="0.7"/>
    <text x="20.0" y="102" text-anchor="middle">1 km</text>
    <line x1="80.0" y1="88" x2="80.0" y2="93" stroke="currentColor" stroke-width="0.7"/>
    <text x="80.0" y="102" text-anchor="middle">1 m</text>
    <line x1="140.0" y1="88" x2="140.0" y2="93" stroke="currentColor" stroke-width="0.7"/>
    <text x="140.0" y="102" text-anchor="middle">1 mm</text>
    <line x1="200.0" y1="88" x2="200.0" y2="93" stroke="currentColor" stroke-width="0.7"/>
    <text x="200.0" y="102" text-anchor="middle">1 µm</text>
    <line x1="260.0" y1="88" x2="260.0" y2="93" stroke="currentColor" stroke-width="0.7"/>
    <text x="260.0" y="102" text-anchor="middle">1 nm</text>
    <line x1="320.0" y1="88" x2="320.0" y2="93" stroke="currentColor" stroke-width="0.7"/>
    <text x="320.0" y="102" text-anchor="middle">1 pm</text>
    <text x="6" y="12">The electromagnetic spectrum: each step right is ten times shorter</text>
    <text x="6" y="30">longer waves, lower frequency,</text>
    <text x="6" y="40">less energy per photon</text>
    <text x="334" y="30" text-anchor="end">shorter waves, higher frequency,</text>
    <text x="334" y="40" text-anchor="end">more energy per photon</text>
    <path d="M202.6,88 L60,150 M208.4,88 L280,150" stroke="currentColor" stroke-width="0.5" fill="none" stroke-dasharray="2 2"/>
  </g>
  <rect x="60" y="150" width="220" height="22" fill="url(#l04vis)"/>
  <g font-size="8" fill="currentColor">
    <text x="60" y="184">740 nm</text>
    <text x="280" y="184" text-anchor="end">380 nm</text>
    <text x="170" y="184" text-anchor="middle">the light our eyes see</text>
    <text x="6" y="210">examples: radar at Mars (15 m); microwave oven (12 cm); your body glows</text>
    <text x="6" y="222">at about 10 µm; sunburn (ultraviolet); X-ray pictures in hospitals;</text>
    <text x="6" y="234">gamma rays from radium</text>
  </g>
</svg>
</div>

*Figure A. The electromagnetic spectrum. Each step to the right is ten times shorter. The light we see is the thin
coloured sliver, enlarged below.*

??? note "Sources"
    - Maxwell's equations predicting an unlimited range of frequencies, all travelling at the speed of light:
      Wikipedia, [Electromagnetic spectrum](https://en.wikipedia.org/wiki/Electromagnetic_spectrum) (weaker).
    - The hertz, one per second, named after Heinrich Hertz, adopted in 1960 in place of "cycles per second":
      Wikipedia, [Hertz](https://en.wikipedia.org/wiki/Hertz) (weaker).

## 4.2 Finding the invisible light { #found }

- **Infrared, 1800.** In England, William Herschel spread sunlight with a prism and found that a thermometer warmed
  up even beyond the red end (history book,
  [chapter 18, section 18.2](../history/18-Light-Split-into-Colours.md#invisible)). Slightly more than half of the
  Sun's energy reaches us as infrared.
- **Ultraviolet, 1801.** In February 1801, in Germany, Johann Ritter found that invisible rays just beyond the violet
  darkened paper soaked in silver chloride faster than violet light itself.
- **Radio, 1886 to 1888.** In Germany, Heinrich Hertz made and detected radio waves, measured their wavelength and
  frequency, and showed that they travel at the speed of light (chapter 1, section 1.6).
- **Millimetre waves, 1895.** In Kolkata, **Jagadish Chandra Bose** made radio waves only about 5 mm long, so that he
  could study how they behave like light. In November 1895, at Kolkata's Town Hall, he sent them through the body of
  the Lieutenant Governor and 23 metres through two walls, to ring a bell and set off gunpowder. He worked at
  frequencies as high as 60 GHz, with horn antennas and lenses, and much of his equipment is still at the Bose
  Institute in Kolkata.
- **X-rays, 1895.** On 8 November 1895, in Germany, **Wilhelm Röntgen** found a new, invisible radiation coming from
  a high-voltage tube. He called it X-radiation, X for unknown. His picture of his wife Anna Bertha Ludwig's hand was
  the first photograph of part of a human body taken with X-rays. He received the first Nobel Prize in Physics.
- **Gamma rays, 1900.** In France, **Paul Villard** found a very penetrating radiation coming from radium. Ernest
  Rutherford named it gamma rays in 1903. In 1914 Rutherford and Edward Andrade measured their wavelengths and found
  them to be like X-rays, only shorter.

??? note "Sources"
    - Herschel in 1800 and slightly more than half the Sun's energy as infrared: Wikipedia,
      [Infrared](https://en.wikipedia.org/wiki/Infrared) (weaker); this site's history book, chapter 18, section 18.2.
    - Ritter in February 1801 and silver chloride: Wikipedia,
      [Ultraviolet](https://en.wikipedia.org/wiki/Ultraviolet) (weaker).
    - Hertz from 1886, measuring wavelength and frequency, and Rutherford and Andrade's measurement of 1914:
      Wikipedia, [Electromagnetic spectrum](https://en.wikipedia.org/wiki/Electromagnetic_spectrum) (weaker).
    - Bose's waves of about 5 mm, the Town Hall demonstration of November 1895, 60 GHz, and his equipment at the Bose
      Institute: Wikipedia, [Jagadish Chandra Bose](https://en.wikipedia.org/wiki/Jagadish_Chandra_Bose) (weaker).
    - Röntgen on 8 November 1895, the name X-radiation, the picture of Anna Bertha Ludwig's hand, and the first Nobel
      Prize in Physics: Wikipedia, [X-ray](https://en.wikipedia.org/wiki/X-ray) (weaker).
    - Villard in 1900 and Rutherford's name of 1903: Wikipedia, [Gamma ray](https://en.wikipedia.org/wiki/Gamma_ray)
      (weaker).

## 4.3 The bands, from longest to shortest { #bands }

| Band | Wavelength | An example |
| --- | --- | --- |
| Radio | longer than about 1 mm | the radar on a Mars orbiter, 15 m |
| Microwave (the short end of radio) | about 1 m to 1 mm | a microwave oven, 12 cm |
| Infrared | 1 mm to 750 nm | your body glows at about 10 µm |
| Visible | about 740 to 380 nm | the colours of chapter 3 |
| Ultraviolet | about 400 to 10 nm | the cause of sunburn |
| X-rays | about 10 nm to 10 pm | X-ray pictures in hospitals |
| Gamma rays | shorter than about 10 pm | rays from radium |

Here µm is a micrometre, a thousandth of a millimetre, and pm is a picometre, a thousandth of a nanometre. The edges
between the bands are not sharp, and different books draw them in slightly different places.

??? note "Sources"
    - Radio below 300 GHz: Wikipedia, [Radio wave](https://en.wikipedia.org/wiki/Radio_wave) (weaker). Microwaves
      from about 1 m to 1 mm, and the microwave oven at 2.45 GHz, 12 cm: Wikipedia,
      [Microwave](https://en.wikipedia.org/wiki/Microwave) (weaker).
    - Infrared from 1 mm to 750 nm, and ultraviolet from about 400 to 10 nm: Wikipedia,
      [Electromagnetic spectrum](https://en.wikipedia.org/wiki/Electromagnetic_spectrum) (weaker). People glowing at
      around 10 µm: Wikipedia, [Infrared](https://en.wikipedia.org/wiki/Infrared) (weaker).
    - X-rays from 10 nm to 10 pm, and medical use: Wikipedia, [X-ray](https://en.wikipedia.org/wiki/X-ray) (weaker).
      The older boundary between X-rays and gamma rays at $10^{-11}$ m: Wikipedia,
      [Ionizing radiation](https://en.wikipedia.org/wiki/Ionizing_radiation) (weaker).
    - Sunburn: Wikipedia, [Ultraviolet](https://en.wikipedia.org/wiki/Ultraviolet) (weaker). The radar: section 4.7.

## 4.4 Small and large packets of energy { #energy }

Light comes in packets called photons (chapter 1, section 1.7), and a photon's energy is set by its frequency:

$$E = hf,$$

where $h$ is Planck's constant, fixed at exactly $6.62607015 \times 10^{-34}$ joule seconds. So a radio photon carries
very little energy, and a gamma-ray photon a great deal.

Gamma rays, X-rays and the shortest ultraviolet are called **ionising radiation**: each photon has enough energy to
knock an electron off an atom, which can set off chemical changes, including in living cells. Visible light and longer
waves are not ionising. There is no sharp line, but one common rule puts the boundary at a photon energy of 10
electronvolts, a wavelength of 124 nm (section 4.8).

Even the longer ultraviolet that reaches the ground does harm: it causes suntan and sunburn, and raises the risk of
skin cancer.

??? note "Sources"
    - Planck's constant, exactly $6.62607015 \times 10^{-34}$ J/Hz: Wikipedia,
      [Planck constant](https://en.wikipedia.org/wiki/Planck_constant) (weaker).
    - Gamma rays, X-rays and extreme ultraviolet as ionising radiation, and visible light as non-ionising: Wikipedia,
      [Electromagnetic spectrum](https://en.wikipedia.org/wiki/Electromagnetic_spectrum) (weaker).
    - The boundary not sharply defined, and the 10 eV, 124 nm definition used by the US Federal Communications
      Commission: Wikipedia, [Ionizing radiation](https://en.wikipedia.org/wiki/Ionizing_radiation) (weaker).
    - Suntan, sunburn and skin cancer: Wikipedia, [Ultraviolet](https://en.wikipedia.org/wiki/Ultraviolet) (weaker).

## 4.5 What gets through the air { #air }

The Earth's air lets only some kinds of light through. The parts of the spectrum that get through are called
**windows**, and there are three main ones: optical, infrared and radio.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="A sketch of how much of each kind of light the Earth's air blocks, from radio waves 100 metres long on the left to X-rays and gamma rays on the right. Radio waves longer than about 30 metres are blocked by the ionosphere. From about 30 metres down to about 0.3 millimetres the air is clear: the radio window. Most infrared is blocked, with patchy gaps caused by water vapour. From about 2 micrometres to 300 nanometres the air is clear again: the optical window, including the light we see. Ultraviolet shorter than about 300 nanometres is absorbed by ozone and oxygen, and X-rays and gamma rays are absorbed too. Telescopes on the ground can use the two windows; the blocked parts need telescopes in space.">
  <rect x="45" y="60" width="276" height="115" fill="#cfc8bf" fill-opacity="0.18"/>
  <polyline points="45.0,60 57.0,60 57.0,175 172.0,175 172.0,60 196.8,60 196.8,70 199.1,170 201.4,90 203.7,175 206.0,75 208.3,160 211.8,100 215.2,170 218.7,110 222.1,175 241.0,175 241.0,60 321.0,60" fill="none" stroke="#c1440e" stroke-width="1.6"/>
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">What the Earth's air lets through (a sketch)</text>
    <text x="42" y="63" text-anchor="end">blocked</text>
    <text x="42" y="178" text-anchor="end">clear</text>
    <text x="114.0" y="167" text-anchor="middle">radio window</text>
    <text x="209.5" y="46" text-anchor="middle">infrared: patchy,</text>
    <text x="209.5" y="56" text-anchor="middle">water vapour</text>
    <text x="231.3" y="187" text-anchor="middle">optical window</text>
    <text x="281.9" y="74" text-anchor="middle">UV, X-rays and</text>
    <text x="281.9" y="84" text-anchor="middle">gamma rays absorbed</text>
    <text x="61.0" y="74">ionosphere blocks longer waves</text>
    <line x1="68.0" y1="175" x2="68.0" y2="179" stroke="currentColor" stroke-width="0.7"/>
    <text x="68.0" y="199" text-anchor="middle">10 m</text>
    <line x1="137.0" y1="175" x2="137.0" y2="179" stroke="currentColor" stroke-width="0.7"/>
    <text x="137.0" y="199" text-anchor="middle">1 cm</text>
    <line x1="183.0" y1="175" x2="183.0" y2="179" stroke="currentColor" stroke-width="0.7"/>
    <text x="183.0" y="199" text-anchor="middle">0.1 mm</text>
    <line x1="229.0" y1="175" x2="229.0" y2="179" stroke="currentColor" stroke-width="0.7"/>
    <text x="229.0" y="199" text-anchor="middle">1 µm</text>
    <line x1="275.0" y1="175" x2="275.0" y2="179" stroke="currentColor" stroke-width="0.7"/>
    <text x="275.0" y="199" text-anchor="middle">10 nm</text>
    <line x1="321.0" y1="175" x2="321.0" y2="179" stroke="currentColor" stroke-width="0.7"/>
    <text x="321.0" y="199" text-anchor="middle">0.1 nm</text>
    <text x="6" y="221">Telescopes on the ground use the two windows. For the rest,</text>
    <text x="6" y="233">telescopes go up on balloons, rockets and satellites.</text>
  </g>
</svg>
</div>

*Figure B. A sketch of how much of each kind of light the Earth's air blocks.*

- **The optical window** runs from about 300 nm, through the light we see, to about 2 µm in the infrared.
- **The radio window** runs from waves about 30 m long (10 MHz) to about 0.3 mm (1 THz) at the best sites. Longer
  waves are turned back by the **ionosphere**, a layer of charged gas high above us.
- **Infrared** gets through only in patches, depending on water vapour and clouds.
- **Ultraviolet** shorter than about 300 nm is absorbed, mainly by ozone and oxygen. The ozone layer absorbs 97 to
  99 per cent of the Sun's ultraviolet between about 200 and 315 nm, which would otherwise harm life at the surface.
- **X-rays and gamma rays** are absorbed by the air. To see X-rays from space, instruments must go up on balloons,
  sounding rockets and satellites; even at balloon heights, X-rays with less than 35 thousand electronvolts of energy
  do not get through.

So radio and visible telescopes can sit on the ground (chapters 16 and 17), but ultraviolet, X-ray and gamma-ray
telescopes must go to space (chapters 18 and 19).

??? note "Sources"
    - Atmospheric windows, the optical, infrared and radio windows as the three main ones, and their dependence on
      clouds and water vapour: Wikipedia, [Atmospheric window](https://en.wikipedia.org/wiki/Atmospheric_window)
      (weaker).
    - The optical window from about 300 nm to about 2 µm: Wikipedia,
      [Optical window](https://en.wikipedia.org/wiki/Optical_window) (weaker).
    - The radio window from about 10 MHz to about 1 THz, and the ionosphere: Wikipedia,
      [Radio window](https://en.wikipedia.org/wiki/Radio_window) (weaker).
    - Ultraviolet shorter than about 300 nm absorbed by ozone and oxygen: Wikipedia,
      [Ultraviolet](https://en.wikipedia.org/wiki/Ultraviolet) (weaker). The ozone layer absorbing 97 to 99 per cent
      from about 200 to 315 nm: Wikipedia, [Ozone layer](https://en.wikipedia.org/wiki/Ozone_layer) (weaker).
    - X-rays absorbed, balloons, sounding rockets and satellites, and the 35 keV limit at balloon heights:
      Wikipedia, [X-ray astronomy](https://en.wikipedia.org/wiki/X-ray_astronomy) (weaker). Gamma rays largely
      absorbed: Wikipedia, [Gamma ray](https://en.wikipedia.org/wiki/Gamma_ray) (weaker).

## 4.6 What each band shows { #sky }

- **Microwaves: the glow of the young universe.** In 1964 Arno Penzias and Robert Wilson, radio astronomers at Bell
  Telephone Laboratories in New Jersey, found by accident a faint microwave glow coming from every direction. This
  **cosmic microwave background** has the spectrum of a body at 2.725 degrees above absolute zero, and is one of the
  main sources of information about the Big Bang.
- **Infrared: through the dust.** Infrared telescopes see into dusty regions of space such as the clouds where stars
  are born, find planets, and see very distant objects from the early days of the universe.
- **Ultraviolet: hot young stars.** Ultraviolet spectra tell astronomers the make-up, density and temperature of the
  gas between the stars, and the temperature and make-up of hot young stars.
- **X-rays: very hot gas.** X-rays come from gas at a million to hundreds of millions of degrees. The first X-ray
  source beyond the solar system, **Scorpius X-1**, was found by a rocket on 19 June 1962. It gives out 10,000 times
  more X-rays than visible light; the Sun gives out about a million times less.
- **Gamma rays: the biggest explosions.** On 2 July 1967, the Vela satellites, built to watch for nuclear weapons
  tests, picked up a flash of gamma rays unlike any bomb. It was the first **gamma-ray burst** found. Gamma-ray
  bursts are the most energetic events known after the Big Bang itself. They last from a few thousandths of a second to
  several hours, and satellites now catch about one a day.

??? note "Sources"
    - Penzias and Wilson in 1964 at Bell Telephone Laboratories, the accidental discovery, and 2.72548 K: Wikipedia,
      [Cosmic microwave background](https://en.wikipedia.org/wiki/Cosmic_microwave_background) (weaker). The CMB as a
      major source of information on the Big Bang: Wikipedia, [Microwave](https://en.wikipedia.org/wiki/Microwave)
      (weaker).
    - Infrared astronomy seeing into dusty regions such as molecular clouds, finding planets and seeing highly
      red-shifted objects: Wikipedia, [Infrared](https://en.wikipedia.org/wiki/Infrared) (weaker).
    - Ultraviolet spectroscopy of the interstellar medium and of hot young stars: Wikipedia,
      [Ultraviolet astronomy](https://en.wikipedia.org/wiki/Ultraviolet_astronomy) (weaker).
    - Hot gas from about a million to hundreds of millions of kelvin, Scorpius X-1 found on 19 June 1962, and its
      X-ray to visible ratio compared with the Sun's: Wikipedia,
      [X-ray astronomy](https://en.wikipedia.org/wiki/X-ray_astronomy) (weaker).
    - The Vela detection of 2 July 1967, the energies, the durations, and about one burst a day: Wikipedia,
      [Gamma-ray burst](https://en.wikipedia.org/wiki/Gamma-ray_burst) (weaker).

## 4.7 Mars in every kind of light { #mars }

- **Radio: talking to the rovers.** Curiosity has an X-band radio that can talk straight to the Earth at up to 32
  kilobits a second. But most of its data goes by UHF radio to the Mars Reconnaissance Orbiter and Mars Odyssey,
  which pass the rover for only about eight minutes a day each, at up to 2,000 and 256 kilobits a second, and pass it
  on to the Earth.
- **Radar: looking under the ground.** The Mars Reconnaissance Orbiter carries **SHARAD**, a radar working at 20 MHz,
  waves 15 m long. Its radio pulses go into the ground and echo back from layers below, mapping the top kilometre of
  Mars in steps of 15 m and searching for water ice. It has seen right through the ice layers at the north pole to the
  rock below. A second radar, MARSIS on Mars Express, goes deeper but sees less detail.
- **Infrared: warm and cold ground.** **THEMIS**, the camera on Mars Odyssey, measures the heat glowing from the
  surface at nine infrared wavelengths, with a detail of 100 m. Pictures taken at night show which ground holds its
  heat, which depends on the size of its grains, from fine dust to solid rock.
- **Ultraviolet: the top of the air.** **MAVEN**, which reached Mars on 22 September 2014, was the first NASA mission
  to study Mars's air. Its ultraviolet spectrometer measured the upper atmosphere, part of a study of how the solar
  wind strips the air away. MAVEN lost contact on 6 December 2025, and NASA declared its mission over on 3 June 2026.
- **Ultraviolet at the ground.** With so little air (chapter 3, section 3.10), the Sun's ultraviolet reaches the
  surface of Mars strongly. For the European rover, stained-glass colour chips were planned for checking the
  cameras' colours, because glass stays unfaded in that ultraviolet.

??? note "Sources"
    - Curiosity's X-band link at up to 32 kbit/s, its UHF radios, relay through the Mars Reconnaissance Orbiter and
      Odyssey at up to 2,000 and 256 kbit/s, and about eight minutes a day each: Wikipedia,
      [Curiosity (rover)](https://en.wikipedia.org/wiki/Curiosity_(rover)) (weaker).
    - SHARAD's 20 MHz, the first kilometre, 15 m resolution, water ice, the north polar layered deposits, and MARSIS
      going deeper with less detail: Wikipedia, [SHARAD](https://en.wikipedia.org/wiki/SHARAD) (weaker).
    - THEMIS on Mars Odyssey, nine thermal infrared wavelengths, 100 m resolution, and night images showing grain size
      through thermal inertia: Wikipedia,
      [Thermal Emission Imaging System](https://en.wikipedia.org/wiki/Thermal_Emission_Imaging_System) (weaker).
    - MAVEN's arrival on 22 September 2014, first NASA mission to study the Martian atmosphere, its Imaging
      Ultraviolet Spectrometer, the stripping by the solar wind, the loss of contact on 6 December 2025 and the end of
      the mission on 3 June 2026: Wikipedia, [MAVEN](https://en.wikipedia.org/wiki/MAVEN) (weaker).
    - Glass colour chips planned for a Mars rover so that they stay unfaded by the high ultraviolet at the surface:
      Wikipedia, [Ultraviolet](https://en.wikipedia.org/wiki/Ultraviolet) (weaker).

## 4.8 Working it out { #working }

**Frequency and wavelength.** $\lambda = c / f$, with $c = 299{,}792{,}458$ m/s.

- A microwave oven, 2.45 GHz: $299{,}792{,}458 / 2.45 \times 10^9 = 0.122$ m, about 12 cm.
- SHARAD, 20 MHz: $299{,}792{,}458 / 2 \times 10^7 = 15.0$ m.
- Bose's 60 GHz: $299{,}792{,}458 / 6 \times 10^{10} = 0.0050$ m, 5 mm.
- Going the other way, your body's glow at 10 µm: $f = c / \lambda = 3.0 \times 10^{13}$ Hz, 30 terahertz.

**Photon energy.** In electronvolts, $E = 1240 / \lambda$, with $\lambda$ in nanometres (chapter 1, section 1.11).

- The ionising boundary, 124 nm: $1240 / 124 = 10$ eV.
- Green light, 550 nm: $1240 / 550 = 2.25$ eV.
- An X-ray of 0.1 nm: $1240 / 0.1 = 12{,}400$ eV.
- A microwave-oven photon, $1.22 \times 10^8$ nm: $1.0 \times 10^{-5}$ eV, about 220,000 times less than green light.

| | Mars | Earth |
| --- | --- | --- |
| Air above each square metre | about 171 kg | about 10,300 kg |
| The Sun's ultraviolet at the ground | strong | shorter than about 300 nm absorbed |
| Radiation dose at the surface | about 0.64 mSv a day, 234 mSv a year | about 2.4 mSv a year from natural sources |

The dose on Mars is about 100 times the Earth's. Not all of it is light: the surface of Mars also gets a lot of
cosmic radiation, fast particles from space.

??? note "Sources"
    - The air above each square metre: chapter 3, section 3.10.
    - Ultraviolet: sections 4.5 and 4.7.
    - The radiation on the surface of Mars, on average 0.64 millisieverts a day, and high cosmic radiation: Wikipedia,
      [Mars](https://en.wikipedia.org/wiki/Mars) (weaker). The worldwide average natural dose of about 2.4 mSv a year:
      Wikipedia, [Background radiation](https://en.wikipedia.org/wiki/Background_radiation) (weaker).
    - The arithmetic is ours.

## 4.9 Counting photons { #photons }

A beam of power $P$ watts carries $P$ joules each second. Each photon carries $hf = hc/\lambda$ joules, so the number
of photons each second is

$$N = \frac{P}{hf} = \frac{P\lambda}{hc}, \qquad hc = 6.626 \times 10^{-34} \times 2.998 \times 10^8
= 1.986 \times 10^{-25} \text{ J m}.$$

- A 1 W green laser at 532 nm: $N = 532 \times 10^{-9} / 1.986 \times 10^{-25} = 2.7 \times 10^{18}$ photons a second.
- 1 W of radio at SHARAD's 20 MHz: $N = 1 / (6.626 \times 10^{-34} \times 2 \times 10^7) = 7.5 \times 10^{25}$
  photons a second, 28 million times as many.

For the same power, the longer the wave, the more photons there are, each carrying less.

**Sunlight.** At the Earth, sunlight brings 1,361 W to each square metre; at Mars, 586 W (chapter 1, section 1.9).
Sunlight is a mixture of wavelengths, but as a rough estimate pretend it is all at 550 nm:

$$N_\text{Earth} \approx \frac{1361 \times 550 \times 10^{-9}}{1.986 \times 10^{-25}} = 3.8 \times 10^{21}, \qquad
N_\text{Mars} \approx 1.6 \times 10^{21}$$

photons on each square metre every second.

??? note "Sources"
    - Planck's constant: section 4.4. The speed of light: chapter 2.
    - Sunlight at 1,361 and 586 W/m²: chapter 1, section 1.9, and its sources.
    - The arithmetic is ours.

## Check yourself { #check }

**1.** (beginner) Name the bands of the electromagnetic spectrum from the longest waves to the shortest.

??? note "Answer"
    Radio (including microwaves), infrared, visible, ultraviolet, X-rays, gamma rays.

**2.** (beginner) Who discovered X-rays, and when?

??? note "Answer"
    Wilhelm Röntgen, on 8 November 1895.

**3.** (beginner) Why can't an X-ray telescope work on the ground?

??? note "Answer"
    The air absorbs X-rays from space, so they never reach the ground.

**4.** (intermediate) Which kinds of light are ionising, and why are they dangerous?

??? note "Answer"
    Gamma rays, X-rays and the shortest ultraviolet. Each photon has enough energy to knock an electron off an atom,
    which can set off chemical changes in living cells.

**5.** (intermediate) How does SHARAD see under the surface of Mars?

??? note "Answer"
    It sends radio pulses, 15 m long waves at 20 MHz, into the ground and times the echoes from the layers below.

**6.** (intermediate) Why are infrared telescopes useful for looking at the clouds where stars are born?

??? note "Answer"
    Infrared gets through the dust that blocks visible light.

**7.** (advanced) Find the wavelength of a 100 MHz radio wave and the energy of one of its photons in electronvolts
($1 \text{ eV} = 1.602 \times 10^{-19}$ J).

??? note "Answer"
    $\lambda = 299{,}792{,}458 / 10^8 = 3.0$ m. $E = hf = 6.626 \times 10^{-34} \times 10^8 = 6.6 \times 10^{-26}$ J,
    which is $6.6 \times 10^{-26} / 1.602 \times 10^{-19} = 4.1 \times 10^{-7}$ eV.

**8.** (expert) How many photons a second are there in a 1 W X-ray beam of wavelength 0.1 nm? How does that compare
with the 1 W green laser?

??? note "Answer"
    $N = 0.1 \times 10^{-9} / 1.986 \times 10^{-25} = 5.0 \times 10^{14}$ a second, about 5,300 times fewer than the
    green laser's $2.7 \times 10^{18}$.

## Summary

- Radio waves, microwaves, infrared, visible light, ultraviolet, X-rays and gamma rays are all electromagnetic waves,
  travelling at the speed of light, with $c = f\lambda$.
- They were found one by one: infrared in 1800, ultraviolet in 1801, radio in the 1880s, millimetre waves and X-rays
  in 1895, gamma rays in 1900.
- A photon's energy is $E = hf$. Gamma rays, X-rays and the shortest ultraviolet are ionising.
- The Earth's air lets through visible light and radio waves, and some infrared. Ultraviolet, X-ray and gamma-ray
  astronomy needs space.
- Each band shows something different: the microwave glow of the Big Bang, dusty star nurseries, hot young stars, very
  hot gas and gamma-ray bursts.
- At Mars, spacecraft use radio to talk, radar to look underground, infrared to map warm and cold ground, and
  ultraviolet to study the top of the air.

**Next:** [chapter 5, Brighter and fainter: the inverse square law](05-The-Inverse-Square-Law.md), where we see why
light fades with distance.

## Further reading

- Bob Berman, *Zapped: From Infrared to X-rays, the Curious History of Invisible Light*, Little, Brown, 2017.
