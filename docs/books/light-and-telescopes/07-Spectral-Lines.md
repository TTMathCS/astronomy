# 7. Spectral lines, the fingerprints of the elements

*Spread out the light of a street lamp, a neon sign or a star, and you often find not a smooth rainbow but sharp
bright or dark lines. Each element makes its own pattern of lines, always in the same places, like a fingerprint. This
chapter explains the three kinds of spectrum, shows where the lines come from inside the atom, and follows the work of
Balmer, Bohr, Meghnad Saha and Cecilia Payne that turned the lines into a list of what the stars are made of. It meets
C. V. Raman's discovery in Calcutta, now carried to Mars on Perseverance, and the lasers that rovers use to read rocks
from metres away. It ends by working out hydrogen's lines from a single formula.*

!!! abstract "In this chapter"
    **You will learn:**

    - the three kinds of spectrum, and what makes each one
    - where you can see spectral lines on Earth
    - why atoms give out and take in light only at certain wavelengths
    - how hydrogen's lines were explained
    - how Saha and Payne found what the stars are made of
    - what the Raman effect is
    - how spectra revealed Mars's air, and how rovers read rocks with lasers
    - how to turn energy levels into wavelengths
    - how to work out hydrogen's lines with the Rydberg formula

    **You need:** chapters 1, 3 and 6. The physics lessons
    [Photons and energy levels](https://physics.akadian.ca/topics/waves/level-8/01-photons-and-energy-levels.html),
    [Emission lines](https://physics.akadian.ca/topics/waves/level-8/02-emission-lines.html) and
    [Absorption lines](https://physics.akadian.ca/topics/waves/level-8/03-absorption-lines.html) help.

    **Levels:** 7.1 to 7.3 are beginner; 7.4 to 7.7 are intermediate; 7.8 is advanced; 7.9 is expert.

## 7.1 Three kinds of spectrum { #three }

In 1859 and 1860, in Heidelberg, Gustav Kirchhoff worked out the rules (history book,
[chapter 18, section 18.4](../history/18-Light-Split-into-Colours.md#elements)). There are three kinds of spectrum:

- **Continuous.** A hot, dense body, like a glowing wire or the inside of a star, gives a smooth band of all colours
  (chapter 6).
- **Bright lines.** A hot, thin gas gives light only at a few sharp wavelengths: an **emission spectrum**.
- **Dark lines.** When light from a hot body passes through a cooler gas, the gas takes out light at exactly the same
  wavelengths that it would give out when hot: an **absorption spectrum**.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Three kinds of spectrum, one above the other, from violet at 380 nanometres on the left to red at 700 on the right. Top: a continuous spectrum, an unbroken band of colours, from a hot, dense glowing body. Middle: an emission spectrum, black except for four bright coloured lines at 410, 434, 486 and 656 nanometres, from hot, thin hydrogen gas. Bottom: an absorption spectrum, the full band of colours crossed by four dark lines at exactly the same places, from a hot body seen through cooler hydrogen gas.">
  <defs><linearGradient id="l07spec" x1="0" x2="1" y1="0" y2="0">
    <stop offset="0.0000" stop-color="#4c004c"/>
    <stop offset="0.0625" stop-color="#6e00a5"/>
    <stop offset="0.1250" stop-color="#5500ff"/>
    <stop offset="0.1875" stop-color="#0000ff"/>
    <stop offset="0.2500" stop-color="#0066ff"/>
    <stop offset="0.3125" stop-color="#00ccff"/>
    <stop offset="0.3750" stop-color="#00ff7f"/>
    <stop offset="0.4375" stop-color="#24ff00"/>
    <stop offset="0.5000" stop-color="#6dff00"/>
    <stop offset="0.5625" stop-color="#b6ff00"/>
    <stop offset="0.6250" stop-color="#ffff00"/>
    <stop offset="0.6875" stop-color="#ffb000"/>
    <stop offset="0.7500" stop-color="#ff6200"/>
    <stop offset="0.8125" stop-color="#ff1300"/>
    <stop offset="0.8750" stop-color="#ff0000"/>
    <stop offset="0.9375" stop-color="#ff0000"/>
    <stop offset="1.0000" stop-color="#ff0000"/>
  </linearGradient></defs>
  <rect x="30" y="40" width="280" height="30" fill="url(#l07spec)"/>
  <rect x="30" y="110" width="280" height="30" fill="#111"/>
  <rect x="55.2" y="110" width="2.4" height="30" fill="#6800d3"/>
  <rect x="76.0" y="110" width="2.4" height="30" fill="#1900ff"/>
  <rect x="121.6" y="110" width="2.4" height="30" fill="#00ebff"/>
  <rect x="270.6" y="110" width="2.4" height="30" fill="#ff0000"/>
  <rect x="30" y="180" width="280" height="30" fill="url(#l07spec)"/>
  <rect x="55.2" y="180" width="2.4" height="30" fill="#111"/>
  <rect x="76.0" y="180" width="2.4" height="30" fill="#111"/>
  <rect x="121.6" y="180" width="2.4" height="30" fill="#111"/>
  <rect x="270.6" y="180" width="2.4" height="30" fill="#111"/>
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">Three kinds of spectrum</text>
    <text x="30" y="35">continuous: a hot, dense body (chapter 6)</text>
    <text x="30" y="105">bright lines: hot, thin hydrogen gas</text>
    <text x="30" y="175">dark lines: a hot body seen through cooler hydrogen</text>
    <text x="56.4" y="152" text-anchor="middle">410</text>
    <text x="77.2" y="152" text-anchor="middle">434</text>
    <text x="122.8" y="152" text-anchor="middle">486</text>
    <text x="271.8" y="152" text-anchor="middle">656</text>
    <text x="30" y="224">380 nm</text>
    <text x="310" y="224" text-anchor="end">700 nm</text>
    <text x="170" y="240" text-anchor="middle">same lines, same places: the fingerprint of hydrogen</text>
  </g>
</svg>
</div>

*Figure A. The three kinds of spectrum. Hydrogen's bright lines and dark lines fall in exactly the same places.*

The Sun's spectrum is of the third kind. Joseph von Fraunhofer mapped hundreds of its dark lines in 1814, and modern
instruments find many thousands. They are made by the gases in the Sun's outer layers.

??? note "Sources"
    - Kirchhoff's statements of 1859 and 1860: Wikipedia,
      [Kirchhoff's law of thermal radiation](https://en.wikipedia.org/wiki/Kirchhoff%27s_law_of_thermal_radiation)
      (weaker).
    - Emission and absorption lines, and absorption lines made when light from a hot, broad source passes through a
      cooler material: Wikipedia, [Spectral line](https://en.wikipedia.org/wiki/Spectral_line) (weaker).
    - Fraunhofer's lines and many thousands detected today: Wikipedia,
      [Fraunhofer lines](https://en.wikipedia.org/wiki/Fraunhofer_lines) (weaker); this site's history book,
      chapter 18, section 18.3.

## 7.2 Lines you can see on Earth { #everyday }

- **Street lamps.** Sodium lamps glow at almost a single wavelength, near 589 nm, a yellow-orange. The Sun's dark
  D lines, at the same place, are made by sodium too. Low-pressure sodium lamps were preferred near observatories,
  because they give out light on just two strong lines, close together near 589 nm.
- **Neon signs.** In December 1910, at the Paris Motor Show, the French engineer Georges Claude showed neon tube
  lighting much as we know it. Neon glows orange; other gases give other colours, such as hydrogen purple-red and
  helium yellow or pink.
- **Flame tests.** Sprinkle a salt into a hot, clear flame and the flame takes on the colour of the metal in it.
  Robert Bunsen's burner of 1855, with its almost colourless flame, made such tests easy. With flames and a
  spectroscope, Bunsen and Kirchhoff found two new elements.
- **Auroras.** The green of an aurora is oxygen glowing at 557.7 nm. Higher up, oxygen glows red at 630 nm, and lower
  down nitrogen adds blue and purple.

??? note "Sources"
    - Sodium lamps near 589 nm, monochromatic yellow-orange, low-pressure sodium preferred near observatories, and
      its two dominant lines:
      Wikipedia, [Sodium-vapor lamp](https://en.wikipedia.org/wiki/Sodium-vapor_lamp) (weaker). The sodium D lines at
      589.29 nm: Wikipedia, [Fraunhofer lines](https://en.wikipedia.org/wiki/Fraunhofer_lines) (weaker).
    - Georges Claude at the Paris Motor Show, 3 to 18 December 1910, and the colours of neon, hydrogen and helium:
      Wikipedia, [Neon lighting](https://en.wikipedia.org/wiki/Neon_lighting) (weaker).
    - Bunsen's burner of 1855 and its non-luminous flame: Wikipedia,
      [Flame test](https://en.wikipedia.org/wiki/Flame_test) (weaker). Caesium and rubidium: this site's history book,
      chapter 18, section 18.4.
    - Oxygen at 557.7 nm and 630 nm, and nitrogen: Wikipedia, [Aurora](https://en.wikipedia.org/wiki/Aurora) (weaker).

## 7.3 Why lines? { #why }

An electron in an atom cannot have just any energy. It can only sit on certain **energy levels**, like the rungs of a
ladder. When it drops from a higher rung to a lower one, the atom gives out one photon whose energy is exactly the gap
between the rungs. Since $E = hf$ (chapter 4), a fixed energy means a fixed frequency and a fixed wavelength: a sharp
line. When light passes through the gas, an electron can also jump up by taking in a photon with exactly the right
energy, and that wavelength goes missing: a dark line.

Every element has its own ladder, so every element has its own lines.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The energy levels of a hydrogen atom drawn as the rungs of a ladder, crowding together towards the top. The second level is at minus 3.4 electronvolts, the third at minus 1.51, the fourth at minus 0.85, the fifth at minus 0.54 and the sixth at minus 0.38; the ground level, at minus 13.6, is far below the bottom of the picture. Arrows show an electron dropping from levels 3, 4, 5 and 6 down to level 2. Each drop gives out a photon: from 3 to 2, red light at 656 nanometres; from 4 to 2, blue-green at 486; from 5 to 2, blue at 434; from 6 to 2, violet at 410. Bigger drops give more energetic photons with shorter wavelengths.">
  <g font-size="8" fill="currentColor">
    <line x1="60" y1="200.6" x2="300" y2="200.6" stroke="currentColor" stroke-width="1.2"/>
    <text x="56" y="203.6" text-anchor="end">n = 2, −3.40 eV</text>
    <line x1="60" y1="111.4" x2="300" y2="111.4" stroke="currentColor" stroke-width="1.2"/>
    <text x="56" y="114.4" text-anchor="end">n = 3, −1.51 eV</text>
    <line x1="60" y1="80.1" x2="300" y2="80.1" stroke="currentColor" stroke-width="1.2"/>
    <text x="56" y="83.1" text-anchor="end">n = 4, −0.85 eV</text>
    <line x1="60" y1="65.7" x2="300" y2="65.7" stroke="currentColor" stroke-width="1.2"/>
    <text x="56" y="68.7" text-anchor="end">n = 5, −0.54 eV</text>
    <line x1="60" y1="57.8" x2="300" y2="57.8" stroke="currentColor" stroke-width="1.2"/>
    <text x="56" y="60.8" text-anchor="end">n = 6, −0.38 eV</text>
    <line x1="60" y1="53.1" x2="300" y2="53.1" stroke="currentColor" stroke-width="0.5"/>
    <line x1="60" y1="50.0" x2="300" y2="50.0" stroke="currentColor" stroke-width="0.5"/>
    <line x1="60" y1="40.0" x2="300" y2="40.0" stroke="currentColor" stroke-width="0.6" stroke-dasharray="3 2"/>
    <text x="56" y="43.0" text-anchor="end">0 eV, free</text>
    <line x1="100" y1="111.4" x2="100" y2="194.6" stroke="#ff0000" stroke-width="2"/>
    <path d="M96,193.6 L100,200.6 L104,193.6" fill="#ff0000"/>
    <text x="100" y="214.6" text-anchor="middle">656 nm</text>
    <line x1="150" y1="80.1" x2="150" y2="194.6" stroke="#00ebff" stroke-width="2"/>
    <path d="M146,193.6 L150,200.6 L154,193.6" fill="#00ebff"/>
    <text x="150" y="214.6" text-anchor="middle">486 nm</text>
    <line x1="200" y1="65.7" x2="200" y2="194.6" stroke="#1900ff" stroke-width="2"/>
    <path d="M196,193.6 L200,200.6 L204,193.6" fill="#1900ff"/>
    <text x="200" y="214.6" text-anchor="middle">434 nm</text>
    <line x1="250" y1="57.8" x2="250" y2="194.6" stroke="#6800d3" stroke-width="2"/>
    <path d="M246,193.6 L250,200.6 L254,193.6" fill="#6800d3"/>
    <text x="250" y="214.6" text-anchor="middle">410 nm</text>
    <text x="6" y="12">Hydrogen's energy ladder: drops to level 2 give visible light</text>
    <text x="180" y="230.6" text-anchor="middle">level 1, −13.6 eV, is far below</text>
  </g>
</svg>
</div>

*Figure B. Hydrogen's energy levels. Drops to level 2 give its four visible lines.*

In 1913 Niels Bohr made the first model of the atom that worked this way. He linked the lines of
hydrogen with jumps between the orbits of its electron. His picture of electrons circling like planets was later
replaced, but the energy levels and the jumps between them remain.

??? note "Sources"
    - Spectral lines from the interaction between atoms and single photons: Wikipedia,
      [Spectral line](https://en.wikipedia.org/wiki/Spectral_line) (weaker).
    - Bohr's model of 1913, connecting the spectral lines with the orbits of electrons and explaining the Rydberg
      formula by jumps between levels, and its replacement: Wikipedia,
      [Bohr model](https://en.wikipedia.org/wiki/Bohr_model) (weaker).

## 7.4 Hydrogen's lines { #hydrogen }

Hydrogen, the simplest atom, has four lines in the visible: **410, 434, 486 and 656 nm**. The red one at 656 nm is
called **H-alpha**, the next H-beta, and so on.

- **Balmer, 1885.** Johann Balmer found a simple formula that gave all four wavelengths, without knowing why it
  worked.
- **Rydberg, 1888.** The Swedish physicist Johannes Rydberg found a more general formula that worked for other series
  of lines too (section 7.9).
- **Bohr, 1913.** Bohr explained the formula: each line is a jump between two levels of the atom (section 7.3).

Hydrogen also has lines in the ultraviolet, from drops to level 1, and in the infrared, from drops to level 3 and
above. Because the stars are mostly hydrogen (section 7.5), its lines are among the most important in astronomy.

??? note "Sources"
    - Balmer's formula of 1885, the four visible lines at 410, 434, 486 and 656 nm, and the names H-alpha and H-beta:
      Wikipedia, [Balmer series](https://en.wikipedia.org/wiki/Balmer_series) (weaker).
    - Rydberg in 1888 and Bohr in 1913: Wikipedia, [Rydberg formula](https://en.wikipedia.org/wiki/Rydberg_formula)
      (weaker).
    - The other series: Wikipedia, [Hydrogen spectral series](https://en.wikipedia.org/wiki/Hydrogen_spectral_series)
      (weaker). Stars made mostly of hydrogen: section 7.5.

## 7.5 What the stars are made of { #stars }

By the early 1920s the Harvard astronomers had sorted more than 200,000 stars by their spectra into the classes O, B,
A, F, G, K, M (history book, chapter 18, section 18.6; book 1, chapter 5). But why did the spectra differ? Were the
stars made of different things?

- **Saha, 1920.** The Indian physicist **Meghnad Saha** showed that the answer is mostly **temperature**. In a hotter
  star, more of the atoms have lost electrons, and that changes which lines they can make. His **ionisation equation**
  let astronomers link the spectral classes of stars to their actual temperatures (history book,
  [chapter 5, section 5.10](../history/05-India.md#exchange)).
- **Payne, 1925.** At Harvard College Observatory, **Cecilia Payne** used Saha's theory on the spectra of stars. In her
  doctoral thesis of 1925 she concluded that the stars are made mostly of **hydrogen and helium**. Leading astronomers,
  including Henry Norris Russell, at first rejected the idea, because it was thought that the Sun and the Earth were
  made of much the same things. Nearly 40 years later the astronomer Otto Struve called it "the most brilliant PhD
  thesis ever written in astronomy".

??? note "Sources"
    - Saha's ionisation equation of 1920, relating spectral classes to temperatures: Wikipedia,
      [Meghnad Saha](https://en.wikipedia.org/wiki/Meghnad_Saha) (weaker); Wikipedia,
      [Saha ionization equation](https://en.wikipedia.org/wiki/Saha_ionization_equation) (weaker).
    - Payne's use of Saha's theory at Harvard, her thesis of 1925, Russell's rejection, and Struve's words: Wikipedia,
      [Cecilia Payne-Gaposchkin](https://en.wikipedia.org/wiki/Cecilia_Payne-Gaposchkin) (weaker).
    - The Harvard classes: this site's history book, chapter 18, section 18.6.

## 7.6 Light that changes colour: the Raman effect { #raman }

On 28 February 1928, in Calcutta, **C. V. Raman** and **K. S. Krishnan** found that when light passes through a
transparent material, a little of the scattered light comes out with a changed wavelength. The molecules of the
material have taken a little energy from the light, or given some to it, as they vibrate. In 1930 Raman received the
Nobel Prize in Physics, the first Asian to do so. India celebrates 28 February as National Science Day.

Each kind of molecule vibrates in its own way, so the changed wavelengths give a fingerprint of the molecule. This is
**Raman spectroscopy**. Today it is done by shining a laser of one colour on a sample and looking for the faint light
with new colours.

??? note "Sources"
    - The discovery on 28 February 1928, Krishnan's finding that the deflected light changes its wavelength, the Nobel
      Prize of 1930, the first Asian, and National Science Day: Wikipedia,
      [C. V. Raman](https://en.wikipedia.org/wiki/C._V._Raman) (weaker).
    - Raman scattering, vibrational modes of molecules, the structural fingerprint and the laser source: Wikipedia,
      [Raman spectroscopy](https://en.wikipedia.org/wiki/Raman_spectroscopy) (weaker).

## 7.7 Reading Mars with spectra { #mars }

**The air of Mars, seen from Earth.** Spectra taken in the 1860s and 1870s led many to think that Mars's air was much
like the Earth's. But in 1894 William Wallace Campbell's spectra suggested that Mars was more like the Moon, with
little air. In 1964 Lewis Kaplan and his team found the lines of water
vapour and carbon dioxide in Mars's spectrum. The next year Mariner 4 flew past and confirmed that the air is mostly
carbon dioxide, at a surface pressure of only about 400 to 700 Pa.

**Lasers that read rocks.** Curiosity's **ChemCam**, built by Los Alamos National Laboratory and a French laboratory,
fires about 30 very short pulses from an infrared laser at a rock up to 7 m away. The laser turns a speck of rock into
a tiny ball of glowing gas, and a spectrometer reads its bright lines, from 240 to 800 nm, to tell which elements are
in it. Perseverance's **SuperCam**, built in France, the United States and Spain, does the same at targets as small as
a grain of rice more than 7 m away, and adds Raman and infrared spectrometers and a microphone.

**Raman on Mars.** Perseverance's **SHERLOC** shines an ultraviolet laser, at 248.6 nm, on rock and looks for the
Raman fingerprints of minerals and organic chemicals: Raman's discovery from Calcutta, working on another planet.

**The methane puzzle.** Several missions and telescopes have reported small amounts of methane in Mars's air, which
some think could be a sign of life. But the ExoMars Trace Gas Orbiter, built by Europe and Russia and in
orbit since 2016, carries the most sensitive methane spectrometers yet sent to Mars and has failed to find it across
the planet. India's Mars Orbiter Mission also carried a Methane Sensor for Mars.

??? note "Sources"
    - The spectra of the 1860s and 1870s, Campbell in 1894, Kaplan's team in 1964, and Mariner 4 in 1965 with 400 to
      700 Pa: Wikipedia, [Atmosphere of Mars](https://en.wikipedia.org/wiki/Atmosphere_of_Mars) (weaker). The methane
      reports and the Trace Gas Orbiter's failure to find it: the same page.
    - ChemCam's makers, its 7 m range, about 30 5-nanosecond pulses from a 1067 nm laser, and the plasma seen from
      240 to 800 nm: Wikipedia, [ChemCam](https://en.wikipedia.org/wiki/ChemCam) (weaker).
    - SuperCam's makers, its 1064 nm laser reaching a grain of rice beyond 7 m, its Raman and infrared spectrometers and
      its microphone: Wikipedia, [SuperCam](https://en.wikipedia.org/wiki/SuperCam) (weaker).
    - SHERLOC's ultraviolet Raman spectrometer and its 248.6 nm laser: Wikipedia,
      [SHERLOC](https://en.wikipedia.org/wiki/SHERLOC) (weaker).
    - The Trace Gas Orbiter, from ESA and Roscosmos, in orbit since 19 October 2016, its spectrometers and its methane
      goal: Wikipedia, [Trace Gas Orbiter](https://en.wikipedia.org/wiki/Trace_Gas_Orbiter) (weaker). The Methane
      Sensor for Mars: Wikipedia, [Mars Orbiter Mission](https://en.wikipedia.org/wiki/Mars_Orbiter_Mission) (weaker).
    - The physics lesson
      [Reading rocks with lasers](https://physics.akadian.ca/topics/waves/level-8/05-reading-rocks-with-lasers.html).

## 7.8 Working it out { #working }

**From energy to wavelength.** A photon of energy $E$ electronvolts has wavelength $\lambda = 1240 / E$ nm
(chapter 1, section 1.11), and the other way round, $E = 1240 / \lambda$.

| Line | Wavelength | Photon energy |
| --- | --- | --- |
| Hydrogen, H-alpha | 656.3 nm | 1.89 eV |
| Sodium, D | 589.3 nm | 2.10 eV |
| Oxygen, green aurora | 557.7 nm | 2.22 eV |
| Oxygen, red aurora | 630.0 nm | 1.97 eV |
| SHERLOC's laser | 248.6 nm | 4.99 eV |

**Hydrogen's levels.** In hydrogen, level $n$ has energy $E_n = -13.6 / n^2$ eV. A drop from level 3 to level 2 gives

$$13.6 \left(\frac{1}{2^2} - \frac{1}{3^2}\right) = 13.6 \times \frac{5}{36} = 1.889 \text{ eV}, \qquad
\lambda = \frac{1240}{1.889} = 656 \text{ nm},$$

which is H-alpha.

| | Mars | Earth |
| --- | --- | --- |
| Carbon dioxide | 95.1% | 0.042% (420 parts per million) |
| Nitrogen | 2.59% | 78.08% |
| Argon | 1.94% | 0.93% |
| Oxygen | 0.16% | 20.95% |

??? note "Sources"
    - Wavelengths: sections 7.2, 7.4 and 7.7.
    - $E_n \approx -13.6/n^2$ eV: Wikipedia, [Bohr model](https://en.wikipedia.org/wiki/Bohr_model) (weaker).
    - The make-up of the air: NASA, [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html)
      and [Earth Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html) (argon 9,340 ppm, carbon
      dioxide 420 ppm). Mars's air found by spectra: section 7.7.
    - The arithmetic is ours.

## 7.9 The Rydberg formula { #rydberg }

All of hydrogen's lines come from one formula. A drop from level $n_2$ down to level $n_1$ gives a line of wavelength
$\lambda$, where

$$\frac{1}{\lambda} = R \left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right),
\qquad R = 1.0968 \times 10^7 \text{ per metre}.$$

For the visible lines, $n_1 = 2$:

| Drop | $\frac{1}{4} - \frac{1}{n_2^2}$ | Wavelength |
| --- | --- | --- |
| 3 to 2 | $5/36 = 0.1389$ | 656.5 nm |
| 4 to 2 | $3/16 = 0.1875$ | 486.3 nm |
| 5 to 2 | $21/100 = 0.2100$ | 434.2 nm |
| 6 to 2 | $8/36 = 0.2222$ | 410.3 nm |

These come out a little longer than the 656.3 and 486.1 nm measured in air, because the formula gives wavelengths in
a vacuum, and air slows light very slightly (chapter 2).

- As $n_2$ grows, the lines crowd together towards a limit: $1/\lambda = R/4$, so $\lambda = 364.7$ nm, in the
  ultraviolet.
- With $n_1 = 1$, the drop from 2 to 1 gives $1/\lambda = R \times 3/4$, $\lambda = 121.6$ nm: the strongest
  ultraviolet line of hydrogen, which only telescopes above the air can see (chapter 4).
- With $n_1 = 3$, the drop from 4 to 3 gives $\lambda = 1{,}876$ nm, in the infrared.

The formula ties back to the energy levels: $hc R = 13.6$ eV.

??? note "Sources"
    - The Rydberg formula, Rydberg in 1888 and Bohr in 1913: Wikipedia,
      [Rydberg formula](https://en.wikipedia.org/wiki/Rydberg_formula) (weaker).
    - The hydrogen series: Wikipedia, [Hydrogen spectral series](https://en.wikipedia.org/wiki/Hydrogen_spectral_series)
      (weaker).
    - The arithmetic is ours.

## Check yourself { #check }

**1.** (beginner) What kind of spectrum does a hot, thin gas give?

??? note "Answer"
    Bright lines on a dark background: an emission spectrum.

**2.** (beginner) What colour is a low-pressure sodium street lamp, and why do astronomers like it?

??? note "Answer"
    Yellow-orange, near 589 nm. It gives out light on just two strong lines close together, so it does less harm
    near observatories.

**3.** (beginner) Why does each element have its own lines?

??? note "Answer"
    Each element has its own set of energy levels, and its lines come from jumps between them.

**4.** (intermediate) What did Meghnad Saha show about the spectra of stars?

??? note "Answer"
    That the differences between them are mainly due to temperature, which controls how many atoms have lost
    electrons. His equation linked spectral classes to real temperatures.

**5.** (intermediate) What did Cecilia Payne find in 1925, and why was it doubted?

??? note "Answer"
    That the stars are mostly hydrogen and helium. It was thought that the Sun was made of much the same things as the
    Earth.

**6.** (intermediate) How does ChemCam find out what a rock is made of from 7 m away?

??? note "Answer"
    Its laser turns a speck of the rock into glowing gas, and a spectrometer reads the bright lines of the elements in
    that gas.

**7.** (advanced) What is the energy of a photon of the green aurora line, 557.7 nm, and of SuperCam's 1064 nm laser?

??? note "Answer"
    $1240 / 557.7 = 2.22$ eV and $1240 / 1064 = 1.17$ eV.

**8.** (expert) Use the Rydberg formula to find the wavelength of the drop from level 5 to level 3 of hydrogen. In
which band is it?

??? note "Answer"
    $1/\lambda = 1.0968 \times 10^7 \times (1/9 - 1/25) = 1.0968 \times 10^7 \times 0.07111 = 7.800 \times 10^5$ per
    metre, so $\lambda = 1{,}282$ nm, in the infrared.

## Summary

- A hot, dense body gives a continuous spectrum; a hot, thin gas gives bright lines; a cooler gas in front of a hot
  source gives dark lines at the same places.
- Sodium lamps, neon signs, flame tests and auroras all show spectral lines.
- Electrons in atoms sit on fixed energy levels; jumps between them give photons of fixed wavelength.
- Hydrogen's visible lines are at 410, 434, 486 and 656 nm; Balmer, Rydberg and Bohr explained them.
- Saha showed that temperature controls stellar spectra, and Payne used his theory to find that stars are mostly
  hydrogen and helium.
- Raman found light that changes wavelength in 1928; Perseverance's SHERLOC uses his effect on Mars.
- Spectra revealed Mars's carbon dioxide air in 1964; rovers read rocks with lasers; methane remains a puzzle.
- $1/\lambda = R(1/n_1^2 - 1/n_2^2)$ gives all of hydrogen's lines.

**Next:** chapter 8, The Doppler shift, where we see how lines move when a star moves.

## Further reading

- Donovan Moore, *What Stars Are Made Of: The Life of Cecilia Payne-Gaposchkin*, Harvard University Press, 2020.
