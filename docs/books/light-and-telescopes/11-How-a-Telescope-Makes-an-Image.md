# 11. How a telescope makes an image

*A telescope does three things: it collects more light than the eye, it shows finer detail, and it magnifies. This
chapter shows how a lens or mirror makes a small upside-down image of the sky, an idea first written about in China
more than 2,300 years ago, and how an eyepiece magnifies that image. It compares Galileo's telescope with Kepler's,
explains the limits on magnification, what the numbers on a pair of binoculars mean, and what a focal ratio is. It
asks how Mars looks through a telescope and how the Earth looks from Mars. It ends with the lens equation and the
scale of the image at a telescope's focus.*

!!! abstract "In this chapter"
    **You will learn:**

    - the three jobs of a telescope, and which matters most
    - how a lens or mirror makes an image
    - the long history of the pinhole image
    - how an eyepiece magnifies, and how to work out the magnification
    - the difference between Galileo's and Kepler's telescopes
    - the smallest and largest useful magnifications
    - what the numbers on binoculars mean
    - what a focal ratio is
    - how big Mars looks through a telescope, and the Earth from Mars
    - how to use the lens equation and the image scale

    **You need:** chapters 9 and 10. The physics lessons
    [The lens equation](https://physics.akadian.ca/topics/waves/level-7/03-the-lens-equation.html),
    [Telescopes](https://physics.akadian.ca/topics/waves/level-7/04-telescopes.html),
    [Seeing Mars from Earth](https://physics.akadian.ca/topics/waves/level-7/05-seeing-mars-from-earth.html) and
    [Seeing Earth from Mars](https://physics.akadian.ca/topics/waves/level-7/06-seeing-earth-from-mars.html) help.

    **Levels:** 11.1 to 11.3 are beginner; 11.4 to 11.8 are intermediate; 11.9 is advanced; 11.10 is expert.

## 11.1 Three jobs { #jobs }

A telescope has three jobs:

- **Gathering light.** Its main lens or mirror, the **objective**, collects far more light than the pupil of your eye,
  so it shows stars and galaxies too faint to see without it.
- **Showing detail.** A bigger objective can separate finer detail (chapter 12).
- **Magnifying.** It makes things look bigger in angle.

Most people think magnifying is the main job, but astronomers care most about the first two, and both depend on the
width of the objective, the **aperture**. In the dark your pupil opens to somewhere between 3 and 8 mm, depending on
the person. Take 7 mm. A telescope 100 mm across collects $(100/7)^2 \approx 200$ times as much light.

??? note "Sources"
    - The light-gathering power related to the area of the objective, and larger objectives resolving finer detail:
      Wikipedia, [Optical telescope](https://en.wikipedia.org/wiki/Optical_telescope) (weaker).
    - The pupil in the dark, 3 to 8 mm, with large variation between people: Wikipedia,
      [Pupil](https://en.wikipedia.org/wiki/Pupil) (weaker).
    - The arithmetic is ours.

## 11.2 Making an image { #image }

Light from every point of an object spreads out in all directions. A converging lens catches some of the light from
each point and brings it back together at a single point on the other side. Do that for every point and you get an
**image**: a picture of the object made of light, which you could catch on a sheet of paper.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="A converging lens making an image. On the left an upright arrow stands on the axis. Three rays from its tip pass through the lens: one parallel to the axis, which is bent through the focus on the far side; one through the centre of the lens, which goes straight on; and one through the near focus, which comes out parallel to the axis. All three meet again on the right, below the axis, at the tip of an upside-down image of the arrow. A telescope lens or mirror does the same with the distant sky, making a small upside-down image at its focus.">
  <g font-size="8" fill="currentColor">
    <line x1="10" y1="140" x2="330" y2="140" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <path d="M170,60 Q188,140 170,220 Q152,140 170,60 Z" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
    <line x1="40" y1="140" x2="40" y2="76" stroke="#c1440e" stroke-width="2.2"/>
    <path d="M35,78 L40,70 L45,78" fill="#c1440e"/>
    <line x1="281.4" y1="140" x2="281.4" y2="194.0" stroke="#c1440e" stroke-width="2.2"/>
    <path d="M276.4,192.0 L281.4,200.0 L286.4,192.0" fill="#c1440e"/>
    <polyline points="40,70 170,70 281.4,200.0" fill="none" stroke="#eea66f" stroke-width="1"/>
    <line x1="40" y1="70" x2="281.4" y2="200.0" stroke="#eea66f" stroke-width="1"/>
    <polyline points="40,70 170,200.0 281.4,200.0" fill="none" stroke="#eea66f" stroke-width="1"/>
    <circle cx="110" cy="140" r="1.8" fill="currentColor"/>
    <text x="110" y="135" text-anchor="middle">F</text>
    <circle cx="230" cy="140" r="1.8" fill="currentColor"/>
    <text x="230" y="135" text-anchor="middle">F</text>
    <text x="40" y="154" text-anchor="middle">object</text>
    <text x="170" y="54" text-anchor="middle">lens</text>
    <text x="289.4" y="170.0">image:</text>
    <text x="289.4" y="180.0">upside down</text>
    <text x="6" y="12">A lens makes an upside-down image</text>
  </g>
</svg>
</div>

*Figure A. Three rays from the tip of the arrow meet again below the axis. The image is upside down.*

The rays cross over as they pass through the lens, so the image is **upside down** and reversed left to right. A
concave mirror makes an image in the same way (chapter 9). For something very far away, like a star or the Moon, the
image forms at the focus, one focal length from the lens or mirror. The longer the focal length, the bigger the image.

**The pinhole.** Even a tiny hole in the wall of a dark room makes an upside-down image of the scene outside on the
opposite wall. This is the **camera obscura**, Latin for "dark room".

- **China, 4th century BCE.** One of the earliest written records of a pinhole image is in the *Mozi*, a book of the
  Mohist school, named after the philosopher Mozi.
- **Greece.** Aristotle, or one of his followers, also described it.
- **Cairo, 11th century.** Ibn al-Haytham studied the camera obscura in great detail.
- **China, 1088.** In his *Dream Pool Essays*, Shen Kuo compared the pinhole with the focus of a concave burning
  mirror, and explained why the image is upside down.
- **Eclipses.** Astronomers used the camera obscura to watch eclipses of the Sun without harming their eyes. The
  oldest known printed drawing of one, by the Dutch physician Gemma Frisius in 1545, shows it used to study an
  eclipse.

??? note "Sources"
    - The *Mozi* in the 4th century BCE, Aristotle, Ibn al-Haytham in the early 11th century, Shen Kuo's *Dream Pool
      Essays* of 1088, eclipses watched safely, and Gemma Frisius's drawing of 1545: Wikipedia,
      [Camera obscura](https://en.wikipedia.org/wiki/Camera_obscura) (weaker).
    - The figure is ours, worked out with the lens equation (section 11.10).

## 11.3 The eyepiece { #eyepiece }

The objective makes a small image at its focus. To look at it, you use a second, small lens with a short focal
length, the **eyepiece**, as a magnifying glass. In a simple telescope the two lenses share a focus.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="How a telescope with two lenses works. On the left, a large objective lens with a long focal length receives parallel rays from a distant star, arriving at a small angle to the axis. It brings them to a point in its focal plane, making a small image. The eyepiece, a small lens with a short focal length, sits one of its own focal lengths beyond that image, so the rays leave it parallel again but at a much larger angle. The angle going out divided by the angle coming in is the magnification, equal to the objective's focal length divided by the eyepiece's, here 200 divided by 50, or 4.">
  <g font-size="8" fill="currentColor">
    <line x1="5" y1="125" x2="335" y2="125" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"/>
    <path d="M40,75 Q52,125 40,175 Q28,125 40,75 Z" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
    <path d="M290,85 Q300,125 290,165 Q280,125 290,85 Z" fill="#5aa0d8" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
    <line x1="240" y1="80" x2="240" y2="170" stroke="#555" stroke-width="0.6" stroke-dasharray="1 2"/>
    <polyline points="5,86.3 40,90 240,146.0 290,160.0 335.0,141.1" fill="none" stroke="#eea66f" stroke-width="1"/>
    <polyline points="5,121.3 40,125 240,146.0 290,151.3 335.0,132.4" fill="none" stroke="#eea66f" stroke-width="1"/>
    <polyline points="5,156.3 40,160 240,146.0 290,142.5 335.0,123.6" fill="none" stroke="#eea66f" stroke-width="1"/>
    <circle cx="240" cy="146.0" r="2" fill="#c1440e"/>
    <text x="40" y="189" text-anchor="middle">objective</text>
    <text x="40" y="199" text-anchor="middle">focal length 200</text>
    <text x="290" y="179" text-anchor="middle">eyepiece</text>
    <text x="290" y="189" text-anchor="middle">focal length 50</text>
    <text x="240" y="183" text-anchor="middle">image</text>
    <text x="240" y="193" text-anchor="middle">(shared focus)</text>
    <text x="8" y="66">small angle in</text>
    <text x="332" y="73" text-anchor="end">big angle out</text>
    <text x="6" y="12">Objective and eyepiece: magnification = 200 / 50 = 4</text>
    <text x="6" y="240">angles drawn larger than in a real telescope</text>
  </g>
</svg>
</div>

*Figure B. The objective makes an image; the eyepiece turns small angles into big ones.*

Rays from a star come in at a small angle and leave the eyepiece at a bigger angle. The ratio of the two angles is the
**magnification**:

$$M = \frac{f_o}{f_e},$$

the focal length of the objective divided by the focal length of the eyepiece. A telescope with a 1,200 mm focal
length and a 3 mm eyepiece magnifies $1{,}200/3 = 400$ times. Change the eyepiece and you change the magnification,
which is why it is not written on the telescope.

A good eyepiece is itself made of several lenses, to give sharp images over a wide view. The **Huygens** eyepiece has
two lenses with an air gap; in 1849 Carl Kellner designed the first modern achromatic eyepiece.

??? note "Sources"
    - The magnification $M = f/f_e$ and the example of 1,200 mm and 3 mm giving 400: Wikipedia,
      [Optical telescope](https://en.wikipedia.org/wiki/Optical_telescope) (weaker).
    - Interchangeable eyepieces and magnification not written on the telescope: Wikipedia,
      [Exit pupil](https://en.wikipedia.org/wiki/Exit_pupil) (weaker).
    - The Huygens eyepiece and Kellner's design of 1849: Wikipedia, [Eyepiece](https://en.wikipedia.org/wiki/Eyepiece)
      (weaker).

## 11.4 Galileo's telescope and Kepler's { #kepler }

- **Galileo, 1609.** Galileo's telescopes had a converging objective and a **diverging** eyepiece. The image is the
  right way up, but the view is narrow. His first magnified about three times; by August 1609 he showed the lawmakers
  of Venice one of eight or nine times, and later he made them up to about 30 times (history book,
  [chapter 15, section 15.2](../history/15-Galileo-and-the-Telescope.md#galileo)).
- **Kepler, 1611.** Johannes Kepler described a telescope with two **converging** lenses, as in figure B. It can
  magnify more than Galileo's design, though the image is upside down. Because there is a real image inside the tube,
  a fine scale or crosshairs placed there are seen sharply against the sky, so the angle between stars can be
  measured.

Astronomers do not mind an upside-down Moon, and Kepler's design became the basis of the modern refracting telescope.

??? note "Sources"
    - Galileo's telescopes of about 3, 8 or 9, and up to about 30 times: this site's history book, chapter 15,
      section 15.2.
    - Kepler's telescope of two convex lenses with higher magnification than Galileo's, the foundation of the modern
      refractor: Wikipedia, [Johannes Kepler](https://en.wikipedia.org/wiki/Johannes_Kepler) (weaker).
    - Kepler's telescope of 1611, the inverted image and the micrometer at the focal plane: Wikipedia,
      [Refracting telescope](https://en.wikipedia.org/wiki/Refracting_telescope) (weaker).

## 11.5 How much magnification? { #limits }

**Not too little.** The light leaves the eyepiece as a narrow beam called the **exit pupil**. Its width is the
aperture divided by the magnification. If it is wider than the pupil of your eye, some of the light is wasted. So
the lowest useful magnification is about the aperture divided by your pupil: for a 100 mm telescope and a 7 mm pupil,
about 14 times.

**Not too much.** Magnifying more does not show more detail. That is set by the aperture and by the steadiness of the
air (chapter 12). Beyond a point the picture just gets bigger, dimmer and blurrier.

**The view.** Each eyepiece shows a circle of a certain apparent size, its **apparent field of view**. The patch of sky
you actually see is smaller by the magnification. An eyepiece with a 50° apparent field, at 100 times, shows
$50°/100 = 0.5°$ of sky, about the width of the full Moon.

Rules of thumb: large faint things such as the Andromeda Galaxy look best at low magnification; planets at the highest
magnification the night's air allows.

??? note "Sources"
    - The minimum useful magnification set by the exit pupil and the observer's pupil, resolution not given by maximum
      magnification, and the rules of thumb for galaxies, planets and large objects: Wikipedia,
      [Optical telescope](https://en.wikipedia.org/wiki/Optical_telescope) (weaker).
    - The apparent field of view: Wikipedia, [Eyepiece](https://en.wikipedia.org/wiki/Eyepiece) (weaker).
    - The arithmetic is ours.

## 11.6 Binoculars { #binoculars }

Binoculars are two small telescopes side by side, one for each eye. They are described by two numbers, such as
**7×50**: the magnification (7) and the width of each objective in millimetres (50). So the exit pupil of a 7×50 pair
is $50/7 \approx 7$ mm, about the size of a dark-adapted pupil, which makes them good for the night sky.

A Kepler-style telescope gives an upside-down image, which would be hopeless for watching birds. Binoculars turn the
image the right way up with **prisms**, blocks of glass in which light bounces off the inner faces by total internal
reflection (chapter 10). The prisms also fold the light path, so the binoculars can be short. The Italian inventor
**Ignazio Porro** patented this arrangement in 1854. Ernst Abbe (chapter 10) and the glass maker Otto Schott later
improved it.

??? note "Sources"
    - The 7×50 description, the first number as magnification, prisms to show the image the right way up and shorten
      the instrument, Porro's patent of 1854, and Abbe and Schott: Wikipedia,
      [Binoculars](https://en.wikipedia.org/wiki/Binoculars) (weaker).
    - Total internal reflection twice inside a Porro prism, erecting the image: Wikipedia,
      [Porro prism](https://en.wikipedia.org/wiki/Porro_prism) (weaker).

## 11.7 Focal ratio { #focal }

The **focal ratio**, or **f-number**, is the focal length divided by the aperture. A telescope with a 1,000 mm focal
length and a 200 mm aperture is f/5.

The brightness of the image of a spread-out object, such as a nebula or the Moon, falls with the square of the
f-number. A low f-number ("fast") gives a bright, small image and a wide view; a high f-number ("slow") gives a large,
dim image. Photographers use the same numbers on camera lenses (chapter 14).

| Telescope | Focal ratio |
| --- | --- |
| Hale Telescope, 1948 (chapter 9) | f/3.3 |
| Newton's first telescope, 1668 (chapter 9) | f/5 |
| Hevelius's long telescope (chapter 10) | f/225 |

??? note "Sources"
    - The f-number as focal length over aperture, and image brightness falling with its square: Wikipedia,
      [F-number](https://en.wikipedia.org/wiki/F-number) (weaker).
    - The focal ratios: chapters 9 and 10.

## 11.8 Mars through a telescope, and the Earth from Mars { #mars }

**Mars from Earth.** Mars is 6,779 km wide. Even at its closest, about 54.6 million km away, it covers only about
25 seconds of arc, some 70 times smaller than the Moon looks. To the eye it is a bright dot. Through a telescope
magnifying about 75 times it looks as big as the full Moon does without one. But magnifying cannot add detail that
the air and the aperture do not allow (chapter 12). Straining to see markings at the very limit is how the "canals"
fooled so many observers; in 1909 Eugène Antoniadi, with a much bigger lens, saw none (history book,
[chapter 17, section 17.8](../history/17-Herschel-and-the-Canals-of-Mars.md#illusion)).

**The Earth from Mars.** From Mars, the Earth is an inner planet, like Venus for us: a bright "evening star" or
"morning star", never far from the Sun.

- On 8 May 2003, NASA's Mars Global Surveyor photographed the Earth and the Moon from 0.93 astronomical units away.
  They shone at magnitudes −2.5 and +0.9.
- To the eye they would look like stars. Through a telescope they would show as crescents, with some detail.
- On 3 October 2007, the HiRISE telescope on the Mars Reconnaissance Orbiter (chapter 9) photographed them from
  142 million km. The Earth came out 90 pixels across and the Moon 24.

From Mars's surface, its own moon Phobos looks about a third as wide as our Moon does from Earth.

??? note "Sources"
    - Mars's size and distances: NASA, [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html)
      (mean radius 3,389.5 km, minimum distance 54.6 million km, largest apparent diameter 25.6″); the physics lesson
      [Seeing Mars from Earth](https://physics.akadian.ca/topics/waves/level-7/05-seeing-mars-from-earth.html).
    - Earth as an evening or morning star from Mars, Mars Global Surveyor's picture of 8 May 2003 at 0.930 AU,
      magnitudes −2.5 and +0.9, crescents in a telescope, and Phobos about a third of the Moon's width: Wikipedia,
      [Astronomy on Mars](https://en.wikipedia.org/wiki/Astronomy_on_Mars) (weaker).
    - HiRISE's picture of 3 October 2007, 90 and 24 pixels at 142 million km: Wikipedia,
      [HiRISE](https://en.wikipedia.org/wiki/HiRISE) (weaker).

## 11.9 Working it out { #working }

**Magnification.** A 1,000 mm objective with a 25 mm eyepiece: $M = 1{,}000/25 = 40$. With a 10 mm eyepiece,
$M = 100$.

**Light and faint stars.** A telescope of aperture $D$ collects $(D/7\text{ mm})^2$ times as much light as a 7 mm
pupil. Since five magnitudes is a factor of 100 (book 1,
[chapter 4, section 4.5](../night-sky/04-How-Bright-Is-a-Star.md#pogson)), it shows stars fainter by
$5 \log_{10}(D/7\text{ mm})$ magnitudes.

| Aperture | Light compared with the eye | Fainter by | Lowest useful magnification |
| --- | --- | --- | --- |
| 50 mm binoculars | 51 | 4.3 magnitudes | 7 |
| 100 mm | 204 | 5.8 | 14 |
| 200 mm | 816 | 7.3 | 29 |
| Hale, 5.1 m | 530,000 | 14.3 | 730 |
| Keck, 10 m | 2,000,000 | 15.8 | 1,430 |

So an eye that can see magnitude 6 unaided could reach about magnitude 13 with a 200 mm telescope, in theory. In
practice the sky's glow and the air take some of that away.

| Seen from the other planet at closest approach | Mars, seen from Earth | Earth, seen from Mars |
| --- | --- | --- |
| Width | 6,779 km | 12,756 km |
| Distance | 54.6 million km | 54.6 million km |
| Angular size | 25.6″ | 48″ |
| Magnification to look as big as the Moon does to the eye (1,865″) | 73 | 39 |

At that moment, though, the Earth lies between Mars and the Sun, so its dark side faces Mars and it is lost in the
Sun's glare. Mars-based astronomers would do better to look when the Earth is farther away but well to one side of the
Sun.

??? note "Sources"
    - Widths and distances: NASA, [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html) and
      [Earth Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html) (equatorial radius
      6,378.1 km).
    - The Moon's 1,865″: the physics lesson
      [Seeing Mars from Earth](https://physics.akadian.ca/topics/waves/level-7/05-seeing-mars-from-earth.html).
    - Diameters of Hale and Keck: chapter 9.
    - The arithmetic is ours.

## 11.10 The lens equation and the image scale { #lensequation }

**The lens equation.** For a thin lens of focal length $f$, an object at distance $u$ in front makes an image at
distance $v$ behind, where

$$\frac{1}{u} + \frac{1}{v} = \frac{1}{f},$$

and the image is $v/u$ times the size of the object, upside down. In figure A the lens has $f = 60$ and the object is
at $u = 130$, so $1/v = 1/60 - 1/130$, $v = 111$: the image is 111 units behind the lens and $111/130 = 0.86$ times as
tall. For an object very far away, $1/u \to 0$ and $v = f$: the image is at the focus.

**Why $M = f_o/f_e$.** A star at a small angle $\alpha$ to the axis makes an image a height $h = f_o \alpha$ from the
axis in the focal plane. The eyepiece, one focal length beyond, sends that light out at an angle $\beta = h/f_e$. So

$$M = \frac{\beta}{\alpha} = \frac{f_o}{f_e}.$$

**The exit pupil.** The eyepiece makes an image of the objective itself. The objective is $f_o + f_e$ away from the
eyepiece, so its image is at $v = f_e(f_o + f_e)/f_o$ and its width is $D f_e / f_o = D/M$. That small bright circle
is the exit pupil, where you put your eye.

**The image scale.** At the focus, an angle $\theta$ in radians becomes a distance $f\theta$. So one millimetre in the
focal plane covers $206{,}265 / f$ seconds of arc, with $f$ in millimetres.

- A 1,000 mm focal length gives 206″ per mm. The Moon, about 0.52° across, makes an image 9.1 mm wide.
- The Hale Telescope, 5.1 m at f/3.3, has $f = 16{,}830$ mm: 12.3″ per mm. Its image of the Moon is 152 mm wide.

??? note "Sources"
    - The lens equation and the angular magnification are standard results; see the physics lessons
      [The lens equation](https://physics.akadian.ca/topics/waves/level-7/03-the-lens-equation.html) and
      [Telescopes](https://physics.akadian.ca/topics/waves/level-7/04-telescopes.html).
    - The Hale Telescope's 5.1 m and f/3.3: Wikipedia, [Hale Telescope](https://en.wikipedia.org/wiki/Hale_Telescope)
      (weaker).
    - The arithmetic is ours.

## Check yourself { #check }

**1.** (beginner) What are the three jobs of a telescope, and which do astronomers care about most?

??? note "Answer"
    Gathering light, showing detail and magnifying. The first two matter most, and both depend on the aperture.

**2.** (beginner) A telescope has an objective of focal length 1,000 mm and an eyepiece of 25 mm. What is its
magnification?

??? note "Answer"
    $1{,}000 / 25 = 40$ times.

**3.** (beginner) Why is the image made by a lens upside down?

??? note "Answer"
    The rays from each point cross over as they pass through the lens, so light from the top of the object ends up at
    the bottom of the image.

**4.** (intermediate) How did Galileo's telescope differ from Kepler's?

??? note "Answer"
    Galileo used a diverging eyepiece, giving an upright image and a narrow view. Kepler used a converging eyepiece,
    giving an upside-down image but higher magnification and a real image where a scale can be placed.

**5.** (intermediate) What do the numbers on 10×50 binoculars mean, and what is their exit pupil?

??? note "Answer"
    They magnify 10 times and each objective is 50 mm wide. The exit pupil is $50/10 = 5$ mm.

**6.** (intermediate) Where is one of the earliest written records of a pinhole image?

??? note "Answer"
    In the *Mozi*, a Chinese book of the 4th century BCE.

**7.** (advanced) For a 200 mm telescope and a 7 mm pupil, what is the lowest useful magnification, and how many
magnitudes fainter can it show than the eye?

??? note "Answer"
    $200/7 \approx 29$ times; $5 \log_{10}(200/7) = 5 \times 1.456 = 7.3$ magnitudes.

**8.** (expert) At the focus of the Hale Telescope (12.3″ per mm), how wide is the image of Mars at its closest
(25.6″)? And of Jupiter at its largest (50.1″)?

??? note "Answer"
    $25.6 / 12.3 = 2.1$ mm for Mars, and $50.1 / 12.3 = 4.1$ mm for Jupiter (NASA's Jupiter fact sheet).

## Summary

- A telescope gathers light, shows detail and magnifies; aperture matters most.
- A lens or concave mirror makes an upside-down image; for distant objects it forms at the focus.
- The pinhole image was described in China in the 4th century BCE, then by Aristotle, Ibn al-Haytham and Shen Kuo.
- An eyepiece magnifies the image: $M = f_o / f_e$.
- Galileo's telescope gives an upright image; Kepler's gives an upside-down image, more magnification and a place for
  a measuring scale.
- The exit pupil, $D/M$, sets the lowest useful magnification; the air and aperture set the highest.
- Binoculars such as 7×50 use prisms to turn the image the right way up.
- The focal ratio is focal length over aperture; low f-numbers give bright, wide views.
- Mars at its closest is 25″ across; the Earth from Mars is a bright evening or morning star.
- $1/u + 1/v = 1/f$; at the focus, one millimetre covers $206{,}265/f$ seconds of arc.

**Next:**
[chapter 12, The limits: diffraction, resolution and seeing](12-The-Limits-Diffraction-Resolution-and-Seeing.md),
where we find what stops a telescope from seeing ever finer detail.

## Further reading

- Fred Watson, *Stargazer: The Life and Times of the Telescope*, Allen & Unwin, 2004.
