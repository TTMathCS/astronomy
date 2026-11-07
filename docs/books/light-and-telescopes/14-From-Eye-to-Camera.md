# 14. From eye to camera

*For 230 years after Galileo, everything seen through a telescope had to be seen by a human eye and drawn by hand.
Then came photography. A photographic plate could keep collecting light for an hour, and so it showed stars and
nebulae no eye had ever seen. This chapter follows the change: the first pictures of the Moon and a star, the great
international plan to photograph the whole sky on glass, the electronic chip that replaced film, how a camera sees
colour, and today's giant sky cameras. It ends with the first close-up pictures of Mars, coloured by hand with
pastels, and with why counting photons always leaves a little uncertainty.*

!!! abstract "In this chapter"
    **You will learn:**

    - what the eye can and cannot do as a light detector
    - who took the first photographs of the Moon, a star, a spectrum and a nebula
    - why long exposures revealed so much
    - how twenty observatories around the world photographed the sky on glass
    - how a CCD works, who invented it, and why it beat film
    - how digital cameras see colour
    - what the largest camera ever built does
    - how the first close-up pictures of Mars were taken and sent home
    - why stacking many pictures makes a cleaner one

    **You need:** chapters 4 and 11, and book 1, [chapter 1](../night-sky/01-Your-First-Clear-Night.md#adapt). The
    physics lessons
    [Photons and energy levels](https://physics.akadian.ca/topics/waves/level-8/01-photons-and-energy-levels.html) and
    [Colour cameras on Mars](https://physics.akadian.ca/topics/waves/level-6/06-colour-cameras-on-mars.html) help.

    **Levels:** 14.1 to 14.3 are beginner; 14.4 to 14.8 are intermediate; 14.9 is advanced; 14.10 is expert.

## 14.1 The eye as a detector { #eye }

The eye is a remarkable detector. After 20 to 30 minutes in the dark it becomes 10,000 to a million times more
sensitive than in daylight. Most of its light-sensing cells are **rods**, about 91 million of them against about 4.5
million colour-sensing **cones** (book 1,
[chapter 1, sections 1.3 and 1.4](../night-sky/01-Your-First-Clear-Night.md#adapt)).

But it has two big limits for astronomy:

- **It cannot save what it sees.** For centuries the only record of a view through a telescope was a drawing. What one
  observer drew, another could doubt. The "canals" of Mars lived on drawings (history book,
  [chapter 17, section 17.8](../history/17-Herschel-and-the-Canals-of-Mars.md#illusion)).
- **It cannot keep adding up light.** Staring longer at a faint galaxy does not make it look brighter. Film and
  electronic cameras can go on collecting light for as long as the shutter stays open.

??? note "Sources"
    - Dark adaptation in 20 to 30 minutes, 10,000 to 1,000,000 times more sensitive, and about 91 million rods to
      4.5 million cones: Wikipedia, [Dark adaptation](https://en.wikipedia.org/wiki/Dark_adaptation) (weaker).
    - Film and digital cameras accumulating photons over long periods: Wikipedia,
      [Astrophotography](https://en.wikipedia.org/wiki/Astrophotography) (weaker).

## 14.2 The first pictures { #first }

The daguerreotype, the first popular kind of photograph, was introduced in 1839, and the Moon was photographed the
same year, though not well.

| Year | First photograph of | Who, and how |
| --- | --- | --- |
| 1840 | the Moon, successfully | **John William Draper** of New York University (chapter 6), on 23 March: a 20-minute daguerreotype through a 13 cm reflector |
| 1850 | a star other than the Sun | **William Cranch Bond** and the photographer **John Adams Whipple**, on 16 and 17 July: Vega, with Harvard's 15-inch refractor |
| 1872 | a star's spectrum with absorption lines | **Henry Draper**, John's son: Vega again (chapter 7) |
| 1880 | a nebula | Henry Draper: the Orion Nebula, a 51-minute exposure on the new "dry plate" |

Late in the 19th century, glass **dry plates** coated with gelatin replaced the older wet plates, and photography
became a serious research tool. In 1883 the amateur astronomer **Andrew Ainslie Common**, using a 91 cm reflector he
had built in the back garden of his home in Ealing, England, photographed the same nebula several times in exposures
of up to an hour.

??? note "Sources"
    - The first photograph of the Moon attempted in 1839, Draper's 20-minute daguerreotype of 23 March 1840 with a
      13 cm reflector, Bond and Whipple's Vega of 16 and 17 July 1850 with Harvard's 15-inch refractor, Henry Draper's
      spectrum of Vega in 1872 and Orion Nebula of 1880 (51 minutes, dry plate), and Common's exposures of up to
      60 minutes in 1883 with a 36-inch reflector built in his back garden in Ealing: Wikipedia,
      [Astrophotography](https://en.wikipedia.org/wiki/Astrophotography) (weaker).
    - Draper as a New York University professor, and dry plates making photography a serious research tool: the same
      page. The daguerreotype introduced in 1839: Wikipedia,
      [Daguerreotype](https://en.wikipedia.org/wiki/Daguerreotype) (weaker). Gelatin dry plates replacing wet plates
      late in the 19th century: Wikipedia, [Photographic plate](https://en.wikipedia.org/wiki/Photographic_plate)
      (weaker).

## 14.3 Adding up light { #exposure }

A photograph adds up light. Double the exposure and the plate collects twice as many photons. With exposures of an hour
or more, photography recorded hundreds of thousands of new stars, and nebulae invisible to the human eye. Telescopes
became, in effect, giant cameras.

But film wastes most of the light.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="Three grids of 100 small circles, each circle standing for one photon of light arriving. Left, photographic film: only 2 of the 100 circles are filled in, because film records only about 2 percent of the light. Middle, a typical astronomical CCD: 70 of the 100 are filled. Right, the best CCDs at some wavelengths: more than 90 are filled. A CCD can therefore collect in one minute what film would need more than half an hour to collect.">
  <g font-size="8" fill="currentColor">
    <circle cx="18" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="27" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="36" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="45" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="54" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="63" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="72" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="81" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="90" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="99" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="18" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="27" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="36" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="45" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="54" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="63" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="72" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="81" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="90" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="99" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="18" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="27" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="36" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="45" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="54" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="63" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="72" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="81" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="90" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="99" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="18" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="27" cy="77" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="36" cy="77" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="45" cy="77" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="54" cy="77" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="63" cy="77" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="72" cy="77" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="81" cy="77" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="90" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="99" cy="77" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="18" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="27" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="36" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="45" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="54" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="63" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="72" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="81" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="90" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="99" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="18" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="27" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="36" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="45" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="54" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="63" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="72" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="81" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="90" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="99" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="18" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="27" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="36" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="45" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="54" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="63" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="72" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="81" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="90" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="99" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="18" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="27" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="36" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="45" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="54" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="63" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="72" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="81" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="90" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="99" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="18" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="27" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="36" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="45" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="54" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="63" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="72" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="81" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="90" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="99" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="18" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="27" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="36" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="45" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="54" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="63" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="72" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="81" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="90" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="99" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <text x="58" y="152" text-anchor="middle">photographic film</text>
    <text x="58" y="164" text-anchor="middle">about 2 in 100</text>
    <circle cx="126" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="135" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="144" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="153" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="162" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="171" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="180" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="189" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="198" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="207" cy="50" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="126" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="135" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="144" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="153" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="162" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="171" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="180" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="189" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="198" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="207" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="126" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="135" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="144" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="153" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="162" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="171" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="180" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="189" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="198" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="207" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="126" cy="77" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="135" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="144" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="153" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="162" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="171" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="180" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="189" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="198" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="207" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="126" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="135" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="144" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="153" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="162" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="171" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="180" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="189" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="198" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="207" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="126" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="135" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="144" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="153" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="162" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="171" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="180" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="189" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="198" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="207" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="126" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="135" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="144" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="153" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="162" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="171" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="180" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="189" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="198" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="207" cy="104" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="126" cy="113" r="3.3" fill="#c1440e"/>
    <circle cx="135" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="144" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="153" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="162" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="171" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="180" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="189" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="198" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="207" cy="113" r="3.3" fill="#c1440e"/>
    <circle cx="126" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="135" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="144" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="153" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="162" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="171" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="180" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="189" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="198" cy="122" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="207" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="126" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="135" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="144" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="153" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="162" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="171" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="180" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="189" cy="131" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="198" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="207" cy="131" r="3.3" fill="#c1440e"/>
    <text x="166" y="152" text-anchor="middle">a typical CCD</text>
    <text x="166" y="164" text-anchor="middle">about 70 in 100</text>
    <circle cx="234" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="243" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="252" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="261" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="270" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="279" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="288" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="297" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="306" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="315" cy="50" r="3.3" fill="#c1440e"/>
    <circle cx="234" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="243" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="252" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="261" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="270" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="279" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="288" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="297" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="306" cy="59" r="3.3" fill="#c1440e"/>
    <circle cx="315" cy="59" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="234" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="243" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="252" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="261" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="270" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="279" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="288" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="297" cy="68" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="306" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="315" cy="68" r="3.3" fill="#c1440e"/>
    <circle cx="234" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="243" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="252" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="261" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="270" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="279" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="288" cy="77" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="297" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="306" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="315" cy="77" r="3.3" fill="#c1440e"/>
    <circle cx="234" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="243" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="252" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="261" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="270" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="279" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="288" cy="86" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="297" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="306" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="315" cy="86" r="3.3" fill="#c1440e"/>
    <circle cx="234" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="243" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="252" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="261" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="270" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="279" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="288" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="297" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="306" cy="95" r="3.3" fill="#c1440e"/>
    <circle cx="315" cy="95" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="234" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="243" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="252" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="261" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="270" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="279" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="288" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="297" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="306" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="315" cy="104" r="3.3" fill="#c1440e"/>
    <circle cx="234" cy="113" r="3.3" fill="#c1440e"/>
    <circle cx="243" cy="113" r="3.3" fill="#c1440e"/>
    <circle cx="252" cy="113" r="3.3" fill="#c1440e"/>
    <circle cx="261" cy="113" r="3.3" fill="#c1440e"/>
    <circle cx="270" cy="113" r="3.3" fill="#c1440e"/>
    <circle cx="279" cy="113" r="3.3" fill="#c1440e"/>
    <circle cx="288" cy="113" r="3.3" fill="#c1440e"/>
    <circle cx="297" cy="113" r="3.3" fill="#c1440e"/>
    <circle cx="306" cy="113" r="3.3" fill="#c1440e"/>
    <circle cx="315" cy="113" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <circle cx="234" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="243" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="252" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="261" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="270" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="279" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="288" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="297" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="306" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="315" cy="122" r="3.3" fill="#c1440e"/>
    <circle cx="234" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="243" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="252" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="261" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="270" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="279" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="288" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="297" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="306" cy="131" r="3.3" fill="#c1440e"/>
    <circle cx="315" cy="131" r="3.3" fill="#c1440e"/>
    <text x="274" y="152" text-anchor="middle">the best CCDs</text>
    <text x="274" y="164" text-anchor="middle">over 90 in 100</text>
    <circle cx="24" cy="200" r="3.3" fill="#c1440e"/>
    <text x="32" y="203">photon recorded</text>
    <circle cx="114" cy="200" r="3.3" fill="none" stroke="#555" stroke-width="0.6"/>
    <text x="122" y="203">photon lost</text>
    <text x="6" y="12">Out of 100 photons arriving, how many are recorded?</text>
    <text x="6" y="232">So a CCD collects in 1 minute what film needs about 35 minutes to collect.</text>
  </g>
</svg>
</div>

*Figure A. The fraction of the light that film and CCDs record.*

The fraction of photons a detector records is its **quantum efficiency**. Photographic film records only about 2% of
the light falling on it. The electronic detectors that replaced it, CCDs (section 14.5), commonly record about 70%,
and more than 90% at some wavelengths. With such detectors, and above the blurring air, Hubble can record stars of
magnitude 31, some 1,000 times fainter than the 5 m Hale Telescope could photograph in 1949.

??? note "Sources"
    - Long exposures recording hundreds of thousands of new stars and nebulae invisible to the eye, telescopes built as
      big cameras, and Hubble reaching magnitude 31, some 1,000 times dimmer than the Hale Telescope in 1949:
      Wikipedia, [Astrophotography](https://en.wikipedia.org/wiki/Astrophotography) (weaker).
    - CCDs commonly responding to 70% of the light, against about 2% for film: Wikipedia,
      [Charge-coupled device](https://en.wikipedia.org/wiki/Charge-coupled_device) (weaker).
    - Film well under 10% and CCDs well over 90% at some wavelengths: Wikipedia,
      [Quantum efficiency](https://en.wikipedia.org/wiki/Quantum_efficiency) (weaker).

## 14.4 The sky on glass { #carte }

In 1887 **Amédée Mouchez**, director of the Paris Observatory, saw that the dry plate could map the whole sky. He
started the **Carte du Ciel** ("map of the sky"). The sky was split into bands by declination, and each band was given
to one observatory:

| Region | Observatories |
| --- | --- |
| Europe | Greenwich, Oxford and Edinburgh in Britain; Paris, Bordeaux and Toulouse in France; the Vatican; Catania in Sicily; Helsinki; Potsdam; Uccle in Belgium; San Fernando in Spain |
| Africa | Algiers; Cape Town |
| Asia | Hyderabad, India, which photographed two bands |
| The Americas | Tacubaya, Mexico; Córdoba, Argentina |
| Australia | Perth; Sydney; Melbourne |

Twenty observatories exposed and measured more than 22,000 glass plates. The first was taken at the Vatican in August
1891, the last at Uccle in December 1950. The printed map was never finished, but the measured part, the
**Astrographic Catalogue**, holds about 4.6 million stars. A century later, compared with the positions measured by
ESA's Hipparcos satellite, those old plates showed how 2.5 million stars had moved across the sky.

**Plates kept for ever.** Glass does not bend or stretch, so plates were far better than film for measuring. Harvard
College Observatory keeps about 600,000 plates taken between the 1880s and 1989; the women "computers" who sorted the
stars by their spectra worked from them (history book,
[chapter 18, section 18.6](../history/18-Light-Split-into-Colours.md#stars)). At **Kodaikanal** in India, a
refractor first bought in 1850 has photographed the whole Sun every clear day since the early 1900s. About 117 years
of its pictures are being digitised to study the last ten cycles of sunspots.

??? note "Sources"
    - Mouchez in 1887, the 20 observatories, more than 22,000 plates, the first at the Vatican in August 1891 and the
      last at Uccle in December 1950, the map never completed, and the table of zones and observatories: Wikipedia,
      [Carte du Ciel](https://en.wikipedia.org/wiki/Carte_du_Ciel) (weaker).
    - About 4.6 million stars, and proper motions for 2.5 million stars using Hipparcos and Tycho-2: Wikipedia,
      [Astrographic Catalogue](https://en.wikipedia.org/wiki/Astrographic_Catalogue) (weaker).
    - Glass plates stable and less likely to bend: Wikipedia,
      [Photographic plate](https://en.wikipedia.org/wiki/Photographic_plate) (weaker).
    - About 600,000 plates from the mid-1880s to 1989: Wikipedia,
      [Harvard College Observatory](https://en.wikipedia.org/wiki/Harvard_College_Observatory) (weaker).
    - Kodaikanal's refractor of 1850, daily white-light pictures since the early 1900s, and about 117 years of
      photographs being digitised: Wikipedia,
      [Kodaikanal Solar Observatory](https://en.wikipedia.org/wiki/Kodaikanal_Solar_Observatory) (weaker).

## 14.5 The CCD { #ccd }

In 1969, at Bell Labs in the United States, **Willard Boyle**, a Canadian born in Amherst, Nova Scotia, and **George
Smith**, an American born in White Plains, New York, invented the **charge-coupled device**, or **CCD**. In 2009 they
shared half of the Nobel Prize in Physics for it.

A CCD is a chip of silicon divided into a grid of pixels. Light falling on a pixel frees electrons (chapter 1, section
1.7), and the pixel stores them: the more light, the more electrons. To read the picture, the chip passes the charges
from pixel to pixel, like buckets along a line, to an amplifier at one corner that turns each into a voltage, and then
a number.

<div class="pattern-row" markdown="0">
<svg viewBox="0 0 340 250" role="img" aria-label="How a CCD reads out a picture. On the left a grid of pixels, four rows by five columns, each holding a pile of electrons made by the light that fell on it: more light, more electrons. Arrows show each row of charge being shifted down one step at a time, like buckets passed along a line, into a single readout row at the bottom. The readout row then shifts its charges sideways, one at a time, into an amplifier that measures each one and turns it into a number. The numbers, row by row, make the picture.">
  <g font-size="8" fill="currentColor">
    <rect x="40" y="40" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="46" cy="64" r="2.6" fill="#eea66f"/>
    <rect x="74" y="40" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="80" cy="64" r="2.6" fill="#eea66f"/>
    <circle cx="89" cy="64" r="2.6" fill="#eea66f"/>
    <rect x="108" y="40" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="114" cy="64" r="2.6" fill="#eea66f"/>
    <circle cx="123" cy="64" r="2.6" fill="#eea66f"/>
    <circle cx="132" cy="64" r="2.6" fill="#eea66f"/>
    <circle cx="114" cy="56" r="2.6" fill="#eea66f"/>
    <circle cx="123" cy="56" r="2.6" fill="#eea66f"/>
    <rect x="142" y="40" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="148" cy="64" r="2.6" fill="#eea66f"/>
    <circle cx="157" cy="64" r="2.6" fill="#eea66f"/>
    <rect x="176" y="40" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="182" cy="64" r="2.6" fill="#eea66f"/>
    <rect x="40" y="74" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="46" cy="98" r="2.6" fill="#eea66f"/>
    <circle cx="55" cy="98" r="2.6" fill="#eea66f"/>
    <rect x="74" y="74" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="80" cy="98" r="2.6" fill="#eea66f"/>
    <circle cx="89" cy="98" r="2.6" fill="#eea66f"/>
    <circle cx="98" cy="98" r="2.6" fill="#eea66f"/>
    <circle cx="80" cy="90" r="2.6" fill="#eea66f"/>
    <circle cx="89" cy="90" r="2.6" fill="#eea66f"/>
    <circle cx="98" cy="90" r="2.6" fill="#eea66f"/>
    <rect x="108" y="74" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="114" cy="98" r="2.6" fill="#eea66f"/>
    <circle cx="123" cy="98" r="2.6" fill="#eea66f"/>
    <circle cx="132" cy="98" r="2.6" fill="#eea66f"/>
    <circle cx="114" cy="90" r="2.6" fill="#eea66f"/>
    <circle cx="123" cy="90" r="2.6" fill="#eea66f"/>
    <circle cx="132" cy="90" r="2.6" fill="#eea66f"/>
    <circle cx="114" cy="82" r="2.6" fill="#eea66f"/>
    <circle cx="123" cy="82" r="2.6" fill="#eea66f"/>
    <circle cx="132" cy="82" r="2.6" fill="#eea66f"/>
    <rect x="142" y="74" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="148" cy="98" r="2.6" fill="#eea66f"/>
    <circle cx="157" cy="98" r="2.6" fill="#eea66f"/>
    <circle cx="166" cy="98" r="2.6" fill="#eea66f"/>
    <circle cx="148" cy="90" r="2.6" fill="#eea66f"/>
    <circle cx="157" cy="90" r="2.6" fill="#eea66f"/>
    <circle cx="166" cy="90" r="2.6" fill="#eea66f"/>
    <rect x="176" y="74" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="182" cy="98" r="2.6" fill="#eea66f"/>
    <circle cx="191" cy="98" r="2.6" fill="#eea66f"/>
    <rect x="40" y="108" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="46" cy="132" r="2.6" fill="#eea66f"/>
    <rect x="74" y="108" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="80" cy="132" r="2.6" fill="#eea66f"/>
    <circle cx="89" cy="132" r="2.6" fill="#eea66f"/>
    <circle cx="98" cy="132" r="2.6" fill="#eea66f"/>
    <rect x="108" y="108" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="114" cy="132" r="2.6" fill="#eea66f"/>
    <circle cx="123" cy="132" r="2.6" fill="#eea66f"/>
    <circle cx="132" cy="132" r="2.6" fill="#eea66f"/>
    <circle cx="114" cy="124" r="2.6" fill="#eea66f"/>
    <circle cx="123" cy="124" r="2.6" fill="#eea66f"/>
    <circle cx="132" cy="124" r="2.6" fill="#eea66f"/>
    <rect x="142" y="108" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="148" cy="132" r="2.6" fill="#eea66f"/>
    <circle cx="157" cy="132" r="2.6" fill="#eea66f"/>
    <circle cx="166" cy="132" r="2.6" fill="#eea66f"/>
    <rect x="176" y="108" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="182" cy="132" r="2.6" fill="#eea66f"/>
    <rect x="40" y="142" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <rect x="74" y="142" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="80" cy="166" r="2.6" fill="#eea66f"/>
    <rect x="108" y="142" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="114" cy="166" r="2.6" fill="#eea66f"/>
    <circle cx="123" cy="166" r="2.6" fill="#eea66f"/>
    <rect x="142" y="142" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <circle cx="148" cy="166" r="2.6" fill="#eea66f"/>
    <rect x="176" y="142" width="30" height="30" fill="#5aa0d8" fill-opacity="0.12" stroke="currentColor" stroke-width="0.8"/>
    <rect x="40" y="184" width="30" height="30" fill="#cfc8bf" fill-opacity="0.35" stroke="currentColor" stroke-width="0.8"/>
    <rect x="74" y="184" width="30" height="30" fill="#cfc8bf" fill-opacity="0.35" stroke="currentColor" stroke-width="0.8"/>
    <rect x="108" y="184" width="30" height="30" fill="#cfc8bf" fill-opacity="0.35" stroke="currentColor" stroke-width="0.8"/>
    <rect x="142" y="184" width="30" height="30" fill="#cfc8bf" fill-opacity="0.35" stroke="currentColor" stroke-width="0.8"/>
    <rect x="176" y="184" width="30" height="30" fill="#cfc8bf" fill-opacity="0.35" stroke="currentColor" stroke-width="0.8"/>
    <path d="M55.0,174 L55.0,182 M52.0,179 L55.0,182 L58.0,179" fill="none" stroke="#c1440e" stroke-width="1"/>
    <path d="M89.0,174 L89.0,182 M86.0,179 L89.0,182 L92.0,179" fill="none" stroke="#c1440e" stroke-width="1"/>
    <path d="M123.0,174 L123.0,182 M120.0,179 L123.0,182 L126.0,179" fill="none" stroke="#c1440e" stroke-width="1"/>
    <path d="M157.0,174 L157.0,182 M154.0,179 L157.0,182 L160.0,179" fill="none" stroke="#c1440e" stroke-width="1"/>
    <path d="M191.0,174 L191.0,182 M188.0,179 L191.0,182 L194.0,179" fill="none" stroke="#c1440e" stroke-width="1"/>
    <path d="M214,199 L236,199 M232,195 L236,199 L232,203" fill="none" stroke="#c1440e" stroke-width="1.2"/>
    <polygon points="240,187 240,211 260,199" fill="#555" fill-opacity="0.25" stroke="currentColor" stroke-width="1"/>
    <text x="250" y="224" text-anchor="middle">amplifier</text>
    <text x="264" y="202">→ numbers</text>
    <text x="218" y="60">each pixel collects</text>
    <text x="218" y="70">electrons: more light,</text>
    <text x="218" y="80">more electrons</text>
    <text x="218" y="130">rows shift down</text>
    <text x="218" y="140">one step at a time</text>
    <text x="40" y="228">readout row: shifts sideways, one pixel at a time</text>
    <text x="6" y="12">Reading a CCD: charges passed along like buckets</text>
  </g>
</svg>
</div>

*Figure B. How a CCD reads out its picture.*

- **Efficient.** It records most of the light, not 2% of it (section 14.3).
- **Ready for computers.** The picture comes out as numbers.

From the early 1980s CCDs gradually replaced plates in observatories, and between 1980 and 2000 Kodak and others
stopped making most kinds of plate. Amateurs followed from the early 1990s. A warm chip slowly fills with electrons
even in the dark, so observatories often cool their CCDs with liquid nitrogen.

??? note "Sources"
    - Boyle and Smith at Bell Labs, the invention in 1969, and the Nobel Prize of 2009: Wikipedia,
      [Charge-coupled device](https://en.wikipedia.org/wiki/Charge-coupled_device) (weaker).
    - Charge passed from one storage capacitor to the next, the last one emptying into an amplifier that turns charge
      into voltage, the voltages digitised, and cooling with liquid nitrogen to reduce the dark current: the same page.
    - Boyle born in Amherst, Nova Scotia, Canadian, and his half share of the 2009 prize: Wikipedia,
      [Willard Boyle](https://en.wikipedia.org/wiki/Willard_Boyle) (weaker).
    - Smith born in White Plains, New York, American: Wikipedia,
      [George E. Smith](https://en.wikipedia.org/wiki/George_E._Smith) (weaker).
    - Plates replaced by CCDs from the early 1980s, and Kodak and others stopping most plates between 1980 and 2000:
      Wikipedia, [Photographic plate](https://en.wikipedia.org/wiki/Photographic_plate) (weaker).
    - Amateurs switching from film to CCDs from the early 1990s: Wikipedia,
      [Astrophotography](https://en.wikipedia.org/wiki/Astrophotography) (weaker).

## 14.6 Colour, and the camera in your phone { #colour }

A pixel measures only how much light falls on it, not its colour.

- **Filters on every pixel.** In 1976 **Bryce Bayer** of Eastman Kodak patented a pattern of tiny red, green and blue
  filters over the pixels, with twice as many green ones as red or blue, to match the eye, which is most sensitive to
  green. Software then works out a full colour for every pixel.
- **One filter at a time.** Astronomers often take separate pictures through filters that each pass one colour, or
  only one spectral line, and combine them later. Then every pixel catches light in every
  picture.

Most cameras today use a newer kind of chip, the **CMOS** sensor, in which each pixel has its own amplifier. Working
versions were made by Mitsubishi Electric in Japan in 1992 and NASA's Jet Propulsion Laboratory in 1993.

??? note "Sources"
    - Bayer of Eastman Kodak, his patent of 1976, and twice as many green elements to mimic the eye: Wikipedia,
      [Bayer filter](https://en.wikipedia.org/wiki/Bayer_filter) (weaker).
    - Filters limiting photons to certain wavelengths: Wikipedia,
      [Astrophotography](https://en.wikipedia.org/wiki/Astrophotography) (weaker).
    - The CMOS active-pixel sensor, now much more common, developed by Mitsubishi Electric in 1992 and NASA's JPL in
      1993: Wikipedia, [Active-pixel sensor](https://en.wikipedia.org/wiki/Active-pixel_sensor) (weaker).

## 14.7 The largest camera ever built { #rubin }

On Cerro Pachón, a 2,682 m mountain in northern Chile, stands the **Vera C. Rubin Observatory**. Its 8.4 m telescope
feeds a camera of **3.2 gigapixels**, made of 189 CCDs of 16 megapixels each, the largest camera yet built. It saw
first light in June 2025 and began its full survey in July 2026. Taking a picture every 40 seconds, it will scan the
whole southern sky every few days for ten years, making a time-lapse film of the changing sky.

??? note "Sources"
    - Cerro Pachón at 2,682 m in northern Chile, the 8.4 m mirror, the 3.2-gigapixel CCD camera, the largest yet,
      189 CCDs of 16 megapixels, first light in June 2025, the full survey from July 2026, a picture every 40 seconds,
      and a full scan every few days for ten years: Wikipedia,
      [Vera C. Rubin Observatory](https://en.wikipedia.org/wiki/Vera_C._Rubin_Observatory) (weaker).

## 14.8 The first close-up pictures of Mars { #mars }

**From Earth.** In 1926 Donald Menzel used William Wright's photographs of Mars, taken at Lick Observatory, to find
the first real numbers for its air
(history book, [chapter 18, section 18.10](../history/18-Light-Split-into-Colours.md#mars)).

**Mariner 4, 1965.** NASA's Mariner 4 was launched on 28 November 1964 and flew past Mars on 14 and 15 July 1965,
9,846 km above the surface at its closest. Its camera was a small **Cassegrain** telescope (chapter 13) with red and
green filters, feeding a **vidicon**, a television tube that turned the image into an electrical signal. It took 21
pictures and part of a 22nd, and stored them on a tape recorder holding 5.24 million bits. Then it played them back to
Earth at just 8⅓ bits per second.

While the team waited for the computers, they printed out the numbers of the first picture, bought a set
of pastels from an art shop and coloured them in by number. The hand-drawn picture matched the computer's version
well. The pictures showed a cratered surface like the Moon's, which scientists had not expected.

**Viking 1, 1976.** On 20 July 1976 the Viking 1 lander became the first spacecraft to land successfully on Mars. Its
first picture started coming home 25 seconds after landing, and within minutes it took a second, a 300° panorama.

**Today.** HiRISE (chapter 13) collects light on 14 CCDs, and its red pictures are 20,048 pixels wide. The rovers'
colour cameras photograph calibration targets with known colours, so the pictures can be adjusted to show Mars as it
really looks, or as the rocks would look under sunlight on Earth (chapter 10).

??? note "Sources"
    - Menzel and Wright's photographs of 1926: this site's history book, chapter 18, section 18.10.
    - Mariner 4's launch on 28 November 1964, the flyby of 14 and 15 July 1965 at 9,846 km, the Cassegrain telescope,
      red and green filters, the vidicon tube, 21 pictures and 21 lines of a 22nd, the 5.24-million-bit tape, the rate
      of 8⅓ bits per second, the pastel set from an art supply store, and the unexpected Moon-like craters: Wikipedia,
      [Mariner 4](https://en.wikipedia.org/wiki/Mariner_4) (weaker).
    - Viking 1's landing on 20 July 1976, the first successful Mars lander, its two facsimile cameras and the 300°
      panorama, and the first image starting 25 seconds after landing: Wikipedia,
      [Viking 1](https://en.wikipedia.org/wiki/Viking_1) (weaker).
    - HiRISE's 14 CCDs and 20,048-pixel red images: Wikipedia, [HiRISE](https://en.wikipedia.org/wiki/HiRISE) (weaker).
    - Calibration targets and white balance: the physics lesson
      [Colour cameras on Mars](https://physics.akadian.ca/topics/waves/level-6/06-colour-cameras-on-mars.html).

## 14.9 Working it out { #working }

**Film against a CCD.** To collect the same number of photons, film at 2% needs $70/2 = 35$ times longer than a CCD at
70%. A 1-minute CCD exposure equals 35 minutes on film.

**Mariner 4's slow line home.** A full tape of 5.24 million bits at 8⅓ bits per second takes

$$\frac{5{,}240{,}000}{8.33} \approx 629{,}000 \text{ s} \approx 7.3 \text{ days}.$$

Shared among its 22 pictures, that is about 240,000 bits, or nearly 8 hours of sending, for each one.

**HiRISE's swath.** 20,048 pixels of 0.3 m make a strip $20{,}048 \times 0.3 \approx 6{,}000$ m wide, the 6 km of
chapter 13.

**Rubin's night.** In 10 hours, one picture every 40 seconds gives 900 pictures of 3.2 gigapixels each: nearly
3 trillion pixels a night.

| A daytime photograph of the ground | Mars | Earth |
| --- | --- | --- |
| Sunlight on each square metre | 586 W | 1,361 W |
| Exposure needed for the same picture | $1{,}361/586 = 2.3$ times longer | 1 |
| Colour of the light | tinted by reddish dust | white |

??? note "Sources"
    - The quantum efficiencies: section 14.3. Mariner 4: section 14.8. HiRISE: section 14.8 and chapter 13. Rubin:
      section 14.7.
    - Sunlight at Mars and Earth: chapter 5, section 5.7, from NASA's
      [Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html).
    - The dust-tinted light: the physics lesson
      [Colour cameras on Mars](https://physics.akadian.ca/topics/waves/level-6/06-colour-cameras-on-mars.html).
    - The arithmetic is ours.

## 14.10 Counting photons: noise and stacking { #noise }

Light arrives as separate photons, at random moments, like raindrops on a roof. If a pixel expects on average $N$
photons during an exposure, the number it actually gets varies from picture to picture by about $\sqrt{N}$. This
**photon noise** can never be removed. So the **signal-to-noise ratio** is

$$\frac{N}{\sqrt{N}} = \sqrt{N}.$$

To make a picture twice as clean you need four times the photons.

**Other noise.** A real camera adds more: electrons freed by heat (the **dark current**, which cooling reduces) and a
little error each time a pixel is read out (**read noise**). If the star gives $S$ electrons, the sky glow $B$, the
dark current $D$, and the read noise is $R$ electrons,

$$\text{signal-to-noise} = \frac{S}{\sqrt{S + B + D + R^2}}.$$

**Stacking.** Add together $n$ pictures of the same thing and the signal grows $n$ times while the random noise grows
only $\sqrt{n}$ times. So averaging $n$ pictures improves the signal-to-noise ratio by $\sqrt{n}$: 100 pictures make
one 10 times cleaner. This is how amateurs get deep pictures from many short exposures, and how lucky imaging works
(chapter 12).

**Why quantum efficiency matters twice.** $N$ is the number of photons *recorded*, $N = \text{QE} \times
(\text{photons arriving})$. For the same signal-to-noise ratio, film at 2% needs 35 times the exposure of a CCD at 70%.

??? note "Sources"
    - Averaging images improving the signal-to-noise ratio by the square root of the number of images: Wikipedia,
      [Image stacking](https://en.wikipedia.org/wiki/Image_stacking) (weaker).
    - Dark current reduced by cooling: Wikipedia,
      [Charge-coupled device](https://en.wikipedia.org/wiki/Charge-coupled_device) (weaker).
    - Photon noise growing as $\sqrt{N}$, and the signal-to-noise formula, are standard results of counting statistics.

## Check yourself { #check }

**1.** (beginner) What two things can a camera do that the eye cannot?

??? note "Answer"
    It can keep a permanent record of what it sees, and it can keep adding up light over a long exposure.

**2.** (beginner) Who took the first successful photograph of the Moon, and when?

??? note "Answer"
    John William Draper in New York, on 23 March 1840, with a 20-minute daguerreotype.

**3.** (beginner) Roughly what fraction of the light does photographic film record, and a CCD?

??? note "Answer"
    About 2% for film; about 70% for a typical CCD, and over 90% at some wavelengths for the best.

**4.** (intermediate) What was the Carte du Ciel, and name three observatories outside Europe that took part.

??? note "Answer"
    An international project, begun in 1887, to photograph the whole sky on glass plates. Any three of: Algiers, Cape
    Town, Hyderabad, Tacubaya, Córdoba, Perth, Sydney, Melbourne.

**5.** (intermediate) How does a CCD read out its picture?

??? note "Answer"
    Each pixel stores electrons freed by light. The charges are passed from pixel to pixel, row by row, to an amplifier
    that turns each into a voltage, which is then turned into a number.

**6.** (intermediate) Why does a Bayer filter have twice as many green pixels as red or blue?

??? note "Answer"
    To match the human eye, which is most sensitive to green light.

**7.** (advanced) Mariner 4 sent 8⅓ bits per second. How long would one picture of 240,000 bits take?

??? note "Answer"
    $240{,}000 / 8.33 \approx 28{,}800$ s, about 8 hours.

**8.** (expert) A star gives 400 electrons in one exposure, and other noise is negligible. What is the signal-to-noise
ratio? How many such exposures must be stacked to reach 100?

??? note "Answer"
    $\sqrt{400} = 20$. Stacking $n$ exposures multiplies it by $\sqrt{n}$, so $20\sqrt{n} = 100$ gives $n = 25$.

## Summary

- The eye adapts well to the dark, but it cannot keep a record or add up light over time.
- Draper photographed the Moon in 1840; Bond and Whipple photographed Vega in 1850; Henry Draper photographed a star's
  spectrum in 1872 and the Orion Nebula in 1880.
- Long exposures on dry plates revealed hundreds of thousands of stars and nebulae no eye had seen.
- Twenty observatories around the world photographed the sky for the Carte du Ciel, from 1891 to 1950.
- Film records about 2% of the light; CCDs, invented by Boyle and Smith in 1969, record 70% or more.
- A CCD passes its charges along like buckets to an amplifier; the picture comes out as numbers.
- Bayer filters let one chip see colour; astronomers often use one filter at a time.
- The Rubin Observatory's 3.2-gigapixel camera scans the southern sky every few days.
- Mariner 4's 21 pictures of Mars came home at 8⅓ bits per second and were first coloured in by hand.
- Photon noise grows as $\sqrt{N}$; stacking $n$ pictures improves the signal-to-noise ratio by $\sqrt{n}$.

**Next:** chapter 15, Spectrographs, where we see how the light caught by a telescope is spread into a spectrum and
read.

## Further reading

- Alan Hirshfeld, *Starlight Detectives: How Astronomers, Inventors, and Eccentrics Discovered the Modern Universe*,
  Bellevue Literary Press, 2014.
