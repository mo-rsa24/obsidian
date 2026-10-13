# Textbooks

The reference shelf for the moment a derivation stalls on a fundamental: a rule for logs, a trig
identity, a matrix derivative. Each book below lists its chapters with the PDF page each one starts
on, so a link can open the book at the right page.

## How a book is named and filed

**One folder per subject.** `general/` holds handbooks that span several subjects. A book goes in the
subject it mostly teaches, even when the shelf holds only one book on that subject, so that a link
written today still resolves when a second book arrives.

**Lowercase words joined by hyphens, named for what the file covers.** `algebra-handbook.pdf`,
`matrix-vector-multiplication.pdf`. No spaces, capitals, underscores or `&`, so a path works unquoted in
the shell and unescaped in a markdown link. Author and version live in this file, never in the name.

**A new book gets a section here when it lands**, with its chapter table, before anything links to it.

## How to link to a page

Add `#page=N` to the path, where N is the PDF's own page count from its first page. Chrome, Edge,
Firefox and Obsidian's built-in PDF viewer open the file at that page.

The shelf lives in the vault at `$HOME/Obsidian/Mathematics/references/textbooks/`.

**From a vault note**, link by filename. Every filename on the shelf is unique, so Obsidian finds it
wherever the note sits, and the text after `|` is what the reader sees:

```markdown
the [[algebra-handbook.pdf#page=109|exponent rules]]
```

**From the learning tree** (a journey plan, a source topic), Obsidian's links do not resolve, so the
link is the absolute path to the file:

```markdown
the [exponent rules](file:///home/molef/Obsidian/Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=109)
```

Written as plain text, the path is
`$HOME/Obsidian/Mathematics/references/textbooks/algebra/algebra-handbook.pdf#page=109`.

**Printed page numbers and PDF page numbers.** For the handbooks and own notes, the number printed on
the page equals the PDF page number. The GED handbook binds three handbooks together, each with its
own printed numbering, so its table gives PDF pages only. The published textbooks and lecture notes
start their printed numbering after front matter, and each one's section states its offset. Every
table on this page gives PDF pages.

## Pages looked up most

| Looking for | Book | PDF page |
| --- | --- | --- |
| exponent rules (product, quotient, power, zero and negative exponents) | [algebra handbook](algebra/algebra-handbook.pdf#page=109) | 109 |
| logarithm rules | [algebra handbook](algebra/algebra-handbook.pdf#page=110) | 110 |
| e and the natural log | [algebra handbook](algebra/algebra-handbook.pdf#page=111) | 111 |
| converting between exponential and log form | [algebra handbook](algebra/algebra-handbook.pdf#page=113) | 113 |
| expanding and condensing log expressions | [algebra handbook](algebra/algebra-handbook.pdf#page=114) | 114 |
| what exponential curves look like | [algebra handbook](algebra/algebra-handbook.pdf#page=118) | 118 |
| what log curves look like | [algebra handbook](algebra/algebra-handbook.pdf#page=122) | 122 |
| solving exponential and log equations | [algebra handbook](algebra/algebra-handbook.pdf#page=125) | 125 |
| matrix derivatives | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=8) | 8 |
| Gaussian identities | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=40) | 40 |
| the area under a product of two Gaussian densities | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=42) | 42 |
| completing the square | [algebra handbook](algebra/algebra-handbook.pdf#page=74) | 74 |
| matrix multiplication | [algebra handbook](algebra/algebra-handbook.pdf#page=91) | 91 |
| gradient of a quadratic form | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=11) | 11 |
| conditional Gaussian; a linear combination of Gaussians, so variances add | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=41) | 41 |
| expectation of linear forms | [matrix cookbook](linear-algebra/matrix-cookbook.pdf#page=35) | 35 |

## general/

### Pre-algebra handbook

`general/pre-algebra-handbook.pdf`, 107 pages. Earl L. Whitney, *Math Handbook of Formulas, Processes
and Tricks: Pre-Algebra*, version 2.5, 2022 (mathguy.us). Was `Pre-Algebra & Basic Statistics.pdf`.

| Chapter | PDF page |
| --- | --- |
| 1 Numbers | [8](general/pre-algebra-handbook.pdf#page=8) |
| 2 Measures and Weights | [17](general/pre-algebra-handbook.pdf#page=17) |
| 3 Operations | [20](general/pre-algebra-handbook.pdf#page=20) |
| 4 Fractions and Decimals | [24](general/pre-algebra-handbook.pdf#page=24) |
| 5 Percents | [33](general/pre-algebra-handbook.pdf#page=33) |
| 6 Exponents and Roots | [39](general/pre-algebra-handbook.pdf#page=39) |
| 7 Equations and Inequalities | [46](general/pre-algebra-handbook.pdf#page=46) |
| 8 Linear Functions | [55](general/pre-algebra-handbook.pdf#page=55) |
| 9 Probability and Statistics | [61](general/pre-algebra-handbook.pdf#page=61) |
| 10 Geometry Basics | [66](general/pre-algebra-handbook.pdf#page=66) |
| 11 Triangles | [70](general/pre-algebra-handbook.pdf#page=70) |
| 12 Quadrilaterals | [77](general/pre-algebra-handbook.pdf#page=77) |
| 13 Transformations | [81](general/pre-algebra-handbook.pdf#page=81) |
| 14 Polygons | [87](general/pre-algebra-handbook.pdf#page=87) |
| 15 Perimeter, Area and Volume | [90](general/pre-algebra-handbook.pdf#page=90) |

### GED handbook

`general/ged-handbook.pdf`, 93 pages. Earl L. Whitney, *Math Handbook of Formulas, Processes and
Tricks: High School Equivalency (GED) Exam*, version 2.2, 2017. Was
`Mathematics Handbook Of Formula Processes & Tricks.pdf`. Selected pages from three of the author's
handbooks, bound in order.

| Part | PDF page |
| --- | --- |
| Pre-algebra | [3](general/ged-handbook.pdf#page=3) |
| Algebra | [17](general/ged-handbook.pdf#page=17) |
| Geometry | [65](general/ged-handbook.pdf#page=65) |

## algebra/

### Algebra handbook

`algebra/algebra-handbook.pdf`, 187 pages. Earl L. Whitney, *Math Handbook of Formulas, Processes and
Tricks: Algebra and PreCalculus*, version 3.5, 2022. Was `AlgebraHandbook.pdf`.

| Chapter | PDF page |
| --- | --- |
| 1 Basics | [9](algebra/algebra-handbook.pdf#page=9) |
| 2 Operations | [15](algebra/algebra-handbook.pdf#page=15) |
| 3 Solving Equations | [18](algebra/algebra-handbook.pdf#page=18) |
| 4 Probability & Statistics | [20](algebra/algebra-handbook.pdf#page=20) |
| 5 Functions | [24](algebra/algebra-handbook.pdf#page=24) |
| 6 Linear Functions | [35](algebra/algebra-handbook.pdf#page=35) |
| 7 Inequalities | [42](algebra/algebra-handbook.pdf#page=42) |
| 8 Systems of Equations | [49](algebra/algebra-handbook.pdf#page=49) |
| 9 Exponents (Basic) and Scientific Notation | [56](algebra/algebra-handbook.pdf#page=56) |
| 10 Polynomials: Basic | [60](algebra/algebra-handbook.pdf#page=60) |
| 11 Quadratic Functions | [73](algebra/algebra-handbook.pdf#page=73) |
| 12 Complex Numbers | [80](algebra/algebra-handbook.pdf#page=80) |
| 13 Radicals | [86](algebra/algebra-handbook.pdf#page=86) |
| 14 Matrices | [90](algebra/algebra-handbook.pdf#page=90) |
| 15 Exponents and Logarithms | [109](algebra/algebra-handbook.pdf#page=109) |
| 16 Polynomials: Intermediate | [126](algebra/algebra-handbook.pdf#page=126) |
| 17 Rational Functions | [137](algebra/algebra-handbook.pdf#page=137) |
| 18 Conic Sections | [148](algebra/algebra-handbook.pdf#page=148) |
| 19 Sequences and Series | [163](algebra/algebra-handbook.pdf#page=163) |

### Quadratic functions

`algebra/quadratic-functions.pdf`, 4 pages. Own notes, 10 September 2021. Was `Quadratic Functions.pdf`.

### Rational functions

`algebra/rational-functions.pdf`, 8 pages. Own notes on domains of rational functions. Was
`Rational_Functions.pdf`.

## geometry/

### Geometry handbook

`geometry/geometry-handbook.pdf`, 137 pages. Earl L. Whitney, *Math Handbook of Formulas, Processes and
Tricks: Geometry*. Was `GeometryHandbook.pdf`.

| Chapter | PDF page |
| --- | --- |
| 1 Basic Geometry | [6](geometry/geometry-handbook.pdf#page=6) |
| 2 Proofs | [16](geometry/geometry-handbook.pdf#page=16) |
| 3 Parallel and Perpendicular Lines | [22](geometry/geometry-handbook.pdf#page=22) |
| 4 Triangles: Basic | [29](geometry/geometry-handbook.pdf#page=29) |
| 5 Polygons | [43](geometry/geometry-handbook.pdf#page=43) |
| 6 Quadrilaterals | [46](geometry/geometry-handbook.pdf#page=46) |
| 7 Transformations | [55](geometry/geometry-handbook.pdf#page=55) |
| 8 Similarity | [68](geometry/geometry-handbook.pdf#page=68) |
| 9 Right Triangles | [80](geometry/geometry-handbook.pdf#page=80) |
| 10 Circles | [92](geometry/geometry-handbook.pdf#page=92) |
| 11 Perimeter and Area | [98](geometry/geometry-handbook.pdf#page=98) |
| 12 Surface Area and Volume | [111](geometry/geometry-handbook.pdf#page=111) |

## trigonometry/

### Trigonometry handbook

`trigonometry/trigonometry-handbook.pdf`, 114 pages. Earl L. Whitney, *Math Handbook of Formulas,
Processes and Tricks: Trigonometry*. Was `TrigonometryHandbook.pdf`.

| Chapter | PDF page |
| --- | --- |
| 1 Functions and Special Angles | [7](trigonometry/trigonometry-handbook.pdf#page=7) |
| 2 Graphs of Trig Functions | [15](trigonometry/trigonometry-handbook.pdf#page=15) |
| 3 Inverse Trigonometric Functions | [33](trigonometry/trigonometry-handbook.pdf#page=33) |
| 4 Key Angle Formulas | [37](trigonometry/trigonometry-handbook.pdf#page=37) |
| 5 Identities and Equations | [43](trigonometry/trigonometry-handbook.pdf#page=43) |
| 6 Solving an Oblique Triangle | [51](trigonometry/trigonometry-handbook.pdf#page=51) |
| 7 Area of a Triangle | [65](trigonometry/trigonometry-handbook.pdf#page=65) |
| 8 Polar Coordinates | [68](trigonometry/trigonometry-handbook.pdf#page=68) |
| 9 Polar Functions | [73](trigonometry/trigonometry-handbook.pdf#page=73) |
| 10 Vectors | [83](trigonometry/trigonometry-handbook.pdf#page=83) |

## linear-algebra/

### Linear algebra textbook

`linear-algebra/linear-algebra-textbook.pdf`, 802 pages. Howard Anton and Chris Rorres, *Elementary
Linear Algebra: Applications Version*, 11th edition, Wiley, 2014. A published textbook, from systems
of equations through vector spaces, eigenvalues, inner products and the SVD. Was
`Elementary Linear Algebra 11th Edition.pdf`. The printed page number is the PDF page minus 14.

| Chapter | PDF page |
| --- | --- |
| 1 Systems of Linear Equations and Matrices | [15](linear-algebra/linear-algebra-textbook.pdf#page=15) |
| 1.1 Introduction to Systems of Linear Equations | [16](linear-algebra/linear-algebra-textbook.pdf#page=16) |
| 1.2 Gaussian Elimination | [25](linear-algebra/linear-algebra-textbook.pdf#page=25) |
| 1.3 Matrices and Matrix Operations | [39](linear-algebra/linear-algebra-textbook.pdf#page=39) |
| 1.4 Inverses; Algebraic Properties of Matrices | [53](linear-algebra/linear-algebra-textbook.pdf#page=53) |
| 1.5 Elementary Matrices and a Method for Finding A-1 | [66](linear-algebra/linear-algebra-textbook.pdf#page=66) |
| 1.6 More on Linear Systems and Invertible Matrices | [75](linear-algebra/linear-algebra-textbook.pdf#page=75) |
| 1.7 Diagonal, Triangular, and Symmetric Matrices | [81](linear-algebra/linear-algebra-textbook.pdf#page=81) |
| 1.8 Matrix Transformations | [89](linear-algebra/linear-algebra-textbook.pdf#page=89) |
| 1.9 Applications of Linear Systems | [98](linear-algebra/linear-algebra-textbook.pdf#page=98) |
| 1.10 Application: Leontief Input-Output Models | [110](linear-algebra/linear-algebra-textbook.pdf#page=110) |
| 2 Determinants | [119](linear-algebra/linear-algebra-textbook.pdf#page=119) |
| 2.1 Determinants by Cofactor Expansion | [119](linear-algebra/linear-algebra-textbook.pdf#page=119) |
| 2.2 Evaluating Determinants by Row Reduction | [127](linear-algebra/linear-algebra-textbook.pdf#page=127) |
| 2.3 Properties of Determinants; Cramer’s Rule | [132](linear-algebra/linear-algebra-textbook.pdf#page=132) |
| 3 Euclidean Vector Spaces | [145](linear-algebra/linear-algebra-textbook.pdf#page=145) |
| 3.1 Vectors in 2-Space, 3-Space, and n-Space | [145](linear-algebra/linear-algebra-textbook.pdf#page=145) |
| 3.2 Norm, Dot Product, and Distance in Rn | [156](linear-algebra/linear-algebra-textbook.pdf#page=156) |
| 3.3 Orthogonality | [169](linear-algebra/linear-algebra-textbook.pdf#page=169) |
| 3.4 The Geometry of Linear Systems | [178](linear-algebra/linear-algebra-textbook.pdf#page=178) |
| 3.5 Cross Product | [186](linear-algebra/linear-algebra-textbook.pdf#page=186) |
| 4 General Vector Spaces | [197](linear-algebra/linear-algebra-textbook.pdf#page=197) |
| 4.1 Real Vector Spaces | [197](linear-algebra/linear-algebra-textbook.pdf#page=197) |
| 4.2 Subspaces | [205](linear-algebra/linear-algebra-textbook.pdf#page=205) |
| 4.3 Linear Independence | [216](linear-algebra/linear-algebra-textbook.pdf#page=216) |
| 4.4 Coordinates and Basis | [226](linear-algebra/linear-algebra-textbook.pdf#page=226) |
| 4.5 Dimension | [235](linear-algebra/linear-algebra-textbook.pdf#page=235) |
| 4.6 Change of Basis | [243](linear-algebra/linear-algebra-textbook.pdf#page=243) |
| 4.7 Row Space, Column Space, and Null Space | [251](linear-algebra/linear-algebra-textbook.pdf#page=251) |
| 4.8 Rank, Nullity, and the Fundamental Matrix Spaces | [262](linear-algebra/linear-algebra-textbook.pdf#page=262) |
| 4.9 Basic Matrix Transformations in R2 and R3 | [273](linear-algebra/linear-algebra-textbook.pdf#page=273) |
| 4.10 Properties of Matrix Transformations | [284](linear-algebra/linear-algebra-textbook.pdf#page=284) |
| 4.11 Application: Geometry of Matrix Operators on R2 | [294](linear-algebra/linear-algebra-textbook.pdf#page=294) |
| 5 Eigenvalues and Eigenvectors | [305](linear-algebra/linear-algebra-textbook.pdf#page=305) |
| 5.1 Eigenvalues and Eigenvectors | [305](linear-algebra/linear-algebra-textbook.pdf#page=305) |
| 5.2 Diagonalization | [316](linear-algebra/linear-algebra-textbook.pdf#page=316) |
| 5.3 Complex Vector Spaces | [327](linear-algebra/linear-algebra-textbook.pdf#page=327) |
| 5.4 Application: Differential Equations | [340](linear-algebra/linear-algebra-textbook.pdf#page=340) |
| 5.5 Application: Dynamical Systems and Markov Chains | [346](linear-algebra/linear-algebra-textbook.pdf#page=346) |
| 6 Inner Product Spaces | [359](linear-algebra/linear-algebra-textbook.pdf#page=359) |
| 6.1 Inner Products | [359](linear-algebra/linear-algebra-textbook.pdf#page=359) |
| 6.2 Angle and Orthogonality in Inner Product Spaces | [369](linear-algebra/linear-algebra-textbook.pdf#page=369) |
| 6.3 Gram–Schmidt Process; QR-Decomposition | [378](linear-algebra/linear-algebra-textbook.pdf#page=378) |
| 6.4 Best Approximation; Least Squares | [392](linear-algebra/linear-algebra-textbook.pdf#page=392) |
| 6.5 Application: Mathematical Modeling Using Least Squares | [401](linear-algebra/linear-algebra-textbook.pdf#page=401) |
| 6.6 Application: Function Approximation; Fourier Series | [408](linear-algebra/linear-algebra-textbook.pdf#page=408) |
| 7 Diagonalization and Quadratic Forms | [415](linear-algebra/linear-algebra-textbook.pdf#page=415) |
| 7.1 Orthogonal Matrices | [415](linear-algebra/linear-algebra-textbook.pdf#page=415) |
| 7.2 Orthogonal Diagonalization | [423](linear-algebra/linear-algebra-textbook.pdf#page=423) |
| 7.3 Quadratic Forms | [431](linear-algebra/linear-algebra-textbook.pdf#page=431) |
| 7.4 Optimization Using Quadratic Forms | [443](linear-algebra/linear-algebra-textbook.pdf#page=443) |
| 7.5 Hermitian, Unitary, and Normal Matrices | [451](linear-algebra/linear-algebra-textbook.pdf#page=451) |
| 8 General Linear Transformations | [461](linear-algebra/linear-algebra-textbook.pdf#page=461) |
| 8.1 General Linear Transformations | [461](linear-algebra/linear-algebra-textbook.pdf#page=461) |
| 8.2 Compositions and Inverse Transformations | [472](linear-algebra/linear-algebra-textbook.pdf#page=472) |
| 8.3 Isomorphism | [480](linear-algebra/linear-algebra-textbook.pdf#page=480) |
| 8.4 Matrices for General Linear Transformations | [486](linear-algebra/linear-algebra-textbook.pdf#page=486) |
| 8.5 Similarity | [495](linear-algebra/linear-algebra-textbook.pdf#page=495) |
| 9 Numerical Methods | [505](linear-algebra/linear-algebra-textbook.pdf#page=505) |
| 9.1 LU-Decompositions | [505](linear-algebra/linear-algebra-textbook.pdf#page=505) |
| 9.2 The Power Method | [515](linear-algebra/linear-algebra-textbook.pdf#page=515) |
| 9.3 Comparison of Procedures for Solving Linear Systems | [523](linear-algebra/linear-algebra-textbook.pdf#page=523) |
| 9.4 Singular Value Decomposition | [528](linear-algebra/linear-algebra-textbook.pdf#page=528) |
| 9.5 Application: Data Compression Using Singular Value Decomposition | [535](linear-algebra/linear-algebra-textbook.pdf#page=535) |
| 10 Applications of Linear Algebra | [541](linear-algebra/linear-algebra-textbook.pdf#page=541) |
| 10.1 Constructing Curves and Surfaces Through Specified Points | [542](linear-algebra/linear-algebra-textbook.pdf#page=542) |
| 10.2 The Earliest Applications of Linear Algebra | [547](linear-algebra/linear-algebra-textbook.pdf#page=547) |
| 10.3 Cubic Spline Interpolation | [554](linear-algebra/linear-algebra-textbook.pdf#page=554) |
| 10.4 Markov Chains | [565](linear-algebra/linear-algebra-textbook.pdf#page=565) |
| 10.5 Graph Theory | [575](linear-algebra/linear-algebra-textbook.pdf#page=575) |
| 10.6 Games of Strategy | [584](linear-algebra/linear-algebra-textbook.pdf#page=584) |
| 10.7 Leontief Economic Models | [593](linear-algebra/linear-algebra-textbook.pdf#page=593) |
| 10.8 Forest Management | [602](linear-algebra/linear-algebra-textbook.pdf#page=602) |
| 10.9 Computer Graphics | [609](linear-algebra/linear-algebra-textbook.pdf#page=609) |
| 10.10 Equilibrium Temperature Distributions | [617](linear-algebra/linear-algebra-textbook.pdf#page=617) |
| 10.11 Computed Tomography | [627](linear-algebra/linear-algebra-textbook.pdf#page=627) |
| 10.12 Fractals | [638](linear-algebra/linear-algebra-textbook.pdf#page=638) |
| 10.13 Chaos | [653](linear-algebra/linear-algebra-textbook.pdf#page=653) |
| 10.14 Cryptography | [666](linear-algebra/linear-algebra-textbook.pdf#page=666) |
| 10.15 Genetics | [677](linear-algebra/linear-algebra-textbook.pdf#page=677) |
| 10.16 Age-Specific Population Growth | [687](linear-algebra/linear-algebra-textbook.pdf#page=687) |
| 10.17 Harvesting of Animal Populations | [697](linear-algebra/linear-algebra-textbook.pdf#page=697) |
| 10.18 A Least Squares Model for Human Hearing | [705](linear-algebra/linear-algebra-textbook.pdf#page=705) |
| 10.19 Warps and Morphs | [711](linear-algebra/linear-algebra-textbook.pdf#page=711) |
| 10.20 Internet Search Engines | [720](linear-algebra/linear-algebra-textbook.pdf#page=720) |
| A Working with Proofs | [729](linear-algebra/linear-algebra-textbook.pdf#page=729) |
| B Complex Numbers | [733](linear-algebra/linear-algebra-textbook.pdf#page=733) |
| Answers to Exercises | [741](linear-algebra/linear-algebra-textbook.pdf#page=741) |

### The Matrix Cookbook

`linear-algebra/matrix-cookbook.pdf`, 72 pages. Petersen and Pedersen, *The Matrix Cookbook*, version
of 15 November 2012. Was `matrixcookbook.pdf`.

| Section | PDF page |
| --- | --- |
| 1 Basics | [6](linear-algebra/matrix-cookbook.pdf#page=6) |
| 2 Derivatives | [8](linear-algebra/matrix-cookbook.pdf#page=8) |
| 3 Inverses | [17](linear-algebra/matrix-cookbook.pdf#page=17) |
| 4 Complex Matrices | [24](linear-algebra/matrix-cookbook.pdf#page=24) |
| 5 Solutions and Decompositions | [28](linear-algebra/matrix-cookbook.pdf#page=28) |
| 6 Statistics and Probability | [34](linear-algebra/matrix-cookbook.pdf#page=34) |
| 7 Multivariate Distributions | [37](linear-algebra/matrix-cookbook.pdf#page=37) |
| 8 Gaussians | [40](linear-algebra/matrix-cookbook.pdf#page=40) |
| 9 Special Matrices | [46](linear-algebra/matrix-cookbook.pdf#page=46) |
| 10 Functions and Operators | [58](linear-algebra/matrix-cookbook.pdf#page=58) |
| A One-dimensional Results | [64](linear-algebra/matrix-cookbook.pdf#page=64) |
| B Proofs and Details | [66](linear-algebra/matrix-cookbook.pdf#page=66) |

### Matrix multiplication

`linear-algebra/matrix-multiplication.pdf`, 16 pages. Own notes, 4 April 2024: the compatibility check
and the dot-product rule for each entry. Was `Linear Algebra.pdf`.

### Matrix-vector multiplication

`linear-algebra/matrix-vector-multiplication.pdf`, 1 page. Own notes. Was
`Martix Vector Multiplcation.pdf`.

### Function evaluation and the dot product

`linear-algebra/function-evaluation-vs-dot-product.pdf`, 1 page. Own notes, 25 March 2021. Was
`Function Evaluation vs Dot Product.pdf`.

### Euclidean vector spaces

`linear-algebra/euclidean-vector-spaces.pdf`, 50 pages. Own notes from the Linear Algebra: Vector Spaces
series, 5 December 2022. Was `Euclidean Vector Spaces.pdf`.

### Spectral normalization

`linear-algebra/spectral-normalization.pdf`, 5 pages. Own notes from the Matrix Decompositions series,
23 January 2022: the spectral norm, then spectral normalization for GANs. Was
`Spectral Normalization.pdf`.

## calculus/

### Calculus textbook

`calculus/calculus-textbook.pdf`, 1318 pages. Howard Anton, Irl Bivens and Stephen Davis, *Calculus:
Early Transcendentals*, 10th edition, Wiley, 2012. A published textbook, single-variable through
vector calculus: derivatives and the chain rule, integration techniques, Taylor series, partial
derivatives and gradients, multiple integrals and Jacobians. Was
`Calculus Early Transcendentals, 10th Edition ( PDFDrive ).pdf`. The printed page number is the PDF
page minus 24.

| Chapter | PDF page |
| --- | --- |
| 0 Before Calculus | [25](calculus/calculus-textbook.pdf#page=25) |
| 0.1 Functions | [25](calculus/calculus-textbook.pdf#page=25) |
| 0.2 New Functions from Old | [39](calculus/calculus-textbook.pdf#page=39) |
| 0.3 Families of Functions | [51](calculus/calculus-textbook.pdf#page=51) |
| 0.4 Inverse Functions; Inverse Trigonometric Functions | [62](calculus/calculus-textbook.pdf#page=62) |
| 0.5 Exponential and Logarithmic Functions | [76](calculus/calculus-textbook.pdf#page=76) |
| 1 Limits and Continuity | [91](calculus/calculus-textbook.pdf#page=91) |
| 1.1 Limits (An Intuitive Approach) | [91](calculus/calculus-textbook.pdf#page=91) |
| 1.2 Computing Limits | [104](calculus/calculus-textbook.pdf#page=104) |
| 1.3 Limits at Infinity; End Behavior of a Function | [113](calculus/calculus-textbook.pdf#page=113) |
| 1.4 Limits (Discussed More Rigorously) | [124](calculus/calculus-textbook.pdf#page=124) |
| 1.5 Continuity | [134](calculus/calculus-textbook.pdf#page=134) |
| 1.6 Continuity of Trigonometric, Exponential, and Inverse Functions | [145](calculus/calculus-textbook.pdf#page=145) |
| 2 The Derivative | [155](calculus/calculus-textbook.pdf#page=155) |
| 2.1 Tangent Lines and Rates of Change | [155](calculus/calculus-textbook.pdf#page=155) |
| 2.2 The Derivative Function | [167](calculus/calculus-textbook.pdf#page=167) |
| 2.3 Introduction to Techniques of Differentiation | [179](calculus/calculus-textbook.pdf#page=179) |
| 2.4 The Product and Quotient Rules | [187](calculus/calculus-textbook.pdf#page=187) |
| 2.5 Derivatives of Trigonometric Functions | [193](calculus/calculus-textbook.pdf#page=193) |
| 2.6 The Chain Rule | [198](calculus/calculus-textbook.pdf#page=198) |
| 3 Topics in Differentiation | [209](calculus/calculus-textbook.pdf#page=209) |
| 3.1 Implicit Differentiation | [209](calculus/calculus-textbook.pdf#page=209) |
| 3.2 Derivatives of Logarithmic Functions | [216](calculus/calculus-textbook.pdf#page=216) |
| 3.3 Derivatives of Exponential and Inverse Trigonometric Functions | [221](calculus/calculus-textbook.pdf#page=221) |
| 3.4 Related Rates | [228](calculus/calculus-textbook.pdf#page=228) |
| 3.5 Local Linear Approximation; Differentials | [236](calculus/calculus-textbook.pdf#page=236) |
| 3.6 L'Hôpital's Rule; Indeterminate Forms | [243](calculus/calculus-textbook.pdf#page=243) |
| 4 The Derivative in Graphing and Applications | [256](calculus/calculus-textbook.pdf#page=256) |
| 4.1 Analysis of Functions I: Increase, Decrease, and Concavity | [256](calculus/calculus-textbook.pdf#page=256) |
| 4.2 Analysis of Functions II: Relative Extrema; Graphing Polynomials | [268](calculus/calculus-textbook.pdf#page=268) |
| 4.3 Analysis of Functions III: Rational Functions, Cusps, and Vertical Tangents | [278](calculus/calculus-textbook.pdf#page=278) |
| 4.4 Absolute Maxima and Minima | [290](calculus/calculus-textbook.pdf#page=290) |
| 4.5 Applied Maximum and Minimum Problems | [298](calculus/calculus-textbook.pdf#page=298) |
| 4.6 Rectilinear Motion | [312](calculus/calculus-textbook.pdf#page=312) |
| 4.7 Newton's Method | [320](calculus/calculus-textbook.pdf#page=320) |
| 4.8 Rolle's Theorem; Mean-Value Theorem | [326](calculus/calculus-textbook.pdf#page=326) |
| 5 Integration | [340](calculus/calculus-textbook.pdf#page=340) |
| 5.1 An Overview of the Area Problem | [340](calculus/calculus-textbook.pdf#page=340) |
| 5.2 The Indefinite Integral | [346](calculus/calculus-textbook.pdf#page=346) |
| 5.3 Integration by Substitution | [356](calculus/calculus-textbook.pdf#page=356) |
| 5.4 The Definition of Area as a Limit; Sigma Notation | [364](calculus/calculus-textbook.pdf#page=364) |
| 5.5 The Definite Integral | [377](calculus/calculus-textbook.pdf#page=377) |
| 5.6 The Fundamental Theorem of Calculus | [386](calculus/calculus-textbook.pdf#page=386) |
| 5.7 Rectilinear Motion Revisited Using Integration | [400](calculus/calculus-textbook.pdf#page=400) |
| 5.8 Average Value of a Function and its Applications | [409](calculus/calculus-textbook.pdf#page=409) |
| 5.9 Evaluating Definite Integrals by Substitution | [414](calculus/calculus-textbook.pdf#page=414) |
| 5.10 Logarithmic and Other Functions Defined by Integrals | [420](calculus/calculus-textbook.pdf#page=420) |
| 6 Applications of the Definite Integral in Geometry, Science, and Engineering | [437](calculus/calculus-textbook.pdf#page=437) |
| 6.1 Area Between Two Curves | [437](calculus/calculus-textbook.pdf#page=437) |
| 6.2 Volumes by Slicing; Disks and Washers | [445](calculus/calculus-textbook.pdf#page=445) |
| 6.3 Volumes by Cylindrical Shells | [456](calculus/calculus-textbook.pdf#page=456) |
| 6.4 Length of a Plane Curve | [462](calculus/calculus-textbook.pdf#page=462) |
| 6.5 Area of a Surface of Revolution | [468](calculus/calculus-textbook.pdf#page=468) |
| 6.6 Work | [473](calculus/calculus-textbook.pdf#page=473) |
| 6.7 Moments, Centers of Gravity, and Centroids | [482](calculus/calculus-textbook.pdf#page=482) |
| 6.8 Fluid Pressure and Force | [491](calculus/calculus-textbook.pdf#page=491) |
| 6.9 Hyperbolic Functions and Hanging Cables | [498](calculus/calculus-textbook.pdf#page=498) |
| 7 Principles of Integral Evaluation | [512](calculus/calculus-textbook.pdf#page=512) |
| 7.1 An Overview of Integration Methods | [512](calculus/calculus-textbook.pdf#page=512) |
| 7.2 Integration by Parts | [515](calculus/calculus-textbook.pdf#page=515) |
| 7.3 Integrating Trigonometric Functions | [524](calculus/calculus-textbook.pdf#page=524) |
| 7.4 Trigonometric Substitutions | [532](calculus/calculus-textbook.pdf#page=532) |
| 7.5 Integrating Rational Functions by Partial Fractions | [538](calculus/calculus-textbook.pdf#page=538) |
| 7.6 Using Computer Algebra Systems and Tables of Integrals | [547](calculus/calculus-textbook.pdf#page=547) |
| 7.7 Numerical Integration; Simpson's Rule | [557](calculus/calculus-textbook.pdf#page=557) |
| 7.8 Improper Integrals | [571](calculus/calculus-textbook.pdf#page=571) |
| 8 Mathematical Modeling with Differential Equations | [585](calculus/calculus-textbook.pdf#page=585) |
| 8.1 Modeling with Differential Equations | [585](calculus/calculus-textbook.pdf#page=585) |
| 8.2 Separation of Variables | [592](calculus/calculus-textbook.pdf#page=592) |
| 8.3 Slope Fields; Euler's Method | [603](calculus/calculus-textbook.pdf#page=603) |
| 8.4 First-Order Differential Equations and Applications | [610](calculus/calculus-textbook.pdf#page=610) |
| 9 Infinite Series | [620](calculus/calculus-textbook.pdf#page=620) |
| 9.1 Sequences | [620](calculus/calculus-textbook.pdf#page=620) |
| 9.2 Monotone Sequences | [631](calculus/calculus-textbook.pdf#page=631) |
| 9.3 Infinite Series | [638](calculus/calculus-textbook.pdf#page=638) |
| 9.4 Convergence Tests | [647](calculus/calculus-textbook.pdf#page=647) |
| 9.5 The Comparison, Ratio, and Root Tests | [655](calculus/calculus-textbook.pdf#page=655) |
| 9.6 Alternating Series; Absolute and Conditional Convergence | [662](calculus/calculus-textbook.pdf#page=662) |
| 9.7 Maclaurin and Taylor Polynomials | [672](calculus/calculus-textbook.pdf#page=672) |
| 9.8 Maclaurin and Taylor Series; Power Series | [683](calculus/calculus-textbook.pdf#page=683) |
| 9.9 Convergence of Taylor Series | [692](calculus/calculus-textbook.pdf#page=692) |
| 9.10 Differentiating and Integrating Power Series; Modeling with Taylor Series | [702](calculus/calculus-textbook.pdf#page=702) |
| 10 Parametric and Polar Curves; Conic Sections | [716](calculus/calculus-textbook.pdf#page=716) |
| 10.1 Parametric Equations; Tangent Lines and Arc Length for Parametric Curves | [716](calculus/calculus-textbook.pdf#page=716) |
| 10.2 Polar Coordinates | [729](calculus/calculus-textbook.pdf#page=729) |
| 10.3 Tangent Lines, Arc Length, and Area for Polar Curves | [743](calculus/calculus-textbook.pdf#page=743) |
| 10.4 Conic Sections | [754](calculus/calculus-textbook.pdf#page=754) |
| 10.5 Rotation of Axes; Second-Degree Equations | [772](calculus/calculus-textbook.pdf#page=772) |
| 10.6 Conic Sections in Polar Coordinates | [778](calculus/calculus-textbook.pdf#page=778) |
| 11 Three-Dimensional Space; Vectors | [791](calculus/calculus-textbook.pdf#page=791) |
| 11.1 Rectangular Coordinates in 3-Space; Spheres; Cylindrical Surfaces | [791](calculus/calculus-textbook.pdf#page=791) |
| 11.2 Vectors | [797](calculus/calculus-textbook.pdf#page=797) |
| 11.3 Dot Product; Projections | [809](calculus/calculus-textbook.pdf#page=809) |
| 11.4 Cross Product | [819](calculus/calculus-textbook.pdf#page=819) |
| 11.5 Parametric Equations of Lines | [829](calculus/calculus-textbook.pdf#page=829) |
| 11.6 Planes in 3-Space | [837](calculus/calculus-textbook.pdf#page=837) |
| 11.7 Quadric Surfaces | [845](calculus/calculus-textbook.pdf#page=845) |
| 11.8 Cylindrical and Spherical Coordinates | [856](calculus/calculus-textbook.pdf#page=856) |
| 12 Vector-Valued Functions | [865](calculus/calculus-textbook.pdf#page=865) |
| 12.1 Introduction to Vector-Valued Functions | [865](calculus/calculus-textbook.pdf#page=865) |
| 12.2 Calculus of Vector-Valued Functions | [872](calculus/calculus-textbook.pdf#page=872) |
| 12.3 Change of Parameter; Arc Length | [882](calculus/calculus-textbook.pdf#page=882) |
| 12.4 Unit Tangent, Normal, and Binormal Vectors | [892](calculus/calculus-textbook.pdf#page=892) |
| 12.5 Curvature | [897](calculus/calculus-textbook.pdf#page=897) |
| 12.6 Motion Along a Curve | [906](calculus/calculus-textbook.pdf#page=906) |
| 12.7 Kepler's Laws of Planetary Motion | [919](calculus/calculus-textbook.pdf#page=919) |
| 13 Partial Derivatives | [930](calculus/calculus-textbook.pdf#page=930) |
| 13.1 Functions of Two or More Variables | [930](calculus/calculus-textbook.pdf#page=930) |
| 13.2 Limits and Continuity | [941](calculus/calculus-textbook.pdf#page=941) |
| 13.3 Partial Derivatives | [951](calculus/calculus-textbook.pdf#page=951) |
| 13.4 Differentiability, Differentials, and Local Linearity | [964](calculus/calculus-textbook.pdf#page=964) |
| 13.5 The Chain Rule | [973](calculus/calculus-textbook.pdf#page=973) |
| 13.6 Directional Derivatives and Gradients | [984](calculus/calculus-textbook.pdf#page=984) |
| 13.7 Tangent Planes and Normal Vectors | [995](calculus/calculus-textbook.pdf#page=995) |
| 13.8 Maxima and Minima of Functions of Two Variables | [1001](calculus/calculus-textbook.pdf#page=1001) |
| 13.9 Lagrange Multipliers | [1013](calculus/calculus-textbook.pdf#page=1013) |
| 14 Multiple Integrals | [1024](calculus/calculus-textbook.pdf#page=1024) |
| 14.1 Double Integrals | [1024](calculus/calculus-textbook.pdf#page=1024) |
| 14.2 Double Integrals over Nonrectangular Regions | [1033](calculus/calculus-textbook.pdf#page=1033) |
| 14.3 Double Integrals in Polar Coordinates | [1042](calculus/calculus-textbook.pdf#page=1042) |
| 14.4 Surface Area; Parametric Surfaces | [1050](calculus/calculus-textbook.pdf#page=1050) |
| 14.5 Triple Integrals | [1063](calculus/calculus-textbook.pdf#page=1063) |
| 14.6 Triple Integrals in Cylindrical and Spherical Coordinates | [1072](calculus/calculus-textbook.pdf#page=1072) |
| 14.7 Change of Variables in Multiple Integrals; Jacobians | [1082](calculus/calculus-textbook.pdf#page=1082) |
| 14.8 Centers of Gravity Using Multiple Integrals | [1095](calculus/calculus-textbook.pdf#page=1095) |
| 15 Topics in Vector Calculus | [1108](calculus/calculus-textbook.pdf#page=1108) |
| 15.1 Vector Fields | [1108](calculus/calculus-textbook.pdf#page=1108) |
| 15.2 Line Integrals | [1118](calculus/calculus-textbook.pdf#page=1118) |
| 15.3 Independence of Path; Conservative Vector Fields | [1135](calculus/calculus-textbook.pdf#page=1135) |
| 15.4 Green's Theorem | [1146](calculus/calculus-textbook.pdf#page=1146) |
| 15.5 Surface Integrals | [1154](calculus/calculus-textbook.pdf#page=1154) |
| 15.6 Applications of Surface Integrals; Flux | [1162](calculus/calculus-textbook.pdf#page=1162) |
| 15.7 The Divergence Theorem | [1172](calculus/calculus-textbook.pdf#page=1172) |
| 15.8 Stokes' Theorem | [1182](calculus/calculus-textbook.pdf#page=1182) |
| Appendices | [1193](calculus/calculus-textbook.pdf#page=1193) |
| A Graphing Functions Using Calculators and Computer Algebra Systems | [1193](calculus/calculus-textbook.pdf#page=1193) |
| B Trigonometry Review | [1205](calculus/calculus-textbook.pdf#page=1205) |
| C Solving Polynomial Equations | [1219](calculus/calculus-textbook.pdf#page=1219) |
| D Selected Proofs | [1226](calculus/calculus-textbook.pdf#page=1226) |
| Answers to Odd-Numbered Exercises | [1237](calculus/calculus-textbook.pdf#page=1237) |

### Calculus practice problems

`calculus/calculus-practice-problems.pdf`, 626 pages. Patrick Jones and the Math Doctors, *Calculus:
1,001 Practice Problems For Dummies*, Wiley, 2014. A workbook: problems in Part I, worked answers in
Part II. Reach for it when a line asks the reader to practise a technique, and for the textbook when it
needs the technique taught. Was `Calculus Practice Problems For Dummies ( PDFDrive ).pdf`. The printed
page number is the PDF page minus 14.

| Chapter | PDF page |
| --- | --- |
| Part I: The Questions | [19](calculus/calculus-practice-problems.pdf#page=19) |
| 1 Algebra Review | [21](calculus/calculus-practice-problems.pdf#page=21) |
| 2 Trigonometry Review | [31](calculus/calculus-practice-problems.pdf#page=31) |
| 3 Limits and Rates of Change | [43](calculus/calculus-practice-problems.pdf#page=43) |
| 4 Derivative Basics | [57](calculus/calculus-practice-problems.pdf#page=57) |
| 5 The Product, Quotient, and Chain Rules | [63](calculus/calculus-practice-problems.pdf#page=63) |
| 6 Exponential and Logarithmic Functions and Tangent Lines | [69](calculus/calculus-practice-problems.pdf#page=69) |
| 7 Implicit Differentiation | [73](calculus/calculus-practice-problems.pdf#page=73) |
| 8 Applications of Derivatives | [77](calculus/calculus-practice-problems.pdf#page=77) |
| 9 Areas and Riemann Sums | [89](calculus/calculus-practice-problems.pdf#page=89) |
| 10 The Fundamental Theorem of Calculus and the Net Change Theorem | [93](calculus/calculus-practice-problems.pdf#page=93) |
| 11 Applications of Integration | [101](calculus/calculus-practice-problems.pdf#page=101) |
| 12 Inverse Trigonometric Functions, Hyperbolic Functions, and L’Hôpital’s Rule | [113](calculus/calculus-practice-problems.pdf#page=113) |
| 13 U-Substitution and Integration by Parts | [121](calculus/calculus-practice-problems.pdf#page=121) |
| 14 Trigonometric Integrals, Trigonometric Substitution, and Partial Fractions | [127](calculus/calculus-practice-problems.pdf#page=127) |
| 15 Improper Integrals and More Approximating Techniques | [135](calculus/calculus-practice-problems.pdf#page=135) |
| Part II: The Answers | [139](calculus/calculus-practice-problems.pdf#page=139) |
| 16 Answers and Explanations | [141](calculus/calculus-practice-problems.pdf#page=141) |

### Integration and series notes

`calculus/integration-and-series-notes.pdf`, 127 pages. *2nd Semester Calculus Lecture Manual*,
MATH1036/7, University of the Witwatersrand, 2013. Lecture notes, numbered from chapter 7: hyperbolic
functions, the definite integral, integration techniques, improper integrals, sequences and series.
Was `Calculus Semester 2 Notes.pdf`. No embedded outline; this table is from the printed contents. The
printed page number is the PDF page minus 2.

| Chapter | PDF page |
| --- | --- |
| 7 Hyperbolic Functions | [3](calculus/integration-and-series-notes.pdf#page=3) |
| 8 Integration Theory and Applications | [4](calculus/integration-and-series-notes.pdf#page=4) |
| 8.1 Riemann Sums and Area Approximation | [4](calculus/integration-and-series-notes.pdf#page=4) |
| 8.2 Area with the Definite Integral | [12](calculus/integration-and-series-notes.pdf#page=12) |
| 8.3 Solids of Revolution | [26](calculus/integration-and-series-notes.pdf#page=26) |
| 8.4 Volumes by Slicing | [37](calculus/integration-and-series-notes.pdf#page=37) |
| 8.5 The Definite Integral as a Function | [41](calculus/integration-and-series-notes.pdf#page=41) |
| 9 Advanced Integration Techniques | [45](calculus/integration-and-series-notes.pdf#page=45) |
| 9.1 Inverse Trigonometric, Exponential and Logarithmic Integrals | [45](calculus/integration-and-series-notes.pdf#page=45) |
| 9.2 Integration by Parts Revisited | [50](calculus/integration-and-series-notes.pdf#page=50) |
| 9.3 Trigonometric Substitutions | [53](calculus/integration-and-series-notes.pdf#page=53) |
| 9.4 Trigonometric Integrals | [57](calculus/integration-and-series-notes.pdf#page=57) |
| 9.5 Partial Fraction Decomposition | [64](calculus/integration-and-series-notes.pdf#page=64) |
| 10 Improper Integrals | [75](calculus/integration-and-series-notes.pdf#page=75) |
| 10.1 Type I: Infinite Interval of Integration | [76](calculus/integration-and-series-notes.pdf#page=76) |
| 10.2 Type II: Infinite Discontinuities | [81](calculus/integration-and-series-notes.pdf#page=81) |
| 11 Infinite Sequences and Series | [87](calculus/integration-and-series-notes.pdf#page=87) |
| 11.1 Sequences | [87](calculus/integration-and-series-notes.pdf#page=87) |
| 11.2 Series | [92](calculus/integration-and-series-notes.pdf#page=92) |
| 11.3 Convergence Tests for Series | [96](calculus/integration-and-series-notes.pdf#page=96) |

### The gamma function

`calculus/gamma-function.pdf`, 5 pages. Own notes from the Mathematical Statistics series, 2 September
2021: the gamma function and a proof by induction that Γ(n) = (n − 1)!. Was `Gamma Function.pdf`.

## statistics/

### Introduction to statistics

`statistics/introduction-to-statistics.pdf`, 148 pages. Charles Chimedza and Nothabo Ndebele, *An
Introduction to Mathematical Statistics*, STAT2012 lecture notes, University of the Witwatersrand, 5 July
2016. Lecture notes: descriptive statistics, probability, random variables, estimation, confidence
intervals, hypothesis tests and simple regression. No embedded outline; this table is from the printed
contents. The printed page number is the PDF page minus 1.

| Chapter | PDF page |
| --- | --- |
| 1 Introduction to Mathematical Statistics | [10](statistics/introduction-to-statistics.pdf#page=10) |
| 1.3 Populations and Samples | [11](statistics/introduction-to-statistics.pdf#page=11) |
| 2 Descriptive Statistics | [18](statistics/introduction-to-statistics.pdf#page=18) |
| 2.2 Graphical Techniques | [18](statistics/introduction-to-statistics.pdf#page=18) |
| 2.3 Summary Statistics | [40](statistics/introduction-to-statistics.pdf#page=40) |
| 2.4 Measures of Location | [40](statistics/introduction-to-statistics.pdf#page=40) |
| 2.5 Box-and-Whisker Plot | [49](statistics/introduction-to-statistics.pdf#page=49) |
| 2.6 Measures of Dispersion | [50](statistics/introduction-to-statistics.pdf#page=50) |
| 3 Introduction to Probability | [54](statistics/introduction-to-statistics.pdf#page=54) |
| 3.4 Counting Methods: Permutations and Combinations | [59](statistics/introduction-to-statistics.pdf#page=59) |
| 3.5 Rules Governing Probability (Axioms) | [64](statistics/introduction-to-statistics.pdf#page=64) |
| 3.7 The Classical Approach | [66](statistics/introduction-to-statistics.pdf#page=66) |
| 4 Random Variables and Distributions | [80](statistics/introduction-to-statistics.pdf#page=80) |
| 4.2 Discrete Random Variables | [80](statistics/introduction-to-statistics.pdf#page=80) |
| 4.3 Moments and Moment Generating Functions of Discrete Random Variables | [82](statistics/introduction-to-statistics.pdf#page=82) |
| 4.4 Continuous Random Variables | [83](statistics/introduction-to-statistics.pdf#page=83) |
| 4.5 Empirical Distributions | [86](statistics/introduction-to-statistics.pdf#page=86) |
| 4.6 Some Discrete Distributions | [87](statistics/introduction-to-statistics.pdf#page=87) |
| 4.7 Some Common Continuous Empirical Distributions | [90](statistics/introduction-to-statistics.pdf#page=90) |
| 4.8 Memoryless Property | [92](statistics/introduction-to-statistics.pdf#page=92) |
| 5 Estimation and Hypothesis Testing | [96](statistics/introduction-to-statistics.pdf#page=96) |
| 5.2 Estimation | [96](statistics/introduction-to-statistics.pdf#page=96) |
| 5.3 Confidence Intervals | [99](statistics/introduction-to-statistics.pdf#page=99) |
| 5.4 Sampling to a Desired Precision | [103](statistics/introduction-to-statistics.pdf#page=103) |
| 5.5 Hypothesis Testing | [105](statistics/introduction-to-statistics.pdf#page=105) |
| 6 Introduction to Correlation and Regression Analysis | [116](statistics/introduction-to-statistics.pdf#page=116) |
| 6.3 Correlation | [117](statistics/introduction-to-statistics.pdf#page=117) |
| 6.4 Simple Linear Regression Analysis | [120](statistics/introduction-to-statistics.pdf#page=120) |
| 6.7 The Least Squares Technique | [128](statistics/introduction-to-statistics.pdf#page=128) |
| 6.9 Making Inferences about β0 and β1 | [133](statistics/introduction-to-statistics.pdf#page=133) |
