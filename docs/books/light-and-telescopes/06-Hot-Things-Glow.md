# 6. Hot things glow

*Heat a poker in a fire and it glows dull red, then orange, then yellow-white. Everything glows like this, even ice
and people, though most of the glow is infrared. This chapter shows how the colour and the strength of the glow
depend on temperature, how a puzzle about that glow led Max Planck and later Satyendra Nath Bose in Dhaka to the
quantum, and how thermal cameras and lamps use it on Earth. On Mars, orbiters read the planet's temperature from its
infrared glow. The chapter ends by working out the temperature of Mars and the Earth from sunlight alone.*

!!! abstract "In this chapter"
    **You will learn:**

    - that everything glows, and why we only see the glow of very hot things
    - how the colour of the glow changes from red-hot to white-hot
    - how much more light a hotter body gives out
    - what a black body is
    - how the puzzle of the glow started quantum physics
    - how lamps and thermal cameras use the glow
    - how spacecraft measure the temperature of Mars from its infrared glow
    - how to use Wien's law and the Stefan–Boltzmann law
    - how to work out a planet's temperature from the sunlight it gets

    **You need:** chapters 4 and 5. Book 1, [chapter 5](../night-sky/05-Star-Colours.md), shows how this explains the
    colours of the stars.

    **Levels:** 6.1 to 6.3 are beginner; 6.4 to 6.7 are intermediate; 6.8 is advanced; 6.9 is expert.

## 6.1 Everything glows { #glow }

Everything gives off light because of its temperature. The atoms in it are always jiggling, and jiggling charges give
out electromagnetic waves (chapter 1). The hotter the thing, the more light it gives out, and the shorter the
wavelengths.

At everyday temperatures the glow is all infrared, so we cannot see it. You glow too: at normal body temperature
people give out most of their light at around 10 µm (chapter 4). Only when something gets very hot does part of its
glow reach the visible band.

??? note "Sources"
    - Humans radiating chiefly at around 10 µm: Wikipedia, [Infrared](https://en.wikipedia.org/wiki/Infrared)
      (weaker).
    - The physics lesson
      [Why things have colour](https://physics.akadian.ca/topics/waves/level-6/03-why-things-have-colour.html).

## 6.2 From red-hot to white-hot { #colour }

Heat a piece of metal in the dark and watch. First comes a faint, "ghostly" grey glow; it is really very dim red light,
too faint for the colour-sensing cells of your eye. Then it glows **dull red**, then **yellow**, and at last a
dazzling **bluish white**.

In 1847 the American scientist John William Draper found that almost all solid materials begin to glow visibly above
about the same temperature, 525 °C (798 K), now called the **Draper point**. Below that, almost all the glow is
infrared.

People who work with fire have long used these colours as a thermometer. Around 1782 the English potter Josiah
Wedgwood made a device to measure the heat of his kilns, at first by comparing the colour of clay fired at known
temperatures. Later instruments called optical pyrometers judged the temperature of a hot object by matching its colour
to a glowing wire.

Stars follow the same rule: red stars are the coolest and blue-white stars the hottest (book 1, chapter 5).

??? note "Sources"
    - The ghostly grey, dull red, yellow and dazzling bluish-white glow: Wikipedia,
      [Black-body radiation](https://en.wikipedia.org/wiki/Black-body_radiation) (weaker).
    - The Draper point, 525 °C, 798 K, above which almost all solid materials glow visibly, set by John William Draper
      in 1847, and bodies below it radiating mainly in the infrared: Wikipedia,
      [Draper point](https://en.wikipedia.org/wiki/Draper_point) (weaker).
    - Wedgwood's pyrometer around 1782 and the matched-filament optical pyrometer: Wikipedia,
      [Pyrometer](https://en.wikipedia.org/wiki/Pyrometer) (weaker).

## 6.3 Hotter is much brighter { #brighter }

The glow does not just change colour; it gets very much stronger. The total light given out by each square metre of a
glowing body goes as the **fourth power** of its temperature in kelvin:

$$\text{power per square metre} = \sigma T^4,$$

where $\sigma = 5.67 \times 10^{-8}$ W per square metre per kelvin to the fourth. Double the temperature and the
glow is $2^4 = 16$ times as strong. This is the **Stefan–Boltzmann law**.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Glow curves for five temperatures, with wavelength from 0.1 to 100 micrometres along the bottom and the light given out per micrometre up the side, both on scales where each step is ten times more. The Sun's surface at 5,772 kelvin peaks in the visible band at about half a micrometre and is far above all the others. A lamp filament at 3,000 kelvin peaks near 1 micrometre, in the infrared. A body at 798 kelvin, where the first faint red glow appears, peaks near 3.6 micrometres, with only a tiny tail in the visible. The Earth at 288 kelvin peaks near 10 micrometres and Mars at 214 kelvin near 14 micrometres, with nothing visible at all. Hotter bodies peak at shorter wavelengths and give out far more light at every wavelength.">
  <defs><linearGradient id="l06vis" x1="0" x2="1" y1="0" y2="0">
    <stop offset="0" stop-color="#6b3fa0"/>
    <stop offset="0.25" stop-color="#2f6fc8"/>
    <stop offset="0.45" stop-color="#3a9a46"/>
    <stop offset="0.62" stop-color="#e6c619"/>
    <stop offset="0.8" stop-color="#e67e22"/>
    <stop offset="1" stop-color="#c0392b"/>
  </linearGradient><clipPath id="l06clip"><rect x="50" y="37" width="270" height="171"/></clipPath></defs>
  <rect x="102.2" y="37" width="26.1" height="171" fill="url(#l06vis)" fill-opacity="0.25"/>
  <g clip-path="url(#l06clip)">
    <polyline points="50.0,143.9 52.0,136.6 54.0,129.7 56.0,123.3 58.0,117.3 60.0,111.6 62.0,106.4 64.0,101.5 66.0,96.9 68.0,92.7 70.0,88.8 72.0,85.1 74.0,81.8 76.0,78.7 78.0,75.8 80.0,73.2 82.0,70.8 84.0,68.7 86.0,66.7 88.0,64.9 90.0,63.3 92.0,61.9 94.0,60.7 96.0,59.6 98.0,58.6 100.0,57.8 102.0,57.1 104.0,56.6 106.0,56.2 108.0,55.9 110.0,55.6 112.0,55.5 114.0,55.5 116.0,55.6 118.0,55.8 120.0,56.1 122.0,56.4 124.0,56.8 126.0,57.3 128.0,57.8 130.0,58.4 132.0,59.1 134.0,59.8 136.0,60.5 138.0,61.3 140.0,62.2 142.0,63.1 144.0,64.0 146.0,64.9 148.0,65.9 150.0,67.0 152.0,68.0 154.0,69.1 156.0,70.2 158.0,71.4 160.0,72.5 162.0,73.7 164.0,74.9 166.0,76.1 168.0,77.3 170.0,78.6 172.0,79.9 174.0,81.1 176.0,82.4 178.0,83.7 180.0,85.1 182.0,86.4 184.0,87.7 186.0,89.1 188.0,90.4 190.0,91.8 192.0,93.2 194.0,94.6 196.0,96.0 198.0,97.4 200.0,98.8 202.0,100.2 204.0,101.6 206.0,103.0 208.0,104.4 210.0,105.9 212.0,107.3 214.0,108.8 216.0,110.2 218.0,111.7 220.0,113.1 222.0,114.6 224.0,116.0 226.0,117.5 228.0,119.0 230.0,120.4 232.0,121.9 234.0,123.4 236.0,124.9 238.0,126.3 240.0,127.8 242.0,129.3 244.0,130.8 246.0,132.3 248.0,133.8 250.0,135.2 252.0,136.7 254.0,138.2 256.0,139.7 258.0,141.2 260.0,142.7 262.0,144.2 264.0,145.7 266.0,147.2 268.0,148.7 270.0,150.2 272.0,151.7 274.0,153.2 276.0,154.7 278.0,156.2 280.0,157.7 282.0,159.2 284.0,160.8 286.0,162.3 288.0,163.8 290.0,165.3 292.0,166.8 294.0,168.3 296.0,169.8 298.0,171.3 300.0,172.8 302.0,174.4 304.0,175.9 306.0,177.4 308.0,178.9 310.0,180.4 312.0,181.9 314.0,183.4 316.0,184.9 318.0,186.5 320.0,188.0" fill="none" stroke="#eea66f" stroke-width="1.4"/>
    <polyline points="66.0,210.5 68.0,200.6 70.0,191.3 72.0,182.6 74.0,174.3 76.0,166.6 78.0,159.4 80.0,152.6 82.0,146.3 84.0,140.3 86.0,134.8 88.0,129.6 90.0,124.8 92.0,120.3 94.0,116.1 96.0,112.3 98.0,108.7 100.0,105.4 102.0,102.4 104.0,99.6 106.0,97.0 108.0,94.7 110.0,92.5 112.0,90.6 114.0,88.9 116.0,87.3 118.0,85.9 120.0,84.7 122.0,83.6 124.0,82.7 126.0,82.0 128.0,81.3 130.0,80.8 132.0,80.4 134.0,80.1 136.0,79.9 138.0,79.8 140.0,79.9 142.0,80.0 144.0,80.2 146.0,80.4 148.0,80.8 150.0,81.2 152.0,81.7 154.0,82.2 156.0,82.8 158.0,83.5 160.0,84.2 162.0,85.0 164.0,85.8 166.0,86.7 168.0,87.6 170.0,88.5 172.0,89.5 174.0,90.5 176.0,91.5 178.0,92.6 180.0,93.6 182.0,94.8 184.0,95.9 186.0,97.1 188.0,98.2 190.0,99.4 192.0,100.7 194.0,101.9 196.0,103.2 198.0,104.4 200.0,105.7 202.0,107.0 204.0,108.3 206.0,109.6 208.0,111.0 210.0,112.3 212.0,113.7 214.0,115.0 216.0,116.4 218.0,117.8 220.0,119.2 222.0,120.6 224.0,122.0 226.0,123.4 228.0,124.8 230.0,126.2 232.0,127.6 234.0,129.0 236.0,130.5 238.0,131.9 240.0,133.4 242.0,134.8 244.0,136.3 246.0,137.7 248.0,139.2 250.0,140.6 252.0,142.1 254.0,143.6 256.0,145.0 258.0,146.5 260.0,148.0 262.0,149.5 264.0,150.9 266.0,152.4 268.0,153.9 270.0,155.4 272.0,156.9 274.0,158.4 276.0,159.9 278.0,161.4 280.0,162.8 282.0,164.3 284.0,165.8 286.0,167.3 288.0,168.8 290.0,170.3 292.0,171.8 294.0,173.3 296.0,174.8 298.0,176.3 300.0,177.8 302.0,179.3 304.0,180.9 306.0,182.4 308.0,183.9 310.0,185.4 312.0,186.9 314.0,188.4 316.0,189.9 318.0,191.4 320.0,192.9" fill="none" stroke="currentColor" stroke-width="1.4"/>
    <polyline points="128.0,214.9 130.0,207.7 132.0,201.0 134.0,194.7 136.0,188.8 138.0,183.3 140.0,178.2 142.0,173.4 144.0,169.0 146.0,164.8 148.0,161.0 150.0,157.5 152.0,154.2 154.0,151.2 156.0,148.4 158.0,145.9 160.0,143.6 162.0,141.5 164.0,139.6 166.0,137.8 168.0,136.3 170.0,134.9 172.0,133.7 174.0,132.7 176.0,131.8 178.0,131.0 180.0,130.4 182.0,129.9 184.0,129.5 186.0,129.2 188.0,129.1 190.0,129.0 192.0,129.0 194.0,129.2 196.0,129.4 198.0,129.6 200.0,130.0 202.0,130.4 204.0,130.9 206.0,131.5 208.0,132.1 210.0,132.8 212.0,133.5 214.0,134.3 216.0,135.1 218.0,135.9 220.0,136.8 222.0,137.8 224.0,138.7 226.0,139.7 228.0,140.8 230.0,141.9 232.0,142.9 234.0,144.1 236.0,145.2 238.0,146.4 240.0,147.6 242.0,148.8 244.0,150.0 246.0,151.2 248.0,152.5 250.0,153.7 252.0,155.0 254.0,156.3 256.0,157.6 258.0,159.0 260.0,160.3 262.0,161.6 264.0,163.0 266.0,164.4 268.0,165.7 270.0,167.1 272.0,168.5 274.0,169.9 276.0,171.3 278.0,172.7 280.0,174.1 282.0,175.5 284.0,177.0 286.0,178.4 288.0,179.8 290.0,181.3 292.0,182.7 294.0,184.2 296.0,185.6 298.0,187.1 300.0,188.5 302.0,190.0 304.0,191.4 306.0,192.9 308.0,194.4 310.0,195.9 312.0,197.3 314.0,198.8 316.0,200.3 318.0,201.8 320.0,203.3" fill="none" stroke="#555" stroke-width="1.4" stroke-dasharray="4 2"/>
    <polyline points="180.0,215.6 182.0,210.9 184.0,206.5 186.0,202.4 188.0,198.6 190.0,195.0 192.0,191.8 194.0,188.8 196.0,186.0 198.0,183.5 200.0,181.2 202.0,179.1 204.0,177.3 206.0,175.6 208.0,174.0 210.0,172.7 212.0,171.5 214.0,170.5 216.0,169.6 218.0,168.8 220.0,168.2 222.0,167.7 224.0,167.3 226.0,167.1 228.0,166.9 230.0,166.9 232.0,166.9 234.0,167.0 236.0,167.2 238.0,167.5 240.0,167.9 242.0,168.3 244.0,168.8 246.0,169.4 248.0,170.0 250.0,170.7 252.0,171.4 254.0,172.2 256.0,173.0 258.0,173.8 260.0,174.8 262.0,175.7 264.0,176.7 266.0,177.7 268.0,178.7 270.0,179.8 272.0,180.9 274.0,182.0 276.0,183.1 278.0,184.3 280.0,185.5 282.0,186.7 284.0,187.9 286.0,189.2 288.0,190.4 290.0,191.7 292.0,193.0 294.0,194.3 296.0,195.6 298.0,196.9 300.0,198.3 302.0,199.6 304.0,201.0 306.0,202.3 308.0,203.7 310.0,205.1 312.0,206.5 314.0,207.9 316.0,209.3 318.0,210.7 320.0,212.1" fill="none" stroke="#5aa0d8" stroke-width="1.4"/>
    <polyline points="196.0,216.7 198.0,212.6 200.0,208.9 202.0,205.4 204.0,202.2 206.0,199.3 208.0,196.6 210.0,194.1 212.0,191.8 214.0,189.8 216.0,187.9 218.0,186.3 220.0,184.8 222.0,183.5 224.0,182.3 226.0,181.3 228.0,180.4 230.0,179.7 232.0,179.1 234.0,178.7 236.0,178.3 238.0,178.1 240.0,177.9 242.0,177.9 244.0,177.9 246.0,178.1 248.0,178.3 250.0,178.6 252.0,179.0 254.0,179.4 256.0,179.9 258.0,180.5 260.0,181.1 262.0,181.8 264.0,182.6 266.0,183.3 268.0,184.2 270.0,185.0 272.0,186.0 274.0,186.9 276.0,187.9 278.0,188.9 280.0,190.0 282.0,191.0 284.0,192.1 286.0,193.3 288.0,194.4 290.0,195.6 292.0,196.8 294.0,198.0 296.0,199.2 298.0,200.4 300.0,201.7 302.0,203.0 304.0,204.3 306.0,205.6 308.0,206.9 310.0,208.2 312.0,209.5 314.0,210.9 316.0,212.2 318.0,213.6 320.0,215.0" fill="none" stroke="#c1440e" stroke-width="1.4"/>
  </g>
  <rect x="50" y="37" width="270" height="171" fill="none" stroke="currentColor" stroke-width="0.6"/>
  <g font-size="8" fill="currentColor">
    <text x="50.0" y="220" text-anchor="middle">0.1</text>
    <text x="140.0" y="220" text-anchor="middle">1</text>
    <text x="230.0" y="220" text-anchor="middle">10</text>
    <text x="320.0" y="220" text-anchor="middle">100</text>
    <text x="185" y="232" text-anchor="middle">wavelength in micrometres</text>
    <text x="46" y="193.9" text-anchor="end">1</text>
    <text x="46" y="125.5" text-anchor="end">10,000</text>
    <text x="46" y="57.1" text-anchor="end">100 million</text>
    <text x="6" y="12">How hot things glow</text>
    <text x="6" y="24">watts per square metre, per micrometre of wavelength</text>
    <text x="104.2" y="205">visible</text>
    <text x="150.3" y="45.9">the Sun's surface, 5,772 K</text>
    <text x="177.3" y="85.3">lamp filament, 3,000 K</text>
    <text x="145.5" y="163.5">first red glow, 798 K</text>
    <text x="190.1" y="160.5">Earth, 288 K</text>
    <text x="243.2" y="203.6">Mars, 214 K</text>
  </g>
</svg>
</div>

*Figure A. How hot things glow. Both scales go up in steps of ten. Hotter curves peak at shorter wavelengths and are
higher everywhere.*

Each square metre of the Sun's surface, at 5,772 K, gives out about 63 million watts. Each square metre of Mars, at
about 214 K, gives out about 120 W, all of it infrared.

??? note "Sources"
    - Radiant exitance proportional to the fourth power of temperature: Wikipedia,
      [Stefan–Boltzmann law](https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_law) (weaker).
    - The Sun's effective temperature of 5,772 K and surface emission of $62.94 \times 10^6$ W/m²: NASA,
      [Sun Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html). Mars's average temperature of
      about 214 K: NASA, [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html). The 120 W
      is worked out in section 6.8.
    - The curves in Figure A are drawn from Planck's law (section 6.5).

## 6.4 Black bodies { #blackbody }

How strongly a thing glows depends a little on its surface as well as its temperature. Physicists imagine an ideal
surface that absorbs all the light that falls on it, reflecting none. In 1860 Gustav Kirchhoff called such a thing a
**black body**. A good absorber is also a good emitter, so a black body glows in the most perfect way for its
temperature.

A good real black body is a small hole in a closed box: light that goes in bounces around inside and almost never
comes out again. The glow coming out of the hole depends only on the temperature inside.

Stars are not perfect black bodies, but they are close enough for a good first guess. The most perfect black-body glow
ever measured comes from the whole sky: the cosmic microwave background (chapter 4, section 4.6), at about 2.7 K.

??? note "Sources"
    - Kirchhoff introducing the term black body in 1860, emissivity equal to absorptivity, stars as approximate black
      bodies, and the cosmic microwave background as the most perfect black-body radiation observed: Wikipedia,
      [Black-body radiation](https://en.wikipedia.org/wiki/Black-body_radiation) (weaker).
    - The small hole in a cavity: Wikipedia, [Black body](https://en.wikipedia.org/wiki/Black_body) (weaker).

## 6.5 The puzzle that started quantum physics { #quantum }

- **Measuring the glow.** In 1864 John Tyndall measured the infrared given out by a glowing platinum wire.
  From his numbers, **Josef Stefan**, a Carinthian Slovene physicist in Vienna, worked out in the late 1870s that the
  glow goes as $T^4$. With it he made the first sensible estimate of the temperature of the Sun's surface, about
  5,430 °C. In 1884 Ludwig Boltzmann showed why it must be so.
- **The peak moves.** In 1893 Wilhelm Wien showed that the peak of the glow moves to shorter wavelengths in
  proportion as the temperature rises: **Wien's law** (section 6.8).
- **A disaster.** Around 1900, the physics of the day gave an answer for the shape of the curve that worked for long
  waves but went wildly wrong for short ones. It said a hot body should give out more and more light at shorter and
  shorter wavelengths, without limit: an infinite amount of energy. Paul Ehrenfest later called this the
  **ultraviolet catastrophe**.
- **Planck's packets, 1900.** Max Planck found a formula that fitted the measurements. To explain it he had
  to assume that energy is handed over only in small packets, $E = hf$. He thought of it as a mathematical trick.
  Five years later Einstein took the packets seriously as real particles of light (chapter 1, section 1.7).
- **Bose in Dhaka, 1924.** **Satyendra Nath Bose**, at the new University of Dhaka, found a new way to get Planck's
  formula: by treating light as a gas of photons and counting them in a new way, as particles that cannot be told
  apart. He sent his paper to Einstein, who translated it into German himself and had it published. Particles that
  follow Bose's way of counting are now called **bosons**, after him.

??? note "Sources"
    - Tyndall's measurements of a platinum filament in 1864, Stefan's fourth power from them, and Boltzmann's
      derivation of 1884: Wikipedia, [Stefan–Boltzmann law](https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_law)
      (weaker).
    - Stefan as a Carinthian Slovene physicist in Vienna, and his Sun at 5,430 °C, the first sensible value: Wikipedia,
      [Josef Stefan](https://en.wikipedia.org/wiki/Josef_Stefan) (weaker).
    - Wien in 1893: Wikipedia, [Wien's displacement law](https://en.wikipedia.org/wiki/Wien%27s_displacement_law)
      (weaker).
    - The Rayleigh–Jeans law predicting infinite energy, and Ehrenfest's name of 1911: Wikipedia,
      [Ultraviolet catastrophe](https://en.wikipedia.org/wiki/Ultraviolet_catastrophe) (weaker).
    - Planck's formula of 1900, his "purely formal assumption", and Einstein's light quanta of 1905: Wikipedia,
      [Planck's law](https://en.wikipedia.org/wiki/Planck%27s_law) (weaker).
    - Bose at the University of Dhaka, his 1924 derivation of Planck's law, Einstein's translation, and the name
      boson: Wikipedia, [Satyendra Nath Bose](https://en.wikipedia.org/wiki/Satyendra_Nath_Bose) (weaker).

## 6.6 Lamps and thermal cameras { #lamps }

- **Old light bulbs** heat a thin tungsten wire to between 2,000 and 3,300 K. At those temperatures most of the glow
  is still infrared: less than 5 per cent of the power becomes visible light, and the rest is heat.
- **"Warm" and "cool" light.** Light is often described by the temperature of the black body it looks like, its
  **colour temperature**. Daylight is like a black body at 5,500 to 6,500 K. Oddly, lamps called "warm" have low colour
  temperatures, 2,700 to 3,000 K, and look yellowish, while "cool" light, above 5,000 K, looks bluish.
- **Thermal cameras** see the infrared glow of everyday things, mostly at wavelengths of 7 to 14 µm. They make pictures
  in total darkness, and firefighters use them to see through smoke and find people.

??? note "Sources"
    - Filament temperatures of 2,000 to 3,300 K and less than 5 per cent of the power as visible light: Wikipedia,
      [Incandescent light bulb](https://en.wikipedia.org/wiki/Incandescent_light_bulb) (weaker).
    - Daylight like a black body at 5,500 to 6,500 K, and "warm" 2,700 to 3,000 K against "cool" above 5,000 K:
      Wikipedia, [Color temperature](https://en.wikipedia.org/wiki/Color_temperature) (weaker).
    - Thermal cameras at 7 to 14 µm and firefighting: Wikipedia,
      [Thermography](https://en.wikipedia.org/wiki/Thermography) (weaker).

## 6.7 Mars glows in the infrared { #mars }

Mars averages about 214 K, −59 °C. At the Viking 1 landing site the temperature swung each day from 184 K to 242 K.
At these temperatures Mars glows most strongly at about 14 µm, in the infrared, so its glow is a thermometer that
spacecraft can read from orbit.

- **The Mars Climate Sounder** on the Mars Reconnaissance Orbiter measures through one visible and near-infrared
  channel and eight far-infrared channels, from 12 to 50 µm. Its measurements build daily weather
  maps of Mars: temperature, pressure, humidity and dust. It has also found direct evidence of carbon dioxide snow.
- **THEMIS** on Mars Odyssey maps the warmth of the ground itself (chapter 4, section 4.7).
- **On the ground**, Curiosity carries a weather station, REMS, built by Spain and Finland, which measures
  temperature, humidity, pressure, wind and ultraviolet light.

??? note "Sources"
    - Mars's average of about 214 K (−59 °C) and the daily range of 184 to 242 K at the Viking 1 site: NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html). The 14 µm is from Wien's law,
      section 6.8.
    - The Mars Climate Sounder's channels, daily weather maps and carbon dioxide snow: Wikipedia,
      [Mars Reconnaissance Orbiter](https://en.wikipedia.org/wiki/Mars_Reconnaissance_Orbiter) (weaker).
    - REMS from Spain and Finland and what it measures: Wikipedia,
      [Rover Environmental Monitoring Station](https://en.wikipedia.org/wiki/Rover_Environmental_Monitoring_Station)
      (weaker).

## 6.8 Working it out { #working }

**Wien's law.** A black body at temperature $T$ glows most strongly at the wavelength

$$\lambda_\text{peak} = \frac{2898}{T} \ \mu\text{m}.$$

| Body | Temperature | Peak |
| --- | --- | --- |
| The Sun's surface | 5,772 K | 0.50 µm, in the visible |
| A lamp filament | 3,000 K | 0.97 µm, near infrared |
| The Draper point | 798 K | 3.6 µm |
| You | about 310 K | 9.3 µm |
| The Earth | 288 K | 10.1 µm |
| Mars | 214 K | 13.5 µm |
| The cosmic microwave background | 2.725 K | 1.06 mm |

**The Stefan–Boltzmann law.** $\sigma T^4$ with $\sigma = 5.670 \times 10^{-8}$:

- The Sun: $5.670 \times 10^{-8} \times 5772^4 = 6.29 \times 10^7$ W/m², matching NASA's $62.94 \times 10^6$.
- The Earth at 288 K: 390 W/m². Mars at 214 K: 119 W/m².

**How much is visible?** Adding up Planck's curve between 380 and 740 nm, the Sun's surface puts about 43 per cent of
its glow into visible light. A body at the Draper point puts in less than one ten-millionth.

| | Mars | Earth |
| --- | --- | --- |
| Average surface temperature | about 214 K | 288 K |
| Peak of the glow | 13.5 µm | 10.1 µm |
| Glow from each square metre | 119 W | 390 W |
| Bond albedo (share of sunlight reflected) | 0.250 | 0.294 |
| Black-body temperature from sunlight alone | 209.8 K | 254.0 K |
| Warming by the air (greenhouse effect) | about 6 K | about 33 K |

??? note "Sources"
    - $b \approx 2898$ µm K: Wikipedia,
      [Wien's displacement law](https://en.wikipedia.org/wiki/Wien%27s_displacement_law) (weaker).
    - Temperatures, Bond albedos and black-body temperatures: NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html),
      [Earth Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html) and
      [Sun Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html). The CMB's 2.725 K: chapter 4.
    - The greenhouse effect of 33 °C on the Earth and about 6 K on Mars: Wikipedia,
      [Greenhouse effect](https://en.wikipedia.org/wiki/Greenhouse_effect) (weaker).
    - The visible shares and the other arithmetic are ours.

## 6.9 A planet's temperature from sunlight { #balance }

A planet warms up until it gives out as much energy as it takes in (Figure B).

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Sunlight arriving at Mars from the left as parallel rays, 586 watts on each square metre facing the Sun. The rays fall on the planet's disc, an area of pi R squared. A quarter of the sunlight is reflected away. The rest warms the planet, which glows in infrared from its whole surface, an area of 4 pi R squared, four times the disc. When what comes in equals what goes out, the planet settles at about 210 kelvin.">
  <line x1="20" y1="89" x2="173.0" y2="89" stroke="#eea66f" stroke-width="1.4"/>
  <path d="M167.0,86 l6,3 l-6,3" fill="none" stroke="#eea66f" stroke-width="1.2"/>
  <line x1="20" y1="107" x2="158.8" y2="107" stroke="#eea66f" stroke-width="1.4"/>
  <path d="M152.8,104 l6,3 l-6,3" fill="none" stroke="#eea66f" stroke-width="1.2"/>
  <line x1="20" y1="125" x2="155.0" y2="125" stroke="#eea66f" stroke-width="1.4"/>
  <path d="M149.0,122 l6,3 l-6,3" fill="none" stroke="#eea66f" stroke-width="1.2"/>
  <line x1="20" y1="143" x2="158.8" y2="143" stroke="#eea66f" stroke-width="1.4"/>
  <path d="M152.8,140 l6,3 l-6,3" fill="none" stroke="#eea66f" stroke-width="1.2"/>
  <line x1="20" y1="161" x2="173.0" y2="161" stroke="#eea66f" stroke-width="1.4"/>
  <path d="M167.0,158 l6,3 l-6,3" fill="none" stroke="#eea66f" stroke-width="1.2"/>
  <circle cx="200" cy="125" r="45" fill="#c1440e" fill-opacity="0.85"/>
  <ellipse cx="200" cy="125" rx="8" ry="45" fill="none" stroke="currentColor" stroke-width="0.7" stroke-dasharray="3 2"/>
  <path d="M251.0,125.0 Q261.0,122.0 265.0,125.0" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
  <path d="M244.2,150.5 Q253.2,151.0 256.3,157.5" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
  <path d="M225.5,169.2 Q232.0,172.2 232.5,181.3" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
  <path d="M200.0,176.0 Q203.0,180.0 200.0,190.0" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
  <path d="M174.5,169.2 Q174.0,172.2 167.5,181.3" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
  <path d="M155.8,150.5 Q152.8,151.0 143.7,157.5" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
  <path d="M155.8,99.5 Q152.8,93.0 143.7,92.5" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
  <path d="M174.5,80.8 Q174.0,71.8 167.5,68.7" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
  <path d="M200.0,74.0 Q203.0,64.0 200.0,60.0" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
  <path d="M225.5,80.8 Q232.0,71.8 232.5,68.7" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
  <path d="M244.2,99.5 Q253.2,93.0 256.3,92.5" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
  <path d="M150,96 L112,58" stroke="#eea66f" stroke-width="1" stroke-dasharray="3 2"/>
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">Sunlight in, infrared out</text>
    <text x="20" y="74">sunlight, 586 W on each</text>
    <text x="20" y="84">square metre facing the Sun</text>
    <text x="64" y="52">a quarter reflected</text>
    <text x="140" y="200">caught by the disc, area πR²</text>
    <text x="265" y="74">infrared glow from</text>
    <text x="265" y="84">the whole surface,</text>
    <text x="265" y="94">area 4πR²</text>
    <text x="6" y="232">In balance when glow out = sunlight kept: Mars settles at about 210 K.</text>
  </g>
</svg>
</div>

*Figure B. Sunlight falls on the disc of the planet; the planet glows from its whole surface.*

- **In.** Sunlight of $S$ watts per square metre falls on the planet's disc, of area $\pi R^2$. A fraction $A$, the
  albedo, is reflected. The planet keeps $S(1 - A)\pi R^2$.
- **Out.** The planet glows from its whole surface, $4\pi R^2$, at $\sigma T^4$ per square metre.

Setting in equal to out, the $\pi R^2$ cancels:

$$S(1 - A)\pi R^2 = 4\pi R^2 \sigma T^4 \quad\Rightarrow\quad T = \left(\frac{S(1 - A)}{4\sigma}\right)^{1/4}.$$

- **Mars:** $S = 586.2$, $A = 0.250$: $T = (586.2 \times 0.750 / 2.268 \times 10^{-7})^{1/4} = 209.8$ K, exactly NASA's
  black-body temperature.
- **The Earth:** $S = 1361$, $A = 0.294$: $T = 255$ K, close to NASA's 254.0 K.

The Earth's real average, 288 K, is 33 K warmer than this, because its air traps part of the outgoing infrared: the
greenhouse effect. Mars's real average, about 214 K, is only a few kelvin above, even though its air has about 70
times as much carbon dioxide as the Earth's. Its air is also about 60 times thinner (chapter 3, section 3.10).

**The size of the Sun.** The same law gives the Sun's radius from its luminosity (chapter 5, section 5.9) and its
temperature: $L = 4\pi R^2 \sigma T^4$, so

$$R = \sqrt{\frac{L}{4\pi\sigma T^4}}
= \sqrt{\frac{3.828 \times 10^{26}}{4\pi \times 5.670 \times 10^{-8} \times 5772^4}}
= 6.957 \times 10^8 \text{ m},$$

695,700 km, just what NASA gives. Astronomers use the same sum to find the sizes of stars too far away to measure.

??? note "Sources"
    - Solar irradiance, Bond albedo and black-body temperature: NASA fact sheets, section 6.8. The Sun's luminosity of
      $382.8 \times 10^{24}$ W, temperature of 5,772 K and radius of 695,700 km: NASA,
      [Sun Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html).
    - Mars's 70 times as much carbon dioxide and small greenhouse effect: Wikipedia,
      [Greenhouse effect](https://en.wikipedia.org/wiki/Greenhouse_effect) (weaker).
    - The energy balance and the arithmetic are ours.

## Check yourself { #check }

**1.** (beginner) Why can't we see the glow of a person in the dark?

??? note "Answer"
    At body temperature the glow is almost all infrared, at around 10 µm, which our eyes cannot see.

**2.** (beginner) In what order do the colours appear as a piece of metal gets hotter?

??? note "Answer"
    A faint grey glow, then dull red, then yellow, then bluish white.

**3.** (beginner) If a body's temperature doubles, how much stronger is its glow?

??? note "Answer"
    $2^4 = 16$ times.

**4.** (intermediate) What is a black body, and what is the best black body we know?

??? note "Answer"
    An ideal body that absorbs all the light that falls on it, and so glows in the ideal way for its temperature. The
    cosmic microwave background is the most perfect black-body glow ever measured.

**5.** (intermediate) What did Satyendra Nath Bose do in 1924?

??? note "Answer"
    He found a new way to get Planck's law, by counting photons as particles that cannot be told apart. Einstein
    translated his paper and had it published, and such particles are now called bosons.

**6.** (intermediate) Why do spacecraft measure the temperature of Mars with infrared rather than visible light?

??? note "Answer"
    At about 214 K Mars glows most strongly at about 14 µm, in the infrared; it gives out no visible light of its own.

**7.** (advanced) The star Betelgeuse has a surface temperature of about 3,800 K (book 1, chapter 5). At what
wavelength does it glow most strongly?

??? note "Answer"
    $2898 / 3800 = 0.76$ µm, just beyond the red end of the visible band. We see it as reddish.

**8.** (expert) Suppose Mars were covered in bright ice with an albedo of 0.6. What would its black-body temperature
be?

??? note "Answer"
    $T = (586.2 \times 0.4 / 2.268 \times 10^{-7})^{1/4} = (1.034 \times 10^9)^{1/4} = 179$ K, about 30 K colder.

## Summary

- Everything glows because of its temperature; at everyday temperatures the glow is infrared.
- Heated things glow dull red from about 798 K, the Draper point, then yellow, then bluish white.
- The glow from each square metre is $\sigma T^4$ (Stefan and Boltzmann), and its peak is at $2898/T$ µm (Wien).
- A black body absorbs all light and glows in the ideal way; the cosmic microwave background is the best one known.
- Explaining the glow led Planck to the quantum in 1900, and Bose in Dhaka to a new way of counting photons in 1924.
- Lamps, colour temperature and thermal cameras all use the glow.
- Mars, at about 214 K, glows most at about 14 µm, and orbiters map its weather from that glow.
- Balancing sunlight in and glow out gives Mars 209.8 K and the Earth 255 K; the Earth's air adds 33 K.

**Next:** [chapter 7, Spectral lines, the fingerprints of the elements](07-Spectral-Lines.md), where we see how dark
and bright lines in a spectrum tell what stars are made of.

## Further reading

- Manjit Kumar, *Quantum: Einstein, Bohr and the Great Debate About the Nature of Reality*, Icon Books, 2008.
