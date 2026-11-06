# 16. Newton, Halley and Rømer

*Kepler had found three rules for the planets but could not say why they held. Galileo had shown how things fall on the
Earth but not what holds the Moon up. In the 1680s Isaac Newton joined the two: the force that pulls an apple down
also holds the Moon in its orbit and the planets round the Sun, and it gets weaker with the square of the distance.
His friend Edmond Halley used it to show that a comet comes back, and in Paris a young Dane, Ole Rømer, used Jupiter's
moons to show that light takes time to travel. In the same years two astronomers, one in Paris and one in South
America, measured how far away Mars is, and with it the size of the whole solar system.*

!!! abstract "In this chapter"
    **You will learn:**

    - how Newton linked the falling apple and the Moon, and why Halley mattered to the *Principia*
    - how one law of gravity explains Kepler's three laws, and how it works for Phobos as well as the Moon
    - how Rømer found that light has a speed, from eclipses of Io
    - how the distance to Mars in 1672 gave the first good size for the solar system
    - how Halley's comet came back on time, with help from Nicole-Reine Lepaute and her colleagues
    - how Newton's ideas reached Japan, India, Istanbul, Bogotá and Maryland

    **You need:** chapter 14 (Kepler's laws, especially section 14.10) and chapter 15 (Jupiter's moons and the moons of
    Mars in section 15.9). The physics lessons
    [The apple and the Moon](https://physics.akadian.ca/topics/gravity/level-4/01-the-apple-and-the-moon.html),
    [Weaker with distance](https://physics.akadian.ca/topics/gravity/level-4/02-weaker-with-distance.html),
    [The law of gravity](https://physics.akadian.ca/topics/gravity/level-6/01-the-law-of-gravity.html),
    [Light takes time](https://physics.akadian.ca/topics/spacetime/level-3/01-light-takes-time.html) and
    [The speed of light](https://physics.akadian.ca/topics/waves/level-5/03-the-speed-of-light.html) help with
    sections 16.2, 16.3 and 16.8.

    **Levels:** 16.1 to 16.3 are beginner; 16.4 to 16.7 are intermediate; 16.8 is advanced; 16.9 is expert.

## 16.1 A boy from Woolsthorpe { #newton }

Isaac Newton was born on Christmas Day 1642 in the calendar England then used (**4 January 1643** in ours) at
Woolsthorpe Manor, a farmhouse in Lincolnshire. He went to Trinity College, Cambridge, and took his first degree in
August 1665, just as the university closed because of the Great Plague. In 1665 he found
the general binomial theorem and began what became calculus, and in the same years he started thinking about gravity
and light.

**The apple.** Newton often told the story that watching an apple fall from a tree started his thinking about gravity.
His friend William Stukeley wrote down one such conversation, from 15 April 1726. The apple did not hit him on the head:
that part was added later.

**A new telescope.** In 1669, at 26, Newton became professor of mathematics at Cambridge. In late 1668 he had built the
earliest known working **reflecting telescope**, which uses a curved mirror instead of a lens; with it he could see Jupiter's
moons and the crescent of Venus. He showed one to the Royal Society in 1672 and was elected a Fellow. He also showed
that a prism splits white light into colours (chapter 18).

??? note "Sources"
    - Birth on 25 December 1642 (4 January 1643), Woolsthorpe Manor, the degree of August 1665 and the plague, the
      binomial theorem and calculus from 1665, the professorship in 1669 at 26, the reflecting telescope of late 1668,
      Jupiter's moons and the crescent of Venus, the Royal Society in 1672, the prism, the apple story told by Newton,
      Stukeley's conversation of 15 April 1726, the apple on the head as a later addition: Wikipedia,
      [Isaac Newton](https://en.wikipedia.org/wiki/Isaac_Newton) (weaker).
    - The earliest known working reflecting telescope: Wikipedia,
      [Newtonian telescope](https://en.wikipedia.org/wiki/Newtonian_telescope) (weaker).

## 16.2 The *Principia*: one law for the sky and the ground { #principia }

**A question among friends.** In January 1684 Halley, the architect Christopher Wren and the scientist Robert Hooke
talked about the planets. Hooke said he could show that a force weakening with the square of the distance gives
Kepler's laws, but he never produced the proof. In August 1684 Halley went to Cambridge to ask Newton, and found he had
already solved it. Newton sent Halley a short paper, *De motu*, "on motion", in late 1684, and then turned it into a great book. **Halley** edited it and paid for it himself. *Philosophiæ Naturalis Principia
Mathematica*, "the mathematical principles of natural philosophy", came out on **5 July 1687**.

**What it said.** The *Principia* set out three laws of motion and one law of gravity: every body pulls every other
with a force that grows with their masses and weakens with the square of the distance. From that, Newton showed why
the planets move on ellipses, why they sweep equal areas, and why the square of the period goes with the cube of the
distance. The same law explained the tides, the slow wobble of the Earth's axis, the paths of comets, and the bulge of
the Earth at the equator.

**The Moon test.** At the Earth's surface a dropped stone falls 4.9 m in its first second. The Moon is about 60 Earth
radii away, so if gravity weakens with the square of the distance, the Moon should fall towards the Earth
$60^2 = 3{,}600$ times less, about 1.4 mm in a second. That is just what it must do to curve round its orbit instead of
flying off in a straight line. The same test works at Mars, with Phobos (section 16.8).

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Moons fall too. Left: Mars and Phobos, drawn to scale; Phobos is 2.77 Mars radii from the centre, where Mars pulls with 3.73 divided by 2.77 squared, 0.487 metres per second squared. In one second Phobos falls about 24 centimetres below the straight line it would follow without gravity. Right: the Earth and the Moon, not to scale; the Moon is 60.3 Earth radii away, where the pull is 9.82 divided by 60.3 squared, 0.0027 metres per second squared, so the Moon falls about 1.4 millimetres in a second. The gaps are drawn much larger than they are.">
  <circle cx="85" cy="115" r="61" fill="none" stroke="currentColor" stroke-width="0.6" stroke-dasharray="3 2" opacity="0.7"/>
  <circle cx="85" cy="115" r="22" fill="#c1440e"/>
  <line x1="85" y1="54" x2="155" y2="54" stroke="currentColor" stroke-width="0.8" stroke-dasharray="4 2"/>
  <path d="M85 54 A61 61 0 0 1 120.0 65.0" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <line x1="113.6" y1="55.5" x2="113.6" y2="59.6" stroke="#c1440e" stroke-width="1.2"/>
  <circle cx="85" cy="54" r="3.5" fill="currentColor"/>
  <g font-size="9" fill="currentColor">
    <text x="85" y="16" text-anchor="middle">Mars and Phobos</text>
    <text x="79" y="48" text-anchor="end">Phobos</text>
    <text x="116.6" y="49" fill="#c1440e">falls 24 cm</text>
    <text x="85" y="196" text-anchor="middle" font-size="8">pull 3.73 ÷ 2.77² = 0.487 m/s²</text>
    <text x="85" y="207" text-anchor="middle" font-size="8">to scale</text>
  </g>
  <path d="M191.9 79.9 A110 110 0 0 1 318.1 79.9" fill="none" stroke="currentColor" stroke-width="0.6" stroke-dasharray="3 2" opacity="0.7"/>
  <circle cx="255" cy="170" r="6" fill="#5aa0d8"/>
  <line x1="255" y1="60" x2="325" y2="60" stroke="currentColor" stroke-width="0.8" stroke-dasharray="4 2"/>
  <path d="M255 60 A110 110 0 0 1 318.1 79.9" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <line x1="306.6" y1="61.5" x2="306.6" y2="71.4" stroke="#c1440e" stroke-width="1.2"/>
  <circle cx="255" cy="60" r="3.5" fill="currentColor"/>
  <g font-size="9" fill="currentColor">
    <text x="255" y="16" text-anchor="middle">Earth and the Moon</text>
    <text x="249" y="54" text-anchor="end">Moon</text>
    <text x="306.6" y="85.9" fill="#c1440e" text-anchor="middle">falls 1.4 mm</text>
    <text x="255" y="196" text-anchor="middle" font-size="8">pull 9.82 ÷ 60.3² = 0.0027 m/s²</text>
    <text x="255" y="207" text-anchor="middle" font-size="8">not to scale</text>
  </g>
  <line x1="170" y1="26" x2="170" y2="212" stroke="currentColor" stroke-width="0.4" opacity="0.4"/>
  <g font-size="8" fill="currentColor">
    <text x="170" y="232" text-anchor="middle">Dashed: the straight path with no gravity. Red: how far each moon</text>
    <text x="170" y="243" text-anchor="middle">falls below it in one second (gaps drawn far larger than they are)</text>
  </g>
</svg>
</div>

**Who was first?** Hooke had written in the 1670s that all heavenly bodies attract one another, and is often credited
with first suggesting that the pull falls with the square of the distance. His letters to Newton in 1679 and 1680
brought Newton back to the problem. Newton said Hooke had told him nothing new. Hooke had the idea; Newton had the
mathematics that proved it, and the two never made peace.

??? note "Sources"
    - The conversation of January 1684, Hooke's claim and missing proof, Halley's visits of August and November 1684,
      *De motu*, Halley's encouragement, Kepler's laws from an inverse-square force, the tides, precession and comets:
      Wikipedia, [Philosophiæ Naturalis Principia Mathematica](https://en.wikipedia.org/wiki/Philosophi%C3%A6_Naturalis_Principia_Mathematica)
      (weaker).
    - *De motu* in the Royal Society's register in December 1684, publication on 5 July 1687, the bulge of the Earth,
      Newton's notebooks of the late 1660s on gravity reaching the Moon: Wikipedia,
      [Isaac Newton](https://en.wikipedia.org/wiki/Isaac_Newton) (weaker). Published at Halley's expense: Wikipedia,
      [Edmond Halley](https://en.wikipedia.org/wiki/Edmond_Halley) (weaker).
    - Hooke's 1674 lecture, gravitation in "all celestial bodies", the inverse-square idea, the letters of 1679 to 1680,
      Newton's reply that Hooke told him nothing new: Wikipedia, [Robert Hooke](https://en.wikipedia.org/wiki/Robert_Hooke)
      (weaker).
    - The figure and the Moon test: our calculation from NASA's
      [Earth](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html),
      [Moon](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html) and
      [Mars](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html) fact sheets.

## 16.3 Rømer: light takes time { #light }

Many people, Hooke among them, thought light was so fast that it was as good as instant. **Ole Rømer**, born in Aarhus in Denmark on
25 September 1644, showed it does not.

In 1671 Rømer helped the French astronomer Jean Picard time about 140 eclipses of Jupiter's moon Io from Hven, where
Tycho's observatory had stood (chapter 14), while Cassini timed them in Paris. Io goes behind Jupiter, into its
shadow, every 42.5 hours, and the tables were good enough to find longitude by. Rømer then joined the Paris
Observatory. He noticed that the eclipses came **early** when the Earth was moving towards Jupiter and **late** when it
was moving away. In 1676 he predicted that Io would come out of Jupiter's shadow on 16 November about ten minutes later
than the tables said, and it did.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Rømer and the speed of light. The Sun is at the centre of the Earth's orbit and Jupiter is far to the right, with its moon Io going in and out of Jupiter's shadow. When the Earth is on the near side of its orbit, the light from Io has a short way to come. Months later, with the Earth on the far side, the light has to cross up to the whole width of the Earth's orbit as well, so the eclipses of Io are seen late. The extra trip takes 16.6 minutes; Rømer estimated 22.">
  <circle cx="120" cy="125" r="60" fill="none" stroke="#5aa0d8" stroke-width="0.8" opacity="0.7"/>
  <circle cx="120" cy="125" r="7" fill="#eea66f"/>
  <rect x="300" y="119" width="40" height="12" fill="currentColor" opacity="0.15"/>
  <circle cx="300" cy="125" r="6" fill="#cfc8bf" stroke="currentColor" stroke-width="0.5"/>
  <circle cx="300" cy="125" r="16" fill="none" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2 2"/>
  <circle cx="315" cy="120" r="2" fill="currentColor"/>
  <line x1="293" y1="123" x2="176.4" y2="104.5" stroke="#eea66f" stroke-width="1" stroke-dasharray="0"/>
  <circle cx="176.4" cy="104.5" r="4" fill="#5aa0d8"/>
  <line x1="293" y1="123" x2="63.6" y2="104.5" stroke="#eea66f" stroke-width="1" stroke-dasharray="4 2"/>
  <circle cx="63.6" cy="104.5" r="4" fill="#5aa0d8"/>
  <line x1="60" y1="147" x2="180" y2="147" stroke="currentColor" stroke-width="0.8"/>
  <line x1="60" y1="143" x2="60" y2="151" stroke="currentColor" stroke-width="0.8"/>
  <line x1="180" y1="143" x2="180" y2="151" stroke="currentColor" stroke-width="0.8"/>
  <g font-size="9" fill="currentColor">
    <text x="120" y="143" text-anchor="middle" fill="#eea66f" font-size="8">Sun</text>
    <text x="180.4" y="95.5" fill="#5aa0d8">Earth near Jupiter</text>
    <text x="61.6" y="95.5" fill="#5aa0d8">Earth far from Jupiter</text>
    <text x="300" y="155" text-anchor="middle">Jupiter</text><text x="320" y="113" font-size="8">Io</text>
    <text x="120" y="163" text-anchor="middle" font-size="8">width of the Earth's orbit, 299 million km</text>
    <text x="6" y="210">The far Earth sees each eclipse of Io late, by up to the time light</text>
    <text x="6" y="222">takes to cross the Earth's orbit: 16.6 minutes. Rømer said 22.</text>
  </g>
</svg>
</div>

Rømer's explanation was that the light from Io has farther to travel when the Earth is on the far side of its orbit.
He reckoned that light takes about **22 minutes** to cross the Earth's orbit. Cassini, his director, was never fully
convinced, but Huygens and Newton were. The true time is 16.6 minutes; Rømer's idea was right even though his number
was too big.

Proof came in 1725 to 1728, when **James Bradley** in England found that every star seems to swing in a small yearly
loop because the Earth is moving through the light coming from it, like rain that seems to slant when you run. That
gave light a time of 8 minutes 12 seconds from the Sun, only about 1.3% too long, and it was direct evidence that the
Earth moves round the Sun.

Rømer later went home to Denmark, became chief of police of Copenhagen, and designed a thermometer whose scale Daniel
Fahrenheit built on after visiting him in 1708. His observation records were lost in the Copenhagen fire of 1728.

??? note "Sources"
    - Picard and Rømer at Hven in 1671 with about 140 eclipses of Io, birth on 25 September 1644 in Aarhus, chief of
      police from 1705, the thermometer and Fahrenheit's visit in 1708, the fire of 1728: Wikipedia,
      [Ole Rømer](https://en.wikipedia.org/wiki/Ole_R%C3%B8mer) (weaker).
    - Cassini's eclipse tables and longitude, early and late eclipses, the prediction for 16 November 1676 of about
      ten minutes, 22 minutes across the orbit, Cassini not convinced, Huygens and Newton in support, Newton's "seven or
      eight minutes" in 1704 against the true 8 minutes 19 seconds: Wikipedia,
      [Rømer's determination of the speed of light](https://en.wikipedia.org/wiki/R%C3%B8mer%27s_determination_of_the_speed_of_light)
      (weaker).
    - Hooke on light as virtually instantaneous, Io's period of 42½ hours: as above.
    - Bradley's aberration of 1725 to 1728 and 8 minutes 12 seconds, 1.3% too high: Wikipedia,
      [James Bradley](https://en.wikipedia.org/wiki/James_Bradley) (weaker). Aberration as direct evidence of the
      Earth's motion: Wikipedia, [Galileo affair](https://en.wikipedia.org/wiki/Galileo_affair) (weaker).
    - The 16.6 minutes: our calculation from the astronomical unit and the speed of light, section 16.8.

## 16.4 How far is Mars? { #distance }

Kepler's third law gives the **shape** of the solar system: Mars is 1.524 times as far from the Sun as the Earth,
Jupiter 5.2 times, and so on. But it does not give the size in kilometres. Measure one distance and you have them all.

The best distance to measure was Mars, at a close opposition. In **1672** Mars came very near the Earth. Cassini
watched it from Paris while his colleague **Jean Richer** watched it from **Cayenne** in French Guiana, in South
America. Seen from two places 7,000 km apart, Mars should appear in slightly different places against the stars, and
the size of that shift gives its distance (chapter 14, section 14.10). Their result put the Sun about **22,000 Earth
radii** away, about 138 million km. That is about 8% short of the true value, but it was the first time anyone had the
right size for the solar system. They could turn Earth radii into kilometres because Picard had just measured the
Earth, in 1669. In England, John Flamsteed made his own estimate the same year from Mars's daily parallax alone.

**A clock that ran slow.** In Cayenne, Richer also found that a pendulum swinging once a second had to be about 2 mm
shorter than in Paris. Newton took this as a sign that gravity is weaker near the equator because the Earth bulges
there; Huygens put it down to the Earth's spin. Both effects are real.

**Better ways.** Halley proposed timing the **transits of Venus** across the Sun from places far apart. They were
observed in 1761 and 1769, including by Cook and Green in Tahiti (chapter 12). Since 2012 the astronomical unit, the
standard Earth to Sun distance, has been fixed as exactly **149,597,870,700 m**.

??? note "Sources"
    - Richer and Cassini, Paris and Cayenne, Mars at its closest in 1672, solar parallax 9.5″ and about 22,000 Earth
      radii, Picard's Earth radius of 1669, Flamsteed's estimate the same year, Halley's transit method, 1761 and 1769
      with Cook and Green, the value of 149,597,870,700 m fixed in 2012: Wikipedia,
      [Astronomical unit](https://en.wikipedia.org/wiki/Astronomical_unit) (weaker).
    - Simultaneous observations of Mars in 1672: Wikipedia,
      [Giovanni Domenico Cassini](https://en.wikipedia.org/wiki/Giovanni_Domenico_Cassini) (weaker).
    - Richer in Cayenne from 1671 to 1673, the pendulum 2.256 mm shorter, Newton's oblateness and Huygens's
      centrifugal force: Wikipedia, [Jean Richer](https://en.wikipedia.org/wiki/Jean_Richer) (weaker).
    - The 7,000 km between Paris and Cayenne, the 138 million km and the 8%: our calculation, section 16.8.

## 16.5 Halley's comet { #halley }

**Edmond Halley** was a generous scientist with a restless life. As a young man he sailed to **Saint Helena** in the
South Atlantic, set up an observatory there in 1676 to 1677, and catalogued 341 southern stars, published in 1679.
He also built a diving bell, and in 1720 became Astronomer Royal.

**One comet, not three.** Using Newton's gravity, Halley worked out the orbits of 24 comets. Three of them, seen in
**1531, 1607 and 1682**, had almost the same orbit. He decided they were one comet coming back about every 76 years,
and predicted its return in **1758**. He died in 1742, so he never saw it.

**The return.** As 1758 came near, three people in Paris, **Alexis Clairaut**, **Jérôme Lalande** and
**Nicole-Reine Lepaute**, worked out how much the pulls of Jupiter and Saturn would delay the comet.
They predicted it would round the Sun in mid-April 1759. On **25 December 1758** Johann Palitzsch, a German farmer and
amateur astronomer, saw it first, and it passed the Sun on **13 March 1759**, a month before their date and 618 days
later than it would have without the giant planets. Lepaute went on to compute the annular eclipse of 1764 and publish
maps of it under her own name.

**Older records.** Chinese astronomers recorded the comet in 240 BC (chapter 4), a Babylonian clay tablet records it in
September 164 BC, and it is stitched into the Bayeux Tapestry of 1066. A line in the Babylonian Talmud about "a star
which appears once in seventy years" may refer to it. The comet goes round the Sun the opposite way to the planets,
from 0.59 to 35 times the Earth's distance. The spacecraft Giotto photographed its nucleus in March 1986, and it will
next round the Sun on 28 July 2061.

??? note "Sources"
    - Saint Helena in 1676 to 1677, 341 stars in 1679, the transit of Mercury, the diving bell of 1691, Astronomer Royal
      in 1720, the orbit work using Newton's law, the prediction for 1758, death in 1742: Wikipedia,
      [Edmond Halley](https://en.wikipedia.org/wiki/Edmond_Halley) (weaker).
    - 24 comets, 1531 (Apianus), 1607 (Kepler) and 1682, Palitzsch on 25 December 1758, perihelion on 13 March 1759,
      618 days from Jupiter and Saturn, Clairaut, Lalande and Lepaute with a one-month error, 240 BC, 164 BC, 1066,
      the Talmud passage, the retrograde orbit, 0.59 and 35 au, Giotto in 1986, 28 July 2061: Wikipedia,
      [Halley's Comet](https://en.wikipedia.org/wiki/Halley%27s_Comet) (weaker).
    - Lepaute's work from June 1757, the eclipse of 1 April 1764 and her maps: Wikipedia,
      [Nicole-Reine Lepaute](https://en.wikipedia.org/wiki/Nicole-Reine_Lepaute) (weaker).

## 16.6 Newton goes round the world { #world }

- **Japan, 1798.** **Shizuki Tadao**, an interpreter of Dutch in Nagasaki, translated a Dutch edition of John Keill's
  book on Newton's physics in his *Rekishō shinsho*. He had to invent Japanese words for gravity, *jūryoku*, attraction,
  *inryoku*, and centrifugal force, *enshinryoku*, which are still in use (chapter 6, section 6.8).
- **India.** In Lucknow, **Tafazzul Husain Kashmiri** (1727 to 1801) learned Greek, Latin and English and translated
  the *Principia* into Arabic, so it could be taught in Indian colleges.
- **Istanbul.** **İbrahim Müteferrika**, the first Muslim to run a printing press with movable Arabic type, printed
  Katip Çelebi's world atlas, *Cihannüma*, and added a long section on the Sun-centred system, with the arguments on each side.
- **Bogotá, 1762.** **José Celestino Mutis**, a Spanish priest and botanist in New Granada (today's Colombia), taught the
  Copernican system at the Colegio del Rosario. In 1774 he had to defend Copernicus and Newton's physics before the
  Inquisition. He found Bogotá's longitude from an eclipse of a moon of Jupiter, and helped found the observatory there.
- **Maryland, 1791.** **Benjamin Banneker**, a free African American farmer who taught himself astronomy from borrowed
  books, worked out the eclipses and the movements of the planets for an almanac for 1792. He sent his figures to Thomas
  Jefferson with a letter against slavery. Jefferson replied and passed the almanac to the French Academy. Many later
  stories about Banneker, such as designing the streets of Washington, are not true; the almanacs are.

??? note "Sources"
    - Shizuki Tadao, Keill's *Introductio ad Veram Physicam*, the *Rekishō shinsho* of 1798, and the words for gravity,
      attraction and centrifugal force: Wikipedia, [Rangaku](https://en.wikipedia.org/wiki/Rangaku) (weaker).
    - Tafazzul Husain Kashmiri, 1727 to 1801, Lucknow, his languages and the Arabic *Principia*: Wikipedia,
      [Tafazzul Husain Kashmiri](https://en.wikipedia.org/wiki/Tafazzul_Husain_Kashmiri) (weaker).
    - Müteferrika, his press, the *Cihannüma* and its section on heliocentrism: Wikipedia,
      [Ibrahim Muteferrika](https://en.wikipedia.org/wiki/Ibrahim_Muteferrika) (weaker).
    - Mutis, March 1762 at the Colegio del Rosario, the Inquisition in 1774, the longitude of Bogotá, the observatory:
      Wikipedia, [José Celestino Mutis](https://en.wikipedia.org/wiki/Jos%C3%A9_Celestino_Mutis) (weaker).
    - Banneker, free, self-taught, the 1792 almanac, the letter to Jefferson and the reply of 30 August 1791, the
      almanac sent to Condorcet, the false stories: Wikipedia,
      [Benjamin Banneker](https://en.wikipedia.org/wiki/Benjamin_Banneker) (weaker).

## 16.7 Newton's laws at Mars { #onmars }

Every spacecraft that has reached Mars got there by Newton's laws. And Rømer's discovery shapes how rovers are driven:
radio, like light, takes between about 3 and 22 minutes to cross from the Earth to Mars, so nobody can steer a rover
live with a joystick.

**A comet at Mars.** On 3 January 2013 Robert McNaught found a comet from **Siding Spring Observatory** in New South
Wales, Australia. Its orbit, worked out by Newton's law, showed it coming from the far edge of the solar system and
passing very close to Mars. On **19 October 2014** it went by at about **140,000 km** from Mars, at 56 km/s. The
spacecraft orbiting Mars, from the USA, Europe and India, hid behind the planet while the dust passed, and all came
through safely. MAVEN saw an intense meteor shower in the Martian sky, which left metals such as magnesium and iron in
the upper air.

??? note "Sources"
    - Discovery by Robert McNaught at Siding Spring on 3 January 2013, the pass of 19 October 2014 at 140,496.6 km and
      56 km/s, the orbiters of NASA, ESA and ISRO in good health, MAVEN's meteor shower, the metals: Wikipedia,
      [C/2013 A1 (Siding Spring)](https://en.wikipedia.org/wiki/C/2013_A1_(Siding_Spring)) (weaker).
    - The orbiters sheltering behind Mars, the comet from the Oort cloud: NASA,
      [Comet C/2013 A1 (Siding Spring)](https://science.nasa.gov/solar-system/comets/c-2013-a1-siding-spring/).
    - The 3 and 22 minutes: our calculation from NASA's nearest and farthest Earth to Mars distances, section 16.8.

## 16.8 Working it out { #working }

**The Moon test, at Mars and at the Earth.** Gravity at a planet's surface is $g$. At $n$ planet radii from the centre
it is $g / n^2$. A moon on a circular orbit of radius $r$ and period $T$ has to be pulled inwards by $4\pi^2 r / T^2$.
Newton's law passes the test if the two agree.

| | Mars and Phobos | Earth and the Moon |
|---|---|---|
| Surface gravity $g$ | 3.73 m/s² | 9.82 m/s² |
| Moon's distance $r$ | 9,378 km | 384,400 km |
| In planet radii, $n$ | 9,378 ÷ 3,389.5 = 2.767 | 384,400 ÷ 6,371 = 60.34 |
| Gravity there, $g / n^2$ | 0.487 m/s² | 0.00270 m/s² |
| Period $T$ | 0.31891 days | 27.3217 days |
| Needed to bend the orbit, $4\pi^2 r / T^2$ | 0.488 m/s² | 0.00272 m/s² |
| Fall below a straight line in 1 s | 24 cm | 1.4 mm |
| Light time to the Sun | 12.7 minutes | 8.3 minutes |

Both pass to within 1%; for Phobos the two numbers agree to 0.2%.

**Rømer's numbers.** One astronomical unit is 149,597,871 km, and light goes 299,792 km a second, so light takes
499 seconds, 8.3 minutes, from the Sun to the Earth, and $2 \times 499 = 998$ s, 16.6 minutes, to cross the Earth's
orbit. Rømer's 22 minutes would give light a speed of $299{,}196{,}000 / 1{,}320 \approx 227{,}000$ km/s. From the
Earth to Mars, light takes $54.6 \text{ million} / 299{,}792 = 182$ s, about 3 minutes, at the closest, and
$401.4 \text{ million} / 299{,}792 = 1{,}339$ s, about 22 minutes, at the farthest.

**The size of the solar system in 1672.** A solar parallax of 9.5″ means the Earth's radius looks 9.5″ wide from the
Sun, so the Sun is

$$\frac{6{,}371 \text{ km}}{9.5 / 206{,}265} \approx 138 \text{ million km}$$

away, about 8% short of 149.6 million km. Then Mars, at 1.524 times that, would be 211 million km from the Sun; the
true value is 228 million km.

**Halley's orbit.** With a period of about 75.5 years, Kepler's third law gives $a = 75.5^{2/3} = 17.9$ times the
Earth's distance. The nearest point is 0.59, so the farthest is $2 \times 17.9 - 0.59 = 35.2$, close to the 35 au
measured.

??? note "Sources"
    - Surface gravity, radii, distances and periods of Mars and Phobos, and the nearest and farthest Earth to Mars
      distances (54.6 and 401.4 million km): NASA, [Mars fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - The Earth and the Moon: NASA, [Earth fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html)
      and [Moon fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html).
    - The astronomical unit and the solar parallax of 9.5″: Wikipedia,
      [Astronomical unit](https://en.wikipedia.org/wiki/Astronomical_unit) (weaker). Halley's orbit, 0.59 and 35 au, and
      the dates 1986 and 2061: Wikipedia, [Halley's Comet](https://en.wikipedia.org/wiki/Halley%27s_Comet) (weaker).
    - All the arithmetic is ours.

## 16.9 How should we judge Newton and his circle? { #assessment }

**The greatest synthesis.** Newton's law joined the sky and the ground and turned Kepler's rules into consequences of
one cause. It let Halley predict a comet, Lepaute and her colleagues correct the date, and later astronomers find a new
planet from its pull (chapter 17). Spacecraft still fly by it.

**A difficult man.** Newton fought with Hooke over gravity and light, with the Astronomer Royal John Flamsteed, whose
star catalogue he had printed before Flamsteed was ready, and with the German mathematician Gottfried Leibniz over who
invented calculus. Historians now agree that Newton and Leibniz found it independently, but in 1713 the Royal Society's
report that found for Newton had been written by Newton himself. His famous line, "if I have seen further it is by
standing on the shoulders of giants", was written to Hooke in 1675; some read it as modest, others as a dig at Hooke,
who was said to be short and bent.

**More than physics.** Newton spent much of his time on alchemy and on the Bible, ran the Royal Mint for
thirty years, and was President of the Royal Society from 1703. He died on 20 March 1727 in the old calendar
(31 March in ours), aged 84, and was the first scientist buried in Westminster Abbey.

**Helpers and rivals.** Halley got the *Principia* written and paid for it. Hooke asked the right question. Rømer and
Bradley showed light has a speed. Richer and Cassini sized the solar system. And the ideas were taken up, translated
and argued over in Nagasaki, Lucknow, Istanbul, Bogotá and Maryland within a century.

??? note "Sources"
    - Flamsteed's catalogue published early, the Mint (Warden 1696, Master 1699 to 1727), President of the Royal
      Society from 1703, alchemy and the Bible, death on 20 March 1727 (31 March), Westminster Abbey, the 1675 letter
      and its two readings: Wikipedia, [Isaac Newton](https://en.wikipedia.org/wiki/Isaac_Newton) (weaker).
    - Independent invention of calculus, the report of 1713 written by Newton: Wikipedia,
      [Leibniz–Newton calculus controversy](https://en.wikipedia.org/wiki/Leibniz%E2%80%93Newton_calculus_controversy)
      (weaker).

## Check yourself { #check }

**1.** (beginner) What did Halley do to get the *Principia* published?

??? note "Answer"
    He asked Newton the question that started it in 1684, encouraged him to write it, edited it and paid for it.

**2.** (beginner) What did Rømer find, and how?

??? note "Answer"
    That light takes time to travel. The eclipses of Jupiter's moon Io came late when the Earth was far from Jupiter
    and early when it was near, because the light had farther or less far to go.

**3.** (beginner) Which comet did Halley predict, and when was it first seen again?

??? note "Answer"
    The comet seen in 1531, 1607 and 1682, now called Halley's comet. Johann Palitzsch saw it on 25 December 1758.

**4.** (intermediate) Why did measuring the distance to Mars in 1672 give the distance to the Sun?

??? note "Answer"
    Kepler's third law already gave all the distances as multiples of the Earth's distance from the Sun. Measuring
    one of them in kilometres, Mars at a close opposition, fixed all the others.

**5.** (intermediate) Why did Halley's comet come back 618 days later than it would have without Jupiter and Saturn?

??? note "Answer"
    The pull of the giant planets changed its orbit as it passed them, so it took longer to return. Clairaut, Lalande
    and Lepaute calculated this delay before the comet came back.

**6.** (intermediate) Give one argument for Hooke and one for Newton in their quarrel about the law of gravity.

??? note "Answer"
    For Hooke: he wrote in the 1670s that all heavenly bodies attract each other, suggested the inverse square, and his
    letters of 1679 started Newton working on it again. For Newton: Hooke never produced a proof, and only Newton showed
    that the inverse square gives Kepler's three laws.

**7.** (advanced) Deimos is 23,459 km from the centre of Mars. Using $g = 3.73$ m/s² and Mars's radius of 3,389.5 km,
find the pull of Mars there, and the period Deimos needs to go round in a circle.

??? note "Answer"
    $n = 23{,}459 / 3{,}389.5 = 6.921$, so the pull is $3.73 / 6.921^2 = 0.0779$ m/s². Then
    $T = 2\pi \sqrt{r / a} = 2\pi \sqrt{23{,}459{,}000 / 0.0779} = 2\pi \times 17{,}353 = 109{,}000$ s, which is 1.26 days.
    NASA gives 1.26244 days.

**8.** (expert) Rømer's own number was 22 minutes across the Earth's orbit. If engineers on Mars had made the same
measurement from the far and near sides of Mars's orbit, how many minutes would they have found, and why is the
measurement easier from Mars? Then use the 1672 parallax value to say how far off their answer in kilometres would be.

??? note "Answer"
    Mars's orbit is $2 \times 1.524 = 3.048$ au wide, so light takes $3.048 \times 499 = 1{,}521$ s, 25.4 minutes, to
    cross it. The delay is half as large again as from the Earth, so the same timing errors matter less. If they had
    used the 1672 size of the solar system (138 million km to the au instead of 149.6), every distance, and so the
    speed of light worked out from the delay, would come out about 8% too small.

## Summary

- Newton (1643 to 1727) showed in the *Principia* (1687) that one law of gravity, weakening with the square of the
  distance, explains falling apples, the Moon, Kepler's three laws, tides and comets. Halley started it and paid for it.
- The same test that works for the Moon works for Phobos at Mars, and better.
- Rømer found in 1676 that light takes time, from the eclipses of Io; Bradley confirmed it in 1728 and showed the Earth
  moves.
- Cassini in Paris and Richer in Cayenne measured Mars in 1672 and put the Sun about 138 million km away, the first
  good size for the solar system.
- Halley predicted his comet's return; Clairaut, Lalande and Lepaute corrected the date; it came back in 1758 to 1759.
- Newton's ideas were translated and taught in Japan, India, the Ottoman Empire and the Americas within a century.
- In 2014 a comet found from Australia passed Mars, exactly where Newton's law said it would.

**Next:** [chapter 17, Herschel, and the canals of Mars](17-Herschel-and-the-Canals-of-Mars.md), where a musician found a new planet, two moons of Mars were
found in a week, and a mistranslated word started a long argument about life on Mars.

## Further reading

- Richard S. Westfall, *Never at Rest: A Biography of Isaac Newton*, Cambridge University Press, 1980.
- Isaac Newton, *The Principia: Mathematical Principles of Natural Philosophy*, translated by I. Bernard Cohen and Anne
  Whitman, University of California Press, 1999.
- Alan Cook, *Edmond Halley: Charting the Heavens and the Seas*, Oxford University Press, 1998.
- Lisa Jardine, *The Curious Life of Robert Hooke*, HarperCollins, 2003.
- Silvio A. Bedini, *The Life of Benjamin Banneker*, Scribner, 1972.
