# 10. Lenses and refraction

*A pencil standing in a glass of water looks broken at the surface. The reason is that light slows down in water
and glass, and bends when it crosses from one to the other. This bending, called refraction, is what lets a lens
focus light. This chapter gives the law of refraction, first written down by Ibn Sahl in Baghdad more than a
thousand years ago, and follows lenses from a piece of rock crystal in an Assyrian palace to Viking lenses on Gotland,
spectacles in Italy and the Dutch telescope. It explains why a single lens gives coloured fringes, how two kinds of
glass cure them, why the biggest lens telescope is only about a metre across, and how little Mars's thin air bends
starlight. It ends with the lens-maker's formula.*

!!! abstract "In this chapter"
    **You will learn:**

    - why light bends when it enters water or glass
    - the law of refraction and who found it
    - how light can be trapped inside glass, and how that carries light along fibres
    - what converging and diverging lenses do
    - the history of lenses, from burning glasses to spectacles
    - why a single lens makes coloured fringes, and how this was cured
    - why lens telescopes stopped growing at about a metre
    - how the air bends starlight, on Earth and on Mars
    - how to use the law of refraction
    - how the shape and glass of a lens set its focal length and its colour error

    **You need:** chapters 2 and 3. The physics lessons
    [Refraction](https://physics.akadian.ca/topics/waves/level-5/05-refraction.html),
    [Refraction and Snell's law](https://physics.akadian.ca/topics/waves/level-7/01-refraction-and-snells-law.html)
    and [Converging lenses](https://physics.akadian.ca/topics/waves/level-7/02-converging-lenses.html) help.

    **Levels:** 10.1 to 10.4 are beginner; 10.5 to 10.9 are intermediate; 10.10 is advanced; 10.11 is expert.

## 10.1 Light that bends { #bend }

Put a pencil at a slant in a glass of water and it seems to bend sharply where it enters the water. A swimming pool
looks shallower than it really is. Both happen because light changes direction as it passes from water into air.

The cause is speed. Light travels more slowly in water and glass than in air (chapter 2). When a beam meets the
surface at a slant, one side of it slows down before the other, so the whole beam swings round, like a line of
marchers turning when one end steps onto mud.

How much a material slows light is given by its **refractive index**, $n$: the speed of light in a vacuum divided by
its speed in the material.

| Material | Refractive index | Speed of light in it |
| --- | --- | --- |
| Air (0 °C, normal pressure) | 1.000293 | almost 300,000 km/s |
| Water | 1.333 | 224,900 km/s |
| Ordinary glass | about 1.5 | about 200,000 km/s |
| Diamond | 2.417 | 124,000 km/s |

??? note "Sources"
    - The pencil appearing to bend and the water appearing shallower, and the wavefront slowed on one side first:
      Wikipedia, [Refraction](https://en.wikipedia.org/wiki/Refraction) (weaker).
    - Refractive indices of air, water and diamond: Wikipedia,
      [Refractive index](https://en.wikipedia.org/wiki/Refractive_index) (weaker). Glass about 1.50: Wikipedia,
      [Total internal reflection](https://en.wikipedia.org/wiki/Total_internal_reflection) (weaker).
    - The speeds are ours: $299{,}792 / n$.

## 10.2 The law of refraction { #law }

Light going from a fast material into a slow one, such as from air into glass, bends **towards** the normal (the line
at right angles to the surface). Going the other way, from glass into air, it bends **away** from the normal.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Two pictures of light crossing the boundary between air and glass, whose refractive index is 1.5. Left: a ray in the air hits the glass at 50 degrees to the normal, the dashed line at right angles to the surface. Inside the glass it bends towards the normal and travels at 31 degrees; a faint ray is also reflected. Right: rays inside the glass heading up to the surface. One meeting it at 30 degrees passes out into the air and bends away from the normal, to 49 degrees. Another meeting it at 50 degrees, more than the critical angle of 41.8 degrees, cannot get out at all and is reflected back into the glass: total internal reflection.">
  <g font-size="8" fill="currentColor">
    <rect x="10" y="125" width="150" height="100" fill="#cfc8bf" fill-opacity="0.35"/>
    <rect x="180" y="125" width="150" height="100" fill="#cfc8bf" fill-opacity="0.35"/>
    <line x1="10" y1="125" x2="160" y2="125" stroke="currentColor" stroke-width="1"/>
    <line x1="180" y1="125" x2="330" y2="125" stroke="currentColor" stroke-width="1"/>
    <line x1="85" y1="40" x2="85" y2="210" stroke="#555" stroke-width="0.6" stroke-dasharray="3 2"/>
    <line x1="12.2" y1="63.9" x2="85" y2="125" stroke="#eea66f" stroke-width="1.6"/>
    <line x1="85" y1="125" x2="133.5" y2="206.7" stroke="#eea66f" stroke-width="1.6"/>
    <line x1="85" y1="125" x2="138.6" y2="80.0" stroke="#eea66f" stroke-width="0.6" stroke-dasharray="2 2"/>
    <text x="65" y="91" text-anchor="middle">50°</text>
    <text x="98" y="165" text-anchor="middle">31°</text>
    <text x="16" y="119">air</text>
    <text x="16" y="139">glass</text>
    <text x="85" y="237" text-anchor="middle">into glass: bends towards the normal</text>
    <line x1="255" y1="40" x2="255" y2="210" stroke="#555" stroke-width="0.6" stroke-dasharray="3 2"/>
    <line x1="207.5" y1="207.3" x2="255" y2="125" stroke="#5aa0d8" stroke-width="1.6"/>
    <line x1="255" y1="125" x2="326.2" y2="62.2" stroke="#5aa0d8" stroke-width="1.6"/>
    <line x1="178.4" y1="189.3" x2="255" y2="125" stroke="#c1440e" stroke-width="1.6"/>
    <line x1="255" y1="125" x2="331.6" y2="189.3" stroke="#c1440e" stroke-width="1.6"/>
    <text x="281" y="85">49°</text>
    <text x="225" y="217" text-anchor="middle">30°</text>
    <text x="193" y="189" text-anchor="middle">50°</text>
    <text x="186" y="119">air</text>
    <text x="186" y="139">glass</text>
    <text x="255" y="237" text-anchor="middle">beyond 41.8°: no way out, all reflected</text>
    <text x="6" y="12">Light bending at a boundary (glass n = 1.5)</text>
  </g>
</svg>
</div>

*Figure A. Left: light entering glass at 50° to the normal bends to 31°. Right: light leaving glass bends away from
the normal, and beyond 41.8° it cannot leave at all.*

The exact rule is

$$n_1 \sin \theta_1 = n_2 \sin \theta_2,$$

where $\theta_1$ and $\theta_2$ are the angles to the normal on the two sides, and $n_1$ and $n_2$ the refractive
indices.

- **Ptolemy**, in Alexandria, measured how much light bends, but his rule was wrong except for small angles.
- **Ibn Sahl**, a Persian scientist at the court in Baghdad, wrote the correct law in 984, in a book on burning
  mirrors and lenses. He used it to work out the shapes of lenses that bring light to a sharp focus.
- **Thomas Harriot** found it again in 1602, and the Dutch astronomer **Willebrord Snellius** in 1621, but neither
  published it. **René Descartes** published it in 1637. In English it is usually called
  **Snell's law**.

??? note "Sources"
    - Ptolemy in Alexandria, Ibn Sahl at the Baghdad court in 984 and his manuscript *On Burning Mirrors and Lenses*,
      Harriot in 1602, Snellius in 1621, Descartes's *La Dioptrique* of 1637: Wikipedia,
      [Snell's law](https://en.wikipedia.org/wiki/Snell%27s_law) (weaker).
    - The angles in the figure are ours, from the law with $n = 1.5$.

## 10.3 Light trapped in glass { #trapped }

When light inside glass meets the surface at a steep slant, the law of refraction asks for an angle outside of more
than 90°, which is impossible. The light cannot get out, and all of it is reflected back inside. This is **total
internal reflection**. It happens beyond the **critical angle**: about 41.8° for ordinary glass and 48.6° for water.

- **Diamonds** sparkle partly because their refractive index is so high that the critical angle is only about 24°,
  so light that gets in bounces around inside before it escapes.
- **Optical fibres** are thin threads of very clear glass. Light sent in at one end is trapped by total internal
  reflection and carried along, even round bends. Daniel Colladon and Jacques Babinet showed light being guided this
  way in Paris in the early 1840s. The name "fibre optics" was coined by the Indian-American physicist **Narinder
  Singh Kapany**. In 1965 **Charles Kao** and George Hockham argued that glass could be made clear enough to carry
  signals over long distances, and Kao received the Nobel Prize in Physics in 2009. Fibres now carry telephone and
  internet signals as pulses of light.
- China's LAMOST telescope uses 4,000 fibres to carry starlight from its focus to its spectrographs (chapter 8).

??? note "Sources"
    - Total internal reflection, the critical angles of 41.8° for glass and 48.6° for water, and its use in optical
      fibres for telecommunications: Wikipedia,
      [Total internal reflection](https://en.wikipedia.org/wiki/Total_internal_reflection) (weaker).
    - Colladon and Babinet, Kapany, Kao and Hockham in 1965, and Kao's Nobel Prize of 2009: Wikipedia,
      [Optical fiber](https://en.wikipedia.org/wiki/Optical_fiber) (weaker).
    - Diamond's critical angle is ours: $\sin^{-1}(1/2.417) = 24.4°$.

## 10.4 Lenses { #lenses }

A **lens** is a piece of glass with curved faces. Its name comes from the Latin word for a lentil, because a lens that
bulges on both sides is shaped like one.

- A **converging** lens is thicker in the middle. Parallel rays passing through it are bent towards each other and
  meet at its **focus**. The distance from the lens to the focus is its **focal length**. A magnifying glass is a
  converging lens.
- A **diverging** lens is thinner in the middle. It spreads parallel rays apart, as if they came from a point in front
  of the lens.

A converging lens can make an image of a distant object at its focus, just as a concave mirror does (chapter 9). That
is how the first telescopes worked (chapter 11).

??? note "Sources"
    - The word lens from the Latin for lentil: Wikipedia, [Lens](https://en.wikipedia.org/wiki/Lens) (weaker).

## 10.5 Lenses through history { #history }

- **Rock crystal in Assyria.** In 1850 Austen Henry Layard dug up a polished, slightly oval piece of rock crystal in
  the Assyrian palace at Nimrud, in modern Iraq, from about the 8th or 7th century BCE. It may have been a magnifying
  glass, a burning glass, or just a decoration.
- **Burning glasses.** The oldest certain mention of a lens used to start a fire is in Aristophanes's play *The
  Clouds*, of 424 BCE. In Rome, Seneca noted that letters look larger through a glass globe filled with water.
- **Reading stones and Viking lenses.** Between the 11th and 13th centuries people used "reading stones" to magnify
  writing. The **Visby lenses**, of rock crystal, were found in Viking graves on the island of Gotland in Sweden and
  date from the 11th or 12th century. The best of them have carefully shaped surfaces and give very good images.
- **Spectacles.** The first spectacles were made in central Italy, probably in Pisa or Florence, by about 1290; a
  friar spoke of them in a sermon in 1306. There are claims of magnifying glasses in China under the Northern Song
  (960–1127), but the evidence is disputed. Lenses for short sight appeared in the mid-15th century, and in 1604
  Johannes Kepler gave the first correct explanation of how spectacles work.
- **The telescope.** In 1608 Hans Lippershey, a spectacle maker of Middelburg in the Netherlands, tried to patent a
  telescope made of two lenses (history book,
  [chapter 15, section 15.1](../history/15-Galileo-and-the-Telescope.md#invention)).

??? note "Sources"
    - The Nimrud lens, Layard in 1850, the 8th-century BCE date and the three possible uses: Wikipedia,
      [Nimrud lens](https://en.wikipedia.org/wiki/Nimrud_lens) (weaker); the 7th-century BCE date: Wikipedia,
      [Lens](https://en.wikipedia.org/wiki/Lens) (weaker), which also gives Aristophanes in 424 BCE, Seneca's water
      globe and reading stones.
    - The Visby lenses, Gotland, the 11th or 12th century, and their imaging: Wikipedia,
      [Visby lenses](https://en.wikipedia.org/wiki/Visby_lenses) (weaker).
    - Spectacles in Pisa or Florence by about 1290, the sermon of 1306, the disputed Song claims, concave lenses in the
      mid-15th century and Kepler in 1604: Wikipedia, [Glasses](https://en.wikipedia.org/wiki/Glasses) (weaker).
    - Lippershey in 1608: Wikipedia, [Refracting telescope](https://en.wikipedia.org/wiki/Refracting_telescope)
      (weaker).

## 10.6 Colour fringes { #colour }

Glass bends blue light a little more than red light. That is how a prism spreads white light into a rainbow
(chapter 3). In a lens it is a nuisance: blue light comes to a focus a little closer to the lens than red light, so
a star seen through a simple lens is surrounded by coloured fringes. This is **chromatic aberration**.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Two lenses with parallel white light coming in from the left. Top: a single glass lens. Glass bends blue light more than red, so the blue rays meet at a focus closer to the lens and the red rays at a focus further away; between them the image of a star is blurred with coloured fringes. This is chromatic aberration. Bottom: an achromatic doublet, a converging lens of crown glass cemented to a weaker diverging lens of flint glass. The flint glass undoes the spreading of the colours while keeping part of the bending, so red and blue rays meet at the same focus.">
  <g font-size="8" fill="currentColor">
    <path d="M90,32 Q112,70 90,108 Q68,70 90,32 Z" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
    <line x1="10" y1="70" x2="330" y2="70" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <line x1="10" y1="42" x2="90" y2="42" stroke="currentColor" stroke-width="1"/>
    <line x1="90" y1="42" x2="239.5" y2="78.4" stroke="#5aa0d8" stroke-width="1.2"/>
    <line x1="90" y1="42" x2="304.5" y2="78.4" stroke="#c1440e" stroke-width="1.2"/>
    <line x1="10" y1="98" x2="90" y2="98" stroke="currentColor" stroke-width="1"/>
    <line x1="90" y1="98" x2="239.5" y2="61.6" stroke="#5aa0d8" stroke-width="1.2"/>
    <line x1="90" y1="98" x2="304.5" y2="61.6" stroke="#c1440e" stroke-width="1.2"/>
    <circle cx="205" cy="70" r="2" fill="#5aa0d8"/>
    <circle cx="255" cy="70" r="2" fill="#c1440e"/>
    <text x="205" y="100" text-anchor="middle">blue focus</text>
    <text x="258" y="100" text-anchor="middle">red focus</text>
    <text x="10" y="26">one glass lens: colours focus apart</text>
    <path d="M88,147 Q110,185 88,223 Q66,185 88,147 Z" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
    <path d="M99,147 Q93,185 99,223 L107,223 Q113,185 107,147 Z" fill="#eea66f" fill-opacity="0.25" stroke="currentColor" stroke-width="1"/>
    <line x1="10" y1="185" x2="330" y2="185" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <line x1="10" y1="157" x2="103" y2="157" stroke="currentColor" stroke-width="1"/>
    <line x1="103" y1="157" x2="287.6" y2="193.4" stroke="#c1440e" stroke-width="1.6"/>
    <line x1="103" y1="157" x2="287.6" y2="193.4" stroke="#5aa0d8" stroke-width="1.2" stroke-dasharray="4 3"/>
    <line x1="10" y1="213" x2="103" y2="213" stroke="currentColor" stroke-width="1"/>
    <line x1="103" y1="213" x2="287.6" y2="176.6" stroke="#c1440e" stroke-width="1.6"/>
    <line x1="103" y1="213" x2="287.6" y2="176.6" stroke="#5aa0d8" stroke-width="1.2" stroke-dasharray="4 3"/>
    <circle cx="245" cy="185" r="2" fill="currentColor"/>
    <text x="245" y="215" text-anchor="middle">one focus</text>
    <text x="10" y="139">crown glass + flint glass: colours focus together</text>
    <text x="88" y="237" text-anchor="middle">crown</text>
    <text x="120" y="237" text-anchor="middle">flint</text>
    <text x="6" y="12">Chromatic aberration and its cure</text>
  </g>
</svg>
</div>

*Figure B. Top: a single lens focuses blue and red light at different places. Bottom: an achromatic doublet brings
them together.*

- **Very long telescopes.** The fringes matter less if a lens is only gently curved, with a long focal length. In
  the 17th century astronomers built absurdly long telescopes. Johannes Hevelius made one with a 200 mm lens and a
  focal length of 46 m. Others left out the tube altogether: in these **aerial telescopes** the lens was hung high on a
  pole or a tower, far from the eyepiece. In 1684 Giovanni Domenico Cassini used one to find two moons of Saturn,
  Dione and Tethys.
- **Mirrors.** Isaac Newton concluded that the fringes come from glass bending colours unequally, and built a
  telescope with a mirror instead in 1668 (chapter 9).
- **Two glasses.** The cure was to combine a converging lens of **crown glass** with a weaker diverging lens of
  **flint glass**, which spreads colours more. The flint undoes the colour spreading of the crown but leaves part of
  its bending (section 10.11). The English lawyer **Chester Moore Hall** made the first such **achromatic** lenses in
  1729 or 1733 and kept them secret. The optician **John Dollond**, son of a Huguenot refugee in London, took out a
  patent in 1758, which led to bitter fights with other opticians.

??? note "Sources"
    - Chromatic aberration from dispersion, the coloured fringes, and Newton's reflecting telescope of 1668: Wikipedia,
      [Chromatic aberration](https://en.wikipedia.org/wiki/Chromatic_aberration) (weaker).
    - Hevelius's f/225 telescope with a 200 mm lens and 46 m focal length: Wikipedia,
      [Refracting telescope](https://en.wikipedia.org/wiki/Refracting_telescope) (weaker).
    - Aerial telescopes, and Cassini finding Dione and Tethys in 1684: Wikipedia,
      [Aerial telescope](https://en.wikipedia.org/wiki/Aerial_telescope) (weaker).
    - Crown and flint, Hall's secret, Dollond's patent of 1758 and the fights over it: Wikipedia,
      [Achromatic lens](https://en.wikipedia.org/wiki/Achromatic_lens) (weaker). Hall's dates of 1729 or 1733:
      Wikipedia, [Chester Moore Hall](https://en.wikipedia.org/wiki/Chester_Moore_Hall) (weaker). Dollond's family:
      Wikipedia, [John Dollond](https://en.wikipedia.org/wiki/John_Dollond) (weaker).

## 10.7 The great refractors { #great }

With achromatic lenses, telescopes with lenses (**refractors**) grew bigger through the 19th century.

- **Yerkes, 1897.** The refractor at Yerkes Observatory in Wisconsin, with a two-part lens 40 inches (1.02 m) across
  made by Alvan Clark & Sons, was the largest in the world when it was dedicated in 1897. It is still the largest
  refracting telescope in the world.
- **Paris, 1900.** For the Paris Exhibition of 1900, a refractor was built with a lens 1.25 m across and a focal length
  of 57 m, the largest ever made. A movable flat mirror 2 m across sent starlight into its tube. No buyer was found
  and it was scrapped.

Why stop there? A lens can only be held at its edge, so a big lens sags under its own weight and distorts the image.
Glass also has bubbles and streaks, and it absorbs some wavelengths. The largest practical lens for a telescope is
about 1 m across. A mirror, by contrast, can be supported all over its back (chapter 9), so the great telescopes of
the 20th century were all reflectors.

??? note "Sources"
    - The Yerkes 40-inch refractor by Alvan Clark & Sons, largest when dedicated in 1897: Wikipedia,
      [Yerkes Observatory](https://en.wikipedia.org/wiki/Yerkes_Observatory) (weaker).
    - The Paris telescope of 1900, the largest refractor ever built, its 1.25 m lens, 57 m focal length, the 2 m
      siderostat mirror, and its scrapping: Wikipedia,
      [Great Paris Exhibition Telescope of 1900](https://en.wikipedia.org/wiki/Great_Paris_Exhibition_Telescope_of_1900)
      (weaker).
    - Lens sag, support only at the edge, about 1 m as the largest practical lens, glass defects and absorption:
      Wikipedia, [Refracting telescope](https://en.wikipedia.org/wiki/Refracting_telescope) (weaker).

## 10.8 Bent starlight { #sky }

The Earth's air is a weak lens wrapped round the planet. It is densest at the ground, so starlight coming in at a
slant is bent downwards on the way, and every star looks a little higher than it really is. At the horizon the lift
is about 35 minutes of arc, more than the width of the Sun (book 1,
[chapter 2, section 2.11](../night-sky/02-Horizon-Zenith-and-the-Four-Directions.md#refraction)).

- **Mirages.** Air close to hot ground or cold sea bends light so strongly that we see a shifted image of distant
  objects or of the sky. The shimmering "water" on a hot road is an image of the sky, easily mistaken for a pool.
- **The green flash.** Air bends blue and green light a little more than red. Just as the last sliver of the Sun
  sets, a green spot can sometimes flash above it, usually for no more than two seconds.
- **Twinkling.** Moving pockets of warmer and cooler air bend starlight this way and that, so stars twinkle
  (chapter 12).

??? note "Sources"
    - Refraction lifting stars, about 35′ at the horizon: this site's book 1, chapter 2, section 2.11.
    - Mirages as displaced images of distant objects or the sky, inferior and superior mirages, and hot roads:
      Wikipedia,
      [Mirage](https://en.wikipedia.org/wiki/Mirage) (weaker).
    - The green flash, its cause and its two seconds: Wikipedia,
      [Green flash](https://en.wikipedia.org/wiki/Green_flash) (weaker).
    - Turbulent air making objects twinkle: Wikipedia,
      [Atmospheric refraction](https://en.wikipedia.org/wiki/Atmospheric_refraction) (weaker).

## 10.9 Lenses and air at Mars { #mars }

**Hardly any bending.** Mars's air is mostly carbon dioxide, which bends light a little more than our air does. But it
is so thin, with a pressure at the ground of only about 6 millibars against our 1,013, that it bends starlight about
80 times less than the Earth's air (section 10.10). An astronomer on Mars would barely need to correct for it.

**Zoom lenses on a rover.** Rover cameras use lenses. Curiosity's Mastcam has two cameras with fixed focal lengths.
Perseverance's **Mastcam-Z**, designed and built by Malin Space Science Systems in San Diego and led by Jim Bell of
Arizona State University, has two **zoom** cameras on the rover's mast that can change their focal length over a range
of 3.6 to 1. Being a pair, they see in stereo, like two eyes, and through filters they take pictures in many colours.

??? note "Sources"
    - Carbon dioxide's refractive index of 1.00045 at 0 °C and 1 atm: Wikipedia,
      [Refractive index](https://en.wikipedia.org/wiki/Refractive_index) (weaker).
    - Mars's surface pressure of 6.36 mb: NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - Mastcam's fixed focal lengths and Mastcam-Z's two zoom cameras, 3.6:1 zoom, stereo and many colours, Malin Space
      Science Systems and Jim Bell: Wikipedia, [Mastcam-Z](https://en.wikipedia.org/wiki/Mastcam-Z) (weaker).

## 10.10 Working it out { #working }

**Using the law.** Light in air ($n = 1$) hits glass ($n = 1.5$) at 30° to the normal:

$$\sin \theta_2 = \frac{\sin 30°}{1.5} = 0.333, \qquad \theta_2 = 19.5°.$$

Light hitting water ($n = 1.333$) at 45°: $\sin \theta_2 = 0.707 / 1.333 = 0.530$, so $\theta_2 = 32.0°$.

**Critical angle.** Going out of a material into air, the outside angle reaches 90° when $\sin \theta_c = 1/n$:

| Material | $n$ | Critical angle |
| --- | --- | --- |
| Water | 1.333 | 48.6° |
| Glass | 1.5 | 41.8° |
| Diamond | 2.417 | 24.4° |

**Bending by the air.** A star at height $h$, at least 45° above the horizon, is lifted by about $(n - 1)/\tan h$
radians, where $n$ is the refractive index of the air at the ground. The amount $n - 1$ grows in proportion to the
density of the gas.

- Earth, air at 10 °C: $n - 1 = 0.000293 \times 273/283 = 0.000283$.
- Mars, carbon dioxide at 6.36 millibars and 214 K: $n - 1 = 0.00045 \times (6.36/1{,}013) \times (273/214) =
  0.0000036$.

| | Mars | Earth |
| --- | --- | --- |
| Air pressure at the ground | 6.36 millibars | 1,013 millibars |
| Temperature used | 214 K | 283 K (10 °C) |
| $n - 1$ for the air at the ground | 0.0000036 | 0.000283 |
| Lift of a star 45° up | 0.74 seconds of arc | 58 seconds of arc |

??? note "Sources"
    - The formula $R = (n_0 - 1) \cot h_a$, good within 45° of the zenith: Wikipedia,
      [Atmospheric refraction](https://en.wikipedia.org/wiki/Atmospheric_refraction) (weaker).
    - Refractive indices of air (1.000293) and carbon dioxide (1.00045) at 0 °C and 1 atm, and of water and diamond:
      Wikipedia, [Refractive index](https://en.wikipedia.org/wiki/Refractive_index) (weaker).
    - Mars's surface pressure (6.36 mb) and average temperature (about 214 K): NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - The arithmetic is ours.

## 10.11 The lens-maker's formula { #lensmaker }

For a thin lens of glass with refractive index $n$, whose two faces are curved with radii $R_1$ and $R_2$,

$$\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right),$$

where a face bulging towards the incoming light has a positive radius and one hollowed towards it a negative radius.
For a lens bulging equally on both sides, $R_1 = R$ and $R_2 = -R$, so

$$f = \frac{R}{2(n - 1)}.$$

With ordinary glass, $n = 1.5$, the focal length equals the radius of the faces.

**The colour error.** Since $1/f$ is proportional to $n - 1$, a small change $\Delta n$ in the refractive index changes
the focal length by the fraction $\Delta n / (n - 1)$. Lens makers measure a glass's colour spread by its **Abbe
number**, named after the German physicist Ernst Abbe:

$$V = \frac{n_d - 1}{n_F - n_C},$$

where $n_F$, $n_d$ and $n_C$ are the refractive indices at 486.1 nm, 587.6 nm and 656.3 nm. Two of these are
hydrogen's lines from chapter 7. Then the blue (486.1 nm) and red (656.3 nm) foci differ by the fraction $1/V$ of the
focal length. Common crown glass has $V$ of about 65; flint glasses are below 55, and dense flints below 25.

- A crown-glass lens with a 1 m focal length has its blue and red foci $1{,}000 / 65 = 15$ mm apart.

**Cancelling it.** For two thin lenses touching, the powers $P = 1/f$ add. The colour errors cancel when

$$\frac{P_1}{V_1} + \frac{P_2}{V_2} = 0.$$

For a doublet with a total focal length of 1 m, made of crown with $V_1 = 65$ and a flint with $V_2 = 35$:
$P_1 = 65/30 = 2.17$ and $P_2 = -35/30 = -1.17$ per metre. So the crown lens has a focal length of 0.46 m and the
flint lens $-0.86$ m. The flint, being a weaker diverging lens, takes away about half of the crown's bending, but all
of its colour.

??? note "Sources"
    - The Abbe number, its definition with the C, d and F lines at 656.3, 587.56 and 486.1 nm, Ernst Abbe, and the
      ranges for flint and crown glasses: Wikipedia, [Abbe number](https://en.wikipedia.org/wiki/Abbe_number) (weaker).
    - The lens-maker's formula and the achromat condition are standard results; the worked numbers are ours.

## Check yourself { #check }

**1.** (beginner) Why does a pencil in a glass of water look bent?

??? note "Answer"
    Light from the part under water bends as it passes from water into air, because it travels faster in air.

**2.** (beginner) Glass has a refractive index of 1.5. How fast does light travel in it?

??? note "Answer"
    $300{,}000 / 1.5 = 200{,}000$ km/s.

**3.** (beginner) What is the difference between a converging and a diverging lens?

??? note "Answer"
    A converging lens is thicker in the middle and brings parallel rays together at a focus; a diverging lens is
    thinner in the middle and spreads them apart.

**4.** (intermediate) Who first wrote down the correct law of refraction, and when?

??? note "Answer"
    Ibn Sahl, at the court in Baghdad, in 984.

**5.** (intermediate) What is chromatic aberration, and how did 17th-century astronomers reduce it?

??? note "Answer"
    Coloured fringes caused by a lens bending blue light more than red. They built telescopes with very long focal
    lengths, even aerial telescopes with no tube.

**6.** (intermediate) Why is there no lens telescope much bigger than about 1 m across?

??? note "Answer"
    A lens can only be held at its edge, so a big one sags and distorts the image; big pieces of glass also have
    flaws and absorb light. Mirrors can be supported from behind.

**7.** (advanced) Light in air hits water ($n = 1.333$) at 60° to the normal. At what angle does it travel in the water?

??? note "Answer"
    $\sin \theta_2 = \sin 60° / 1.333 = 0.866 / 1.333 = 0.650$, so $\theta_2 = 40.5°$.

**8.** (expert) A lens of crown glass ($n = 1.5$, $V = 65$) bulges equally on both sides, with faces of radius 0.5 m.
What is its focal length, and how far apart are its blue and red foci?

??? note "Answer"
    $f = 0.5 / (2 \times 0.5) = 0.5$ m. The foci are $500 / 65 = 7.7$ mm apart.

## Summary

- Light slows down in water and glass; the refractive index $n$ says by how much.
- Light bends towards the normal entering a slower material: $n_1 \sin\theta_1 = n_2 \sin\theta_2$, first found by
  Ibn Sahl in 984.
- Beyond the critical angle light is trapped inside glass; optical fibres use this.
- Converging lenses bring parallel light to a focus; diverging lenses spread it.
- Lenses go back to burning glasses and rock crystal; spectacles came from Italy about 1290, telescopes from the
  Netherlands in 1608.
- A single lens focuses colours at different places; very long telescopes, mirrors and crown-and-flint doublets were
  the answers.
- Lens telescopes stopped at about 1 m (Yerkes, 1897) because big lenses sag.
- Air lifts starlight by up to about 35′ on Earth; Mars's thin air bends it about 80 times less.
- $1/f = (n-1)(1/R_1 - 1/R_2)$; the colour error is the fraction $1/V$ of the focal length.

**Next:** chapter 11, How a telescope makes an image, where lenses and mirrors are put together to magnify the sky.

## Further reading

- Vincent Ilardi, *Renaissance Vision from Spectacles to Telescopes*, American Philosophical Society, 2007.
