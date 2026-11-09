# 18. Where the Sun's wind ends

*The Sun does not only shine. It also blows: a thin, hot wind of charged particles streams out from it in every
direction at hundreds of kilometres a second, carrying the Sun's magnetic field with it. The wind fills the whole
solar system and blows a bubble in the gas between the stars, and only two spacecraft have ever reached its edge. This
chapter follows the wind from the Sun to that edge: what the wind is, why its magnetic field winds into a spiral, what
the Voyagers found at the boundary, the storms that ride on the wind, how people around the world worked it out, the
spacecraft that measure it today, what it does at Mars, and a short calculation that shows why the bubble ends about
100 AU out.*

!!! abstract "In this chapter"
    **You will learn:**

    - what the solar wind is made of, how fast it blows, and why the Sun loses a million tonnes a second to it
    - why the Sun's magnetic field is wound into a spiral as the wind carries it out
    - what the termination shock, the heliosheath and the heliopause are, and what the Voyagers found there
    - how storms on the Sun travel out on the wind, from the Carrington event of 1859 to the great storm of May 2024
    - how people from Assyria and Japan to Norway, Germany, the Soviet Union and the United States worked out the wind
    - which spacecraft measure the wind today, from Parker Solar Probe near the Sun to Voyager 1 a light-day away
    - how the wind meets Mars, a planet with no magnetic field to shield it
    - how to work out how far the wind reaches, by balancing its push against the push from outside

    **You need:** chapter 6 (section 6.4) for the Earth's magnetic shield; chapter 17 for comet tails; book 3, chapter 9
    (section 9.3), for the L1 point.

    **Levels:** 18.1 to 18.3 are beginner; 18.4 to 18.7 are intermediate; 18.8 is advanced; 18.9 is expert.

## 18.1 The solar wind { #basics }

**A wind of charged particles.** The **solar wind** is a stream of charged particles flowing out from the Sun's outer
layer, the **corona**. It is mostly electrons, protons and alpha particles (the nuclei of helium atoms), with traces of
heavier atoms. A gas of charged particles like this is called a **plasma**.

**Why it blows.** The corona is hotter than a million kelvin. Its particles move at about 145 km/s on average, well
below the 618 km/s needed to escape the Sun. But the light electrons move much faster and do escape, and as they leave
they set up an electric field that pulls the heavier ions out after them. Far from the Sun the wind blows faster than
the speed of sound in it.

**Two kinds of wind.** Near the Earth there are two kinds.

| | Slow wind | Fast wind |
| --- | --- | --- |
| Speed | 300 to 500 km/s | about 750 km/s |
| Temperature | about 100,000 K | about 800,000 K |
| Density | about twice as dense | |
| Comes from | the **streamer belt** round the Sun's equator | **coronal holes**, often near the poles |

**At the Earth.** At 1 AU the wind blows at 250 to 750 km/s, with 3 to 10 particles in each cubic centimetre, billions
of billions of times thinner than the air we breathe. At 400 km/s it takes about **4.3 days** to get here (section
18.8).

**Where the wind begins.** Close to the Sun, the corona's magnetic field still holds the gas. The wind breaks free at
the **Alfvén surface**, once thought to lie 10 to 20 solar radii out. On **28 April 2021** Parker Solar Probe crossed
it at **18.8 solar radii**, the first spacecraft to fly inside the corona.

**What the Sun loses.** The wind carries off about $1.3 \times 10^{36}$ particles a second, **1.3 to 1.9 million tonnes
a second**, an Earth's mass every 150 million years. Even so, in all its life the Sun has lost only about 0.01% of its
mass this way.

??? note "Sources"
    - What the wind is made of, the corona over a megakelvin, the 145 km/s average and 618 km/s escape speed, the
      electrons escaping and setting up an electric field, supersonic flow, slow wind at 300 to 500 km/s and 100,000 K
      from the streamer belt and twice as dense, fast wind at 750 km/s and 800,000 K from coronal holes near the
      poles, 250 to 750 km/s and 3 to 10 particles per cm³ at 1 AU, the Alfvén surface at 10 to 20 solar radii and
      Parker Solar Probe inside it at 18.8 on 28 April 2021, $1.3 \times 10^{36}$ particles a second, 1.3 to 1.9
      million tonnes a second, an Earth mass every 150 million years and 0.01% since the Sun formed: Wikipedia,
      [Solar wind](https://en.wikipedia.org/wiki/Solar_wind) (weaker).
    - "Inside the corona": NASA's "touching the Sun", from Wikipedia,
      [Parker Solar Probe](https://en.wikipedia.org/wiki/Parker_Solar_Probe) (weaker). "Billions of billions of times
      thinner than air": standard, as air has about $2.5 \times 10^{19}$ molecules per cm³.
    - The 4.3 days: our arithmetic (section 18.8).

## 18.2 The Sun's field, wound into a spiral { #spiral }

**The field goes too.** Because the wind is a plasma, it conducts electricity, and the Sun's magnetic field is carried
out with it, as if the field lines were frozen into the gas.

**A turning sprinkler.** The wind blows straight out from the Sun. But the Sun turns, once in about **25 days**, and
each field line stays tied at its foot to the turning Sun. So the field lines wind up into a spiral, like the stream
of water from a turning garden sprinkler. This is the **Parker spiral**, named for Eugene Parker, who worked it out in
1958 (section 18.5).

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="The solar system out to Mars seen from above the Sun's north pole, with the orbits of the Earth at 1 astronomical unit and Mars at 1.52. Short arrows show the solar wind blowing straight out from the Sun in every direction. Four curved lines show the Sun's magnetic field carried out by the wind: because the Sun turns once in about 25 days, each line is wound back into a spiral, like the stream from a turning garden sprinkler. Where a line crosses the Earth's orbit it makes an angle of about 47 degrees with the line to the Sun, and at Mars about 58 degrees.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">The Sun's field, wound into a spiral</text>
    <circle cx="150.0" cy="118.0" r="52.0" fill="none" stroke="#cfc8bf" stroke-width="0.7" stroke-dasharray="2 2"/>
    <circle cx="150.0" cy="118.0" r="79.2" fill="none" stroke="#cfc8bf" stroke-width="0.7" stroke-dasharray="2 2"/>
    <line x1="164.8" y1="111.9" x2="177.7" y2="106.5" stroke="#eea66f" stroke-width="0.9"/>
    <path d="M 180.5 105.4 L 178.5 108.4 L 177.0 104.7 z" fill="#eea66f"/>
    <line x1="156.1" y1="103.2" x2="161.5" y2="90.3" stroke="#eea66f" stroke-width="0.9"/>
    <path d="M 162.6 87.5 L 163.3 91.0 L 159.6 89.5 z" fill="#eea66f"/>
    <line x1="143.9" y1="103.2" x2="138.5" y2="90.3" stroke="#eea66f" stroke-width="0.9"/>
    <path d="M 137.4 87.5 L 140.4 89.5 L 136.7 91.0 z" fill="#eea66f"/>
    <line x1="135.2" y1="111.9" x2="122.3" y2="106.5" stroke="#eea66f" stroke-width="0.9"/>
    <path d="M 119.5 105.4 L 123.0 104.7 L 121.5 108.4 z" fill="#eea66f"/>
    <line x1="135.2" y1="124.1" x2="122.3" y2="129.5" stroke="#eea66f" stroke-width="0.9"/>
    <path d="M 119.5 130.6 L 121.5 127.6 L 123.0 131.3 z" fill="#eea66f"/>
    <line x1="143.9" y1="132.8" x2="138.5" y2="145.7" stroke="#eea66f" stroke-width="0.9"/>
    <path d="M 137.4 148.5 L 136.7 145.0 L 140.4 146.5 z" fill="#eea66f"/>
    <line x1="156.1" y1="132.8" x2="161.5" y2="145.7" stroke="#eea66f" stroke-width="0.9"/>
    <path d="M 162.6 148.5 L 159.6 146.5 L 163.3 145.0 z" fill="#eea66f"/>
    <line x1="164.8" y1="124.1" x2="177.7" y2="129.5" stroke="#eea66f" stroke-width="0.9"/>
    <path d="M 180.5 130.6 L 177.0 131.3 L 178.5 127.6 z" fill="#eea66f"/>
    <polyline points="152.5,117.4 153.0,117.3 153.5,117.2 154.1,117.1 154.6,117.1 155.1,117.0 155.6,117.0 156.1,116.9 156.7,116.9 157.2,116.9 157.7,116.9 158.3,116.9 158.8,117.0 159.3,117.0 159.8,117.0 160.4,117.1 160.9,117.2 161.4,117.3 161.9,117.4 162.5,117.5 163.0,117.6 163.5,117.7 164.0,117.9 164.6,118.0 165.1,118.2 165.6,118.3 166.1,118.5 166.6,118.7 167.1,118.9 167.6,119.1 168.1,119.4 168.7,119.6 169.2,119.9 169.6,120.1 170.1,120.4 170.6,120.7 171.1,121.0 171.6,121.3 172.1,121.6 172.5,121.9 173.0,122.2 173.5,122.6 173.9,122.9 174.4,123.3 174.8,123.7 175.3,124.1 175.7,124.5 176.2,124.9 176.6,125.3 177.0,125.7 177.4,126.2 177.8,126.6 178.2,127.1 178.6,127.5 179.0,128.0 179.4,128.5 179.8,129.0 180.1,129.5 180.5,130.0 180.8,130.5 181.2,131.1 181.5,131.6 181.8,132.1 182.2,132.7 182.5,133.3 182.8,133.8 183.1,134.4 183.4,135.0 183.6,135.6 183.9,136.2 184.2,136.8 184.4,137.4 184.6,138.1 184.9,138.7 185.1,139.4 185.3,140.0 185.5,140.7 185.7,141.3 185.9,142.0 186.0,142.7 186.2,143.4 186.4,144.0 186.5,144.7 186.6,145.4 186.7,146.1 186.8,146.9 186.9,147.6 187.0,148.3 187.1,149.0 187.2,149.8 187.2,150.5 187.2,151.2 187.3,152.0 187.3,152.7 187.3,153.5 187.3,154.3 187.3,155.0 187.2,155.8 187.2,156.6 187.1,157.3 187.0,158.1 187.0,158.9 186.9,159.7 186.8,160.5 186.6,161.3 186.5,162.0 186.4,162.8 186.2,163.6 186.0,164.4 185.8,165.2 185.6,166.0 185.4,166.8 185.2,167.6 185.0,168.4 184.7,169.2 184.4,170.0 184.2,170.8 183.9,171.6 183.6,172.4 183.3,173.2 182.9,174.0 182.6,174.8 182.2,175.6 181.9,176.4 181.5,177.2 181.1,178.0 180.7,178.8 180.2,179.6 179.8,180.4 179.4,181.2 178.9,182.0 178.4,182.8 177.9,183.5 177.4,184.3 176.9,185.1 176.4,185.9 175.8,186.6 175.3,187.4 174.7,188.1 174.1,188.9 173.5,189.6 172.9,190.4 172.3,191.1 171.6,191.9 171.0,192.6 170.3,193.3 169.6,194.0 168.9,194.7 168.2,195.4 167.5,196.1 166.8,196.8 166.0,197.5 165.3,198.2 164.5,198.9 163.7,199.5 162.9,200.2 162.1,200.8 161.3,201.5 160.5,202.1 159.6,202.7 158.8,203.3 157.9,204.0 157.0,204.6 156.1,205.1 155.2,205.7 154.3,206.3 153.4,206.9 152.5,207.4 151.5,207.9 150.6,208.5 149.6,209.0 148.6,209.5 147.6,210.0 146.6,210.5 145.6,211.0 144.6,211.4 143.5,211.9 142.5,212.3 141.4,212.8 140.4,213.2 139.3,213.6" fill="none" stroke="#5aa0d8" stroke-width="1.3"/>
    <polyline points="149.4,115.5 149.3,115.0 149.2,114.5 149.1,113.9 149.1,113.4 149.0,112.9 149.0,112.4 148.9,111.9 148.9,111.3 148.9,110.8 148.9,110.3 148.9,109.7 149.0,109.2 149.0,108.7 149.0,108.2 149.1,107.6 149.2,107.1 149.3,106.6 149.4,106.1 149.5,105.5 149.6,105.0 149.7,104.5 149.9,104.0 150.0,103.4 150.2,102.9 150.3,102.4 150.5,101.9 150.7,101.4 150.9,100.9 151.1,100.4 151.4,99.9 151.6,99.3 151.9,98.8 152.1,98.4 152.4,97.9 152.7,97.4 153.0,96.9 153.3,96.4 153.6,95.9 153.9,95.5 154.2,95.0 154.6,94.5 154.9,94.1 155.3,93.6 155.7,93.2 156.1,92.7 156.5,92.3 156.9,91.8 157.3,91.4 157.7,91.0 158.2,90.6 158.6,90.2 159.1,89.8 159.5,89.4 160.0,89.0 160.5,88.6 161.0,88.2 161.5,87.9 162.0,87.5 162.5,87.2 163.1,86.8 163.6,86.5 164.1,86.2 164.7,85.8 165.3,85.5 165.8,85.2 166.4,84.9 167.0,84.6 167.6,84.4 168.2,84.1 168.8,83.8 169.4,83.6 170.1,83.4 170.7,83.1 171.4,82.9 172.0,82.7 172.7,82.5 173.3,82.3 174.0,82.1 174.7,82.0 175.4,81.8 176.0,81.6 176.7,81.5 177.4,81.4 178.1,81.3 178.9,81.2 179.6,81.1 180.3,81.0 181.0,80.9 181.8,80.8 182.5,80.8 183.2,80.8 184.0,80.7 184.7,80.7 185.5,80.7 186.3,80.7 187.0,80.7 187.8,80.8 188.6,80.8 189.3,80.9 190.1,81.0 190.9,81.0 191.7,81.1 192.5,81.2 193.3,81.4 194.0,81.5 194.8,81.6 195.6,81.8 196.4,82.0 197.2,82.2 198.0,82.4 198.8,82.6 199.6,82.8 200.4,83.0 201.2,83.3 202.0,83.6 202.8,83.8 203.6,84.1 204.4,84.4 205.2,84.7 206.0,85.1 206.8,85.4 207.6,85.8 208.4,86.1 209.2,86.5 210.0,86.9 210.8,87.3 211.6,87.8 212.4,88.2 213.2,88.6 214.0,89.1 214.8,89.6 215.5,90.1 216.3,90.6 217.1,91.1 217.9,91.6 218.6,92.2 219.4,92.7 220.1,93.3 220.9,93.9 221.6,94.5 222.4,95.1 223.1,95.7 223.9,96.4 224.6,97.0 225.3,97.7 226.0,98.4 226.7,99.1 227.4,99.8 228.1,100.5 228.8,101.2 229.5,102.0 230.2,102.7 230.9,103.5 231.5,104.3 232.2,105.1 232.8,105.9 233.5,106.7 234.1,107.5 234.7,108.4 235.3,109.2 236.0,110.1 236.6,111.0 237.1,111.9 237.7,112.8 238.3,113.7 238.9,114.6 239.4,115.5 239.9,116.5 240.5,117.4 241.0,118.4 241.5,119.4 242.0,120.4 242.5,121.4 243.0,122.4 243.4,123.4 243.9,124.5 244.3,125.5 244.8,126.6 245.2,127.6 245.6,128.7" fill="none" stroke="#5aa0d8" stroke-width="1.3"/>
    <polyline points="147.5,118.6 147.0,118.7 146.5,118.8 145.9,118.9 145.4,118.9 144.9,119.0 144.4,119.0 143.9,119.1 143.3,119.1 142.8,119.1 142.3,119.1 141.7,119.1 141.2,119.0 140.7,119.0 140.2,119.0 139.6,118.9 139.1,118.8 138.6,118.7 138.1,118.6 137.5,118.5 137.0,118.4 136.5,118.3 136.0,118.1 135.4,118.0 134.9,117.8 134.4,117.7 133.9,117.5 133.4,117.3 132.9,117.1 132.4,116.9 131.9,116.6 131.3,116.4 130.8,116.1 130.4,115.9 129.9,115.6 129.4,115.3 128.9,115.0 128.4,114.7 127.9,114.4 127.5,114.1 127.0,113.8 126.5,113.4 126.1,113.1 125.6,112.7 125.2,112.3 124.7,111.9 124.3,111.5 123.8,111.1 123.4,110.7 123.0,110.3 122.6,109.8 122.2,109.4 121.8,108.9 121.4,108.5 121.0,108.0 120.6,107.5 120.2,107.0 119.9,106.5 119.5,106.0 119.2,105.5 118.8,104.9 118.5,104.4 118.2,103.9 117.8,103.3 117.5,102.7 117.2,102.2 116.9,101.6 116.6,101.0 116.4,100.4 116.1,99.8 115.8,99.2 115.6,98.6 115.4,97.9 115.1,97.3 114.9,96.6 114.7,96.0 114.5,95.3 114.3,94.7 114.1,94.0 114.0,93.3 113.8,92.6 113.6,92.0 113.5,91.3 113.4,90.6 113.3,89.9 113.2,89.1 113.1,88.4 113.0,87.7 112.9,87.0 112.8,86.2 112.8,85.5 112.8,84.8 112.7,84.0 112.7,83.3 112.7,82.5 112.7,81.7 112.7,81.0 112.8,80.2 112.8,79.4 112.9,78.7 113.0,77.9 113.0,77.1 113.1,76.3 113.2,75.5 113.4,74.7 113.5,74.0 113.6,73.2 113.8,72.4 114.0,71.6 114.2,70.8 114.4,70.0 114.6,69.2 114.8,68.4 115.0,67.6 115.3,66.8 115.6,66.0 115.8,65.2 116.1,64.4 116.4,63.6 116.7,62.8 117.1,62.0 117.4,61.2 117.8,60.4 118.1,59.6 118.5,58.8 118.9,58.0 119.3,57.2 119.8,56.4 120.2,55.6 120.6,54.8 121.1,54.0 121.6,53.2 122.1,52.5 122.6,51.7 123.1,50.9 123.6,50.1 124.2,49.4 124.7,48.6 125.3,47.9 125.9,47.1 126.5,46.4 127.1,45.6 127.7,44.9 128.4,44.1 129.0,43.4 129.7,42.7 130.4,42.0 131.1,41.3 131.8,40.6 132.5,39.9 133.2,39.2 134.0,38.5 134.7,37.8 135.5,37.1 136.3,36.5 137.1,35.8 137.9,35.2 138.7,34.5 139.5,33.9 140.4,33.3 141.2,32.7 142.1,32.0 143.0,31.4 143.9,30.9 144.8,30.3 145.7,29.7 146.6,29.1 147.5,28.6 148.5,28.1 149.4,27.5 150.4,27.0 151.4,26.5 152.4,26.0 153.4,25.5 154.4,25.0 155.4,24.6 156.5,24.1 157.5,23.7 158.6,23.2 159.6,22.8 160.7,22.4" fill="none" stroke="#5aa0d8" stroke-width="1.3"/>
    <polyline points="150.6,120.5 150.7,121.0 150.8,121.5 150.9,122.1 150.9,122.6 151.0,123.1 151.0,123.6 151.1,124.1 151.1,124.7 151.1,125.2 151.1,125.7 151.1,126.3 151.0,126.8 151.0,127.3 151.0,127.8 150.9,128.4 150.8,128.9 150.7,129.4 150.6,129.9 150.5,130.5 150.4,131.0 150.3,131.5 150.1,132.0 150.0,132.6 149.8,133.1 149.7,133.6 149.5,134.1 149.3,134.6 149.1,135.1 148.9,135.6 148.6,136.1 148.4,136.7 148.1,137.2 147.9,137.6 147.6,138.1 147.3,138.6 147.0,139.1 146.7,139.6 146.4,140.1 146.1,140.5 145.8,141.0 145.4,141.5 145.1,141.9 144.7,142.4 144.3,142.8 143.9,143.3 143.5,143.7 143.1,144.2 142.7,144.6 142.3,145.0 141.8,145.4 141.4,145.8 140.9,146.2 140.5,146.6 140.0,147.0 139.5,147.4 139.0,147.8 138.5,148.1 138.0,148.5 137.5,148.8 136.9,149.2 136.4,149.5 135.9,149.8 135.3,150.2 134.7,150.5 134.2,150.8 133.6,151.1 133.0,151.4 132.4,151.6 131.8,151.9 131.2,152.2 130.6,152.4 129.9,152.6 129.3,152.9 128.6,153.1 128.0,153.3 127.3,153.5 126.7,153.7 126.0,153.9 125.3,154.0 124.6,154.2 124.0,154.4 123.3,154.5 122.6,154.6 121.9,154.7 121.1,154.8 120.4,154.9 119.7,155.0 119.0,155.1 118.2,155.2 117.5,155.2 116.8,155.2 116.0,155.3 115.3,155.3 114.5,155.3 113.7,155.3 113.0,155.3 112.2,155.2 111.4,155.2 110.7,155.1 109.9,155.0 109.1,155.0 108.3,154.9 107.5,154.8 106.7,154.6 106.0,154.5 105.2,154.4 104.4,154.2 103.6,154.0 102.8,153.8 102.0,153.6 101.2,153.4 100.4,153.2 99.6,153.0 98.8,152.7 98.0,152.4 97.2,152.2 96.4,151.9 95.6,151.6 94.8,151.3 94.0,150.9 93.2,150.6 92.4,150.2 91.6,149.9 90.8,149.5 90.0,149.1 89.2,148.7 88.4,148.2 87.6,147.8 86.8,147.4 86.0,146.9 85.2,146.4 84.5,145.9 83.7,145.4 82.9,144.9 82.1,144.4 81.4,143.8 80.6,143.3 79.9,142.7 79.1,142.1 78.4,141.5 77.6,140.9 76.9,140.3 76.1,139.6 75.4,139.0 74.7,138.3 74.0,137.6 73.3,136.9 72.6,136.2 71.9,135.5 71.2,134.8 70.5,134.0 69.8,133.3 69.1,132.5 68.5,131.7 67.8,130.9 67.2,130.1 66.5,129.3 65.9,128.5 65.3,127.6 64.7,126.8 64.0,125.9 63.4,125.0 62.9,124.1 62.3,123.2 61.7,122.3 61.1,121.4 60.6,120.5 60.1,119.5 59.5,118.6 59.0,117.6 58.5,116.6 58.0,115.6 57.5,114.6 57.0,113.6 56.6,112.6 56.1,111.5 55.7,110.5 55.2,109.4 54.8,108.4 54.4,107.3" fill="none" stroke="#5aa0d8" stroke-width="1.3"/>
    <circle cx="150.0" cy="118.0" r="7" fill="#eea66f"/>
    <path d="M 161.0 114.0 A 11.7 11.7 0 0 0 154.0 107.0" fill="none" stroke="currentColor" stroke-width="0.8"/>
    <path d="M 154.0 107.0 l 3.5 -1.5 l -0.5 3.5 z" fill="currentColor"/>
    <text x="159.0" y="104.0">Sun turns</text>
    <line x1="150.0" y1="118.0" x2="200.3" y2="167.0" stroke="#555" stroke-width="0.6" stroke-dasharray="1.5 1.5"/>
    <circle cx="187.3" cy="154.3" r="3.2" fill="#5aa0d8"/>
    <text x="193.3" y="157.3">Earth, 47°</text>
    <line x1="150.0" y1="118.0" x2="172.9" y2="212.7" stroke="#555" stroke-width="0.6" stroke-dasharray="1.5 1.5"/>
    <circle cx="168.7" cy="195.0" r="3.2" fill="#c1440e"/>
    <text x="174.7" y="198.0">Mars, 58°</text>
    <text x="208.0" y="32.0" fill="#eea66f">wind blows straight out</text>
    <text x="30.0" y="36.0" fill="#5aa0d8">field lines are wound back</text>
    <text x="6" y="226">Seen from above the Sun's north pole. The wind, about 400 km/s, blows straight out, but each field</text>
    <text x="6" y="235">line stays tied to the turning Sun, so it winds into a spiral. The angle to the line to the Sun is</text>
    <text x="6" y="244">about 47° at the Earth and 58° at Mars (section 18.8). Orbits to scale; 1 AU is the Earth's orbit.</text>
  </g>
</svg>
</div>

| Where | Angle of the field to the line from the Sun |
| --- | --- |
| Earth, 1 AU | 47° |
| Mars, 1.52 AU | 58° |
| Jupiter, 5.2 AU | 80° |
| Neptune, 30 AU | 88° |

Beyond about 10 to 20 AU the field runs almost round the Sun rather than out from it.

**A ballerina's skirt.** The field points outward over one half of the Sun and inward over the other. The surface
between the two halves, where an electric current flows, is the **heliospheric current sheet**. It is only about
**10,000 km** thick near the Earth's orbit, but it reaches out to the edge of the bubble, the largest structure in the
solar system. Because the Sun's magnetic poles are tilted from its spin axis, the sheet is wavy, and as it turns it
looks like a twirling ballerina's skirt. The Earth passes above and below it as it turns. At each solar maximum the
Sun's whole field flips, so the field in the wind flips too.

**Switchbacks.** The field in the wind is not smooth. Ulysses, the first spacecraft to fly over the Sun's poles, found
sudden kinks where it doubles back on itself, now called **switchbacks**. Parker Solar Probe saw its first on 6
November 2018, and has found many more close to the Sun.

??? note "Sources"
    - Field lines tied to the material in the wind, the Archimedean spiral named after Parker, the garden-sprinkler
      comparison, nearly circular beyond 10 to 20 AU, the current sheet's 10,000 km near the Earth's orbit, the
      largest structure in the solar system, its waviness from the tilt of the magnetic axis, the ballerina skirt, its
      turning in about 25 days, and the field flipping at solar maximum: Wikipedia,
      [Heliospheric current sheet](https://en.wikipedia.org/wiki/Heliospheric_current_sheet) (weaker).
    - The Sun's rotation of 609.12 hours at 16° latitude: NASA,
      [Sun fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html).
    - Switchbacks first observed by Ulysses, the first spacecraft over the Sun's poles, and Parker Solar Probe's first
      on 6 November 2018: Wikipedia, Parker Solar Probe (above).
    - The angles: our arithmetic for a 400 km/s wind (section 18.8). Plasma carrying a field: standard.

## 18.3 The edge of the bubble { #bubble }

**A bubble in the Galaxy.** The wind blows a bubble in the thin gas between the stars. The bubble is the
**heliosphere**, a name first used in print in 1967, probably by Alexander J. Dessler. Inside it, the Sun's wind and
field shield the planets from much of the cosmic radiation that fills the Galaxy.

**What is outside.** The Sun is now passing through the **Local Interstellar Cloud**, gas at about **7,000 K** with
only about **0.3 atoms** in each cubic centimetre. Seen from the Earth, the gas flows in towards us from the direction
of Scorpius. By one estimate, the Sun will leave this cloud within the next 1,900 years.

**Three boundaries.** Going outward, the wind meets three changes.

| Boundary | What happens | Voyager 1 | Voyager 2 |
| --- | --- | --- | --- |
| Termination shock | the wind slows below the speed of sound and heats up | Dec 2004, 94 AU | Aug 2007, 83 AU |
| Heliosheath | slow, hot, stirred-up wind, a "foam" of magnetic bubbles about 1 AU across | | |
| Heliopause | the edge, where the Sun's plasma meets the plasma of the Galaxy | Aug 2012, 121 AU | Nov 2018, 119 AU |

On the front side the heliosheath is 10 to 100 AU thick.

**Leaving the bubble.** When Voyager 1 crossed the heliopause, the plasma around it suddenly became forty times denser.
Its own instrument for measuring plasma had failed in 1980, so the crossing was worked out from waves in the plasma,
and it was only announced in September 2013. To everyone's surprise, the magnetic field outside pointed much the same
way as the Sun's field inside. Voyager 2 still had a working plasma instrument in 2018. It saw the Sun's low-energy
particles suddenly drop away and the cosmic rays from the Galaxy rise.

**Lopsided.** Voyager 2 met the shock about 1.6 billion km closer to the Sun than Voyager 1 did, so the bubble seems
pushed in on the south side, probably by the magnetic field outside.

**What shape?** For a long time the heliosphere was drawn like a comet, round at the front, about 100 AU out, with a
long **heliotail** thousands of AU long behind. Data from Cassini and IBEX in 2009 challenged that; in 2013 IBEX
found signs of a tail with four lobes; and in 2020 a team led by Merav Opher described the shape as a deflated
**croissant**. The question is still open. In front, there may be no sharp **bow shock**, but only a gentler
**bow wave**, like the wave in front of a ship, with a "hydrogen wall" of piled-up interstellar gas.

??? note "Sources"
    - The heliosphere as the Sun's bubble, the shield against cosmic radiation, Dessler and 1967, the termination
      shock, heliosheath and heliopause, Voyager 1 at the shock in December 2004 at 94 AU, the shock at the speed of
      sound with compression and heating, the heliosheath 10 to 100 AU thick on the windward side and its magnetic
      bubbles about 1 AU wide, Voyager 1 at the heliopause on 25 August 2012 at 121 AU with a forty-fold rise in
      plasma density, announced in September 2013, the galactic field lined up with the solar one, Voyager 2 at 119 AU
      on 5 November 2018 with the drop in low-energy ions and rise in cosmic rays, the flow from Scorpius, the comet
      shape and heliotail, Cassini and IBEX in 2009, the four-lobed tail in 2013, Opher's croissant in 2020, the bow
      wave and hydrogen wall: Wikipedia, [Heliosphere](https://en.wikipedia.org/wiki/Heliosphere) (weaker).
    - Voyager 1's plasma spectrometer failing in 1980 and the plasma-wave measurement: Wikipedia,
      [Voyager 1](https://en.wikipedia.org/wiki/Voyager_1) (weaker). Voyager 2 at the shock on 30 August 2007 about
      1.6 billion km closer than Voyager 1, because of the interstellar magnetic field, and at 119.7 AU on 5 November
      2018: Wikipedia, [Voyager 2](https://en.wikipedia.org/wiki/Voyager_2) (weaker).
    - The Local Interstellar Cloud at 7,000 K and 0.3 atoms per cm³, and leaving it within 1,900 years: Wikipedia,
      [Local Interstellar Cloud](https://en.wikipedia.org/wiki/Local_Interstellar_Cloud) (weaker).
    - Voyager 2's 83 AU: our arithmetic, 94 AU less 1.6 billion km (10.7 AU). "Pushed in on the south side": the
      Heliosphere page's bulge in the north and push in the south.

## 18.4 Storms in the wind { #storms }

**Bursts of plasma.** Now and then the Sun throws off a huge, fast cloud of plasma, a **coronal mass ejection**, when
magnetic energy in its corona is suddenly let go. These are the "solar storms" of the news. When one hits the Earth it
shakes our magnetic field, a **geomagnetic storm**, and auroras spread far from the poles.

**The Carrington event, 1859.** Just before noon on **1 September 1859**, the English astronomers Richard Carrington
and Richard Hodgson each saw a brilliant flash on the Sun, the first solar flare ever recorded. The cloud of plasma
from it reached the Earth in only **17.6 hours**, where most take several days. On 1 and 2 September the strongest
geomagnetic storm on record followed. Telegraph systems across Europe and North America failed, some operators got
electric shocks, and sparks flew from the wires. Auroras were seen as far towards the equator as Mexico, Cuba,
Hawaii, Queensland, southern Japan and China, and Colombia.

**An older storm.** A Japanese diary from **1770**, found in 2017, shows auroras over Kyoto, and suggests that storm may
have been about 7% bigger than Carrington's.

**May 2024.** From **10 to 13 May 2024** a burst of storms gave the strongest geomagnetic storm since March 1989, and
auroras far from the poles. It got different names in different places: the Mother's Day storm, the Gannon storm
(after the space physicist Jennifer Gannon), the Han Anniversary storm and the Victory Day storm. The wind's push
squeezed the edge of the Earth's magnetic shield from more than **10 Earth radii** out to about **5**.

**On through the solar system.** The storms do not stop at the Earth. Measurements on the way to Mars showed that fast
clouds of plasma keep slowing down beyond the Earth's orbit, dragged back by the slower wind around them (section
18.7).

??? note "Sources"
    - Coronal mass ejections as releases of magnetic energy, called "solar storms": Wikipedia, Solar wind (above).
    - The flare of 1 September 1859 seen by "the English astronomers" Carrington and Hodgson, the 17.6 hours against
      several days, the storm of 1 and 2 September, the telegraphs, shocks and sparks, and the aurora's reach:
      Wikipedia, [Carrington Event](https://en.wikipedia.org/wiki/Carrington_Event) (weaker).
    - The 1770 diary found in 2017 and the 7%: Wikipedia, [Aurora](https://en.wikipedia.org/wiki/Aurora) (weaker).
    - The storms of 10 to 13 May 2024, the strongest since March 1989, the four names and Jennifer Gannon, and the
      magnetopause from more than 10 down to 5 Earth radii: Wikipedia,
      [May 2024 solar storms](https://en.wikipedia.org/wiki/May_2024_solar_storms) (weaker).
    - Fast CMEs slowing beyond the Earth's orbit: Wikipedia,
      [Radiation assessment detector](https://en.wikipedia.org/wiki/Radiation_assessment_detector) (weaker).
    - "Geomagnetic storm" and auroras spreading from the poles: standard.

## 18.5 Who worked it out { #history }

Long before anyone knew of the wind, people around the world saw its effects in the sky.

- **Early records.** A Chinese legend written around 2600 BCE is the oldest known written record of a winter
  aurora. Assyrian reports to the king from about 680 to 650 BCE are the oldest that can be dated (history book,
  [section 2.4](../history/02-Mesopotamia.md#omens)). In Japan, "red pheasant tails" seen across the sky in 620 CE may
  have been a red aurora, and the poet Fujiwara no Teika recorded auroras in a diary (history book,
  [section 6.7](../history/06-Korea-and-Japan.md#onmyodo)).
- **In the south.** Aboriginal Australians linked the southern aurora with fire: the Gunditjmara people of western
  Victoria called it *puae buae*, "ashes", and the Gunai people of eastern Victoria saw bushfires in the spirit world.
  The Māori of New Zealand saw *Tahunui-a-rangi*, "great torches in the sky".
- **1610.** Johannes Kepler, in a letter to Galileo, wrote of a "heavenly breeze" that pushes comets.
- **1859.** Carrington and Hodgson saw the first solar flare, followed by a great storm (section 18.4), and the idea
  grew that something flows from the Sun to the Earth.
- **About 1900 to 1913.** The Norwegian space physicist **Kristian Birkeland** set up observatories under the aurora,
  fired beams of electrons at a magnetised ball standing in for the Earth, saw rings of light form round its poles, and
  suggested that the Sun sends out both electrons and ions. In 1913 Birkeland may have been the first to predict that
  plasma fills space.
- **1940s and 1950s.** Comet tails gave the clue. The German astronomer **Paul Ahnert** is credited with first linking
  the direction of a comet's tail to a wind from the Sun, from comet Whipple–Fedke of 1942. In the 1950s the German
  astronomer **Ludwig Biermann**, puzzled that comet tails always point away from the Sun, argued that a steady stream
  of particles from the Sun pushes them. The British mathematician **Sydney Chapman** worked out
  that the corona is so hot that it must reach past the Earth's orbit.
- **1958.** The American physicist **Eugene Parker** put these together: the corona cannot sit still, but must flow
  out as a wind, faster than sound, with its field wound into a spiral. Two reviewers told the *Astrophysical Journal*
  to reject the paper; one called it "utter nonsense". The editor, **Subrahmanyan Chandrasekhar**, found no mistake in
  it and published it, though not convinced by it.
- **1959.** In January 1959 the Soviet spacecraft **Luna 1** measured the wind directly for the first time, a discovery
  made by **Konstantin Gringauz**. Luna 2, Luna 3 and Venera 1 confirmed it.
- **1962.** The American geophysicist **Marcia Neugebauer** and colleagues measured the wind with Mariner 2 on its way
  to Venus, and found its slow and fast streams.
- **2012 and 2018.** Voyager 1 and Voyager 2 left the bubble (section 18.3).
- **2018.** Parker Solar Probe became the first NASA spacecraft named after a living person. Parker watched its
  launch, and died in 2022, aged 94.

??? note "Sources"
    - The Chinese legend of about 2600 BC, the 1770 diary, the "red pheasant tails" of 620 AD, the Gunditjmara, Gunai
      and Māori names and beliefs: Wikipedia, Aurora (above). The Assyrian reports: history book, chapter 2. Teika:
      history book, chapter 6.
    - Kepler's letter of 1610 and the "heavenly breeze", Carrington, Birkeland ("Norwegian scientist") on ions and
      electrons, Ahnert ("German astronomer") and comet Whipple–Fedke, Biermann ("German astronomer"), Chapman
      ("British mathematician"), Parker's 1958 paper, the two reviewers and "utter nonsense", Chandrasekhar overruling
      them while disagreeing, Luna 1 in January 1959 and Gringauz, Luna 2, Luna 3 and Venera 1, and Neugebauer
      ("American geophysicist") with Mariner 2 and its two components: Wikipedia, Solar wind (above).
    - Birkeland ("Norwegian space physicist"), the polar observatories, the terrella and the 1913 prediction: Wikipedia,
      [Kristian Birkeland](https://en.wikipedia.org/wiki/Kristian_Birkeland) (weaker). Biermann's "solar corpuscular
      radiation": Wikipedia, [Ludwig Biermann](https://en.wikipedia.org/wiki/Ludwig_Biermann) (weaker).
    - Parker as an "American solar and plasma physicist", watching the launch in 2018, and dying on 15 March 2022 aged
      94: Wikipedia, [Eugene Parker](https://en.wikipedia.org/wiki/Eugene_Parker) (weaker). The first NASA spacecraft
      named after a living person: Wikipedia, Parker Solar Probe (above).
    - Mariner 2 going to Venus: standard. The dates "about 1900 to 1913": the polar expedition of 1899 to 1900 and the
      1913 prediction, from the Birkeland page.

## 18.6 Spacecraft in the wind { #missions }

**The wind in the Moon's soil.** The Apollo astronauts put out sheets of aluminium foil to catch the wind, and the
soil they brought home turned out to be rich in atoms planted by the wind over billions of years.

**Over the poles.** **Ulysses**, from the European Space Agency and NASA, was launched in 1990. It flew past Jupiter,
whose gravity threw it out of the plane of the planets, onto an orbit that took it over the Sun's north and south
poles. It made three sweeps from pole to pole, in 1994–95, 2000–01 and 2007–08, and worked until 30 June 2009.

**The Voyagers, still going.** Both Voyagers are now outside the bubble, and their power is running down.

- **Voyager 1** was 172.5 AU from the Sun in October 2026 (book 3,
  [section 7.5](../orbits/07-Speed-Energy-and-Escape.md#bound)). As of 2026 only two of its instruments still work,
  one for plasma waves and a magnetometer. It is expected to be one **light-day** from the Earth on 18 November 2026,
  so a message to it takes a whole day to arrive. Its power may last for engineering data until about 2036.
- **Voyager 2** was 143 AU from the Earth in February 2026. Its plasma instrument was switched off on 26 September
  2024 to save power, and NASA planned to switch off another, for low-energy charged particles, in March 2025.

**Mapping the edge from home.** **IBEX**, a small NASA satellite launched on 19 October 2008 from a rocket dropped by an
aircraft over Kwajalein Atoll in the Pacific, maps the edge of the bubble from Earth orbit. It catches **neutral
atoms** made out at the boundary, which fly in straight lines, unbent by magnetic fields. Its first maps showed an
unexpected narrow **ribbon** across the sky, two to three times brighter than anything else.

**Touching the Sun.** **Parker Solar Probe** was launched on 12 August 2018. On 24 December 2024 it passed **6.16
million km** from the Sun's surface at **191 km/s**, the fastest object ever built (section 18.8).

**At L1.** The point L1, 1.5 million km towards the Sun, is a good place to watch the wind before it reaches us (book 3,
[section 9.3](../orbits/09-Lagrange-Points-and-Trojans.md#parking)).

- India's **Aditya-L1**, its first mission to study the Sun, was launched on 2 September 2023 and reached its orbit
  round L1 on 6 January 2024. Its ASPEX instrument measures the solar wind.
- NASA's **IMAP** was launched on 24 September 2025, with NOAA's SWFO-L1 and NASA's Carruthers Geocorona Observatory on
  the same rocket. From an orbit round L1 it maps the edge of the bubble, studies the IBEX ribbon, and sends live data
  for forecasting space weather.

??? note "Sources"
    - Apollo's aluminium collectors and solar wind nuclei in the lunar soil: Wikipedia, Solar wind (above). "Over
      billions of years": standard.
    - Ulysses, ESA and NASA, launched in 1990, the Jupiter flyby out of the plane, the passes over both poles, the
      three fast latitude scans and the last day of 30 June 2009: Wikipedia,
      [Ulysses (spacecraft)](https://en.wikipedia.org/wiki/Ulysses_(spacecraft)) (weaker).
    - Voyager 1: book 3, chapter 7, and Wikipedia, Voyager 1 (above): two instruments working as of 2026, one
      light-day projected for 18 November 2026, engineering data possibly until 2036. Voyager 2: 143.05 AU from the
      Earth in February 2026, the plasma science instrument off on 26 September 2024, and the LECP shutdown planned for
      24 March 2025: Wikipedia, Voyager 2 (above).
    - IBEX, NASA's Small Explorer, launched on 19 October 2008 on a Pegasus XL dropped from the Stargazer aircraft
      from Kwajalein Atoll, its energetic neutral atom imagers, and the ribbon: Wikipedia,
      [Interstellar Boundary Explorer](https://en.wikipedia.org/wiki/Interstellar_Boundary_Explorer) (weaker), and
      Heliosphere (above). Neutral atoms unbent by magnetic fields: standard.
    - Parker Solar Probe's launch, its closest pass on 24 December 2024 at 6.16 million km from the surface and its
      191 km/s: Wikipedia, Parker Solar Probe (above).
    - Aditya-L1 as the first Indian mission to observe the Sun, launched on 2 September 2023, at L1 on 6 January 2024,
      about 1.5 million km away, and ASPEX: Wikipedia, [Aditya-L1](https://en.wikipedia.org/wiki/Aditya-L1)
      (weaker).
    - IMAP launched on 24 September 2025 with SWFO-L1 and Carruthers, its orbit round L1, the ribbon and real-time
      data: Wikipedia,
      [Interstellar Mapping and Acceleration Probe](https://en.wikipedia.org/wiki/Interstellar_Mapping_and_Acceleration_Probe)
      (weaker).

## 18.7 The wind at Mars { #mars }

| | Mars | Earth |
| --- | --- | --- |
| Distance from the Sun | 1.52 AU | 1 AU |
| Sunlight | 586 W/m² | 1,361 W/m² |
| Particles in the wind, typical | about 2 per cm³ | about 5 per cm³ |
| Push of the wind | 0.43 of the Earth's | 1 to 6 nPa |
| Angle of the Sun's field | 58° | 47° |
| Wind's trip at 400 km/s | 6.6 days | 4.3 days |
| Magnetic field round the planet | none, only patches in the crust | yes |

**No shield.** The Earth's magnetic field holds the wind off more than 10 Earth radii out (chapter 6,
[section 6.4](06-The-Earth-as-a-Planet.md#magnetic)). Mars has no such field, so the wind runs straight into its upper
air. The charged gas up there pushes back, and the wind's own field drapes round the planet, so Mars, like Venus and
like a comet, has a weaker **induced** magnetic bubble made by the wind itself.

**Auroras everywhere.** With no global field to steer the particles to the poles, Mars's auroras turn up in odd places.
The first, on 14 August 2004, glowed over a patch of magnetised crust. In 2014 the MAVEN orbiter found auroras spread
over the whole planet, even near the equator, and on 18 March 2024 Perseverance saw a faint green aurora from the
ground (book 1, [section 21.7](../night-sky/21-The-Night-Sky-from-Mars.md#aurora)).

**A storm at Mars.** In September 2017 a large and unexpected storm from the Sun hit Mars. The radiation at the
surface briefly **doubled**, and the aurora was **25 times brighter** than any seen there before.

**Radiation on the way.** The radiation detector on Curiosity measured the radiation inside the spacecraft on its way
to Mars. For the shortest possible round trip with today's rockets and similar shielding, a crew would get about
**0.66 sievert**, a serious health risk.

**Losing air.** NASA's **MAVEN** reached Mars on 22 September 2014 to measure how fast the wind strips away the upper
air, and found the loss rises sharply during storms from the Sun. Contact with it was lost on 6 December 2025. How much
air Mars has lost, and why, is in chapter 19.

??? note "Sources"
    - Mars's distance and sunlight of 586.2 W/m²: NASA,
      [Mars fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
      The Earth's 1,361 W/m²: standard. 5 per cm³ at the Earth: a typical value inside the 3 to 10 of section 18.1.
    - The 2 per cm³, the 0.43, the 58° and 47°, and the trip times: our arithmetic (section 18.8). The Earth's field
      out past 10 Earth radii: Wikipedia, May 2024 solar storms (above).
    - Mars, like Venus and comets, having an induced magnetosphere: Wikipedia,
      [Comet](https://en.wikipedia.org/wiki/Comet) (weaker). "The charged gas pushes back, the field drapes round":
      standard.
    - Auroras: book 1, chapter 21. MAVEN's widespread auroras in 2014, the September 2017 storm with doubled radiation
      and an aurora 25 times brighter, MAVEN's arrival on 22 September 2014, the greater loss during storms, and lost
      contact on 6 December 2025: Wikipedia, [MAVEN](https://en.wikipedia.org/wiki/MAVEN) (weaker).
    - The 0.66 ± 0.12 sievert: Wikipedia, Radiation assessment detector (above).

## 18.8 Working it out { #working }

**Trip times.** At 400 km/s the wind covers 1 AU in $1.496 \times 10^{11}/(4 \times 10^5) = 3.74 \times 10^5$ s, 4.3
days. The fast wind, at 750 km/s, takes 2.3 days. To Mars, 1.524 AU, the slow wind takes 6.6 days.

**The Carrington cloud.** 150 million km in 17.6 hours is $1.5 \times 10^8/(17.6 \times 3{,}600) = 2{,}370$ km/s.

**The spiral.** A field line leaves the Sun at the wind's speed $v$ while its foot turns at $\Omega = 2\pi/(609.12
\times 3{,}600 \text{ s}) = 2.87 \times 10^{-6}$ per second. At distance $r$ the field has been carried round by
$\Omega r$ for every $v$ it moved out, so its angle $\psi$ to the line from the Sun has $\tan \psi = \Omega r / v$. For
$v = 400$ km/s: at the Earth $\tan\psi = 2.87 \times 10^{-6} \times 1.496 \times 10^{11}/(4 \times 10^5) = 1.07$,
$\psi = 47°$; at Mars $1.63$, $58°$; at Jupiter $5.57$, $80°$; at Neptune $32$, $88°$.

**Thinning out.** The wind keeps the same speed, so the same number of particles crosses every sphere round the Sun,
and the density falls as $1/r^2$. With 5 per cm³ at the Earth: $5/1.524^2 = 2.2$ at Mars, and $5/94^2 = 0.0006$ at the
shock. The Voyagers measured 0.001 to 0.005 between 80 and 120 AU, partly in the squeezed wind beyond the shock.

**Counting particles.** $n v \times 4\pi r^2 = 5 \times 10^6 \times 4 \times 10^5 \times 4\pi \times (1.496 \times
10^{11})^2 = 5.6 \times 10^{35}$ protons a second, and as many electrons: $1.1 \times 10^{36}$ particles, close to the
$1.3 \times 10^{36}$ of section 18.1. Their mass is $5.6 \times 10^{35} \times 1.67 \times 10^{-27} = 9.4 \times 10^8$
kg/s, about a million tonnes a second.

**One light-day.** Light goes $2.998 \times 10^8 \times 86{,}400 = 2.59 \times 10^{13}$ m in a day, 173.1 AU. Voyager
1, at 172.5 AU in October 2026 and moving out 3.6 AU a year, gets there about two months later.

**Fast probe.** 191 km/s is $1.91 \times 10^5/(3.00 \times 10^8) = 0.064\%$ of the speed of light.

??? note "Sources"
    - The speeds, densities, particle count, 17.6 hours and 191 km/s: sections 18.1, 18.4 and 18.6. The Sun's rotation:
      NASA, Sun fact sheet (above). The Voyagers' densities: Wikipedia, Solar wind (above).
    - The proton mass, the speed of light and the AU: standard. The spiral formula: standard, as Parker worked it out.
    - Everything else: our arithmetic.

## 18.9 How far the wind reaches { #derive }

Why does the bubble end about 100 AU out, and not at 10 or 1,000? Because that is where the wind's push has fallen to
the push of the gas and field outside.

**The wind's push.** A stream of particles of mass $m$, $n$ to each cubic metre, moving at speed $v$, pushes on
whatever stops it with a pressure

$$p = m n v^2.$$

At the Earth, with $n = 5 \times 10^6$ per m³ and $v = 4 \times 10^5$ m/s,
$p = 1.67 \times 10^{-27} \times 5 \times 10^6 \times (4 \times 10^5)^2 = 1.34 \times 10^{-9}$ Pa, inside the usual 1
to 6 nPa. Since the density falls as $1/r^2$ and the speed stays the same, at $r$ AU

$$p(r) = \frac{1.34 \times 10^{-9}}{r^2} \text{ Pa}.$$

**The push from outside.** Two things push back.

- The magnetic field between the stars, which Voyager 2 suggested is 0.37 to 0.55 nT. A field $B$ pushes with
  $B^2/(2\mu_0)$: from $(0.37 \times 10^{-9})^2/(2 \times 1.257 \times 10^{-6}) = 0.54 \times 10^{-13}$ Pa to
  $1.20 \times 10^{-13}$ Pa.
- The hot gas: $2 n k T$, counting electrons and protons, with the 0.05 to 0.2 particles per cm³ the Voyagers found
  just outside, taken as electrons with as many protons, and $T = 7{,}000$ K: from $0.10 \times 10^{-13}$ to
  $0.39 \times 10^{-13}$ Pa.

Together, about **0.64 to $1.59 \times 10^{-13}$ Pa**.

**Where they balance.** Setting $1.34 \times 10^{-9}/r^2 = p_{out}$ gives $r = \sqrt{1.34 \times 10^{-9}/p_{out}}$:
from $\sqrt{1.34 \times 10^{-9}/1.59 \times 10^{-13}} = 92$ AU to
$\sqrt{1.34 \times 10^{-9}/0.64 \times 10^{-13}} = 144$ AU. The Voyagers met the shock at 83 and 94 AU and the
heliopause at 119 and 121 AU. A sum on the back of an envelope puts the edge of the Sun's bubble in the right place.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="A graph of pressure, from a hundred-millionth to a hundred-trillionth of a pascal, against distance from the Sun from 1 to 300 astronomical units, both on scales where each step is ten times the last. A falling line shows the push of the solar wind, about 1.3 billionths of a pascal at the Earth and dropping as one over the distance squared, with a shaded band for its usual range of 1 to 6 billionths. A flat band shows the push of the gas and magnetic field between the stars, about 0.07 to 0.16 trillionths of a pascal. The wind line meets the flat band between about 90 and 140 astronomical units. Dashed lines show where the Voyagers met the termination shock, at about 83 and 94, and the heliopause, at 119 and 121.">
  <g font-size="8" fill="currentColor">
    <text x="6" y="12">The wind's push against the push from outside</text>
    <line x1="48.0" y1="176.0" x2="330.0" y2="176.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="45.0" y="179.0" text-anchor="end">10<tspan dy="-3" font-size="6">-14</tspan></text>
    <line x1="48.0" y1="151.7" x2="330.0" y2="151.7" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="45.0" y="154.7" text-anchor="end">10<tspan dy="-3" font-size="6">-13</tspan></text>
    <line x1="48.0" y1="127.3" x2="330.0" y2="127.3" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="45.0" y="130.3" text-anchor="end">10<tspan dy="-3" font-size="6">-12</tspan></text>
    <line x1="48.0" y1="103.0" x2="330.0" y2="103.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="45.0" y="106.0" text-anchor="end">10<tspan dy="-3" font-size="6">-11</tspan></text>
    <line x1="48.0" y1="78.7" x2="330.0" y2="78.7" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="45.0" y="81.7" text-anchor="end">10<tspan dy="-3" font-size="6">-10</tspan></text>
    <line x1="48.0" y1="54.3" x2="330.0" y2="54.3" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="45.0" y="57.3" text-anchor="end">10<tspan dy="-3" font-size="6">-9</tspan></text>
    <line x1="48.0" y1="30.0" x2="330.0" y2="30.0" stroke="#cfc8bf" stroke-width="0.4"/>
    <text x="45.0" y="33.0" text-anchor="end">10<tspan dy="-3" font-size="6">-8</tspan></text>
    <text x="45.0" y="21.0" text-anchor="end">Pa</text>
    <text x="48.0" y="186.0" text-anchor="middle">1</text>
    <text x="161.8" y="186.0" text-anchor="middle">10</text>
    <text x="275.7" y="186.0" text-anchor="middle">100</text>
    <text x="330.0" y="186.0" text-anchor="middle">300</text>
    <text x="189.0" y="196.0" text-anchor="middle">distance from the Sun, AU</text>
    <polygon points="48.0,35.4 330.0,156.0 330.0,174.9 48.0,54.3" fill="#eea66f" opacity="0.2"/>
    <line x1="48.0" y1="51.3" x2="330.0" y2="171.8" stroke="#eea66f" stroke-width="1.6"/>
    <rect x="48.0" y="146.8" width="282.0" height="9.6" fill="#5aa0d8" opacity="0.35"/>
    <text x="54.9" y="142.8" fill="#5aa0d8">push of the gas and field between the stars</text>
    <text x="71.2" y="53.3">push of the solar wind, 1/r²</text>
    <line x1="266.5" y1="30.0" x2="266.5" y2="176.0" stroke="#555" stroke-width="0.6" stroke-dasharray="2 2"/>
    <line x1="272.6" y1="30.0" x2="272.6" y2="176.0" stroke="#555" stroke-width="0.6" stroke-dasharray="2 2"/>
    <line x1="284.3" y1="30.0" x2="284.3" y2="176.0" stroke="#555" stroke-width="0.6" stroke-dasharray="2 2"/>
    <line x1="285.1" y1="30.0" x2="285.1" y2="176.0" stroke="#555" stroke-width="0.6" stroke-dasharray="2 2"/>
    <text x="267.4" y="38.0" text-anchor="end" fill="#555">shock, 83 and 94</text>
    <text x="287.7" y="38.0" fill="#555">heliopause,</text>
    <text x="287.7" y="47.0" fill="#555">119 and 121</text>
    <circle cx="48.0" cy="176.0" r="2.2" fill="#5aa0d8"/>
    <text x="52.0" y="171.0" text-anchor="start">Earth</text>
    <circle cx="129.5" cy="176.0" r="2.2" fill="#5aa0d8"/>
    <text x="129.5" y="171.0" text-anchor="middle">Jupiter</text>
    <circle cx="216.3" cy="176.0" r="2.2" fill="#5aa0d8"/>
    <text x="216.3" y="171.0" text-anchor="middle">Neptune</text>
    <text x="6" y="226">Wind: 5 particles per cm³ at 400 km/s at 1 AU (line); usual range 1 to 6 billionths of a pascal (band).</text>
    <text x="6" y="235">Outside: a field of 0.37 to 0.55 nT plus gas at 7,000 K. Dashed: where Voyager 1 and 2 crossed the</text>
    <text x="6" y="244">termination shock and the heliopause. The two pushes meet near 100 AU (section 18.9).</text>
  </g>
</svg>
</div>

**What we left out.** Strictly, the shock sits where the wind's push matches the pressure of the hot heliosheath,
which in turn matches the outside at the heliopause, so the shock comes a little inside the balance point and the
heliopause a little outside it. We also took the gas just outside to be as hot as the cloud, and left out the push of
the interstellar gas streaming past and of the cosmic rays. So the answer is only rough; what matters is that it lands
near 100 AU, not 10 or 1,000.

**A breathing bubble.** Since $r \propto \sqrt{p}$, if the wind's push doubles, the edge moves out by $\sqrt{2} = 1.41$,
41% further. Gusts of 1 to 6 nPa would put it anywhere from about 100 to 240 AU, but the bubble is too big to follow
each gust: it grows and shrinks slowly, following the wind averaged over months and years.

**Other stars.** Other stars blow bubbles too, called **astrospheres**. A star with a stronger wind, or in thinner gas,
has a bigger one, in proportion to the square root of the ratio of the pushes.

**And Mars.** At Mars the wind's push is $1.34 \times 10^{-9}/1.524^2 = 0.58 \times 10^{-9}$ Pa. With no magnetic
field, it is the pressure of Mars's own upper air that has to stand up to it (chapter 19).

??? note "Sources"
    - Ram pressure $m n v^2$ and the 1 to 6 nPa at 1 AU: Wikipedia, Solar wind (above), which gives the same formula.
      The 0.05 to 0.2 particles per cm³ beyond the heliopause: the same page.
    - The interstellar field of 370 to 550 picoteslas from Voyager 2 in 2009, and 7,000 K: Wikipedia, Local
      Interstellar Cloud (above).
    - Magnetic pressure $B^2/(2\mu_0)$, gas pressure $nkT$, $\mu_0$ and Boltzmann's constant: standard. The word
      astrosphere: Wikipedia, Heliosphere (above).
    - The balance, the 92 to 144 AU, the 41%, the 100 to 240 AU, the bubble following the wind only slowly, the
      corrections, and the Mars push: our arithmetic and reasoning. The shock and heliopause distances: section 18.3.

## Check yourself { #check }

**1.** (beginner) What is the solar wind made of, and where does it come from?

??? note "Answer"
    It is a plasma of charged particles, mostly electrons, protons and alpha particles (helium nuclei), flowing out
    from the Sun's hot outer layer, the corona.

**2.** (beginner) What are the termination shock and the heliopause?

??? note "Answer"
    The termination shock is where the wind suddenly slows below the speed of sound, about 83 to 94 AU out where the
    Voyagers crossed it. The heliopause is the edge of the Sun's bubble, about 120 AU out, where the Sun's plasma gives
    way to the plasma between the stars.

**3.** (beginner) Why does the Sun's magnetic field form a spiral, when the wind blows straight out?

??? note "Answer"
    The field is carried out by the wind, but each field line stays tied to the Sun, which turns once in about 25
    days. So the field lines are wound back, like water from a turning garden sprinkler.

**4.** (intermediate) What happened in the Carrington event of 1859?

??? note "Answer"
    On 1 September 1859 Carrington and Hodgson saw the first recorded solar flare. A cloud of plasma reached the Earth
    in only 17.6 hours and caused the strongest geomagnetic storm on record: telegraphs failed, sparks flew from the
    wires, and auroras were seen as far as Cuba, Hawaii and Colombia.

**5.** (intermediate) Why was Eugene Parker's 1958 paper nearly rejected, and who published it?

??? note "Answer"
    Two reviewers thought the idea of a fast, steady wind from the Sun was wrong; one called it "utter nonsense". The
    editor of the *Astrophysical Journal*, Subrahmanyan Chandrasekhar, could find no mistake in it and published it.
    Luna 1 and Mariner 2 soon showed that the wind is real.

**6.** (intermediate) Why are Mars's auroras so different from the Earth's?

??? note "Answer"
    Mars has no magnetic field round the whole planet to guide particles to the poles. So its auroras appear over
    patches of magnetised crust, or spread over the whole planet, even near the equator.

**7.** (advanced) How long does a fast wind of 750 km/s take to reach Mars, and what is the angle of the Sun's field
there for that wind?

??? note "Answer"
    $1.524 \times 1.496 \times 10^{11}/(7.5 \times 10^5) = 3.04 \times 10^5$ s, about 3.5 days. The angle has
    $\tan\psi = 2.87 \times 10^{-6} \times 2.28 \times 10^{11}/(7.5 \times 10^5) = 0.87$, so $\psi = 41°$: a faster wind
    winds the field less.

**8.** (expert) Suppose the Sun's wind pushed four times harder, with the same push from outside. How far out would
the termination shock be, if it is at 90 AU now?

??? note "Answer"
    The balance distance goes as $\sqrt{p}$, so four times the push gives $\sqrt{4} = 2$ times the distance: about
    180 AU.

## Summary

- The solar wind is a plasma of electrons, protons and helium nuclei from the Sun's corona, blowing at 250 to 750 km/s;
  the Sun loses 1.3 to 1.9 million tonnes a second to it.
- The wind carries the Sun's magnetic field, which the Sun's turning winds into the Parker spiral, 47° at the Earth
  and 58° at Mars, with a wavy current sheet like a ballerina's skirt.
- The wind blows a bubble, the heliosphere. It slows at the termination shock and ends at the heliopause, which
  Voyager 1 crossed at 121 AU in 2012 and Voyager 2 at 119 AU in 2018.
- Coronal mass ejections ride out on the wind; the Carrington event of 1859, a Kyoto storm of 1770 and the storm of May
  2024 lit auroras far from the poles.
- Auroras were seen and recorded in China, Assyria, Japan, Australia and New Zealand long before Birkeland, Biermann,
  Chapman and Parker explained the wind, and Luna 1 first measured it in 1959.
- Parker Solar Probe has flown inside the corona, Aditya-L1 and IMAP watch the wind from L1, and IBEX maps the edge.
- With no magnetic shield, Mars takes the wind into its upper air: auroras all over the planet, radiation on the
  ground, and air lost to space.
- The edge of the bubble is where the wind's push, falling as $1/r^2$, matches the push of the gas and field outside:
  about 100 AU.

**Next:** chapter 19, Air, magnetism and weather on other worlds, where we compare the air, the magnetic shields and
the weather of the planets and moons, and see how Mars lost most of its air.

## Further reading

- Jim Bell, *The Interstellar Age: Inside the Forty-Year Voyager Mission*, Dutton, New York, 2015. A planetary
  scientist tells the story of the two spacecraft and the people who flew them, from the planets
  to the edge of the Sun's bubble.
