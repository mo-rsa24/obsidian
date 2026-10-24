---
aliases: [trigonometry, trig]
standard: vault-note v2
---

# Trigonometry

Up: [[Mathematics]]

Mathematics, Trigonometry.

**Trigonometry measures triangles and the circles they sit in. Its cosine and sine are the two legs of a right triangle whose longest side is 1. That makes them the two coordinates of a point on the circle of radius 1.**

**The toy angle.** Every note here is worked at one angle, 46.25°, the angle of post 51 in [[The Quarter Circle Under The Cosine Schedule]]. Each step is drawn on a Cartesian plane with the Python that made the picture.

Read them in this order, top to bottom.

## The circle and the point

- [[The Unit Circle]]: the cosine as adjacent over hypotenuse, the circle of radius 1 sampled every 15° with why its equation squares and sums the legs, and an angle as one line from the origin.
- [[Polar Coordinates]]: a point given by its length and its turn read as $(x, y) = (r\cos\theta, r\sin\theta) = (0.6915, 0.7224)$, and the way back with `atan2`.
- [[Running The Unit Circle]]: the nine-step sandbox that runs the figure scripts of both notes in an empty folder, each output read field by field.

## The angle as a length

- [[Radians]]: the angle as the length of arc it cuts, 46.25° = 0.8072 rad and 90° = π/2 = 1.5708, and what goes wrong when degrees are fed to `math.cos`.

## The wave and its flat ends

- [[The Cosine Wave]]: the two squared legs as shares of 1, the cosine and its square over one full turn, and why $\cos^2$ is flat at 0 and π/2 over the quarter turn the cosine noise schedule uses, beside the cosine alone ending at slope −1.
- [[How The Cosine Wave Works]]: the identity from Pythagoras, the slope $-2\cos\theta\sin\theta = -\sin 2\theta$ one step per line, and the drops 0.067 and 0.25 from that slope.
- [[Running The Cosine Wave]]: the nine-step sandbox for the cosine wave's three figure scripts and its slope measured two ways, each output read field by field.

**One helper, one folder.** The notes here share one figure helper, [plane.py](sandbox/plane.py), and one folder of runs, `~/playground/sandbox/unit-circle-figures`, made in [[Running The Unit Circle#Try the unit circle yourself|step 3 of the unit circle sandbox]]. [[Radians]] and [[Running The Cosine Wave]] run their scripts in that same folder.

## Words this uses

Each word links to the heading that teaches it, in reading order.

- [[The Unit Circle#The base word: cosine, on a right triangle|cosine]]: adjacent over hypotenuse, 0.6915 at 46.25°; on the unit circle it is the point's x-coordinate, the horizontal leg.
- [[The Unit Circle#The base word: cosine, on a right triangle|hypotenuse]]: the side facing the right angle, of length 1 on the unit circle.
- [[The Unit Circle#The angle: one line from the origin|sine]]: the point's y-coordinate, the vertical leg, 0.7224 at 46.25°.
- [[The Unit Circle#The angle: one line from the origin|angle in standard position]]: a turn anticlockwise from the positive x-axis, drawn as one line of length 1 from the origin.
- [[The Unit Circle#The circle: every point at distance 1|unit circle]]: every point at distance 1 from the origin, $x^2 + y^2 = 1$.
- [[The Unit Circle#The angles and their table|toy angle]]: 46.25°, whose point on the unit circle is $(0.6915, 0.7224)$.
- [[Polar Coordinates#The base word: coordinates|coordinates]]: the numbers that name a point, the usual pair saying how far right and how far up.
- [[Polar Coordinates#The point: from length and angle to x and y|polar coordinates]]: a point named by its length and its turn, $(r, \theta)$, read as $(r\cos\theta, r\sin\theta)$.
- [[Polar Coordinates#Other ways to convert|atan2]]: the turn from $(x, y)$ with the quadrant chosen, 226.25° for $(-0.6915, -0.7224)$ where $\tan^{-1}(y/x)$ alone gives 46.25°.
- [[Radians#The base word: radian|radian]]: an angle measured by the arc it cuts on radius 1; one radian is 57.30°.
- [[Radians#The base word: radian|arc length]]: $s = r\theta$, the radius times the angle in radians.
- [[Radians#Then the conversion: degrees to radians|degrees to radians]]: multiply by π/180, so 46.25° is 0.8072 rad.
- [[Radians#The consequence: degrees fed in as radians|degrees fed in as radians]]: `math.cos(46.25)` returns −0.6418 where 0.6915 was meant.
- [[The Cosine Wave#The base word: wave|period]]: $2\pi$, the turn after which the cosine repeats.
- [[The Cosine Wave#The two shares|the two shares]]: $\cos^2\theta$ and $\sin^2\theta$, which fill 1 between them, 0.4782 + 0.5218 at 46.25°.
- [[How The Cosine Wave Works#The identity|Pythagorean identity]]: $\cos^2\theta + \sin^2\theta = 1$, Pythagoras divided by $r^2$.
- [[The Cosine Wave#The quarter turn: where the square is flat|quarter turn]]: the angles from 0 to π/2 = 1.5708 rad, over which $\cos^2$ falls from 1 to 0.
- [[The Cosine Wave#The quarter turn: where the square is flat|slope of cos²]]: $-2\cos\theta\sin\theta = -\sin 2\theta$, 0 at both ends of the quarter turn and −1 at π/4.
- [[How The Cosine Wave Works#The slope|chain rule]]: the step that gives the slope its 2, the outer square's own slope $2u$ for $u^2$.
- [[How The Cosine Wave Works#The drops|drops]]: how much $\cos^2$ loses over each 15° step, 0.067 at the ends and 0.25 in the middle.
