# 10. Wobbling orbits and the finding of Neptune

*Kepler's ellipses are exact only when two bodies are alone. In the solar system every planet also pulls on every
other, so each orbit wobbles, slowly turns and slowly changes shape. This chapter shows how small those pulls are, how
they made Halley's comet late, and how astronomers in Paris and Cambridge worked backwards from the wobbles of Uranus to
a planet nobody had seen. Then it follows the same method into failure, with Vulcan and Planet X, and asks whether the
solar system will hold together at all.*

!!! abstract "In this chapter"
    **You will learn:**

    - why no planet follows a perfect, fixed ellipse
    - how Jupiter and Saturn made Halley's comet 618 days late
    - how Le Verrier and Adams worked from the wobbles of Uranus to Neptune, and what Neptune is called around the world
    - how orbits slowly turn, from the Moon's in 9 years to Mercury's, with 43 arcseconds a century left over
    - how the same method failed with Vulcan and Planet X, and why some astronomers now hunt for Planet Nine
    - whether the solar system is stable, from Laplace to computer runs in Paris and Toronto
    - how Mars's orbit turns and stretches, and how Mars spacecraft help pin down where the planets are
    - why a tiny push grows into a large error

    **You need:** chapters 4, 5 and 7.

    **Levels:** 10.1 to 10.3 are beginner; 10.4 to 10.7 are intermediate; 10.8 is advanced; 10.9 is expert.

## 10.1 Not quite ellipses { #wobble }

A planet alone with the Sun would go round the same ellipse for ever (chapter 5). But the Earth also feels Venus, Mars,
Jupiter and the rest. The biggest of these pulls comes from Jupiter. Even when Jupiter is at its closest, 4.2 AU away,
it pulls on the Earth only about 1/18,500 as hard as the Sun does. That is small, but it acts on every orbit, again and
again, and its effects add up.

Astronomers deal with this by asking: what ellipse would the planet follow if every other pull stopped right now?
That ellipse is called the **osculating orbit**, from the Latin for kissing, because it just touches the real path at
that moment. Its six numbers (chapter 4, [section 4.6](04-Ellipses.md#elements)) change slowly as time goes on. The
ellipse turns, so that its nearest point to the Sun, the **perihelion**, creeps round. It gets a little more or less
stretched, and it tilts.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="An orbit that slowly turns. The Sun sits at one focus of an ellipse. Five copies of the same ellipse are drawn, each turned a little further round the Sun, from faint to dark, with a dot at each perihelion, the nearest point to the Sun. A curved arrow shows the perihelion moving round in the same direction as the planet goes. The pulls of the other planets do this to every orbit. Mars's perihelion moves 0.44 degrees a century and goes once round in about 81,000 years; the Earth's moves 0.32 degrees a century and goes round in about 111,000 years. The drawing is stretched and speeded up a great deal.">
  <g font-size="8" fill="currentColor">
    <ellipse cx="122.7" cy="102.2" rx="70" ry="62.5" transform="rotate(30 122.7 102.2)" fill="none" stroke="#5aa0d8" stroke-width="0.9" stroke-opacity="0.25"/>
    <circle cx="183.3" cy="137.2" r="2.2" fill="#c1440e" fill-opacity="0.25"/>
    <ellipse cx="119.0" cy="112.5" rx="70" ry="62.5" transform="rotate(10 119.0 112.5)" fill="none" stroke="#5aa0d8" stroke-width="0.9" stroke-opacity="0.44"/>
    <circle cx="187.9" cy="124.7" r="2.2" fill="#c1440e" fill-opacity="0.44"/>
    <ellipse cx="119.0" cy="123.5" rx="70" ry="62.5" transform="rotate(-10 119.0 123.5)" fill="none" stroke="#5aa0d8" stroke-width="0.9" stroke-opacity="0.62"/>
    <circle cx="187.9" cy="111.3" r="2.2" fill="#c1440e" fill-opacity="0.62"/>
    <ellipse cx="122.7" cy="133.8" rx="70" ry="62.5" transform="rotate(-30 122.7 133.8)" fill="none" stroke="#5aa0d8" stroke-width="0.9" stroke-opacity="0.81"/>
    <circle cx="183.3" cy="98.8" r="2.2" fill="#c1440e" fill-opacity="0.81"/>
    <ellipse cx="129.8" cy="142.1" rx="70" ry="62.5" transform="rotate(-50 129.8 142.1)" fill="none" stroke="#5aa0d8" stroke-width="0.9" stroke-opacity="1.00"/>
    <circle cx="174.7" cy="88.5" r="2.2" fill="#c1440e" fill-opacity="1.00"/>
    <circle cx="150" cy="118" r="6" fill="#eea66f"/>
    <text x="150" y="134" text-anchor="middle">Sun</text>
    <path d="M194.6,141.7 L196.1,138.5 L197.5,135.3 L198.5,131.9 L199.4,128.5 L200.0,125.0 L200.4,121.5 L200.5,118.0 L200.4,114.5 L200.0,111.0 L199.4,107.5 L198.5,104.1 L197.5,100.7 L196.1,97.5 L194.6,94.3 L192.8,91.2 L190.9,88.3 L188.7,85.5 L186.3,82.9 L183.8,80.5" fill="none" stroke="#c1440e" stroke-width="0.9"/>
    <line x1="186.3" y1="82.9" x2="183.8" y2="80.5" stroke="#c1440e" stroke-width="0.9"/>
    <path d="M187.6,81.7 L183.8,80.5 L185.2,84.2" fill="none" stroke="#c1440e" stroke-width="0.9"/>
    <text x="186.3" y="72.7">perihelion moves round</text>
    <text x="214" y="104">Mars: 0.44° a century,</text>
    <text x="214" y="113">once round in 81,000 years</text>
    <text x="214" y="131">Earth: 0.32° a century,</text>
    <text x="214" y="140">once round in 111,000 years</text>
    <text x="6" y="12">An orbit that slowly turns</text>
    <text x="6" y="226">The pulls of the other planets make each ellipse turn slowly round the Sun, so the</text>
    <text x="6" y="235">perihelion, the nearest point, creeps forwards. Drawn far more stretched and far faster</text>
    <text x="6" y="244">than any planet: Mars's orbit is nearly round, and turns about 1° in 225 years.</text>
  </g>
</svg>
</div>

*Figure A. An orbit whose ellipse slowly turns.*

There are two ways to work out the changes. The old way, **general perturbations**, solves the equations with long
series of terms, worked by hand for centuries. The modern way, **special perturbations**, steps every planet forward a
little at a time on a computer, adding up all the pulls at each step.

??? note "Sources"
    - The osculating orbit as the orbit a body would have if perturbations were absent: Wikipedia,
      [Osculating orbit](https://en.wikipedia.org/wiki/Osculating_orbit) (weaker). The Latin meaning is standard.
    - General perturbations solved by series and special perturbations by numerical integration: Wikipedia,
      [Perturbation (astronomy)](https://en.wikipedia.org/wiki/Perturbation_(astronomy)) (weaker).
    - The rates at which Mars's and the Earth's perihelia move, 0.44441088° and 0.32327364° a century, a best fit for
      1800 to 2050: NASA JPL, [Approximate positions of the planets](https://ssd.jpl.nasa.gov/planets/approx_pos.html).
    - Jupiter's pull: our arithmetic in section 10.8.

## 10.2 A comet held back { #halley }

Edmond Halley worked out that the comets of 1531, 1607 and 1682 were one comet coming back, and predicted its return
for 1758 (history book, [section 16.5](../history/16-Newton-Halley-and-Romer.md#halley)). As the date came near, three
people in Paris, Alexis Clairaut, Jérôme Lalande and Nicole-Reine Lepaute, worked for more than six months, barely
stopping to eat, to find how much Jupiter and Saturn would hold it back. They predicted it would round the Sun on
13 April 1759. It did so on 13 March, a month early by their reckoning, but 618 days later than it would have without
the two giants. It was the first time anything other than a planet had been shown to go round the Sun.

Lalande wrote that they could never have done the sums without Lepaute. Clairaut left her name out of the book he
published in 1760.

A comet on a long, loose ellipse is easily pushed about: a small change in its speed changes the size of its orbit,
and so its period (chapter 7, [section 7.6](07-Speed-Energy-and-Escape.md#visviva)). The 618 days were about 2% of its
76-year period.

Records from around the world now help trace the comet's orbit back in time. The Chinese *Records of the Grand
Historian* note it in 240 BC (history book, [section 4.7](../history/04-China.md#guests)), and Babylonian tablets record
it in 164 and 87 BC (history book, [section 2.6](../history/02-Mesopotamia.md#diaries)). Working the orbit backwards
needs these ancient Chinese sightings. In March 1986 five spacecraft met it: Europe's Giotto, the Soviet Vega 1 and 2,
and Japan's Suisei and Sakigake. It will be back in 2061.

??? note "Sources"
    - The delay of 618 days from Jupiter and Saturn, perihelion on 13 March 1759, the prediction of 13 April by
      Clairaut, Lalande and Lepaute, the first proof that something other than planets orbits the Sun, Chinese records
      needed for the calculations, the Shiji record of 240 BC, the Babylonian tablets of 164 and 87 BC, Giotto, Vega 1
      and 2, Suisei and Sakigake in 1986, and the return in 2061: Wikipedia,
      [Halley's Comet](https://en.wikipedia.org/wiki/Halley%27s_Comet) (weaker).
    - More than six months of work, Lalande's thanks and Clairaut's 1760 book: Wikipedia,
      [Nicole-Reine Lepaute](https://en.wikipedia.org/wiki/Nicole-Reine_Lepaute) (weaker).
    - The 2% is our arithmetic.

## 10.3 A planet found by its pull { #neptune }

William Herschel found Uranus in 1781 (history book,
[section 17.1](../history/17-Herschel-and-the-Canals-of-Mars.md#herschel)). In 1821 Alexis Bouvard published tables
of where it should be, allowing for the pulls of Jupiter and Saturn. Uranus soon drifted away from them, both in its
place along its orbit and in its distance from the Sun. Perhaps the Sun's gravity was different so far out; perhaps the
old observations were wrong; or perhaps an unknown planet was pulling Uranus.

John Couch Adams in Cambridge and Urbain Le Verrier in Paris each tried the third idea. It was a sum done backwards.
Guess a planet: its mass, its orbit and where it is now. Work out the path Uranus should follow with that planet
pulling it. Compare with where Uranus was really seen, change the guess to make the fit better, and do it all again.
Every step was done by hand. Le Verrier sent his answer to Johann Galle at the Berlin Observatory, and on the night of
23 to 24 September 1846 Galle and Heinrich d'Arrest found the planet in less than an hour, less than 1° from the place
Le Verrier gave (history book, [section 17.4](../history/17-Herschel-and-the-Canals-of-Mars.md#rule); book 1,
[section 13.6](../night-sky/13-Finding-the-Planets.md#faint)).

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Uranus and Neptune from 1781 to 1846, drawn to scale from today's orbital elements. The Sun is in the middle. Uranus, on the inner circle, went more than three-quarters of the way round between its discovery by Herschel in 1781 and 1846. Neptune, on the outer circle, went less than half as far. Uranus caught up with Neptune and passed it in about 1822, when the two were about 11 astronomical units apart and Neptune's pull on Uranus was strongest. Neptune was found in 1846 at the place marked with a star.">
  <g font-size="8" fill="currentColor">
    <circle cx="118" cy="124" r="57.6" fill="none" stroke="#555" stroke-width="0.5" stroke-dasharray="2 2"/>
    <circle cx="118" cy="124" r="90.2" fill="none" stroke="#555" stroke-width="0.5" stroke-dasharray="2 2"/>
    <path d="M112.9,180.8 L115.1,180.8 L117.2,180.8 L119.4,180.7 L121.6,180.5 L123.8,180.2 L125.9,179.8 L128.1,179.4 L130.2,178.9 L132.4,178.3 L134.4,177.6 L136.5,176.8 L138.6,176.0 L140.6,175.0 L142.6,174.0 L144.5,172.9 L146.4,171.8 L148.3,170.5 L150.1,169.2 L151.8,167.8 L153.5,166.4 L155.2,164.9 L156.8,163.3 L158.3,161.7 L159.8,160.0 L161.2,158.2 L162.5,156.4 L163.7,154.5 L164.9,152.6 L166.0,150.6 L167.1,148.6 L168.0,146.6 L168.9,144.5 L169.7,142.4 L170.4,140.3 L171.0,138.1 L171.5,135.9 L172.0,133.7 L172.4,131.5 L172.6,129.2 L172.8,127.0 L172.9,124.7 L172.9,122.5 L172.8,120.2 L172.7,118.0 L172.4,115.7 L172.1,113.5 L171.7,111.3 L171.1,109.1 L170.5,107.0 L169.9,104.8 L169.1,102.7 L168.3,100.7 L167.3,98.6 L166.3,96.6 L165.3,94.7 L164.1,92.8 L162.9,90.9 L161.6,89.1 L160.3,87.3 L158.8,85.6 L157.4,84.0 L155.8,82.4 L154.2,80.9 L152.6,79.5 L150.9,78.1 L149.1,76.8 L147.3,75.5 L145.5,74.3 L143.6,73.2 L141.7,72.2 L139.7,71.2 L137.8,70.4 L135.7,69.5 L133.7,68.8 L131.7,68.2 L129.6,67.6 L127.5,67.1 L125.4,66.7 L123.3,66.4 L121.1,66.1 L119.0,65.9 L116.9,65.8 L114.7,65.8 L112.6,65.9 L110.5,66.0 L108.4,66.2 L106.3,66.5 L104.2,66.9 L102.2,67.3 L100.1,67.9 L98.1,68.4 L96.1,69.1 L94.2,69.8 L92.2,70.7 L90.3,71.5 L88.5,72.5 L86.6,73.5 L84.9,74.5 L83.1,75.7 L81.4,76.9 L79.8,78.1 L78.2,79.4 L76.6,80.8 L75.1,82.2 L73.6,83.7 L72.2,85.2 L70.9,86.8 L69.6,88.4 L68.4,90.0 L67.2,91.7 L66.1,93.5 L65.1,95.3 L64.1,97.1 L63.2,98.9 L62.4,100.8 L61.6,102.7 L60.9,104.6 L60.3,106.6 L59.7,108.6 L59.2,110.5 L58.8,112.6 L58.5,114.6 L58.2,116.6 L58.0,118.7 L57.9,120.7 L57.8,122.8 L57.8,124.8 L57.9,126.9 L58.1,128.9 L58.3,131.0" fill="none" stroke="#5aa0d8" stroke-width="2.2" stroke-opacity="0.8"/>
    <path d="M208.7,120.2 L208.7,118.5 L208.5,116.8 L208.4,115.1 L208.2,113.4 L208.0,111.7 L207.8,110.0 L207.5,108.4 L207.2,106.7 L206.9,105.0 L206.5,103.3 L206.1,101.7 L205.7,100.0 L205.2,98.4 L204.7,96.7 L204.2,95.1 L203.7,93.5 L203.1,91.9 L202.5,90.3 L201.8,88.7 L201.2,87.2 L200.5,85.6 L199.7,84.1 L199.0,82.5 L198.2,81.0 L197.4,79.5 L196.5,78.1 L195.6,76.6 L194.7,75.1 L193.8,73.7 L192.9,72.3 L191.9,70.9 L190.9,69.5 L189.8,68.2 L188.8,66.8 L187.7,65.5 L186.6,64.2 L185.5,62.9 L184.3,61.7 L183.1,60.5 L181.9,59.3 L180.7,58.1 L179.4,56.9 L178.2,55.8 L176.9,54.7 L175.6,53.6 L174.2,52.5 L172.9,51.5 L171.5,50.4 L170.1,49.5 L168.7,48.5 L167.3,47.6 L165.8,46.7 L164.4,45.8 L162.9,44.9 L161.4,44.1 L159.9,43.3 L158.4,42.5 L156.8,41.8 L155.3,41.1 L153.7,40.4 L152.1,39.8 L150.6,39.1 L149.0,38.5 L147.3,38.0 L145.7,37.5 L144.1,37.0 L142.4,36.5 L140.8,36.1 L139.1,35.7 L137.5,35.3 L135.8,34.9 L134.1,34.6 L132.4,34.4 L130.7,34.1 L129.0,33.9 L127.3,33.7 L125.6,33.6 L123.9,33.4 L122.2,33.4 L120.5,33.3 L118.8,33.3 L117.1,33.3 L115.4,33.3 L113.7,33.4 L112.0,33.5 L110.3,33.7 L108.6,33.8 L106.9,34.1 L105.2,34.3 L103.5,34.6 L101.8,34.9 L100.1,35.2 L98.4,35.6 L96.8,36.0 L95.1,36.4 L93.5,36.9 L91.8,37.3 L90.2,37.9 L88.6,38.4 L87.0,39.0 L85.4,39.6 L83.8,40.3 L82.2,41.0 L80.6,41.7 L79.1,42.4 L77.5,43.2 L76.0,44.0 L74.5,44.8 L73.0,45.6 L71.6,46.5 L70.1,47.4 L68.7,48.4 L67.2,49.3 L65.8,50.3 L64.5,51.3 L63.1,52.4 L61.7,53.5 L60.4,54.5 L59.1,55.7 L57.8,56.8 L56.6,58.0 L55.3,59.2 L54.1,60.4 L52.9,61.6 L51.8,62.9 L50.6,64.2 L49.5,65.5 L48.4,66.8 L47.3,68.2 L46.3,69.6" fill="none" stroke="#c1440e" stroke-width="2.2" stroke-opacity="0.8"/>
    <circle cx="118" cy="124" r="5" fill="#eea66f"/>
    <line x1="118" y1="124" x2="118.0" y2="29.5" stroke="currentColor" stroke-width="0.5" stroke-dasharray="3 2"/>
    <circle cx="112.9" cy="180.8" r="2.6" fill="currentColor"/>
    <circle cx="58.3" cy="131.0" r="2.6" fill="currentColor"/>
    <circle cx="208.7" cy="120.2" r="2.6" fill="currentColor"/>
    <circle cx="46.3" cy="69.6" r="2.6" fill="currentColor"/>
    <text x="117.9" y="183.8">1781</text>
    <text x="63.3" y="140.0">1846</text>
    <text x="213.7" y="123.2">1781</text>
    <text x="42.3" y="63.6" text-anchor="end">found 1846</text>
    <text x="118.0" y="25.5" text-anchor="middle">passing, about 1822</text>
    <text x="236" y="96" fill="#5aa0d8">Uranus, 84-year orbit</text>
    <text x="236" y="108" fill="#c1440e">Neptune, 165-year orbit</text>
    <text x="236" y="126">Thick lines: where</text>
    <text x="236" y="135">each went from 1781</text>
    <text x="236" y="144">to 1846</text>
    <text x="6" y="12">Uranus overtakes Neptune</text>
    <text x="6" y="226">To scale. Uranus caught up with Neptune and passed it in the 1820s, when Neptune's pull on it</text>
    <text x="6" y="235">was strongest. That pull first drew Uranus forwards, then held it back, and the tables of</text>
    <text x="6" y="244">1821 could not keep up. Positions from today's orbital elements.</text>
  </g>
</svg>
</div>

*Figure B. Uranus overtook Neptune in the 1820s.*

The timing helped. Uranus goes round in 84 years and Neptune in 165, so Uranus catches up with Neptune every 171 years
or so. It passed Neptune in about 1822, just after Bouvard's tables came out. Then the two were only 10.9 AU apart, and
Neptune pulled on Uranus about 1/6,100 as hard as the Sun. Before they met, Neptune was ahead and pulled Uranus
forwards; after, it was behind and held it back.

Seventeen days after Neptune was found, William Lassell found its largest moon, Triton. Neptune took until
11 July 2011 to go once round the Sun since it was found. In Chinese, Japanese, Korean and Vietnamese its name is the
"sea king star" (海王星). In Mongolian it is Dalain van, the ruler of the sea. In Nahuatl, the language of the Aztecs,
it is Tlāloccītlalli, after the rain god Tlāloc, and in 2009 the Academy of the Hebrew Language chose Rahab, a sea
monster from the Psalms.

??? note "Sources"
    - Bouvard's tables of 1821, the drift in longitude and distance, the three possible explanations, Adams's method
      of guessing, computing, comparing and adjusting, Le Verrier's results posted to Galle, the discovery on 23 to 24
      September 1846 within an hour and less than 1° from the prediction, with d'Arrest, and Triton found by Lassell
      17 days later: Wikipedia, [Discovery of Neptune](https://en.wikipedia.org/wiki/Discovery_of_Neptune) (weaker).
    - Neptune's first full orbit since discovery on 11 July 2011, and its names in Chinese, Vietnamese, Japanese,
      Korean, Mongolian, Nahuatl and Hebrew: Wikipedia, [Neptune](https://en.wikipedia.org/wiki/Neptune) (weaker).
    - The year of passing, the 171 years, the 10.9 AU and the 1/6,100: our arithmetic in section 10.8, from NASA JPL's
      approximate orbital elements (above). Which way the pull acted before and after is standard geometry.

## 10.4 Orbits that turn { #turning }

Only a pull that falls off exactly as the inverse square, from a single body, gives an ellipse that closes on itself
(chapter 5, [section 5.5](05-Newtons-Law-of-Gravity.md#kepler)). So when an orbit turns, something else is pulling.

**The Moon.** The Moon's orbit turns quickly, because the Sun pulls on it hard. Its nearest point to the Earth goes
round once in about 8.85 years. Hipparchus noticed this in the 2nd century BC, and the Antikythera mechanism, a geared
Greek model of the sky, allowed for it with 8.88 years (history book,
[section 7.7](../history/07-Greece-and-Alexandria.md#antikythera)).

**The Earth.** The Earth's perihelion goes round in about 112,000 years. It is one of the slow changes that steer the
ice ages.

**Mercury.** Mercury's perihelion moves too. The pulls of the other planets account for 532 arcseconds a century. In
1859 Le Verrier reported that this was not the whole story: about 43 arcseconds a century were left over, less than a
tenth of the total, but far more than the errors. Section 10.5 tells how he tried to explain it, and chapter 18 how
Einstein did.

??? note "Sources"
    - Bertrand's theorem and closed ellipses under an inverse-square pull, the Moon's apsidal period of about 8.85
      years noted by Hipparchus and allowed for in the Antikythera mechanism as 8.88 years, the Earth's of about
      112,000 years and its part in the Milankovitch cycles, and Mercury's 532 arcseconds a century from the planets
      and 43 from general relativity: Wikipedia, [Apsidal precession](https://en.wikipedia.org/wiki/Apsidal_precession)
      (weaker).
    - Le Verrier in 1859 being the first to report that Mercury's precession could not be fully explained: Wikipedia,
      [Urbain Le Verrier](https://en.wikipedia.org/wiki/Urbain_Le_Verrier) (weaker).
    - The Sun's pull as the main reason the Moon's orbit turns: standard. "Less than a tenth": our arithmetic.

## 10.5 Vulcan, Planet X and Planet Nine { #failures }

**Vulcan.** After Neptune, Le Verrier blamed Mercury's leftover turning on an unseen planet, or a swarm of small
bodies, inside Mercury's orbit. Edmond Lescarbault, a French doctor who watched the Sun from an observatory outside
his surgery, wrote to him that he had seen a small black dot cross the Sun on 26 March 1859. On 2 January 1860 Le
Verrier announced the new planet to the Académie des Sciences in Paris and named it Vulcan. During the total eclipse
of 29 July 1878, James Craig Watson of the Ann Arbor Observatory and Lewis Swift of Rochester both thought they saw
it. No one ever saw it again. In 1915 Einstein's general relativity explained the 43 arcseconds with no new planet at
all (chapter 18). The wobble was real, but this time the cause was not a planet.

**Planet X.** Percival Lowell thought Uranus and Neptune were still slightly off course and searched for a "Planet X"
beyond them. In 1930 Clyde Tombaugh found Pluto at Lowell's observatory (history book,
[section 17.8](../history/17-Herschel-and-the-Canals-of-Mars.md#illusion)), and for a while it seemed Lowell had been
right. But the discovery of Pluto's moon Charon in 1978 showed that Pluto is far too light to pull on Uranus. The
puzzle was solved by Voyager 2's flyby of Neptune in 1989. It showed that Neptune is 0.5% lighter than had been
thought, a difference about the mass of Mars. When Myles Standish redid the sums with the new mass, the wobbles of
Uranus disappeared. Planet X had been a small error in Neptune's mass.

**Planet Nine.** In 2014 Chad Trujillo and Scott Sheppard noticed that the orbits of Sedna, 2012 VP113 and some other
far-off icy bodies are oddly alike. In 2016 Konstantin Batygin and Michael Brown proposed that a planet several times
the Earth's mass, hundreds of AU from the Sun, has herded them into line. Nobody has seen Planet Nine, and it is still
only an idea.

??? note "Sources"
    - Le Verrier's unseen planet or asteroids inside Mercury's orbit, Lescarbault's observatory outside his surgery,
      his dot of 26 March 1859, the announcement of 2 January 1860 to the Académie des Sciences, Watson and Swift at
      the eclipse of 29 July 1878, and general relativity in 1915: Wikipedia,
      [Vulcan (hypothetical planet)](https://en.wikipedia.org/wiki/Vulcan_(hypothetical_planet)) (weaker).
    - Lowell's Planet X, Pluto in 1930, Charon in 1978, Voyager 2's 1989 measurement of Neptune's mass 0.5% lower,
      about the mass of Mars, and Standish's recalculation: Wikipedia,
      [Planets beyond Neptune](https://en.wikipedia.org/wiki/Planets_beyond_Neptune) (weaker).
    - Trujillo and Sheppard in 2014, Batygin and Brown in 2016, the clustering of orbits, a mass of five to ten Earths,
      and Planet Nine being hypothetical: Wikipedia, [Planet Nine](https://en.wikipedia.org/wiki/Planet_Nine) (weaker).

## 10.6 Will the solar system hold together? { #stable }

**Laplace.** In the 18th century Jupiter's orbit seemed to be shrinking and Saturn's growing. If that went on, the
solar system would come apart. Leonhard Euler in 1748 and Joseph-Louis Lagrange in 1763 tried to explain it and failed;
they had left out terms that looked too small to matter. Pierre-Simon Laplace kept them, and saw that small terms can
add up over a long time. He showed the drift is a swing, back and forth over nearly 900 years, because five orbits of
Jupiter take almost the same time as two of Saturn (chapter 11). He went on to argue that the solar system is stable.

**Chaos.** Laplace's answer did not settle it. Gauss, Poincaré, Kolmogorov, Arnold, Moser and others kept working on
the question, and with computers it changed. In 1989 Jacques Laskar of the Bureau des Longitudes in Paris followed the
planets for 200 million years and found that the inner planets' orbits are **chaotic**: an error of just 15 m in the
Earth's position today makes it impossible to say where the Earth will be in its orbit a little over 100 million years
from now.

In 2008 Laskar and Mickaël Gastineau ran 2,501 futures, each starting with Mercury moved by about 1 m. In 20 of them
Mercury's orbit was stretched so far that it often hit Venus or fell into the Sun, and in one Mercury's pulls sent Mars
heading towards the Earth. In 2020 Garett Brown and Hanno Rein at the University of Toronto followed the planets for 5
billion years: an error of 0.38 mm in Mercury's position is enough to make its orbit's shape unknowable after about
200 million years.

So the answer is yes, for now. No collisions or escapes are likely in the next few billion years, but the exact
details cannot be forecast more than a few tens of millions of years ahead.

??? note "Sources"
    - Jupiter's orbit seeming to shrink and Saturn's to grow, Euler in 1748 and Lagrange in 1763, Laplace keeping the
      small terms that build up over time, the period of nearly 900 years from $2n_J - 5n_S$, and his stability work:
      Wikipedia, [Pierre-Simon Laplace](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace) (weaker).
    - The names who searched for proofs of stability, Laskar in 1989 with the 15 m error, Laskar and Gastineau's 2,501
      runs with Mercury moved by about 1 m and 20 dangerous outcomes including Mars heading towards the Earth, Brown and
      Rein in 2020 with the 0.38 mm error, and the solar system being stable for the next few billion years while not
      predictable beyond a few tens of millions: Wikipedia,
      [Stability of the Solar System](https://en.wikipedia.org/wiki/Stability_of_the_Solar_System) (weaker).

## 10.7 Wobbles at Mars { #mars }

**Mars's turning orbit.** Mars's perihelion moves forwards by about 0.44° a century, so it goes once round in about
81,000 years, faster than the Earth's. Jupiter is the main reason: at its closest it pulls on Mars about 1/6,100 as
hard as the Sun does, three times its share at the Earth. Mars's orbit is also slowly getting more stretched, at
present by 0.00008 a century. Over millions of years these changes, together with changes in Mars's tilt, alter how
much sunlight each pole gets, and chapter 20 follows what that does to Mars's climate.

**Pinning down the planets.** Mars is the planet nearest to the asteroid belt, so it feels the asteroids most. Since
the JPL ephemeris called DE421, the tables of where the planets are include the pulls of 343 asteroids, about 90% of
the mass of the main belt. The tables are fitted to radio ranges to spacecraft at the planets, and the newer ones use
ranging and tracking of Mars spacecraft. The inner planets are placed to about 0.001 arcseconds, about 1 km at the
distance of Mars.

**Mars's own bulge.** A spinning planet bulges at its equator, and the extra mass there pulls a tilted orbit round it
so that the orbit slowly turns. Mars's bulge is nearly twice as strong as the Earth's. NASA's Mars Reconnaissance
Orbiter uses this to cross the equator at about 3 pm local time every day, so that shadows always fall the same way
(physics lesson [Orbits that drift](https://physics.akadian.ca/topics/gravity/level-8/04-orbits-that-drift.html);
chapter 19).

**A crater for Le Verrier.** Craters on Mars and on the Moon, a ring of Neptune and the asteroid 1997 Leverrier are
named after him.

??? note "Sources"
    - Mars's perihelion rate of 0.44441088° a century and its eccentricity rate of +0.00007882 a century, a best fit
      for 1800 to 2050: NASA JPL, Approximate positions of the planets (above).
    - DE421 including 343 asteroids, about 90% of the main belt's mass; the fits to radio ranges of spacecraft, with
      added ranging and VLBI of Mars spacecraft; and DE405's accuracy of about 0.001 arcseconds, about 1 km at Mars's
      distance, for the inner planets: Wikipedia,
      [Jet Propulsion Laboratory Development Ephemeris](https://en.wikipedia.org/wiki/Jet_Propulsion_Laboratory_Development_Ephemeris)
      (weaker).
    - Mars's $J_2$ of $1.96 \times 10^{-3}$ against the Earth's $1.08 \times 10^{-3}$, and MRO's 3 pm orbit: physics
      lesson, Orbits that drift (above).
    - The craters, ring and asteroid named after Le Verrier: Wikipedia, Urbain Le Verrier (above).
    - Jupiter's pull and the 81,000 years: our arithmetic in section 10.8. Mars being nearest the belt, and sunlight at
      the poles depending on the orbit and the tilt: standard.

## 10.8 Working it out { #working }

**Jupiter on the Earth.** At its closest Jupiter is $5.203 - 1.000 = 4.203$ AU away. The Sun is 1,047.6 times as
heavy, so Jupiter's pull compared with the Sun's is $1 / (1{,}047.6 \times 4.203^2) = 1/18{,}500$.

**Jupiter on Mars.** At its closest it is $5.203 - 1.524 = 3.679$ AU from Mars, which is 1.524 AU from the Sun. The
ratio is $(1.524 / 3.679)^2 / 1{,}047.6 = 1/6{,}100$, three times the ratio at the Earth.

**Neptune on Uranus.** Uranus catches up once every $1 / (1/84.0 - 1/164.8) = 171$ years. Working the orbits forward
from NASA JPL's elements, it passed Neptune late in 1821, when Uranus was 19.38 AU from the Sun and Neptune 30.24 AU,
10.86 AU apart. The Sun is 19,412 times as heavy as Neptune, so the ratio is
$(19.38 / 10.86)^2 / 19{,}412 = 1/6{,}100$, by chance the same as Jupiter's on Mars.

**Mars's perihelion.** At 0.4444° a century it goes round $360 / 0.4444 = 810$ centuries, about 81,000 years, and
moves 1° every 225 years.

**Halley's comet.** $618 / (76 \times 365.25) = 0.022$, about 2% of a period.

| | Mars | Earth |
| --- | --- | --- |
| Jupiter's pull at its closest, against the Sun's | 1 in 6,100 | 1 in 18,500 |
| Perihelion moves, 1800 to 2050 | 0.444° a century | 0.323° a century |
| Once round | about 81,000 years | about 111,000 years |
| Eccentricity in 2000 | 0.0934 | 0.0167 |
| Change in eccentricity a century | +0.000079 | −0.000044 |
| Strength of the equatorial bulge, $J_2$ | $1.96 \times 10^{-3}$ | $1.08 \times 10^{-3}$ |

??? note "Sources"
    - Semi-major axes, eccentricities and their rates, and perihelion rates: NASA JPL, Approximate positions of the
      planets (above). $GM$ values for the Sun, Jupiter and Neptune: chapter 6 and NASA's fact sheets. $J_2$: physics
      lesson, Orbits that drift (above). The arithmetic is ours. The JPL rates are a best fit for 1800 to 2050, and the
      111,000 years from them is close to the 112,000 years in section 10.4.

## 10.9 How a small push grows { #derive }

Take a planet on a nearly round orbit of radius $a$, moving at speed $v$, with $v^2 = GM/a$. Give it a small push
$\Delta v$ along its motion. The vis-viva equation (chapter 7,
[section 7.6](07-Speed-Energy-and-Escape.md#visviva)) is

$$v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right).$$

The push happens at one place, so $r$ stays the same, and only $v$ and $a$ change:

$$2v\,\Delta v = \frac{GM}{a^2}\,\Delta a \quad\Rightarrow\quad \frac{\Delta a}{a} = \frac{2a v\,\Delta v}{GM}
= \frac{2\,\Delta v}{v}.$$

Kepler's third law, $P \propto a^{3/2}$, then gives

$$\frac{\Delta P}{P} = \frac{3}{2}\,\frac{\Delta a}{a} = \frac{3\,\Delta v}{v}.$$

A push forwards makes the orbit bigger and the year longer, so the planet falls behind where it would have been
(chapter 7, [section 7.2](07-Speed-Energy-and-Escape.md#paradox)). Each orbit it loses a fraction $3\Delta v/v$ of a
whole circuit, and the losses pile up. After $N$ orbits it is behind by about

$$N \times 2\pi a \times \frac{3\,\Delta v}{v}.$$

**For Mars**, with $v = 24.08$ km/s and a push of 1 cm/s, $3\Delta v / v = 1.25 \times 10^{-6}$. Each orbit Mars falls
$2\pi \times 227.9$ million km $\times 1.25 \times 10^{-6} = 1{,}780$ km further behind, and after 10 orbits,
18.8 years, it is 17,800 km out. This is why a pull too small to notice in one year shows up after decades, and why
the drift of Uranus grew year by year until it could not be ignored.

??? note "Sources"
    - Vis-viva and the third law: chapters 3 and 7. The derivation is standard; the Mars numbers are our arithmetic,
      with Mars's mean speed of 24.08 km/s from NASA,
      [Mars fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).

## Check yourself { #check }

**1.** (beginner) Why does no planet follow a perfect, fixed ellipse?

??? note "Answer"
    Kepler's ellipses are exact only for two bodies. Every planet is also pulled by all the others, mostly by Jupiter,
    so its ellipse slowly turns, stretches and tilts.

**2.** (beginner) Why did Halley's comet come back 618 days later than it would have otherwise?

??? note "Answer"
    The pulls of Jupiter and Saturn held it back. Clairaut, Lalande and Lepaute worked out the delay before it
    happened, to within a month.

**3.** (beginner) How was Neptune found?

??? note "Answer"
    Uranus drifted away from its tables. Le Verrier, and Adams separately, worked out what unseen planet could be
    pulling it. Galle and d'Arrest looked where Le Verrier said, on 23 to 24 September 1846, and found Neptune less
    than 1° away.

**4.** (intermediate) What happened to Planet X?

??? note "Answer"
    It was never there. The wobbles of Uranus that seemed to need it came from using a mass for Neptune that was 0.5%
    too large. Voyager 2 measured the right mass in 1989, and with it the wobbles vanished.

**5.** (intermediate) Mercury's perihelion turns about 575 arcseconds a century, and the other planets account for
532. How much is left over, and what explains it?

??? note "Answer"
    About 43 arcseconds a century. Le Verrier blamed a planet, Vulcan, but none exists. Einstein's general relativity
    explained it in 1915.

**6.** (intermediate) Mars's perihelion moves 0.444° a century. How long does it take to move a quarter of the way
round?

??? note "Answer"
    $90 / 0.444 = 203$ centuries, about 20,000 years.

**7.** (advanced) Show that Jupiter at its closest pulls on Mars, compared with the Sun's pull, about 3 times as hard
as it pulls on the Earth. Use 5.203, 1.524 and 1.000 AU.

??? note "Answer"
    The two ratios share the factor $1/1{,}047.6$, so compare $(1.524 / 3.679)^2 = 0.1716$ for Mars with
    $(1 / 4.203)^2 = 0.0566$ for the Earth. $0.1716 / 0.0566 = 3.03$.

**8.** (expert) A spacecraft going round the Sun with the Earth, at 29.78 km/s and 149.6 million km from the Sun, gets
a push forwards of 1 mm/s. About how far behind will it be after 1 year and after 10?

??? note "Answer"
    $3\Delta v / v = 3 \times 0.001 / 29{,}780 = 1.01 \times 10^{-7}$. Each orbit it falls behind by
    $2\pi \times 149.6$ million km $\times 1.01 \times 10^{-7} = 95$ km, so about 95 km after one year and 950 km after
    ten. A push far too small to feel moves it nearly 1,000 km.

## Summary

- Every planet is pulled by the others, so its ellipse slowly turns, stretches and tilts; the biggest pull is
  Jupiter's.
- Jupiter and Saturn delayed Halley's comet by 618 days in 1759, as Clairaut, Lalande and Lepaute predicted.
- Le Verrier and Adams worked backwards from the drift of Uranus; Galle and d'Arrest found Neptune on 23 to
  24 September 1846, within 1° of Le Verrier's place.
- Orbits turn: the Moon's in 8.85 years, the Earth's in about 112,000 years, Mars's in about 81,000. Mercury's has
  43 arcseconds a century that no planet explains.
- Vulcan and Planet X were false trails; Planet Nine is still only an idea.
- Laplace showed Jupiter and Saturn swing back and forth over about 900 years. Computers show the planets are chaotic
  but likely to stay safe for billions of years.
- At Mars, Jupiter's pull turns the orbit, asteroids nudge it, and Mars's bulge turns the orbits of spacecraft.
- A small push grows: a forward push of $\Delta v$ makes the year longer by $3\Delta v / v$, and the lag adds up orbit
  after orbit.

**Next:** chapter 11, Resonances, where orbits that keep in step, such as Jupiter and Saturn's 5 to 2, give each other
the same nudge again and again.

## Further reading

- Tom Standage, *The Neptune File: A Story of Astronomical Rivalry and the Pioneers of Planet Hunting*, Walker &
  Company, 2000.
