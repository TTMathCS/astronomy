# 14. Orbits around the Earth

*Thousands of satellites now go round the Earth, and their orbits are chosen with great care. Some skim the top of the
air, some hang still over the equator, some swing far out over the north, and some keep pace with the Sun. This
chapter shows what each kind of orbit is for, how the Earth's bulge slowly turns them, how navigation satellites tell
you where you are, why the sky is getting crowded, and which of these tricks also work at Mars.*

!!! abstract "In this chapter"
    **You will learn:**

    - how the height of an orbit sets its period, from 93 minutes to a day
    - why a satellite's track over the ground is a wave that creeps west
    - how geostationary satellites came about, and what they are used for
    - how the Earth's bulge turns orbits, and how that gives sun-synchronous orbits
    - why the Soviet Union invented the long, tilted Molniya orbit
    - how the world's navigation satellites are arranged
    - why space debris worries everyone who flies in low orbit
    - how the same kinds of orbit are used round Mars
    - how to work out the tilt of a sun-synchronous orbit

    **You need:** chapters 3, 4 and 7.

    **Levels:** 14.1 to 14.3 are beginner; 14.4 to 14.8 are intermediate; 14.9 is advanced; 14.10 is expert.

## 14.1 Low, middle and high { #kinds }

Kepler's third law (chapter 3) ties an orbit's period to its size: the higher the orbit, the longer it takes. That one
rule sorts satellites into families.

| Orbit | Height above the ground | Period | Tilt to the equator | Used for |
| --- | --- | --- | --- | --- |
| Space station | about 400 km | 93 minutes | 51.6° | living and working in space |
| Sun-synchronous | 600 to 800 km | 96 to 100 minutes | about 98° | photographing the Earth and the weather |
| GPS | about 20,200 km | 12 hours | about 55° | navigation |
| Molniya | about 600 to 40,000 km | 12 hours | 63.4° | television and messages in the far north |
| Geostationary | 35,786 km | one day | 0° | television, messages, weather |

**Low Earth orbit**, up to a couple of thousand kilometres, is cheapest to reach and closest for cameras, but a
satellite there races across any one place in a few minutes. **Medium Earth orbit** holds the navigation satellites.
**Geostationary orbit** is far out, where one orbit takes exactly as long as the Earth takes to turn.

A tilt of more than 90° means the satellite goes round **backwards**, westwards, against the Earth's spin. That costs
extra fuel at launch (chapter 13), but section 14.4 shows why it is worth it.

??? note "Sources"
    - The space station's 51.6°, about 400 km, about 93 minutes and 15.5 orbits a day: Wikipedia,
      [International Space Station](https://en.wikipedia.org/wiki/International_Space_Station) (weaker).
    - Sun-synchronous orbits of 600 to 800 km, 96 to 100 minutes and about 98°: Wikipedia,
      [Sun-synchronous orbit](https://en.wikipedia.org/wiki/Sun-synchronous_orbit) (weaker).
    - GPS at about 20,200 km, two orbits each sidereal day, six planes at about 55°: Wikipedia,
      [Global Positioning System](https://en.wikipedia.org/wiki/Global_Positioning_System) (weaker).
    - Molniya: 63.4°, half a sidereal day, apogee up to 40,000 km: Wikipedia,
      [Molniya orbit](https://en.wikipedia.org/wiki/Molniya_orbit) (weaker). The perigee of about 600 km: our
      arithmetic, section 14.9.
    - Geostationary at 35,786 km: book 1, chapter 16, section 16.6, and section 14.9 below.

## 14.2 Tracks on the ground { #tracks }

Draw on a map the point on the ground right under a satellite, and you get its **ground track**. For a satellite on a
tilted orbit it is a wave. The wave reaches as far north and south as the orbit's tilt: the space station, tilted
51.6°, never flies over anywhere farther north than 51.6° N or farther south than 51.6° S.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The track of the International Space Station over the ground for three orbits, drawn on a flat map of the world with longitude across and latitude up. Each orbit makes a wave that rises to 51.6 degrees north and falls to 51.6 degrees south. Each wave starts 23 degrees farther west than the one before, because the Earth turns under the orbit during the 93 minutes the station takes to go round.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">Where the space station flies over, three orbits</text>
    <rect x="20" y="40" width="300" height="150" fill="none" stroke="currentColor" stroke-width="0.6"/>
    <line x1="20" y1="165.0" x2="320" y2="165.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="18" y="168.0" text-anchor="end">60°S</text>
    <line x1="20" y1="140.0" x2="320" y2="140.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="18" y="143.0" text-anchor="end">30°S</text>
    <line x1="20" y1="115.0" x2="320" y2="115.0" stroke="#cfc8bf" stroke-width="0.8"/>
    <text x="18" y="118.0" text-anchor="end">0°</text>
    <line x1="20" y1="90.0" x2="320" y2="90.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="18" y="93.0" text-anchor="end">30°N</text>
    <line x1="20" y1="65.0" x2="320" y2="65.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="18" y="68.0" text-anchor="end">60°N</text>
    <line x1="70.0" y1="40" x2="70.0" y2="190" stroke="#cfc8bf" stroke-width="0.4"/>
    <line x1="120.0" y1="40" x2="120.0" y2="190" stroke="#cfc8bf" stroke-width="0.4"/>
    <line x1="170.0" y1="40" x2="170.0" y2="190" stroke="#cfc8bf" stroke-width="0.4"/>
    <line x1="220.0" y1="40" x2="220.0" y2="190" stroke="#cfc8bf" stroke-width="0.4"/>
    <line x1="270.0" y1="40" x2="270.0" y2="190" stroke="#cfc8bf" stroke-width="0.4"/>
    <line x1="320.0" y1="40" x2="320.0" y2="190" stroke="#cfc8bf" stroke-width="0.4"/>
    <line x1="20" y1="72.0" x2="320" y2="72.0" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <line x1="20" y1="158.0" x2="320" y2="158.0" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <text x="318" y="69.0" text-anchor="end" fill="#555">51.6° N, the farthest north it goes</text>
    <path d="M170.0,115.0 L170.5,114.2 L171.1,113.5 L171.6,112.7 L172.2,112.0 L172.7,111.2 L173.2,110.5 L173.8,109.7 L174.3,108.9 L174.9,108.2 L175.4,107.4 L176.0,106.7 L176.6,105.9 L177.1,105.2 L177.7,104.4 L178.3,103.7 L178.8,102.9 L179.4,102.2 L180.0,101.5 L180.6,100.7 L181.2,100.0 L181.8,99.3 L182.4,98.5 L183.0,97.8 L183.7,97.1 L184.3,96.4 L184.9,95.7 L185.6,94.9 L186.2,94.2 L186.9,93.5 L187.6,92.8 L188.3,92.1 L189.0,91.5 L189.7,90.8 L190.5,90.1 L191.2,89.4 L192.0,88.8 L192.7,88.1 L193.5,87.4 L194.3,86.8 L195.1,86.2 L196.0,85.5 L196.8,84.9 L197.7,84.3 L198.6,83.7 L199.5,83.1 L200.4,82.5 L201.3,81.9 L202.3,81.4 L203.3,80.8 L204.3,80.3 L205.3,79.7 L206.4,79.2 L207.4,78.7 L208.5,78.2 L209.6,77.7 L210.8,77.3 L211.9,76.8 L213.1,76.4 L214.3,76.0 L215.6,75.6 L216.8,75.2 L218.1,74.8 L219.4,74.5 L220.7,74.2 L222.1,73.9 L223.4,73.6 L224.8,73.3 L226.2,73.1 L227.6,72.9 L229.1,72.7 L230.5,72.5 L232.0,72.4 L233.4,72.2 L234.9,72.2 L236.4,72.1 L237.9,72.0 L239.4,72.0 L240.9,72.0 L242.4,72.0 L243.9,72.1 L245.4,72.2 L246.8,72.2 L248.3,72.4 L249.8,72.5 L251.2,72.7 L252.7,72.9 L254.1,73.1 L255.5,73.3 L256.9,73.6 L258.2,73.9 L259.6,74.2 L260.9,74.5 L262.2,74.8 L263.5,75.2 L264.7,75.6 L266.0,76.0 L267.2,76.4 L268.4,76.8 L269.5,77.3 L270.7,77.7 L271.8,78.2 L272.9,78.7 L273.9,79.2 L275.0,79.7 L276.0,80.3 L277.0,80.8 L278.0,81.4 L279.0,81.9 L279.9,82.5 L280.8,83.1 L281.7,83.7 L282.6,84.3 L283.5,84.9 L284.3,85.5 L285.2,86.2 L286.0,86.8 L286.8,87.4 L287.6,88.1 L288.3,88.8 L289.1,89.4 L289.8,90.1 L290.6,90.8 L291.3,91.5 L292.0,92.1 L292.7,92.8 L293.4,93.5 L294.0,94.2 L294.7,94.9 L295.4,95.7 L296.0,96.4 L296.6,97.1 L297.3,97.8 L297.9,98.5 L298.5,99.3 L299.1,100.0 L299.7,100.7 L300.3,101.5 L300.9,102.2 L301.5,102.9 L302.0,103.7 L302.6,104.4 L303.2,105.2 L303.7,105.9 L304.3,106.7 L304.9,107.4 L305.4,108.2 L306.0,108.9 L306.5,109.7 L307.1,110.5 L307.6,111.2 L308.1,112.0 L308.7,112.7 L309.2,113.5 L309.8,114.2 L310.3,115.0 L310.8,115.8 L311.4,116.5 L311.9,117.3 L312.5,118.0 L313.0,118.8 L313.5,119.5 L314.1,120.3 L314.6,121.1 L315.2,121.8 L315.7,122.6 L316.3,123.3 L316.8,124.1 L317.4,124.8 L318.0,125.6 L318.5,126.3 L319.1,127.1 L319.7,127.8 L319.9,128.0" fill="none" stroke="#c1440e" stroke-width="1.1"/>
    <path d="M20.1,128.3 L20.7,129.0 L21.3,129.8 L21.9,130.5 L22.5,131.2 L23.1,131.9 L23.7,132.7 L24.4,133.4 L25.0,134.1 L25.7,134.8 L26.3,135.5 L27.0,136.2 L27.7,136.9 L28.4,137.6 L29.1,138.3 L29.8,139.0 L30.5,139.7 L31.2,140.4 L32.0,141.0 L32.8,141.7 L33.5,142.3 L34.3,143.0 L35.2,143.6 L36.0,144.3 L36.8,144.9 L37.7,145.5 L38.6,146.1 L39.5,146.7 L40.4,147.3 L41.3,147.9 L42.3,148.5 L43.2,149.0 L44.2,149.6 L45.3,150.1 L46.3,150.6 L47.4,151.1 L48.5,151.6 L49.6,152.1 L50.7,152.6 L51.9,153.0 L53.0,153.5 L54.2,153.9 L55.5,154.3 L56.7,154.7 L58.0,155.0 L59.3,155.4 L60.6,155.7 L61.9,156.0 L63.3,156.3 L64.7,156.6 L66.0,156.8 L67.5,157.0 L68.9,157.2 L70.3,157.4 L71.8,157.6 L73.3,157.7 L74.7,157.8 L76.2,157.9 L77.7,158.0 L79.2,158.0 L80.7,158.0 L82.2,158.0 L83.7,157.9 L85.2,157.9 L86.7,157.8 L88.1,157.7 L89.6,157.5 L91.0,157.4 L92.5,157.2 L93.9,157.0 L95.3,156.7 L96.7,156.5 L98.1,156.2 L99.4,155.9 L100.7,155.6 L102.1,155.3 L103.3,154.9 L104.6,154.5 L105.8,154.2 L107.1,153.7 L108.3,153.3 L109.4,152.9 L110.6,152.4 L111.7,151.9 L112.8,151.5 L113.9,151.0 L114.9,150.4 L116.0,149.9 L117.0,149.4 L118.0,148.8 L118.9,148.3 L119.9,147.7 L120.8,147.1 L121.7,146.5 L122.6,145.9 L123.5,145.3 L124.3,144.7 L125.2,144.1 L126.0,143.4 L126.8,142.8 L127.6,142.1 L128.4,141.5 L129.1,140.8 L129.9,140.1 L130.6,139.5 L131.3,138.8 L132.1,138.1 L132.8,137.4 L133.4,136.7 L134.1,136.0 L134.8,135.3 L135.4,134.6 L136.1,133.9 L136.7,133.1 L137.4,132.4 L138.0,131.7 L138.6,131.0 L139.2,130.2 L139.8,129.5 L140.4,128.8 L141.0,128.0 L141.6,127.3 L142.2,126.6 L142.7,125.8 L143.3,125.1 L143.9,124.3 L144.4,123.6 L145.0,122.8 L145.5,122.1 L146.1,121.3 L146.6,120.6 L147.2,119.8 L147.7,119.0 L148.3,118.3 L148.8,117.5 L149.3,116.8 L149.9,116.0 L150.4,115.3 L151.0,114.5 L151.5,113.7 L152.0,113.0 L152.6,112.2 L153.1,111.5 L153.7,110.7 L154.2,109.9 L154.7,109.2 L155.3,108.4 L155.8,107.7 L156.4,106.9 L157.0,106.2 L157.5,105.4 L158.1,104.7 L158.7,103.9 L159.2,103.2 L159.8,102.5 L160.4,101.7 L161.0,101.0 L161.6,100.2 L162.2,99.5 L162.8,98.8 L163.4,98.1 L164.0,97.3 L164.7,96.6 L165.3,95.9 L166.0,95.2 L166.6,94.5 L167.3,93.8 L168.0,93.1 L168.7,92.4 L169.4,91.7 L170.1,91.0 L170.8,90.3 L171.5,89.6 L172.3,89.0 L173.1,88.3 L173.8,87.7 L174.6,87.0 L175.5,86.4 L176.3,85.7 L177.1,85.1 L178.0,84.5 L178.9,83.9 L179.8,83.3 L180.7,82.7 L181.6,82.1 L182.6,81.5 L183.5,81.0 L184.5,80.4 L185.6,79.9 L186.6,79.4 L187.7,78.9 L188.8,78.4 L189.9,77.9 L191.0,77.4 L192.1,77.0 L193.3,76.5 L194.5,76.1 L195.8,75.7 L197.0,75.3 L198.3,75.0 L199.6,74.6 L200.9,74.3 L202.2,74.0 L203.6,73.7 L205.0,73.4 L206.3,73.2 L207.8,73.0 L209.2,72.8 L210.6,72.6 L212.1,72.4 L213.6,72.3 L215.0,72.2 L216.5,72.1 L218.0,72.0 L219.5,72.0 L221.0,72.0 L222.5,72.0 L224.0,72.1 L225.5,72.1 L226.9,72.2 L228.4,72.3 L229.9,72.5 L231.3,72.6 L232.8,72.8 L234.2,73.0 L235.6,73.3 L237.0,73.5 L238.4,73.8 L239.7,74.1 L241.0,74.4 L242.4,74.7 L243.6,75.1 L244.9,75.5 L246.1,75.8 L247.4,76.3 L248.6,76.7 L249.7,77.1 L250.9,77.6 L252.0,78.1 L253.1,78.5 L254.2,79.0 L255.2,79.6 L256.3,80.1 L257.3,80.6 L258.3,81.2 L259.2,81.7 L260.2,82.3 L261.1,82.9 L262.0,83.5 L262.9,84.1 L263.8,84.7 L264.6,85.3 L265.5,85.9 L266.3,86.6 L267.1,87.2 L267.9,87.9 L268.7,88.5 L269.4,89.2 L270.2,89.9 L270.9,90.5 L271.6,91.2 L272.4,91.9 L273.1,92.6 L273.7,93.3 L274.4,94.0 L275.1,94.7 L275.7,95.4 L276.4,96.1 L277.0,96.9 L277.7,97.6 L278.3,98.3 L278.9,99.0 L279.5,99.8 L280.1,100.5 L280.7,101.2 L281.3,102.0 L281.9,102.7 L282.4,103.4 L283.0,104.2 L283.6,104.9 L284.2,105.7 L284.7,106.4 L285.3,107.2 L285.8,107.9 L286.4,108.7 L286.9,109.4 L287.5,110.2 L288.0,111.0 L288.6,111.7 L289.1,112.5 L289.6,113.2 L290.2,114.0 L290.7,114.7 L291.2,115.5 L291.8,116.3 L292.3,117.0 L292.9,117.8 L293.4,118.5 L294.0,119.3 L294.5,120.1 L295.0,120.8 L295.6,121.6 L296.1,122.3 L296.7,123.1 L297.3,123.8 L297.8,124.6 L298.4,125.3 L298.9,126.1 L299.5,126.8 L300.1,127.5 L300.7,128.3 L301.3,129.0 L301.9,129.8 L302.5,130.5 L303.1,131.2 L303.7,131.9 L304.3,132.7 L305.0,133.4 L305.6,134.1 L306.3,134.8 L306.9,135.5 L307.6,136.2 L308.3,136.9 L309.0,137.6 L309.7,138.3 L310.4,139.0 L311.1,139.7 L311.8,140.4 L312.6,141.0 L313.4,141.7 L314.1,142.3 L314.9,143.0 L315.7,143.6 L316.6,144.3 L317.4,144.9 L318.3,145.5 L319.2,146.1 L319.8,146.5" fill="none" stroke="#c1440e" stroke-width="1.1"/>
    <path d="M20.1,146.7 L21.0,147.3 L21.9,147.9 L22.9,148.5 L23.8,149.0 L24.8,149.6 L25.9,150.1 L26.9,150.6 L28.0,151.1 L29.0,151.6 L30.2,152.1 L31.3,152.6 L32.4,153.0 L33.6,153.5 L34.8,153.9 L36.0,154.3 L37.3,154.7 L38.6,155.0 L39.9,155.4 L41.2,155.7 L42.5,156.0 L43.9,156.3 L45.2,156.6 L46.6,156.8 L48.1,157.0 L49.5,157.2 L50.9,157.4 L52.4,157.6 L53.8,157.7 L55.3,157.8 L56.8,157.9 L58.3,158.0 L59.8,158.0 L61.3,158.0 L62.8,158.0 L64.3,157.9 L65.8,157.9 L67.2,157.8 L68.7,157.7 L70.2,157.5 L71.6,157.4 L73.1,157.2 L74.5,157.0 L75.9,156.7 L77.3,156.5 L78.7,156.2 L80.0,155.9 L81.3,155.6 L82.6,155.3 L83.9,154.9 L85.2,154.5 L86.4,154.2 L87.7,153.7 L88.8,153.3 L90.0,152.9 L91.2,152.4 L92.3,151.9 L93.4,151.5 L94.5,151.0 L95.5,150.4 L96.6,149.9 L97.6,149.4 L98.6,148.8 L99.5,148.3 L100.5,147.7 L101.4,147.1 L102.3,146.5 L103.2,145.9 L104.1,145.3 L104.9,144.7 L105.8,144.1 L106.6,143.4 L107.4,142.8 L108.2,142.1 L109.0,141.5 L109.7,140.8 L110.5,140.1 L111.2,139.5 L111.9,138.8 L112.7,138.1 L113.3,137.4 L114.0,136.7 L114.7,136.0 L115.4,135.3 L116.0,134.6 L116.7,133.9 L117.3,133.1 L118.0,132.4 L118.6,131.7 L119.2,131.0 L119.8,130.2 L120.4,129.5 L121.0,128.8 L121.6,128.0 L122.2,127.3 L122.7,126.6 L123.3,125.8 L123.9,125.1 L124.4,124.3 L125.0,123.6 L125.6,122.8 L126.1,122.1 L126.7,121.3 L127.2,120.6 L127.8,119.8 L128.3,119.0 L128.8,118.3 L129.4,117.5 L129.9,116.8 L130.5,116.0 L131.0,115.3 L131.5,114.5 L132.1,113.7 L132.6,113.0 L133.2,112.2 L133.7,111.5 L134.2,110.7 L134.8,109.9 L135.3,109.2 L135.9,108.4 L136.4,107.7 L137.0,106.9 L137.5,106.2 L138.1,105.4 L138.7,104.7 L139.2,103.9 L139.8,103.2 L140.4,102.5 L141.0,101.7 L141.6,101.0 L142.2,100.2 L142.8,99.5 L143.4,98.8 L144.0,98.1 L144.6,97.3 L145.3,96.6 L145.9,95.9 L146.6,95.2 L147.2,94.5 L147.9,93.8 L148.6,93.1 L149.3,92.4 L150.0,91.7 L150.7,91.0 L151.4,90.3 L152.1,89.6 L152.9,89.0 L153.7,88.3 L154.4,87.7 L155.2,87.0 L156.0,86.4 L156.9,85.7 L157.7,85.1 L158.6,84.5 L159.5,83.9 L160.4,83.3 L161.3,82.7 L162.2,82.1 L163.2,81.5 L164.1,81.0 L165.1,80.4 L166.2,79.9 L167.2,79.4 L168.3,78.9 L169.3,78.4 L170.5,77.9 L171.6,77.4 L172.7,77.0 L173.9,76.5 L175.1,76.1 L176.3,75.7 L177.6,75.3 L178.9,75.0 L180.2,74.6 L181.5,74.3 L182.8,74.0 L184.2,73.7 L185.5,73.4 L186.9,73.2 L188.4,73.0 L189.8,72.8 L191.2,72.6 L192.7,72.4 L194.1,72.3 L195.6,72.2 L197.1,72.1 L198.6,72.0 L200.1,72.0 L201.6,72.0 L203.1,72.0 L204.6,72.1 L206.1,72.1 L207.5,72.2 L209.0,72.3 L210.5,72.5 L211.9,72.6 L213.4,72.8 L214.8,73.0 L216.2,73.3 L217.6,73.5 L219.0,73.8 L220.3,74.1 L221.6,74.4 L222.9,74.7 L224.2,75.1 L225.5,75.5 L226.7,75.8 L228.0,76.3 L229.1,76.7 L230.3,77.1 L231.5,77.6 L232.6,78.1 L233.7,78.5 L234.8,79.0 L235.8,79.6 L236.9,80.1 L237.9,80.6 L238.9,81.2 L239.8,81.7 L240.8,82.3 L241.7,82.9 L242.6,83.5 L243.5,84.1 L244.4,84.7 L245.2,85.3 L246.1,85.9 L246.9,86.6 L247.7,87.2 L248.5,87.9 L249.3,88.5 L250.0,89.2 L250.8,89.9 L251.5,90.5 L252.2,91.2 L252.9,91.9 L253.6,92.6 L254.3,93.3 L255.0,94.0 L255.7,94.7 L256.3,95.4 L257.0,96.1 L257.6,96.9 L258.3,97.6 L258.9,98.3 L259.5,99.0 L260.1,99.8 L260.7,100.5 L261.3,101.2 L261.9,102.0 L262.5,102.7 L263.0,103.4 L263.6,104.2 L264.2,104.9 L264.7,105.7 L265.3,106.4 L265.9,107.2 L266.4,107.9 L267.0,108.7 L267.5,109.4 L268.1,110.2 L268.6,111.0 L269.1,111.7 L269.7,112.5 L270.2,113.2 L270.8,114.0 L271.3,114.7 L271.8,115.5 L272.4,116.3 L272.9,117.0 L273.5,117.8 L274.0,118.5 L274.5,119.3 L275.1,120.1 L275.6,120.8 L276.2,121.6 L276.7,122.3 L277.3,123.1 L277.8,123.8 L278.4,124.6 L279.0,125.3 L279.5,126.1 L280.1,126.8 L280.7,127.5 L281.3,128.3 L281.9,129.0 L282.5,129.8 L283.1,130.5 L283.7,131.2 L284.3,131.9 L284.9,132.7 L285.6,133.4 L286.2,134.1 L286.8,134.8 L287.5,135.5 L288.2,136.2 L288.9,136.9 L289.5,137.6 L290.3,138.3 L291.0,139.0 L291.7,139.7 L292.4,140.4 L293.2,141.0 L294.0,141.7 L294.7,142.3 L295.5,143.0 L296.3,143.6 L297.2,144.3 L298.0,144.9 L298.9,145.5 L299.8,146.1 L300.6,146.7 L301.6,147.3 L302.5,147.9 L303.5,148.5 L304.4,149.0 L305.4,149.6 L306.5,150.1 L307.5,150.6 L308.6,151.1 L309.6,151.6 L310.7,152.1 L311.9,152.6 L313.0,153.0 L314.2,153.5 L315.4,153.9 L316.6,154.3 L317.9,154.7 L319.2,155.0 L319.6,155.2" fill="none" stroke="#c1440e" stroke-width="1.1"/>
    <path d="M20.0,155.3 L21.3,155.6 L22.7,155.9 L24.0,156.2 L25.4,156.5 L26.8,156.7 L28.2,157.0 L29.6,157.2 L31.0,157.4 L32.5,157.5 L34.0,157.7 L35.4,157.8 L36.9,157.9 L38.4,157.9 L39.9,158.0 L41.4,158.0 L42.9,158.0 L44.4,158.0 L45.9,157.9 L47.3,157.8 L48.8,157.7 L50.3,157.6 L51.7,157.4 L53.2,157.2 L54.6,157.0 L56.0,156.8 L57.4,156.6 L58.8,156.3 L60.2,156.0 L61.5,155.7 L62.8,155.4 L64.1,155.0 L65.4,154.7 L66.6,154.3 L67.8,153.9 L69.0,153.5 L70.2,153.0 L71.4,152.6 L72.5,152.1 L73.6,151.6 L74.7,151.1 L75.8,150.6 L76.8,150.1 L77.8,149.6 L78.8,149.0 L79.8,148.5 L80.8,147.9 L81.7,147.3 L82.6,146.7 L83.5,146.1 L84.4,145.5 L85.2,144.9 L86.1,144.3 L86.9,143.6 L87.7,143.0 L88.5,142.3 L89.3,141.7 L90.1,141.0 L90.8,140.4 L91.6,139.7 L92.3,139.0 L93.0,138.3 L93.7,137.6 L94.4,136.9 L95.1,136.2 L95.8,135.5 L96.4,134.8 L97.1,134.1 L97.7,133.4 L98.3,132.7 L99.0,131.9 L99.6,131.2 L100.2,130.5 L100.8,129.8 L101.4,129.0 L102.0,128.3 L102.6,127.5 L103.1,126.8 L103.7,126.1 L104.3,125.3 L104.9,124.6 L105.4,123.8 L106.0,123.1 L106.5,122.3 L107.1,121.6 L107.6,120.8 L108.2,120.1 L108.7,119.3 L109.3,118.5 L109.8,117.8 L110.3,117.0 L110.9,116.3 L111.4,115.5 L111.8,115.0" fill="none" stroke="#c1440e" stroke-width="1.1"/>
    <circle cx="170.0" cy="115.0" r="2.2" fill="#5aa0d8"/>
    <text x="168.0" y="125.0" text-anchor="end" fill="#5aa0d8">1</text>
    <circle cx="150.6" cy="115.0" r="2.2" fill="#5aa0d8"/>
    <text x="148.6" y="125.0" text-anchor="end" fill="#5aa0d8">2</text>
    <circle cx="131.2" cy="115.0" r="2.2" fill="#5aa0d8"/>
    <text x="129.2" y="125.0" text-anchor="end" fill="#5aa0d8">3</text>
    <text x="6" y="208">Blue dots 1, 2, 3: where each orbit crosses the equator going north.</text>
    <text x="6" y="226">The station goes round in 93 minutes. Meanwhile the Earth turns 23° under it, so each new</text>
    <text x="6" y="235">wave starts 23° farther west. In about a day the waves fill in every part of the Earth between</text>
    <text x="6" y="244">51.6° N and 51.6° S, but the station never flies over the poles.</text>
  </g>
</svg>
</div>

The waves do not repeat, because the Earth turns underneath. In the 93 minutes the station takes to go round, the
Earth turns 23°, so each orbit crosses the equator 23° farther west than the one before (Figure A). Over a day the
waves fill in the whole band between 51.6° N and 51.6° S. This is why you can see the station from most of the
world, but not from near the poles (book 1,
[section 16.3](../night-sky/16-Satellites-and-the-Space-Station.md#iss)).

A satellite on a polar orbit, tilted near 90°, passes over the whole Earth in time, which is just what a camera
satellite wants.

??? note "Sources"
    - Ground tracks: Wikipedia, [Ground track](https://en.wikipedia.org/wiki/Ground_track) (weaker).
    - The station's tilt and period: Wikipedia, International Space Station (above). The 23°: our arithmetic, section
      14.9. The track in Figure A is our calculation for a circular orbit, leaving out the small turning of section
      14.4.

## 14.3 Hanging still { #geo }

At 35,786 km above the equator, a satellite goes round once a day, in step with the Earth, and seems to hang still in
the sky (book 1, [section 16.6](../night-sky/16-Satellites-and-the-Space-Station.md#heights)). Herman Potočnik
described such orbits in 1928, as places for space stations. Arthur C. Clarke made the idea famous in 1945, in a paper
in *Wireless World* about using three of them to relay radio round the world.

The first satellite to go round once a day, **Syncom 2**, was launched in 1963, but its orbit was tilted, so
it drifted north and south. **Syncom 3**, launched in 1964, was the first truly geostationary satellite. It sat near
the International Date Line and carried television of the **1964 Olympic Games in Tokyo** across the Pacific to the
United States.

Today the ring above the equator is busy. Each satellite is given a "slot" above a particular longitude. Weather
satellites there watch a whole face of the Earth at once: Russia's Elektro-L, Japan's Himawari, China's Fengyun and
India's INSAT, among others. When a geostationary satellite is worn out, it is pushed a little higher, into a
**graveyard orbit**, so that it cannot collide with the working ones.

There is one catch. A geostationary satellite sits over the equator, so from the far north it is low in the southern
sky, or below the horizon altogether. Section 14.5 shows what the Soviet Union did about that.

??? note "Sources"
    - Potočnik in 1928, Clarke's 1945 paper in *Wireless World*, slots, the weather satellites Elektro-L, Himawari,
      Fengyun and INSAT, and graveyard orbits: Wikipedia,
      [Geostationary orbit](https://en.wikipedia.org/wiki/Geostationary_orbit) (weaker).
    - Syncom 2 in 1963, the first geosynchronous communications satellite; Syncom 3 in 1964, the first geostationary
      satellite, near the International Date Line, used to send the 1964 Summer Olympics in Tokyo to the United States:
      Wikipedia, [Syncom](https://en.wikipedia.org/wiki/Syncom) (weaker).
    - Three satellites for worldwide coverage in Clarke's paper, and Syncom 2's north-south drift: standard.
    - Low in the sky from high latitudes: Wikipedia, Molniya orbit (above), and standard.

## 14.4 The bulge that turns orbits { #bulge }

The Earth is not a perfect ball. Its spin makes it bulge at the equator, about 21 km wider in radius than at the
poles. That extra ring of mass pulls a little harder on a satellite as it passes over the equator, and the result is
a slow twist: the whole plane of the orbit turns round the Earth's axis. This is called **nodal precession**.

For an ordinary tilted orbit going eastwards, the plane turns westwards by a few degrees a day. A satellite 800 km up
on an orbit tilted 56° has its plane swing right round in 98 days. The more steeply the orbit is tilted, the slower
the turning; a polar orbit does not turn at all. And an orbit tilted past 90°, going backwards, turns **eastwards**.

**Sun-synchronous orbits.** The Sun moves eastwards round our sky by about 1° a day, once a year. Pick a backward
tilt that makes the orbit turn eastwards by exactly that much, and the orbit keeps the same angle to the Sun all year.
For a satellite 600 to 800 km up, the tilt needed is about 98° (section 14.10). Such a satellite crosses the equator
at the same local time on every orbit, for example at 3 o'clock every afternoon. Photographs taken weeks or years
apart then have the same lighting, so changes on the ground stand out. A **dawn–dusk** orbit rides along the line
between day and night, so that its solar panels are always in sunshine.

??? note "Sources"
    - Nodal precession caused by the Earth's oblateness, a few degrees a day to the west, the worked example of 800 km
      and 56° giving 3.683° a day and a full turn in 98 days, eastward precession for retrograde orbits, and its use for
      sun-synchronous orbits: Wikipedia, [Nodal precession](https://en.wikipedia.org/wiki/Nodal_precession) (weaker).
    - Sun-synchronous orbits: passing at the same local mean solar time, an example crossing at about 15:00, the
      dawn–dusk orbit, typical heights and tilts, and their use for imaging and weather: Wikipedia, Sun-synchronous
      orbit (above).
    - The Earth's equatorial radius of 6,378.1 km and polar radius of 6,356.8 km: NASA,
      [Earth Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html). A polar orbit not turning:
      $\cos 90° = 0$ in section 14.10.

## 14.5 Molniya: an orbit for the far north { #molniya }

For the Soviet Union, geostationary orbit was a poor fit. Much of the country lies so far north that a satellite over
the equator would be low in the sky, and reaching geostationary orbit from Soviet launch sites, far from the equator,
took a lot of energy (chapter 13). So in the 1960s the design bureau OKB-1 chose a different orbit: a long, thin
ellipse, tilted 63.4°, with its high point over Soviet territory. The first satellite to use it successfully,
**Molniya 1-1**, was launched on 23 April 1965. *Molniya* means "lightning", for the speed at which it flashes past
its low point.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="A Molniya orbit drawn to scale in its own plane, a long thin ellipse with the Earth near the bottom end. The satellite is marked at every hour of its 12-hour orbit. Near the Earth the dots are far apart, because it rushes past its low point in about an hour. Near the top, about 40,000 km up, the dots crowd together, because it moves slowly there. The top half of the orbit lies over the northern hemisphere, so the satellite spends about 11 of every 12 hours north of the equator, high in the sky of Russia and other northern countries.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">A Molniya orbit, to scale, marked every hour</text>
    <path d="M104.0,205.3 L105.0,205.3 L106.1,205.3 L107.1,205.2 L108.1,205.1 L109.2,205.0 L110.2,204.8 L111.2,204.7 L112.3,204.5 L113.3,204.2 L114.3,204.0 L115.3,203.7 L116.4,203.4 L117.4,203.1 L118.4,202.7 L119.4,202.3 L120.4,201.9 L121.4,201.5 L122.4,201.0 L123.4,200.5 L124.3,200.0 L125.3,199.5 L126.3,198.9 L127.2,198.3 L128.2,197.7 L129.1,197.1 L130.1,196.4 L131.0,195.8 L131.9,195.0 L132.8,194.3 L133.7,193.6 L134.6,192.8 L135.5,192.0 L136.4,191.2 L137.2,190.3 L138.1,189.5 L138.9,188.6 L139.8,187.7 L140.6,186.7 L141.4,185.8 L142.2,184.8 L143.0,183.8 L143.8,182.8 L144.6,181.8 L145.3,180.7 L146.0,179.6 L146.8,178.5 L147.5,177.4 L148.2,176.3 L148.9,175.2 L149.5,174.0 L150.2,172.8 L150.9,171.6 L151.5,170.4 L152.1,169.2 L152.7,167.9 L153.3,166.7 L153.9,165.4 L154.4,164.1 L155.0,162.8 L155.5,161.5 L156.0,160.1 L156.5,158.8 L157.0,157.4 L157.4,156.1 L157.9,154.7 L158.3,153.3 L158.7,151.9 L159.1,150.5 L159.5,149.1 L159.9,147.6 L160.2,146.2 L160.5,144.7 L160.9,143.3 L161.2,141.8 L161.4,140.3 L161.7,138.9 L161.9,137.4 L162.2,135.9 L162.4,134.4 L162.6,132.9 L162.7,131.4 L162.9,129.9 L163.0,128.3 L163.1,126.8 L163.2,125.3 L163.3,123.8 L163.4,122.2 L163.4,120.7 L163.4,119.2 L163.5,117.7 L163.4,116.1 L163.4,114.6 L163.4,113.1 L163.3,111.5 L163.2,110.0 L163.1,108.5 L163.0,107.0 L162.9,105.5 L162.7,103.9 L162.6,102.4 L162.4,100.9 L162.2,99.4 L161.9,97.9 L161.7,96.4 L161.4,95.0 L161.2,93.5 L160.9,92.0 L160.5,90.6 L160.2,89.1 L159.9,87.7 L159.5,86.2 L159.1,84.8 L158.7,83.4 L158.3,82.0 L157.9,80.6 L157.4,79.2 L157.0,77.9 L156.5,76.5 L156.0,75.2 L155.5,73.8 L155.0,72.5 L154.4,71.2 L153.9,69.9 L153.3,68.6 L152.7,67.4 L152.1,66.1 L151.5,64.9 L150.9,63.7 L150.2,62.5 L149.5,61.3 L148.9,60.1 L148.2,59.0 L147.5,57.9 L146.8,56.8 L146.0,55.7 L145.3,54.6 L144.6,53.5 L143.8,52.5 L143.0,51.5 L142.2,50.5 L141.4,49.5 L140.6,48.6 L139.8,47.7 L138.9,46.7 L138.1,45.9 L137.2,45.0 L136.4,44.1 L135.5,43.3 L134.6,42.5 L133.7,41.7 L132.8,41.0 L131.9,40.3 L131.0,39.6 L130.1,38.9 L129.1,38.2 L128.2,37.6 L127.2,37.0 L126.3,36.4 L125.3,35.8 L124.3,35.3 L123.4,34.8 L122.4,34.3 L121.4,33.8 L120.4,33.4 L119.4,33.0 L118.4,32.6 L117.4,32.2 L116.4,31.9 L115.3,31.6 L114.3,31.3 L113.3,31.1 L112.3,30.9 L111.2,30.7 L110.2,30.5 L109.2,30.3 L108.1,30.2 L107.1,30.1 L106.1,30.1 L105.0,30.0 L104.0,30.0 L103.0,30.0 L101.9,30.1 L100.9,30.1 L99.9,30.2 L98.8,30.3 L97.8,30.5 L96.8,30.7 L95.7,30.9 L94.7,31.1 L93.7,31.3 L92.7,31.6 L91.6,31.9 L90.6,32.2 L89.6,32.6 L88.6,33.0 L87.6,33.4 L86.6,33.8 L85.6,34.3 L84.6,34.8 L83.7,35.3 L82.7,35.8 L81.7,36.4 L80.8,37.0 L79.8,37.6 L78.9,38.2 L77.9,38.9 L77.0,39.6 L76.1,40.3 L75.2,41.0 L74.3,41.7 L73.4,42.5 L72.5,43.3 L71.6,44.1 L70.8,45.0 L69.9,45.9 L69.1,46.7 L68.2,47.7 L67.4,48.6 L66.6,49.5 L65.8,50.5 L65.0,51.5 L64.2,52.5 L63.4,53.5 L62.7,54.6 L62.0,55.7 L61.2,56.8 L60.5,57.9 L59.8,59.0 L59.1,60.1 L58.5,61.3 L57.8,62.5 L57.1,63.7 L56.5,64.9 L55.9,66.1 L55.3,67.4 L54.7,68.6 L54.1,69.9 L53.6,71.2 L53.0,72.5 L52.5,73.8 L52.0,75.2 L51.5,76.5 L51.0,77.9 L50.6,79.2 L50.1,80.6 L49.7,82.0 L49.3,83.4 L48.9,84.8 L48.5,86.2 L48.1,87.7 L47.8,89.1 L47.5,90.6 L47.1,92.0 L46.8,93.5 L46.6,95.0 L46.3,96.4 L46.1,97.9 L45.8,99.4 L45.6,100.9 L45.4,102.4 L45.3,103.9 L45.1,105.5 L45.0,107.0 L44.9,108.5 L44.8,110.0 L44.7,111.5 L44.6,113.1 L44.6,114.6 L44.6,116.1 L44.5,117.7 L44.6,119.2 L44.6,120.7 L44.6,122.2 L44.7,123.8 L44.8,125.3 L44.9,126.8 L45.0,128.3 L45.1,129.9 L45.3,131.4 L45.4,132.9 L45.6,134.4 L45.8,135.9 L46.1,137.4 L46.3,138.9 L46.6,140.3 L46.8,141.8 L47.1,143.3 L47.5,144.7 L47.8,146.2 L48.1,147.6 L48.5,149.1 L48.9,150.5 L49.3,151.9 L49.7,153.3 L50.1,154.7 L50.6,156.1 L51.0,157.4 L51.5,158.8 L52.0,160.1 L52.5,161.5 L53.0,162.8 L53.6,164.1 L54.1,165.4 L54.7,166.7 L55.3,167.9 L55.9,169.2 L56.5,170.4 L57.1,171.6 L57.8,172.8 L58.5,174.0 L59.1,175.2 L59.8,176.3 L60.5,177.4 L61.2,178.5 L62.0,179.6 L62.7,180.7 L63.4,181.8 L64.2,182.8 L65.0,183.8 L65.8,184.8 L66.6,185.8 L67.4,186.7 L68.2,187.7 L69.1,188.6 L69.9,189.5 L70.8,190.3 L71.6,191.2 L72.5,192.0 L73.4,192.8 L74.3,193.6 L75.2,194.3 L76.1,195.0 L77.0,195.8 L77.9,196.4 L78.9,197.1 L79.8,197.7 L80.8,198.3 L81.7,198.9 L82.7,199.5 L83.7,200.0 L84.6,200.5 L85.6,201.0 L86.6,201.5 L87.6,201.9 L88.6,202.3 L89.6,202.7 L90.6,203.1 L91.6,203.4 L92.7,203.7 L93.7,204.0 L94.7,204.2 L95.7,204.5 L96.8,204.7 L97.8,204.8 L98.8,205.0 L99.9,205.1 L100.9,205.2 L101.9,205.3 L103.0,205.3 L104.0,205.3 Z" fill="none" stroke="#5aa0d8" stroke-width="1"/>
    <circle cx="104" cy="182.1" r="21.0" fill="#5aa0d8" fill-opacity="0.35" stroke="currentColor" stroke-width="0.5"/>
    <text x="104" y="185.1" text-anchor="middle">Earth</text>
    <line x1="64.0" y1="182.1" x2="144.0" y2="182.1" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <text x="146.0" y="185.1" fill="#555">equator</text>
    <circle cx="104.0" cy="205.3" r="2.2" fill="#c1440e"/>
    <text x="112.0" y="208.3" text-anchor="start">0 h, low point</text>
    <circle cx="48.3" cy="148.5" r="2.2" fill="#c1440e"/>
    <text x="43.3" y="151.5" text-anchor="end">1 h</text>
    <circle cx="45.7" cy="100.5" r="2.2" fill="#c1440e"/>
    <circle cx="55.1" cy="67.8" r="2.2" fill="#c1440e"/>
    <circle cx="69.4" cy="46.3" r="2.2" fill="#c1440e"/>
    <circle cx="86.2" cy="34.0" r="2.2" fill="#c1440e"/>
    <circle cx="104.0" cy="30.0" r="2.2" fill="#c1440e"/>
    <text x="104.0" y="24.0" text-anchor="middle">6 h, 40,000 km up</text>
    <circle cx="121.8" cy="34.0" r="2.2" fill="#c1440e"/>
    <circle cx="138.6" cy="46.3" r="2.2" fill="#c1440e"/>
    <circle cx="152.9" cy="67.8" r="2.2" fill="#c1440e"/>
    <circle cx="162.3" cy="100.5" r="2.2" fill="#c1440e"/>
    <circle cx="159.7" cy="148.5" r="2.2" fill="#c1440e"/>
    <text x="164.7" y="151.5" text-anchor="start">11 h</text>
    <line x1="230" y1="196" x2="263.0" y2="196" stroke="currentColor" stroke-width="1"/>
    <text x="230" y="192">10,000 km</text>
    <text x="200" y="60">The satellite crawls round</text>
    <text x="200" y="70">the top of its orbit and</text>
    <text x="200" y="80">rushes past the bottom</text>
    <text x="200" y="90">(Kepler's second law).</text>
    <text x="200" y="100"></text>
    <text x="200" y="110">It is north of the equator</text>
    <text x="200" y="120">for about 11 of every 12 hours,</text>
    <text x="200" y="130">high in the sky of Russia</text>
    <text x="200" y="140">and other northern lands.</text>
    <text x="6" y="226">The orbit is tilted 63.4° to the equator and takes 12 hours. Its high point stays over the north</text>
    <text x="6" y="235">because at that tilt the Earth's bulge does not turn the long axis round. Several such</text>
    <text x="6" y="244">satellites, taking turns, give round-the-clock coverage of the far north.</text>
  </g>
</svg>
</div>

The orbit takes 12 hours. By Kepler's second law (chapter 3) the satellite crawls round the top of its orbit, up to
40,000 km above the northern hemisphere, and rushes round the bottom. It spends about 11 of every 12 hours north of
the equator (Figure B), high in the sky over Russia or Canada. A few such satellites, taking turns, cover the north
all day.

**Why 63.4°?** The Earth's bulge does not only turn the plane of an orbit; it also turns the long axis of the ellipse
round within that plane. At a tilt of exactly 63.4° this second turning stops (section 14.10), so the high point stays
over the north without burning fuel to hold it there.

**Cousins.** A **Tundra** orbit uses the same tilt with a period of a whole day. From 2000 to 2016 the company
Sirius ran satellite radio from three satellites in Tundra orbits. Japan's navigation system QZSS uses two
geostationary satellites and three in Tundra-type orbits, so that one of them is always nearly overhead in Japan,
where tall buildings and mountains block much of the sky. A mirror-image Molniya orbit, with its high point over the
south, was once proposed to bring the internet to bases in Antarctica, with early money from the Australian Space
Research Programme, but it was never built.

??? note "Sources"
    - The Molniya orbit's 63.4° tilt, argument of perigee of 270°, half a sidereal day, the high energy needed for
      geostationary orbit from Russian latitudes, OKB-1, the apogee over Russian territory, Molniya 1-1 on 23 April
      1965, the name referring to the speed through perigee, apogee up to 40,000 km, coverage of Russia or Canada,
      multiple satellites needed for continuous coverage, 63.4° chosen so that the perigee does not drift without
      fuel, and the proposed inverted orbit for Antarctica funded at first by the Australian Space Research Programme:
      Wikipedia, Molniya orbit (above).
    - Tundra orbits at about 63.4° with a period of one sidereal day, and Sirius's three satellites from 2000 to 2016:
      Wikipedia, [Tundra orbit](https://en.wikipedia.org/wiki/Tundra_orbit) (weaker).
    - QZSS's two geostationary and three Tundra-type satellites: Wikipedia,
      [Quasi-Zenith Satellite System](https://en.wikipedia.org/wiki/Quasi-Zenith_Satellite_System) (weaker). Its
      purpose of keeping a satellite high over Japan's cities and mountains: standard.
    - The 11 hours: our arithmetic, section 14.9.

## 14.6 Finding your way { #gnss }

A navigation satellite carries an atomic clock and keeps broadcasting the time and its own position. A receiver on
the ground compares the times from four or more satellites; the differences tell it how far away each one is, and so
where it is. For this to work anywhere on Earth, many satellites must be spread round the sky, which is why they sit
in medium orbits on several tilted planes.

There are four worldwide systems and two regional ones.

- **GPS**, from the United States, working since 1978 and worldwide since 1994: up to 32 satellites on six planes
  tilted about 55°, 20,200 km up, each going round twice a day.
- **GLONASS**, Soviet and now Russian, first launched in 1982, worldwide since 1995 with 24 satellites.
- **BeiDou**, from China, which began over Asia and the Pacific and became worldwide in 2018; its last satellite was
  launched on 23 June 2020. Besides its medium-orbit satellites it uses geostationary and tilted day-long orbits.
- **Galileo**, from the European Union and ESA, whose first test satellite was launched on 28 December 2005, working
  since 15 December 2016.
- **QZSS** (Japan) and **NavIC** (India) cover their own regions. NavIC has seven satellites: three geostationary over
  the Indian Ocean and four on tilted day-long orbits, covering India and 1,500 km around it.

A phone today often listens to several of these at once. The clocks must also be corrected for Einstein's relativity:
seen from the ground, GPS clocks run 38 millionths of a second a day fast, which would add up to kilometres of error if
ignored (chapter 18).

??? note "Sources"
    - The four global systems and two regional ones, GPS operational since 1978 and global since 1994 with up to 32
      satellites in six planes, GLONASS (1982) with 24 satellites and global since 1995, BeiDou (2000) global in
      December 2018 and complete on 23 June 2020 with medium, geostationary and inclined orbits, Galileo (2005) with its
      first satellite on 28 December 2005 and working from 15 December 2016, and relativity applied to the clocks:
      Wikipedia, [Satellite navigation](https://en.wikipedia.org/wiki/Satellite_navigation) (weaker).
    - GPS at 20,200 km, about 55°, two orbits a sidereal day, and the 38 microseconds a day: Wikipedia, Global
      Positioning System (above).
    - NavIC's seven satellites, three in geostationary and four in geosynchronous orbits: Wikipedia, Satellite
      navigation (above). Three over the Indian Ocean, covering India and 1,500 km around: Wikipedia,
      [Indian Regional Navigation Satellite System](https://en.wikipedia.org/wiki/Indian_Regional_Navigation_Satellite_System)
      (weaker).
    - How a receiver finds its position from four clocks, and "kilometres of error": standard; 38 microseconds of light
      travel is $299{,}792 \times 0.000038 = 11$ km, our arithmetic.

## 14.7 Too crowded { #debris }

Every satellite that dies, every spent rocket stage, every flake of paint stays in orbit until the thin air drags it
down (chapter 1, [section 1.6](01-Falling-Round-the-Earth.md#decay)). Up there, things meet at many kilometres a
second, so even a small piece can wreck a satellite.

In 1978 Donald Kessler and Burton Cour-Palais of NASA warned of a chain reaction: once low orbit is crowded enough,
each collision makes debris that causes more collisions, and the amount of debris grows on its own. This is now called
the **Kessler syndrome**. Some events since have made it worse.

- **2007.** China destroyed one of its own weather satellites, Fengyun-1C, 865 km up, with a missile, in a test.
- **2009.** On 10 February, the working American satellite Iridium 33 and the dead Russian satellite Kosmos 2251 hit
  each other at 11.7 km/s, 789 km above Siberia. It was the first time two whole satellites had collided.
- **2021.** Russia destroyed its own satellite Kosmos 1408 with a missile, making 1,500 pieces large enough to track.

As of 2021 there were thought to be about 23,000 pieces of debris larger than 10 cm and 600,000 between 1 and 10 cm.
The space station sometimes has to move out of the way. Thousands of new Starlink satellites have added to the crowd
(book 1, [section 16.5](../night-sky/16-Satellites-and-the-Space-Station.md#crowded)).

??? note "Sources"
    - Kessler and Cour-Palais in 1978, the cascade, China's test of 11 January 2007 against FY-1C at 865 km, Russia's
      test of 15 November 2021 against Kosmos 1408 with 1,500 tracked pieces, and the 2021 estimates of 600,000 pieces
      of 1 to 10 cm and 23,000 larger: Wikipedia, [Kessler syndrome](https://en.wikipedia.org/wiki/Kessler_syndrome)
      (weaker).
    - Iridium 33 and Kosmos 2251 on 10 February 2009, 11.7 km/s, 789 km, the first collision between two satellites:
      Wikipedia, [2009 satellite collision](https://en.wikipedia.org/wiki/2009_satellite_collision) (weaker).
    - The space station moving to avoid debris: standard.

## 14.8 Orbits round Mars { #mars }

The same tricks work at Mars, and Mars's bulge is even bigger for its size: NASA gives Mars's $J_2$, the number that
measures the bulge's pull, as 1,960 millionths, against 1,083 millionths for the Earth. So Mars can have
sun-synchronous orbits too, and it only needs them to turn once a Mars year, 687 days.

- **NASA's Mars Reconnaissance Orbiter** has flown since 2006 in a nearly circular orbit 250 to 316 km up, taking
  about 112 minutes and tilted about 93°. Our arithmetic in section 14.10 shows that this is just the tilt at which
  Mars's bulge turns an orbit once a Mars year, so the orbiter keeps the same angle to the Sun.
- **India's Mars Orbiter Mission**, Mangalyaan, reached Mars on 24 September 2014, on India's first try, making India
  the first Asian country to orbit Mars. Its long ellipse, from 421.7 km to 76,993.6 km up and taking almost 73 hours,
  let its camera photograph the whole planet at once.
- **The United Arab Emirates' Hope** has orbited since 9 February 2021, from about 20,000 to 43,000 km up, once every
  55 hours. Over its orbit it sees Mars's weather at every time of day, which a sun-synchronous orbiter cannot do.

Mars also has its own stationary orbit, 17,032 km above its equator (book 1,
[section 16.8](../night-sky/16-Satellites-and-the-Space-Station.md#mars)). A relay satellite there could stay in
touch with one landing site all day.

??? note "Sources"
    - Mars's $J_2$ of 1,960.45 × 10⁻⁶ and the Earth's of 1,082.63 × 10⁻⁶: NASA,
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html) and Earth Fact Sheet (above).
      Sun-synchronous orbits possible around Mars: Wikipedia, Sun-synchronous orbit (above).
    - MRO's final orbit of 250 to 316 km, about 112 minutes and about 93° from September 2006: Wikipedia,
      [Mars Reconnaissance Orbiter](https://en.wikipedia.org/wiki/Mars_Reconnaissance_Orbiter) (weaker). That 93°
      matches a sun-synchronous orbit: our arithmetic, section 14.10.
    - The Mars Orbiter Mission in orbit from 24 September 2014, success at the first attempt, the first Asian nation
      to reach Mars orbit, periapsis 421.7 km, apoapsis 76,993.6 km, period 72 h 51 min 51 s, and full-disk images:
      Wikipedia, [Mars Orbiter Mission](https://en.wikipedia.org/wiki/Mars_Orbiter_Mission) (weaker).
    - Hope, in orbit from 9 February 2021, about 20,000 by 43,000 km, 55 hours, chosen to study the atmosphere and
      compare weather at different times of day: Wikipedia,
      [Emirates Mars Mission](https://en.wikipedia.org/wiki/Emirates_Mars_Mission) (weaker).
    - A stationary relay staying in touch with one site: standard.

## 14.9 Working it out { #working }

**Height from period.** From Kepler's third law with Newton's constant (chapter 5), a circular orbit of period $T$
round a body with $GM$ has radius

$$r = \left(\frac{GM\,T^2}{4\pi^2}\right)^{1/3}.$$

For the Earth, $GM = 398{,}600$ km³/s² and the radius at the equator is 6,378 km.

- **Geostationary.** $T$ is one turn of the Earth, a sidereal day of 86,164 s: $r = 42{,}164$ km, so the height is
  $42{,}164 - 6{,}378 = 35{,}786$ km.
- **GPS.** Half a sidereal day, 43,082 s: $r = 26{,}562$ km, a height of 20,184 km.
- **The space station.** At 400 km, $r = 6{,}778$ km and $T = 2\pi\sqrt{r^3/GM} = 5{,}554$ s, about 93 minutes.
- **Mars's stationary orbit.** With $GM = 42{,}828$ km³/s² and Mars's day of 88,642 s, $r = 20{,}428$ km, which is
  17,031 km above the equator, where the radius is 3,396 km.

**The westward step.** In 92.9 minutes the Earth turns $360° \times 92.9 \times 60 / 86{,}164 = 23.3°$.

**Molniya.** Its period is also half a sidereal day, so its semi-major axis is the same 26,562 km as GPS. With the high
point 39,700 km up, at 46,078 km from the centre, the low point is at $2 \times 26{,}562 - 46{,}078 = 7{,}046$ km from
the centre, 668 km up, and $e = (46{,}078 - 7{,}046)/(46{,}078 + 7{,}046) = 0.735$. Solving Kepler's equation
(chapter 4) shows it spends 92% of the time, 11 hours of the 12, on the half of the orbit north of the equator.

**Mars orbiters.** Hope's orbit has $a = 3{,}396 + (20{,}000 + 43{,}000)/2 = 34{,}896$ km, giving
$T = 2\pi\sqrt{a^3/GM} = 55.0$ hours, as reported. For the Mars Orbiter Mission, $a = 42{,}104$ km gives 72.9 hours.

| | Mars | Earth |
| --- | --- | --- |
| Stationary orbit, height | 17,031 km | 35,786 km |
| Low orbit period | 113 minutes at 283 km | 93 minutes at 400 km |
| Bulge, $J_2$ | 1,960 millionths | 1,083 millionths |
| Sun-synchronous orbit must turn | 0.524° a day | 0.986° a day |
| Sun-synchronous tilt, low orbit | about 92.6° at 283 km | about 98.6° at 800 km |

??? note "Sources"
    - $GM$, the equatorial radii, the sidereal day of the Earth, Mars's day of 24.6229 hours and $J_2$: NASA fact
      sheets (above). The year lengths of 365.24 and 686.98 days: the same fact sheets.
    - The reported periods of Hope and the Mars Orbiter Mission: section 14.8. The rest is our arithmetic.

## 14.10 The bulge, worked out { #derive }

For a nearly circular orbit of radius $a$, tilt $i$ and mean motion $n = 2\pi/T$, the bulge turns the orbit's plane at
the rate

$$\frac{d\Omega}{dt} = -\frac{3}{2}\, n\, J_2 \left(\frac{R}{a}\right)^2 \cos i,$$

where $R$ is the planet's equatorial radius. The minus sign means westwards when $\cos i > 0$, an eastward-going orbit;
for $i > 90°$, $\cos i < 0$ and the plane turns eastwards. At $i = 90°$ it does not turn.

**Check.** For the Earth at 800 km and $i = 56°$: $a = 7{,}178$ km, $n = 0.001038$ rad/s, and
$\tfrac{3}{2} \times 0.001038 \times 0.0010826 \times (6{,}378/7{,}178)^2 \times \cos 56° = 7.4 \times 10^{-7}$ rad/s,
or $3.68°$ a day westwards, the figure in section 14.4.

**Sun-synchronous.** Set the rate equal to the Sun's apparent motion, $+360°$ per year, and solve for $i$:

$$\cos i = -\frac{360°/\text{year}}{\tfrac{3}{2}\, n\, J_2 (R/a)^2}.$$

- **Earth, 800 km.** The bottom works out to $6.59°$ a day; the top is $0.986°$ a day. So $\cos i = -0.150$ and
  $i = 98.6°$.
- **Mars, 283 km.** With $R = 3{,}396$ km, $a = 3{,}679$ km, $J_2 = 0.00196$: the bottom is $11.5°$ a day and the top
  $360/687 = 0.524°$ a day. So $\cos i = -0.0456$ and $i = 92.6°$, close to MRO's 93°.

**The frozen ellipse.** The bulge also turns the long axis of an ellipse within its plane, at a rate proportional to
$2 - \tfrac{5}{2}\sin^2 i$. This is zero when $\sin^2 i = 4/5$, that is $i = 63.4°$ (or $116.6°$). That is the
Molniya tilt.

??? note "Sources"
    - The nodal precession formula and its worked example: Wikipedia, Nodal precession (above). The sun-synchronous
      condition: Wikipedia, Sun-synchronous orbit (above). The turning of the perigee with $J_2$ and the 63.4°:
      Wikipedia, Molniya orbit (above). The numbers are our arithmetic, with values from the NASA fact sheets.

## Check yourself { #check }

**1.** (beginner) Why does a satellite 400 km up go round faster than one 36,000 km up?

??? note "Answer"
    By Kepler's third law, a smaller orbit has a shorter period, and the pull of gravity is stronger closer in, so the
    satellite must move faster to stay up (chapter 7).

**2.** (beginner) The space station's orbit is tilted 51.6°. Can it fly over London, at 51.5° N? Over Oslo, at
59.9° N?

??? note "Answer"
    Over London, just. Over Oslo, never: it never goes farther north than 51.6°.

**3.** (beginner) What did Syncom 3 do in 1964?

??? note "Answer"
    It was the first geostationary satellite, and it carried television of the Tokyo Olympic Games across the Pacific
    to the United States.

**4.** (intermediate) Why are many Earth-photographing satellites tilted about 98°, going slightly backwards?

??? note "Answer"
    At that tilt the Earth's bulge turns the orbit's plane eastwards by about 1° a day, keeping pace with the Sun. The
    satellite then passes over each place at the same local time, so the lighting is the same in every picture.

**5.** (intermediate) Why did the Soviet Union use Molniya orbits instead of geostationary ones?

??? note "Answer"
    Much of the country is so far north that geostationary satellites are low in its sky, and reaching geostationary
    orbit from Soviet launch sites took a lot of energy. A Molniya satellite spends most of its 12-hour orbit high over
    the north.

**6.** (intermediate) Name the four worldwide navigation systems and who runs them.

??? note "Answer"
    GPS (United States), GLONASS (Russia), BeiDou (China) and Galileo (European Union and ESA).

**7.** (advanced) Find the radius and height of an orbit with a period of 6 hours round the Earth.

??? note "Answer"
    $r = (398{,}600 \times 21{,}600^2 / 4\pi^2)^{1/3} = (4.711 \times 10^{12})^{1/3} = 16{,}770$ km, about 10,400 km
    above the ground.

**8.** (expert) An orbit round the Earth 600 km up has a full bulge rate, $\tfrac{3}{2} n J_2 (R/a)^2$, of $7.27°$ a
day. What tilt makes it sun-synchronous?

??? note "Answer"
    $\cos i = -0.986 / 7.27 = -0.136$, so $i = 97.8°$.

## Summary

- An orbit's height sets its period: about 93 minutes for the space station, 12 hours for GPS, a day for geostationary
  satellites.
- A ground track is a wave reaching as far north and south as the orbit's tilt, stepping west as the Earth turns.
- Potočnik and Clarke described geostationary orbits; Syncom 3 was the first, in 1964.
- The Earth's bulge turns orbit planes. Tilted near 98°, an orbit keeps pace with the Sun: a sun-synchronous orbit.
- Molniya orbits, tilted 63.4° so their long axis stays put, give the far north satellites high in its sky.
- GPS, GLONASS, BeiDou and Galileo cover the world; QZSS and NavIC cover Japan and India.
- Collisions and missile tests have filled low orbit with debris, which could grow by itself.
- Round Mars, MRO uses a sun-synchronous orbit, while India's and the Emirates' orbiters use long ellipses to see the
  whole planet.

**Next:** [chapter 15, The road to Mars](15-The-Road-to-Mars.md), where we work out the cheapest path from the Earth
to Mars, why it takes about seven months, and why the chance to go comes only once every 26 months.

## Further reading

- Michel Capderou, *Satellites: Orbits and Missions*, Springer, 2005.
