# 9. Telling time by the sky

*Long before watches, the sky was the clock and the calendar. A shadow told the hour by day, the stars told it by night,
the Moon counted the months and the Sun counted the year. This chapter shows how to read those clocks yourself: a
stick in the ground, the Big Dipper turning round Polaris, and the Moon and stars that mark the months. It explains why
a sundial and a watch disagree, why calendars need leap days, and how people working with rovers keep time on Mars.
It ends with the equation of time, the reason the Sun itself runs fast and slow.*

!!! abstract "In this chapter"
    **You will learn:**

    - how to tell the time from a shadow
    - why sundial time and clock time differ, and where time zones came from
    - why the stars keep a different time from the Sun
    - how to read the Big Dipper as a clock
    - how the day, the month and the year are fitted into calendars
    - how people keep time on Mars
    - why the Sun runs up to a quarter of an hour fast or slow

    **You need:** chapters 6 and 8.

    **Levels:** 9.1 to 9.4 are beginner; 9.5 to 9.7 are intermediate; 9.8 is advanced; 9.9 is expert.

## 9.1 A stick in the ground { #shadow }

Push a straight stick upright into the ground on a sunny morning. Its shadow points away from the Sun, so as the Sun
crosses the sky the shadow swings round: it points west in the morning and east in the afternoon. The stick is called
a **gnomon**.

Mark the tip of the shadow every half hour. The shadow is shortest when the Sun is highest, as it crosses the meridian
due south (chapter 6). That moment is **local noon**, or 12:00 local apparent time. In Canada, Europe or anywhere north
of the tropics, the shortest shadow points due north.

The Sun goes round the sky once in 24 hours, so it moves 15° each hour. A real sundial uses this. Its shadow edge,
the **style**, must be parallel to the Earth's axis, pointing at the celestial pole, so it leans at an angle equal to
your latitude. Then the dial reads correctly all year round.

Sundials are very old. The earliest known are shadow clocks from Egypt and Babylon, from about 1500 BC (this site's
history book, [chapter 3, section 3.6](../history/03-Egypt.md#clocks)).

??? note "Sources"
    - The sundial's gnomon and style, the style parallel to the Earth's axis at an angle equal to the latitude, and the
      earliest shadow clocks from Egyptian and Babylonian astronomy about 1500 BC: Wikipedia,
      [Sundial](https://en.wikipedia.org/wiki/Sundial) (weaker). The Egyptian sundial: this site's history book,
      chapter 3, section 3.6.
    - Local apparent noon as 12:00 local apparent time: Wikipedia,
      [Solar time](https://en.wikipedia.org/wiki/Solar_time) (weaker).
    - 15° an hour is 360° in 24 hours. The shadow pointing north at noon north of the tropics follows from chapter 8,
      section 8.5: there the Sun is always south of overhead at noon.

## 9.2 Sundial time and clock time { #zones }

Check a sundial against your watch and they will rarely agree. There are three reasons.

**1. Where you are in your time zone.** The Sun crosses the meridian 4 minutes later for every degree you go west,
since 360° takes 24 hours. Until the 1800s most towns kept their own Sun time, so noon in one town was a few minutes off
noon in the next. Railways made that a nuisance.

- From November 1840 the Great Western Railway in Britain ran on Greenwich Mean Time, carried along the line by
  chronometers. Other British railways followed: "railway time".
- In 1876 the Scottish-born Canadian **Sandford Fleming** proposed dividing the world into 24 time zones,
  each 15° of longitude wide, with clocks in neighbouring zones one hour apart.
- North American railways switched to standard time zones on 18 November 1883, "the Day of Two Noons", when station
  clocks were reset as standard noon arrived in each zone.

Inside a zone, every clock shows the same time, so the Sun crosses the meridian at 12:00 only near the middle of the
zone. Some countries stretch a zone much further: China and India each use one time zone across land far wider than
15°, and Spain and France keep the time of 15°E although the Greenwich meridian runs through them.

**2. Daylight saving time.** In spring and summer many places put the clocks forward an hour, so the Sun crosses the
meridian around 1 pm.

**3. The Sun runs fast and slow.** Even at the middle of a zone, with no daylight saving, a sundial is up to 16½
minutes ahead of the clock in early November and 14 minutes behind in February. This is the **equation of time**
(section 9.9).

??? note "Sources"
    - GMT, the Great Western Railway in November 1840 and railway time, Fleming's proposal of 1876 for 24 zones of 15°
      one hour apart, the Day of Two Noons on 18 November 1883, China and India using a single zone, Spain and France
      on 15°E time, and daylight saving time adding an hour in spring and summer: Wikipedia,
      [Time zone](https://en.wikipedia.org/wiki/Time_zone) (weaker).
    - The equation of time, 16 min 33 s around 3 November and 14 min 6 s around 11 February: Wikipedia,
      [Equation of time](https://en.wikipedia.org/wiki/Equation_of_time) (weaker).
    - 4 minutes a degree is 24 hours ÷ 360°.

## 9.3 Star time { #stars }

Chapter 6, section 6.5, showed that a star comes back to the same place every **23 hours 56 minutes 4 seconds**, not
every 24 hours. Figure A shows why.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The Sun at the top and the Earth at two places on its orbit below, one day apart, with the distance moved greatly exaggerated. At the first place it is noon for an observer: an arrow pointing straight up from the observer points at the Sun, and also at a very distant star in the same direction. After the Earth has turned once, 23 hours 56 minutes later, the Earth has moved along its orbit; the observer's arrow points in the same direction as before, at the distant star, but no longer at the Sun. The Earth must turn a little more, about 4 minutes, before the arrow points at the Sun again and it is noon: 24 hours.">
  <path d="M 123.6 172.7 A 150 150 0 0 0 247.3 158.6" fill="none" stroke="currentColor" stroke-width="0.7" stroke-dasharray="3 3"/>
  <circle cx="170" cy="30" r="14" fill="#eea66f"/>
  <circle cx="170.0" cy="180.0" r="16" fill="#5aa0d8"/>
  <circle cx="233.4" cy="165.9" r="16" fill="#5aa0d8"/>
  <line x1="170" y1="180" x2="170" y2="150" stroke="#c1440e" stroke-width="1.6"/>
  <line x1="170" y1="150" x2="170" y2="46" stroke="#c1440e" stroke-width="0.6" stroke-dasharray="2 3"/>
  <line x1="233.4" y1="165.9" x2="233.4" y2="135.9" stroke="currentColor" stroke-width="1.6"/>
  <line x1="233.4" y1="135.9" x2="233.4" y2="14" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 3"/>
  <line x1="233.4" y1="165.9" x2="220.7" y2="138.8" stroke="#c1440e" stroke-width="1.6"/>
  <line x1="220.7" y1="138.8" x2="176.3" y2="43.6" stroke="#c1440e" stroke-width="0.6" stroke-dasharray="2 3"/>
  <path d="M 233.4 143.9 A 22 22 0 0 0 224.1 146.0" fill="none" stroke="currentColor" stroke-width="0.8"/>
  <polygon points="233.4,8 230.4,14 236.4,14" fill="currentColor"/>
  <g font-size="8" fill="currentColor">
    <text x="239.4" y="14">far star</text>
    <text x="239.4" y="24">(much farther away)</text>
    <text x="170" y="33" text-anchor="middle" fill="#222">Sun</text>
    <text x="170" y="208" text-anchor="middle">Day 1, noon: Sun and</text>
    <text x="170" y="218" text-anchor="middle">far star straight up</text>
    <text x="255.4" y="155.9">one turn, 23 h 56 min:</text>
    <text x="255.4" y="165.9">far star straight up</text>
    <text x="255.4" y="179.9" fill="#c1440e">4 min more, 24 h:</text>
    <text x="255.4" y="189.9" fill="#c1440e">Sun straight up</text>
    <text x="8" y="246">Not to scale: the Earth really moves about 1° along its orbit in a day.</text>
  </g>
</svg>
</div>

*Figure A. After one turn the Earth faces the same far star again, but it has moved along its orbit, so it must turn
about 1° more, about 4 minutes, to face the Sun.*

So there are two kinds of day:

- the **solar day**, noon to noon, 24 hours on average, which our clocks keep;
- the **sidereal day**, one turn against the stars, 23 h 56 min 4 s.

In a year the Earth turns about 366¼ times against the stars, but sees the Sun cross the meridian only 365¼ times. One
turn is "used up" by going once round the Sun.

Astronomers keep **sidereal time** as well as ordinary time. Local sidereal time tells you which part of the sky is
crossing your meridian, and so which stars are best placed. Chapter 17 shows how to use it with a star's position.

The Egyptians made star clocks for the night from this. They chose 36 stars, the **decans**, that rose one after
another, and moved their list on by one every ten days, as the stars rose 40 minutes earlier (history book,
[chapter 3, section 3.4](../history/03-Egypt.md#decans)).

??? note "Sources"
    - The sidereal day of 23 h 56 min 4.0905 s and the mean solar day nearly 4 minutes longer: Wikipedia,
      [Sidereal day](https://en.wikipedia.org/wiki/Sidereal_day) (weaker).
    - Sidereal time as the angle from the observer's meridian to the March equinox, used with stars' right ascension
      to time their meridian crossings: Wikipedia, [Sidereal time](https://en.wikipedia.org/wiki/Sidereal_time)
      (weaker).
    - The 366¼ turns are worked out in section 9.8. The decans: this site's history book, chapter 3, section 3.4.

## 9.4 The Big Dipper clock { #dipper }

The Big Dipper goes round Polaris once each sidereal day, anticlockwise as you face north (chapter 6, section 6.1). So
it makes a clock hand, with Polaris as the centre of the dial. The hand is the line from Polaris through the two
**pointer stars**, Merak and Dubhe, at the end of the Dipper's bowl.

It turns 15° an hour: a quarter turn in 6 hours, half a turn in 12. Here is a simple rule for reading it.

1. **Around 20 March**, the pointers are **straight above Polaris** at about **11 pm** local Sun time.
2. For each month after 20 March, that moment comes **2 hours earlier**: about 9 pm on 20 April, 7 pm on 20 May, and so
   on round the year.
3. From that moment, the pointers move **anticlockwise**, to the left, by 15° each hour.

So at 11 pm, the pointers are above Polaris in March, to its left in June, below it in September and to its right in
December. To turn local Sun time into clock time, add an hour for daylight saving and allow for where you are in your
time zone and for the equation of time (section 9.2). Judging the angle by eye to the nearest 15° gives the time to
within about half an hour.

An old instrument, the **nocturnal**, does this sum. It has an outer disc marked with the months, an inner disc marked
with the hours, and an arm turning on the same centre. You sight Polaris through a hole in the centre, turn the arm to
line up with the pointer stars or with Kochab in the Little Dipper, and read the time.

??? note "Sources"
    - Dubhe at right ascension 11 h 03.7 min and Merak at 11 h 01.8 min: Wikipedia,
      [Dubhe](https://en.wikipedia.org/wiki/Dubhe) and [Merak](https://en.wikipedia.org/wiki/Merak_(star)) (weaker).
      The rule is worked out from these in section 9.8.
    - The nocturnal, its discs and pointer, Polaris sighted through the centre, a fixed star going round the pole star
      in 23 hours 56 minutes as an hour hand, and the Big Dipper's pointers or Kochab as reference stars: Wikipedia,
      [Nocturnal (instrument)](https://en.wikipedia.org/wiki/Nocturnal_(instrument)) (weaker).
    - "Within about half an hour" is half of a 15°, one-hour step.

## 9.5 Day, month and year { #calendars }

The sky gives three natural units of time:

- the **day**, from the Earth's turning;
- the **month**, from the Moon's phases: 29.53 days from new Moon to new Moon;
- the **year**, from the Sun's return to the same equinox: 365.2422 days, the **tropical year**.

The trouble is that they do not fit. Twelve months make 354.37 days, 11 days short of a year, and neither the month nor
the year is a whole number of days. Every calendar is a way of living with this, and there are three main kinds.

**Lunar calendars follow the Moon.** The Islamic calendar has 12 lunar months in a year of 354 or 355 days.
Traditionally each month begins with the first sighting of the thin crescent, the *hilal*, just after sunset, as in
ancient Babylon (history book, [chapter 2, section 2.2](../history/02-Mesopotamia.md#month)). It adds no extra months,
so it slips 10 to 11 days earlier against the seasons each year, and the month of fasting, **Ramadan**, moves through
all the seasons.

**Solar calendars follow the Sun.** The Gregorian calendar ignores the Moon. It has 365
days, plus a leap day every four years, except in century years that cannot be divided by 400: 1900 was not a leap
year, 2000 was. That gives 97 leap days every 400 years and an average year of 365.2425 days. Pope Gregory XIII brought
it in in October 1582, when Thursday 4 October was followed by Friday 15 October (history book,
[chapter 9, section 9.10](../history/09-Byzantium-and-Medieval-Europe.md#gregorian)). The Egyptians had kept a year of
exactly 365 days long before (history book, [chapter 3, section 3.2](../history/03-Egypt.md#year)).

**Lunisolar calendars follow both.** Their months follow the Moon, but now and then a 13th month is added to keep up
with the Sun. The Hebrew calendar adds a leap month in 7 out of every 19 years, because 235 months are almost exactly
19 years: the **Metonic cycle**, which Babylon also used (history book,
[chapter 2, section 2.8](../history/02-Mesopotamia.md#nineteen)). The Chinese calendar runs its months alongside the
24 solar terms (history book, [chapter 4, section 4.5](../history/04-China.md#calendar)).

??? note "Sources"
    - The synodic month of 29.53059 days: Wikipedia, [Lunar month](https://en.wikipedia.org/wiki/Lunar_month)
      (weaker).
    - The tropical year of 365.24219 days in 2000: Wikipedia,
      [Tropical year](https://en.wikipedia.org/wiki/Tropical_year) (weaker).
    - The Islamic calendar of 12 lunar months and 354 or 355 days, 354.37 days for 12 lunar months, and the hilal:
      Wikipedia, [Islamic calendar](https://en.wikipedia.org/wiki/Islamic_calendar) (weaker). The Islamic year 10 to 11
      days shorter than the solar year, and Ramadan moving through the seasons: Wikipedia,
      [Ramadan](https://en.wikipedia.org/wiki/Ramadan) (weaker).
    - The Gregorian leap-year rule, 97 leap days in 400 years, 365.2425 days, Gregory XIII, and 4 October followed by
      15 October 1582: Wikipedia, [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) (weaker).
    - Leap months in 7 of every 19 years in the Hebrew calendar: Wikipedia,
      [Hebrew calendar](https://en.wikipedia.org/wiki/Hebrew_calendar) (weaker). 235 synodic months and 19 tropical
      years: Wikipedia, [Metonic cycle](https://en.wikipedia.org/wiki/Metonic_cycle) (weaker).

## 9.6 The Moon and the stars together { #moonstars }

Many peoples fixed their months by watching the Moon beside the stars, or a star's first return at dawn (chapter 6,
section 6.5).

- The **Borana Oromo** of southern Ethiopia and northern Kenya keep a lunar-stellar calendar of 12 months of about
  29.5 days, 354 days in all. They find each month by watching which stars the Moon is seen beside; the year begins
  when the Moon is seen with Triangulum (history book, [chapter 10, section 10.3](../history/10-Africa.md#borana)).
- In the **Māori** calendar of Aotearoa New Zealand, the year begins with the dawn return of Matariki, the Pleiades,
  in late June or early July. Each later month was marked the same way, by a star first seen before dawn at the new
  Moon; the tenth month by Altair (history book,
  [chapter 12, section 12.5](../history/12-Oceania-and-Australia.md#matariki)).
- In the high **Andes** of Peru and Bolivia, Quechua and Aymara farmers look at the Pleiades before dawn around 24 June.
  If the cluster looks bright and big they plant potatoes on time; if dim, they plant later (history book,
  [chapter 11, section 11.6](../history/11-The-Americas.md#pleiades)).

These are calendars anyone can check by going outside: the sky itself says what time of year it is.

??? note "Sources"
    - The Borana, Māori and Andean calendars: this site's history book, chapter 10, section 10.3, chapter 12,
      section 12.5, and chapter 11, section 11.6, and their sources.

## 9.7 Time on Mars { #mars }

A day on Mars, a **sol**, lasts **24 h 39 min 35 s**, about 2.75% longer than an Earth day. One turn against the stars
takes 24 h 37 min 23 s.

**Mars time.** Rovers work by the Sun at their landing site, and Mars clocks split the sol into 24 "Mars hours" of
1 h 1 min 39 s each, so noon is always 12:00. For the Mars Pathfinder, Spirit and Opportunity, Phoenix and Curiosity
missions, the operations teams on Earth worked on "Mars time", keeping to the day at the landing site. Their working
day slid about 40 minutes later every day, round the clock and back again. Many team members wore wristwatches set to
Mars time.

**A Mars sundial runs badly.** Mars's orbit is far more stretched than ours, so the equation of time is much larger:
the Sun can be **51 minutes slow** or **40 minutes fast** against a steady Mars clock.

**A standard time.** Scientists have proposed a **Coordinated Mars Time**, the Mars version of Universal Time: the
mean solar time at Mars's prime meridian, which passes through the small crater Airy-0.

**Dates.** Scientists give the time of year on Mars as the angle Mars has gone round its orbit since the northward
equinox, and increasingly number the Mars years from the equinox of 11 April 1955. There are also proposed calendars.
In 1985 the engineer **Thomas Gangale** designed the **Darian calendar**, named after his son Darius, with 24 months
of 27 or 28 sols. Its year matches Mars's year of 668.59 sols by having six years of 669 sols and four of 668 in each
ten.

??? note "Sources"
    - The sol of 24 h 39 min 35.244 s, the sidereal day of 24 h 37 min 22.663 s, 2.75% longer, the Mars hour of 1 h 1
      min 39 s, the teams of Pathfinder, the Mars Exploration Rovers, Phoenix and Mars Science Laboratory on "Mars
      time", the schedule sliding about 40 minutes a day, Mars wristwatches, the Sun 51 minutes slow or 40 minutes
      fast, Coordinated Mars Time as mean solar time at the prime meridian, Airy-0, the time of year measured from the
      northward equinox, and Mars years numbered from 11 April 1955: Wikipedia,
      [Timekeeping on Mars](https://en.wikipedia.org/wiki/Timekeeping_on_Mars) (weaker).
    - The Darian calendar, Gangale, 1985, Darius, 24 months of 28 sols or 27 sols, 668.5907 sols, and six 669-sol and
      four 668-sol years each decade: Wikipedia, [Darian calendar](https://en.wikipedia.org/wiki/Darian_calendar)
      (weaker).

## 9.8 Working it out { #working }

**Sun and longitude.** The Sun moves $360^\circ / 24 = 15^\circ$ an hour, or $1^\circ$ in 4 minutes. A town at 80°W
in a zone set to the time of 75°W is $5^\circ$ west of the zone's centre, so the Sun crosses its meridian
$5 \times 4 = 20$ minutes after the zone's noon (before allowing for the equation of time).

**The sidereal day.** In one tropical year the Earth sees the Sun cross the meridian 365.2422 times, but turns once
more than that against the stars, because it has also gone once round the Sun. So

$$\text{sidereal day} = 24 \times \frac{365.2422}{366.2422}
= 23.9345 \text{ hours} = 23 \text{ h } 56 \text{ min } 4 \text{ s}.$$

For Mars, with 668.59 sols in a year:
$24 \text{ h } 39 \text{ min } 35.2 \text{ s} \times 668.59/669.59 = 24 \text{ h } 37 \text{ min } 22.7 \text{ s}$,
which agrees with the measured value.

**The Big Dipper rule.** A star is highest, crossing the meridian above the pole, when the local sidereal time equals
its right ascension. The pointers are at about 11 h, so they stand above Polaris at sidereal time 11 h. On the March
equinox the Sun is at right ascension 0 h, so sidereal time is 12 hours ahead of Sun time, and 11 h sidereal comes at
11 pm. Each day the stars gain about 4 minutes, which is 2 hours a month, so the moment comes 2 hours earlier each
month.

**Calendars.**

- Gregorian: $365 + 97/400 = 365.2425$ days, against 365.24219. The error is 0.00031 days a year, about one day in
  3,200 years.
- Lunar: $12 \times 29.5306 = 354.37$ days, $10.87$ days short of the year. A lunar calendar goes once round the
  seasons in about $365.24 / 10.87 \approx 34$ of its own years, about 33 solar years.
- Metonic: $235 \times 29.5306 = 6939.69$ days and $19 \times 365.2422 = 6939.60$ days, only about 2 hours apart.

| | Mars | Earth |
| --- | --- | --- |
| Solar day | 24 h 39 min 35 s | 24 h 00 min |
| Sidereal day | 24 h 37 min 23 s | 23 h 56 min 4 s |
| Stars rise earlier each day by | 2 min 13 s | 3 min 56 s |
| Year | 668.59 sols | 365.2422 days |
| Sundial at most fast / slow | 40 min / 51 min | 16.5 min / 14.1 min |
| Shape of the analemma | teardrop | figure eight |

??? note "Sources"
    - Day, year and month lengths: sections 9.5 and 9.7 and their sources. Dubhe and Merak: section 9.4.
    - The analemma shapes and the equation of time: section 9.9 and its sources.
    - The rest is our arithmetic.

## 9.9 Why the Sun runs fast and slow { #eot }

A sundial shows **apparent solar time**, set by the real Sun. A clock shows **mean solar time**, set by an imaginary
Sun that moves at a perfectly steady rate. The difference between them is the **equation of time**.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="A graph of how far a sundial is ahead of or behind a steady clock through the year, in minutes. The curve starts near minus 3 minutes in early January, falls to its lowest, a sundial about 14 minutes slow, around 11 February, rises through zero around 15 April to a small peak of about 4 minutes fast in mid May, falls through zero around 13 June to about 6 minutes slow in late July, rises through zero around 1 September to its highest, about 16 and a half minutes fast, around 3 November, and falls back through zero around 25 December.">
  <line x1="34" y1="120" x2="324" y2="120" stroke="currentColor" stroke-width="0.8"/>
  <line x1="34" y1="26.5" x2="34" y2="202.5" stroke="currentColor" stroke-width="0.8"/>
  <polyline points="34.0,136.9 34.8,139.4 35.6,141.8 36.4,144.3 37.2,146.6 38.0,149.0 38.8,151.3 39.6,153.6 40.4,155.8 41.2,158.0 41.9,160.2 42.7,162.3 43.5,164.4 44.3,166.4 45.1,168.4 45.9,170.4 46.7,172.2 47.5,174.1 48.3,175.8 49.1,177.6 49.9,179.2 50.7,180.8 51.5,182.4 52.3,183.8 53.1,185.3 53.9,186.6 54.7,187.9 55.5,189.1 56.2,190.3 57.0,191.4 57.8,192.4 58.6,193.3 59.4,194.2 60.2,195.0 61.0,195.8 61.8,196.4 62.6,197.0 63.4,197.6 64.2,198.0 65.0,198.4 65.8,198.7 66.6,199.0 67.4,199.1 68.2,199.2 69.0,199.3 69.8,199.2 70.5,199.1 71.3,199.0 72.1,198.7 72.9,198.4 73.7,198.0 74.5,197.6 75.3,197.1 76.1,196.5 76.9,195.9 77.7,195.2 78.5,194.5 79.3,193.6 80.1,192.8 80.9,191.9 81.7,190.9 82.5,189.9 83.3,188.8 84.1,187.7 84.8,186.5 85.6,185.3 86.4,184.0 87.2,182.7 88.0,181.3 88.8,179.9 89.6,178.5 90.4,177.1 91.2,175.6 92.0,174.0 92.8,172.5 93.6,170.9 94.4,169.3 95.2,167.7 96.0,166.0 96.8,164.3 97.6,162.7 98.4,161.0 99.2,159.3 99.9,157.5 100.7,155.8 101.5,154.1 102.3,152.3 103.1,150.6 103.9,148.9 104.7,147.1 105.5,145.4 106.3,143.7 107.1,142.0 107.9,140.3 108.7,138.6 109.5,136.9 110.3,135.2 111.1,133.6 111.9,132.0 112.7,130.4 113.5,128.8 114.2,127.3 115.0,125.8 115.8,124.3 116.6,122.9 117.4,121.4 118.2,120.1 119.0,118.7 119.8,117.4 120.6,116.1 121.4,114.9 122.2,113.7 123.0,112.6 123.8,111.5 124.6,110.4 125.4,109.4 126.2,108.5 127.0,107.6 127.8,106.7 128.5,105.9 129.3,105.2 130.1,104.4 130.9,103.8 131.7,103.2 132.5,102.6 133.3,102.1 134.1,101.7 134.9,101.3 135.7,101.0 136.5,100.7 137.3,100.5 138.1,100.3 138.9,100.2 139.7,100.1 140.5,100.1 141.3,100.1 142.1,100.2 142.8,100.3 143.6,100.5 144.4,100.8 145.2,101.1 146.0,101.4 146.8,101.8 147.6,102.2 148.4,102.7 149.2,103.2 150.0,103.8 150.8,104.4 151.6,105.1 152.4,105.8 153.2,106.5 154.0,107.3 154.8,108.1 155.6,108.9 156.4,109.8 157.2,110.7 157.9,111.6 158.7,112.6 159.5,113.6 160.3,114.6 161.1,115.6 161.9,116.7 162.7,117.7 163.5,118.8 164.3,119.9 165.1,121.1 165.9,122.2 166.7,123.3 167.5,124.5 168.3,125.6 169.1,126.8 169.9,128.0 170.7,129.1 171.5,130.3 172.2,131.4 173.0,132.6 173.8,133.7 174.6,134.9 175.4,136.0 176.2,137.1 177.0,138.2 177.8,139.2 178.6,140.3 179.4,141.3 180.2,142.3 181.0,143.3 181.8,144.3 182.6,145.2 183.4,146.1 184.2,146.9 185.0,147.7 185.8,148.5 186.5,149.3 187.3,150.0 188.1,150.7 188.9,151.3 189.7,151.9 190.5,152.4 191.3,152.9 192.1,153.4 192.9,153.8 193.7,154.1 194.5,154.4 195.3,154.7 196.1,154.9 196.9,155.0 197.7,155.1 198.5,155.2 199.3,155.1 200.1,155.1 200.8,154.9 201.6,154.8 202.4,154.5 203.2,154.2 204.0,153.8 204.8,153.4 205.6,153.0 206.4,152.4 207.2,151.8 208.0,151.2 208.8,150.5 209.6,149.7 210.4,148.9 211.2,148.0 212.0,147.1 212.8,146.1 213.6,145.1 214.4,144.0 215.2,142.8 215.9,141.6 216.7,140.4 217.5,139.1 218.3,137.7 219.1,136.3 219.9,134.9 220.7,133.4 221.5,131.9 222.3,130.3 223.1,128.7 223.9,127.0 224.7,125.3 225.5,123.6 226.3,121.8 227.1,120.0 227.9,118.2 228.7,116.3 229.5,114.5 230.2,112.5 231.0,110.6 231.8,108.6 232.6,106.7 233.4,104.7 234.2,102.7 235.0,100.6 235.8,98.6 236.6,96.6 237.4,94.5 238.2,92.4 239.0,90.4 239.8,88.3 240.6,86.3 241.4,84.2 242.2,82.2 243.0,80.1 243.8,78.1 244.5,76.1 245.3,74.1 246.1,72.1 246.9,70.1 247.7,68.2 248.5,66.3 249.3,64.4 250.1,62.5 250.9,60.7 251.7,58.9 252.5,57.1 253.3,55.4 254.1,53.7 254.9,52.1 255.7,50.5 256.5,48.9 257.3,47.4 258.1,45.9 258.8,44.5 259.6,43.2 260.4,41.8 261.2,40.6 262.0,39.4 262.8,38.3 263.6,37.2 264.4,36.2 265.2,35.2 266.0,34.3 266.8,33.5 267.6,32.8 268.4,32.1 269.2,31.5 270.0,30.9 270.8,30.4 271.6,30.0 272.4,29.7 273.2,29.4 273.9,29.2 274.7,29.1 275.5,29.1 276.3,29.1 277.1,29.2 277.9,29.4 278.7,29.6 279.5,30.0 280.3,30.4 281.1,30.8 281.9,31.4 282.7,32.0 283.5,32.7 284.3,33.5 285.1,34.4 285.9,35.3 286.7,36.3 287.5,37.3 288.2,38.5 289.0,39.7 289.8,40.9 290.6,42.3 291.4,43.7 292.2,45.1 293.0,46.7 293.8,48.3 294.6,49.9 295.4,51.6 296.2,53.4 297.0,55.2 297.8,57.1 298.6,59.0 299.4,61.0 300.2,63.0 301.0,65.1 301.8,67.3 302.5,69.4 303.3,71.6 304.1,73.9 304.9,76.2 305.7,78.5 306.5,80.8 307.3,83.2 308.1,85.6 308.9,88.1 309.7,90.6 310.5,93.0 311.3,95.5 312.1,98.1 312.9,100.6 313.7,103.2 314.5,105.7 315.3,108.3 316.1,110.8 316.8,113.4 317.6,116.0 318.4,118.6 319.2,121.1 320.0,123.7 320.8,126.2 321.6,128.8 322.4,131.3 323.2,133.8 324.0,136.3" fill="none" stroke="#c1440e" stroke-width="1.6"/>
  <circle cx="118.6" cy="120" r="2.2" fill="#5aa0d8"/>
  <circle cx="164.7" cy="120" r="2.2" fill="#5aa0d8"/>
  <circle cx="227.5" cy="120" r="2.2" fill="#5aa0d8"/>
  <circle cx="318.8" cy="120" r="2.2" fill="#5aa0d8"/>
  <g font-size="8" fill="currentColor">
    <line x1="31" y1="202.5" x2="34" y2="202.5" stroke="currentColor" stroke-width="0.6"/>
    <text x="29" y="205.5" text-anchor="end">−15</text>
    <line x1="31" y1="175.0" x2="34" y2="175.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="29" y="178.0" text-anchor="end">−10</text>
    <line x1="31" y1="147.5" x2="34" y2="147.5" stroke="currentColor" stroke-width="0.6"/>
    <text x="29" y="150.5" text-anchor="end">−5</text>
    <line x1="31" y1="92.5" x2="34" y2="92.5" stroke="currentColor" stroke-width="0.6"/>
    <text x="29" y="95.5" text-anchor="end">+5</text>
    <line x1="31" y1="65.0" x2="34" y2="65.0" stroke="currentColor" stroke-width="0.6"/>
    <text x="29" y="68.0" text-anchor="end">+10</text>
    <line x1="31" y1="37.5" x2="34" y2="37.5" stroke="currentColor" stroke-width="0.6"/>
    <text x="29" y="40.5" text-anchor="end">+15</text>
    <text x="29" y="123" text-anchor="end">0</text>
    <line x1="34.0" y1="120" x2="34.0" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="45.9" y="216.5" text-anchor="middle">J</text>
    <line x1="58.6" y1="120" x2="58.6" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="70.5" y="216.5" text-anchor="middle">F</text>
    <line x1="80.9" y1="120" x2="80.9" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="92.8" y="216.5" text-anchor="middle">M</text>
    <line x1="105.5" y1="120" x2="105.5" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="117.4" y="216.5" text-anchor="middle">A</text>
    <line x1="129.3" y1="120" x2="129.3" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="141.3" y="216.5" text-anchor="middle">M</text>
    <line x1="154.0" y1="120" x2="154.0" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="165.9" y="216.5" text-anchor="middle">J</text>
    <line x1="177.8" y1="120" x2="177.8" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="189.7" y="216.5" text-anchor="middle">J</text>
    <line x1="202.4" y1="120" x2="202.4" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="214.4" y="216.5" text-anchor="middle">A</text>
    <line x1="227.1" y1="120" x2="227.1" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="239.0" y="216.5" text-anchor="middle">S</text>
    <line x1="250.9" y1="120" x2="250.9" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="262.8" y="216.5" text-anchor="middle">O</text>
    <line x1="275.5" y1="120" x2="275.5" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="287.5" y="216.5" text-anchor="middle">N</text>
    <line x1="299.4" y1="120" x2="299.4" y2="123" stroke="currentColor" stroke-width="0.6"/>
    <text x="311.3" y="216.5" text-anchor="middle">D</text>
    <text x="40" y="37.5">sundial fast</text>
    <text x="232.6" y="186.0">sundial slow</text>
    <text x="271.5" y="24.1" text-anchor="end" fill="#c1440e">+16.5 min, 3 Nov</text>
    <text x="89.6" y="199.2" fill="#c1440e">−14.1 min, 11 Feb</text>
    <text x="40" y="20" fill="#5aa0d8">Blue dots: sundial and clock agree.</text>
    <text x="8" y="246">Minutes a sundial is ahead of (+) or behind (−) a steady clock.</text>
  </g>
</svg>
</div>

*Figure B. How far a sundial is ahead of or behind a steady clock through the year. The highest point is about +16½
minutes around 3 November, the lowest about −14 minutes around 11 February.*

The sundial and the clock agree only four times a year, near 15 April, 13 June, 1 September and 25 December. A single
solar day is never more than about 20 seconds shorter or 30 seconds longer than average, but long days and short days
come in runs, and the differences add up to a quarter of an hour.

There are two causes, and each makes a wave.

**1. The stretched orbit.** The Earth moves fastest when nearest the Sun, in early January (chapter 8, section 8.9).
Then the Sun moves fastest eastward against the stars, and the Earth must turn a little further each day to catch it
up. The solar days are longer than average, and the sundial falls behind. Six months later the opposite happens. This
wave repeats once a year and swings up to about 7.7 minutes either way.

**2. The tilt.** The Sun moves along the ecliptic, which is tilted 23.44° to the celestial equator. But our time comes
from the Earth's turning, which is measured along the equator. Near the equinoxes the Sun's path crosses the equator at
a slant, so part of its daily motion is northward or southward and its eastward progress is slower. Near the solstices
its path runs parallel to the equator and closer to the pole, where the hour lines crowd together, so it gains faster.
This wave repeats twice a year and swings up to about 9.9 minutes either way.

Add the two and you get figure B. In minutes, a good approximation is

$$\Delta t \approx -7.659 \sin D + 9.863 \sin(2D + 3.5932),$$

where $D$ grows by $2\pi$ radians over the year (the full formula for $D$ is in the source below).

Photograph the Sun at the same clock time every week for a year, and the pictures make a figure eight called the
**analemma**. Its height, about 47°, is twice the tilt: the Sun moving north and south. Its width is the equation of
time: the Sun early and late.

The equation of time disappears only for a planet with no tilt and a perfectly circular orbit. Mars has a tilt like
ours but a far more stretched orbit, so on Mars the two effects combine into a **teardrop**-shaped analemma, and the
Sun runs up to 51 minutes slow and 40 minutes fast.

??? note "Sources"
    - Apparent and mean solar time, the extremes of 16 min 33 s around 3 November and 14 min 6 s around 11 February,
      the zeros near 15 April, 13 June, 1 September and 25 December, the two causes (obliquity and eccentricity), the
      sum of two sine waves with periods of a year and half a year, the formula
      $-7.659 \sin D + 9.863 \sin(2D + 3.5932)$ with $D = 6.24004077 + 0.01720197\,(365.25(y - 2000) + d)$, and the
      equation of time vanishing only for zero tilt and zero eccentricity: Wikipedia,
      [Equation of time](https://en.wikipedia.org/wiki/Equation_of_time) (weaker). Figure B is drawn from this formula.
    - Solar days up to 20 seconds shorter or 30 seconds longer than average, building up over time: Wikipedia,
      [Solar time](https://en.wikipedia.org/wiki/Solar_time) (weaker).
    - The analemma as a figure eight about 47° long, twice the obliquity, and the teardrop shape on Mars: Wikipedia,
      [Analemma](https://en.wikipedia.org/wiki/Analemma) (weaker).
    - Mars's equation of time: Wikipedia, [Timekeeping on Mars](https://en.wikipedia.org/wiki/Timekeeping_on_Mars)
      (weaker).

## Check yourself { #check }

**1.** (beginner) Which way does the shadow of an upright stick point at local noon in Canada?

??? note "Answer"
    Due north. The Sun is due south at noon, and the shadow points away from it.

**2.** (beginner) Why does a star rise about 4 minutes earlier each night?

??? note "Answer"
    The Earth turns once against the stars in 23 h 56 min. Our 24-hour day is a little longer because the Earth also
    moves along its orbit and must turn about 1° more to face the Sun again.

**3.** (beginner) Around 20 March at 11 pm, where are the Big Dipper's pointer stars?

??? note "Answer"
    Straight above Polaris.

**4.** (intermediate) Why does Ramadan come in a different season every few years?

??? note "Answer"
    The Islamic calendar follows the Moon: 12 months make 354 or 355 days and no extra months are added. So each year
    Ramadan comes 10 to 11 days earlier against the seasons.

**5.** (intermediate) A town is at 80°W, in a time zone set to the time of 75°W. Ignoring daylight saving and the
equation of time, when does the Sun cross its meridian?

??? note "Answer"
    It is 5° west of the zone's centre, so 20 minutes late: at 12:20.

**6.** (intermediate) Why did the working day of a rover team on "Mars time" slide later every day?

??? note "Answer"
    A sol is about 40 minutes longer than an Earth day, so each sol's start comes about 40 minutes later by Earth
    clocks.

**7.** (advanced) Where are the pointer stars at 11 pm local Sun time on 20 June?

??? note "Answer"
    20 June is three months after 20 March, so the pointers stand above Polaris $3 \times 2 = 6$ hours earlier, at
    5 pm. By 11 pm they have turned $6 \times 15 = 90^\circ$ anticlockwise: a quarter turn, to the left of Polaris.

**8.** (expert) Why would a planet with no tilt and a perfectly circular orbit have no equation of time?

??? note "Answer"
    With a circular orbit the planet moves at a steady speed, so the Sun moves steadily against the stars. With no
    tilt the Sun moves along the equator itself, so all of its motion counts towards the time. Then every solar day
    is the same length and a sundial keeps perfect time with a clock.

## Summary

- A shadow is shortest at local noon, when the Sun crosses the meridian; the Sun moves 15° an hour.
- Clocks differ from sundials because of time zones (from the 1880s), daylight saving and the equation of time.
- The stars keep sidereal time: one turn takes 23 h 56 min 4 s, so stars rise 4 minutes earlier each night.
- The Big Dipper's pointers are above Polaris at about 11 pm around 20 March, 2 hours earlier each month, and turn
  anticlockwise 15° an hour.
- Lunar calendars follow the Moon and drift through the seasons; the Gregorian calendar follows the Sun with 97 leap
  days in 400 years; lunisolar calendars add a 13th month 7 times in 19 years.
- On Mars a sol is 24 h 39 min 35 s; mission teams have lived on Mars time, and the Sun runs up to 51 minutes slow.
- The equation of time comes from the Earth's stretched orbit and its tilt, and makes the analemma a figure eight.

**Next:** chapter 10, The Moon's phases, where we watch the Moon change shape through the month and see why.

## Further reading

- E. G. Richards, *Mapping Time: The Calendar and its History*, Oxford University Press, 1998. The calendars of the
  world, how they work and how to convert between them.
- Dava Sobel, *Longitude*, Walker, 1995. How the clockmaker John Harrison built a clock good enough to find longitude
  at sea.
- Terence Dickinson, *NightWatch: A Practical Guide to Viewing the Universe*, 4th edition, Firefly Books, 2006.
