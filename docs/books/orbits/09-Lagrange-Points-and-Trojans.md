# 9. Lagrange points and Trojans

*Two bodies going round each other follow Kepler's ellipses exactly. Add a third and there is no tidy formula any
more, but there are still five places where a small body can keep pace with the other two. This chapter shows where
they are, who found them, why two of them hold on to whatever drifts in while the other three let go, and what lives
there: telescopes, solar watchmen, a radio relay for the far side of the Moon, faint clouds of dust, and thousands of
asteroids that share Jupiter's orbit, with a few that share Mars's.*

!!! abstract "In this chapter"
    **You will learn:**

    - where the five Lagrange points of two orbiting bodies are
    - how Euler and Lagrange found them in the 18th century, long before anything was seen there
    - why spacecraft from Europe, the United States, India and China are parked at them
    - what the Trojan asteroids are, how they got their names, and where the Lucy probe is going
    - why L4 and L5 hold on to things while L1, L2 and L3 do not
    - what shares the Earth's orbit, and the faint dust clouds near the Moon
    - how far out a planet's or a moon's own gravity is in charge
    - what shares Mars's orbit, and how little room Phobos has to itself
    - why the triangle points work, and how to find L2 more exactly

    **You need:** chapters 3 and 5.

    **Levels:** 9.1 to 9.4 are beginner; 9.5 to 9.8 are intermediate; 9.9 is advanced; 9.10 is expert.

## 9.1 Five places to keep pace { #five }

A body closer to the Sun than the Earth goes round faster, and one farther out goes round slower (chapter 3). So it
seems nothing else could keep step with the Earth. But the Earth pulls too. Just inside the Earth's orbit, on the line
to the Sun, the Earth pulls outwards against the Sun, so a body there can go round more slowly than its distance would
allow, and it takes exactly a year. Just outside the Earth's orbit the Earth's pull adds to the Sun's, so a body there
can go round faster than its distance would allow, again in exactly a year. These two places are **L1** and **L2**.

There are three more. **L3** is on the far side of the Sun, just beyond the Earth's distance, where the Earth's small
pull added to the Sun's again makes the year come out right. **L4** and **L5** are on the Earth's orbit, 60° ahead of
the Earth and 60° behind it. Each makes an equal-sided triangle with the Sun and the Earth.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The five Lagrange points of the Sun and a planet. The Sun is in the middle and the planet goes round it anticlockwise on a dashed circle. L1 is just inside the planet's orbit, between it and the Sun, and L2 just outside, on the far side of the planet; for the Earth both are about 1.5 million km away, where SOHO and Aditya-L1 watch the Sun from L1 and Webb and Gaia look out from L2. L3 is on the far side of the Sun, always hidden behind it. L4 is 60 degrees ahead of the planet and L5 60 degrees behind; each makes an equal-sided triangle with the Sun and the planet. Shaded zones round L4 and L5 are where Trojans gather: Jupiter's Greek camp at L4 and its Trojan camp at L5, the Earth's Trojan 2010 TK7 at L4, and Mars's Trojan Eureka at L5.">
  <g font-size="8" fill="currentColor">
    <circle cx="140" cy="118" r="82" fill="none" stroke="#555" stroke-width="0.6" stroke-dasharray="3 2"/>
    <path d="M204.6,67.5 A82,82 0 0 0 151.4,36.8" fill="none" stroke="#eea66f" stroke-width="7" stroke-opacity="0.45"/>
    <path d="M151.4,199.2 A82,82 0 0 0 204.6,168.5" fill="none" stroke="#eea66f" stroke-width="7" stroke-opacity="0.45"/>
    <path d="M140,118 L181.0,47.0 L222.0,118.0" fill="none" stroke="#5aa0d8" stroke-width="0.6" stroke-dasharray="2 2"/>
    <path d="M140,118 L181.0,189.0 L222.0,118.0" fill="none" stroke="#5aa0d8" stroke-width="0.6" stroke-dasharray="2 2"/>
    <line x1="50.0" y1="118" x2="244.0" y2="118" stroke="#5aa0d8" stroke-width="0.6" stroke-dasharray="2 2"/>
    <circle cx="140" cy="118" r="9" fill="#eea66f"/>
    <text x="140" y="138" text-anchor="middle">Sun</text>
    <circle cx="222.0" cy="118" r="4" fill="#5aa0d8"/>
    <text x="222.0" y="132" text-anchor="middle">planet</text>
    <line x1="219.6" y1="98.2" x2="213.7" y2="82.1" stroke="#555" stroke-width="0.8"/>
    <path d="M216.6,84.8 L213.7,82.1 L213.3,86.0" fill="none" stroke="#555" stroke-width="0.8"/>
    <circle cx="208.0" cy="118.0" r="2.4" fill="#c1440e"/>
    <circle cx="236.0" cy="118.0" r="2.4" fill="#c1440e"/>
    <circle cx="58.0" cy="118.0" r="2.4" fill="#c1440e"/>
    <circle cx="181.0" cy="47.0" r="2.4" fill="#c1440e"/>
    <circle cx="181.0" cy="189.0" r="2.4" fill="#c1440e"/>
    <text x="208.0" y="112" text-anchor="middle">L1</text>
    <text x="236.0" y="112" text-anchor="middle">L2</text>
    <text x="58.0" y="111" text-anchor="middle">L3</text>
    <text x="52" y="134" text-anchor="end">behind</text>
    <text x="52" y="143" text-anchor="end">the Sun</text>
    <text x="175.0" y="50.0" text-anchor="end">L4</text>
    <text x="175.0" y="192.0" text-anchor="end">L5</text>
    <text x="196" y="28">L4, 60° ahead: Jupiter's Greek</text>
    <text x="196" y="37">camp, the Earth's 2010 TK7</text>
    <text x="196" y="205">L5, 60° behind: Jupiter's Trojan</text>
    <text x="196" y="214">camp, Mars's Eureka</text>
    <text x="252" y="92">L1: SOHO, Aditya-L1</text>
    <text x="252" y="101">L2: Webb, Gaia</text>
    <text x="252" y="140">For the Earth, L1</text>
    <text x="252" y="149">and L2 are 1.5 million</text>
    <text x="252" y="158">km away, drawn here</text>
    <text x="252" y="167">far too far out.</text>
    <text x="6" y="12">The five Lagrange points</text>
    <text x="6" y="226">A small body at any of the five points keeps pace with the planet. L1, L2 and L3 lie on</text>
    <text x="6" y="235">the line through the Sun and the planet. L4 and L5 make equal-sided triangles with them,</text>
    <text x="6" y="244">and the shaded zones round them are where Trojans gather.</text>
  </g>
</svg>
</div>

*Figure A. The five Lagrange points of the Sun and a planet.*

Every pair of bodies in orbit has its own five points: the Sun and the Earth, the Sun and Jupiter, the Earth and the
Moon, Mars and Phobos. They are named after Joseph-Louis Lagrange, and are also called libration points. The physics
lesson [Lagrange points](https://physics.akadian.ca/topics/gravity/level-8/03-lagrange-points.html) shows the same
balance with a moving picture.

??? note "Sources"
    - The five points, L1, L2 and L3 on the line through the two bodies and L4 and L5 at the third corners of
      equal-sided triangles, 60° ahead of and behind the smaller body, and the name libration points: Wikipedia,
      [Lagrange point](https://en.wikipedia.org/wiki/Lagrange_point) (weaker).
    - Closer orbits being faster: chapter 3. How the planet's pull adds to or takes from the Sun's: standard.

## 9.2 Euler, Lagrange and the three-body problem { #history }

Newton solved the problem of two bodies: each goes round their balance point on an ellipse (chapter 5,
[section 5.6](05-Newtons-Law-of-Gravity.md#barycentre); history book,
[section 16.2](../history/16-Newton-Halley-and-Romer.md#principia)). With three bodies, each pulls on the other two
and their paths change all the time, and no general formula gives them. Mathematicians in the 18th century looked
instead at special cases, above all the **restricted** problem, where the third body is too small to move the other
two.

The Swiss mathematician Leonhard Euler found the three points on the line around 1750. About a decade later the
Italian-born Joseph-Louis Lagrange found the other two, and in 1772 he published an *Essay on the three-body problem*.
He predicted that a small body sharing a planet's orbit, 60° ahead of it or behind it, would be trapped there.

For more than a century nobody saw one. E. E. Barnard recorded an asteroid in 1904, later numbered 12126 Chersidamas,
without anyone realising what it was. In 1906 the German astronomer Max Wolf found 588 Achilles, 60° ahead of Jupiter.
In 1906 and 1907 August Kopff found two more, 624 Hektor and 617 Patroclus. Lagrange's prediction had waited
134 years.

??? note "Sources"
    - Euler finding L1, L2 and L3 around 1750, a decade before Lagrange found L4 and L5, and Lagrange's 1772 *Essay on
      the three-body problem*: Wikipedia, Lagrange point (above).
    - Lagrange's prediction for the restricted problem, Barnard's 1904 observation of 12126 Chersidamas, Max Wolf's
      588 Achilles in 1906, and Kopff's 624 Hektor and 617 Patroclus in 1906 and 1907: Wikipedia,
      [Jupiter trojan](https://en.wikipedia.org/wiki/Jupiter_trojan) (weaker).
    - That there is no general formula for three bodies: standard. The 134 years is our arithmetic.

## 9.3 Parking places in space { #parking }

**L1: watching the Sun.** The Sun–Earth L1 point is about 1.5 million km from the Earth, towards the Sun. A spacecraft
there never passes into the Earth's shadow, and the solar wind sweeps past it on its way to us. The first was ISEE-3 in
1978, an early warning post for storms from the Sun. Since then SOHO, Wind, ACE and DSCOVR have gone there, and DSCOVR
also takes pictures of the whole sunlit face of the Earth. India's **Aditya-L1**, named after the Sanskrit word for
the Sun, was built by ISRO and launched on a PSLV rocket on 2 September 2023, and reached L1 on 6 January 2024. It is
India's first mission to study the Sun. Solar wind at about 400 km/s takes about an hour to cross from L1 to the
Earth, so these craft give about an hour's warning of a storm.

**L2: looking out.** The Sun–Earth L2 point is the same distance on the other side of the Earth. Webb reached it in
January 2022 (book 2, [section 19.5](../light-and-telescopes/19-Telescopes-in-Space.md#webb)); Gaia and Euclid are
there too, and WMAP and Planck were before them. From L2 the Sun, the Earth and the Moon are all on the same side, so
one sunshade can block all three, and the Earth is always in view for sending data home.

**Behind the Moon.** The Earth–Moon L2 point is beyond the far side of the Moon. China's space agency, the CNSA,
launched **Queqiao** on 20 May 2018, and on 14 June it settled into an orbit about 65,000 km from the Moon. It passes
messages between the Earth and the Chang'e 4 lander on the far side, which can never see the Earth directly. It was
the first relay satellite at that point.

**L3** is always hidden behind the Sun. Stories and comic books have put a "Counter-Earth" there, but the pulls of the
other planets rule out a planet at L3.

Spacecraft do not sit exactly on the points. Webb, Euclid, Aditya-L1 and Queqiao circle them on **halo orbits**, and
Gaia on a looser Lissajous orbit. Section 9.5 explains why they need to keep moving.

??? note "Sources"
    - L1 about 1.5 million km from the Earth; ISEE-3 in 1978 as the first mission there; SOHO, Wind, Aditya-L1 and ACE
      at L1; DSCOVR at L1 studying the solar wind and taking images of the Earth; Gaia and Euclid at L2 and WMAP and
      Planck before them; the advantages of L2 for power, fuel and keeping the Earth in view; L3 and Counter-Earth:
      Wikipedia, Lagrange point (above).
    - Aditya-L1, the name meaning Sun, ISRO, launch on PSLV-C57 on 2 September 2023, arrival at L1 in a halo orbit on
      6 January 2024, and India's first mission dedicated to the Sun: Wikipedia,
      [Aditya-L1](https://en.wikipedia.org/wiki/Aditya-L1) (weaker).
    - Webb reaching L2 in January 2022, its halo orbit, and its sunshield guarding against the Sun, the Earth and the
      Moon: Wikipedia, [James Webb Space Telescope](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope) (weaker).
    - Queqiao, CNSA, launched 20 May 2018, its final burn on 14 June 2018 into a halo orbit about 65,000 km from the
      Moon, its relay role for Chang'e 4, and being the first relay at Earth–Moon L2: Wikipedia,
      [Queqiao relay satellite](https://en.wikipedia.org/wiki/Queqiao_relay_satellite) (weaker).
    - A solar wind speed of about 400 km/s is standard; the hour is our arithmetic in section 9.9. That the Sun, Earth
      and Moon lie on one side from L2 is standard geometry.

## 9.4 The Trojans of Jupiter { #trojans }

The asteroids at Jupiter's L4 and L5 points were named after the heroes of Homer's *Iliad*, the poem of the war for
Troy. Those at L4, ahead of Jupiter, take Greek names and are called the **Greek camp**; those at L5, behind it, take
the names of heroes of Troy and are the **Trojan camp**. Together they are the Trojans. More than 15,300 had been
found by October 2025, and there may be about a million larger than 1 km, about as many as in the main asteroid belt.
Many are dark and reddish. In 2001 617 Patroclus was the first to be found to be a pair, two bodies going round each
other.

NASA's **Lucy** probe was launched on 16 October 2021 to visit them. It is named after the Lucy fossil, the bones of
an early human relative, because the Trojans may be "fossils of planet formation", left over from the time the planets
were built. On the way it flew past the asteroid Dinkinesh on 1 November 2023; Dinkinesh is the Amharic name for the
Lucy fossil. Lucy found that Dinkinesh has a moon, Selam, made of two lumps stuck together. It passed Donaldjohanson in
April 2025. In August 2027 it reaches the Greek camp, where it will pass Eurybates, Polymele, Leucus and Orus. In 2031
it swings past the Earth (chapter 16) and heads for the Trojan camp, to reach Patroclus and its partner Menoetius in
2033.

??? note "Sources"
    - The names from the *Iliad*, the Greek camp at L4 and the Trojan camp at L5: Wikipedia, Lagrange point and Jupiter
      trojan (above).
    - More than 15,300 found by October 2025, about a million larger than 1 km, about as many as in the main belt, dark
      reddish bodies, and Patroclus found to be binary in 2001: Wikipedia, Jupiter trojan (above).
    - Lucy's launch on 16 October 2021, its name and the "fossils of planet formation", the flybys of Dinkinesh and
      Donaldjohanson, Eurybates in August 2027 with Polymele, Leucus and Orus, the Earth flyby in 2031 and
      Patroclus–Menoetius in 2033: Wikipedia, [Lucy (spacecraft)](https://en.wikipedia.org/wiki/Lucy_(spacecraft))
      (weaker).
    - Dinkinesh as the Amharic name for the Lucy fossil, the flyby on 1 November 2023 and its contact-binary moon
      Selam: Wikipedia, [152830 Dinkinesh](https://en.wikipedia.org/wiki/152830_Dinkinesh) (weaker).

## 9.5 Hilltops and hollows { #stable }

**L1, L2 and L3 let go.** A body nudged off L1 or L2 drifts farther away, like a ball balanced on a hilltop (book 2,
[section 19.10](../light-and-telescopes/19-Telescopes-in-Space.md#l2)). For the Sun–Earth L1 and L2 points, a small
error grows by a factor of about $e$, 2.7 times, every 23 days. So natural bodies rarely stay at these points, and
spacecraft there fire their thrusters now and then to stay on their halo orbits.

**L4 and L5 hold on.** A body nudged off L4 or L5 does not run away. As it moves, the turning of the whole system bends
its path sideways (the **Coriolis effect**), and the path curls round the point instead of away from it. A Trojan that
strays towards the planet is tugged backwards by it, loses a little energy, drops to a slightly smaller and faster
orbit, and draws away again. Seen from a frame that turns with the planet, a Trojan swings slowly round its point on a
long curved path called a **tadpole orbit**. A body with a wider swing can travel past L3 and back on a **horseshoe
orbit**, but it is not counted as a Trojan.

This only works if the bigger body is more than 24.96 times as heavy as the smaller one. The Sun is 1,048 times as
heavy as Jupiter and 332,946 times as heavy as the Earth, so their L4 and L5 points are stable. The Earth is 81.3 times
as heavy as the Moon, so the Earth–Moon points are stable too, by a smaller margin.

??? note "Sources"
    - L1, L2 and L3 unstable, natural objects rare there, and spacecraft needing small station-keeping burns; Sun–Earth
      L1 and L2 unstable with a time constant of about 23 days; L4 and L5 stable through the Coriolis effect when the
      mass ratio is above 24.96, which holds for Sun–Earth, Sun–Jupiter and, by a smaller margin, Earth–Moon; horseshoe
      orbits not being Trojans: Wikipedia, Lagrange point (above).
    - Trojans moving round the points on tadpole or horseshoe orbits: Wikipedia, Jupiter trojan (above).
    - The mass ratios, from standard $GM$ values: our arithmetic. The tug from the planet and the drop to a faster
      orbit: standard, as in chapter 7, [section 7.2](07-Speed-Energy-and-Escape.md#paradox).

## 9.6 The Earth's Trojans and the Moon's dust clouds { #earth }

**The Earth's Trojans.** Seen from the Earth, L4 and L5 are always 60° from the Sun, in the evening or morning sky,
so small bodies there are hard to spot. The first Earth Trojan, **2010 TK7**, about 300 m across, was found on
1 October 2010 by WISE, an infrared telescope in orbit. The second, **2020 XL5**, about 1.2 km across, was found by the
Pan-STARRS survey on 12 December 2020 and recognised as a Trojan in January 2021. Both are at L4; none are yet known at
L5. Both points also hold thin clouds of dust.

**The Moon's dust clouds.** Between 1953 and 1956 a team led by Clyde Tombaugh, who had found Pluto, planned to
search the Earth–Moon L4 and L5 points for small moons, but bad weather stopped them. The Polish astronomer Kazimierz
Kordylewski also searched for objects there and found none. In 1956 Józef Witkowski suggested that he look for faint
clouds of dust instead, and in 1961 Kordylewski saw them from the Tatra Mountains, in what was then Czechoslovakia.

Other astronomers could not always see them, and the clouds became controversial. They are very faint, hard to tell
apart from other glows of the night sky, and Japan's Hiten spacecraft found nothing when it passed in 1991 and 1992.
In 2018 a team from Eötvös Loránd University in Hungary, led by Judit Slíz-Balogh, first worked out on a computer how
the L5 cloud should look in polarised light, then photographed it, and found what they expected. The clouds are now
said to be tentatively confirmed.

??? note "Sources"
    - 2010 TK7, 300 m, found by WISE on 1 October 2010; 2020 XL5, 1.2 km, found by Pan-STARRS on 12 December 2020 and
      recognised in January 2021; both at L4 and none known at L5: Wikipedia,
      [Earth trojan](https://en.wikipedia.org/wiki/Earth_trojan) (weaker).
    - Dust at the Sun–Earth L4 and L5 points: Wikipedia, Lagrange point (above).
    - Tombaugh's planned search of 1953 to 1956, Kordylewski's search, Witkowski's suggestion in 1956, the sighting
      of 1961 from the Tatra Mountains, the controversy, the glow problem, Hiten in 1991 and 1992, and the 2018
      polarisation study by Slíz-Balogh's team at Eötvös Loránd University: Wikipedia,
      [Kordylewski cloud](https://en.wikipedia.org/wiki/Kordylewski_cloud) (weaker).
    - Tombaugh finding Pluto: history book, [section 17.8](../history/17-Herschel-and-the-Canals-of-Mars.md#illusion).
      That L4 and L5 are 60° from the Sun as seen from the Earth is the geometry of the equal-sided triangle.

## 9.7 Who is in charge where { #hill }

Every planet has a region round it where its own gravity, not the Sun's, decides what can orbit it. This is the
**Hill sphere**, worked out by the American astronomer George William Hill from the work of the French astronomer
Édouard Roche (chapter 8, [section 8.9](08-Tides.md#roche)). Its edge is at L1 and L2, so its radius is the distance
found in book 2, [section 19.10](../light-and-telescopes/19-Telescopes-in-Space.md#l2):

$$r_H = a\left(\frac{m}{3M}\right)^{1/3},$$

where $a$ is the planet's distance from the Sun, $m$ its mass and $M$ the Sun's. For the Earth it is about 1.5 million
km. The Moon, at 384,400 km, is about a quarter of the way out. A moon much farther out would spend part of its orbit
beyond the edge, where the Sun would pull it away. Orbits that go round the wrong way, against the planet's spin,
stay stable farther out than those going the usual way.

The cube root makes the Hill sphere grow slowly with mass: a planet 1,000 times lighter at the same distance has a
Hill sphere only 10 times smaller. The idea works on any scale. The Sun's own Hill sphere, against the pull of the
rest of the Galaxy, reaches out about 230,000 AU, 3.6 light-years.

??? note "Sources"
    - The Hill sphere as the region where a body's own gravity dominates in holding satellites, its definition by the
      American astronomer George William Hill from the French astronomer Édouard Roche's work, the Earth's at about
      1.5 million km, objects beyond it being pulled away, retrograde orbits staying stable over a wider region, and
      the Sun's of about 230,000 AU or 3.6 light-years: Wikipedia,
      [Hill sphere](https://en.wikipedia.org/wiki/Hill_sphere) (weaker).
    - The formula: book 2, section 19.10. A quarter of the way out, and the factor of 10: our arithmetic in section 9.9.

## 9.8 Lagrange points and Trojans of Mars { #mars }

**Mars's Hill sphere** reaches about 1.08 million km (book 2,
[section 19.10](../light-and-telescopes/19-Telescopes-in-Space.md#l2)). Deimos, at 23,459 km, is only about 2% of the
way out, far deeper inside than the Moon is in the Earth's.

**Mars's Trojans.** The first was found on 20 June 1990 by David H. Levy and Henry Holt at Palomar Observatory:
**5261 Eureka**, at Mars's L5 point. It swings so little that its distance from Mars changes by only about 0.3 AU in
each trip round the Sun. Eureka spins in 2.69 hours and has a small moon of its own, about 0.46 km across and 2.1 km
away, found on 28 November 2011. Today 17 asteroids have been shown by long computer runs to be stable Mars Trojans,
and 9 of them are accepted by the Minor Planet Center.

Most of the smaller ones at L5 follow orbits so like Eureka's that they are thought to be pieces of it. Sunlight
falling on an uneven body and given off again as heat gives it a tiny, steady twist, the **YORP effect**. Over a long
time this spun Eureka up to its fast spin, and pieces flew off. Eureka and two others look rich in olivine, a green
mineral. The Trojan at L4, 1999 UJ7, tumbles slowly and chaotically, about once every 50 hours, which stops YORP
spinning it up, and its light looks quite different from that of the Eureka family.

**Phobos and Deimos have Hill spheres too**, against the pull of Mars. Phobos's reaches only 16.6 km from its centre,
and Phobos itself is 13.0 km from its centre to the end of its long axis, which points at Mars. The ends of Phobos are
78% of the way to the edge, which fits the strong outward pull at its ends found in chapter 8,
[section 8.7](08-Tides.md#mars). Deimos is smaller, but it is farther from Mars, and its Hill sphere is 25 km, more
than three times its own half-length.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The Hill spheres of Phobos and Deimos, drawn to scale. Each moon is shown from above Mars's pole, with Mars off to the left. Phobos is 26 km long and points its long axis at Mars; its Hill sphere, the distance out to its own L1 and L2 points, is only 16.6 km in radius, so the tips of Phobos reach 78% of the way to the edge. Deimos is only 15.6 km long, but because it is farther from Mars its Hill sphere is 25 km in radius, more than three times its own half-length.">
  <g font-size="8" fill="currentColor">
    <circle cx="88" cy="112" r="49.7" fill="#5aa0d8" fill-opacity="0.12" stroke="#5aa0d8" stroke-width="0.9" stroke-dasharray="4 3"/>
    <ellipse cx="88" cy="112" rx="39.0" ry="34.2" fill="#cfc8bf" stroke="#555" stroke-width="0.6"/>
    <text x="88" y="115" text-anchor="middle" fill="#222">Phobos</text>
    <line x1="88" y1="112" x2="122.7" y2="147.7" stroke="#5aa0d8" stroke-width="0.6"/>
    <text x="88" y="173.7" text-anchor="middle" fill="#5aa0d8">Hill sphere, 16.6 km</text>
    <circle cx="240" cy="112" r="75.7" fill="#5aa0d8" fill-opacity="0.12" stroke="#5aa0d8" stroke-width="0.9" stroke-dasharray="4 3"/>
    <ellipse cx="240" cy="112" rx="23.4" ry="18.0" fill="#cfc8bf" stroke="#555" stroke-width="0.6"/>
    <text x="240" y="115" text-anchor="middle" fill="#222">Deimos</text>
    <line x1="240" y1="112" x2="292.8" y2="166.3" stroke="#5aa0d8" stroke-width="0.6"/>
    <text x="240" y="199.7" text-anchor="middle" fill="#5aa0d8">Hill sphere, 25 km</text>
    <line x1="64.0" y1="34.0" x2="36.0" y2="34.0" stroke="#c1440e" stroke-width="0.9"/>
    <path d="M39.6,32.3 L36.0,34.0 L39.6,35.7" fill="none" stroke="#c1440e" stroke-width="0.9"/>
    <text x="68" y="37">to Mars</text>
    <line x1="49.0" y1="112" x2="49.0" y2="58" stroke="currentColor" stroke-width="0.4"/>
    <text x="49.0" y="54" text-anchor="middle">tip, 13 km</text>
    <line x1="150" y1="206" x2="180" y2="206" stroke="currentColor" stroke-width="1"/>
    <line x1="150" y1="203" x2="150" y2="209" stroke="currentColor" stroke-width="0.6"/>
    <line x1="180" y1="203" x2="180" y2="209" stroke="currentColor" stroke-width="0.6"/>
    <text x="165" y="201" text-anchor="middle">10 km</text>
    <text x="6" y="12">How far each moon's own gravity rules</text>
    <text x="6" y="226">To scale. Each dashed circle reaches out to the moon's own L1 and L2 points. Phobos</text>
    <text x="6" y="235">nearly fills it: the ends of its long axis are 78% of the way out. Deimos, farther from</text>
    <text x="6" y="244">Mars, sits well inside a sphere more than three times its half-length.</text>
  </g>
</svg>
</div>

*Figure B. Phobos nearly fills its Hill sphere; Deimos does not.*

**A shield at L1.** In 2017 a NASA conference discussed putting a magnetic shield at the Sun–Mars L1 point, to stand
in for the magnetic field Mars has lost and keep some of the solar wind off it.

??? note "Sources"
    - Mars's Hill sphere of 1.08 million km: book 2, section 19.10. The orbit of Deimos and the sizes of Phobos and
      Deimos: NASA, [Mars fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - Eureka found on 20 June 1990 by Levy and Holt at Palomar, the first Mars Trojan, at L5, its distance from Mars
      changing by only 0.3 AU each revolution, its 0.46 km moon 2.1 km away found on 28 November 2011, and its 2.69 hour
      spin: Wikipedia, [5261 Eureka](https://en.wikipedia.org/wiki/5261_Eureka) (weaker).
    - 17 stable Mars Trojans with 9 accepted by the Minor Planet Center, the smaller L5 members as fragments of Eureka
      spun off by YORP, the olivine-rich spectra, and 1999 UJ7's chaotic rotation of about 50 hours and different
      spectrum: Wikipedia, [Mars trojan](https://en.wikipedia.org/wiki/Mars_trojan) (weaker).
    - The 2017 NASA conference idea of a magnetic shield at Sun–Mars L1 as an artificial magnetosphere: Wikipedia,
      Lagrange point (above).
    - How YORP works, and Mars having lost its global magnetic field: standard. The Hill spheres of Phobos and Deimos
      and the 78%: our arithmetic in section 9.9.

## 9.9 Working it out { #working }

The Hill radius, the distance to L1 and L2, is $r_H = a(m/3M)^{1/3}$.

**The Earth.** The Sun is 332,946 times as heavy, so $(1/998{,}838)^{1/3} = 0.01000$ and
$r_H = 0.01000 \times 149.6$ million km $= 1.50$ million km. The Moon's 384,400 km is 26% of it.

**The Moon.** The Earth is 81.30 times as heavy, so $(1/243.9)^{1/3} = 0.1601$ and
$r_H = 0.1601 \times 384{,}400 = 61{,}500$ km beyond the Moon. Section 9.10 gives a better answer.

**Phobos.** Mars's mass is $6.417 \times 10^{23}$ kg and Phobos's $1.0637 \times 10^{16}$ kg, so
$m / 3M = 5.53 \times 10^{-9}$, whose cube root is 0.001768, and $r_H = 0.001768 \times 9{,}378 = 16.6$ km. The end
of Phobos, at 13.0 km, is $13.0 / 16.6 = 78\%$ of the way out.

**Deimos.** With $2.4 \times 10^{15}$ kg, $m / 3M = 1.25 \times 10^{-9}$, the cube root is 0.001076, and
$r_H = 0.001076 \times 23{,}459 = 25.2$ km, 3.2 times Deimos's long half-axis of 7.8 km.

**The warning from L1.** Solar wind at 400 km/s crosses 1.5 million km in $1{,}500{,}000 / 400 = 3{,}750$ s, about an
hour.

| | Mars | Earth |
| --- | --- | --- |
| The Sun's mass, compared with the planet's | 3.10 million times | 332,946 times |
| Hill sphere, out to L1 and L2 | 1.08 million km | 1.50 million km |
| Largest moon, as a share of the Hill sphere | Deimos, 2% | the Moon, 26% |
| Trojans known | 17 shown stable, 9 accepted | 2, both at L4 |
| First Trojan found | Eureka, 1990 | 2010 TK7, 2010 |

??? note "Sources"
    - $GM$ values and masses: chapter 6. Distances: NASA fact sheets, chapter 8. Trojans: sections 9.6 and 9.8. The
      arithmetic is ours.

## 9.10 Why the triangle points work, and a better L2 { #derive }

**The triangle points.** Put the balance point of the Sun and the planet at the origin. The Sun, of mass $M$, is at
position $\mathbf{S}$ and the planet, of mass $m$, at $\mathbf{P}$, so that $M\mathbf{S} + m\mathbf{P} = 0$, and they
are a distance $a$ apart. Both go round the origin with angular speed $\omega$, where $\omega^2 = G(M + m)/a^3$
(chapter 5, [section 5.5](05-Newtons-Law-of-Gravity.md#kepler)).

Now put a small body at $\mathbf{L}$, a distance $a$ from both. The pull on it is

$$\mathbf{g} = \frac{GM(\mathbf{S} - \mathbf{L})}{a^3} + \frac{Gm(\mathbf{P} - \mathbf{L})}{a^3}
= \frac{G}{a^3}\left[(M\mathbf{S} + m\mathbf{P}) - (M + m)\mathbf{L}\right]$$

$$= -\frac{G(M + m)}{a^3}\,\mathbf{L} = -\omega^2\mathbf{L}.$$

This points straight at the balance point, and it is exactly the pull needed to go round it at angular speed $\omega$.
So the body keeps pace with the planet for ever. The trick works only because both distances are $a$, so that each
$1/a^3$ matches the one in $\omega^2$. That is why the three must make an equal-sided triangle.

**A better L2.** The simple formula treats the planet as tiny. Measure distances in units of $a$ from the balance
point, and let $\mu = m/(M + m)$. Then the big body is at $x = -\mu$ and the small one at $x = 1 - \mu$. A point at
$x$ beyond the small body keeps pace when the pull it gets equals the pull it needs, $\omega^2 x a$, which gives

$$x = \frac{1 - \mu}{(x + \mu)^2} + \frac{\mu}{(x - 1 + \mu)^2}.$$

This cannot be solved neatly, but trial and error closes in fast. For the Earth and the Moon, $\mu = 0.01215$, and the
answer is $x - (1 - \mu) = 0.1678$, so L2 is 64,500 km beyond the Moon, 5% farther than the simple 61,500 km. Queqiao's
orbit round it reaches about 65,000 km from the Moon. The same sum with a minus sign on the second term gives L1,
58,000 km on the Earth's side of the Moon. For the Sun and the Earth, $\mu$ is only $3.0 \times 10^{-6}$, and the
simple formula is within 0.3%.

??? note "Sources"
    - The barycentre form of Kepler's third law: chapter 5. The derivations are standard; the numbers are our
      arithmetic. Queqiao's orbit: section 9.3.

## Check yourself { #check }

**1.** (beginner) Where are Jupiter's L4 and L5 points, and what is found there?

??? note "Answer"
    On Jupiter's orbit, 60° ahead of Jupiter and 60° behind it. Both hold the Trojan asteroids: the Greek camp at L4
    and the Trojan camp at L5, more than 15,300 of them known.

**2.** (beginner) Why is the Sun–Earth L1 point a good place to watch the Sun?

??? note "Answer"
    It never passes into the Earth's shadow, so the Sun is always in view, and the solar wind passes it about an hour
    before it reaches the Earth, which gives warning of storms.

**3.** (beginner) Why did China put Queqiao beyond the Moon, near the Earth–Moon L2 point?

??? note "Answer"
    Chang'e 4 landed on the far side of the Moon, which never faces the Earth, so it could not send signals home
    directly. From its orbit round L2, Queqiao can see both the far side and the Earth and pass the messages on.

**4.** (intermediate) Webb fires its thrusters now and then to stay near L2, but the Trojans have stayed near
Jupiter's L4 and L5 for ages without any. Why the difference?

??? note "Answer"
    L2 is like a hilltop: a small error grows, about 2.7 times every 23 days, so Webb must correct it. At L4 and L5 a
    body that drifts is turned sideways by the Coriolis effect and swings round the point instead of leaving it.

**5.** (intermediate) The Earth is 81.3 times as heavy as the Moon. Could small bodies stay at the Earth–Moon L4
and L5 points?

??? note "Answer"
    Yes, because 81.3 is more than 24.96, though by a smaller margin than for the Sun and Jupiter. The Kordylewski dust
    clouds are thought to be there.

**6.** (intermediate) The Sun is 3.10 million times as heavy as Mars, which is 227.9 million km from it. Find the
radius of Mars's Hill sphere.

??? note "Answer"
    $(1/(3 \times 3.10 \times 10^6))^{1/3} = (1/9.3 \times 10^6)^{1/3} = 0.00476$, and
    $0.00476 \times 227.9$ million km $= 1.08$ million km.

**7.** (advanced) Charon has 0.122 of Pluto's mass (chapter 5). Can Pluto and Charon have stable Trojans?

??? note "Answer"
    No. Pluto is $1/0.122 = 8.2$ times as heavy as Charon, less than the 24.96 needed, so its L4 and L5 points are
    not stable.

**8.** (expert) For the Sun and the Earth, $\mu = 3.0 \times 10^{-6}$. Put $x = 1.01$ into the right-hand side of the
L2 equation in section 9.10. How close is it to 1.01, and what does that say about where L2 is?

??? note "Answer"
    $\dfrac{1 - \mu}{(1.010003)^2} + \dfrac{\mu}{(0.010003)^2} = 0.98029 + 0.03002 = 1.01030$, within 0.03% of
    1.01. So L2 is very close to $x = 1.01$, about $0.01 \times 149.6$ million km $= 1.5$ million km beyond the
    Earth. A slightly larger $x$, 1.01003, balances it exactly.

## Summary

- Every pair of orbiting bodies has five Lagrange points where a small third body can keep pace: L1, L2 and L3 on the
  line through them, and L4 and L5 at 60° ahead and behind.
- Euler found L1 to L3 around 1750 and Lagrange found L4 and L5 in 1772; the first Trojan was found in 1906.
- Sun–Earth L1 and L2, 1.5 million km away, hold solar watchmen such as SOHO and Aditya-L1 and telescopes such as Webb
  and Gaia; Queqiao relays from behind the Moon.
- L1, L2 and L3 are unstable, so spacecraft there must keep correcting; L4 and L5 are stable when the big body is more
  than 24.96 times as heavy as the small one.
- Jupiter has more than 15,300 known Trojans, and the Lucy probe is on its way to them. The Earth has two, and the
  Moon's L4 and L5 points seem to hold faint dust clouds.
- The Hill sphere, out to L1 and L2, is where a body's own gravity is in charge: 1.5 million km for the Earth and
  1.08 million km for Mars.
- Mars has 17 known stable Trojans, most of them probably pieces of Eureka. Phobos nearly fills its own Hill sphere.

**Next:** [chapter 10, Wobbling orbits and the finding of Neptune](10-Wobbling-Orbits-and-the-Finding-of-Neptune.md),
where the planets' small pulls on each other bend
their orbits, and a wobble in the path of Uranus leads to a new planet.

## Further reading

- Carl D. Murray and Stanley F. Dermott, *Solar System Dynamics*, Cambridge University Press, 1999. Chapter 3 is on
  the restricted three-body problem and the Lagrange points; it is a university text.
