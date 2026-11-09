# 19. Orbits at Mars

*Mars has two small moons and, right now, about half a dozen working spacecraft going round it. The moons move in
ways no moon of ours does: one rises in the west twice a day, the other hangs in the sky for two and a half days.
The spacecraft fly low to see the ground, high to see the whole planet, and pass messages from rovers to the Earth.
This chapter looks at all of them, at the stationary orbit nobody has used yet, and at why a spacecraft cannot
simply orbit Phobos.*

!!! abstract "In this chapter"
    **You will learn:**

    - why Phobos rises in the west and Deimos stays up for days
    - the two main ideas for where the moons came from, and the mission sent to decide
    - which spacecraft orbit Mars today, and why their orbits differ
    - how orbiters pass messages from rovers to the Earth, and how long each pass lasts
    - where a stationary orbit round Mars would be, and why it would be awkward to use
    - why a spacecraft cannot orbit Phobos in the usual way, and what it does instead
    - why Mars orbiters must stay up for decades, and which old ones are still there
    - how to work out sky motions, relay passes and the reach of a small moon's gravity

    **You need:** chapters 3, 6, 8 and 14.

    **Levels:** 19.1 to 19.3 are beginner; 19.4 to 19.7 are intermediate; 19.8 is advanced; 19.9 is expert.

## 19.1 Two moons in the Martian sky { #moons }

Asaph Hall, an American astronomer at the US Naval Observatory in Washington, found **Deimos** on 12 August 1877 and
**Phobos** on 18 August. Both are small, dark and lumpy. Phobos is about 26 by 23 by 18 km; Deimos has a mean radius
of only 6.2 km.

Phobos orbits 6,000 km above the ground, once every 7 hours 39 minutes. Mars turns once in 24 hours 37 minutes, so
Phobos goes round faster than the ground under it. Seen from the surface, it **rises in the west**, crosses the sky
in 4 hours 15 minutes or less, and sets in the east, about twice each Martian day, every 11 hours 6 minutes. It is so
low that from latitudes beyond 70.4° it never comes above the horizon at all.

Deimos is just outside the stationary orbit
([chapter 8, section 8.7](08-Tides.md#mars)), going round in 30.3 hours, only a little slower than Mars turns.
It **rises in the east** and sets in the west like our Moon, but very slowly. Our arithmetic gives about two and a
half days above the horizon, then nearly three days below it.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="How high Phobos and Deimos stand in the sky over about three days, for someone on Mars's equator. Phobos makes short, high arcs: it rises in the west, crosses the sky in about four and a quarter hours, sets in the east, and rises again about eleven hours after the last rise, so about seven arcs fit into three days. Deimos makes one long, low-climbing arc that lasts about two and a half days, because it moves only a little faster than the stars, rising in the east and setting in the west, and then it stays below the horizon for nearly three days.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">Phobos and Deimos in the sky, seen from Mars's equator</text>
    <line x1="40" y1="160.0" x2="326" y2="160.0" stroke="#cfc8bf" stroke-width="0.8"/>
    <text x="37" y="163.0" text-anchor="end">0°</text>
    <line x1="40" y1="118.0" x2="326" y2="118.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="37" y="121.0" text-anchor="end">30°</text>
    <line x1="40" y1="76.0" x2="326" y2="76.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="37" y="79.0" text-anchor="end">60°</text>
    <line x1="40" y1="34.0" x2="326" y2="34.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="37" y="37.0" text-anchor="end">90°</text>
    <text x="6" y="26">height above the horizon</text>
    <line x1="40.0" y1="160" x2="40.0" y2="163" stroke="currentColor" stroke-width="0.6"/>
    <text x="40.0" y="171" text-anchor="middle">0 h</text>
    <line x1="132.8" y1="160" x2="132.8" y2="163" stroke="currentColor" stroke-width="0.6"/>
    <text x="132.8" y="171" text-anchor="middle">24 h</text>
    <line x1="225.5" y1="160" x2="225.5" y2="163" stroke="currentColor" stroke-width="0.6"/>
    <text x="225.5" y="171" text-anchor="middle">48 h</text>
    <line x1="318.3" y1="160" x2="318.3" y2="163" stroke="currentColor" stroke-width="0.6"/>
    <text x="318.3" y="171" text-anchor="middle">72 h</text>
    <path d="M55.5,159.4 L55.7,157.1 L55.8,154.8 L56.0,152.5 L56.2,150.1 L56.4,147.7 L56.6,145.3 L56.8,142.8 L57.0,140.3 L57.2,137.8 L57.4,135.3 L57.6,132.7 L57.8,130.0 L58.0,127.4 L58.2,124.7 L58.4,122.0 L58.6,119.2 L58.7,116.4 L58.9,113.5 L59.1,110.7 L59.3,107.7 L59.5,104.8 L59.7,101.8 L59.9,98.7 L60.1,95.6 L60.3,92.5 L60.5,89.3 L60.7,86.1 L60.9,82.9 L61.1,79.6 L61.3,76.3 L61.5,73.0 L61.6,69.6 L61.8,66.2 L62.0,62.7 L62.2,59.3 L62.4,55.8 L62.6,52.3 L62.8,48.8 L63.0,45.2 L63.2,41.7 L63.4,38.1 L63.6,34.6 L63.8,37.0 L64.0,40.5 L64.2,44.1 L64.3,47.6 L64.5,51.1 L64.7,54.6 L64.9,58.1 L65.1,61.6 L65.3,65.0 L65.5,68.5 L65.7,71.9 L65.9,75.2 L66.1,78.5 L66.3,81.8 L66.5,85.1 L66.7,88.3 L66.9,91.5 L67.1,94.6 L67.2,97.7 L67.4,100.8 L67.6,103.8 L67.8,106.7 L68.0,109.7 L68.2,112.6 L68.4,115.4 L68.6,118.3 L68.8,121.0 L69.0,123.8 L69.2,126.5 L69.4,129.2 L69.6,131.8 L69.8,134.4 L70.0,137.0 L70.1,139.5 L70.3,142.0 L70.5,144.5 L70.7,146.9 L70.9,149.3 L71.1,151.7 L71.3,154.0 L71.5,156.4 L71.7,158.7" fill="none" stroke="#c1440e" stroke-width="1.2"/>
    <path d="M98.4,159.7 L98.6,157.4 L98.7,155.1 L98.9,152.7 L99.1,150.4 L99.3,148.0 L99.5,145.6 L99.7,143.1 L99.9,140.6 L100.1,138.1 L100.3,135.6 L100.5,133.0 L100.7,130.4 L100.9,127.7 L101.1,125.0 L101.3,122.3 L101.5,119.5 L101.6,116.7 L101.8,113.9 L102.0,111.0 L102.2,108.1 L102.4,105.1 L102.6,102.1 L102.8,99.1 L103.0,96.0 L103.2,92.9 L103.4,89.7 L103.6,86.5 L103.8,83.3 L104.0,80.0 L104.2,76.7 L104.3,73.4 L104.5,70.0 L104.7,66.6 L104.9,63.2 L105.1,59.7 L105.3,56.2 L105.5,52.7 L105.7,49.2 L105.9,45.7 L106.1,42.1 L106.3,38.6 L106.5,35.0 L106.7,36.5 L106.9,40.1 L107.1,43.6 L107.2,47.2 L107.4,50.7 L107.6,54.2 L107.8,57.7 L108.0,61.2 L108.2,64.6 L108.4,68.1 L108.6,71.4 L108.8,74.8 L109.0,78.1 L109.2,81.4 L109.4,84.7 L109.6,87.9 L109.8,91.1 L110.0,94.2 L110.1,97.3 L110.3,100.4 L110.5,103.4 L110.7,106.4 L110.9,109.3 L111.1,112.2 L111.3,115.1 L111.5,117.9 L111.7,120.7 L111.9,123.5 L112.1,126.2 L112.3,128.8 L112.5,131.5 L112.7,134.1 L112.9,136.7 L113.0,139.2 L113.2,141.7 L113.4,144.2 L113.6,146.6 L113.8,149.0 L114.0,151.4 L114.2,153.8 L114.4,156.1 L114.6,158.4" fill="none" stroke="#c1440e" stroke-width="1.2"/>
    <path d="M141.3,160.0 L141.5,157.7 L141.6,155.4 L141.8,153.0 L142.0,150.7 L142.2,148.3 L142.4,145.9 L142.6,143.4 L142.8,140.9 L143.0,138.4 L143.2,135.9 L143.4,133.3 L143.6,130.7 L143.8,128.0 L144.0,125.3 L144.2,122.6 L144.4,119.9 L144.5,117.1 L144.7,114.2 L144.9,111.3 L145.1,108.4 L145.3,105.5 L145.5,102.5 L145.7,99.4 L145.9,96.4 L146.1,93.3 L146.3,90.1 L146.5,86.9 L146.7,83.7 L146.9,80.4 L147.1,77.1 L147.2,73.8 L147.4,70.4 L147.6,67.0 L147.8,63.6 L148.0,60.1 L148.2,56.6 L148.4,53.1 L148.6,49.6 L148.8,46.1 L149.0,42.6 L149.2,39.0 L149.4,35.4 L149.6,36.1 L149.8,39.7 L150.0,43.2 L150.1,46.8 L150.3,50.3 L150.5,53.8 L150.7,57.3 L150.9,60.8 L151.1,64.2 L151.3,67.6 L151.5,71.0 L151.7,74.4 L151.9,77.7 L152.1,81.0 L152.3,84.3 L152.5,87.5 L152.7,90.7 L152.9,93.8 L153.0,97.0 L153.2,100.0 L153.4,103.1 L153.6,106.0 L153.8,109.0 L154.0,111.9 L154.2,114.8 L154.4,117.6 L154.6,120.4 L154.8,123.1 L155.0,125.8 L155.2,128.5 L155.4,131.2 L155.6,133.8 L155.8,136.3 L155.9,138.9 L156.1,141.4 L156.3,143.9 L156.5,146.3 L156.7,148.7 L156.9,151.1 L157.1,153.5 L157.3,155.8 L157.5,158.1" fill="none" stroke="#c1440e" stroke-width="1.2"/>
    <path d="M184.4,157.9 L184.5,155.6 L184.7,153.3 L184.9,150.9 L185.1,148.6 L185.3,146.1 L185.5,143.7 L185.7,141.2 L185.9,138.7 L186.1,136.2 L186.3,133.6 L186.5,131.0 L186.7,128.3 L186.9,125.7 L187.1,122.9 L187.3,120.2 L187.4,117.4 L187.6,114.6 L187.8,111.7 L188.0,108.8 L188.2,105.8 L188.4,102.8 L188.6,99.8 L188.8,96.7 L189.0,93.6 L189.2,90.5 L189.4,87.3 L189.6,84.1 L189.8,80.8 L190.0,77.5 L190.2,74.2 L190.3,70.8 L190.5,67.4 L190.7,64.0 L190.9,60.5 L191.1,57.1 L191.3,53.6 L191.5,50.0 L191.7,46.5 L191.9,43.0 L192.1,39.4 L192.3,35.9 L192.5,35.7 L192.7,39.2 L192.9,42.8 L193.0,46.3 L193.2,49.9 L193.4,53.4 L193.6,56.9 L193.8,60.4 L194.0,63.8 L194.2,67.2 L194.4,70.6 L194.6,74.0 L194.8,77.3 L195.0,80.6 L195.2,83.9 L195.4,87.1 L195.6,90.3 L195.8,93.5 L195.9,96.6 L196.1,99.7 L196.3,102.7 L196.5,105.7 L196.7,108.6 L196.9,111.5 L197.1,114.4 L197.3,117.3 L197.5,120.0 L197.7,122.8 L197.9,125.5 L198.1,128.2 L198.3,130.9 L198.5,133.5 L198.7,136.0 L198.8,138.6 L199.0,141.1 L199.2,143.6 L199.4,146.0 L199.6,148.4 L199.8,150.8 L200.0,153.2 L200.2,155.5 L200.4,157.8" fill="none" stroke="#c1440e" stroke-width="1.2"/>
    <path d="M227.3,158.2 L227.4,155.9 L227.6,153.6 L227.8,151.2 L228.0,148.9 L228.2,146.4 L228.4,144.0 L228.6,141.5 L228.8,139.0 L229.0,136.5 L229.2,133.9 L229.4,131.3 L229.6,128.7 L229.8,126.0 L230.0,123.3 L230.2,120.5 L230.3,117.7 L230.5,114.9 L230.7,112.0 L230.9,109.1 L231.1,106.2 L231.3,103.2 L231.5,100.2 L231.7,97.1 L231.9,94.0 L232.1,90.9 L232.3,87.7 L232.5,84.5 L232.7,81.2 L232.9,77.9 L233.1,74.6 L233.2,71.2 L233.4,67.8 L233.6,64.4 L233.8,61.0 L234.0,57.5 L234.2,54.0 L234.4,50.5 L234.6,46.9 L234.8,43.4 L235.0,39.9 L235.2,36.3 L235.4,35.3 L235.6,38.8 L235.8,42.4 L235.9,45.9 L236.1,49.4 L236.3,53.0 L236.5,56.5 L236.7,59.9 L236.9,63.4 L237.1,66.8 L237.3,70.2 L237.5,73.6 L237.7,76.9 L237.9,80.2 L238.1,83.5 L238.3,86.7 L238.5,89.9 L238.7,93.1 L238.8,96.2 L239.0,99.3 L239.2,102.3 L239.4,105.3 L239.6,108.3 L239.8,111.2 L240.0,114.1 L240.2,116.9 L240.4,119.7 L240.6,122.5 L240.8,125.2 L241.0,127.9 L241.2,130.5 L241.4,133.2 L241.6,135.7 L241.7,138.3 L241.9,140.8 L242.1,143.3 L242.3,145.7 L242.5,148.2 L242.7,150.5 L242.9,152.9 L243.1,155.2 L243.3,157.6 L243.5,159.8" fill="none" stroke="#c1440e" stroke-width="1.2"/>
    <path d="M270.2,158.5 L270.3,156.2 L270.5,153.9 L270.7,151.5 L270.9,149.1 L271.1,146.7 L271.3,144.3 L271.5,141.8 L271.7,139.3 L271.9,136.8 L272.1,134.2 L272.3,131.6 L272.5,129.0 L272.7,126.3 L272.9,123.6 L273.1,120.9 L273.2,118.1 L273.4,115.2 L273.6,112.4 L273.8,109.5 L274.0,106.5 L274.2,103.6 L274.4,100.5 L274.6,97.5 L274.8,94.4 L275.0,91.2 L275.2,88.1 L275.4,84.8 L275.6,81.6 L275.8,78.3 L275.9,75.0 L276.1,71.6 L276.3,68.2 L276.5,64.8 L276.7,61.4 L276.9,57.9 L277.1,54.4 L277.3,50.9 L277.5,47.4 L277.7,43.8 L277.9,40.3 L278.1,36.7 L278.3,34.8 L278.5,38.4 L278.7,41.9 L278.8,45.5 L279.0,49.0 L279.2,52.5 L279.4,56.0 L279.6,59.5 L279.8,63.0 L280.0,66.4 L280.2,69.8 L280.4,73.2 L280.6,76.5 L280.8,79.9 L281.0,83.1 L281.2,86.4 L281.4,89.6 L281.6,92.7 L281.7,95.8 L281.9,98.9 L282.1,102.0 L282.3,105.0 L282.5,107.9 L282.7,110.9 L282.9,113.7 L283.1,116.6 L283.3,119.4 L283.5,122.1 L283.7,124.9 L283.9,127.6 L284.1,130.2 L284.3,132.8 L284.5,135.4 L284.6,138.0 L284.8,140.5 L285.0,143.0 L285.2,145.4 L285.4,147.9 L285.6,150.3 L285.8,152.6 L286.0,155.0 L286.2,157.3 L286.4,159.6" fill="none" stroke="#c1440e" stroke-width="1.2"/>
    <path d="M313.1,158.8 L313.2,156.5 L313.4,154.2 L313.6,151.8 L313.8,149.4 L314.0,147.0 L314.2,144.6 L314.4,142.1 L314.6,139.6 L314.8,137.1 L315.0,134.5 L315.2,131.9 L315.4,129.3 L315.6,126.6 L315.8,123.9 L316.0,121.2 L316.1,118.4 L316.3,115.6 L316.5,112.7 L316.7,109.8 L316.9,106.9 L317.1,103.9 L317.3,100.9 L317.5,97.9 L317.7,94.8 L317.9,91.6 L318.1,88.4 L318.3,85.2 L318.5,82.0 L318.7,78.7 L318.9,75.4 L319.0,72.0 L319.2,68.6 L319.4,65.2 L319.6,61.8 L319.8,58.3 L320.0,54.8 L320.2,51.3 L320.4,47.8 L320.6,44.3 L320.8,40.7 L321.0,37.1 L321.2,34.4 L321.4,38.0 L321.6,41.5 L321.7,45.1 L321.9,48.6 L322.1,52.1 L322.3,55.6 L322.5,59.1 L322.7,62.6 L322.9,66.0 L323.1,69.4 L323.3,72.8 L323.5,76.1 L323.7,79.5 L323.9,82.7 L324.1,86.0 L324.3,89.2 L324.5,92.3 L324.6,95.5 L324.8,98.6 L325.0,101.6 L325.2,104.6 L325.4,107.6 L325.6,110.5 L325.8,113.4 L326.0,116.2" fill="none" stroke="#c1440e" stroke-width="1.2"/>
    <path d="M65.9,159.9 L66.1,159.7 L66.3,159.5 L66.5,159.3 L66.7,159.1 L66.9,159.0 L67.1,158.8 L67.2,158.6 L67.4,158.4 L67.6,158.2 L67.8,158.0 L68.0,157.8 L68.2,157.6 L68.4,157.4 L68.6,157.2 L68.8,157.0 L69.0,156.8 L69.2,156.6 L69.4,156.4 L69.6,156.3 L69.8,156.1 L70.0,155.9 L70.1,155.7 L70.3,155.5 L70.5,155.3 L70.7,155.1 L70.9,154.9 L71.1,154.7 L71.3,154.5 L71.5,154.3 L71.7,154.1 L71.9,153.9 L72.1,153.7 L72.3,153.5 L72.5,153.3 L72.7,153.1 L72.9,153.0 L73.0,152.8 L73.2,152.6 L73.4,152.4 L73.6,152.2 L73.8,152.0 L74.0,151.8 L74.2,151.6 L74.4,151.4 L74.6,151.2 L74.8,151.0 L75.0,150.8 L75.2,150.6 L75.4,150.4 L75.6,150.2 L75.8,150.0 L75.9,149.8 L76.1,149.6 L76.3,149.4 L76.5,149.2 L76.7,149.0 L76.9,148.9 L77.1,148.7 L77.3,148.5 L77.5,148.3 L77.7,148.1 L77.9,147.9 L78.1,147.7 L78.3,147.5 L78.5,147.3 L78.6,147.1 L78.8,146.9 L79.0,146.7 L79.2,146.5 L79.4,146.3 L79.6,146.1 L79.8,145.9 L80.0,145.7 L80.2,145.5 L80.4,145.3 L80.6,145.1 L80.8,144.9 L81.0,144.7 L81.2,144.5 L81.4,144.3 L81.5,144.1 L81.7,143.9 L81.9,143.7 L82.1,143.5 L82.3,143.3 L82.5,143.1 L82.7,142.9 L82.9,142.7 L83.1,142.5 L83.3,142.3 L83.5,142.1 L83.7,141.9 L83.9,141.7 L84.1,141.5 L84.3,141.4 L84.4,141.2 L84.6,141.0 L84.8,140.8 L85.0,140.6 L85.2,140.4 L85.4,140.2 L85.6,140.0 L85.8,139.8 L86.0,139.6 L86.2,139.4 L86.4,139.2 L86.6,139.0 L86.8,138.8 L87.0,138.6 L87.2,138.4 L87.3,138.2 L87.5,138.0 L87.7,137.8 L87.9,137.6 L88.1,137.4 L88.3,137.2 L88.5,137.0 L88.7,136.8 L88.9,136.6 L89.1,136.4 L89.3,136.2 L89.5,136.0 L89.7,135.8 L89.9,135.6 L90.0,135.4 L90.2,135.2 L90.4,135.0 L90.6,134.8 L90.8,134.5 L91.0,134.3 L91.2,134.1 L91.4,133.9 L91.6,133.7 L91.8,133.5 L92.0,133.3 L92.2,133.1 L92.4,132.9 L92.6,132.7 L92.8,132.5 L92.9,132.3 L93.1,132.1 L93.3,131.9 L93.5,131.7 L93.7,131.5 L93.9,131.3 L94.1,131.1 L94.3,130.9 L94.5,130.7 L94.7,130.5 L94.9,130.3 L95.1,130.1 L95.3,129.9 L95.5,129.7 L95.7,129.5 L95.8,129.3 L96.0,129.1 L96.2,128.9 L96.4,128.7 L96.6,128.5 L96.8,128.3 L97.0,128.1 L97.2,127.9 L97.4,127.7 L97.6,127.5 L97.8,127.3 L98.0,127.1 L98.2,126.8 L98.4,126.6 L98.6,126.4 L98.7,126.2 L98.9,126.0 L99.1,125.8 L99.3,125.6 L99.5,125.4 L99.7,125.2 L99.9,125.0 L100.1,124.8 L100.3,124.6 L100.5,124.4 L100.7,124.2 L100.9,124.0 L101.1,123.8 L101.3,123.6 L101.5,123.4 L101.6,123.2 L101.8,123.0 L102.0,122.8 L102.2,122.5 L102.4,122.3 L102.6,122.1 L102.8,121.9 L103.0,121.7 L103.2,121.5 L103.4,121.3 L103.6,121.1 L103.8,120.9 L104.0,120.7 L104.2,120.5 L104.3,120.3 L104.5,120.1 L104.7,119.9 L104.9,119.7 L105.1,119.5 L105.3,119.2 L105.5,119.0 L105.7,118.8 L105.9,118.6 L106.1,118.4 L106.3,118.2 L106.5,118.0 L106.7,117.8 L106.9,117.6 L107.1,117.4 L107.2,117.2 L107.4,117.0 L107.6,116.8 L107.8,116.6 L108.0,116.3 L108.2,116.1 L108.4,115.9 L108.6,115.7 L108.8,115.5 L109.0,115.3 L109.2,115.1 L109.4,114.9 L109.6,114.7 L109.8,114.5 L110.0,114.3 L110.1,114.1 L110.3,113.8 L110.5,113.6 L110.7,113.4 L110.9,113.2 L111.1,113.0 L111.3,112.8 L111.5,112.6 L111.7,112.4 L111.9,112.2 L112.1,112.0 L112.3,111.8 L112.5,111.5 L112.7,111.3 L112.9,111.1 L113.0,110.9 L113.2,110.7 L113.4,110.5 L113.6,110.3 L113.8,110.1 L114.0,109.9 L114.2,109.7 L114.4,109.5 L114.6,109.2 L114.8,109.0 L115.0,108.8 L115.2,108.6 L115.4,108.4 L115.6,108.2 L115.8,108.0 L115.9,107.8 L116.1,107.6 L116.3,107.3 L116.5,107.1 L116.7,106.9 L116.9,106.7 L117.1,106.5 L117.3,106.3 L117.5,106.1 L117.7,105.9 L117.9,105.7 L118.1,105.4 L118.3,105.2 L118.5,105.0 L118.7,104.8 L118.8,104.6 L119.0,104.4 L119.2,104.2 L119.4,104.0 L119.6,103.8 L119.8,103.5 L120.0,103.3 L120.2,103.1 L120.4,102.9 L120.6,102.7 L120.8,102.5 L121.0,102.3 L121.2,102.1 L121.4,101.8 L121.5,101.6 L121.7,101.4 L121.9,101.2 L122.1,101.0 L122.3,100.8 L122.5,100.6 L122.7,100.4 L122.9,100.1 L123.1,99.9 L123.3,99.7 L123.5,99.5 L123.7,99.3 L123.9,99.1 L124.1,98.9 L124.3,98.6 L124.4,98.4 L124.6,98.2 L124.8,98.0 L125.0,97.8 L125.2,97.6 L125.4,97.4 L125.6,97.1 L125.8,96.9 L126.0,96.7 L126.2,96.5 L126.4,96.3 L126.6,96.1 L126.8,95.9 L127.0,95.6 L127.2,95.4 L127.3,95.2 L127.5,95.0 L127.7,94.8 L127.9,94.6 L128.1,94.4 L128.3,94.1 L128.5,93.9 L128.7,93.7 L128.9,93.5 L129.1,93.3 L129.3,93.1 L129.5,92.9 L129.7,92.6 L129.9,92.4 L130.1,92.2 L130.2,92.0 L130.4,91.8 L130.6,91.6 L130.8,91.3 L131.0,91.1 L131.2,90.9 L131.4,90.7 L131.6,90.5 L131.8,90.3 L132.0,90.0 L132.2,89.8 L132.4,89.6 L132.6,89.4 L132.8,89.2 L132.9,89.0 L133.1,88.7 L133.3,88.5 L133.5,88.3 L133.7,88.1 L133.9,87.9 L134.1,87.7 L134.3,87.4 L134.5,87.2 L134.7,87.0 L134.9,86.8 L135.1,86.6 L135.3,86.4 L135.5,86.1 L135.7,85.9 L135.8,85.7 L136.0,85.5 L136.2,85.3 L136.4,85.1 L136.6,84.8 L136.8,84.6 L137.0,84.4 L137.2,84.2 L137.4,84.0 L137.6,83.8 L137.8,83.5 L138.0,83.3 L138.2,83.1 L138.4,82.9 L138.6,82.7 L138.7,82.4 L138.9,82.2 L139.1,82.0 L139.3,81.8 L139.5,81.6 L139.7,81.4 L139.9,81.1 L140.1,80.9 L140.3,80.7 L140.5,80.5 L140.7,80.3 L140.9,80.0 L141.1,79.8 L141.3,79.6 L141.5,79.4 L141.6,79.2 L141.8,78.9 L142.0,78.7 L142.2,78.5 L142.4,78.3 L142.6,78.1 L142.8,77.9 L143.0,77.6 L143.2,77.4 L143.4,77.2 L143.6,77.0 L143.8,76.8 L144.0,76.5 L144.2,76.3 L144.4,76.1 L144.5,75.9 L144.7,75.7 L144.9,75.4 L145.1,75.2 L145.3,75.0 L145.5,74.8 L145.7,74.6 L145.9,74.3 L146.1,74.1 L146.3,73.9 L146.5,73.7 L146.7,73.5 L146.9,73.2 L147.1,73.0 L147.2,72.8 L147.4,72.6 L147.6,72.4 L147.8,72.1 L148.0,71.9 L148.2,71.7 L148.4,71.5 L148.6,71.3 L148.8,71.0 L149.0,70.8 L149.2,70.6 L149.4,70.4 L149.6,70.1 L149.8,69.9 L150.0,69.7 L150.1,69.5 L150.3,69.3 L150.5,69.0 L150.7,68.8 L150.9,68.6 L151.1,68.4 L151.3,68.2 L151.5,67.9 L151.7,67.7 L151.9,67.5 L152.1,67.3 L152.3,67.1 L152.5,66.8 L152.7,66.6 L152.9,66.4 L153.0,66.2 L153.2,65.9 L153.4,65.7 L153.6,65.5 L153.8,65.3 L154.0,65.1 L154.2,64.8 L154.4,64.6 L154.6,64.4 L154.8,64.2 L155.0,63.9 L155.2,63.7 L155.4,63.5 L155.6,63.3 L155.8,63.1 L155.9,62.8 L156.1,62.6 L156.3,62.4 L156.5,62.2 L156.7,61.9 L156.9,61.7 L157.1,61.5 L157.3,61.3 L157.5,61.1 L157.7,60.8 L157.9,60.6 L158.1,60.4 L158.3,60.2 L158.5,59.9 L158.7,59.7 L158.8,59.5 L159.0,59.3 L159.2,59.1 L159.4,58.8 L159.6,58.6 L159.8,58.4 L160.0,58.2 L160.2,57.9 L160.4,57.7 L160.6,57.5 L160.8,57.3 L161.0,57.0 L161.2,56.8 L161.4,56.6 L161.6,56.4 L161.7,56.2 L161.9,55.9 L162.1,55.7 L162.3,55.5 L162.5,55.3 L162.7,55.0 L162.9,54.8 L163.1,54.6 L163.3,54.4 L163.5,54.1 L163.7,53.9 L163.9,53.7 L164.1,53.5 L164.3,53.2 L164.4,53.0 L164.6,52.8 L164.8,52.6 L165.0,52.4 L165.2,52.1 L165.4,51.9 L165.6,51.7 L165.8,51.5 L166.0,51.2 L166.2,51.0 L166.4,50.8 L166.6,50.6 L166.8,50.3 L167.0,50.1 L167.2,49.9 L167.3,49.7 L167.5,49.4 L167.7,49.2 L167.9,49.0 L168.1,48.8 L168.3,48.5 L168.5,48.3 L168.7,48.1 L168.9,47.9 L169.1,47.7 L169.3,47.4 L169.5,47.2 L169.7,47.0 L169.9,46.8 L170.1,46.5 L170.2,46.3 L170.4,46.1 L170.6,45.9 L170.8,45.6 L171.0,45.4 L171.2,45.2 L171.4,45.0 L171.6,44.7 L171.8,44.5 L172.0,44.3 L172.2,44.1 L172.4,43.8 L172.6,43.6 L172.8,43.4 L173.0,43.2 L173.1,42.9 L173.3,42.7 L173.5,42.5 L173.7,42.3 L173.9,42.0 L174.1,41.8 L174.3,41.6 L174.5,41.4 L174.7,41.1 L174.9,40.9 L175.1,40.7 L175.3,40.5 L175.5,40.3 L175.7,40.0 L175.8,39.8 L176.0,39.6 L176.2,39.4 L176.4,39.1 L176.6,38.9 L176.8,38.7 L177.0,38.5 L177.2,38.2 L177.4,38.0 L177.6,37.8 L177.8,37.6 L178.0,37.3 L178.2,37.1 L178.4,36.9 L178.6,36.7 L178.7,36.4 L178.9,36.2 L179.1,36.0 L179.3,35.8 L179.5,35.5 L179.7,35.3 L179.9,35.1 L180.1,34.9 L180.3,34.6 L180.5,34.4 L180.7,34.2 L180.9,34.0 L181.1,34.3 L181.3,34.5 L181.5,34.7 L181.6,34.9 L181.8,35.2 L182.0,35.4 L182.2,35.6 L182.4,35.8 L182.6,36.1 L182.8,36.3 L183.0,36.5 L183.2,36.7 L183.4,37.0 L183.6,37.2 L183.8,37.4 L184.0,37.6 L184.2,37.9 L184.4,38.1 L184.5,38.3 L184.7,38.5 L184.9,38.8 L185.1,39.0 L185.3,39.2 L185.5,39.4 L185.7,39.7 L185.9,39.9 L186.1,40.1 L186.3,40.3 L186.5,40.5 L186.7,40.8 L186.9,41.0 L187.1,41.2 L187.3,41.4 L187.4,41.7 L187.6,41.9 L187.8,42.1 L188.0,42.3 L188.2,42.6 L188.4,42.8 L188.6,43.0 L188.8,43.2 L189.0,43.5 L189.2,43.7 L189.4,43.9 L189.6,44.1 L189.8,44.4 L190.0,44.6 L190.2,44.8 L190.3,45.0 L190.5,45.3 L190.7,45.5 L190.9,45.7 L191.1,45.9 L191.3,46.2 L191.5,46.4 L191.7,46.6 L191.9,46.8 L192.1,47.1 L192.3,47.3 L192.5,47.5 L192.7,47.7 L192.9,48.0 L193.0,48.2 L193.2,48.4 L193.4,48.6 L193.6,48.8 L193.8,49.1 L194.0,49.3 L194.2,49.5 L194.4,49.7 L194.6,50.0 L194.8,50.2 L195.0,50.4 L195.2,50.6 L195.4,50.9 L195.6,51.1 L195.8,51.3 L195.9,51.5 L196.1,51.8 L196.3,52.0 L196.5,52.2 L196.7,52.4 L196.9,52.7 L197.1,52.9 L197.3,53.1 L197.5,53.3 L197.7,53.5 L197.9,53.8 L198.1,54.0 L198.3,54.2 L198.5,54.4 L198.7,54.7 L198.8,54.9 L199.0,55.1 L199.2,55.3 L199.4,55.6 L199.6,55.8 L199.8,56.0 L200.0,56.2 L200.2,56.4 L200.4,56.7 L200.6,56.9 L200.8,57.1 L201.0,57.3 L201.2,57.6 L201.4,57.8 L201.6,58.0 L201.7,58.2 L201.9,58.5 L202.1,58.7 L202.3,58.9 L202.5,59.1 L202.7,59.3 L202.9,59.6 L203.1,59.8 L203.3,60.0 L203.5,60.2 L203.7,60.5 L203.9,60.7 L204.1,60.9 L204.3,61.1 L204.4,61.4 L204.6,61.6 L204.8,61.8 L205.0,62.0 L205.2,62.2 L205.4,62.5 L205.6,62.7 L205.8,62.9 L206.0,63.1 L206.2,63.4 L206.4,63.6 L206.6,63.8 L206.8,64.0 L207.0,64.2 L207.2,64.5 L207.3,64.7 L207.5,64.9 L207.7,65.1 L207.9,65.3 L208.1,65.6 L208.3,65.8 L208.5,66.0 L208.7,66.2 L208.9,66.5 L209.1,66.7 L209.3,66.9 L209.5,67.1 L209.7,67.3 L209.9,67.6 L210.1,67.8 L210.2,68.0 L210.4,68.2 L210.6,68.5 L210.8,68.7 L211.0,68.9 L211.2,69.1 L211.4,69.3 L211.6,69.6 L211.8,69.8 L212.0,70.0 L212.2,70.2 L212.4,70.4 L212.6,70.7 L212.8,70.9 L213.0,71.1 L213.1,71.3 L213.3,71.5 L213.5,71.8 L213.7,72.0 L213.9,72.2 L214.1,72.4 L214.3,72.6 L214.5,72.9 L214.7,73.1 L214.9,73.3 L215.1,73.5 L215.3,73.7 L215.5,74.0 L215.7,74.2 L215.9,74.4 L216.0,74.6 L216.2,74.8 L216.4,75.1 L216.6,75.3 L216.8,75.5 L217.0,75.7 L217.2,75.9 L217.4,76.2 L217.6,76.4 L217.8,76.6 L218.0,76.8 L218.2,77.0 L218.4,77.3 L218.6,77.5 L218.8,77.7 L218.9,77.9 L219.1,78.1 L219.3,78.4 L219.5,78.6 L219.7,78.8 L219.9,79.0 L220.1,79.2 L220.3,79.5 L220.5,79.7 L220.7,79.9 L220.9,80.1 L221.1,80.3 L221.3,80.6 L221.5,80.8 L221.6,81.0 L221.8,81.2 L222.0,81.4 L222.2,81.6 L222.4,81.9 L222.6,82.1 L222.8,82.3 L223.0,82.5 L223.2,82.7 L223.4,83.0 L223.6,83.2 L223.8,83.4 L224.0,83.6 L224.2,83.8 L224.4,84.0 L224.5,84.3 L224.7,84.5 L224.9,84.7 L225.1,84.9 L225.3,85.1 L225.5,85.3 L225.7,85.6 L225.9,85.8 L226.1,86.0 L226.3,86.2 L226.5,86.4 L226.7,86.7 L226.9,86.9 L227.1,87.1 L227.3,87.3 L227.4,87.5 L227.6,87.7 L227.8,88.0 L228.0,88.2 L228.2,88.4 L228.4,88.6 L228.6,88.8 L228.8,89.0 L229.0,89.3 L229.2,89.5 L229.4,89.7 L229.6,89.9 L229.8,90.1 L230.0,90.3 L230.2,90.5 L230.3,90.8 L230.5,91.0 L230.7,91.2 L230.9,91.4 L231.1,91.6 L231.3,91.8 L231.5,92.1 L231.7,92.3 L231.9,92.5 L232.1,92.7 L232.3,92.9 L232.5,93.1 L232.7,93.4 L232.9,93.6 L233.1,93.8 L233.2,94.0 L233.4,94.2 L233.6,94.4 L233.8,94.6 L234.0,94.9 L234.2,95.1 L234.4,95.3 L234.6,95.5 L234.8,95.7 L235.0,95.9 L235.2,96.1 L235.4,96.4 L235.6,96.6 L235.8,96.8 L235.9,97.0 L236.1,97.2 L236.3,97.4 L236.5,97.6 L236.7,97.9 L236.9,98.1 L237.1,98.3 L237.3,98.5 L237.5,98.7 L237.7,98.9 L237.9,99.1 L238.1,99.4 L238.3,99.6 L238.5,99.8 L238.7,100.0 L238.8,100.2 L239.0,100.4 L239.2,100.6 L239.4,100.8 L239.6,101.1 L239.8,101.3 L240.0,101.5 L240.2,101.7 L240.4,101.9 L240.6,102.1 L240.8,102.3 L241.0,102.5 L241.2,102.8 L241.4,103.0 L241.6,103.2 L241.7,103.4 L241.9,103.6 L242.1,103.8 L242.3,104.0 L242.5,104.2 L242.7,104.5 L242.9,104.7 L243.1,104.9 L243.3,105.1 L243.5,105.3 L243.7,105.5 L243.9,105.7 L244.1,105.9 L244.3,106.1 L244.5,106.4 L244.6,106.6 L244.8,106.8 L245.0,107.0 L245.2,107.2 L245.4,107.4 L245.6,107.6 L245.8,107.8 L246.0,108.0 L246.2,108.3 L246.4,108.5 L246.6,108.7 L246.8,108.9 L247.0,109.1 L247.2,109.3 L247.3,109.5 L247.5,109.7 L247.7,109.9 L247.9,110.1 L248.1,110.4 L248.3,110.6 L248.5,110.8 L248.7,111.0 L248.9,111.2 L249.1,111.4 L249.3,111.6 L249.5,111.8 L249.7,112.0 L249.9,112.2 L250.1,112.5 L250.2,112.7 L250.4,112.9 L250.6,113.1 L250.8,113.3 L251.0,113.5 L251.2,113.7 L251.4,113.9 L251.6,114.1 L251.8,114.3 L252.0,114.5 L252.2,114.7 L252.4,115.0 L252.6,115.2 L252.8,115.4 L253.0,115.6 L253.1,115.8 L253.3,116.0 L253.5,116.2 L253.7,116.4 L253.9,116.6 L254.1,116.8 L254.3,117.0 L254.5,117.2 L254.7,117.5 L254.9,117.7 L255.1,117.9 L255.3,118.1 L255.5,118.3 L255.7,118.5 L255.9,118.7 L256.0,118.9 L256.2,119.1 L256.4,119.3 L256.6,119.5 L256.8,119.7 L257.0,119.9 L257.2,120.1 L257.4,120.3 L257.6,120.6 L257.8,120.8 L258.0,121.0 L258.2,121.2 L258.4,121.4 L258.6,121.6 L258.8,121.8 L258.9,122.0 L259.1,122.2 L259.3,122.4 L259.5,122.6 L259.7,122.8 L259.9,123.0 L260.1,123.2 L260.3,123.4 L260.5,123.6 L260.7,123.8 L260.9,124.1 L261.1,124.3 L261.3,124.5 L261.5,124.7 L261.6,124.9 L261.8,125.1 L262.0,125.3 L262.2,125.5 L262.4,125.7 L262.6,125.9 L262.8,126.1 L263.0,126.3 L263.2,126.5 L263.4,126.7 L263.6,126.9 L263.8,127.1 L264.0,127.3 L264.2,127.5 L264.4,127.7 L264.5,127.9 L264.7,128.1 L264.9,128.3 L265.1,128.5 L265.3,128.7 L265.5,129.0 L265.7,129.2 L265.9,129.4 L266.1,129.6 L266.3,129.8 L266.5,130.0 L266.7,130.2 L266.9,130.4 L267.1,130.6 L267.3,130.8 L267.4,131.0 L267.6,131.2 L267.8,131.4 L268.0,131.6 L268.2,131.8 L268.4,132.0 L268.6,132.2 L268.8,132.4 L269.0,132.6 L269.2,132.8 L269.4,133.0 L269.6,133.2 L269.8,133.4 L270.0,133.6 L270.2,133.8 L270.3,134.0 L270.5,134.2 L270.7,134.4 L270.9,134.6 L271.1,134.8 L271.3,135.0 L271.5,135.2 L271.7,135.4 L271.9,135.6 L272.1,135.8 L272.3,136.0 L272.5,136.2 L272.7,136.4 L272.9,136.6 L273.1,136.8 L273.2,137.0 L273.4,137.2 L273.6,137.4 L273.8,137.6 L274.0,137.8 L274.2,138.0 L274.4,138.2 L274.6,138.4 L274.8,138.6 L275.0,138.8 L275.2,139.0 L275.4,139.2 L275.6,139.4 L275.8,139.6 L275.9,139.8 L276.1,140.0 L276.3,140.2 L276.5,140.4 L276.7,140.6 L276.9,140.8 L277.1,141.0 L277.3,141.2 L277.5,141.4 L277.7,141.6 L277.9,141.8 L278.1,142.0 L278.3,142.2 L278.5,142.4 L278.7,142.6 L278.8,142.8 L279.0,143.0 L279.2,143.2 L279.4,143.4 L279.6,143.6 L279.8,143.8 L280.0,144.0 L280.2,144.2 L280.4,144.4 L280.6,144.6 L280.8,144.8 L281.0,145.0 L281.2,145.2 L281.4,145.4 L281.6,145.6 L281.7,145.8 L281.9,146.0 L282.1,146.2 L282.3,146.4 L282.5,146.6 L282.7,146.8 L282.9,147.0 L283.1,147.1 L283.3,147.3 L283.5,147.5 L283.7,147.7 L283.9,147.9 L284.1,148.1 L284.3,148.3 L284.5,148.5 L284.6,148.7 L284.8,148.9 L285.0,149.1 L285.2,149.3 L285.4,149.5 L285.6,149.7 L285.8,149.9 L286.0,150.1 L286.2,150.3 L286.4,150.5 L286.6,150.7 L286.8,150.9 L287.0,151.1 L287.2,151.3 L287.4,151.5 L287.5,151.7 L287.7,151.8 L287.9,152.0 L288.1,152.2 L288.3,152.4 L288.5,152.6 L288.7,152.8 L288.9,153.0 L289.1,153.2 L289.3,153.4 L289.5,153.6 L289.7,153.8 L289.9,154.0 L290.1,154.2 L290.2,154.4 L290.4,154.6 L290.6,154.8 L290.8,155.0 L291.0,155.2 L291.2,155.3 L291.4,155.5 L291.6,155.7 L291.8,155.9 L292.0,156.1 L292.2,156.3 L292.4,156.5 L292.6,156.7 L292.8,156.9 L293.0,157.1 L293.1,157.3 L293.3,157.5 L293.5,157.7 L293.7,157.9 L293.9,158.1 L294.1,158.2 L294.3,158.4 L294.5,158.6 L294.7,158.8 L294.9,159.0 L295.1,159.2 L295.3,159.4 L295.5,159.6 L295.7,159.8 L295.9,160.0" fill="none" stroke="#5aa0d8" stroke-width="1.4"/>
    <line x1="8" y1="183" x2="22" y2="183" stroke="#c1440e" stroke-width="1.2"/>
    <text x="26" y="186">Phobos: rises in the west, up about 4¼ hours, rises again every 11 hours</text>
    <line x1="8" y1="197" x2="22" y2="197" stroke="#5aa0d8" stroke-width="1.4"/>
    <text x="26" y="200">Deimos: rises in the east, up about 2½ days, then gone for nearly 3 days</text>
    <text x="6" y="212">Worked out for moons in circular orbits over the equator, seen from the equator.</text>
    <text x="6" y="226">Phobos goes round faster than Mars turns, so it overtakes the ground and crosses the sky backwards,</text>
    <text x="6" y="235">west to east. Deimos goes round only a little slower than Mars turns, so it drifts across very</text>
    <text x="6" y="244">slowly, east to west. From beyond about 70° north or south, Phobos never rises at all.</text>
  </g>
</svg>
</div>

*Figure B. Phobos's short, fast trips across the sky against Deimos's slow one.*

Phobos overhead is about 0.2° across, about two-fifths the width of the full Moon seen from the Earth, and the Sun
from Mars is 0.35°. So Phobos can never cover the whole Sun. Instead it **transits** across it, a black blob crossing
the Sun in well under a minute. The rover Opportunity photographed several of these transits. Deimos is so small
and far that it would look like a bright star.

??? note "Sources"
    - Hall as an American astronomer, finding Deimos on 12 August 1877 and Phobos on 18 August at the US Naval
      Observatory in Washington: Wikipedia, [Moons of Mars](https://en.wikipedia.org/wiki/Moons_of_Mars) (weaker).
    - Phobos's size, 25.90 × 22.60 × 18.32 km; rising in the west, crossing the sky in 4 h 15 min or less and setting
      in the east, about twice each Martian day, every 11 h 6 min; never above the horizon beyond 70.4°; too small to
      cause a total eclipse; transits photographed by Opportunity: Wikipedia,
      [Phobos (moon)](https://en.wikipedia.org/wiki/Phobos_(moon)) (weaker).
    - Deimos rising in the east and setting in the west, its mean radius 6.2 km and its 30.3-hour orbit: Wikipedia,
      [Deimos (moon)](https://en.wikipedia.org/wiki/Deimos_(moon)) (weaker).
    - Phobos's and Deimos's orbits and Mars's day: chapter 8, section 8.7. Phobos about 6,000 km up:
      our arithmetic, $9{,}376 - 3{,}396$.
    - How long Deimos stays up, the sizes of Phobos and the Sun in the Martian sky, and "well under a minute": our
      arithmetic, section 19.8. Deimos looking like a bright star: our reasoning from its size of about 0.04°.

## 19.2 Where the moons came from { #origin }

Nobody is sure where Phobos and Deimos came from. There are two main ideas.

- **Captured asteroids.** Both are small and dark, rather like some asteroids, so perhaps Mars caught two of them.
- **Made at Mars.** A giant impact on Mars may have thrown out a ring of rubble that gathered into moons. The same
  impact may explain why Mars's northern half is so much lower and smoother than its southern half.

The orbits are a clue. Both moons go round in **nearly circular orbits, almost exactly over Mars's equator**. A
captured body would arrive on a long, tilted ellipse. Mars's thin air and its tides would then have to round off the
orbit and swing it into the equator, and it is not clear there has been time for that to happen to Deimos.

Japan's **Martian Moons eXploration** (MMX) was launched on 19 October 2026 and is due to reach Mars orbit in August
2027. It will study both moons, land on Phobos to collect a sample and bring it back to the Earth in 2031. Rock from
an asteroid and rock from Mars should look quite different in a laboratory.

The biggest crater on Phobos, **Stickney**, is 9 km across, a large share of the whole moon. The impact that made it
nearly broke Phobos apart.

??? note "Sources"
    - The two hypotheses, the moons' likeness to asteroids, the giant impact perhaps linked to the Martian dichotomy
      and the Borealis Basin, and the circular, equatorial orbits needing drag and tides to explain if the moons were
      captured, with doubt about the time available for Deimos: Wikipedia, Moons of Mars (above).
    - MMX launched on 19 October 2026, due in Mars orbit in August 2027, with samples back in 2031: chapter 15,
      sections 15.3 and 15.7, and Wikipedia,
      [Martian Moons eXploration](https://en.wikipedia.org/wiki/Martian_Moons_Exploration) (weaker).
    - Stickney, 9 km across, a large share of the surface: Wikipedia, Phobos (moon) (above). "Nearly broke Phobos
      apart": standard, often said of so large a crater on so small a body.
    - Laboratory tests telling Mars rock from asteroid rock: our reasoning.

## 19.3 The working fleet { #fleet }

These orbiters were working in the latest sources we could check, in November 2026.

| Orbiter | From | Arrived | Orbit |
| --- | --- | --- | --- |
| Mars Odyssey | United States | 24 October 2001 | low and polar, about 400 km up |
| Mars Express | Europe | late 2003 | 259 × 11,560 km, nearly polar, 7.5 h (at first) |
| Mars Reconnaissance Orbiter | United States | 10 March 2006 | 250 to 316 km, sun-synchronous |
| Trace Gas Orbiter | Europe and Russia | 19 October 2016 | about 400 km, circular |
| Hope | United Arab Emirates | 9 February 2021 | 20,000 × 43,000 km, 55 h |
| Tianwen-1 orbiter | China | 10 February 2021 | changed several times |

Two others have stopped. India's **Mars Orbiter Mission** ended in 2022. NASA's **MAVEN** lost contact on 6 December
2025, and getting it back was thought very unlikely.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Orbits round Mars drawn to scale, each laid flat in the page to compare sizes, not real directions. Mars is a small disc. Hugging its surface is a ring for the low, nearly circular orbits of Mars Odyssey, the Mars Reconnaissance Orbiter and the Trace Gas Orbiter, a few hundred kilometres up. Phobos circles about 9,400 km from the centre and Deimos about 23,500 km. A dashed circle just inside the orbit of Deimos, at 20,428 km, marks the stationary orbit, where no spacecraft has been placed. Mars Express follows an ellipse from about 300 to over 11,000 km up, and the Emirates' Hope a large ellipse from 20,000 to 43,000 km up, reaching well beyond Deimos.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">Orbits round Mars, to scale, laid flat to compare sizes</text>
    <ellipse cx="217.6" cy="105" rx="83.8" ry="79.1" fill="none" stroke="#eea66f" stroke-width="1.1"/>
    <ellipse cx="176.4" cy="105" rx="22.3" ry="17.7" fill="none" stroke="#5aa0d8" stroke-width="1.0" transform="rotate(-45 190 105)"/>
    <circle cx="190" cy="105" r="56.3" fill="none" stroke="#555" stroke-width="0.8"/>
    <circle cx="190" cy="105" r="49.0" fill="none" stroke="currentColor" stroke-width="0.6" stroke-dasharray="3 2"/>
    <circle cx="190" cy="105" r="22.5" fill="none" stroke="#555" stroke-width="0.8"/>
    <circle cx="190" cy="105" r="9.0" fill="none" stroke="currentColor" stroke-width="0.6"/>
    <circle cx="190" cy="105" r="8.2" fill="#c1440e"/>
    <circle cx="167.5" cy="105.0" r="1.8" fill="#555"/>
    <circle cx="150.2" cy="65.2" r="1.8" fill="#555"/>
    <text x="118" y="40" text-anchor="end" fill="#555">Deimos</text>
    <line x1="121" y1="37" x2="150.2" y2="65.2" stroke="#555" stroke-width="0.5"/>
    <text x="118" y="64" text-anchor="end" fill="currentColor">stationary orbit, none there</text>
    <line x1="121" y1="61" x2="143.9" y2="88.2" stroke="currentColor" stroke-width="0.5"/>
    <text x="118" y="108" text-anchor="end" fill="#555">Phobos</text>
    <line x1="121" y1="105" x2="167.5" y2="105.0" stroke="#555" stroke-width="0.5"/>
    <text x="118" y="150" text-anchor="end" fill="#5aa0d8">Mars Express</text>
    <line x1="121" y1="147" x2="164.6" y2="130.4" stroke="#5aa0d8" stroke-width="0.5"/>
    <text x="118" y="174" text-anchor="end" fill="currentColor">Odyssey, MRO and TGO</text>
    <line x1="121" y1="171" x2="185.5" y2="112.8" stroke="currentColor" stroke-width="0.5"/>
    <text x="304.4" y="108" fill="#eea66f">Hope</text>
    <text x="6" y="204">MRO: Mars Reconnaissance Orbiter. TGO: Trace Gas Orbiter.</text>
    <text x="6" y="226">Low orbiters see the ground close up and pass over landers a few times a day. Long ellipses,</text>
    <text x="6" y="235">like Hope's, see the whole planet at once. Phobos is inside the stationary orbit and Deimos just</text>
    <text x="6" y="244">outside it (chapter 8). The Tianwen-1 orbiter is left out: its present orbit was not in our sources.</text>
  </g>
</svg>
</div>

*Figure A. The fleet and the moons, to scale.*

The orbits fall into two groups. **Low, nearly circular, nearly polar orbits** (Odyssey, MRO, TGO) see the ground
close up and, as Mars turns under them, pass over every part of it. MRO's orbit is sun-synchronous
([chapter 10](10-Wobbling-Orbits-and-the-Finding-of-Neptune.md#mars)), so it always crosses the equator at the same
local time. **Long ellipses** (Mars Express, Hope) swing far out and see a whole face of Mars at once, which is what
you need to watch weather and dust storms. Hope's low point, about 20,000 km up, is close to Deimos's height. On 10
March 2023 it flew close to Deimos and took the first close-up pictures of the whole moon.

Odyssey has been working for over 25 years, the longest any spacecraft has kept going round a planet other than the
Earth.

??? note "Sources"
    - Odyssey reaching Mars orbit on 24 October 2001; a polar orbit with a semi-major axis of about 3,800 km (as of
      2019); the record of over 25 years: Wikipedia,
      [2001 Mars Odyssey](https://en.wikipedia.org/wiki/2001_Mars_Odyssey) (weaker). The height of about 400 km is
      our arithmetic, $3{,}800 - 3{,}396$.
    - Mars Express arriving after course corrections in September and December 2003, its 259 × 11,560 km orbit at
      86° with a period of about 7.5 hours: Wikipedia, [Mars Express](https://en.wikipedia.org/wiki/Mars_Express)
      (weaker).
    - MRO reaching Mars on 10 March 2006: Wikipedia,
      [Mars Reconnaissance Orbiter](https://en.wikipedia.org/wiki/Mars_Reconnaissance_Orbiter) (weaker); its orbit:
      chapter 14, section 14.8, and chapter 10, section 10.7.
    - TGO orbiting since 19 October 2016, circularised at 400 km in 2018: Wikipedia,
      [Trace Gas Orbiter](https://en.wikipedia.org/wiki/Trace_Gas_Orbiter) (weaker).
    - Hope's orbit and arrival: chapter 14, section 14.8. Its Deimos flyby on 10 March 2023 and the first close-up
      global images: Wikipedia, [Emirates Mars Mission](https://en.wikipedia.org/wiki/Emirates_Mars_Mission)
      (weaker). Hope's low point close to Deimos's height, about $23{,}458 - 3{,}396 = 20{,}062$ km: our arithmetic.
    - Tianwen-1 entering orbit on 10 February 2021: Wikipedia,
      [Tianwen-1](https://en.wikipedia.org/wiki/Tianwen-1) (weaker). "Changed several times" is our summary of the
      mission's history; we did not find its present orbit.
    - MOM, in orbit from 24 September 2014, ending on 27 September 2022 after contact was lost: Wikipedia,
      [List of missions to Mars](https://en.wikipedia.org/wiki/List_of_missions_to_Mars) (weaker). MAVEN losing
      contact on 6 December 2025, recovery "very unlikely": Wikipedia, [MAVEN](https://en.wikipedia.org/wiki/MAVEN)
      (weaker).
    - Which orbits suit which jobs: standard, as in chapter 14.

## 19.4 Passing messages { #relay }

A rover on Mars has a small radio and little power. It can talk straight to the Earth, but slowly. It is much quicker
to send its pictures a few hundred kilometres up to an orbiter passing overhead, and let the orbiter's big dish send
them on. This is called a **relay**.

- **Odyssey** carried about 85% of the pictures and other data from the rovers Spirit and Opportunity, and has
  relayed for Curiosity.
- **MRO**, **TGO** and **MAVEN** carry NASA's **Electra** radio, made for relaying, which also measures the Doppler
  shift of the signal, so it helps work out where a lander is.
- **Mars Express** has passed messages for China's Zhurong rover
  ([chapter 6](06-Weighing.md#mars)), and the **Tianwen-1** orbiter relayed for Zhurong after it landed in 2021.

The catch is that a low orbiter is only overhead for a short time. At 300 km up it can see a lander for at most about
**15 minutes** each pass, and only gets a few good passes each day. Rovers plan their work round these passes.

ESA lists what the relay buys a lander: more data, less power, a lighter radio, more chances to talk, a record of
risky moments like landing, and help in finding its way.

??? note "Sources"
    - Odyssey relaying about 85% of Spirit and Opportunity's data, and for Curiosity: Wikipedia, 2001 Mars Odyssey
      (above).
    - Electra on MRO as a UHF relay radio that also collects Doppler data: Wikipedia, Mars Reconnaissance Orbiter
      (above). Electra on TGO and the list of benefits to landers: Wikipedia, Trace Gas Orbiter (above). Electra on
      MAVEN: Wikipedia, MAVEN (above).
    - Mars Express relaying for Zhurong: chapter 6, section 6.7. The Tianwen-1 orbiter serving as a relay for the
      rover: Wikipedia, Tianwen-1 (above).
    - A rover's radio talking straight to the Earth only slowly, and rovers planning round passes: standard.
    - The 15-minute pass: our arithmetic, section 19.8.

## 19.5 A stationary orbit nobody uses { #areostationary }

Round the Earth, a satellite 35,786 km up keeps pace with the turning ground and seems to hang still
([chapter 14](14-Orbits-Around-the-Earth.md#geo)). Mars has the same kind of orbit, the **areostationary orbit**,
about **17,032 km** above its equator. A relay satellite there would always see the same half of Mars and could pass
on far more data than low orbiters that come and go.

Nobody has put a satellite there yet ([chapter 3](03-Keplers-Three-Laws.md#mars)). It would also be harder to keep in
place than an Earth one. The orbit lies between Phobos and Deimos, whose pulls build up through resonances, so it
would need more fuel to stay on station. Mars's lumpy gravity also drags anything there towards one of two stable
longitudes, about 18° W and 168° E.

From that height a satellite sees out to about 80° from the point under it, almost pole to pole. Two or three of them
could keep in touch with almost all of Mars all the time.

??? note "Sources"
    - The areostationary orbit about 17,032 km above the equator; relay satellites there allowing more data to be
      passed on; the extra station-keeping cost from lying between Phobos and Deimos; the two stable longitudes,
      17.92° W and 167.83° E: Wikipedia, [Areostationary orbit](https://en.wikipedia.org/wiki/Areostationary_orbit)
      (weaker).
    - No satellite there yet: chapter 3, section 3.8.
    - Seeing out to 80° and "two or three": our arithmetic and reasoning, section 19.8. That the drift to two stable
      longitudes comes from Mars's uneven gravity: standard, as for the Earth's stationary orbit.

## 19.6 Why you cannot orbit Phobos { #phobosorbit }

To orbit a moon, you must stay where the moon's pull is stronger than Mars's attempt to tear you away. The region
where the moon wins is its **Hill sphere**. For Phobos it reaches only about **17 km** from its centre, and Phobos
itself is 13 km from its centre to the tip of its long axis. Stable orbits only exist well inside the Hill sphere, so
there is no room for one. Deimos's reach is about 21 km against its 6.2 km radius, still very tight.

So spacecraft use a trick, the **quasi-satellite orbit**. The spacecraft orbits **Mars**, not the moon, with the
same period as Phobos but a slightly oval orbit. When it is nearer Mars than Phobos it moves a little faster and
pulls ahead; when farther out it drops behind. Seen from Phobos, it loops round the moon once every 7.65 hours, about
twice as far along the orbit as up and down. Mars's gravity does the work and Phobos's own pull hardly matters.

- In early 1989 the Soviet **Phobos 2** was put into a quasi-satellite orbit round Phobos, about 100 km from it on
  average. It was lost soon afterwards, before it could drop its landers.
- **Mars Express** flew close past Phobos on 5 March 2010 to measure its gravity
  ([chapter 6](06-Weighing.md#mars)).
- **MMX** will use quasi-satellite orbits round Phobos and Deimos, because, as the mission says, they "have
  insufficient mass to support conventional satellite orbits".

??? note "Sources"
    - Phobos 2 in a quasi-satellite orbit round Phobos in early 1989 with a mean radius of about 100 km, and MMX
      aiming for a similar orbit because Phobos is too small for real orbits: Wikipedia,
      [Quasi-satellite](https://en.wikipedia.org/wiki/Quasi-satellite) (weaker). Phobos 2 being lost before
      dropping its landers: standard.
    - MMX's quasi-satellite orbits, quoted: Wikipedia, Martian Moons eXploration (above).
    - The Mars Express flyby: chapter 6, section 6.7.
    - The Hill sphere sizes: our arithmetic, section 19.9. Stable orbits only well inside the Hill sphere: standard.
    - How the quasi-satellite loop works: standard; section 19.9 works it out.

## 19.7 Old spacecraft and new arrivals { #future }

Landers sent to Mars are cleaned very carefully, so they do not bring Earth microbes with them. Orbiters are not
cleaned so hard, so they must not fall onto Mars too soon. The rule is that an orbiter must stay up for **at least 20
years** after arriving, with 99% certainty, and for 50 years with 95% certainty. That is why orbiters are parked high
enough at the end of their missions, and why low aerobraking passes
([chapter 17](17-Arriving.md#aerobraking)) are planned so carefully.

So Mars keeps its dead spacecraft. In 2016 there were thought to be **eight derelicts** in orbit, whose exact
positions are not well known. The Viking 1 orbiter, from 1976, was not expected to come down until at least 2019.
Mariner 9, the first spacecraft to orbit another planet, in 1971, was expected to enter the atmosphere around 2022.
MAVEN and MOM have since joined them.

New ones are on the way:

- **MMX**, launched 19 October 2026, due in August 2027, to orbit Mars and then Phobos.
- **ESCAPADE**, NASA's twin spacecraft Blue and Gold, due in Mars orbit by September 2027, to study how the
  solar wind helped strip away most of Mars's air.
- **Mars Express** is confirmed to the end of 2026 and provisionally to 2028. A newer plan could keep it going
  to 2034, ready to support MMX in 2029.

??? note "Sources"
    - The rule of at least 20 years with 99% probability and 50 years with 95% probability: Wikipedia,
      [Planetary protection](https://en.wikipedia.org/wiki/Planetary_protection) (weaker). That landers are cleaned
      more strictly, and why the rule exists: standard.
    - Eight derelicts believed in orbit as of 2016; Viking 1 orbiter not expected to decay until at least 2019;
      Mariner 9, in orbit from 1971, expected to enter the atmosphere around 2022: Wikipedia, List of
      missions to Mars (above). Mariner 9 as the first spacecraft to orbit another planet, and the Viking 1
      orbiter arriving in 1976: standard.
    - MMX: section 19.2. ESCAPADE's twin spacecraft, due by September 2027, to study Mars's magnetosphere and
      how the solar wind helped strip its air: Wikipedia, [ESCAPADE](https://en.wikipedia.org/wiki/ESCAPADE)
      (weaker), as in chapter 15, section 15.3.
    - Mars Express confirmed to 31 December 2026 and provisionally to 31 December 2028, and the update that could
      keep it going to 2034 to support MMX in 2029: Wikipedia, Mars Express (above).

## 19.8 Working it out { #working }

Use $GM = 42{,}828$ km³/s² and radius $R = 3{,}396$ km for Mars, and its turn of 24.623 hours.

| | Mars | Earth |
| --- | --- | --- |
| Stationary orbit, from the centre | 20,428 km | 42,164 km |
| Stationary orbit, height | 17,032 km | 35,786 km |
| Period of an orbit 300 km up | 114 minutes | 90.5 minutes |
| Longest pass over a lander, 300 km up | 14.7 minutes | 8.7 minutes |
| Moons inside the stationary orbit | Phobos | none |

**Phobos in the sky.** Phobos goes round in 7.654 hours and the ground in 24.623 hours, so Phobos gains one lap on the
ground every

$$\frac{1}{1/7.654 - 1/24.623} = 11.11 \text{ hours}.$$

From the equator it is above the horizon while it is within an angle $\theta$ of overhead, measured at Mars's centre,
where $\cos\theta = R/a = 3{,}396/9{,}376$, so $\theta = 68.8°$. It is up for $2 \times 68.8/360$ of 11.11 hours,
**4.24 hours**. The source's 4 h 15 min matches.

**Deimos in the sky.** Deimos is slower than the ground, so the ground gains on it:
$1/(1/24.623 - 1/30.312) = 131.2$ hours, about 5.5 days. With $\cos\theta = 3{,}396/23{,}458$, $\theta = 81.7°$,
and it is up for $2 \times 81.7/360 \times 131.2 = $ **59.5 hours**, about two and a half days.

**Sizes in the sky.** Phobos, 22 km wide and about 5,980 km up, spans $22/5{,}980$ rad $= 0.21°$. The Sun, 1.39
million km wide at 228 million km, spans $0.35°$. Deimos, 12.4 km wide at 20,060 km, spans $0.035°$. Phobos crosses
the sky's 180° in roughly 4 hours, so it crosses the Sun's 0.35° in about $0.35/180 \times 4$ hours, about 30 seconds.

**The stationary orbit.** $r^3 = GM\,T^2/(4\pi^2)$ with $T = 88{,}642$ s gives $r = 20{,}428$ km, 17,032 km up. The
edge of its view is where $\cos\theta = 3{,}396/20{,}428$, $\theta = 80.4°$.

**A relay pass.** At 300 km, $r = 3{,}696$ km and $T = 2\pi\sqrt{r^3/GM} = 6{,}822$ s $= 113.7$ minutes. The lander
can see it while it is within $\theta$ of overhead, $\cos\theta = 3{,}396/3{,}696$, $\theta = 23.3°$. A pass straight
overhead lasts $2 \times 23.3/360 \times 113.7 = $ **14.7 minutes**, less if it passes to one side.

??? note "Sources"
    - Mars's $GM$ and radius: chapter 6. The Earth's numbers: chapter 14. Phobos's and Deimos's distances and
      periods: chapter 8 and the Wikipedia pages above.
    - Everything else: our arithmetic. It treats the orbits as circles over the equator and ignores Mars's turn
      during a relay pass. Our simple 68.8° gives a latitude limit a little below the source's 70.4°.

## 19.9 A small moon's reach, worked out { #derive }

**The Hill sphere.** Put a spacecraft at distance $r$ from a moon of mass $m$, on the line to a planet of mass $M$,
with the moon at distance $a$ from the planet. Going round with the moon, the spacecraft feels three things along that
line: the moon's pull $Gm/r^2$, and the difference between the planet's pull and the push outwards of going round,
which for small $r$ comes to $3GM r/a^3$ pulling it away. They balance where

$$\frac{Gm}{r^2} = \frac{3GMr}{a^3}, \qquad r_H = a\left(\frac{m}{3M}\right)^{1/3}.$$

- **Phobos:** $m = 1.064 \times 10^{16}$ kg, $M = 6.417 \times 10^{23}$ kg, $a = 9{,}376$ km.
  $m/3M = 5.53 \times 10^{-9}$, its cube root is $1.77 \times 10^{-3}$, and $r_H =$ **16.6 km**, against
  the 13 km from Phobos's centre to the tip of its long axis.
- **Deimos:** $m = 1.44 \times 10^{15}$ kg, $a = 23{,}458$ km: $r_H =$ **21.3 km**, against its 6.2 km radius.
  Chapter 6 used NASA's larger mass, $2.4 \times 10^{15}$ kg, which gives 25 km; either way it is tight.

**The quasi-satellite loop.** Take an orbit round Mars with the same $a$ as Phobos, so the same period, but a small
eccentricity $e$. To first order in $e$ its distance from Mars is $r = a(1 - e\cos M)$, where $M$ is the mean
anomaly, the angle Phobos itself has turned. Its true angle runs ahead of Phobos by $2e\sin M$. So, measured from
Phobos,

$$x = -ae\cos M \text{ (outwards)}, \qquad y = 2ae\sin M \text{ (along the orbit)}.$$

That is an ellipse twice as long as it is wide, gone round once per orbit. As $M$ grows, the point moves from inside
($x < 0$) to ahead ($y > 0$) to outside to behind: the opposite way to Phobos's own motion round Mars. For a loop
reaching about 100 km along the orbit, $2ae = 100$ km and $e = 100/18{,}752 = 0.0053$; it comes about 50 km above and
below. That is far outside the 17 km Hill sphere, so Mars steers the spacecraft and Phobos only nudges it.

??? note "Sources"
    - Phobos's mass: chapter 6, from Guo, Yan and others. Deimos's mass, $1.441 \times 10^{15}$ kg: Wikipedia, Deimos
      (moon) (above). Mars's mass: from its $GM$, chapter 6. Phobos's long axis: section 19.1.
    - The Hill radius and its derivation, and the first-order motion of a slightly eccentric orbit, $r = a(1 - e\cos
      M)$ and an angle $M + 2e\sin M$: standard.
    - The numbers and the loop's direction: our arithmetic.

## Check yourself { #check }

**1.** (beginner) Which way does Phobos cross the Martian sky, and why?

??? note "Answer"
    West to east. It goes round Mars faster than Mars turns, so it overtakes the ground beneath it.

**2.** (beginner) Why can Phobos never cause a total eclipse of the Sun?

??? note "Answer"
    It is too small: about 0.2° across in the sky, while the Sun from Mars is about 0.35°. It only transits across
    the Sun as a dark blob.

**3.** (beginner) Why do rovers send most of their data up to an orbiter instead of straight to the Earth?

??? note "Answer"
    A rover's radio is small and short of power. An orbiter is only a few hundred kilometres away and has a big dish
    to send the data on to the Earth, so far more gets through.

**4.** (intermediate) Why do low orbiters like MRO and long ellipses like Hope's do different jobs?

??? note "Answer"
    A low, nearly polar orbit sees the ground close up and, as Mars turns, passes over every part of it. A long
    ellipse swings far out and sees a whole face of Mars at once, good for weather and dust storms.

**5.** (intermediate) Why would a satellite in the areostationary orbit need extra fuel to stay in place?

??? note "Answer"
    The orbit lies between Phobos and Deimos, and their repeated pulls build up through resonances. Mars's uneven
    gravity also pushes it towards one of two stable longitudes.

**6.** (intermediate) Why must a Mars orbiter stay up for at least 20 years?

??? note "Answer"
    Orbiters are not cleaned as strictly as landers. If one fell onto Mars soon, it might carry living Earth microbes
    there. After decades in space, far fewer would survive.

**7.** (advanced) TGO orbits about 400 km up. How long can a lander see it on a pass straight overhead?

??? note "Answer"
    $r = 3{,}796$ km, so $T = 2\pi\sqrt{3{,}796^3/42{,}828} = 7{,}101$ s, about 118 minutes. $\cos\theta =
    3{,}396/3{,}796$ gives $\theta = 26.5°$, so the pass lasts $2 \times 26.5/360 \times 118 = 17.4$ minutes.

**8.** (expert) A quasi-satellite orbit round Phobos reaches 200 km ahead and behind it. What eccentricity is that,
and how far above and below Phobos's orbit does it go?

??? note "Answer"
    $2ae = 200$ km with $a = 9{,}376$ km gives $e = 0.0107$. It goes $ae = 100$ km inside and outside Phobos's orbit.

## Summary

- Phobos goes round faster than Mars turns, so it rises in the west every 11 hours and crosses the sky in about 4.
  Deimos is just slower than Mars and stays up for about two and a half days.
- The moons may be captured asteroids or rubble from a giant impact; MMX, launched in October 2026, will bring back a
  piece of Phobos to tell.
- Six orbiters were working in late 2026: Odyssey, Mars Express, MRO, TGO, Hope and the Tianwen-1 orbiter. Low orbits
  see the ground close up; long ellipses see the whole planet.
- Orbiters relay data from rovers. A pass from 300 km up lasts at most about 15 minutes.
- The areostationary orbit, 17,032 km up, would be ideal for relays but nobody uses it; Phobos and Deimos make it
  costly to hold.
- Phobos's gravity only wins within about 17 km, so spacecraft fly quasi-satellite orbits round Mars that loop round
  the moon instead.
- Orbiters must stay up for at least 20 years, so Mars keeps its dead spacecraft.

**Next:** chapter 20, Mars's changing orbit and tilt, where we follow Mars's own orbit and axis over millions of
years, and see how their slow swings change its climate and its ice.

## Further reading

- Alfred S. McEwen, Candice Hansen-Koharcheck and Ari Espinoza, *Mars: The Pristine Beauty of the Red Planet*,
  University of Arizona Press, 2017. Pictures from MRO's HiRISE camera, one of the orbiters in this chapter.
