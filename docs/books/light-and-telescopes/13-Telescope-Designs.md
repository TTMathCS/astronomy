# 13. Telescope designs

*There are only two ways to bring light to a focus, with a lens or with a curved mirror, but there are many ways to
arrange them. This chapter tours the main designs: the refractor, Newton's reflector, the folded telescopes of Gregory
and Cassegrain, the Ritchey–Chrétien used by Hubble and most large observatories, Bernhard Schmidt's wide-angle camera,
the compact telescopes sold to amateurs, and John Dobson's cheap, big "sidewalk" telescope. It then looks at how a
telescope is held and turned to follow the stars, from Su Song's water-driven clock tower to the computer-driven mounts
of today, and at the folded telescope that photographs Mars from orbit.*

!!! abstract "In this chapter"
    **You will learn:**

    - the three families of telescope, and the strengths and weaknesses of each
    - how a Newtonian telescope works
    - how Gregory and Cassegrain folded the light to make shorter telescopes
    - why most large telescopes are Ritchey–Chrétiens
    - how Schmidt's camera photographs wide areas of sky
    - which designs amateurs use, and why
    - the difference between altazimuth and equatorial mounts
    - how the HiRISE telescope fits a 12 m focal length into a 1.6 m box
    - how mirrors shaped like parabolas, ellipses and hyperbolas work together

    **You need:** chapters 9, 10 and 11, and book 1,
    [chapter 6](../night-sky/06-Rising-Setting-and-the-Pole-Star.md), on how the sky turns.

    **Levels:** 13.1 to 13.3 are beginner; 13.4 to 13.9 are intermediate; 13.10 is advanced; 13.11 is expert.

## 13.1 Three families { #families }

| Family | Brings light to a focus with | Good | Not so good |
| --- | --- | --- | --- |
| **Refractor** | lenses (chapter 10) | no mirror blocking the light | colour fringes, unless costly special glass is used; big lenses sag |
| **Reflector** | mirrors (chapter 9) | no colour fringes; mirrors can be made very large | a smaller mirror or camera usually sits in the light path |
| **Catadioptric** | a mirror and a thin lens together | short tube, or a wide sharp view | a curved image (Schmidt), or a second mirror in the light path |

**Why the biggest telescopes are reflectors.** A lens can only be held by its edge, so a large one sags under its own
weight and distorts the image. The largest practical lens is about 1 m across, the size of the Yerkes refractor
(chapter 10). A mirror can be supported all over its back, and the largest, such as Keck's (chapter 9), are ten times
as wide.

**The shadow in the middle.** A concave mirror brings light to a focus in front of itself, so nearly every reflector
needs a second mirror, or a camera, near that focus, partly blocking the light coming in.

??? note "Sources"
    - Colour fringing in refractors, costly apochromats, lens sag with the lens held only by its edge, and about 1 m
      as the largest practical lens: Wikipedia,
      [Refracting telescope](https://en.wikipedia.org/wiki/Refracting_telescope) (weaker).
    - Parabolic mirrors without chromatic aberration, and almost all reflectors having a secondary mirror or detector
      near the focus partly obstructing the light: Wikipedia,
      [Reflecting telescope](https://en.wikipedia.org/wiki/Reflecting_telescope) (weaker).
    - Catadioptric designs combining mirrors and lenses: Wikipedia,
      [Catadioptric system](https://en.wikipedia.org/wiki/Catadioptric_system) (weaker).

## 13.2 Newton's reflector { #newtonian }

In the **Newtonian** telescope a concave main mirror at the bottom of the tube reflects the light back up. Before it
reaches the focus, a small flat mirror set at 45° turns it out through the side of the tube to the eyepiece.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Two reflecting telescopes, each a tube with light entering from the left. Top, a Newtonian: a concave main mirror at the far end sends the light back up the tube, and a small flat mirror set at 45 degrees near the front turns it out through the side of the tube to an eyepiece. Bottom, a Cassegrain: the concave main mirror has a hole in its centre. A small convex mirror near the front sends the light back down the tube, through the hole, to an eyepiece behind the main mirror. Folding the light back this way makes the Cassegrain tube much shorter than its focal length.">
  <g font-size="8" fill="currentColor">
    <rect x="30" y="45" width="262" height="60" fill="none" stroke="#555" stroke-width="0.8"/>
    <polyline points="279.0,47 279.3,51 279.5,55 279.7,59 279.8,63 279.9,67 280.0,71 280.0,75 280.0,79 279.9,83 279.8,87 279.7,91 279.5,95 279.3,99 279.0,103" fill="none" stroke="currentColor" stroke-width="2"/>
    <line x1="113" y1="63" x2="137" y2="87" stroke="currentColor" stroke-width="2"/>
    <rect x="117" y="18" width="16" height="12" fill="#5aa0d8" fill-opacity="0.3" stroke="currentColor" stroke-width="0.8"/>
    <polyline points="8,55 279.5,55 120.9,70.9 125,30" fill="none" stroke="#eea66f" stroke-width="1"/>
    <polyline points="8,95 279.5,95 130.0,80.0 125,30" fill="none" stroke="#eea66f" stroke-width="1"/>
    <text x="300" y="58">main</text>
    <text x="300" y="68">mirror</text>
    <text x="300" y="78">(concave)</text>
    <text x="141" y="27">eyepiece</text>
    <text x="141" y="102">flat mirror at 45°</text>
    <text x="6" y="12">Newtonian: a flat mirror turns the light out of the side</text>
    <rect x="30" y="150" width="240" height="60" fill="none" stroke="#555" stroke-width="0.8"/>
    <polyline points="258.7,152 258.9,154 259.0,156 259.2,158 259.3,160 259.5,162 259.6,164 259.7,166 259.8,168 259.8,170 259.9,172 259.9,174" fill="none" stroke="currentColor" stroke-width="2"/>
    <polyline points="259.9,186 259.9,188 259.8,190 259.8,192 259.7,194 259.6,196 259.5,198 259.3,200 259.2,202 259.0,204 258.9,206 258.7,208" fill="none" stroke="currentColor" stroke-width="2"/>
    <path d="M150,171 Q156,180 150,189" fill="none" stroke="currentColor" stroke-width="2"/>
    <rect x="303" y="174" width="14" height="12" fill="#5aa0d8" fill-opacity="0.3" stroke="currentColor" stroke-width="0.8"/>
    <polyline points="8,160 259.3,160 152,174.4 305,180" fill="none" stroke="#eea66f" stroke-width="1"/>
    <polyline points="8,200 259.3,200 152,185.6 305,180" fill="none" stroke="#eea66f" stroke-width="1"/>
    <text x="150" y="166" text-anchor="middle">convex mirror</text>
    <text x="262" y="222" text-anchor="middle">main mirror with a hole</text>
    <text x="310" y="198" text-anchor="middle">eyepiece</text>
    <text x="6" y="138">Cassegrain: a convex mirror folds the light back through a hole</text>
  </g>
</svg>
</div>

*Figure A. Two ways to get the light out of a reflector.*

Newton's first, finished in 1668, is the earliest reflecting telescope known to have worked (chapter 9). Its design is
so simple that it is still very popular with people who make their own telescopes.

William Herschel did without the second mirror. He tilted his main mirror so that he could look straight at its focus
from the front of the tube without his head blocking the light coming in. He built his great 40-foot telescope this
way in 1789.

??? note "Sources"
    - The concave primary and flat diagonal secondary, Newton's telescope of 1668 as the earliest known working
      reflector, and its popularity with amateur telescope makers: Wikipedia,
      [Newtonian telescope](https://en.wikipedia.org/wiki/Newtonian_telescope) (weaker).
    - The Herschelian reflector with its tilted primary, and the 40-foot telescope of 1789: Wikipedia,
      [Reflecting telescope](https://en.wikipedia.org/wiki/Reflecting_telescope) (weaker).

## 13.3 Folding the light: Gregory and Cassegrain { #cassegrain }

A long focal length gives a big image (chapter 11), but a long tube is heavy, wobbly and hard to house. Two designs of
the 1660s and 1670s fold the light back on itself.

- **Gregory, 1663.** The Scottish mathematician **James Gregory** described a telescope with two concave mirrors in
  his book *Optica Promota*. The main mirror brings the light to a focus; beyond it a small concave mirror sends it
  back through a hole in the middle of the main mirror. The image is the right way up. Gregory had no practical skill
  and could find no optician able to make one; **Robert Hooke** built the first in 1673.
- **Cassegrain, 1672.** In April 1672 a French journal printed a design with a small **convex** mirror instead,
  placed before the focus. It is credited to **Laurent Cassegrain**, a Catholic priest born near Chartres. The convex
  mirror makes the cone of light narrower, so the focal length grows, and the light comes out behind the main mirror.
  Ideas like it had been written down by Bonaventura Cavalieri in 1632 and Marin Mersenne in 1636.

Folding makes the telescope short and compact. The Cassegrain arrangement, and versions of it, is now very common in
large telescopes, Hubble among them, and in good amateur ones. Gregory's design is used in the Magellan
telescopes in Chile and the Large Binocular Telescope in Arizona, and in radio telescopes such as Green Bank and
MeerKAT (chapter 17).

??? note "Sources"
    - Gregory's *Optica Promota* of 1663, two concave mirrors, the light reflected back through a hole in the primary,
      the erect image, Gregory's failed attempts, Hooke's first in 1673, and the Magellan and Large Binocular
      telescopes and radio telescopes using Gregorian optics: Wikipedia,
      [Gregorian telescope](https://en.wikipedia.org/wiki/Gregorian_telescope) (weaker).
    - The design in the journal of 25 April 1672, the convex secondary, the folded compact path, the earlier
      writings of Cavalieri (1632) and Mersenne (1636), and its use in Hubble, Keck, the VLT and high-grade amateur
      telescopes: Wikipedia, [Cassegrain reflector](https://en.wikipedia.org/wiki/Cassegrain_reflector) (weaker).
    - Cassegrain as a Catholic priest born in the region of Chartres around 1629: Wikipedia,
      [Laurent Cassegrain](https://en.wikipedia.org/wiki/Laurent_Cassegrain) (weaker).

## 13.4 The Ritchey–Chrétien { #rc }

A parabolic mirror is perfect for a star in the middle of the view, but stars near the edge come out shaped like
little comets, a fault called **coma**. For photographs of wide areas of sky this matters.

In the early 1910s the American astronomer **George Willis Ritchey** and the French astronomer **Henri Chrétien**
designed a Cassegrain with both mirrors shaped as **hyperbolas** (section 13.11), which removes coma. Ritchey built the
first successful one, 60 cm across, in 1927.

Since the middle of the 20th century most large research telescopes have been Ritchey–Chrétiens:

- the Hubble Space Telescope (chapter 12);
- the Keck telescopes in Hawaii (chapter 9);
- Europe's Very Large Telescope in Chile;
- India's 2 m Himalayan Chandra Telescope at Hanle (chapter 12).

??? note "Sources"
    - Ritchey and Chrétien in the early 1910s, hyperbolic primary and secondary to remove off-axis errors, Ritchey's
      60 cm telescope of 1927, the majority of large telescopes since the mid 20th century, Hubble, Keck, the VLT,
      and the Himalayan Chandra Telescope: Wikipedia,
      [Ritchey–Chrétien telescope](https://en.wikipedia.org/wiki/Ritchey%E2%80%93Chr%C3%A9tien_telescope) (weaker).

## 13.5 Schmidt's camera { #schmidt }

**Bernhard Schmidt** grew up on the island of Naissaar, off Tallinn in Estonia, then part of the Russian Empire. As a
boy of 15 he packed an iron pipe with gunpowder and it exploded; he lost his right hand. He became a maker of lenses
and mirrors anyway, and from 1916 he was in touch with the Hamburg Observatory at Bergedorf in Germany.

In 1930 he invented the **Schmidt camera**:

- a **spherical** main mirror, which is easy to make;
- a thin glass **corrector plate** at the mirror's centre of curvature, shaped to cancel the mirror's spherical
  aberration (chapter 9);
- the film at the focus, inside the tube, on a curved holder, because the image is strongly curved.

It gave sharp pictures over a wide area of sky with short exposures. Big Schmidts at Palomar in California, in
Australia (the UK Schmidt) and in Chile (the ESO Schmidt) made most of the photographic maps of the whole sky from 1950
to 2000, when electronic cameras took over. ESA's Hipparcos satellite (1989 to 1993) and NASA's Kepler planet hunter
were built round Schmidt designs, and China's **LAMOST**, the Guo Shoujing Telescope, is a reflecting Schmidt that
feeds 4,000 optical fibres at once (chapter 8; history book,
[chapter 4, section 4.10](../history/04-China.md#guo)).

??? note "Sources"
    - Schmidt as an Estonian optician, born and raised on Naissaar off Tallinn, then in the Russian Empire, the
      explosion at 15 and the loss of his right hand, contact with the Hamburg Observatory from 1916, and the
      invention of 1930: Wikipedia, [Bernhard Schmidt](https://en.wikipedia.org/wiki/Bernhard_Schmidt) (weaker).
    - The spherical primary, the corrector plate at the centre of curvature, the strongly curved focal plane, the
      Palomar (Samuel Oschin), UK and ESO Schmidts as the main source of all-sky photographs from 1950 to 2000,
      Hipparcos and Kepler: Wikipedia, [Schmidt camera](https://en.wikipedia.org/wiki/Schmidt_camera) (weaker).
    - LAMOST as a reflecting Schmidt with 4,000 fibres, named after Guo Shoujing: Wikipedia,
      [LAMOST](https://en.wikipedia.org/wiki/LAMOST) (weaker).

## 13.6 Short telescopes for everyone { #compact }

Two designs combine a mirror and a thin lens to fit a long focal length into a short tube.

- **Schmidt–Cassegrain.** The American astronomer **James Gilbert Baker** proposed adding a Cassegrain's convex
  mirror to a Schmidt camera in 1940, and the optical shop at Mount Wilson made the first during the Second World War.
  It is now one of the most popular designs sold to amateurs, because all its surfaces are spherical and easy to make,
  and it gives the long focal length of a refractor in a tube a fraction of the length.
- **Maksutov.** In 1941 the Soviet optician **Dmitri Maksutov** patented a design with a bowl-shaped lens called a
  **meniscus** in front of a spherical mirror. Albert Bouwers patented a similar one the same year. Maksutovs have
  been sold to amateurs since the 1950s.

??? note "Sources"
    - Baker's proposal of 1940, the first made at Mount Wilson during the Second World War, and its popularity with
      consumer makers for its spherical surfaces and long focal length in a short tube: Wikipedia,
      [Schmidt–Cassegrain telescope](https://en.wikipedia.org/wiki/Schmidt%E2%80%93Cassegrain_telescope) (weaker).
    - Maksutov's patent of 1941, the meniscus lens and spherical mirror, Bouwers's patent of 1941, and sales since the
      1950s: Wikipedia, [Maksutov telescope](https://en.wikipedia.org/wiki/Maksutov_telescope) (weaker).

## 13.7 Dobson's sidewalk telescope { #dobson }

**John Dobson** was born in Beijing in 1915 to missionary parents and grew up to study chemistry. He spent 23 years as
a monk of a Vedanta order. After leaving the order he co-founded the
**San Francisco Sidewalk Astronomers** in 1968, to bring astronomy to people on the street.

His telescopes, which he called "sidewalk telescopes", were Newtonians on a very simple mount: a plywood box that
turns round on a base and lets the tube tilt up and down, sliding on strips of Teflon. He made mirrors from ship's
porthole glass. Everything could be bought at a hardware store. The **Dobsonian** made big telescopes cheap, and it
greatly increased the size of telescope an amateur could own. Dobson died in 2014.

??? note "Sources"
    - Dobson's dates, birth in Beijing to missionary parents, chemistry, 23 years as a Vedanta monk, leaving in 1967,
      and the San Francisco Sidewalk Astronomers of 1968: Wikipedia,
      [John Dobson](https://en.wikipedia.org/wiki/John_Dobson_(amateur_astronomer)) (weaker).
    - The design popularised in 1965, porthole glass, plywood and Teflon, "sidewalk telescope", and the great increase
      in size of amateur telescopes: Wikipedia, [Dobsonian telescope](https://en.wikipedia.org/wiki/Dobsonian_telescope)
      (weaker).
    - Parts found in any hardware store: Wikipedia, [Altazimuth mount](https://en.wikipedia.org/wiki/Altazimuth_mount)
      (weaker).

## 13.8 Holding a telescope { #mounts }

The sky turns once a day (book 1, [chapter 6](../night-sky/06-Rising-Setting-and-the-Pole-Star.md#turning)), so a star
drifts out of a telescope's view within minutes, or seconds at high magnification. The mount must hold the telescope
steady and let it follow.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Two ways to hold a telescope. Left, an altazimuth mount: the telescope turns round a vertical axis, like a door, to face any direction, and tilts up and down about a horizontal axis. To follow a star it must move on both axes at changing speeds. Right, an equatorial mount: one axis, the polar axis, is tilted to point at the celestial pole, at an angle above the horizon equal to the observer's latitude, so it is parallel to the Earth's own axis. Turning that one axis slowly, once a day, keeps a star in view. A counterweight balances the telescope.">
  <g font-size="8" fill="currentColor">
    <line x1="8" y1="210" x2="160" y2="210" stroke="#555" stroke-width="1"/>
    <line x1="180" y1="210" x2="332" y2="210" stroke="#555" stroke-width="1"/>
    <line x1="80" y1="225" x2="80" y2="95" stroke="#5aa0d8" stroke-width="1" stroke-dasharray="3 2"/>
    <rect x="62" y="196" width="36" height="14" fill="#cfc8bf" fill-opacity="0.5" stroke="currentColor" stroke-width="0.8"/>
    <path d="M68,196 L68,150 M92,196 L92,150" stroke="currentColor" stroke-width="2"/>
    <circle cx="80" cy="150" r="3" fill="none" stroke="currentColor" stroke-width="1"/>
    <polygon points="126.1,128.7 115.8,113.9 50.3,159.8 60.6,174.6" fill="#5aa0d8" fill-opacity="0.2" stroke="currentColor" stroke-width="1"/>
    <path d="M58,218 A22,6 0 1 0 102,218" fill="none" stroke="#c1440e" stroke-width="1"/>
    <path d="M98,222 L102,218 L97,215" fill="none" stroke="#c1440e" stroke-width="1"/>
    <text x="108" y="232">turn round</text>
    <path d="M140,130 A62,62 0 0 0 128,95" fill="none" stroke="#c1440e" stroke-width="1"/>
    <path d="M124,99 L128,95 L130,100" fill="none" stroke="#c1440e" stroke-width="1"/>
    <text x="122" y="145">tilt up</text>
    <text x="122" y="155">and down</text>
    <text x="10" y="40">Altazimuth</text>
    <text x="10" y="52">two moves at changing</text>
    <text x="10" y="62">speeds to follow a star</text>
    <rect x="208" y="200" width="28" height="10" fill="#cfc8bf" fill-opacity="0.5" stroke="currentColor" stroke-width="0.8"/>
    <line x1="222" y1="200" x2="268.0" y2="161.4" stroke="currentColor" stroke-width="3"/>
    <line x1="268.0" y1="161.4" x2="329.2" y2="110.0" stroke="#5aa0d8" stroke-width="1" stroke-dasharray="3 2"/>
    <text x="329.2" y="108.0" text-anchor="middle" font-size="12">✶</text>
    <text x="325.2" y="96.0" text-anchor="end">celestial pole</text>
    <line x1="284.7" y1="181.3" x2="248.7" y2="138.5" stroke="currentColor" stroke-width="2"/>
    <circle cx="284.7" cy="181.3" r="6" fill="#555"/>
    <polygon points="248.7,92.7 233.0,95.5 245.1,164.5 260.9,161.7" fill="#5aa0d8" fill-opacity="0.2" stroke="currentColor" stroke-width="1"/>
    <path d="M252,210 A30,30 0 0 0 245.0,190.7" fill="none" stroke="#c1440e" stroke-width="1"/>
    <text x="256" y="207">latitude</text>
    <text x="298.7" y="197.3" text-anchor="middle">counterweight</text>
    <text x="240.0" y="165.4" text-anchor="end">polar axis</text>
    <text x="185" y="232">one slow turn a day follows the stars</text>
    <text x="185" y="40">Equatorial</text>
  </g>
</svg>
</div>

*Figure B. The two kinds of mount.*

- **Altazimuth.** The simplest mount turns round a vertical axis and tilts about a horizontal one, like Dobson's. To
  follow a star it must move on both axes at once, at speeds that keep changing.
- **Equatorial.** One axis, the **polar axis**, is tilted to point at the celestial pole, so it is parallel to the
  Earth's own axis. Its angle above the horizon equals your latitude. Then a single slow turn of that axis, once a
  day, follows the stars. A motor that does this is a **clock drive**. Joseph von Fraunhofer designed the "German"
  equatorial mount for the Great Dorpat Refractor, finished in 1824.

**The first clock drive.** Over 700 years earlier, in 1092, **Su Song** described the great astronomical clock tower
he had built at Kaifeng in China. A water wheel, held to a steady pace by an escapement, turned an armillary sphere on
its roof so that it kept pace with the sky. It was the first armillary sphere driven by clockwork (history book,
[chapter 4, section 4.9](../history/04-China.md#machines)).

**Today.** An equatorial mount for a giant telescope would be enormously heavy and costly. Since computers became able
to steer two axes at once, nearly all large research telescopes use altazimuth mounts.

**Where the light goes.** A heavy instrument is hard to hang on the back of a moving telescope. In a **Nasmyth** focus
a third mirror sends the light out to the side of the telescope, where heavy instruments can be mounted. In a
**coudé** focus (French for "elbow") more mirrors bring it to a fixed place that does not move as the telescope turns,
where large spectrographs can be built (chapter 15).

??? note "Sources"
    - The altazimuth mount's vertical and horizontal axes: Wikipedia,
      [Altazimuth mount](https://en.wikipedia.org/wiki/Altazimuth_mount) (weaker).
    - The polar axis parallel to the Earth's axis, the clock drive, and Fraunhofer's German equatorial mount for the
      Great Dorpat Refractor of 1824: Wikipedia, [Equatorial mount](https://en.wikipedia.org/wiki/Equatorial_mount)
      (weaker).
    - The pole's height equal to the latitude: book 1, chapter 7.
    - Su Song's tower at Kaifeng, his treatise of 1092, the escapement of Yi Xing and Liang Lingzan, and the first
      armillary sphere with a mechanical clock drive: Wikipedia, [Su Song](https://en.wikipedia.org/wiki/Su_Song)
      (weaker).
    - Altazimuth mounts in practically all modern large research telescopes since digital tracking: Wikipedia,
      [Telescope mount](https://en.wikipedia.org/wiki/Telescope_mount) (weaker).
    - The Nasmyth focus, the coudé focus from the French for elbow, and large spectrographs: Wikipedia,
      [Coudé focus](https://en.wikipedia.org/wiki/Coud%C3%A9_focus) (weaker).

## 13.9 A folded telescope at Mars { #mars }

Every kilogram sent to Mars is costly, and a spacecraft has little room, so a long focal length has to be folded up.

- **HiRISE.** The telescope on NASA's Mars Reconnaissance Orbiter (chapter 9) has a 0.5 m mirror at f/24, so its
  focal length is about 12 m. Yet the whole instrument is only about 1.6 m long and 0.9 m wide, and weighs about
  65 kg. Mirrors fold the light back and forth inside it. From 300 km up, each pixel covers about 30 cm, the size of a
  basketball, in pictures 6 km wide.
- **CTX.** Beside it, the Context Camera, with a focal length of 350 mm at f/3.25, takes wider pictures, 30 km
  across, to show where the HiRISE close-ups fit.
- **ChemCam.** On the mast of the Curiosity rover, a small telescope focuses ChemCam's laser on a rock several metres
  away, and its camera, the Remote Micro-Imager, can see a human hair 2 m away (chapter 7).

??? note "Sources"
    - HiRISE's 0.5 m aperture at f/24: HiRISE team, [HiRISE specifications](https://www.uahirise.org/specs/).
    - HiRISE's focal length of about 12 m, its size, mass, 30 cm pixels from 300 km and 6 km swath, and CTX's 350 mm
      at f/3.25 and 30 km swath: NASA,
      [MRO science instruments](https://science.nasa.gov/mission/mars-reconnaissance-orbiter/science-instruments/).
    - ChemCam's telescope on the mast focusing the laser and the camera: NASA,
      [Curiosity science instruments](https://science.nasa.gov/mission/msl-curiosity/science-instruments/); the hair
      seen 2 m away: ChemCam team, [ChemCam](https://www.msl-chemcam.com/).

## 13.10 Working it out { #working }

**The shadow of the second mirror.** The light blocked is the area of the second mirror over the area of the main
one, $(d/D)^2$.

| Telescope | Main mirror | Second mirror | Light blocked |
| --- | --- | --- | --- |
| Amateur Newtonian | 200 mm | 50 mm | 6.3% |
| Amateur Newtonian | 150 mm | 35 mm | 5.4% |

**Folding.** HiRISE's focal length is $0.5 \times 24 = 12$ m, in an instrument 1.6 m long: the light path is folded
into about $12/1.6 = 7.5$ times less length.

**Following the stars.** A clock drive turns the polar axis once per **sidereal day**, the time the planet takes to
spin once against the stars.

| | Mars | Earth |
| --- | --- | --- |
| Sidereal day | 24.6229 hours | 23.9345 hours |
| Clock drive speed | $360°/24.6229 = 14.62°$ an hour | $360°/23.9345 = 15.04°$ an hour |
| Polar axis tilted at | your latitude | your latitude |
| It points near | Deneb, in Cygnus (no bright pole star) | Polaris |

An equatorial mount carried from Earth to Mars would need its clock drive slowed by about 3%, and its polar axis
pointed at a different part of the sky (book 1,
[chapter 6, section 6.8](../night-sky/06-Rising-Setting-and-the-Pole-Star.md#mars)).

??? note "Sources"
    - Sidereal rotation periods: NASA, [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - Mars's north celestial pole in Cygnus near Deneb: book 1, chapter 6, section 6.8.
    - HiRISE: section 13.9. The amateur mirror sizes are typical values.
    - The arithmetic is ours.

## 13.11 Parabola, ellipse, hyperbola { #conics }

Each mirror in this chapter is a slice of a **conic section**, a curve you get by cutting a cone, and each has its own
trick with light.

- **Parabola.** Rays coming in parallel to its axis all meet at one point, the focus (chapter 9). That is the main
  mirror of a Newtonian or a classic Cassegrain.
- **Ellipse.** It has two foci. Light leaving one focus reflects to the other. In a Gregorian, the main mirror's focus
  is placed at one focus of a concave elliptical second mirror, which sends the light on to its other focus, behind
  the main mirror.
- **Hyperbola.** It also has two foci, but light heading *towards* one focus reflects off the convex side towards the
  other. In a Cassegrain, the light converging on the main mirror's focus meets a convex hyperbolic second mirror
  first, and is sent to the second focus instead.

**How much longer?** If the main mirror's focus is a distance $p$ beyond the second mirror, and the final focus is a
distance $q$ from the second mirror, the second mirror multiplies the focal length by $m = q/p$:

$$F = m f_1.$$

For example, a main mirror of focal length 1 m with $m = 4$ gives a 4 m focal length in a telescope little more than
1 m long. HiRISE's 12 m in a 1.6 m instrument comes from the same idea, with extra folding mirrors.

**Why Schmidt used a sphere.** A sphere looks the same from its centre in every direction. Put the corrector plate,
and the opening of the telescope, at that centre, and a star at the edge of the view meets the mirror in exactly the
same way as a star in the middle. There is no special axis, so there is no coma and no astigmatism; the plate only has
to fix the spherical aberration, which is the same for every star.

??? note "Sources"
    - The parabolic primary and hyperbolic secondary of the classic Cassegrain: Wikipedia,
      [Cassegrain reflector](https://en.wikipedia.org/wiki/Cassegrain_reflector) (weaker).
    - The concave paraboloid primary and concave ellipsoid secondary of the Gregorian: Wikipedia,
      [Gregorian telescope](https://en.wikipedia.org/wiki/Gregorian_telescope) (weaker).
    - The corrector at the centre of curvature, and the Schmidt correcting spherical aberration, coma and astigmatism:
      Wikipedia, [Schmidt camera](https://en.wikipedia.org/wiki/Schmidt_camera) and
      [Bernhard Schmidt](https://en.wikipedia.org/wiki/Bernhard_Schmidt) (weaker).
    - The focal properties of the conic sections and the magnification of the secondary are standard geometry.

## Check yourself { #check }

**1.** (beginner) What are the three families of telescope?

??? note "Answer"
    Refractors, which use lenses; reflectors, which use mirrors; and catadioptrics, which use a mirror and a thin
    lens together.

**2.** (beginner) Why are the world's largest telescopes reflectors?

??? note "Answer"
    A lens can only be held by its edge, so a big one sags and distorts the image; about 1 m is the practical limit.
    A mirror can be supported all over its back, and it shows no colour fringes.

**3.** (beginner) In a Newtonian telescope, what does the small flat mirror do?

??? note "Answer"
    It is set at 45° and turns the light from the main mirror out through the side of the tube to the eyepiece.

**4.** (intermediate) How does a Cassegrain differ from a Gregorian?

??? note "Answer"
    A Cassegrain uses a small convex second mirror placed before the main mirror's focus; a Gregorian uses a small
    concave one placed beyond the focus, and gives an upright image. Both send the light back through a hole in the
    main mirror.

**5.** (intermediate) What problem did Schmidt's camera solve, and how?

??? note "Answer"
    It took sharp pictures of a wide area of sky. A spherical mirror has no special axis, and a thin corrector plate at
    its centre of curvature cancels its spherical aberration.

**6.** (intermediate) Why does an equatorial mount need only one motor to follow a star?

??? note "Answer"
    Its polar axis is parallel to the Earth's axis, so turning that one axis once a sidereal day cancels the Earth's
    spin.

**7.** (advanced) A Newtonian has a 250 mm main mirror and a 60 mm second mirror. What fraction of the light is blocked?

??? note "Answer"
    $(60/250)^2 = 0.0576$, about 5.8%.

**8.** (expert) A Cassegrain's main mirror has a focal length of 2 m. Its convex second mirror sits 0.4 m in front of
the main mirror's focus and sends the light to a focus 2.4 m from the second mirror. What is the final focal length,
and roughly how long is the telescope?

??? note "Answer"
    $m = q/p = 2.4/0.4 = 6$, so $F = 6 \times 2 = 12$ m. The second mirror is $2 - 0.4 = 1.6$ m from the main
    mirror, so the tube is about 1.6 m long, with the focus $2.4 - 1.6 = 0.8$ m behind the main mirror.

## Summary

- Refractors use lenses, reflectors use mirrors, and catadioptrics use both. Lenses larger than about 1 m sag.
- Newton's reflector of 1668 turns the light out of the side with a flat mirror at 45°.
- Gregory (1663) and Cassegrain (1672) folded the light back through a hole in the main mirror.
- Most large telescopes, Hubble among them, are Ritchey–Chrétiens with two hyperbolic mirrors.
- Bernhard Schmidt's camera of 1930 photographed wide areas of sky; Schmidts mapped the whole sky from 1950 to 2000.
- Schmidt–Cassegrains and Maksutovs pack long focal lengths into short tubes; Dobson made big Newtonians cheap.
- An equatorial mount follows the stars with one axis; Su Song's tower drove an armillary sphere by clockwork in
  the 11th century; large telescopes now use computer-driven altazimuth mounts.
- HiRISE folds a 12 m focal length into an instrument 1.6 m long.
- Parabolas, ellipses and hyperbolas each send light from one focus to another in their own way.

**Next:** chapter 14, From eye to camera, where we follow the light from the eyepiece to photographic plates and
electronic sensors.

## Further reading

- Philip S. Harrington, *Star Ware: The Amateur Astronomer's Guide to Choosing, Buying, and Using Telescopes and
  Accessories*, 4th edition, Wiley, 2007.
