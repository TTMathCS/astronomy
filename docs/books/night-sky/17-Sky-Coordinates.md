# 17. Sky coordinates

*Every town on the Earth has an address in latitude and longitude. Every star has one too. This chapter builds the
grid astronomers use to say where anything is in the sky: first your own grid of altitude and azimuth, which changes
as the sky turns, then the fixed grid of declination and right ascension, which turns with the stars. It shows how to
use a star's address to tell when it crosses your meridian and how high it climbs, why every star catalogue gives a
date, what other grids exist, how people mapped the sky in the past, how the grid looks from Mars, and ends with the
formula that turns a star's address into where to point.*

!!! abstract "In this chapter"
    **You will learn:**

    - what altitude and azimuth are, and why they are not enough
    - what the celestial sphere is
    - what declination and right ascension are, and why right ascension is measured in hours
    - how to use a star's coordinates and the sidereal time to find when and where it is highest
    - why star positions are given for a date such as J2000
    - what ecliptic and galactic coordinates are for
    - how Babylon, China, Greece and the Islamic world mapped the stars
    - where the poles of Mars lie on our grid
    - how to turn right ascension and declination into altitude and azimuth

    **You need:** chapters 2, 6 and 9.

    **Levels:** 17.1 to 17.4 are beginner; 17.5 to 17.9 are intermediate; 17.10 is advanced; 17.11 is expert.

## 17.1 Your own grid: altitude and azimuth { #altaz }

Chapter 2 gave you a simple way to say where something is in the sky:

- its **altitude**, how many degrees it is above the horizon, from 0° on the horizon to 90° at the zenith;
- its **azimuth**, how far round the horizon it is, measured from north through east: north is 0°, east 90°, south
  180° and west 270°.

The word *azimuth* comes from the Arabic *al-sumūt*, "the directions", just as *zenith* comes from Arabic too
(chapter 2).

This grid is easy to use, because it is fixed to your own horizon. But that is also its weakness. As the sky turns,
every star's altitude and azimuth change minute by minute, and from another town they are different again. A star
catalogue cannot list a star's altitude. It needs a grid fixed to the stars themselves.

??? note "Sources"
    - Azimuth as the angle round the horizon, usually from true north increasing eastward, and altitude: Wikipedia,
      [Horizontal coordinate system](https://en.wikipedia.org/wiki/Horizontal_coordinate_system) (weaker).
    - The Arabic *al-sumūt*, "the directions": Wikipedia, [Azimuth](https://en.wikipedia.org/wiki/Azimuth) (weaker).
    - *Zenith*: chapter 2, section 2.1.

## 17.2 The celestial sphere { #sphere }

Imagine the sky as a huge sphere with the Earth at its centre and the stars fixed on the inside. This is the
**celestial sphere**. It is not real, as chapter 2 said, but it is a very useful picture: we only want directions, so
we can make the sphere as big as we like.

Now copy the Earth's grid onto it:

- Extend the Earth's axis until it meets the sphere. That gives the **north** and **south celestial poles**. The north
  pole is close to Polaris.
- Extend the Earth's equator outward. That gives the **celestial equator** (chapter 6, section 6.4).

The Sun's yearly path round the sky, the **ecliptic** (chapter 8), is tilted 23.4° to the celestial equator, because
the Earth's axis is tilted. The two circles cross at two points. The point where the Sun crosses the equator going
north, on about 20 March, is the **March equinox point**.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The celestial sphere: a huge imaginary sphere centred on the Earth. The Earth's axis, extended, meets it at the north and south celestial poles; the north pole is near Polaris. The Earth's equator, extended, gives the celestial equator. The ecliptic, the Sun's yearly path, is tilted 23.4 degrees to it and crosses it at the March and September equinox points. A star's declination is its angle north of the celestial equator, like latitude. Its right ascension is measured eastward along the celestial equator from the March equinox point, like longitude.">
  <circle cx="160" cy="130" r="92" fill="none" stroke="currentColor" stroke-width="0.8"/>
  <polyline points="160.0,167.4 164.8,167.4 169.6,167.2 174.4,167.0 179.1,166.6 183.8,166.1 188.4,165.6 193.0,164.9 197.4,164.2 201.8,163.3 206.0,162.4 210.1,161.4 214.1,160.3 217.9,159.1 221.6,157.8 225.1,156.5 228.4,155.0 231.5,153.5 234.4,152.0 237.2,150.4 239.7,148.7 242.0,147.0 244.0,145.2 245.9,143.4 247.5,141.6 248.9,139.7 250.0,137.8 250.9,135.9 251.5,133.9 251.9,132.0 252.0,130.0" fill="none" stroke="#5aa0d8" stroke-width="1.4"/>
  <polyline points="252.0,130.0 251.9,128.0 251.5,126.1 250.9,124.1 250.0,122.2 248.9,120.3 247.5,118.4 245.9,116.6 244.0,114.8 242.0,113.0 239.7,111.3 237.2,109.6 234.4,108.0 231.5,106.5 228.4,105.0 225.1,103.5 221.6,102.2 217.9,100.9 214.1,99.7 210.1,98.6 206.0,97.6 201.8,96.7 197.4,95.8 193.0,95.1 188.4,94.4 183.8,93.9 179.1,93.4 174.4,93.0 169.6,92.8 164.8,92.6 160.0,92.6 155.2,92.6 150.4,92.8 145.6,93.0 140.9,93.4 136.2,93.9 131.6,94.4 127.0,95.1 122.6,95.8 118.2,96.7 114.0,97.6 109.9,98.6 105.9,99.7 102.1,100.9 98.4,102.2 94.9,103.5 91.6,105.0 88.5,106.5 85.6,108.0 82.8,109.6 80.3,111.3 78.0,113.0 76.0,114.8 74.1,116.6 72.5,118.4 71.1,120.3 70.0,122.2 69.1,124.1 68.5,126.1 68.1,128.0" fill="none" stroke="#5aa0d8" stroke-width="0.8" stroke-dasharray="2 2"/>
  <polyline points="68.1,128.0 68.0,130.0 68.1,132.0 68.5,133.9 69.1,135.9 70.0,137.8 71.1,139.7 72.5,141.6 74.1,143.4 76.0,145.2 78.0,147.0 80.3,148.7 82.8,150.4 85.6,152.0 88.5,153.5 91.6,155.0 94.9,156.5 98.4,157.8 102.1,159.1 105.9,160.3 109.9,161.4 114.0,162.4 118.2,163.3 122.6,164.2 127.0,164.9 131.6,165.6 136.2,166.1 140.9,166.6 145.6,167.0 150.4,167.2 155.2,167.4 160.0,167.4" fill="none" stroke="#5aa0d8" stroke-width="1.4"/>
  <polyline points="160.0,167.4 164.4,165.6 168.8,163.7 173.2,161.7 177.5,159.7 181.8,157.5 186.1,155.3 190.2,153.0 194.3,150.6 198.3,148.2 202.2,145.7 206.0,143.2 209.6,140.6 213.1,138.0 216.5,135.4 219.7,132.8 222.7,130.2 225.6,127.6 228.3,124.9 230.8,122.3 233.1,119.8 235.2,117.2 237.1,114.7 238.8,112.2 240.3,109.8 241.5,107.4 242.6,105.1 243.4,102.8 243.9,100.7 244.3,98.6 244.4,96.6 244.3,94.7 243.9,92.8 243.4,91.1" fill="none" stroke="#eea66f" stroke-width="1.4"/>
  <polyline points="243.4,91.1 242.6,89.5 241.5,88.0 240.3,86.6 238.8,85.4 237.1,84.2 235.2,83.2 233.1,82.3 230.8,81.6 228.3,81.0 225.6,80.5 222.7,80.1 219.7,79.9 216.5,79.8 213.1,79.9 209.6,80.1 206.0,80.4 202.2,80.9 198.3,81.5 194.3,82.2 190.2,83.1 186.1,84.1 181.8,85.2 177.5,86.4 173.2,87.8 168.8,89.3 164.4,90.9 160.0,92.6 155.6,94.4 151.2,96.3 146.8,98.3 142.5,100.3 138.2,102.5 133.9,104.7 129.8,107.0 125.7,109.4 121.7,111.8 117.8,114.3 114.0,116.8 110.4,119.4 106.9,122.0 103.5,124.6 100.3,127.2 97.3,129.8 94.4,132.4 91.7,135.1 89.2,137.7 86.9,140.2 84.8,142.8 82.9,145.3 81.2,147.8 79.7,150.2 78.5,152.6 77.4,154.9 76.6,157.2 76.1,159.3 75.7,161.4 75.6,163.4 75.7,165.3 76.1,167.2 76.6,168.9" fill="none" stroke="#eea66f" stroke-width="0.8" stroke-dasharray="2 2"/>
  <polyline points="76.6,168.9 77.4,170.5 78.5,172.0 79.7,173.4 81.2,174.6 82.9,175.8 84.8,176.8 86.9,177.7 89.2,178.4 91.7,179.0 94.4,179.5 97.3,179.9 100.3,180.1 103.5,180.2 106.9,180.1 110.4,179.9 114.0,179.6 117.8,179.1 121.7,178.5 125.7,177.8 129.8,176.9 133.9,175.9 138.2,174.8 142.5,173.6 146.8,172.2 151.2,170.7 155.6,169.1 160.0,167.4" fill="none" stroke="#eea66f" stroke-width="1.4"/>
  <line x1="160.0" y1="32.0" x2="160.0" y2="228.0" stroke="currentColor" stroke-width="0.6" stroke-dasharray="4 2"/>
  <circle cx="160" cy="130" r="7" fill="#5aa0d8"/>
  <polyline points="238.0,149.8 237.9,145.4 237.6,140.9 237.1,136.4 236.3,131.9 235.4,127.4 234.2,122.9 232.8,118.4 231.3,113.9 229.5,109.5 227.6,105.1 225.4,100.9 223.1,96.6 220.6,92.5 218.0,88.5 215.2,84.6 212.2,80.8 209.1,77.2 205.9,73.7 202.5,70.3 199.0,67.1 195.4,64.1 191.7,61.3 188.0,58.6 184.1,56.2 180.2,53.9 176.2,51.9 172.2,50.1 168.2,48.5 164.1,47.1 160.0,46.0" fill="none" stroke="currentColor" stroke-width="0.6"/>
  <polyline points="238.0,149.8 238.0,146.9 237.8,143.9 237.6,140.9 237.3,137.9 236.8,134.9 236.3,131.9 235.7,128.9 235.0,125.9 234.2,122.9 233.3,119.9 232.3,116.9 231.3,113.9 230.1,111.0 228.9,108.1 227.6,105.1 226.2,102.3 224.7,99.4 223.1,96.6 221.5,93.9" fill="none" stroke="#c1440e" stroke-width="1.8"/>
  <polyline points="160.0,167.4 163.2,167.4 166.4,167.3 169.6,167.2 172.8,167.1 176.0,166.9 179.1,166.6 182.3,166.3 185.4,166.0 188.4,165.6 191.5,165.2 194.5,164.7 197.4,164.2 200.3,163.6 203.2,163.0 206.0,162.4 208.8,161.7 211.4,161.0 214.1,160.3 216.6,159.5 219.1,158.7 221.6,157.8 223.9,156.9 226.2,156.0 228.4,155.0 230.5,154.1 232.5,153.0 234.4,152.0 236.3,150.9 238.0,149.8" fill="none" stroke="#c1440e" stroke-width="1.8"/>
  <circle cx="160.0" cy="167.4" r="2.6" fill="currentColor"/>
  <circle cx="221.5" cy="93.9" r="3.2" fill="#eea66f" stroke="currentColor" stroke-width="0.5"/>
  <g font-size="8" fill="currentColor">
    <text x="166.0" y="38.0">north celestial pole (near Polaris)</text>
    <text x="166.0" y="226.0">south celestial pole</text>
    <text x="156.0" y="191.4" text-anchor="end">March equinox point ↗</text>
    <text x="227.5" y="91.9">star</text>
    <text x="237.8" y="124.4" fill="#c1440e">declination δ</text>
    <text x="208.6" y="176.7" fill="#c1440e">right ascension α, eastward</text>
    <text x="64" y="128" text-anchor="end" fill="#5aa0d8">celestial</text>
    <text x="64" y="138" text-anchor="end" fill="#5aa0d8">equator</text>
    <text x="8" y="200" fill="#eea66f">ecliptic,</text>
    <text x="8" y="210" fill="#eea66f">tilted 23.4°</text>
    <text x="150" y="122" text-anchor="end">Earth</text>
    <text x="6" y="12">The celestial sphere</text>
  </g>
</svg>
</div>

*Figure A. The celestial sphere. Declination is measured north or south from the celestial equator, and right
ascension eastward along it from the March equinox point.*

??? note "Sources"
    - The celestial sphere as an abstract sphere of arbitrarily large radius, concentric with the Earth: Wikipedia,
      [Celestial sphere](https://en.wikipedia.org/wiki/Celestial_sphere) (weaker).
    - The celestial equator as the projection of the Earth's equator: Wikipedia,
      [Celestial equator](https://en.wikipedia.org/wiki/Celestial_equator) (weaker).
    - The ecliptic and the tilt of 23.4°: chapter 8 and its sources. The March equinox point: Wikipedia,
      [First point of Aries](https://en.wikipedia.org/wiki/First_point_of_Aries) (weaker).

## 17.3 Declination: latitude on the sky { #declination }

A star's **declination** (δ) is its angle north or south of the celestial equator. It works just like latitude:

- 0° on the celestial equator;
- +90° at the north celestial pole, −90° at the south celestial pole;
- north is written with a plus sign and south with a minus sign, and the sign is always given.

| Star | Declination |
| --- | --- |
| Polaris | +89° 16′ |
| Vega | +38° 47′ |
| Betelgeuse | +7° 24′ |
| Sirius | −16° 43′ |

Because the celestial equator is right above the Earth's equator, a star at declination +43.7° passes straight over
the heads of people at latitude 43.7° N, such as Toronto. In general, a star passes through your zenith if its
declination equals your latitude.

Declination also tells you which stars you can see at all. Chapter 6, section 6.9, worked out the rule: from latitude
φ north, stars with declination above 90° − φ never set, and stars below −(90° − φ) never rise.

??? note "Sources"
    - Declination as the angle from the celestial equator, like latitude, with 0° on the equator, +90° and −90° at the
      poles, and the sign always included: Wikipedia, [Declination](https://en.wikipedia.org/wiki/Declination)
      (weaker).
    - Declinations for the epoch J2000: Wikipedia, [Polaris](https://en.wikipedia.org/wiki/Polaris) (+89° 15′ 51″),
      [Vega](https://en.wikipedia.org/wiki/Vega) (+38° 47′ 01″),
      [Betelgeuse](https://en.wikipedia.org/wiki/Betelgeuse) (+7° 24′ 25″) and
      [Sirius](https://en.wikipedia.org/wiki/Sirius) (−16° 42′ 58″), all weaker. The table rounds them to the nearest
      minute of arc.
    - The zenith rule follows from the picture: the celestial equator is overhead at the Earth's equator, and the pole
      stands at an altitude equal to your latitude (chapter 7).

## 17.4 Right ascension: longitude on the sky { #ra }

Longitude needs a starting line, and Greenwich was chosen for the Earth. On the sky the starting point is the March
equinox point. A star's **right ascension** (α) is measured **eastward** along the celestial equator from that point,
to the circle running from the pole down through the star.

Right ascension is given not in degrees but in **hours, minutes and seconds**, from 0 h to 24 h:

$$24 \text{ h} = 360°, \qquad 1 \text{ h} = 15°, \qquad 1 \text{ min} = 15′.$$

Why hours? Because the sky turns once a day. As the Earth spins, the lines of right ascension pass across your
meridian one after another, an hour's worth of right ascension each hour of sidereal time (chapter 9). So right
ascension says **when** a star crosses your meridian, compared with other stars:

| Star | Right ascension |
| --- | --- |
| Polaris | 2 h 32 min |
| Betelgeuse | 5 h 55 min |
| Sirius | 6 h 45 min |
| Vega | 18 h 37 min |

Betelgeuse crosses the meridian 50 minutes (of sidereal time) before Sirius; Vega crosses nearly 13 hours after
Betelgeuse, so it is near its lowest when Betelgeuse is highest.

The March equinox point is also called the **first point of Aries**, because the Sun was in Aries at the March
equinox in ancient times. Precession has since moved it about 30°, and it now lies in Pisces, near the border with
Aquarius.

??? note "Sources"
    - Right ascension measured eastward along the celestial equator from the March equinox, 24 h to a circle, 1 h =
      15° and 1 min = 15′: Wikipedia, [Right ascension](https://en.wikipedia.org/wiki/Right_ascension) (weaker).
    - Right ascensions for the epoch J2000: the Polaris, Betelgeuse, Sirius and Vega pages listed in section 17.3,
      rounded to the nearest minute.
    - The first point of Aries, moved about 30° since Hipparchus and now in Pisces near Aquarius: Wikipedia,
      [First point of Aries](https://en.wikipedia.org/wiki/First_point_of_Aries) (weaker).
    - Sidereal time: chapter 9, section 9.3, and its sources.

## 17.5 Using the grid { #using }

**When is a star highest?** Your **local sidereal time** is the right ascension that is crossing your meridian right
now (chapter 9). A star is highest, due south from the northern hemisphere, when the local sidereal time equals its
right ascension. The **hour angle** says how long ago that was:

$$\text{hour angle} = \text{local sidereal time} - \text{right ascension}.$$

An hour angle of −3 h means the star will cross the meridian in 3 hours; +2 h means it crossed 2 hours ago.

**How high does it get?** On the meridian, the celestial equator is $90° - \varphi$ above the south horizon, where
φ is your latitude, and a star is δ above or below that. So its greatest altitude is

$$h_{\max} = 90° - \varphi + \delta,$$

the formula of chapter 6, section 6.9. Figure B shows it for Toronto.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="A slice through the sky along the meridian, seen from latitude 43.7 degrees north, the latitude of Toronto. North is on the left, south on the right. The north celestial pole stands 43.7 degrees above the north horizon, equal to the latitude. The celestial equator crosses the meridian 46.3 degrees above the south horizon, 90 degrees minus the latitude. Sirius, at declination minus 16.7 degrees, crosses the meridian 16.7 degrees below the equator, at 29.6 degrees. Vega, at plus 38.8 degrees, passes 85.1 degrees up, almost overhead.">
  <line x1="14" y1="196" x2="326" y2="196" stroke="currentColor" stroke-width="1"/>
  <path d="M50,196 A120,120 0 0 1 290,196" fill="none" stroke="currentColor" stroke-width="0.6" stroke-dasharray="3 2"/>
  <line x1="170" y1="196" x2="83.2" y2="113.1" stroke="currentColor" stroke-width="0.8"/>
  <line x1="170" y1="196" x2="252.9" y2="109.2" stroke="#5aa0d8" stroke-width="1.2"/>
  <line x1="170" y1="196" x2="274.4" y2="136.8" stroke="#eea66f" stroke-width="1.2"/>
  <line x1="170" y1="196" x2="180.3" y2="76.4" stroke="#eea66f" stroke-width="0.8"/>
  <line x1="170" y1="196" x2="170.0" y2="76.0" stroke="currentColor" stroke-width="0.4"/>
  <circle cx="83.2" cy="113.1" r="2.8" fill="#eea66f" stroke="currentColor" stroke-width="0.5"/>
  <circle cx="274.4" cy="136.8" r="2.8" fill="#eea66f" stroke="currentColor" stroke-width="0.5"/>
  <circle cx="180.3" cy="76.4" r="2.8" fill="#eea66f" stroke="currentColor" stroke-width="0.5"/>
  <path d="M145.4,172.5 A34,34 0 0 0 136.0,196.0" fill="none" stroke="currentColor" stroke-width="1"/>
  <path d="M224.0,196.0 A54,54 0 0 0 207.3,157.0" fill="none" stroke="#5aa0d8" stroke-width="1"/>
  <path d="M239.6,156.5 A80,80 0 0 0 225.3,138.2" fill="none" stroke="#eea66f" stroke-width="1"/>
  <circle cx="170" cy="192" r="3" fill="currentColor"/>
  <g font-size="8" fill="currentColor">
    <text x="83.2" y="95.1" text-anchor="middle">north celestial pole,</text>
    <text x="83.2" y="105.1" text-anchor="middle">43.7° up</text>
    <text x="258.9" y="103.2" fill="#5aa0d8">celestial equator,</text>
    <text x="258.9" y="113.2" fill="#5aa0d8">46.3° up</text>
    <text x="280.4" y="139.8">Sirius,</text>
    <text x="280.4" y="149.8">29.6° up</text>
    <text x="186.3" y="74.4">Vega, 85.1° up</text>
    <text x="164.0" y="72.0" text-anchor="end">zenith</text>
    <text x="128.9" y="183.1" text-anchor="end">φ</text>
    <text x="226.3" y="176.2" fill="#5aa0d8">90° − φ</text>
    <text x="238.9" y="146.9" fill="#eea66f">δ</text>
    <text x="16" y="208">north horizon</text>
    <text x="324" y="208" text-anchor="end">south horizon</text>
    <text x="170" y="208" text-anchor="middle">you, at 43.7° N</text>
    <text x="6" y="12">The meridian from Toronto (φ = 43.7°)</text>
    <text x="170" y="226" text-anchor="middle">Highest altitude = 90° − φ + δ</text>
  </g>
</svg>
</div>

*Figure B. The meridian from latitude 43.7° N. The pole is as high as your latitude; the equator crosses 90° − φ above
the south horizon; each star crosses δ above or below the equator.*

**Planets move on the grid.** Stars keep their coordinates for years, but the Sun, the Moon and the planets move
through the grid, so an almanac or an app lists them day by day. At its opposition on 19 February 2027 (chapter 14),
Mars is at about right ascension 10 h 17 min and declination +15½°, in Leo. From Toronto it then climbs to about
$90° - 43.7° + 15.5° = 62°$ at midnight.

Star charts and apps (chapter 18) and computer-driven telescopes (chapter 19) all use this grid.

??? note "Sources"
    - Local hour angle = local sidereal time − right ascension: Wikipedia,
      [Hour angle](https://en.wikipedia.org/wiki/Hour_angle) (weaker).
    - Sidereal time and meridian crossings: chapter 9 and its sources. The greatest altitude: chapter 6, section 6.9.
    - Mars's position on 19 February 2027 was worked out by us from JPL's orbital elements, as in chapter 14, and is
      good to a fraction of a degree.

## 17.6 Why star positions have a date { #epoch }

The grid is fixed to the Earth's equator and the March equinox point, and those move. Precession swings the Earth's
axis round once in about 26,000 years (chapter 6, section 6.10), so the whole grid slowly slides across the stars,
and every star's right ascension and declination slowly change.

So a star catalogue always says which date its grid belongs to, the **epoch**. Most use **J2000**, the grid as it was
at the start of the year 2000. Before about 1984, catalogues dated to 1950 or 1900 were common. In 26 years precession
moves the grid about $26 \times 50″ = 0.36°$. For your eyes or binoculars that hardly matters; for a large telescope
it does.

Today the official grid is pinned to very distant **quasars**, whose positions are measured with radio telescopes
spread across the world. Since 1 January 2022 it has also included the grid measured in visible light by the European
**Gaia** spacecraft.

??? note "Sources"
    - Precession and its rate of about 50″ a year: chapter 6, section 6.10, and its sources.
    - J2000, and coordinate systems dated to 1950 or 1900 before about 1984: Wikipedia,
      [Epoch (astronomy)](https://en.wikipedia.org/wiki/Epoch_(astronomy)) (weaker).
    - The International Celestial Reference Frame defined by extragalactic sources, mainly quasars, observed by
      very-long-baseline radio interferometry, and the IAU decision that from 1 January 2022 it comprises ICRF3 for
      radio and Gaia-CRF3 for light: Wikipedia,
      [International Celestial Reference System](https://en.wikipedia.org/wiki/International_Celestial_Reference_System)
      (weaker).

## 17.7 Other grids { #others }

Astronomers choose the grid that suits the job.

- **Ecliptic coordinates** use the ecliptic in place of the celestial equator, measuring **ecliptic longitude** along
  the Sun's path from the March equinox point and **ecliptic latitude** north or south of it. The planets (except
  Mercury) orbit close to the plane of the ecliptic, so their ecliptic latitudes stay small, which makes this grid
  handy for the Solar System.
- **Galactic coordinates** use the plane of our Milky Way galaxy, with longitude measured from the direction of the
  galaxy's centre, in Sagittarius. The International Astronomical Union set them up in **1958** using radio maps of
  hydrogen gas. The best marker of the true centre, the radio source **Sagittarius A***, lies at right ascension
  17 h 45 min 40 s and declination −29° 00′.

??? note "Sources"
    - Ecliptic longitude measured along the ecliptic from the March equinox, and most planets (except Mercury) having
      only slight inclinations to it: Wikipedia,
      [Ecliptic coordinate system](https://en.wikipedia.org/wiki/Ecliptic_coordinate_system) (weaker).
    - Galactic coordinates: defined by the IAU in 1958 from radio observations of neutral hydrogen, and Sagittarius A*
      at 17h 45m 40.04s, −29° 00′ 28.1″ (J2000): Wikipedia,
      [Galactic coordinate system](https://en.wikipedia.org/wiki/Galactic_coordinate_system) (weaker).

## 17.8 Mapping the sky in history { #history }

- **Babylon** built its sky around the Sun's path. Around 400 BC its astronomers divided the path into twelve equal
  signs of 30° (history book,
  [chapter 2, section 2.9](../history/02-Mesopotamia.md#zodiac)), the ancestor of ecliptic longitude.
- **China** built its sky around the pole and the equator, with a ring of 28 **mansions** that the Moon passes
  through. In the 4th century BC, Shi Shen and Gan De wrote the first Chinese star catalogues (history book,
  [chapter 4, section 4.4](../history/04-China.md#mansions)).
- **Hipparchus**, in the 2nd century BC, listed about 850 stars with their positions and brightness. Part of his lost
  catalogue was found in 2022, hidden under later writing on a reused parchment, with positions good to within one
  degree (history book, [chapter 7, section 7.6](../history/07-Greece-and-Alexandria.md#hipparchus)). He measured stars
  in equatorial coordinates, an early form of right ascension and declination.
- **Ptolemy**'s *Almagest*, written around AD 150, had a star catalogue of its own, less accurate than Hipparchus'
  (history book, [chapter 7, section 7.8](../history/07-Greece-and-Alexandria.md#ptolemy)).
- In **964** al-Sufi in Isfahan checked Ptolemy's catalogue against the sky in his *Book of Fixed Stars* (history book,
  [chapter 8, section 8.4](../history/08-The-Islamic-World-and-Persia.md#stars)).
- In the 1420s and 1430s **Ulugh Beg**'s observatory at Samarkand measured a new catalogue of 1,018 stars (history
  book, [chapter 8, section 8.10](../history/08-The-Islamic-World-and-Persia.md#samarkand)).

??? note "Sources"
    - Babylon, China, Hipparchus, Ptolemy, al-Sufi and Ulugh Beg: this site's history book, chapters 2, 4, 7 and 8, and
      their sources.
    - Hipparchus measuring stars in equatorial coordinates in the 2nd century BC: Wikipedia,
      [Right ascension](https://en.wikipedia.org/wiki/Right_ascension) (weaker).

## 17.9 The poles of Mars on our grid { #mars }

Mars's axis points in a different direction from ours (chapter 6, section 6.8). On our grid, Mars's **north celestial
pole** lies in Cygnus at right ascension **21 h 10 min 42 s**, declination **+52° 53′**. The top two stars of the
Northern Cross, Sadr and Deneb, point to it. Its **south celestial pole** is at 9 h 10 min 42 s, −52° 53′, a couple of
degrees from Kappa Velorum.

Astronomers living on Mars would not use our grid. They would build their own on Mars's equator and Mars's March
equinox point, just as we did. Their celestial equator would be tilted 37° to ours (section 17.10), so every star would
have a different "Martian declination". Only the stars themselves, and the distant quasars, would be the same.

??? note "Sources"
    - Mars's north celestial pole at 21h 10m 42s, +52° 53.0′, in Cygnus, with Sadr and Deneb pointing to it, and the
      south pole at 9h 10m 42s, −52° 53.0′, a couple of degrees from Kappa Velorum: Wikipedia,
      [Astronomy on Mars](https://en.wikipedia.org/wiki/Astronomy_on_Mars) (weaker).
    - Mars's pole stars: chapter 6, section 6.8.

## 17.10 Working it out { #working }

**Hours to degrees.** Sirius is at right ascension 6 h 45 min 9 s:

$$6 + \frac{45}{60} + \frac{9}{3600} = 6.7525 \text{ h}, \qquad 6.7525 \times 15 = 101.29°.$$

**When does Sirius cross the meridian?** When the local sidereal time is 6 h 45 min. On the March equinox, sidereal
time is about 12 hours ahead of sun time (chapter 9, section 9.8), so that is about 6:45 pm, still in twilight. The
stars come round 2 hours earlier each month, so going back three months, to late December, Sirius crosses
$3 \times 2 = 6$ hours later, about 12:45 am: around New Year, Sirius is highest at about midnight.

**How high?** From Toronto, $h_{\max} = 90° - 43.7° + (-16.7°) = 29.6°$. From latitude 73.3° N, Sirius would just
reach the horizon; further north it never rises.

**The tilt of Mars's grid.** The angle between two great circles equals the angle between their poles. Our pole is at
declination +90°, and Mars's at +52.9°, so Mars's celestial equator is tilted $90° - 52.9° = 37.1°$ to ours.

| | Mars | Earth |
| --- | --- | --- |
| North celestial pole, on our grid | 21 h 10.7 min, +52.9°, in Cygnus | +90°, near Polaris |
| North pole star | none bright; Deneb less than 10° away | Polaris, less than 1° away |
| South pole star | Kappa Velorum, magnitude 2.5 | Sigma Octantis, magnitude 5.5 |
| Tilt of the axis | 25.19° | 23.4° |
| The sky turns once in | 24 h 37 min 23 s | 23 h 56 min 4 s |
| The sky turns per hour | 14.62° | 15.04° |

??? note "Sources"
    - Sirius's right ascension and declination: section 17.3. Sidereal time and the 2 hours a month: chapter 9, section
      9.8.
    - Mars's poles: section 17.9. Pole stars: chapter 6, sections 6.8 and 6.9. Mars's tilt of 25.19°: NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html). The Earth's 23.4°: chapter 8.
    - Sidereal days: chapter 9, section 9.8. The arithmetic is ours.

## 17.11 From the grid to the sky { #convert }

To point a telescope, or to know where to look, you need to turn a star's declination δ and hour angle H into
altitude h and azimuth A at your latitude φ.

Draw a triangle on the sky with corners at the north celestial pole, your zenith and the star. Its sides are

- pole to zenith: $90° - \varphi$;
- pole to star: $90° - \delta$;
- zenith to star: $90° - h$;

and the angle at the pole is the hour angle H. The cosine rule for a triangle on a sphere,
$\cos c = \cos a \cos b + \sin a \sin b \cos C$, then gives

$$\sin h = \sin\varphi \sin\delta + \cos\varphi \cos\delta \cos H,$$

and for the azimuth, measured from north,

$$\cos A = \frac{\sin\delta - \sin h \sin\varphi}{\cos h \cos\varphi},$$

taking A between 0° and 180° when the star is in the east (H negative) and $360° - A$ when it is in the west.

**Check.** On the meridian, $H = 0$ and $\cos H = 1$, so $\sin h = \cos(\varphi - \delta)$ and
$h = 90° - \varphi + \delta$, the formula of section 17.5.

**Example.** Betelgeuse (δ = +7.41°) from Toronto (φ = 43.7°), three hours before it crosses the meridian,
$H = -3 \text{ h} = -45°$:

$$\sin h = 0.6909 \times 0.1289 + 0.7230 \times 0.9917 \times 0.7071 = 0.0891 + 0.5069 = 0.5960,$$

so $h = 36.6°$. Then

$$\cos A = \frac{0.1289 - 0.5960 \times 0.6909}{0.8030 \times 0.7230} = -0.487,$$

so $A = 119.2°$: Betelgeuse is 36.6° up, between east-south-east and south-east.

**Rising and setting.** Put $h = 0$ in the first formula: $\cos H_0 = -\tan\varphi \tan\delta$. For Betelgeuse from
Toronto, $\cos H_0 = -0.9556 \times 0.1300 = -0.124$, so $H_0 = 97.1° = 6 \text{ h } 29 \text{ min}$. It is above the
horizon for twice that, about 12 h 57 min of sidereal time, and it rises at azimuth $\arccos(\sin\delta / \cos\varphi)
= 79.7°$, just north of east, as chapter 6 said a star north of the equator must.

??? note "Sources"
    - The spherical cosine rule and the conversion between hour angle, declination, altitude and azimuth are standard;
      see Duffett-Smith and Zwart under Further reading. Hour angle: section 17.5.
    - Betelgeuse's declination: section 17.3. Stars north of the equator rising north of east: chapter 6, section 6.4.
      The arithmetic is ours.

## Check yourself { #check }

**1.** (beginner) Why can't a star catalogue list a star's altitude and azimuth?

??? note "Answer"
    They change all the time as the sky turns, and they are different from every place on the Earth.

**2.** (beginner) What is declination like on the Earth, and what is the declination of the north celestial pole?

??? note "Answer"
    It is like latitude. The north celestial pole is at +90°.

**3.** (beginner) How many degrees is one hour of right ascension?

??? note "Answer"
    15°, because 24 hours make the full 360°.

**4.** (intermediate) Vega is at right ascension 18 h 37 min. At what local sidereal time is it highest?

??? note "Answer"
    At 18 h 37 min of local sidereal time, when its right ascension is on the meridian.

**5.** (intermediate) Why do star catalogues give an epoch such as J2000?

??? note "Answer"
    Precession slowly moves the celestial equator and the March equinox point, so the coordinates of every star slowly
    change. The epoch says which date's grid is meant.

**6.** (intermediate) Where is the "first point of Aries" now, and why is it not in Aries?

??? note "Answer"
    It lies in Pisces, near the border with Aquarius. Precession has moved it about 30° since ancient times, when it
    was in Aries.

**7.** (advanced) How high does Vega (δ = +38.8°) climb from Toronto (φ = 43.7°), and from Sydney (φ = 33.9° S)?

??? note "Answer"
    From Toronto, $90° - 43.7° + 38.8° = 85.1°$, almost overhead. From Sydney the formula with φ = −33.9° gives
    $90° + 33.9° + 38.8° = 162.7°$, which means it crosses north of the zenith at $180° - 162.7° = 17.3°$ above the
    north horizon.

**8.** (expert) Find the altitude of Sirius (δ = −16.7°) from Toronto (φ = 43.7°) two hours after it crosses the
meridian.

??? note "Answer"
    $H = +2 \text{ h} = 30°$.
    $\sin h = 0.6909 \times (-0.2874) + 0.7230 \times 0.9578 \times 0.8660 = -0.1986 + 0.5997 = 0.4011$, so
    $h = 23.6°$, in the south-south-west.

## Summary

- Altitude and azimuth are your own grid; they change as the sky turns and from place to place.
- The celestial sphere carries the Earth's poles and equator out to the sky.
- Declination is latitude on the sky, from +90° to −90°.
- Right ascension is longitude on the sky, measured eastward from the March equinox point in hours; 1 h is 15°.
- A star is highest when the local sidereal time equals its right ascension, at altitude 90° − φ + δ.
- Precession slowly moves the grid, so positions are given for an epoch such as J2000; today the grid is pinned to
  quasars and Gaia.
- Ecliptic coordinates suit the Solar System; galactic coordinates suit the Milky Way.
- Hipparchus, Chinese astronomers, Ptolemy, al-Sufi and Ulugh Beg all made star catalogues.
- Mars's north celestial pole is in Cygnus; its equator is tilted 37° to ours.
- $\sin h = \sin\varphi \sin\delta + \cos\varphi \cos\delta \cos H$ turns the grid into where to look.

**Next:** [chapter 18, Star charts, planispheres and apps](18-Star-Charts-Planispheres-and-Apps.md), where we put the
grid to work and learn to read a map of the sky.

## Further reading

- Peter Duffett-Smith and Jonathan Zwart, *Practical Astronomy with your Calculator or Spreadsheet*, 4th edition,
  Cambridge University Press, 2011. Clear, worked methods for coordinates, sidereal time, rising and setting.
- Guy Consolmagno and Dan M. Davis, *Turn Left at Orion*, 5th edition, Cambridge University Press, 2018.
