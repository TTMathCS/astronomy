# 15. Spectrographs

*Chapters 7 and 8 showed how much a spectrum can tell us: what a star is made of, how hot it is, and how fast it is
moving. This chapter is about the instrument that makes the spectrum, the spectrograph. It explains its four parts,
how a grating spreads light far more than a prism, and how finely a spectrograph can split colours. It tells how hairs
strung between two screws in Philadelphia led to the gratings that now measure stars wobbling by a few centimetres
a second, how a Japanese design folds a long spectrum into stripes, and how robots now place thousands of fibres
to take thousands of spectra at once. It ends with the spectrometers that found clays on Mars.*

!!! abstract "In this chapter"
    **You will learn:**

    - the four parts of a spectrograph and what each does
    - how a diffraction grating spreads light, and the history of gratings
    - what resolving power is, and how much each job needs
    - how an echelle spectrograph works
    - how astronomers take thousands of spectra at once
    - how one instrument can take a spectrum of every point in an image
    - how the Sun is photographed in the light of a single line
    - what spectrometers orbiting Mars have found
    - why your own planet's motion must be taken out of every measurement

    **You need:** chapters 3, 7, 8 and 11. The physics lessons
    [The diffraction grating](https://physics.akadian.ca/topics/waves/level-8/04-the-diffraction-grating.html) and
    [Doppler shifts of light](https://physics.akadian.ca/topics/waves/level-8/06-doppler-shifts-of-light.html) help.

    **Levels:** 15.1 to 15.3 are beginner; 15.4 to 15.8 are intermediate; 15.9 is advanced; 15.10 is expert.

## 15.1 Four parts { #parts }

In 1814 Joseph von Fraunhofer found the dark lines in sunlight that are named after him, and he invented the
**spectroscope** (history book, [chapter 18, section 18.3](../history/18-Light-Split-into-Colours.md#lines)). The
early spectroscopes already had the parts every spectrograph has.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The parts of a spectrograph, with light travelling from left to right. Light from the telescope comes to a focus on a narrow slit. Beyond it the light spreads out until a collimator lens makes the rays parallel. The parallel beam strikes a diffraction grating, which sends each colour off at a slightly different angle: blue, orange and red beams are drawn. A camera lens then focuses each colour to a different point on the detector, so the slit is imaged once for every wavelength, side by side, making the spectrum.">
  <g font-size="8" fill="currentColor">
    <line x1="5" y1="125" x2="335" y2="125" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <line x1="8" y1="103" x2="40" y2="125" stroke="#cfc8bf" stroke-width="1"/>
    <line x1="8" y1="147" x2="40" y2="125" stroke="#cfc8bf" stroke-width="1"/>
    <line x1="40" y1="95" x2="40" y2="123" stroke="currentColor" stroke-width="2.5"/>
    <line x1="40" y1="127" x2="40" y2="155" stroke="currentColor" stroke-width="2.5"/>
    <path d="M100,91 Q110,125 100,159 Q90,125 100,91 Z" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="1"/>
    <path d="M210,81 Q222,125 210,169 Q198,125 210,81 Z" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="1"/>
    <polyline points="40,125 100,105 150,105" fill="none" stroke="#cfc8bf" stroke-width="1"/>
    <polyline points="40,125 100,145 150,145" fill="none" stroke="#cfc8bf" stroke-width="1"/>
    <line x1="150" y1="91" x2="150" y2="159" stroke="currentColor" stroke-width="1.5"/>
    <line x1="150" y1="93" x2="153" y2="93" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="97" x2="153" y2="97" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="101" x2="153" y2="101" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="105" x2="153" y2="105" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="109" x2="153" y2="109" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="113" x2="153" y2="113" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="117" x2="153" y2="117" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="121" x2="153" y2="121" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="125" x2="153" y2="125" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="129" x2="153" y2="129" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="133" x2="153" y2="133" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="137" x2="153" y2="137" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="141" x2="153" y2="141" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="145" x2="153" y2="145" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="149" x2="153" y2="149" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="153" x2="153" y2="153" stroke="currentColor" stroke-width="0.6"/>
    <line x1="150" y1="157" x2="153" y2="157" stroke="currentColor" stroke-width="0.6"/>
    <polyline points="150,105 210,90.0 290,105.1" fill="none" stroke="#5aa0d8" stroke-width="1"/>
    <polyline points="150,145 210,130.0 290,105.1" fill="none" stroke="#5aa0d8" stroke-width="1"/>
    <rect x="289" y="102.1" width="5" height="6" fill="#5aa0d8"/>
    <polyline points="150,105 210,105.0 290,125.0" fill="none" stroke="#eea66f" stroke-width="1"/>
    <polyline points="150,145 210,145.0 290,125.0" fill="none" stroke="#eea66f" stroke-width="1"/>
    <rect x="289" y="122.0" width="5" height="6" fill="#eea66f"/>
    <polyline points="150,105 210,120.0 290,144.9" fill="none" stroke="#c1440e" stroke-width="1"/>
    <polyline points="150,145 210,160.0 290,144.9" fill="none" stroke="#c1440e" stroke-width="1"/>
    <rect x="289" y="141.9" width="5" height="6" fill="#c1440e"/>
    <rect x="290" y="75" width="4" height="100" fill="none" stroke="currentColor" stroke-width="1"/>
    <text x="40" y="167" text-anchor="middle">slit</text>
    <text x="100" y="173" text-anchor="middle">collimator</text>
    <text x="100" y="183" text-anchor="middle">makes rays parallel</text>
    <text x="150" y="85" text-anchor="middle">grating</text>
    <text x="158" y="201" text-anchor="middle">sends each colour</text>
    <text x="158" y="211" text-anchor="middle">a different way</text>
    <text x="210" y="183" text-anchor="middle">camera lens</text>
    <text x="292" y="69" text-anchor="middle">detector</text>
    <text x="292" y="187" text-anchor="middle">spectrum</text>
    <text x="8" y="92">from the</text>
    <text x="8" y="101">telescope</text>
    <text x="6" y="12">Slit, collimator, grating, camera</text>
    <text x="6" y="240">angles drawn larger than in a real instrument</text>
  </g>
</svg>
</div>

*Figure A. The parts of a spectrograph.*

1. **The slit.** The telescope focuses its light on a narrow slit. Each colour will make an image of the slit, so a
   narrow slit gives sharp, narrow lines.
2. **The collimator.** A lens or mirror makes the light from the slit into a beam of parallel rays.
3. **The disperser.** A prism or a grating sends each wavelength off in a slightly different direction.
4. **The camera.** A second lens or mirror focuses each wavelength to a different place on the detector.

At first observers looked at the spectrum through an eyepiece. With photography came the **spectrograph**, which had a
camera in place of the viewing tube. The word was first used in 1876 by Henry Draper, who used his to photograph the
spectrum of Vega (chapter 14). Modern spectrographs use a grating, a detector and a computer to run it all.

??? note "Sources"
    - The early 19th-century spectroscope's slit and collimating lens, the spectrograph with a camera in place of the
      viewing tube, the word first used in 1876 by Henry Draper for photographs of Vega's spectrum, and modern
      spectrographs with a grating, slit and computer-controlled detector: Wikipedia,
      [Spectrograph](https://en.wikipedia.org/wiki/Spectrograph) (weaker).
    - Fraunhofer and the dark lines: this site's history book, chapter 18, section 18.3.

## 15.2 Prism or grating { #grating }

A prism spreads light because glass bends blue light more than red (chapter 3,
[section 3.2](03-Colours-Prisms-and-Rainbows.md#prism)). A **diffraction grating** does it by diffraction (chapter 12).
It is a surface ruled with thousands of fine, evenly spaced lines. The light from each gap spreads out, and the waves
add up strongly only in directions where the paths from neighbouring gaps differ by a whole number of wavelengths:

$$d\sin\theta = m\lambda,$$

where $d$ is the spacing of the lines and $m = 0, 1, 2, \dots$ is the **order**. Each wavelength comes out at its own
angle, and a grating spreads the colours far more widely than a prism. You can see the effect in the rainbow colours
on a CD or DVD, whose closely spaced tracks act as a grating.

**A short history.**

- **The 17th century.** About a year after Newton's experiments with prisms, James Gregory saw the patterns made by
  light passing through a bird's feather, in effect a natural grating.
- **Philadelphia, about 1785.** **David Rittenhouse** made the first human-made grating by stringing hairs between
  two finely threaded screws.
- **Germany, 1821.** Fraunhofer made a grating of fine wires.
- **Baltimore, 1882.** **Henry Rowland** of Johns Hopkins University described the gratings he made with a diamond
  point ruling lines on metal or glass, using "dividing engines" of extraordinary accuracy that he built himself. By
  the end of the century his concave gratings were the best available, and he used them to study the Sun's
  spectrum in detail.

Gratings are described by how many lines they have per millimetre, for example 600.

??? note "Sources"
    - The grating equation, the order, gratings spreading light much more widely than a prism, and 600 lines per mm:
      the physics lesson
      [The diffraction grating](https://physics.akadian.ca/topics/waves/level-8/04-the-diffraction-grating.html).
    - Colours from CDs and DVDs, Gregory and the feather about a year after Newton's prism experiments, Rittenhouse's
      hairs and screws about 1785, Fraunhofer's wire grating of 1821, Rowland's concave gratings as the best by the end
      of the 19th century, and groove density per millimetre: Wikipedia,
      [Diffraction grating](https://en.wikipedia.org/wiki/Diffraction_grating) (weaker).
    - Rowland at Johns Hopkins in Baltimore, his description of 1882, diamond-ruled metal or glass, his dividing
      engines, and his work on the solar spectrum: Wikipedia,
      [Henry Augustus Rowland](https://en.wikipedia.org/wiki/Henry_Augustus_Rowland) (weaker).

## 15.3 How finely? Resolving power { #resolution }

A spectrograph's **resolving power** is

$$R = \frac{\lambda}{\Delta\lambda},$$

where $\Delta\lambda$ is the smallest difference in wavelength it can separate. For a grating, $R$ can be at most the
order times the number of lines the light falls on, $mN$.

| Job | Resolving power needed |
| --- | --- |
| Split the two yellow sodium lines, 589.0 and 589.6 nm (chapter 7) | about 1,000 |
| Map the minerals on Mars from orbit (section 15.8) | about 150 |
| Measure a star's speed to 3 km/s from the Doppler shift (chapter 8) | about 100,000 |

A grating 50 mm wide with 600 lines per millimetre has 30,000 lines, so in first order it gives $R = 30{,}000$, and in
second order 60,000. To go higher, use a higher order, which brings us to the echelle.

??? note "Sources"
    - Resolving power $R = \lambda/\Delta\lambda$: Wikipedia,
      [Spectral resolution](https://en.wikipedia.org/wiki/Spectral_resolution) (weaker).
    - $R \le mN$ and the sodium pair needing about 980: the physics lesson
      [The diffraction grating](https://physics.akadian.ca/topics/waves/level-8/04-the-diffraction-grating.html).
    - The Mars and Doppler values: sections 15.8 and 15.9.

## 15.4 The echelle: a spectrum folded into stripes { #echelle }

An **echelle** grating (from the French for "ladder") has fairly coarse grooves, cut so that it works at a steep angle
in very high orders. High orders spread the colours very widely, but the orders overlap one another. The answer is a
second, weaker disperser turned at right angles, the **cross-disperser**, which pulls the orders apart into a stack of
stripes.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="What an echelle spectrograph puts on its detector. Instead of one long strip of spectrum, the detector holds many short stripes stacked one above another, each a little tilted. Each stripe is one diffraction order and covers a short piece of the spectrum, with wavelength increasing from left to right along it and from stripe to stripe, from blue at the bottom to red at the top. Dark absorption lines cross the stripes. A second, weaker disperser, the cross-disperser, spreads the orders apart so they do not overlap. The long spectrum fits on a square detector at high resolution.">
  <defs>
    <linearGradient id="l15g0" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#5aa0d8"/><stop offset="1" stop-color="#5aa0d8"/></linearGradient>
    <linearGradient id="l15g1" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#5aa0d8"/><stop offset="1" stop-color="#8fb0b8"/></linearGradient>
    <linearGradient id="l15g2" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#8fb0b8"/><stop offset="1" stop-color="#8fb0b8"/></linearGradient>
    <linearGradient id="l15g3" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#8fb0b8"/><stop offset="1" stop-color="#cfc8bf"/></linearGradient>
    <linearGradient id="l15g4" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#cfc8bf"/><stop offset="1" stop-color="#eea66f"/></linearGradient>
    <linearGradient id="l15g5" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#eea66f"/><stop offset="1" stop-color="#eea66f"/></linearGradient>
    <linearGradient id="l15g6" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#eea66f"/><stop offset="1" stop-color="#d9744a"/></linearGradient>
    <linearGradient id="l15g7" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#d9744a"/><stop offset="1" stop-color="#d9744a"/></linearGradient>
    <linearGradient id="l15g8" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#c1440e"/><stop offset="1" stop-color="#c1440e"/></linearGradient>
  </defs>
  <g font-size="8" fill="currentColor">
    <rect x="40" y="40" width="170" height="170" fill="#111" stroke="currentColor" stroke-width="1"/>
    <polygon points="50,199 200,193 200,185 50,191" fill="url(#l15g0)"/>
    <line x1="69.5" y1="198.2" x2="69.5" y2="190.2" stroke="#111" stroke-width="1.2"/>
    <line x1="149.0" y1="195.0" x2="149.0" y2="187.0" stroke="#111" stroke-width="1.2"/>
    <line x1="137.0" y1="195.5" x2="137.0" y2="187.5" stroke="#111" stroke-width="1.2"/>
    <line x1="156.5" y1="194.7" x2="156.5" y2="186.7" stroke="#111" stroke-width="1.2"/>
    <polygon points="50,182 200,176 200,168 50,174" fill="url(#l15g1)"/>
    <line x1="120.5" y1="179.2" x2="120.5" y2="171.2" stroke="#111" stroke-width="1.2"/>
    <line x1="83.0" y1="180.7" x2="83.0" y2="172.7" stroke="#111" stroke-width="1.2"/>
    <line x1="110.0" y1="179.6" x2="110.0" y2="171.6" stroke="#111" stroke-width="1.2"/>
    <polygon points="50,165 200,159 200,151 50,157" fill="url(#l15g2)"/>
    <line x1="96.5" y1="163.1" x2="96.5" y2="155.1" stroke="#111" stroke-width="1.2"/>
    <line x1="173.0" y1="160.1" x2="173.0" y2="152.1" stroke="#111" stroke-width="1.2"/>
    <line x1="185.0" y1="159.6" x2="185.0" y2="151.6" stroke="#111" stroke-width="1.2"/>
    <polygon points="50,148 200,142 200,134 50,140" fill="url(#l15g3)"/>
    <line x1="69.5" y1="147.2" x2="69.5" y2="139.2" stroke="#111" stroke-width="1.2"/>
    <line x1="149.0" y1="144.0" x2="149.0" y2="136.0" stroke="#111" stroke-width="1.2"/>
    <line x1="137.0" y1="144.5" x2="137.0" y2="136.5" stroke="#111" stroke-width="1.2"/>
    <line x1="156.5" y1="143.7" x2="156.5" y2="135.7" stroke="#111" stroke-width="1.2"/>
    <polygon points="50,131 200,125 200,117 50,123" fill="url(#l15g4)"/>
    <line x1="120.5" y1="128.2" x2="120.5" y2="120.2" stroke="#111" stroke-width="1.2"/>
    <line x1="83.0" y1="129.7" x2="83.0" y2="121.7" stroke="#111" stroke-width="1.2"/>
    <line x1="110.0" y1="128.6" x2="110.0" y2="120.6" stroke="#111" stroke-width="1.2"/>
    <polygon points="50,114 200,108 200,100 50,106" fill="url(#l15g5)"/>
    <line x1="96.5" y1="112.1" x2="96.5" y2="104.1" stroke="#111" stroke-width="1.2"/>
    <line x1="173.0" y1="109.1" x2="173.0" y2="101.1" stroke="#111" stroke-width="1.2"/>
    <line x1="185.0" y1="108.6" x2="185.0" y2="100.6" stroke="#111" stroke-width="1.2"/>
    <polygon points="50,97 200,91 200,83 50,89" fill="url(#l15g6)"/>
    <line x1="69.5" y1="96.2" x2="69.5" y2="88.2" stroke="#111" stroke-width="1.2"/>
    <line x1="149.0" y1="93.0" x2="149.0" y2="85.0" stroke="#111" stroke-width="1.2"/>
    <line x1="137.0" y1="93.5" x2="137.0" y2="85.5" stroke="#111" stroke-width="1.2"/>
    <line x1="156.5" y1="92.7" x2="156.5" y2="84.7" stroke="#111" stroke-width="1.2"/>
    <polygon points="50,80 200,74 200,66 50,72" fill="url(#l15g7)"/>
    <line x1="120.5" y1="77.2" x2="120.5" y2="69.2" stroke="#111" stroke-width="1.2"/>
    <line x1="83.0" y1="78.7" x2="83.0" y2="70.7" stroke="#111" stroke-width="1.2"/>
    <line x1="110.0" y1="77.6" x2="110.0" y2="69.6" stroke="#111" stroke-width="1.2"/>
    <polygon points="50,63 200,57 200,49 50,55" fill="url(#l15g8)"/>
    <line x1="96.5" y1="61.1" x2="96.5" y2="53.1" stroke="#111" stroke-width="1.2"/>
    <line x1="173.0" y1="58.1" x2="173.0" y2="50.1" stroke="#111" stroke-width="1.2"/>
    <line x1="185.0" y1="57.6" x2="185.0" y2="49.6" stroke="#111" stroke-width="1.2"/>
    <path d="M60,222 L190,222 M186,218 L190,222 L186,226" fill="none" stroke="currentColor" stroke-width="1"/>
    <text x="125" y="236" text-anchor="middle">along a stripe: a short piece of the spectrum</text>
    <path d="M24,200 L24,50 M20,54 L24,50 L28,54" fill="none" stroke="currentColor" stroke-width="1"/>
    <text x="18" y="130" text-anchor="middle" transform="rotate(-90 18 130)">order to order (cross-disperser)</text>
    <text x="218" y="62">red end</text>
    <text x="218" y="196">blue end</text>
    <text x="218" y="110">each stripe is</text>
    <text x="218" y="120">one order of</text>
    <text x="218" y="130">the grating; dark</text>
    <text x="218" y="140">ticks are lines</text>
    <text x="6" y="12">An echelle spectrum: one long spectrum folded into stripes</text>
  </g>
</svg>
</div>

*Figure B. An echelle spectrum on the detector.*

The coarse grating used at a grazing angle was found by Albert Michelson in 1898. The modern form, with the crossed
second disperser, was invented in 1923 by the Japanese scientists **Nagaoka** and **Mishima**, and has been
built in much the same layout ever since.

Echelles are the spectrographs that find planets by the wobble of their stars (chapter 8,
[section 8.6](08-The-Doppler-Shift.md#planets)): HARPS in Chile, PARAS in India, and **ESPRESSO**, which takes light
from Europe's Very Large Telescope in Chile. ESPRESSO saw first light on one of the four telescopes in December 2017
and with all four in February 2018. It is designed to measure changes in a star's speed of 10 cm/s. The Earth makes
the Sun wobble by 9 cm/s.

??? note "Sources"
    - Echelle from the French for ladder, low groove density, high angles and high orders, use in cross-dispersed
      spectrographs such as HARPS and PARAS, Michelson's "echelon" of 1898, and the crossed layout invented by
      Nagaoka and Mishima in 1923: Wikipedia, [Echelle grating](https://en.wikipedia.org/wiki/Echelle_grating) (weaker).
    - ESPRESSO, a fibre-fed cross-dispersed echelle on the VLT, first light in December 2017 and with all four units in
      February 2018, the 10 cm/s requirement, and the Earth's 9 cm/s on the Sun: Wikipedia,
      [ESPRESSO](https://en.wikipedia.org/wiki/ESPRESSO) (weaker).

## 15.5 Thousands of spectra at once { #multi }

A slit takes the spectrum of one star at a time. There are billions of stars.

- **A prism over the whole telescope.** Put a thin prism in front of the telescope, with no slit at all, and every star
  in the picture becomes a tiny spectrum. With this **objective prism**, Harvard College Observatory photographed the
  spectra for the **Henry Draper Catalogue** (1924), which sorted hundreds of thousands of stars. Williamina
  Fleming and then Annie Jump Cannon led the work (history book,
  [chapter 18, section 18.6](../history/18-Light-Split-into-Colours.md#stars)).
- **Fibres.** An optical fibre placed at the image of each star carries its light to the spectrograph. The fibres'
  other ends are lined up to make a long "slit".
    - **Australia.** The 2dF instrument on the 3.9 m Anglo-Australian Telescope had two banks of 200
      fibres, so it took 400 spectra at once. It measured good spectra of 221,414 galaxies.
    - **New Mexico, from 2000.** The Sloan Digital Sky Survey's 2.5 m telescope fed 640 fibres through holes drilled in
      an aluminium plate for each field. It has taken spectra of more than 4 million objects.
    - **China.** LAMOST, the Guo Shoujing Telescope, feeds 4,000 fibres (chapter 13).
    - **Arizona, 2021 to 2026.** DESI, on the Mayall Telescope at Kitt Peak, has 5,000 fibres, each moved into place
      by its own small robot. In its five-year survey it mapped more than 47 million galaxies and quasars in three
      dimensions.

??? note "Sources"
    - Slitless spectroscopy for surveys, and the Henry Draper Catalogue of 1924 from objective-prism spectra at
      Harvard, led by Fleming and then Cannon: Wikipedia,
      [Objective prism](https://en.wikipedia.org/wiki/Objective_prism) (weaker).
    - 2dF's two banks of 200 fibres, the 3.9 m Anglo-Australian Telescope, the 2° field and 221,414 good galaxy
      spectra: Wikipedia, [2dF Galaxy Redshift Survey](https://en.wikipedia.org/wiki/2dF_Galaxy_Redshift_Survey)
      (weaker).
    - SDSS's 2.5 m telescope at Apache Point, 640 spectra at once, fibres through holes drilled in aluminium plates,
      data from 2000, and more than 4 million spectra: Wikipedia,
      [Sloan Digital Sky Survey](https://en.wikipedia.org/wiki/Sloan_Digital_Sky_Survey) (weaker).
    - DESI's 5,000 robotic fibre positioners, the Mayall Telescope on Kitt Peak, the survey from 15 May 2021, and more
      than 47 million galaxies and quasars by 2026: Wikipedia,
      [Dark Energy Spectroscopic Instrument](https://en.wikipedia.org/wiki/Dark_Energy_Spectroscopic_Instrument)
      (weaker).

## 15.6 A spectrum for every point { #ifu }

An **integral field** spectrograph takes a spectrum of every point in a small patch of sky at once. Tiny lenses, a
bundle of fibres or a stack of narrow mirrors chop the image into pieces and line them up along the slit. The result
is a **data cube**: two directions of picture and one of wavelength. With it astronomers can map the speeds and star
formation across a galaxy, point by point. The **MUSE** instrument is built from 24 such spectrographs working side by
side.

The same idea, looking down at a planet, is called **imaging spectroscopy**: every pixel records many bands of the
spectrum instead of just red, green and blue (chapter 14). It is how orbiters map minerals (section 15.8).

??? note "Sources"
    - Integral field units made with lenslets, fibres or mirrors, the image reformatted into a long-slit-like output,
      the data cube with two spatial and one spectral dimension, and MUSE built from 24 integral field spectrographs:
      Wikipedia, [Integral field spectrograph](https://en.wikipedia.org/wiki/Integral_field_spectrograph) (weaker).
    - Maps of speeds and star formation within galaxies from bundled fibres (MaNGA): Wikipedia,
      [Sloan Digital Sky Survey](https://en.wikipedia.org/wiki/Sloan_Digital_Sky_Survey) (weaker).
    - Imaging spectroscopy, many bands per pixel instead of three: Wikipedia,
      [Imaging spectroscopy](https://en.wikipedia.org/wiki/Imaging_spectroscopy) (weaker).

## 15.7 The Sun in a single colour { #sun }

Put a second slit where the spectrum forms, so that only one wavelength gets through, and move both slits slowly
across the image of the Sun. Line by line you build a picture of the Sun in the light of that one wavelength. This is
the **spectroheliograph**. It was invented independently in the 1890s by **George Ellery Hale** in the United States
and **Henri Deslandres** in France, who later directed the Meudon and Paris observatories.

Kodaikanal in India has had spectroheliographs since 1904, and still photographs the whole Sun in the light of single
lines of calcium and hydrogen (history book,
[chapter 18, section 18.9](../history/18-Light-Split-into-Colours.md#world)).

??? note "Sources"
    - The spectroheliograph as a photograph of the Sun at a single wavelength, developed independently by Hale and
      Deslandres in the 1890s: Wikipedia, [Spectroheliograph](https://en.wikipedia.org/wiki/Spectroheliograph)
      (weaker).
    - Deslandres as director of the Meudon and Paris observatories: Wikipedia,
      [Henri-Alexandre Deslandres](https://en.wikipedia.org/wiki/Henri-Alexandre_Deslandres) (weaker).
    - Kodaikanal's spectroheliographs of 1904 and 1911, and full-disc pictures in single lines: Wikipedia,
      [Kodaikanal Solar Observatory](https://en.wikipedia.org/wiki/Kodaikanal_Solar_Observatory) (weaker).

## 15.8 Spectrometers at Mars { #mars }

**From Earth.** In 1964 Lewis Kaplan's team found faint lines of water vapour in Mars's air with a spectrograph on
Earth, separating them from the Earth's own water lines by the Doppler shift (chapter 7,
[section 7.7](07-Spectral-Lines.md#mars); history book,
[chapter 18, section 18.10](../history/18-Light-Split-into-Colours.md#mars)).

**From orbit.**

- **OMEGA**, a French imaging spectrometer on ESA's Mars Express, in orbit since 2003, found water ice in the south
  polar cap in January 2004 and, in 2005, hydrated sulphates and silicates: minerals that hold water.
- In March 2004 Mars Express also reported a trace of **methane** in the air, about 10 parts in a thousand million.
  Its instruments include an Italian infrared spectrometer, PFS, for the air.
- **CRISM**, built at the Johns Hopkins University Applied Physics Laboratory for NASA's Mars Reconnaissance
  Orbiter, measured light from 362 to 3,920 nm in steps of 6.55 nm: 544 wavelengths. Recording about 50 of them at 100
  to 200 m per pixel, it mapped half of Mars within a few months. It found clays and carbonates, minerals that form in
  water, and in many places a layer of aluminium-rich clay lying over iron- and magnesium-rich clay.

**On the ground.** ChemCam on Curiosity and SuperCam on Perseverance (chapter 7) carry spectrometers too. ChemCam's
splits the light from rock vaporised by its laser into three spectrographs.

??? note "Sources"
    - Kaplan's team and water vapour in 1964: this site's history book, chapter 18, section 18.10, and chapter 7.
    - Mars Express since 2003, OMEGA from France, PFS from Italy, water ice in the south polar cap (23 January 2004),
      methane at about 10 parts in a thousand million (30 March 2004), and hydrated sulphates and silicates (2005):
      Wikipedia, [Mars Express](https://en.wikipedia.org/wiki/Mars_Express) (weaker).
    - CRISM built by the Johns Hopkins APL, 362 to 3,920 nm in 6.55 nm steps, 544 wavelengths, about 50 recorded at
      100 to 200 m per pixel, half of Mars mapped in a few months, phyllosilicates and carbonates, and the layered
      clays: Wikipedia,
      [CRISM](https://en.wikipedia.org/wiki/Compact_Reconnaissance_Imaging_Spectrometer_for_Mars) (weaker).
    - ChemCam's three spectrographs: NASA,
      [Curiosity science instruments](https://science.nasa.gov/mission/msl-curiosity/science-instruments/).

## 15.9 Working it out { #working }

**Grating angles.** With 600 lines per mm, $d = 1/600$ mm $= 1.67\ \mu$m. Hydrogen's red line, 656 nm, leaves at
$\sin\theta = 0.656/1.67 = 0.394$, $\theta = 23.2°$ in first order, and at $\sin\theta = 0.787$, $\theta = 51.9°$ in
second order.

**Resolving power for a speed.** A Doppler shift of speed $v$ changes the wavelength by the fraction $v/c$. To see it
as a full line width needs $R = c/v$: for 3 km/s, $R = 300{,}000/3 = 100{,}000$.

**ESPRESSO's 10 cm/s.** The fraction is $0.1/(3\times10^8) = 3.3\times10^{-10}$. At 550 nm that is a shift of
$1.8\times10^{-16}$ m, smaller than an atomic nucleus. No spectrograph can split lines that finely; section 15.10
shows how it is measured anyway.

**CRISM's resolving power.** At 1,000 nm with steps of 6.55 nm, $R \approx 1{,}000/6.55 \approx 150$.

**Your own planet moves.** Every observer is carried round the Sun, so every star's lines shift back and forth over
the year. A spectrograph's results must be corrected for this before a star's own speed can be found.

| An observer carried round the Sun | Mars | Earth |
| --- | --- | --- |
| Mean orbital speed | 24.08 km/s | 29.78 km/s |
| Largest shift of a 500 nm line, towards or away | 0.040 nm | 0.050 nm |
| Swing over a year, for a star in the plane of the orbit | 0.080 nm | 0.099 nm |
| Compared with ESPRESSO's 10 cm/s | 240,000 times larger | 300,000 times larger |

??? note "Sources"
    - Mean orbital speeds: NASA, [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - The grating spacing and angle: the physics lesson
      [The diffraction grating](https://physics.akadian.ca/topics/waves/level-8/04-the-diffraction-grating.html).
    - The arithmetic is ours.

## 15.10 Where $R = mN$ comes from, and measuring the unmeasurable { #theory }

**Resolving power.** Take a grating of $N$ lines with spacing $d$, used in order $m$. In the direction $\theta$ of a
bright peak, light from neighbouring lines differs in path by $m\lambda$, and from the first line to the last by
$Nm\lambda$. Turn a little away from the peak until that end-to-end difference grows by one more wavelength, to
$Nm\lambda + \lambda$: then the light from the two halves of the grating cancels, and the brightness falls to zero. A
second wavelength $\lambda + \Delta\lambda$ has its peak just there when

$$Nm(\lambda + \Delta\lambda) = Nm\lambda + \lambda \quad\Rightarrow\quad \frac{\lambda}{\Delta\lambda} = mN.$$

That is Rayleigh's rule again (chapter 12): one peak on the first dark point of the other.

**Spread.** Differentiating $d\sin\theta = m\lambda$ gives the angular spread

$$\frac{d\theta}{d\lambda} = \frac{m}{d\cos\theta}.$$

It grows with the order $m$ and with steep angles, where $\cos\theta$ is small. That is exactly how an echelle is used.

**Measuring the unmeasurable.** A spectral line seen with $R = 100{,}000$ is about 3 km/s wide. But its *centre* can be
found far more precisely than its width, roughly the width divided by the signal-to-noise ratio (chapter 14). With a
signal-to-noise of 100, one line gives its speed to about 30 m/s. A star's spectrum holds thousands of lines, and
averaging $n$ lines improves this by $\sqrt{n}$ (chapter 14, section 14.10): 4,000 lines give about
$30/\sqrt{4{,}000} \approx 0.5$ m/s. Add many nights, an instrument held at a very steady temperature, and an exact
wavelength reference, and the shift can be followed down towards 10 cm/s.

??? note "Sources"
    - The grating equation and resolving power $mN$: the physics lesson
      [The diffraction grating](https://physics.akadian.ca/topics/waves/level-8/04-the-diffraction-grating.html).
    - The derivation, the angular dispersion, and the rough estimate of line-centre precision are ours, using standard
      wave optics and counting statistics.

## Check yourself { #check }

**1.** (beginner) Name the four parts of a spectrograph.

??? note "Answer"
    The slit, the collimator, the disperser (a prism or grating), and the camera, which focuses the spectrum on a
    detector.

**2.** (beginner) Why does a CD show rainbow colours?

??? note "Answer"
    Its closely spaced tracks act as a diffraction grating, sending each colour off at a different angle.

**3.** (beginner) What did David Rittenhouse make his grating from, and when?

??? note "Answer"
    Hairs strung between two finely threaded screws, around 1785, in Philadelphia.

**4.** (intermediate) What does the cross-disperser in an echelle spectrograph do?

??? note "Answer"
    It spreads the overlapping high orders apart at right angles, so the spectrum lies on the detector as a stack of
    stripes.

**5.** (intermediate) How did the Sloan Digital Sky Survey take 640 spectra at once?

??? note "Answer"
    An optical fibre was placed at the position of each object, through holes drilled in an aluminium plate, and the
    fibres carried the light to the spectrographs.

**6.** (intermediate) What did CRISM find on Mars, and why does it matter?

??? note "Answer"
    Clays and carbonates, minerals that form in water, often with aluminium-rich clays over iron- and magnesium-rich
    ones. They show that water acted on Mars's surface in the past.

**7.** (advanced) A grating has 1,200 lines per mm. At what angle does 500 nm light leave it in first order?

??? note "Answer"
    $d = 1/1{,}200$ mm $= 0.833\ \mu$m. $\sin\theta = 0.5/0.833 = 0.600$, so $\theta = 36.9°$.

**8.** (expert) What resolving power is needed to see a speed of 1 km/s as a full line width? With 30,000 lines, what
order would a grating need?

??? note "Answer"
    $R = c/v = 300{,}000$. Since $R = mN$, $m = 300{,}000/30{,}000 = 10$: a high order, as in an echelle.

## Summary

- A spectrograph has a slit, a collimator, a disperser and a camera; Henry Draper named it in 1876.
- A grating spreads light by diffraction, $d\sin\theta = m\lambda$, far more widely than a prism.
- Gratings went from Rittenhouse's hairs (about 1785) and Fraunhofer's wires (1821) to Rowland's ruled gratings (1882).
- Resolving power $R = \lambda/\Delta\lambda$ is at most $mN$; measuring star speeds needs about 100,000.
- Echelles use high orders and a cross-disperser; the layout came from Nagaoka and Mishima in Japan in 1923.
- Objective prisms, fibres and robots let one telescope take thousands of spectra at once; DESI mapped 47 million
  galaxies and quasars.
- Integral field spectrographs take a spectrum of every point in an image.
- Spectroheliographs, invented by Hale and Deslandres, photograph the Sun in one line.
- Spectrometers orbiting Mars found water ice, hydrated minerals, a trace of methane and layered clays.
- Line centres can be measured far more finely than line widths, which is how 10 cm/s is within reach.

**Next:** chapter 16, Giant telescopes and the observatories of the world, where we visit the largest telescopes and
the mountaintops that hold them.

## Further reading

- Keith Robinson, *Spectroscopy: The Key to the Stars: Reading the Lines in Stellar Spectra*, Springer, 2007.
