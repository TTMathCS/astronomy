# 13. Rockets and getting to orbit

*Everything in the last twelve chapters moves under gravity alone. To put something into orbit ourselves, we need a
machine that can change its own speed in empty space: a rocket. This chapter shows how a rocket works, where rockets
came from, why the rocket equation makes reaching orbit so hard, why rockets come in stages and head east, and why
leaving Mars is so much easier than leaving the Earth.*

!!! abstract "In this chapter"
    **You will learn:**

    - how a rocket pushes itself along with nothing to push against
    - how rockets grew from fire arrows in China, Korea and India into the first spacecraft
    - the rocket equation, and why most of a rocket has to be propellant
    - what exhaust speed is, and why ion engines are so frugal but so weak
    - why rockets drop their empty stages on the way up
    - where the 9.4 km/s to reach orbit goes, and why launch sites like to be near the equator
    - why one stage is enough to get off Mars, and how its fuel might be made there
    - how to derive the rocket equation from the conservation of momentum

    **You need:** chapters 1 and 7.

    **Levels:** 13.1 to 13.3 are beginner; 13.4 to 13.7 are intermediate; 13.8 is advanced; 13.9 is expert.

## 13.1 Pushing on nothing { #push }

Stand on a skateboard and throw a heavy ball forwards: you roll backwards. A rocket does the same thing over and over,
very fast. It throws hot gas out of the back, and the gas pushes the rocket forwards. This is Newton's third law: the
push on the gas and the push on the rocket are equal and opposite. Put another way, the momentum the gas carries
backwards is matched by momentum the rocket gains forwards.

Nothing in this needs air. A rocket pushes on its own exhaust, not on the air behind it, and it works best of all in
a vacuum, where there is no air to get in the way (physics lesson
[No air needed](https://physics.akadian.ca/topics/rockets/level-2/03-no-air-needed.html)).

Not everyone believed it. In January 1920, the day after a front-page story reported that Robert Goddard believed a
rocket could reach the Moon, an unsigned editorial in *The New York Times* mocked him: once out of the air, it said,
the rocket's charges could neither speed it up nor keep it going, and Goddard seemed to lack "the knowledge ladled out
daily in high schools". On **17 July 1969**, the day after Apollo 11 was launched to the Moon, the paper printed "A
Correction": "it is now definitely established that a rocket can function in a vacuum as well as in an atmosphere. The
Times regrets the error."

??? note "Sources"
    - The *New York Times* front page of 12 January 1920, the editorial "A Severe Strain on Credulity" of 13 January
      1920 and its words, and "A Correction" of 17 July 1969: Wikipedia,
      [Robert H. Goddard](https://en.wikipedia.org/wiki/Robert_H._Goddard) (weaker).
    - Newton's third law and momentum: standard, and the physics lesson above.

## 13.2 From fire arrows to the first satellite { #history }

**China.** The first rockets were arrows pushed along by burning gunpowder. The official *History of Song* credits
their invention to Yue Yifang and Feng Jisheng in 969, though the historian Joseph Needham argued that true rockets
came only in the 12th century. By 1232 there were reports of fire arrows used in war. In the mid-14th century, the
military book *Huolongjing* by Jiao Yu described the oldest known rocket with two stages, the "fire-dragon issuing
from the water", used by the Chinese navy.

**Across Asia and beyond.** Rockets probably spread across Eurasia with the Mongol invasions of the 13th century.
Between 1270 and 1280 Hasan al-Rammah wrote a book of 107 gunpowder recipes, 22 of them for rockets. In Korea, the
Joseon kingdom had a cart that fired many rockets at once, the *Munjong Hwacha*, by 1451. In Europe, Conrad Haas
experimented with rockets of several stages in 1551, in Hermannstadt in Transylvania.

**India.** In the Kingdom of Mysore, Hyder Ali and his son Tipu Sultan used the first successful rockets with iron
cases against the British East India Company in the 1780s and 1790s. The iron let them hold more powder, so they flew
farther, up to 2 km. Meeting them in battle led the British to develop the Congreve rocket of 1805.

**The space age.** In 1903 Konstantin Tsiolkovsky, a mathematics teacher living in Kaluga, about 150 km from Moscow,
published *Exploration of Outer Space by Means of Rocket Devices*, the first serious scientific work on spaceflight.
It contained the rocket equation (section 13.3). Hermann Oberth published *The Rocket into Planetary Space* in 1923. On
**16 March 1926**, at Auburn, Massachusetts, Goddard launched the first rocket to burn liquid fuel, petrol and liquid
oxygen. It rose 12.5 m and landed 56 m away in a cabbage field after 2.5 seconds. Within twenty years a German V-2
had reached space (chapter 1, [section 1.5](01-Falling-Round-the-Earth.md#height)), and in 1957 Sergei Korolev's R-7
put Sputnik 1 into orbit from Baikonur (chapter 1, [section 1.7](01-Falling-Round-the-Earth.md#club)).

??? note "Sources"
    - Fire arrows, the *History of Song*'s credit to Yue Yifang and Feng Jisheng in 969, and Needham's doubt: Wikipedia,
      [Fire arrow](https://en.wikipedia.org/wiki/Fire_arrow) (weaker).
    - Reports from 1232, the *Huolongjing* of Jiao Yu in the mid-14th century and its "fire-dragon issuing from the
      water", the spread with the Mongol invasions, Hasan al-Rammah's 107 recipes (22 for rockets) of 1270 to 1280,
      the Munjong Hwacha by 1451, Mysore and the Congreve rocket, Tsiolkovsky in 1903 as a mathematics teacher, Oberth
      in 1923, Goddard on 16 March 1926 at Auburn, and the R-7 launching Sputnik 1 under Korolev: Wikipedia,
      [History of rockets](https://en.wikipedia.org/wiki/History_of_rockets) (weaker).
    - The fire-dragon as the oldest known multistage rocket, and Conrad Haas's experiments of 1551 in Hermannstadt:
      Wikipedia, [Multistage rocket](https://en.wikipedia.org/wiki/Multistage_rocket) (weaker).
    - Iron-cased rockets under Hyder Ali and Tipu Sultan in the 1780s and 1790s, up to 2 km, and the Congreve rocket
      of 1805: Wikipedia, [Mysorean rockets](https://en.wikipedia.org/wiki/Mysorean_rockets) (weaker).
    - Tsiolkovsky's work of May 1903 and his home near Kaluga, about 150 km from Moscow: Wikipedia,
      [Konstantin Tsiolkovsky](https://en.wikipedia.org/wiki/Konstantin_Tsiolkovsky) (weaker).
    - Goddard's rocket of petrol and liquid oxygen, 12.5 m high, 56 m away, 2.5 seconds, a cabbage field: Wikipedia,
      Robert H. Goddard (above).
    - Sputnik 1 launched from Baikonur: Wikipedia,
      [Baikonur Cosmodrome](https://en.wikipedia.org/wiki/Baikonur_Cosmodrome) (weaker).

## 13.3 The rocket equation { #equation }

A rocket's gain in speed, $\Delta v$, depends on just two things: how fast its exhaust leaves, $v_e$, and how much
lighter it is at the end of the burn than at the start. If it starts with mass $m_0$ and ends with mass $m_1$,

$$\Delta v = v_e \ln\frac{m_0}{m_1}.$$

The ratio $m_0/m_1$ is the **mass ratio**, and $\ln$ is the natural logarithm. This is the **rocket equation**.
Tsiolkovsky published it in 1903; William Moore had outlined it as early as 1810, and Goddard and Oberth later found
it again for themselves. Section 13.9 shows where it comes from.

The logarithm is the trouble. Doubling the mass ratio adds only $0.69\,v_e$ to the speed. Turn the equation round and
the mass ratio needed grows very fast with the speed wanted:

$$\frac{m_0}{m_1} = e^{\Delta v / v_e}.$$

Reaching orbit from the Earth's surface takes about 9.4 km/s (section 13.6). With kerosene engines, whose exhaust
averages about 3.3 km/s on the climb, the mass ratio must be $e^{9.4/3.3} = 17$: 94% of the rocket at lift-off must
be propellant, leaving 6% for the tanks, the engines and whatever it is carrying. This is sometimes called **the
tyranny of the rocket equation**. Figure A shows it.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="How much of a rocket must be propellant, from the rocket equation, against the speed it has to gain, from 0 to 12 km/s. Three curves are drawn for exhaust speeds of 3.3 km/s, about what kerosene engines average on the climb, 4.4 km/s for hydrogen engines, and 26 km/s for an ion engine like Dawn's. A line at 4.1 km/s marks the climb from the surface of Mars to orbit: 71% propellant with kerosene, 61% with hydrogen. A line at 9.4 km/s marks the climb from the Earth's surface to orbit: 94% propellant with kerosene, 88% with hydrogen, leaving very little for tanks, engines and payload. The ion engine needs only 30% even for 9.4 km/s, but its push is far too weak to lift off.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">How much of the rocket must be propellant?</text>
    <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="0.6"/>
    <line x1="40" y1="190" x2="40" y2="30" stroke="currentColor" stroke-width="0.6"/>
    <line x1="37" y1="190.0" x2="40" y2="190.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="35" y="193.0" text-anchor="end">0%</text>
    <line x1="37" y1="150.0" x2="40" y2="150.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="35" y="153.0" text-anchor="end">25%</text>
    <line x1="37" y1="110.0" x2="40" y2="110.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="35" y="113.0" text-anchor="end">50%</text>
    <line x1="37" y1="70.0" x2="40" y2="70.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="35" y="73.0" text-anchor="end">75%</text>
    <line x1="37" y1="30.0" x2="40" y2="30.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="35" y="33.0" text-anchor="end">100%</text>
    <line x1="40.0" y1="190" x2="40.0" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="40.0" y="201" text-anchor="middle">0</text>
    <line x1="83.3" y1="190" x2="83.3" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="83.3" y="201" text-anchor="middle">2</text>
    <line x1="126.7" y1="190" x2="126.7" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="126.7" y="201" text-anchor="middle">4</text>
    <line x1="170.0" y1="190" x2="170.0" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="170.0" y="201" text-anchor="middle">6</text>
    <line x1="213.3" y1="190" x2="213.3" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="213.3" y="201" text-anchor="middle">8</text>
    <line x1="256.7" y1="190" x2="256.7" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="256.7" y="201" text-anchor="middle">10</text>
    <line x1="300.0" y1="190" x2="300.0" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="300.0" y="201" text-anchor="middle">12</text>
    <text x="300" y="210" text-anchor="end">speed to gain, km/s</text>
    <line x1="128.8" y1="190" x2="128.8" y2="26" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2 2"/>
    <text x="128.8" y="23" text-anchor="middle">Mars to orbit</text>
    <line x1="243.7" y1="190" x2="243.7" y2="26" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2 2"/>
    <text x="243.7" y="23" text-anchor="middle">Earth to orbit</text>
    <path d="M40.0,190.0 L42.2,185.2 L44.3,180.6 L46.5,176.1 L48.7,171.7 L50.8,167.5 L53.0,163.4 L55.2,159.4 L57.3,155.6 L59.5,151.8 L61.7,148.2 L63.8,144.6 L66.0,141.2 L68.2,137.9 L70.3,134.7 L72.5,131.6 L74.7,128.5 L76.8,125.6 L79.0,122.7 L81.2,120.0 L83.3,117.3 L85.5,114.7 L87.7,112.1 L89.8,109.7 L92.0,107.3 L94.2,105.0 L96.3,102.8 L98.5,100.6 L100.7,98.5 L102.8,96.4 L105.0,94.5 L107.2,92.5 L109.3,90.7 L111.5,88.9 L113.7,87.1 L115.8,85.4 L118.0,83.7 L120.2,82.1 L122.3,80.6 L124.5,79.1 L126.7,77.6 L128.8,76.2 L131.0,74.8 L133.2,73.5 L135.3,72.2 L137.5,70.9 L139.7,69.7 L141.8,68.5 L144.0,67.4 L146.2,66.2 L148.3,65.2 L150.5,64.1 L152.7,63.1 L154.8,62.1 L157.0,61.1 L159.2,60.2 L161.3,59.3 L163.5,58.4 L165.7,57.6 L167.8,56.8 L170.0,56.0 L172.2,55.2 L174.3,54.4 L176.5,53.7 L178.7,53.0 L180.8,52.3 L183.0,51.7 L185.2,51.0 L187.3,50.4 L189.5,49.8 L191.7,49.2 L193.8,48.6 L196.0,48.1 L198.2,47.5 L200.3,47.0 L202.5,46.5 L204.7,46.0 L206.8,45.5 L209.0,45.1 L211.2,44.6 L213.3,44.2 L215.5,43.7 L217.7,43.3 L219.8,42.9 L222.0,42.5 L224.2,42.2 L226.3,41.8 L228.5,41.5 L230.7,41.1 L232.8,40.8 L235.0,40.5 L237.2,40.2 L239.3,39.8 L241.5,39.6 L243.7,39.3 L245.8,39.0 L248.0,38.7 L250.2,38.5 L252.3,38.2 L254.5,38.0 L256.7,37.7 L258.8,37.5 L261.0,37.3 L263.2,37.1 L265.3,36.8 L267.5,36.6 L269.7,36.4 L271.8,36.3 L274.0,36.1 L276.2,35.9 L278.3,35.7 L280.5,35.5 L282.7,35.4 L284.8,35.2 L287.0,35.1 L289.2,34.9 L291.3,34.8 L293.5,34.6 L295.7,34.5 L297.8,34.3 L300.0,34.2" fill="none" stroke="#c1440e" stroke-width="1.2"/>
    <circle cx="128.8" cy="76.2" r="1.8" fill="#c1440e"/>
    <circle cx="243.7" cy="39.3" r="1.8" fill="#c1440e"/>
    <path d="M40.0,190.0 L42.2,186.4 L44.3,182.9 L46.5,179.5 L48.7,176.1 L50.8,172.8 L53.0,169.6 L55.2,166.5 L57.3,163.4 L59.5,160.4 L61.7,157.5 L63.8,154.6 L66.0,151.8 L68.2,149.1 L70.3,146.4 L72.5,143.8 L74.7,141.2 L76.8,138.7 L79.0,136.3 L81.2,133.9 L83.3,131.6 L85.5,129.3 L87.7,127.0 L89.8,124.9 L92.0,122.7 L94.2,120.6 L96.3,118.6 L98.5,116.6 L100.7,114.7 L102.8,112.8 L105.0,110.9 L107.2,109.1 L109.3,107.3 L111.5,105.6 L113.7,103.9 L115.8,102.2 L118.0,100.6 L120.2,99.0 L122.3,97.5 L124.5,95.9 L126.7,94.5 L128.8,93.0 L131.0,91.6 L133.2,90.2 L135.3,88.9 L137.5,87.5 L139.7,86.2 L141.8,85.0 L144.0,83.7 L146.2,82.5 L148.3,81.4 L150.5,80.2 L152.7,79.1 L154.8,78.0 L157.0,76.9 L159.2,75.8 L161.3,74.8 L163.5,73.8 L165.7,72.8 L167.8,71.9 L170.0,70.9 L172.2,70.0 L174.3,69.1 L176.5,68.2 L178.7,67.4 L180.8,66.5 L183.0,65.7 L185.2,64.9 L187.3,64.1 L189.5,63.3 L191.7,62.6 L193.8,61.9 L196.0,61.1 L198.2,60.4 L200.3,59.8 L202.5,59.1 L204.7,58.4 L206.8,57.8 L209.0,57.2 L211.2,56.6 L213.3,56.0 L215.5,55.4 L217.7,54.8 L219.8,54.3 L222.0,53.7 L224.2,53.2 L226.3,52.7 L228.5,52.2 L230.7,51.7 L232.8,51.2 L235.0,50.7 L237.2,50.2 L239.3,49.8 L241.5,49.3 L243.7,48.9 L245.8,48.5 L248.0,48.1 L250.2,47.6 L252.3,47.3 L254.5,46.9 L256.7,46.5 L258.8,46.1 L261.0,45.8 L263.2,45.4 L265.3,45.1 L267.5,44.7 L269.7,44.4 L271.8,44.1 L274.0,43.7 L276.2,43.4 L278.3,43.1 L280.5,42.8 L282.7,42.5 L284.8,42.3 L287.0,42.0 L289.2,41.7 L291.3,41.5 L293.5,41.2 L295.7,41.0 L297.8,40.7 L300.0,40.5" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
    <circle cx="128.8" cy="93.0" r="1.8" fill="#5aa0d8"/>
    <circle cx="243.7" cy="48.9" r="1.8" fill="#5aa0d8"/>
    <path d="M40.0,190.0 L42.2,189.4 L44.3,188.8 L46.5,188.2 L48.7,187.6 L50.8,187.0 L53.0,186.3 L55.2,185.7 L57.3,185.2 L59.5,184.6 L61.7,184.0 L63.8,183.4 L66.0,182.8 L68.2,182.2 L70.3,181.6 L72.5,181.0 L74.7,180.5 L76.8,179.9 L79.0,179.3 L81.2,178.7 L83.3,178.2 L85.5,177.6 L87.7,177.0 L89.8,176.5 L92.0,175.9 L94.2,175.3 L96.3,174.8 L98.5,174.2 L100.7,173.7 L102.8,173.1 L105.0,172.6 L107.2,172.0 L109.3,171.5 L111.5,170.9 L113.7,170.4 L115.8,169.8 L118.0,169.3 L120.2,168.8 L122.3,168.2 L124.5,167.7 L126.7,167.2 L128.8,166.7 L131.0,166.1 L133.2,165.6 L135.3,165.1 L137.5,164.6 L139.7,164.1 L141.8,163.5 L144.0,163.0 L146.2,162.5 L148.3,162.0 L150.5,161.5 L152.7,161.0 L154.8,160.5 L157.0,160.0 L159.2,159.5 L161.3,159.0 L163.5,158.5 L165.7,158.0 L167.8,157.5 L170.0,157.0 L172.2,156.5 L174.3,156.1 L176.5,155.6 L178.7,155.1 L180.8,154.6 L183.0,154.1 L185.2,153.7 L187.3,153.2 L189.5,152.7 L191.7,152.2 L193.8,151.8 L196.0,151.3 L198.2,150.8 L200.3,150.4 L202.5,149.9 L204.7,149.4 L206.8,149.0 L209.0,148.5 L211.2,148.1 L213.3,147.6 L215.5,147.2 L217.7,146.7 L219.8,146.3 L222.0,145.8 L224.2,145.4 L226.3,144.9 L228.5,144.5 L230.7,144.1 L232.8,143.6 L235.0,143.2 L237.2,142.8 L239.3,142.3 L241.5,141.9 L243.7,141.5 L245.8,141.0 L248.0,140.6 L250.2,140.2 L252.3,139.8 L254.5,139.3 L256.7,138.9 L258.8,138.5 L261.0,138.1 L263.2,137.7 L265.3,137.3 L267.5,136.8 L269.7,136.4 L271.8,136.0 L274.0,135.6 L276.2,135.2 L278.3,134.8 L280.5,134.4 L282.7,134.0 L284.8,133.6 L287.0,133.2 L289.2,132.8 L291.3,132.4 L293.5,132.0 L295.7,131.6 L297.8,131.2 L300.0,130.9" fill="none" stroke="#555" stroke-width="1.2"/>
    <circle cx="128.8" cy="166.7" r="1.8" fill="#555"/>
    <circle cx="243.7" cy="141.5" r="1.8" fill="#555"/>
    <text x="247.7" y="34.3" fill="#c1440e">94%</text>
    <text x="247.7" y="56.9" fill="#5aa0d8">88%</text>
    <text x="124.8" y="73.2" text-anchor="end" fill="#c1440e">71%</text>
    <text x="132.8" y="102.0" fill="#5aa0d8">61%</text>
    <text x="239.7" y="136.5" text-anchor="end" fill="#555">30%</text>
    <line x1="252" y1="79" x2="264" y2="79" stroke="#c1440e" stroke-width="1.5"/>
    <text x="268" y="82">kerosene 3.3</text>
    <line x1="252" y1="91" x2="264" y2="91" stroke="#5aa0d8" stroke-width="1.5"/>
    <text x="268" y="94">hydrogen 4.4</text>
    <line x1="252" y1="103" x2="264" y2="103" stroke="#555" stroke-width="1.5"/>
    <text x="268" y="106">ion 26</text>
    <text x="252" y="70">exhaust speed, km/s</text>
    <text x="6" y="226">Each curve is the rocket equation for one exhaust speed. Leaving the Earth with kerosene</text>
    <text x="6" y="235">engines, 94% of the rocket must be propellant, which is why Earth rockets come in stages.</text>
    <text x="6" y="244">Leaving Mars needs much less. An ion engine sips propellant but cannot lift itself off the ground.</text>
  </g>
</svg>
</div>

The physics lesson
[Tsiolkovsky's rocket equation](https://physics.akadian.ca/topics/rockets/level-6/05-the-rocket-equation.html) works
through more cases.

??? note "Sources"
    - The equation, Tsiolkovsky in 1903, William Moore in 1810 and 1813, Goddard and Oberth finding it independently,
      and "the tyranny of the rocket equation": Wikipedia,
      [Tsiolkovsky rocket equation](https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation) (weaker).
    - The 3.3 km/s average for kerosene on the climb: this site's physics lesson
      [Staging, worked out](https://physics.akadian.ca/topics/rockets/level-6/06-staging.html). The 9.4 km/s: section
      13.6. The percentages are our arithmetic, section 13.8.

## 13.4 Exhaust speed { #exhaust }

Since $\Delta v$ is proportional to $v_e$, a faster exhaust is worth a great deal. Engineers often give exhaust speed
as **specific impulse**, in seconds: the exhaust speed divided by $g_0 = 9.81$ m/s². The physics lesson
[Specific impulse](https://physics.akadian.ca/topics/rockets/level-6/03-specific-impulse.html) explains why.

- **Chemical rockets** burn a fuel with an oxidiser, and the exhaust speed is limited by how much energy the reaction
  gives. A rocket at sea level manages a specific impulse of 200 to 400 s. The hydrogen and oxygen engines of the
  Space Shuttle, the RS-25, reach 453 s in a vacuum, an exhaust speed of 4.44 km/s. The best ever tested, 542 s, used
  lithium, fluorine and hydrogen together, too dangerous and awkward to be practical.
- **Ion engines** use electricity, usually from solar panels, to throw out charged atoms of a gas such as xenon at 20
  to 50 km/s. Their push is tiny, 25 to 250 millinewtons, the weight of 2.5 to 25 grams on Earth, so they are useless
  for leaving the ground, but in space they can run for years. NASA's Dawn, launched in 2007 to the asteroids Vesta
  and Ceres, gained about 11 km/s with its ion engines, more than any spacecraft before had managed on its own after
  leaving its launcher, using 425 kg of xenon (section 13.8). Japan's Hayabusa and Hayabusa2 and Europe's SMART-1 and
  BepiColombo also used electric engines.

So there is a trade. Strong pushes need chemical rockets, with slow exhaust and huge mass ratios. Frugal engines give
gentle pushes over months.

??? note "Sources"
    - Specific impulse in seconds, the RS-25's 453 s and 4.44 km/s in a vacuum, rockets at sea level between 200 and
      400 s, and the 542 s lithium–fluorine–hydrogen test: Wikipedia,
      [Specific impulse](https://en.wikipedia.org/wiki/Specific_impulse) (weaker).
    - Ion thrusters' exhaust velocities of 20 to 50 km/s and thrusts of 25 to 250 mN, xenon, Hayabusa, Hayabusa2,
      SMART-1 and BepiColombo: Wikipedia, [Ion thruster](https://en.wikipedia.org/wiki/Ion_thruster) (weaker).
    - Dawn's launch in September 2007 to Vesta and Ceres, its 425 kg of xenon and its velocity change of about 11 km/s,
      more than any earlier spacecraft after separation from its launcher: Wikipedia,
      [Dawn (spacecraft)](https://en.wikipedia.org/wiki/Dawn_(spacecraft)) (weaker).
    - The weight of 2.5 to 25 g: $0.025 / 9.81$ and $0.25 / 9.81$ kg, our arithmetic.

## 13.5 Stages { #stages }

Once the propellant in a tank is used up, the empty tank is dead weight, and so are the big engines that were needed
to lift the full rocket. A **multistage** rocket throws them away. Each stage burns, then drops off, and the next
starts with a much lighter rocket to push.

The physics lesson [Staging, worked out](https://physics.akadian.ca/topics/rockets/level-6/06-staging.html) puts
numbers on it, for kerosene engines and stages whose tanks and engines are 8% of their fuelled mass.

| Stages | Payload, as a share of the launch mass |
| --- | --- |
| 1 | cannot reach orbit: even empty, it reaches only 8.3 km/s |
| 2 | 3.0% |
| 3 | 3.7% |

The big step is from one stage to two; a third adds a little more, along with more engines, more separations and more
to go wrong. Most launchers have two stages, often with extra boosters strapped to the sides. Upper stages often burn
hydrogen, because every kilogram saved high up is a kilogram the first stage does not have to lift.

**The Saturn V**, which sent astronauts to the Moon, had three stages and weighed about 2,900 tonnes fully fuelled.
It could put about 140 tonnes into low orbit round the Earth, counting its third stage still partly full of
propellant for the trip on to the Moon: just under 5% of its launch mass. Thirteen were launched, from 1967 to 1973.

??? note "Sources"
    - The stage-by-stage payload shares and the advice on hydrogen upper stages: this site's physics lesson Staging,
      worked out (above).
    - The Saturn V's three liquid-fuelled stages, its fuelled mass of 2,822 to 2,965 t, 140 t to low Earth orbit
      including the partly fuelled third stage, and thirteen launches from 1967 to 1973: Wikipedia,
      [Saturn V](https://en.wikipedia.org/wiki/Saturn_V) (weaker).
    - Why staging helps: Wikipedia, Multistage rocket (above).

## 13.6 The road to orbit { #budget }

A satellite in low orbit moves at about 7.8 km/s (chapter 1). Yet a rocket needs to be able to gain about **9.4 km/s**
to get it there. The extra 1.5 to 2 km/s is lost on the way.

- **Gravity.** While a rocket climbs, gravity slows it by 9.8 m/s every second. So a rocket wants to climb out of the
  thick air quickly, then tip over and build up speed sideways, where gravity no longer takes so much. The physics
  lesson [Gravity losses](https://physics.akadian.ca/topics/rockets/level-8/03-gravity-losses.html) shows how.
- **Air.** Drag takes a smaller share, mostly low down where the air is thick.

**A free push.** The ground is already moving east as the Earth spins, at 465 m/s at the equator and less farther north
or south (chapter 7, [section 7.4](07-Speed-Energy-and-Escape.md#escape)). A rocket launched eastwards keeps that speed
for free. Figure B shows how much each launch site gets.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="How much speed the Earth's spin gives a rocket launched due east, against the latitude of the launch site, from 465 m/s at the equator falling to 233 m/s at 60 degrees. Seven launch sites are marked: Kourou in French Guiana at 5 degrees north gets 463 m/s; Sriharikota in India at 14 degrees, 452; Wenchang in China at 20 degrees, 438; Cape Canaveral in the USA at 28 degrees, 409; Tanegashima in Japan at 30 degrees, 401; Mahia in New Zealand at 39 degrees south, 360; and Baikonur in Kazakhstan at 46 degrees, 323.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">A free push from the Earth's spin</text>
    <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="0.6"/>
    <line x1="40" y1="190" x2="40" y2="40" stroke="currentColor" stroke-width="0.6"/>
    <line x1="37" y1="190.0" x2="40" y2="190.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="35" y="193.0" text-anchor="end">0</text>
    <line x1="37" y1="160.0" x2="40" y2="160.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="35" y="163.0" text-anchor="end">100</text>
    <line x1="37" y1="130.0" x2="40" y2="130.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="35" y="133.0" text-anchor="end">200</text>
    <line x1="37" y1="100.0" x2="40" y2="100.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="35" y="103.0" text-anchor="end">300</text>
    <line x1="37" y1="70.0" x2="40" y2="70.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="35" y="73.0" text-anchor="end">400</text>
    <line x1="37" y1="40.0" x2="40" y2="40.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="35" y="43.0" text-anchor="end">500</text>
    <text x="10" y="32">m/s eastward</text>
    <line x1="40.0" y1="190" x2="40.0" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="40.0" y="201" text-anchor="middle">0°</text>
    <line x1="83.3" y1="190" x2="83.3" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="83.3" y="201" text-anchor="middle">10°</text>
    <line x1="126.7" y1="190" x2="126.7" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="126.7" y="201" text-anchor="middle">20°</text>
    <line x1="170.0" y1="190" x2="170.0" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="170.0" y="201" text-anchor="middle">30°</text>
    <line x1="213.3" y1="190" x2="213.3" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="213.3" y="201" text-anchor="middle">40°</text>
    <line x1="256.7" y1="190" x2="256.7" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="256.7" y="201" text-anchor="middle">50°</text>
    <line x1="300.0" y1="190" x2="300.0" y2="193" stroke="currentColor" stroke-width="0.6"/>
    <text x="300.0" y="201" text-anchor="middle">60°</text>
    <text x="300" y="210" text-anchor="end">latitude of the launch site, north or south</text>
    <path d="M40.0,50.5 L42.2,50.5 L44.3,50.5 L46.5,50.5 L48.7,50.6 L50.8,50.6 L53.0,50.7 L55.2,50.7 L57.3,50.8 L59.5,50.9 L61.7,51.0 L63.8,51.1 L66.0,51.2 L68.2,51.4 L70.3,51.5 L72.5,51.7 L74.7,51.8 L76.8,52.0 L79.0,52.2 L81.2,52.4 L83.3,52.6 L85.5,52.8 L87.7,53.0 L89.8,53.3 L92.0,53.5 L94.2,53.8 L96.3,54.0 L98.5,54.3 L100.7,54.6 L102.8,54.9 L105.0,55.2 L107.2,55.5 L109.3,55.9 L111.5,56.2 L113.7,56.6 L115.8,56.9 L118.0,57.3 L120.2,57.7 L122.3,58.1 L124.5,58.5 L126.7,58.9 L128.8,59.3 L131.0,59.7 L133.2,60.2 L135.3,60.6 L137.5,61.1 L139.7,61.6 L141.8,62.0 L144.0,62.5 L146.2,63.0 L148.3,63.5 L150.5,64.1 L152.7,64.6 L154.8,65.1 L157.0,65.7 L159.2,66.2 L161.3,66.8 L163.5,67.4 L165.7,68.0 L167.8,68.6 L170.0,69.2 L172.2,69.8 L174.3,70.4 L176.5,71.0 L178.7,71.7 L180.8,72.3 L183.0,73.0 L185.2,73.6 L187.3,74.3 L189.5,75.0 L191.7,75.7 L193.8,76.4 L196.0,77.1 L198.2,77.8 L200.3,78.6 L202.5,79.3 L204.7,80.0 L206.8,80.8 L209.0,81.6 L211.2,82.3 L213.3,83.1 L215.5,83.9 L217.7,84.7 L219.8,85.5 L222.0,86.3 L224.2,87.1 L226.3,88.0 L228.5,88.8 L230.7,89.6 L232.8,90.5 L235.0,91.3 L237.2,92.2 L239.3,93.1 L241.5,94.0 L243.7,94.8 L245.8,95.7 L248.0,96.6 L250.2,97.5 L252.3,98.5 L254.5,99.4 L256.7,100.3 L258.8,101.2 L261.0,102.2 L263.2,103.1 L265.3,104.1 L267.5,105.1 L269.7,106.0 L271.8,107.0 L274.0,108.0 L276.2,109.0 L278.3,110.0 L280.5,111.0 L282.7,112.0 L284.8,113.0 L287.0,114.0 L289.2,115.0 L291.3,116.1 L293.5,117.1 L295.7,118.1 L297.8,119.2 L300.0,120.2" fill="none" stroke="#5aa0d8" stroke-width="1.2"/>
    <circle cx="62.4" cy="51.0" r="2.2" fill="#c1440e"/>
    <line x1="62.4" y1="54.0" x2="62.4" y2="56.0" stroke="#555" stroke-width="0.4"/>
    <text x="62.4" y="63.0" text-anchor="middle">Kourou 463</text>
    <circle cx="99.5" cy="54.5" r="2.2" fill="#c1440e"/>
    <line x1="99.5" y1="57.5" x2="99.5" y2="69.5" stroke="#555" stroke-width="0.4"/>
    <text x="99.5" y="76.5" text-anchor="middle">Sriharikota 452</text>
    <circle cx="125.0" cy="58.6" r="2.2" fill="#c1440e"/>
    <line x1="125.0" y1="61.6" x2="125.0" y2="83.6" stroke="#555" stroke-width="0.4"/>
    <text x="125.0" y="90.6" text-anchor="middle">Wenchang 438</text>
    <circle cx="163.5" cy="67.4" r="2.2" fill="#c1440e"/>
    <line x1="163.5" y1="70.4" x2="163.5" y2="110.4" stroke="#555" stroke-width="0.4"/>
    <text x="163.5" y="117.4" text-anchor="middle">Cape Canaveral 409</text>
    <circle cx="171.7" cy="69.7" r="2.2" fill="#c1440e"/>
    <text x="174.7" y="61.7">Tanegashima 401</text>
    <circle cx="210.1" cy="82.0" r="2.2" fill="#c1440e"/>
    <text x="213.1" y="74.0">Mahia 360</text>
    <circle cx="239.2" cy="93.0" r="2.2" fill="#c1440e"/>
    <text x="242.2" y="85.0">Baikonur 323</text>
    <text x="6" y="226">A rocket sitting on the launch pad is already moving east with the ground. Fired due east,</text>
    <text x="6" y="235">it keeps that speed: 465 m/s at the equator, less farther north or south. Numbers are m/s.</text>
    <text x="6" y="244">Launching west means first cancelling the spin, so rockets head east whenever the orbit allows.</text>
  </g>
</svg>
</div>

So launch sites are placed with care. Europe launches from Kourou in French Guiana, only 5° north of the equator, with
open sea to the east and north. India's Sriharikota is on an island off its east coast, near the equator, with the
Bay of Bengal to the east. China chose Wenchang, on Hainan island at 19° north, for its heaviest rocket, the Long March
5, because its low latitude lets bigger payloads be launched. A site's latitude also sets the least tilt an orbit can
have if the rocket flies straight there, which matters for satellites that must sit above the equator.

Not everyone can go east. Israel launches its Shavit rockets westwards from Palmachim, out over the Mediterranean,
because of where Israel lies and its hostile relations with neighbouring countries. Going west means first cancelling
the Earth's spin, so the satellites must be lighter.

??? note "Sources"
    - The 9.4 km/s to reach a low orbit, and the 7.8 km/s plus 1.5 to 2 km/s for drag and gravity: Wikipedia,
      [Delta-v budget](https://en.wikipedia.org/wiki/Delta-v_budget) (weaker).
    - Gravity losses and pitching over: this site's physics lesson Gravity losses (above).
    - Kourou at 5°, about 500 km north of the equator, with open sea to the east and north, in use since 1968:
      Wikipedia, [Guiana Space Centre](https://en.wikipedia.org/wiki/Guiana_Space_Centre) (weaker).
    - Sriharikota off the east coast, with the Bay of Bengal, and its nearness to the equator helping eastward launches:
      Wikipedia, [Satish Dhawan Space Centre](https://en.wikipedia.org/wiki/Satish_Dhawan_Space_Centre) (weaker).
    - Wenchang at 19° north, chosen for larger payloads, the only site of the Long March 5: Wikipedia,
      [Wenchang Space Launch Site](https://en.wikipedia.org/wiki/Wenchang_Space_Launch_Site) (weaker).
    - Palmachim, Shavit launches into retrograde orbit, westwards over the Mediterranean because of Israel's relations
      with neighbouring countries: Wikipedia, [Palmachim Airbase](https://en.wikipedia.org/wiki/Palmachim_Airbase)
      (weaker).
    - The latitudes of the sites in Figure B: the coordinates in the Wikipedia articles above and in
      [Cape Canaveral Space Force Station](https://en.wikipedia.org/wiki/Cape_Canaveral_Space_Force_Station),
      [Tanegashima Space Center](https://en.wikipedia.org/wiki/Tanegashima_Space_Center) and
      [Rocket Lab Launch Complex 1](https://en.wikipedia.org/wiki/Rocket_Lab_Launch_Complex_1) (all weaker). The speeds
      are our arithmetic, section 13.8. The least tilt equal to the latitude, and lighter payloads westwards: standard.

## 13.7 Leaving Mars { #mars }

Nothing has yet been launched from the surface of Mars. But the numbers are much kinder there.

**Less speed.** A low orbit round Mars needs about 3.5 km/s (chapter 1,
[section 1.9](01-Falling-Round-the-Earth.md#mars)). With the losses on the way, a rocket climbing from the surface
needs about **4.1 km/s**, less than half the Earth's 9.4. Mars's spin gives at most 241 m/s at its equator, about half
what the Earth gives.

**One stage is enough.** With methane engines, whose exhaust leaves at about 3.7 km/s, the mass ratio is
$e^{4.1/3.7} = 3.0$: two thirds of the rocket is propellant, and one stage can carry about a quarter of its launch
mass into orbit. From the Earth, the same engines would need a mass ratio of nearly 13.

**Fuel from Mars.** A crew's rocket home might need around 100 tonnes of methane and liquid oxygen, far too much to
bring. It could be made on Mars from the air, which is 95% carbon dioxide, and from ice under the ground: split the
water into hydrogen and oxygen with electricity, then join the hydrogen to carbon dioxide to make methane. The physics
lesson [Propellant from Mars](https://physics.akadian.ca/topics/rockets/level-8/02-propellant-from-mars.html) works out
how much water, power and time it would take. A small start has been made. **MOXIE**, a box on NASA's Perseverance
rover, made oxygen from Mars's carbon dioxide on 16 runs, the first on 20 April 2021 and the last on 7 August 2023:
122 g in all, about what a small dog breathes in 10 hours.

**The first launch from Mars.** A joint NASA and ESA mission to bring back the rock samples Perseverance has collected
was cancelled in 2026 (history book, [section 21.9](../history/21-The-Space-Age-at-Mars.md#samples)). China's
**Tianwen-3**, due to be launched in 2028, plans a lander carrying a small ascent rocket, to bring about 500 g of Mars
to the Earth by 2031. If it works, it will be the first rocket ever to lift off from another planet.

??? note "Sources"
    - The 4.1 km/s from the surface, 3.7 km/s for methane engines, the mass ratio of 3.03, the payload of about 27% for
      one stage, and nearly 13 from the Earth: this site's physics lessons Tsiolkovsky's rocket equation and Staging,
      worked out (above).
    - Around 100 t of methane and oxygen, Mars's air 95% carbon dioxide, ice under the ground, electrolysis and the
      Sabatier reaction: this site's physics lesson Propellant from Mars (above).
    - Mars's equatorial radius of 3,396.2 km and day of 24.6229 hours: NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html). The 241 m/s: our arithmetic.
    - MOXIE's solid oxide electrolysis from 20 April 2021, its 16th and final run on 7 August 2023, 122 g in all, and
      the small dog: Wikipedia, [MOXIE](https://en.wikipedia.org/wiki/MOXIE) (weaker).
    - The NASA–ESA mission cancelled in 2026: Wikipedia,
      [Mars sample-return mission](https://en.wikipedia.org/wiki/Mars_sample-return_mission) (weaker). Tianwen-3 to be
      launched in 2028 with a lander and ascent vehicle, returning about 500 g by 2031: Wikipedia,
      [Tianwen-3](https://en.wikipedia.org/wiki/Tianwen-3) (weaker).
    - That nothing has yet been launched from Mars, as of 2026: standard; no sample return has flown.

## 13.8 Working it out { #working }

**Propellant shares.** The share of a rocket that is propellant is $1 - m_1/m_0 = 1 - e^{-\Delta v / v_e}$.

| Exhaust speed | Mars to orbit, 4.1 km/s | Earth to orbit, 9.4 km/s |
| --- | --- | --- |
| kerosene, 3.3 km/s | mass ratio 3.5, 71% propellant | mass ratio 17.3, 94% |
| methane, 3.7 km/s | 3.0, 67% | 12.7, 92% |
| hydrogen, 4.4 km/s | 2.5, 61% | 8.5, 88% |
| ion, 26 km/s | 1.17, 15% | 1.44, 30% |

**Dawn.** At launch it had a mass of 1,218 kg, with 425 kg of xenon. Using all the xenon gives a mass ratio of
$1{,}218 / 793 = 1.536$, and $\ln 1.536 = 0.429$. To gain 11 km/s, the exhaust must have averaged
$11 / 0.429 = 26$ km/s. A chemical engine at 4.4 km/s would have needed a mass ratio of $e^{11/4.4} = 12$.

**Saturn V.** $140 / 2{,}965 = 4.7\%$ of the heaviest launch mass reached low orbit.

**The free push.** A point on the equator goes round once a sidereal day, 86,164 s:
$2\pi \times 6{,}378{,}137 / 86{,}164 = 465$ m/s. At latitude $\varphi$ it is $465 \cos\varphi$; at Baikonur,
$465 \times \cos 46.0° = 323$ m/s. On Mars, $2\pi \times 3{,}396{,}200 / (24.6229 \times 3{,}600) = 241$ m/s.

**Low orbit at Mars.** $v = \sqrt{GM/r}$ with $GM = 42{,}828$ km³/s² and $r = 3{,}390 + 200 = 3{,}590$ km gives
$\sqrt{42{,}828 / 3{,}590} = 3.45$ km/s.

| | Mars | Earth |
| --- | --- | --- |
| Speed in a low orbit | 3.45 km/s at 200 km | 7.8 km/s |
| Speed to gain from the ground, with losses | about 4.1 km/s | about 9.4 km/s |
| Mass ratio with methane engines | 3.0 | 12.7 |
| Free push from the spin at the equator | 241 m/s | 465 m/s |
| Rockets launched from the surface so far | none | thousands |

??? note "Sources"
    - Dawn's launch mass of 2,684.6 lb (1,218 kg) and 425 kg of xenon: Wikipedia, Dawn (above). The Saturn V's mass:
      Wikipedia, Saturn V (above).
    - The Earth's equatorial radius of 6,378.137 km and sidereal day of 23.9345 hours: NASA,
      [Earth Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html). Mars's $GM$ of 42,828 km³/s²
      and radius of 3,389.5 km: NASA, Mars Fact Sheet (above).
    - The exhaust speeds: sections 13.3, 13.4 and 13.7. "Thousands" of launches from the Earth: standard. The
      arithmetic is ours.

## 13.9 The rocket equation from momentum { #derive }

Picture a rocket far out in space, away from any planet, with mass $m$ and speed $v$. In a short moment it throws out
a little exhaust of mass $\delta m$, backwards at speed $v_e$ relative to itself.

Watch from a frame moving along with the rocket at that moment. Before, everything is at rest, so the momentum is
zero. After, the rocket, now of mass $m - \delta m$, moves forwards at $\delta v$, and the exhaust moves backwards at
$v_e$. Momentum is conserved, so

$$0 = (m - \delta m)\,\delta v - \delta m\, v_e.$$

The term $\delta m\,\delta v$ is the product of two tiny amounts and can be dropped, leaving
$m\,\delta v = v_e\,\delta m$. The rocket's mass falls by $\delta m$, so writing its change of mass as
$dm = -\delta m$,

$$dv = -v_e\,\frac{dm}{m}.$$

Add up all the small steps, from the full mass $m_0$ to the empty mass $m_1$:

$$\Delta v = -v_e \int_{m_0}^{m_1} \frac{dm}{m} = v_e \ln\frac{m_0}{m_1}.$$

Two things stand out. The answer does not depend on how fast the propellant is burned, only on how much. And it is a
logarithm, because each kilogram of exhaust pushes a lighter rocket than the one before it, but the early kilograms
have to push all the propellant still waiting in the tanks.

**With gravity.** Near a planet, gravity pulls the whole time the engine burns. Climbing at an angle $\gamma$ above the
horizon for a time $t$, the rocket loses $\int g\sin\gamma\,dt$ of its speed. This is the gravity loss of section 13.6,
and it is why a slow, steep climb wastes propellant.

??? note "Sources"
    - The derivation and the gravity loss term: standard, and this site's physics lessons Tsiolkovsky's rocket
      equation and Gravity losses (above).

## Check yourself { #check }

**1.** (beginner) What does a rocket push against in empty space?

??? note "Answer"
    Its own exhaust. It throws gas out backwards, and by Newton's third law the gas pushes it forwards. It needs no air.

**2.** (beginner) Name three places in Asia where rockets were made before 1800.

??? note "Answer"
    China, with fire arrows from around the 10th to 12th centuries and the two-stage "fire-dragon" of the 14th; Korea,
    with the Munjong Hwacha by 1451; and Mysore in India, with iron-cased rockets in the 1780s and 1790s.

**3.** (beginner) What two things does the rocket equation say a rocket's gain in speed depends on?

??? note "Answer"
    The exhaust speed and the mass ratio, the full mass divided by the empty mass.

**4.** (intermediate) A rocket's exhaust leaves at 3 km/s and it has a mass ratio of 4. How much speed can it gain
in empty space?

??? note "Answer"
    $\Delta v = 3 \ln 4 = 3 \times 1.386 = 4.2$ km/s.

**5.** (intermediate) Why do rockets that reach orbit from the Earth almost always have more than one stage?

??? note "Answer"
    Reaching orbit needs a mass ratio of 8.5 to 17, so 88% to 94% of the rocket must be propellant. One stage cannot be
    built that light. Dropping empty tanks and engines lets the later stages push much less mass.

**6.** (intermediate) Why is Kourou, 5° from the equator, a good place to launch from?

??? note "Answer"
    The ground there moves east at 463 m/s, almost the most anywhere, and a rocket launched east keeps that speed. It
    also has open sea to the east and north, so spent stages fall into the ocean.

**7.** (advanced) An ion engine has an exhaust speed of 30 km/s. What fraction of a spacecraft must be xenon for it
to gain 6 km/s?

??? note "Answer"
    $m_0/m_1 = e^{6/30} = e^{0.2} = 1.221$, so the xenon is $1 - 1/1.221 = 18\%$ of the starting mass.

**8.** (expert) In the derivation, why can the term $\delta m\,\delta v$ be dropped?

??? note "Answer"
    It is the product of two tiny amounts. If each is made ten times smaller, it gets a hundred times smaller, while
    the other terms get only ten times smaller. In the limit it vanishes, and the sum becomes an exact integral.

## Summary

- A rocket throws exhaust backwards and is pushed forwards; it needs no air, and works best in a vacuum.
- Rockets began as fire arrows in Song China, spread across Asia to Korea and the Middle East, were cased in iron in
  Mysore, and became spacecraft through Tsiolkovsky, Goddard, Oberth and Korolev.
- The rocket equation, $\Delta v = v_e \ln(m_0/m_1)$, makes the needed mass ratio grow exponentially with speed.
- Chemical engines push hard with exhaust at 3 to 4.4 km/s; ion engines reach 20 to 50 km/s but push very gently.
- Reaching orbit from the Earth takes about 9.4 km/s, so rockets are staged, climb steeply then tip over, and launch
  east from sites as near the equator as they can.
- Leaving Mars takes about 4.1 km/s and a mass ratio of about 3, so one stage is enough, and its fuel could be made
  from Mars's air and ice.

**Next:** [chapter 14, Orbits around the Earth](14-Orbits-Around-the-Earth.md), where we look at the different orbits
satellites use, from the space station skimming the top of the air to geostationary satellites that seem to hang still
in the sky.

## Further reading

- Frank H. Winter, *Rockets into Space*, Harvard University Press, 1990.
