# 20. Water and the search for life

*Is there life anywhere else in the solar system? Nobody knows yet, but we know where to look. Life as we know it
needs liquid water, and this chapter follows the water: the Earth's open oceans, the ice and buried water of Mars,
and the hidden oceans under the ice of moons far from the Sun. It tells how people around the world have imagined and
searched for life beyond the Earth, from old scriptures to Viking's experiments and a spotted rock found by
Perseverance in 2024. It ends with a calculation that shows why water on Mars today cannot stay liquid for long.*

!!! abstract "In this chapter"
    **You will learn:**

    - what life as we know it needs, and what the habitable zone is
    - where water is found in the solar system, as ice, as open sea and as oceans hidden under ice
    - how much water Mars had, and where its water is now
    - how the search for life on Mars has gone, from Viking in 1976 to the spotted rock Cheyava Falls
    - how people from India and the Islamic world to Italy, the Soviet Union, Japan and China thought about and
      searched for life on other worlds
    - which spacecraft are on their way to look, and how samples of Mars might reach the Earth
    - why Europa, Enceladus and Titan are as interesting as Mars
    - how to work out the temperatures at which water can be liquid at a given air pressure

    **You need:** chapter 6 for the Earth's water, chapter 8 for Mars, chapter 15 for the oceans under ice, and chapter
    19 for Mars's thin air. For 20.9, the exponential function.

    **Levels:** 20.1 to 20.3 are beginner; 20.4 to 20.7 are intermediate; 20.8 is advanced; 20.9 is expert.

## 20.1 What life needs { #needs }

**Three things.** Every living thing we know needs:

- **liquid water**, in which its chemistry takes place;
- **a source of energy**, such as sunlight or chemicals that can react;
- **the right ingredients**, above all carbon, hydrogen, nitrogen, oxygen, phosphorus and sulphur.

Carbon and the other ingredients are common in the solar system: dark asteroids, many meteorites and comets are
rich in carbon (chapters 9, 10 and 17). Energy is easy to find too. **Liquid water** is the hard part,
because water is liquid only within a narrow range of temperature and pressure.

**The habitable zone.** The **habitable zone** is the range of distances from a star where a planet's surface could
hold liquid water. Too close, and the water boils away; too far, and it freezes. Estimates for the Sun vary widely,
because they depend on the planet's air. One estimate puts the zone between **0.84 and 1.7 AU**, which takes in the
Earth and Mars but not Venus. The most cautious estimates take in only the Earth; the most generous stretch from
Mercury to Saturn.

**Not just distance.** Being in the zone is not enough. A planet also needs air thick enough to keep water liquid. A
study led by the Italian astronomer Giovanni Vladilo in 2013 found that below about **15 millibars**, a small change
in pressure or temperature is enough to stop water being liquid at all. Mars, at 6.36 millibars, is below that line
(section 20.9). And being outside the zone is not the end either: the moons of the giant planets are far beyond it,
yet several have oceans under their ice, kept warm from inside by tides (chapter 15,
[section 15.3](15-Moons-of-the-Giants.md#oceans)).

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Where water is found in the solar system, against distance from the Sun on a scale where each step is ten times the last, from 0.3 to 50 astronomical units. A shaded band from 0.84 to 1.7 AU marks one estimate of the habitable zone, where sunlight could keep water liquid on a surface. Top row, liquid water open on the surface: only the Earth. Middle row, liquid water probably under ice or rock: Mars deep down, Ceres, Europa, Ganymede and Callisto at Jupiter, Enceladus and Titan at Saturn, and perhaps Pluto. Bottom row, ice: Mercury and the Moon in dark polar craters, Mars in its polar caps and ground, and comets.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">Where the water is</text>
    <rect x="114.3" y="24.0" width="37.2" height="168.0" fill="#5aa0d8" opacity="0.15"/>
    <text x="132.9" y="32.0" text-anchor="middle" fill="#5aa0d8">habitable zone?</text>
    <line x1="60.0" y1="24.0" x2="60.0" y2="192.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="60.0" y="202.0" text-anchor="middle">0.3</text>
    <line x1="123.5" y1="24.0" x2="123.5" y2="192.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="123.5" y="202.0" text-anchor="middle">1</text>
    <line x1="181.5" y1="24.0" x2="181.5" y2="192.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="181.5" y="202.0" text-anchor="middle">3</text>
    <line x1="245.1" y1="24.0" x2="245.1" y2="192.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="245.1" y="202.0" text-anchor="middle">10</text>
    <line x1="303.0" y1="24.0" x2="303.0" y2="192.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="303.0" y="202.0" text-anchor="middle">30</text>
    <text x="195.0" y="212.0" text-anchor="middle">distance from the Sun (AU)</text>
    <text x="6" y="55">on the surface</text>
    <line x1="60.0" y1="52" x2="330.0" y2="52" stroke="#555" stroke-width="0.5" stroke-dasharray="2 2"/>
    <text x="6" y="109">liquid, hidden</text>
    <line x1="60.0" y1="106" x2="330.0" y2="106" stroke="#555" stroke-width="0.5" stroke-dasharray="2 2"/>
    <text x="6" y="163">ice</text>
    <line x1="60.0" y1="160" x2="330.0" y2="160" stroke="#555" stroke-width="0.5" stroke-dasharray="2 2"/>
    <circle cx="123.5" cy="52" r="3.6" fill="#5aa0d8"/>
    <text x="123.5" y="44" text-anchor="middle">Earth</text>
    <circle cx="145.8" cy="106" r="3.6" fill="#c1440e"/>
    <text x="145.8" y="98" text-anchor="middle">Mars, deep</text>
    <circle cx="177.3" cy="106" r="3.6" fill="#eea66f"/>
    <text x="177.3" y="119" text-anchor="middle">Ceres</text>
    <circle cx="210.5" cy="106" r="3.6" fill="#eea66f"/>
    <text x="210.5" y="82" text-anchor="middle">Europa,</text>
    <text x="210.5" y="90" text-anchor="middle">Ganymede,</text>
    <text x="210.5" y="98" text-anchor="middle">Callisto</text>
    <circle cx="242.6" cy="106" r="3.6" fill="#eea66f"/>
    <text x="242.6" y="119" text-anchor="middle">Enceladus,</text>
    <text x="242.6" y="127" text-anchor="middle">Titan</text>
    <circle cx="317.6" cy="106" r="3.6" fill="#eea66f"/>
    <text x="317.6" y="98" text-anchor="middle">Pluto?</text>
    <circle cx="73.4" cy="160" r="3.6" fill="#cfc8bf"/>
    <text x="73.4" y="152" text-anchor="middle">Mercury</text>
    <circle cx="123.5" cy="160" r="3.6" fill="#cfc8bf"/>
    <text x="123.5" y="173" text-anchor="middle">Moon</text>
    <circle cx="145.8" cy="160" r="3.6" fill="#c1440e"/>
    <text x="145.8" y="152" text-anchor="middle">Mars</text>
    <circle cx="181.5" cy="160" r="3.6" fill="#cfc8bf"/>
    <text x="181.5" y="152" text-anchor="middle">comets</text>
    <circle cx="266.5" cy="160" r="3.6" fill="#cfc8bf"/>
    <text x="266.5" y="152" text-anchor="middle">comets</text>
    <text x="6" y="226">Shaded: one estimate of where sunlight could keep water liquid on a surface. Only the Earth has</text>
    <text x="6" y="235">open water now. Most liquid water is far outside the zone, under the ice of moons warmed from</text>
    <text x="6" y="244">inside by tides. Mars keeps its water as ice, with perhaps some liquid 10 to 20 km down.</text>
  </g>
</svg>
</div>

??? note "Sources"
    - The six ingredients: Wikipedia, [Enceladus](https://en.wikipedia.org/wiki/Enceladus) (weaker), which lists
      them as "the set of basic chemical ingredients for life". Water, energy and ingredients as what life needs:
      standard. Carbon-rich asteroids, meteorites and comets: chapters 9, 10 and 17.
    - The habitable zone, its definition, estimates that "vary widely", 0.84 to 1.7 AU including the Earth and Mars
      but not Venus, the most cautious and most generous estimates, and Vladilo's 15 mb in 2013: Wikipedia,
      [Circumstellar habitable zone](https://en.wikipedia.org/wiki/Circumstellar_habitable_zone) (weaker).
    - Mars's 6.36 mb: chapter 19. Tides warming the moons' oceans: chapter 15.

## 20.2 Water across the solar system { #water }

**Water is everywhere, but rarely liquid.** Beyond the snow line, where the planets formed, water ice was one of the
commonest solids (chapter 2), so the outer solar system is full of it. Here is where it is found today:

| World | Where its water is | Liquid now? |
|---|---|---|
| Mercury | ice in dark craters at the poles | no |
| Moon | ice in dark polar craters; traces in the soil | no |
| Earth | oceans, ice caps, the ground and the air | yes, open on the surface |
| Mars | polar caps, ice in the ground | perhaps, deep underground |
| Ceres | brine under the crust | perhaps, as salty water |
| Europa, Ganymede, Callisto | oceans under ice | very likely |
| Enceladus, Titan | oceans under ice | very likely |
| Pluto | perhaps an ocean under ice | perhaps |
| Comets | ice | no |

The Earth is the only world with liquid water lying open on its surface, about 1.4 × 10²¹ kg of it (chapter 6,
[section 6.3](06-The-Earth-as-a-Planet.md#oceans)). The Moon's and Mercury's ice sits in craters near the poles that
sunlight never reaches (chapter 7, [section 7.5](07-The-Moon.md#water), and chapter 4,
[section 4.3](04-Mercury.md#ice)). Ceres has brine under its crust that has reached the surface in hundreds of places
(chapter 9, [section 9.5](09-The-Asteroid-Belt-and-Ceres.md#ceres)), and Pluto may have an ocean at least 100 km
deep (chapter 16, [section 16.2](16-Pluto-and-the-Kuiper-Belt.md#pluto)).

**The hidden oceans.** Europa's ocean may hold **2 to 3 times** as much water as all the Earth's oceans (chapter 15).
**Enceladus**, a moon only 504 km across, sprays its ocean into space: jets of water vapour, hydrogen, salt
and ice near its south pole throw out about **200 kg a second**. Cassini flew through the spray and found salts,
organic molecules and hydrogen, and in 2023 phosphates were found too, so all six ingredients of 20.1 are there.

**Where the Earth's water came from.** Nobody is sure. It may have come out of the Earth's own rocks, or been
brought by icy bodies hitting the young Earth. Comet 67P's water has three times as much heavy hydrogen as our oceans,
so comets like it cannot have brought most of it (chapter 17, [section 17.3](17-Comets-and-the-Oort-Cloud.md#makeup)).

??? note "Sources"
    - The snow line and ice in the outer solar system: chapter 2. Mercury, the Moon, Earth, Ceres and Pluto: chapters
      4, 7, 6, 9 and 16. Europa, Ganymede, Callisto and Titan: chapter 15. Mars: section 20.3. Comets: chapter 17.
    - Enceladus's jets near the south pole, about 200 kg/s, Cassini's finds in the plumes including organics and
      hydrogen, and the phosphates of June 2023: Wikipedia, Enceladus (above). Its size of 504 km: chapter 15.
    - Possible sources of the Earth's water, "still not completely understood": Wikipedia, Circumstellar habitable
      zone (above). 67P's deuterium: chapter 17.

## 20.3 Mars's water, then and now { #marswater }

**Then.** Mars's oldest ground, more than 3.7 billion years old, is cut by branching **river valleys**, probably made
by rain or by water seeping out of the ground, and many craters held **lakes** (chapter 8,
[section 8.4](08-Mars-among-the-Planets.md#ages)). Later, huge floods carved long single channels. Before about 3.8
billion years ago Mars may have had thicker air and higher temperatures, and possibly an **ocean** covering a third
of the planet, in the low northern plains. The water in Mars's air today has **eight times** as much heavy hydrogen as
the Earth's. Light hydrogen escapes more easily (chapter 19, [section 19.4](19-Air-Magnetism-and-Weather.md#loss)),
so this suggests Mars once had far more water. China's rover Zhurong, in Utopia Planitia, sent back data by
September 2022 that supports the idea of an old ocean there.

**Now.** Most of Mars's water is **ice**. The northern polar cap holds about **1.6 million cubic kilometres**, and the
southern cap with the layered ground round it about the same; Greenland's ice sheet holds 2.85 million. Counting the
ice in the ground, more than **5 million cubic kilometres** lie at or near the surface, enough to cover the whole
planet **35 m** deep. Under Utopia Planitia alone there is as much ice as there is water in Lake Superior.

**Liquid water?** In 2018 radar on Mars Express showed what may be a lake of liquid water **1.5 km** under the south
polar cap, about 20 km across, though others doubt it. In August 2024 a study of the marsquakes recorded by InSight
suggested a store of liquid water **10 to 20 km** down in the crust, far too deep to reach. At the surface, water
cannot stay liquid for long: the air is so thin that water boils away almost as soon as it melts (section 20.9).

??? note "Sources"
    - The Noachian valley networks, Hesperian outflow channels, crater lakes, the possible ocean on a third of the
      planet before about 3.8 billion years ago, the eight times deuterium, the 5 million km³ and 35 m, the ice under
      Utopia Planitia, the 2018 lake 1.5 km down and 20 km across, and the InSight study of August 2024: Wikipedia,
      [Water on Mars](https://en.wikipedia.org/wiki/Water_on_Mars) (weaker). Mars Express's radar as the instrument,
      and the doubts: standard. The Noachian's age: chapter 8.
    - The two polar caps' 1.6 million km³ each, and Greenland's 2.85 million: Wikipedia,
      [Martian polar ice caps](https://en.wikipedia.org/wiki/Martian_polar_ice_caps) (weaker).
    - Zhurong's data by September 2022 supporting an old ocean in Utopia Planitia: Wikipedia,
      [Zhurong](https://en.wikipedia.org/wiki/Zhurong_(rover)) (weaker).
    - Light hydrogen escaping more easily: chapter 19.

## 20.4 Looking for life on Mars { #life }

**Viking, 1976.** The two Viking landers carried experiments to look for living things in the soil. In the **labelled
release** experiment, a drop of nutrient made with radioactive carbon was added to the soil, and both landers saw
radioactive gas come off at once, as if something were eating it. But another instrument found **no organic
molecules** at all in the soil. Most Viking scientists concluded that the landers had not found life, and that the gas
came from chemistry, though Gilbert Levin, who ran the experiment, still argued years later that it had. In 2008
Phoenix found **perchlorate** in the soil, a salt that destroys organic molecules when the soil is heated, as the
Viking instrument did. So Viking may have missed organic matter that was there.

**A meteorite, 1996.** On 6 August 1996 a NASA team led by David McKay announced that the Martian meteorite
**ALH84001** (book 3, [section 7.7](../orbits/07-Speed-Energy-and-Escape.md#mars)) held tiny shapes like fossil
bacteria and crystals of magnetite like those some bacteria make. It made headlines around the world, but most
scientists came to reject it once every odd feature had been explained without life.

**Methane.** Methane breaks down in sunlight within a few hundred years, so methane in Mars's air would need a source,
perhaps living things, perhaps reactions between water and rock. In 2003 several parts per billion were reported, and
Curiosity has measured short bursts of up to 21 parts per billion at Gale crater. But Europe's Trace Gas Orbiter,
looking from above since 2018, finds less than 0.05 parts per billion. Nobody yet knows why the two disagree.

**Cheyava Falls, 2024.** On 18 July 2024 Perseverance found a reddish rock about a metre long in an old river valley
running into Jezero crater (book 11, [section 11.10](../history/11-The-Americas.md#mars)). It has white veins and
small pale spots ringed with black, like a leopard's. On 21 July the rover drilled a core from it, called **Sapphire
Canyon**. On 10 September 2025 NASA called it a **"potential biosignature"**: the rock holds organic carbon, and its
spots contain iron minerals, vivianite and greigite. On the Earth, vivianite is often found round decaying organic
matter, and some microbes make greigite. Both can also form without life. If life made them, it lived about **3.5
billion years** ago. Only tests in laboratories on the Earth can tell, so the core waits in a tube for a ride home.

??? note "Sources"
    - Viking's labelled release, the radioactive carbon, positive results at both landers, Levin, the conclusion of
      most Viking scientists, and Phoenix's perchlorate in 2008 destroying organics: Wikipedia,
      [Viking lander biological experiments](https://en.wikipedia.org/wiki/Viking_lander_biological_experiments)
      (weaker). No organics found by the other instrument: Wikipedia,
      [Life on Mars](https://en.wikipedia.org/wiki/Life_on_Mars) (weaker). Perchlorate acting when heated, as the
      Viking instrument heated its samples: standard.
    - ALH84001: 6 August 1996, McKay, the fossil-like shapes, magnetite, headlines worldwide and later rejection:
      Wikipedia, [Allan Hills 84001](https://en.wikipedia.org/wiki/Allan_Hills_84001) (weaker). Its discovery: book 3.
    - Methane breaking down in sunlight, its possible sources, several ppb in 2003, Curiosity's up to 21 ppb, and the
      Trace Gas Orbiter's under 0.05 ppbv: Wikipedia, Life on Mars (above). "A few hundred years": standard.
    - Cheyava Falls: 18 July 2024, 0.98 by 0.61 m, Neretva Vallis, the veins and leopard spots, the core of 21 July
      called Sapphire Canyon, NASA's "potential biosignature" of 10 September 2025, vivianite and greigite and where
      they are found on the Earth, 3.5 billion years, and the need for sample return: Wikipedia,
      [Cheyava Falls](https://en.wikipedia.org/wiki/Cheyava_Falls) (weaker). That such minerals can form without life:
      standard. Perseverance at Jezero: book 11, chapter 11.

## 20.5 Life on other worlds, round the world { #history }

**Many worlds.**

- **India.** The scriptures of **Jainism** describe many worlds that support human life, among them Bharat Kshetra
  and Mahavideh Kshetra: the earliest known written claim of people living beyond our world.
- **Greece.** **Democritus** and **Epicurus** taught that there are countless worlds in a vast universe.
- **The Islamic world.** Medieval Muslim writers such as **Fakhr al-Din al-Razi** and **Muhammad al-Baqir** argued
  from the Qur'an for many worlds.
- **Europe.** In 1440 **Nicholas of Cusa** called the Earth a "brilliant star" and thought that every body in
  the sky, even the Sun, could have life, and in the 16th century the
  Italian philosopher **Giordano Bruno** argued that every star has its own planets, with "animals and inhabitants".

**Life on Mars.**

- **1877 to 1906.** Giovanni Schiaparelli mapped *canali*, channels, on Mars, and the American astronomer
  **Percival Lowell** argued in books of 1895 and 1906 that they were canals built by Martians. They turned out to be
  tricks of the eye (book 11, [chapter 17](../history/17-Herschel-and-the-Canals-of-Mars.md#lowell)).
- **The Soviet Union and Kazakhstan, 1940s and 1950s.** The Soviet astronomer **Gavriil Tikhov** stayed in Alma-Ata
  (now Almaty) after an eclipse trip in 1941, headed **astrobotany** there and studied whether there could be life on
  other worlds of the solar system. Tikhov is called the father of astrobotany.
- **1947 and 1963.** Gerard Kuiper found carbon dioxide in Mars's air in 1947. Water vapour was not found for sure
  until 1963, at Mount Wilson Observatory.

**The habitable zone.** In 1913 Edward Maunder used the words "habitable zone" in the book *Are the Planets
Inhabited?*. In 1953 Hubertus Strughold wrote of "zones" where life could arise, and Harlow Shapley of a "liquid
water belt". **Su-Shu Huang**, an American astrophysicist, worked out the modern idea in papers in the 1950s and 1960s.

**Searching by spacecraft.**

- **1976.** The Viking landers ran the first tests for life on another world (section 20.4).
- **2009.** Instruments on India's **Chandrayaan-1**, among them NASA's Moon Mineralogy Mapper, found water molecules
  spread through the Moon's soil (chapter 7).
- **2023.** Scientists announced that the samples Japan's **Hayabusa2** brought back from the asteroid Ryugu in 2020
  contain **uracil**, one of the four bases of RNA, and vitamin B3, as well as 20 different amino acids.
- **2022 to 2025.** China's Zhurong found signs of an old ocean, and Perseverance found Cheyava Falls.

??? note "Sources"
    - Jain scriptures and the worlds named, "the earliest recorded assertion of extraterrestrial human life",
      Democritus and Epicurus, al-Razi and al-Baqir, Nicholas of Cusa in 1440 ("brilliant star"), and Bruno ("Italian
      philosopher", with the quotation): Wikipedia,
      [Extraterrestrial life](https://en.wikipedia.org/wiki/Extraterrestrial_life) (weaker).
    - Lowell ("American astronomer") and the books of 1895 and 1906: Wikipedia, Life on Mars (above). Schiaparelli
      and the canals: book 11, chapter 17.
    - Tikhov ("Soviet astronomer", "father of astrobotany", the 1941 eclipse trip, head of astrobotany in Alma-Ata,
      studying life on other bodies of the solar system): Wikipedia,
      [Gavriil Tikhov](https://en.wikipedia.org/wiki/Gavriil_Adrianovich_Tikhov) (weaker). The 1940s and 1950s:
      our reading of the move to Alma-Ata in 1941 and Tikhov's death in 1960.
    - Kuiper's carbon dioxide in 1947 and water vapour at Mount Wilson in 1963: Wikipedia, Water on Mars (above).
    - Maunder in 1913, Strughold and Shapley in 1953, and Huang ("American astrophysicist"): Wikipedia, Circumstellar
      habitable zone (above).
    - Chandrayaan-1 finding water molecules in the soil: Wikipedia,
      [Chandrayaan-1](https://en.wikipedia.org/wiki/Chandrayaan-1) (weaker); the date: chapter 7.
    - Ryugu's samples returned on 5 December 2020, the 20 amino acids, and uracil and vitamin B3 announced in March
      2023: Wikipedia, [162173 Ryugu](https://en.wikipedia.org/wiki/162173_Ryugu) (weaker). Uracil as one of the
      four bases of RNA: the same page.

## 20.6 Going to look { #missions }

- **Europa Clipper** (NASA) was launched on 14 October 2024. It swings past the Earth on 3 December 2026, is due to
  go into orbit round Jupiter in **April 2030**, and is to fly past Europa again and again from March 2031, to study
  its ice and the ocean below.
- **JUICE** (Europe) is due at Jupiter in July 2031 and is to end in orbit round Ganymede (chapter 15,
  [section 15.6](15-Moons-of-the-Giants.md#missions)).
- **Dragonfly** (NASA) is to be launched in July 2028 and reach Titan in 2034, to fly from place to place and study
  its chemistry (chapter 19, [section 19.6](19-Air-Magnetism-and-Weather.md#missions)).
- **Rosalind Franklin** (Europe) is a rover built to look for signs of past or present life, with a drill that
  reaches **2 m** down, below the reach of the radiation that breaks organic molecules at the surface. It is due to
  be launched in 2028 and land in 2030.
- **Tianwen-3** (China) is planned to use the Mars launch window of December 2028 to January 2029, with two rockets,
  and to bring about **500 g** of Mars back to the Earth by 2031. It would be the first sample ever returned from
  Mars.
- **MMX** (Japan) was launched on 19 October 2026 and is due in Mars orbit in August 2027, to bring back samples from
  Phobos in 2031.
- **Mars Sample Return**, the joint NASA and European plan to collect Perseverance's cores, was cancelled by the
  United States in 2026, so Sapphire Canyon has no ride home yet.

??? note "Sources"
    - Europa Clipper: launch on 14 October 2024, Earth flyby on 3 December 2026, Jupiter orbit in April 2030 and
      Europa flybys from March 2031: Wikipedia, [Europa Clipper](https://en.wikipedia.org/wiki/Europa_Clipper)
      (weaker). JUICE: chapter 15. Dragonfly: chapter 19, with "prebiotic chemistry" from the page cited there.
    - Rosalind Franklin's aim, its 2 m drill, launch in 2028 and landing in 2030: Wikipedia,
      [Rosalind Franklin](https://en.wikipedia.org/wiki/Rosalind_Franklin_(rover)) (weaker). Radiation breaking
      organics near the surface: standard.
    - Tianwen-3's window, two launches, 500 g, return by 2031 and "first Mars sample return": Wikipedia,
      [Tianwen-3](https://en.wikipedia.org/wiki/Tianwen-3) (weaker).
    - MMX's launch on 19 October 2026, Mars orbit in August 2027 and samples in 2031: Wikipedia,
      [Martian Moons eXploration](https://en.wikipedia.org/wiki/Martian_Moons_eXploration) (weaker).
    - Mars Sample Return "cancelled by the US in 2026": Wikipedia,
      [Mars sample-return mission](https://en.wikipedia.org/wiki/Mars_sample-return_mission) (weaker).

## 20.7 Mars beside Europa, Enceladus and Titan { #mars }

| | Mars | Europa | Enceladus | Titan |
|---|---|---|---|---|
| Distance from the Sun | 1.52 AU | 5.20 AU | 9.54 AU | 9.54 AU |
| Where the water is | ice caps and ground ice | ocean under ice | ocean under ice | ocean under ice |
| Liquid water now | perhaps, 10 to 20 km down | very likely | very likely | very likely |
| What keeps it warm | sunlight, and heat inside | tides from Jupiter | tides from Saturn | tides from Saturn |
| Organic matter found | yes, in rocks | not yet | yes, in the spray | yes, in the air and lakes |
| How we can sample it | rovers, and samples to bring home | flybys | flying through the spray | Dragonfly, from 2034 |

**Mars: the best record of the past.** Mars had lakes and rivers more than 3.7 billion years ago, and its old rocks
still lie at the surface where rovers can reach them.
If life ever started on Mars, its traces may be waiting in rocks like Cheyava Falls. But today's surface is cold,
dry, and bathed in radiation and perchlorate; any life now would have to be deep underground.

**The ocean moons: the best chance of life today.** Europa's and Enceladus's oceans are liquid now, and they touch
rock at their floors, where water and rock can react and release chemical energy, as at vents on the Earth's sea
floor. Enceladus makes it easy: its spray carries samples of the ocean up into space, where a spacecraft can fly
through it. Titan has two places to look: the water ocean deep down, and lakes of methane at the surface, where any
life would have to be very different from ours.

??? note "Sources"
    - Distances: NASA fact sheets (chapter 19). Water, oceans and tides: sections 20.2 and 20.3, and chapter 15.
      Organic matter: Cheyava Falls (above), Enceladus (above), and Titan's haze and lakes in chapter 15.
    - Lakes and rivers more than 3.7 billion years ago: section 20.3 and chapter 8.
    - Enceladus's ocean touching its rocky core: Wikipedia, Enceladus (above). Europa's ocean touching rock,
      water–rock reactions releasing energy, and vents on the Earth's sea floor: standard. Perchlorate: section 20.4.
      Radiation on the surface: chapter 18. "Very different from ours": our reasoning.

## 20.8 Working it out { #working }

**Mars's ice as a sea.** Mars's surface area is $4\pi \times 3{,}389.5^2 = 1.44 \times 10^8$ km². The two polar caps,
$3.2 \times 10^6$ km³, would spread to a layer $3.2 \times 10^6/1.44 \times 10^8 = 0.022$ km, **22 m** deep. All the
ice near the surface, $5 \times 10^6$ km³, gives 35 m, as section 20.3 says. The Earth's water would cover the Earth
2.7 km deep (chapter 6), about 80 times as deep.

**Sunlight in the zone.** At 1 AU the Sun gives 1,361 W per square metre. Sunlight falls as $1/d^2$, so at the
edges of the zone in 20.1 it is $1{,}361/0.84^2 = 1{,}930$ W/m² and $1{,}361/1.7^2 = 471$ W/m². Mars, at 1.524 AU,
gets $1{,}361/1.524^2 = 586$ W/m², inside that range.

**Enceladus's spray.** At 200 kg a second, Enceladus throws out $200 \times 3.156 \times 10^7 = 6.3 \times 10^9$ kg a
year, a lake about 2.5 km long, 2.5 km wide and 1 m deep. Over 4.5 billion years that would be $2.8 \times 10^{19}$
kg, 26% of Enceladus's mass of $1.08 \times 10^{20}$ kg.

**Europa's ocean.** At 2 to 3 times the Earth's water, Europa's ocean holds 2.8 to $4.2 \times 10^{21}$ kg.

??? note "Sources"
    - Mars's radius, the solar constant and Mars's 586 W/m²: NASA fact sheets (chapter 19). The ice volumes: section
      20.3. The Earth's 2.7 km: chapter 6.
    - Enceladus's 200 kg/s, and its mass of 1.080 × 10²⁰ kg: Wikipedia, Enceladus (above), which says the loss over
      4.5 billion years would be about 30% of its first mass.
    - All the sums: our arithmetic.

## 20.9 Can water flow on Mars today? { #derive }

Liquid water needs two things at once: the temperature must be above freezing, and the air pressure must be higher
than the pressure at which water boils at that temperature. The second rule is why water boils at a lower
temperature high on a mountain.

**The boiling curve.** As water warms, more of its molecules have enough energy to escape, so the pressure needed to
keep it from boiling, its **vapour pressure** $p$, rises steeply. The Clausius–Clapeyron equation says how:

$$\frac{dp}{dT} = \frac{L p}{R_v T^2}$$

where $L = 2.50 \times 10^6$ J/kg is the heat needed to turn a kilogram of water into vapour, and $R_v = 8.314/0.018015
= 461.5$ J/(kg·K) is the gas constant for a kilogram of water vapour. Dividing by $p$ and adding up from the **triple
point**, where ice, water and vapour can all exist together at $p_0 = 611.657$ Pa and $T_0 = 273.16$ K, gives

$$p(T) = p_0 \exp\left[\frac{L}{R_v}\left(\frac{1}{T_0} - \frac{1}{T}\right)\right]$$

with $L/R_v = 5{,}417$ K.

**Checking it.** At 25 °C, $T = 298.15$ K: $5{,}417 \times (1/273.16 - 1/298.15) = 1.662$, and $p = 611.657 \times
e^{1.662} = 3{,}220$ Pa. The measured value is 3,170 Pa, so the formula is good to about 2% near room temperature. It
is rougher further out: it puts the boiling point at 1 bar at 95 °C instead of 100 °C, because $L$ gets a little
smaller as water gets hotter.

**Turning it round.** For a given air pressure $p$, water boils at

$$T_b = \left[\frac{1}{T_0} - \frac{R_v}{L}\ln\frac{p}{p_0}\right]^{-1}$$

**On Mars.** At the average pressure, $p = 636$ Pa: $\ln(636/611.657) = 0.039$, and $T_b = 273.70$ K, **0.5 °C**.
So at the average pressure, water is liquid only between 0 °C and half a degree above it. At the highest seasonal
pressure, 870 Pa, $T_b = 278.1$ K, about 5 °C. Where the pressure is below 611.657 Pa, water cannot be liquid at any
temperature: ice turns straight into vapour.

**How thick would the air need to be?** At Vladilo's 15 mb (section 20.1), $T_b = 286.1$ K, 13 °C. For water to stay
liquid up to 25 °C, the air must press with at least 3,220 Pa, 32 mb: five times Mars's average today. The thicker
air of Mars's past (chapter 19, [section 19.7](19-Air-Magnetism-and-Weather.md#mars)) would have made all the
difference.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Temperature from minus 20 to 40 degrees Celsius across, air pressure from 1 to 100 millibars up, on a scale where each step is ten times the last. A curve rising to the right shows the pressure at which water boils at each temperature; a vertical line at 0 degrees shows where it freezes. Water can be liquid only above the curve and to the right of the line. The two meet at the triple point, 6.1 millibars and 0.01 degrees. A band from 4.0 to 8.7 millibars shows Mars's air pressure through the year: at Mars's average of 6.36 millibars, water is liquid only between 0 and about half a degree. A dashed line at 15 millibars gives liquid water from 0 to about 13 degrees.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">When can water be liquid? Mars sits right at the edge</text>
    <line x1="52.0" y1="190.0" x2="318.0" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="48.0" y="193.0" text-anchor="end">1</text>
    <line x1="52.0" y1="150.4" x2="318.0" y2="150.4" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="48.0" y="153.4" text-anchor="end">3</text>
    <line x1="52.0" y1="107.0" x2="318.0" y2="107.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="48.0" y="110.0" text-anchor="end">10</text>
    <line x1="52.0" y1="67.4" x2="318.0" y2="67.4" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="48.0" y="70.4" text-anchor="end">30</text>
    <line x1="52.0" y1="24.0" x2="318.0" y2="24.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="48.0" y="27.0" text-anchor="end">100</text>
    <line x1="52.0" y1="24.0" x2="52.0" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="52.0" y="200.0" text-anchor="middle">-20</text>
    <line x1="96.3" y1="24.0" x2="96.3" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="96.3" y="200.0" text-anchor="middle">-10</text>
    <line x1="140.7" y1="24.0" x2="140.7" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="140.7" y="200.0" text-anchor="middle">0</text>
    <line x1="185.0" y1="24.0" x2="185.0" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="185.0" y="200.0" text-anchor="middle">10</text>
    <line x1="229.3" y1="24.0" x2="229.3" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="229.3" y="200.0" text-anchor="middle">20</text>
    <line x1="273.7" y1="24.0" x2="273.7" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="273.7" y="200.0" text-anchor="middle">30</text>
    <line x1="318.0" y1="24.0" x2="318.0" y2="190.0" stroke="#cfc8bf" stroke-width="0.6"/>
    <text x="318.0" y="200.0" text-anchor="middle">40</text>
    <text x="185.0" y="210.0" text-anchor="middle">temperature (°C)</text>
    <text x="6" y="28.0">mb</text>
    <polygon points="140.7,24.0 140.7,124.7 140.7,124.7 142.9,123.4 145.1,122.1 147.4,120.8 149.6,119.5 151.8,118.2 154.0,117.0 156.2,115.7 158.4,114.4 160.7,113.1 162.9,111.9 165.1,110.6 167.3,109.4 169.5,108.1 171.7,106.9 174.0,105.6 176.2,104.4 178.4,103.1 180.6,101.9 182.8,100.7 185.0,99.5 187.3,98.3 189.5,97.0 191.7,95.8 193.9,94.6 196.1,93.4 198.3,92.2 200.6,91.1 202.8,89.9 205.0,88.7 207.2,87.5 209.4,86.3 211.6,85.2 213.9,84.0 216.1,82.8 218.3,81.7 220.5,80.5 222.7,79.4 224.9,78.2 227.2,77.1 229.4,76.0 231.6,74.8 233.8,73.7 236.0,72.6 238.2,71.4 240.5,70.3 242.7,69.2 244.9,68.1 247.1,67.0 249.3,65.9 251.5,64.8 253.8,63.7 256.0,62.6 258.2,61.5 260.4,60.4 262.6,59.3 264.8,58.3 267.1,57.2 269.3,56.1 271.5,55.0 273.7,54.0 275.9,52.9 278.1,51.9 280.4,50.8 282.6,49.8 284.8,48.7 287.0,47.7 289.2,46.6 291.4,45.6 293.7,44.6 295.9,43.5 298.1,42.5 300.3,41.5 302.5,40.5 304.7,39.4 307.0,38.4 309.2,37.4 311.4,36.4 313.6,35.4 315.8,34.4 318.0,33.4 318.0,24.0" fill="#5aa0d8" opacity="0.25"/>
    <polyline points="52.0,188.8 54.2,187.0 56.4,185.3 58.6,183.6 60.9,181.9 63.1,180.2 65.3,178.5 67.5,176.8 69.7,175.2 72.0,173.5 74.2,171.8 76.4,170.2 78.6,168.5 80.8,166.9 83.0,165.2 85.2,163.6 87.5,162.0 89.7,160.4 91.9,158.8 94.1,157.1 96.3,155.5 98.5,153.9 100.8,152.4 103.0,150.8 105.2,149.2 107.4,147.6 109.6,146.1 111.8,144.5 114.1,142.9 116.3,141.4 118.5,139.9 120.7,138.3 122.9,136.8 125.2,135.3 127.4,133.7 129.6,132.2 131.8,130.7 134.0,129.2 136.2,127.7 138.4,126.2 140.7,124.7 142.9,123.4 145.1,122.1 147.3,120.8 149.5,119.5 151.8,118.3 154.0,117.0 156.2,115.7 158.4,114.4 160.6,113.2 162.8,111.9 165.1,110.6 167.3,109.4 169.5,108.1 171.7,106.9 173.9,105.6 176.1,104.4 178.3,103.2 180.6,101.9 182.8,100.7 185.0,99.5 187.2,98.3 189.4,97.1 191.7,95.9 193.9,94.7 196.1,93.5 198.3,92.3 200.5,91.1 202.7,89.9 204.9,88.7 207.2,87.5 209.4,86.4 211.6,85.2 213.8,84.0 216.0,82.9 218.2,81.7 220.5,80.6 222.7,79.4 224.9,78.3 227.1,77.1 229.3,76.0 231.6,74.8 233.8,73.7 236.0,72.6 238.2,71.5 240.4,70.3 242.6,69.2 244.8,68.1 247.1,67.0 249.3,65.9 251.5,64.8 253.7,63.7 255.9,62.6 258.1,61.5 260.4,60.4 262.6,59.4 264.8,58.3 267.0,57.2 269.2,56.1 271.4,55.1 273.7,54.0 275.9,52.9 278.1,51.9 280.3,50.8 282.5,49.8 284.8,48.7 287.0,47.7 289.2,46.7 291.4,45.6 293.6,44.6 295.8,43.6 298.1,42.5 300.3,41.5 302.5,40.5 304.7,39.5 306.9,38.5 309.1,37.4 311.3,36.4 313.6,35.4 315.8,34.4 318.0,33.4" fill="none" stroke="#5aa0d8" stroke-width="1.6"/>
    <line x1="140.7" y1="24.0" x2="140.7" y2="124.7" stroke="#5aa0d8" stroke-width="1.6"/>
    <rect x="52.0" y="112.0" width="266.0" height="28.0" fill="#c1440e" opacity="0.25"/>
    <line x1="52.0" y1="123.3" x2="318.0" y2="123.3" stroke="#c1440e" stroke-width="1.2"/>
    <text x="202.7" y="137.3" fill="#c1440e">Mars, 4.0 to 8.7 mb</text>
    <line x1="52.0" y1="92.4" x2="318.0" y2="92.4" stroke="#555" stroke-width="0.8" stroke-dasharray="3 2"/>
    <text x="56.4" y="89.4" fill="#555">15 mb</text>
    <circle cx="140.7" cy="124.7" r="2.4" fill="currentColor"/>
    <text x="134.0" y="135.7" text-anchor="end">triple point</text>
    <text x="238.2" y="42.4">liquid</text>
    <text x="74.2" y="67.4">ice</text>
    <text x="264.8" y="165.0">vapour</text>
    <text x="6" y="226">Shaded blue: water can be liquid. The curve is where it boils (or, below 0 °C, where ice turns</text>
    <text x="6" y="235">to vapour), from section 20.9. At Mars's average 6.36 mb, water is liquid only from 0 °C to</text>
    <text x="6" y="244">about 0.5 °C; at the seasonal top, 8.7 mb, to about 5 °C. Air of 15 mb would allow up to 13 °C.</text>
  </g>
</svg>
</div>

Salt makes Mars a little kinder: it lowers the freezing point, so brines can stay liquid below 0 °C. Dry air makes
it harsher: in Mars's thin, dry air, water evaporates fast even below its boiling point. Either way, open water
does not last.

??? note "Sources"
    - The Clausius–Clapeyron equation, the heat of vaporisation of about 2.50 × 10⁶ J/kg near 0 °C, the gas constant,
      the molar mass of water (18.015 g), the triple point (611.657 Pa, 273.16 K), the vapour pressure of 3,170 Pa at
      25 °C, and $L$ falling as water warms: standard. Below the triple point the figure uses the heat for ice turning
      to vapour, 2.834 × 10⁶ J/kg: standard.
    - Mars's 636 and 870 Pa: NASA, Mars fact sheet (chapter 19). Vladilo's 15 mb: section 20.1.
    - Salt lowering the freezing point, and evaporation into dry air: standard.
    - All the sums: our arithmetic.

## Check yourself { #check }

**1.** (beginner) What three things does life as we know it need?

??? note "Answer"
    Liquid water, a source of energy, and the right ingredients: carbon, hydrogen, nitrogen, oxygen, phosphorus and
    sulphur.

**2.** (beginner) Name three worlds other than the Earth that very likely have liquid water now, and say where it is.

??? note "Answer"
    Any three of Europa, Ganymede, Callisto, Enceladus and Titan. In each, the water is an ocean under a crust of ice.

**3.** (beginner) What did Perseverance find at Cheyava Falls, and why is it not proof of life?

??? note "Answer"
    A rock with organic carbon and small "leopard spots" holding iron minerals, vivianite and greigite. On the Earth
    these are often linked with decaying organic matter or microbes, but they can also form without life, and only
    laboratory tests on samples brought to the Earth can tell which.

**4.** (intermediate) The Viking labelled release experiment gave a positive result on both landers. Why did most
scientists conclude that Viking had not found life?

??? note "Answer"
    Another instrument found no organic molecules in the soil, and the gas could be explained by chemistry in the
    soil. Later, Phoenix found perchlorate, which may have destroyed organic matter when Viking heated its samples, so
    the question is not fully closed.

**5.** (intermediate) Why is the habitable zone not the whole story when we look for liquid water?

??? note "Answer"
    A world in the zone also needs air thick enough, above about 15 mb, for water to stay liquid; Mars is in some
    estimates of the zone but its air is too thin. And worlds far outside it, like Europa and Enceladus, have oceans
    under their ice, warmed from inside by tides.

**6.** (intermediate) Mars's polar caps hold about 3.2 million km³ of ice. If it melted and spread evenly over Mars,
how deep would it be?

??? note "Answer"
    Mars's area is $4\pi \times 3{,}389.5^2 = 1.44 \times 10^8$ km², so the depth is $3.2 \times 10^6/1.44 \times
    10^8 = 0.022$ km, about 22 m.

**7.** (advanced) Enceladus throws out about 200 kg a second. Check that over 4.5 billion years this would be about a
quarter of its mass, $1.08 \times 10^{20}$ kg.

??? note "Answer"
    $200 \times 4.5 \times 10^9 \times 3.156 \times 10^7 = 2.8 \times 10^{19}$ kg, and $2.8 \times 10^{19}/1.08
    \times 10^{20} = 0.26$, about a quarter.

**8.** (expert) Using the formula of section 20.9, what air pressure would keep water liquid up to 10 °C?

??? note "Answer"
    $T = 283.15$ K: $5{,}417 \times (1/273.16 - 1/283.15) = 0.700$, and $p = 611.657 \times e^{0.700} = 1{,}230$
    Pa, about 12 mb: nearly twice Mars's average.

## Summary

- Life as we know it needs liquid water, energy and the right ingredients; liquid water is the hard part.
- The habitable zone, where sunlight could keep water liquid on a surface, is perhaps 0.84 to 1.7 AU for the Sun,
  but a planet also needs air thicker than about 15 mb.
- Only the Earth has open water. Mars, Mercury and the Moon have ice, and Europa, Ganymede, Callisto, Enceladus and
  Titan very likely have oceans under their ice.
- Mars once had rivers, lakes and perhaps an ocean. Now most of its water is ice, enough to cover it 35 m deep, with
  perhaps liquid water 10 to 20 km down.
- Viking's tests in 1976 were not clear, ALH84001 in 1996 was not accepted, and the Cheyava Falls rock of 2024 is a
  "potential biosignature" that needs testing on the Earth.
- Ideas of life on other worlds go back to the Jain scriptures, Greece and medieval Muslim writers; the search by
  spacecraft now involves NASA, Europe, India, Japan and China.
- Europa Clipper, JUICE, Dragonfly, Rosalind Franklin, Tianwen-3 and MMX are on their way or being built.
- At Mars's average pressure, water can be liquid only between 0 and 0.5 °C; it would need air five times thicker to
  stay liquid up to 25 °C.

**Next:** this is the last chapter. Go back to the [contents](index.md#contents) to read it in another order, or see
how people all over the world came to understand the planets in the [history of astronomy](../history/index.md).

## Further reading

- Sarah Stewart Johnson, *The Sirens of Mars: Searching for Life on Another World*, Crown, New York, 2020. A
  planetary scientist who worked on Spirit, Opportunity and Curiosity tells the story of the search for life on
  Mars, from the canals to the rovers.
