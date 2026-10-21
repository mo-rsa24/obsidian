---
aliases: [trigonometry, trig]
---

# Trigonometry

Up: [[Mathematics]]

Mathematics, Trigonometry. **Trigonometry measures triangles and the circles they sit in.** Its cosine and sine are the two legs of a right triangle whose longest side is 1, which makes them the two coordinates of a point on the circle of radius 1. Every note here is worked at one angle, 46.25°, and draws each step on a Cartesian plane with the Python that made the picture.

Read them in this order:

- [[The Unit Circle]]: the cosine as adjacent over hypotenuse, the circle of radius 1 sampled every 15°, an angle as one line from the origin, and a point given by length and angle read as $(x, y) = (0.6915, 0.7224)$.
- [[Radians]]: the angle as the length of arc it cuts, 46.25° = 0.8072 rad and 90° = π/2 = 1.5708, and what goes wrong when degrees are fed to `math.cos`.
- [[The Cosine Wave]]: the two squared legs as shares of 1, the cosine and its square over one full turn, and why $\cos^2$ is flat at 0 and π/2 over the quarter turn the cosine noise schedule uses.

The three notes share one figure helper, [plane.py](sandbox/plane.py), and one folder of runs, made in [[The Unit Circle#Try the unit circle yourself]].
