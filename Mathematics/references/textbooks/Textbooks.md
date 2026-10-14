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
| the Jacobian as the m by n matrix of first-order partial derivatives (Definition 5.6) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=156) | 156 |
| gradients of matrices, and of vector-valued functions | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=155) | 155 |
| sum rule and marginalisation; product rule and Bayes' theorem | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=190) | 190 |
| the marginal likelihood (evidence) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=192) | 192 |
| mean, expected value, variance | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=193) | 193 |
| covariance (Definition 6.5) | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=196) | 196 |
| the Gaussian distribution | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=203) | 203 |
| change of variables for densities | [mathematics for machine learning](machine-learning/mathematics-for-machine-learning.pdf#page=220) | 220 |
| what a vector field is (Definition 15.1.1) | [calculus textbook](calculus/calculus-textbook.pdf#page=1109) | 1109 |
| gradient fields: a field that is the gradient of a function | [calculus textbook](calculus/calculus-textbook.pdf#page=1111) | 1111 |
| expectation (discrete): the definition, why it is the dataset average, with figure (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=141) | 141 |
| expectation (continuous): the integral definition with uniform and exponential worked examples | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=196) | 196 |
| conditional expectation: the definition for discrete and continuous variables | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=291) | 291 |
| conditional expectation: law of total expectation, with proof | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=292) | 292 |
| conditional expectation: E[X] = E[E[X|Y]] with a worked two-class example | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=293) | 293 |
| variance (continuous): the definition and the E[X²] − μ² shortcut, with proof | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=200) | 200 |
| variance: worked example for the uniform distribution | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=201) | 201 |
| covariance: the definition, and Cov(X, Y) = E[XY] − E[X]E[Y] with proof | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=278) | 278 |
| covariance: why joint expectation is E[XY], through the angle between two vectors (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=274) | 274 |
| conditional probability: the definition P[A|B] = P[A ∩ B] / P[B], with intuition | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=97) | 97 |
| Bayes' rule: the theorem with proof, plus the law of total probability | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=105) | 105 |
| Bayes' rule: worked examples (winning a match against three player types, a noisy channel) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=107) | 107 |
| the Gaussian distribution: the density and its two parameters, mean and variance | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=227) | 227 |
| the Gaussian distribution: plots of how μ and σ move and widen the curve (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=228) | 228 |
| the multivariate Gaussian: the d-dimensional density with Σ⁻¹ (definition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=306) | 306 |
| the multivariate Gaussian: its mean vector and covariance matrix, the diagonal case | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=307) | 307 |
| hypothesis testing: null and alternative hypotheses, the courtroom picture (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=582) | 582 |
| hypothesis testing: a worked die example with an estimator | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=583) | 583 |
| hypothesis testing: the p-value, with a worked number | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=588) | 588 |
| maximum likelihood estimation: the likelihood function from the joint density (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=484) | 484 |
| maximum likelihood estimation: the i.i.d. likelihood and log-likelihood | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=486) | 486 |
| maximum likelihood estimation: the ML estimate, with a Bernoulli worked example | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=489) | 489 |
| law of large numbers: the sample average and its mean | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=367) | 367 |
| law of large numbers: the weak law, with proof by Chebyshev | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=370) | 370 |
| central limit theorem: the dice picture and what the theorem says (intuition) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=382) | 382 |
| central limit theorem: the theorem statement (Theorem 6.19) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=388) | 388 |
| joint distribution: the joint PMF, with figure | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=262) | 262 |
| marginal distribution: the marginal PMF and PDF by summing or integrating out one variable | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=266) | 266 |
| conditional distribution: the conditional PMF p(x|y) = p(x, y) / p(y) | [probability for data science](statistics/introduction-to-probability-for-data-science.pdf#page=283) | 283 |
| backpropagation: the chain rule over a computational graph, then the algorithm (sections 6.5.1 to 6.5.4) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=220) | 220 |
| backpropagation: the algorithm for a fully-connected net (Algorithm 6.2 on PDF page 226, forward and backward passes 6.3 and 6.4 on 228 and 229) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=226) | 226 |
| backpropagation worked on a small network, then the algorithm and its summary (section 7.4; summary on page 120) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=117) | 117 |
| the score and score matching: what the score is and why matching it avoids the partition function (section 18.4 starts here) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=633) | 633 |
| denoising score matching: fitting the score of a noise-corrupted data distribution (section 18.5) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=635) | 635 |
| energy-based models: p̃(x) = exp(−E(x)), equation 16.7 | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=585) | 585 |
| Markov chain Monte Carlo: why a Markov chain is used to sample from p_model (section 17.3) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=611) | 611 |
| Metropolis-Hastings: named in a single sentence as an alternative to Gibbs sampling, with no derivation | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=615) | 615 |
| diffusion models: the overview and what the encoder and decoder do (chapter 18) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=362) | 362 |
| diffusion models: the forward process that adds noise (section 18.2) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=363) | 363 |
| diffusion models: the reverse process, starting from Bayes' rule on the forward step (section 18.3) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=369) | 369 |
| diffusion models: training and the loss (section 18.4) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=370) | 370 |
| the Gaussian, univariate: the density and its mean and variance (section 3.9.3) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=79) | 79 |
| the Gaussian, univariate: the density with parameters µ and σ² (equation C.21) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=470) | 470 |
| the multivariate Gaussian: spherical, diagonal and full covariance, drawn as contours | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=471) | 471 |
| KL divergence: definition and non-negativity (equation 3.50) | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=90) | 90 |
| KL divergence: definition for densities (equation C.28) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=474) | 474 |
| cross-entropy: H(P, Q) = H(P) + D_KL(P‖Q), equation 3.51 | [deep learning textbook](machine-learning/deep-learning-textbook.pdf#page=91) | 91 |
| cross-entropy loss: fitting a model by minimising the distance to the empirical distribution, equal to negative log-likelihood (section 5.7) | [understanding deep learning](machine-learning/understanding-deep-learning.pdf#page=85) | 85 |

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
| 14.7 Change of Variables in Multiple Integrals; Jacobians | [1083](calculus/calculus-textbook.pdf#page=1083) |
| 14.8 Centers of Gravity Using Multiple Integrals | [1095](calculus/calculus-textbook.pdf#page=1095) |
| 15 Topics in Vector Calculus | [1108](calculus/calculus-textbook.pdf#page=1108) |
| 15.1 Vector Fields | [1109](calculus/calculus-textbook.pdf#page=1109) |
| Gradient fields and conservative fields (15.1.3) | [1111](calculus/calculus-textbook.pdf#page=1111) |
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

### Calculus handbook

`calculus/calculus-handbook.pdf`, 242 pages. Earl, *Calculus Handbook*, version 5.6. A compact handbook for a
first-year course: limits, differentiation and its rules, integration techniques, hyperbolic functions,
definite and improper integrals, differential equations, vector calculus, series, and appendices of key
definitions, theorems and formulas. The printed page number equals the PDF page number. The table is from
the book's own contents pages.

| Chapter or topic | PDF page |
| --- | --- |
| 1 Functions and Limits | [8](calculus/calculus-handbook.pdf#page=8) |
| Functions | [8](calculus/calculus-handbook.pdf#page=8) |
| Continuity Examples | [10](calculus/calculus-handbook.pdf#page=10) |
| Limits | [11](calculus/calculus-handbook.pdf#page=11) |
| Techniques for Finding Limits | [12](calculus/calculus-handbook.pdf#page=12) |
| Indeterminate Forms | [14](calculus/calculus-handbook.pdf#page=14) |
| When Limits Fail to Exist | [16](calculus/calculus-handbook.pdf#page=16) |
| 2 Differentiation | [17](calculus/calculus-handbook.pdf#page=17) |
| Definition, Basic Rules, Product Rule | [17](calculus/calculus-handbook.pdf#page=17) |
| Quotient, Chain and Power Rules; Exponential and Logarithmic Functions | [18](calculus/calculus-handbook.pdf#page=18) |
| Trigonometric and Inverse Trigonometric Functions | [19](calculus/calculus-handbook.pdf#page=19) |
| Generalized Product Rule | [23](calculus/calculus-handbook.pdf#page=23) |
| Inverse Function Rule | [25](calculus/calculus-handbook.pdf#page=25) |
| Partial Differentiation | [26](calculus/calculus-handbook.pdf#page=26) |
| Implicit Differentiation | [27](calculus/calculus-handbook.pdf#page=27) |
| Logarithmic Differentiation | [30](calculus/calculus-handbook.pdf#page=30) |
| 3 Applications of Derivatives | [31](calculus/calculus-handbook.pdf#page=31) |
| Maxima and Minima (i.e., Extrema) | [31](calculus/calculus-handbook.pdf#page=31) |
| Inflection Points | [33](calculus/calculus-handbook.pdf#page=33) |
| Special Case: Extrema and Inflection Points of Polynomials | [34](calculus/calculus-handbook.pdf#page=34) |
| Relationship Among f(x), f'(x) and f''(x) | [35](calculus/calculus-handbook.pdf#page=35) |
| Curve Sketching | [39](calculus/calculus-handbook.pdf#page=39) |
| Determining the Shape of a Curve Based On Its Derivatives | [44](calculus/calculus-handbook.pdf#page=44) |
| Rolles's Theorem and the Mean Value Theorem (MVT) | [45](calculus/calculus-handbook.pdf#page=45) |
| Related Rates | [46](calculus/calculus-handbook.pdf#page=46) |
| Kinematics (Particle Motion) | [49](calculus/calculus-handbook.pdf#page=49) |
| Differentials | [52](calculus/calculus-handbook.pdf#page=52) |
| Curvature | [53](calculus/calculus-handbook.pdf#page=53) |
| Newton's Method | [54](calculus/calculus-handbook.pdf#page=54) |
| 4 Integration | [56](calculus/calculus-handbook.pdf#page=56) |
| Indefinite Integration (Antiderivatives) | [56](calculus/calculus-handbook.pdf#page=56) |
| Exponential and Logarithmic Functions | [57](calculus/calculus-handbook.pdf#page=57) |
| Trigonometric Functions | [57](calculus/calculus-handbook.pdf#page=57) |
| Inverse Trigonometric Functions | [60](calculus/calculus-handbook.pdf#page=60) |
| Selecting the Right Function for an Intergral | [62](calculus/calculus-handbook.pdf#page=62) |
| 5 Techniques of Integration | [63](calculus/calculus-handbook.pdf#page=63) |
| u -Substitution | [63](calculus/calculus-handbook.pdf#page=63) |
| Integration by Partial Fractions | [65](calculus/calculus-handbook.pdf#page=65) |
| Integration by Parts | [68](calculus/calculus-handbook.pdf#page=68) |
| Integration by Trigonometric Substitution | [72](calculus/calculus-handbook.pdf#page=72) |
| Gamma Function | [74](calculus/calculus-handbook.pdf#page=74) |
| Beta Function | [76](calculus/calculus-handbook.pdf#page=76) |
| Impossible Integrals | [78](calculus/calculus-handbook.pdf#page=78) |
| 6 Hyperbolic Functions | [79](calculus/calculus-handbook.pdf#page=79) |
| Definitions | [79](calculus/calculus-handbook.pdf#page=79) |
| Identities | [80](calculus/calculus-handbook.pdf#page=80) |
| Relationship to Trigonometric Functions | [81](calculus/calculus-handbook.pdf#page=81) |
| Inverse Hyperbolic Functions | [82](calculus/calculus-handbook.pdf#page=82) |
| Graphs of Hyperbolic Functions and Their Inverses | [83](calculus/calculus-handbook.pdf#page=83) |
| Derivatives | [84](calculus/calculus-handbook.pdf#page=84) |
| Integrals | [85](calculus/calculus-handbook.pdf#page=85) |
| 7 Definite Integrals | [87](calculus/calculus-handbook.pdf#page=87) |
| Riemann Sums | [87](calculus/calculus-handbook.pdf#page=87) |
| Rules of Definite Integration | [92](calculus/calculus-handbook.pdf#page=92) |
| Fundamental Theorems of Calculus | [92](calculus/calculus-handbook.pdf#page=92) |
| Properties of Definite Integrals | [94](calculus/calculus-handbook.pdf#page=94) |
| Solving Definite Integrals with Directed Line Segments | [95](calculus/calculus-handbook.pdf#page=95) |
| u -Subsitution | [96](calculus/calculus-handbook.pdf#page=96) |
| Special Techniques for Evaluation | [98](calculus/calculus-handbook.pdf#page=98) |
| Derivative of an Integral | [100](calculus/calculus-handbook.pdf#page=100) |
| 8 Applications of Integration | [101](calculus/calculus-handbook.pdf#page=101) |
| Area Under a Curve | [101](calculus/calculus-handbook.pdf#page=101) |
| Area Between Curves | [102](calculus/calculus-handbook.pdf#page=102) |
| Area in Polar Form | [103](calculus/calculus-handbook.pdf#page=103) |
| Areas of Limacons | [105](calculus/calculus-handbook.pdf#page=105) |
| Arc Length | [107](calculus/calculus-handbook.pdf#page=107) |
| Comparison of Formulas for Rectangular, Polar and Parametric Forms | [110](calculus/calculus-handbook.pdf#page=110) |
| Area of a Surface of Revolution | [111](calculus/calculus-handbook.pdf#page=111) |
| Volumes of Solids of Revolution | [112](calculus/calculus-handbook.pdf#page=112) |
| 9 Improper Integrals | [118](calculus/calculus-handbook.pdf#page=118) |
| Definite Integrals with Infinite Limits of Integration | [118](calculus/calculus-handbook.pdf#page=118) |
| Definite Integrals with Discontinuous Integrands | [119](calculus/calculus-handbook.pdf#page=119) |
| 10 Differential Equations | [120](calculus/calculus-handbook.pdf#page=120) |
| Definitions | [120](calculus/calculus-handbook.pdf#page=120) |
| Separable First Order Differential Equations | [121](calculus/calculus-handbook.pdf#page=121) |
| Slope Fields | [123](calculus/calculus-handbook.pdf#page=123) |
| Logistic Function | [124](calculus/calculus-handbook.pdf#page=124) |
| Numerical Methods | [125](calculus/calculus-handbook.pdf#page=125) |
| 11 Vector Calculus | [129](calculus/calculus-handbook.pdf#page=129) |
| Introduction | [129](calculus/calculus-handbook.pdf#page=129) |
| Special Unit Vectors | [129](calculus/calculus-handbook.pdf#page=129) |
| Vector Components | [129](calculus/calculus-handbook.pdf#page=129) |
| Properties of Vectors | [130](calculus/calculus-handbook.pdf#page=130) |
| Dot Product | [131](calculus/calculus-handbook.pdf#page=131) |
| Cross Product | [132](calculus/calculus-handbook.pdf#page=132) |
| Triple Products | [134](calculus/calculus-handbook.pdf#page=134) |
| Kinematics (Particle Motion) | [135](calculus/calculus-handbook.pdf#page=135) |
| Gradient | [136](calculus/calculus-handbook.pdf#page=136) |
| Divergence | [137](calculus/calculus-handbook.pdf#page=137) |
| Curl | [138](calculus/calculus-handbook.pdf#page=138) |
| Laplacian | [139](calculus/calculus-handbook.pdf#page=139) |
| 12 Sequences | [140](calculus/calculus-handbook.pdf#page=140) |
| Definitions and Types of Sequences | [140](calculus/calculus-handbook.pdf#page=140) |
| More Definitions and Theorems | [141](calculus/calculus-handbook.pdf#page=141) |
| Limits (Convergence and Divergence) | [142](calculus/calculus-handbook.pdf#page=142) |
| Basic Recursive Sequence Theory | [143](calculus/calculus-handbook.pdf#page=143) |
| 13 Series | [147](calculus/calculus-handbook.pdf#page=147) |
| Introduction | [147](calculus/calculus-handbook.pdf#page=147) |
| Key Properties | [148](calculus/calculus-handbook.pdf#page=148) |
| n-th Term Convergence Theorems | [148](calculus/calculus-handbook.pdf#page=148) |
| Power Series | [148](calculus/calculus-handbook.pdf#page=148) |
| Telescoping Series | [149](calculus/calculus-handbook.pdf#page=149) |
| Geometric Series | [150](calculus/calculus-handbook.pdf#page=150) |
| Estimating the Value of Series with Positive Terms | [151](calculus/calculus-handbook.pdf#page=151) |
| Riemann Zeta Function (p -Series) | [152](calculus/calculus-handbook.pdf#page=152) |
| Bernoulli Numbers | [156](calculus/calculus-handbook.pdf#page=156) |
| Convergence Tests | [158](calculus/calculus-handbook.pdf#page=158) |
| Alternating Series | [163](calculus/calculus-handbook.pdf#page=163) |
| Radius and Interval of Convergence of Power Series | [165](calculus/calculus-handbook.pdf#page=165) |
| Summary of Convergence/Divergence Tests | [168](calculus/calculus-handbook.pdf#page=168) |
| 14 Taylor and MacLaurin Series | [169](calculus/calculus-handbook.pdf#page=169) |
| Taylor Series | [169](calculus/calculus-handbook.pdf#page=169) |
| MacLaurin Series | [169](calculus/calculus-handbook.pdf#page=169) |
| LaGrange Remainder | [171](calculus/calculus-handbook.pdf#page=171) |
| 15 Miscellaneous Cool Stuff | [172](calculus/calculus-handbook.pdf#page=172) |
| e | [172](calculus/calculus-handbook.pdf#page=172) |
| Derivation of Euler's Formula | [173](calculus/calculus-handbook.pdf#page=173) |
| Logarithms of Negative Real Numbers and Complex Numbers | [175](calculus/calculus-handbook.pdf#page=175) |
| What Is i | [176](calculus/calculus-handbook.pdf#page=176) |
| z | [177](calculus/calculus-handbook.pdf#page=177) |
| Derivatives of a Circle | [178](calculus/calculus-handbook.pdf#page=178) |
| Derivatives of a Ellipse | [179](calculus/calculus-handbook.pdf#page=179) |
| Derivatives of a Hyperbola | [180](calculus/calculus-handbook.pdf#page=180) |
| 3 3 3 | [181](calculus/calculus-handbook.pdf#page=181) |
| Inflection Points of the PDF of the Normal Distribution | [182](calculus/calculus-handbook.pdf#page=182) |
| Appendix A: Key Definitions | [183](calculus/calculus-handbook.pdf#page=183) |
| Appendix B: Key Theorems | [203](calculus/calculus-handbook.pdf#page=203) |
| Appendix C: List of Key Derivatives and Integrals | [207](calculus/calculus-handbook.pdf#page=207) |
| Appendix D: Key Functions and Their Derivatives | [214](calculus/calculus-handbook.pdf#page=214) |
| Appendix E: Geometry and Trigonometry Formulas | [218](calculus/calculus-handbook.pdf#page=218) |
| Appendix F: Polar and Parametric Equations | [223](calculus/calculus-handbook.pdf#page=223) |
| Appendix G: Interesting Series | [234](calculus/calculus-handbook.pdf#page=234) |
| Index | [235](calculus/calculus-handbook.pdf#page=235) |
| Appendix A Key Definitions | [183](calculus/calculus-handbook.pdf#page=183) |
| Appendix B Key Theorems | [203](calculus/calculus-handbook.pdf#page=203) |
| Appendix C Key Derivatives and Integrals | [207](calculus/calculus-handbook.pdf#page=207) |
| Appendix D Functions and Their Derivatives | [215](calculus/calculus-handbook.pdf#page=215) |
| Appendix E Geometry and Trigonometry Formulas | [218](calculus/calculus-handbook.pdf#page=218) |

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

### Introduction to probability for data science

`statistics/introduction-to-probability-for-data-science.pdf`, 709 pages. Stanley H. Chan, *Introduction to Probability for Data Science*, Michigan Publishing,
2021 (Purdue University; free electronic edition, first edition). A first course in probability written
for data science: each idea comes with a figure, a plain-words summary box ("What is conditional
expectation?") and a worked example, and the proofs are kept short. Chapters 1 to 5 build probability,
random variables and joint distributions; 6 to 9 cover sample statistics, the law of large numbers and
the central limit theorem, regression, maximum-likelihood and MAP estimation, confidence intervals and
hypothesis tests; 10 is random processes. Was `Introduction to Probability for Data Science (Stanley
Chan) (Z-Library).pdf`. The embedded outline lists sections without numbers; the numbers below follow
the printed contents. The printed page number is the PDF page minus 16.

| Chapter or section | PDF page |
| --- | --- |
| 1 Mathematical Background | [17](statistics/introduction-to-probability-for-data-science.pdf#page=17) |
| 1.1 Infinite Series | [18](statistics/introduction-to-probability-for-data-science.pdf#page=18) |
| 1.2 Approximation | [26](statistics/introduction-to-probability-for-data-science.pdf#page=26) |
| 1.3 Integration | [31](statistics/introduction-to-probability-for-data-science.pdf#page=31) |
| 1.4 Linear Algebra | [36](statistics/introduction-to-probability-for-data-science.pdf#page=36) |
| 1.5 Basic Combinatorics | [47](statistics/introduction-to-probability-for-data-science.pdf#page=47) |
| 2 Probability | [59](statistics/introduction-to-probability-for-data-science.pdf#page=59) |
| 2.1 Set Theory | [60](statistics/introduction-to-probability-for-data-science.pdf#page=60) |
| 2.2 Probability Space | [74](statistics/introduction-to-probability-for-data-science.pdf#page=74) |
| 2.3 Axioms of Probability | [90](statistics/introduction-to-probability-for-data-science.pdf#page=90) |
| 2.4 Conditional Probability | [96](statistics/introduction-to-probability-for-data-science.pdf#page=96) |
| 3 Discrete Random Variables | [119](statistics/introduction-to-probability-for-data-science.pdf#page=119) |
| 3.1 Random Variables | [121](statistics/introduction-to-probability-for-data-science.pdf#page=121) |
| 3.2 Probability Mass Function | [126](statistics/introduction-to-probability-for-data-science.pdf#page=126) |
| 3.3 Cumulative Distribution Functions (Discrete) | [137](statistics/introduction-to-probability-for-data-science.pdf#page=137) |
| 3.4 Expectation | [141](statistics/introduction-to-probability-for-data-science.pdf#page=141) |
| 3.5 Common Discrete Random Variables | [152](statistics/introduction-to-probability-for-data-science.pdf#page=152) |
| 4 Continuous Random Variables | [187](statistics/introduction-to-probability-for-data-science.pdf#page=187) |
| 4.1 Probability Density Function | [188](statistics/introduction-to-probability-for-data-science.pdf#page=188) |
| 4.2 Expectation, Moment, and Variance | [196](statistics/introduction-to-probability-for-data-science.pdf#page=196) |
| 4.3 Cumulative Distribution Function | [201](statistics/introduction-to-probability-for-data-science.pdf#page=201) |
| 4.4 Median, Mode, and Mean | [212](statistics/introduction-to-probability-for-data-science.pdf#page=212) |
| 4.5 Uniform and Exponential Random Variables | [217](statistics/introduction-to-probability-for-data-science.pdf#page=217) |
| 4.6 Gaussian Random Variables | [227](statistics/introduction-to-probability-for-data-science.pdf#page=227) |
| 4.7 Functions of Random Variables | [239](statistics/introduction-to-probability-for-data-science.pdf#page=239) |
| 4.8 Generating Random Numbers | [245](statistics/introduction-to-probability-for-data-science.pdf#page=245) |
| 5 Joint Distributions | [257](statistics/introduction-to-probability-for-data-science.pdf#page=257) |
| 5.1 Joint PMF and Joint PDF | [260](statistics/introduction-to-probability-for-data-science.pdf#page=260) |
| 5.2 Joint Expectation | [273](statistics/introduction-to-probability-for-data-science.pdf#page=273) |
| 5.3 Conditional PMF and PDF | [282](statistics/introduction-to-probability-for-data-science.pdf#page=282) |
| 5.4 Conditional Expectation | [291](statistics/introduction-to-probability-for-data-science.pdf#page=291) |
| 5.5 Sum of Two Random Variables | [296](statistics/introduction-to-probability-for-data-science.pdf#page=296) |
| 5.6 Random Vectors and Covariance Matrices | [302](statistics/introduction-to-probability-for-data-science.pdf#page=302) |
| 5.7 Transformation of Multidimensional Gaussians | [309](statistics/introduction-to-probability-for-data-science.pdf#page=309) |
| 5.8 Principal-Component Analysis | [319](statistics/introduction-to-probability-for-data-science.pdf#page=319) |
| 6 Sample Statistics | [335](statistics/introduction-to-probability-for-data-science.pdf#page=335) |
| 6.1 Moment-Generating and Characteristic Functions | [340](statistics/introduction-to-probability-for-data-science.pdf#page=340) |
| 6.2 Probability Inequalities | [349](statistics/introduction-to-probability-for-data-science.pdf#page=349) |
| 6.3 Law of Large Numbers | [367](statistics/introduction-to-probability-for-data-science.pdf#page=367) |
| 6.4 Central Limit Theorem | [382](statistics/introduction-to-probability-for-data-science.pdf#page=382) |
| 7 Regression | [405](statistics/introduction-to-probability-for-data-science.pdf#page=405) |
| 7.1 Principles of Regression | [410](statistics/introduction-to-probability-for-data-science.pdf#page=410) |
| 7.2 Overfitting | [434](statistics/introduction-to-probability-for-data-science.pdf#page=434) |
| 7.3 Bias and Variance Trade-Off | [445](statistics/introduction-to-probability-for-data-science.pdf#page=445) |
| 7.4 Regularization | [456](statistics/introduction-to-probability-for-data-science.pdf#page=456) |
| 8 Estimation | [481](statistics/introduction-to-probability-for-data-science.pdf#page=481) |
| 8.1 Maximum-Likelihood Estimation | [484](statistics/introduction-to-probability-for-data-science.pdf#page=484) |
| 8.2 Properties of ML Estimates | [507](statistics/introduction-to-probability-for-data-science.pdf#page=507) |
| 8.3 Maximum A Posteriori Estimation | [518](statistics/introduction-to-probability-for-data-science.pdf#page=518) |
| 8.4 Minimum Mean-Square Estimation | [536](statistics/introduction-to-probability-for-data-science.pdf#page=536) |
| 9 Confidence and Hypothesis | [557](statistics/introduction-to-probability-for-data-science.pdf#page=557) |
| 9.1 Confidence Interval | [559](statistics/introduction-to-probability-for-data-science.pdf#page=559) |
| 9.2 Bootstrapping | [575](statistics/introduction-to-probability-for-data-science.pdf#page=575) |
| 9.3 Hypothesis Testing | [582](statistics/introduction-to-probability-for-data-science.pdf#page=582) |
| 9.4 Neyman-Pearson Test | [593](statistics/introduction-to-probability-for-data-science.pdf#page=593) |
| 9.5 ROC and Precision-Recall Curve | [605](statistics/introduction-to-probability-for-data-science.pdf#page=605) |
| 10 Random Processes | [627](statistics/introduction-to-probability-for-data-science.pdf#page=627) |
| 10.1 Basic Concepts | [628](statistics/introduction-to-probability-for-data-science.pdf#page=628) |
| 10.2 Mean and Correlation Functions | [634](statistics/introduction-to-probability-for-data-science.pdf#page=634) |
| 10.3 Wide-Sense Stationary Processes | [646](statistics/introduction-to-probability-for-data-science.pdf#page=646) |
| 10.4 Power Spectral Density | [652](statistics/introduction-to-probability-for-data-science.pdf#page=652) |
| 10.5 WSS Process through LTI Systems | [659](statistics/introduction-to-probability-for-data-science.pdf#page=659) |
| 10.6 Optimal Linear Filter | [669](statistics/introduction-to-probability-for-data-science.pdf#page=669) |
| Appendix to chapter 10 | [686](statistics/introduction-to-probability-for-data-science.pdf#page=686) |
| Appendix | [697](statistics/introduction-to-probability-for-data-science.pdf#page=697) |

## machine-learning/

### Mathematics for machine learning

`machine-learning/mathematics-for-machine-learning.pdf`, 417 pages. Marc Peter Deisenroth, A. Aldo Faisal
and Cheng Soon Ong, *Mathematics for Machine Learning*, draft of 15 October 2019, Cambridge University
Press. Part I covers the foundations: linear algebra, analytic geometry, matrix decompositions, vector
calculus, probability and distributions, continuous optimisation. Part II applies them to linear
regression, dimensionality reduction, density estimation and classification. The printed page number is
the PDF page minus 6. The table is from the PDF's own outline, with each section's page found from its
heading in the text; Part II is listed down to the chapters and their first sections.

| Chapter or section | PDF page |
| --- | --- |
| 1 Introduction and Motivation | [17](machine-learning/mathematics-for-machine-learning.pdf#page=17) |
| 1.1 Finding Words for Intuitions | [18](machine-learning/mathematics-for-machine-learning.pdf#page=18) |
| 1.2 Two Ways to Read This Book | [19](machine-learning/mathematics-for-machine-learning.pdf#page=19) |
| 1.3 Exercises and Feedback | [22](machine-learning/mathematics-for-machine-learning.pdf#page=22) |
| 2 Linear Algebra | [23](machine-learning/mathematics-for-machine-learning.pdf#page=23) |
| 2.1 Systems of Linear Equations | [25](machine-learning/mathematics-for-machine-learning.pdf#page=25) |
| 2.2 Matrices | [28](machine-learning/mathematics-for-machine-learning.pdf#page=28) |
| 2.3 Solving Systems of Linear Equations | [33](machine-learning/mathematics-for-machine-learning.pdf#page=33) |
| 2.4 Vector Spaces | [41](machine-learning/mathematics-for-machine-learning.pdf#page=41) |
| 2.5 Linear Independence | [46](machine-learning/mathematics-for-machine-learning.pdf#page=46) |
| 2.6 Basis and Rank | [50](machine-learning/mathematics-for-machine-learning.pdf#page=50) |
| 2.7 Linear Mappings | [54](machine-learning/mathematics-for-machine-learning.pdf#page=54) |
| 2.8 Affine Spaces | [67](machine-learning/mathematics-for-machine-learning.pdf#page=67) |
| 3 Analytic Geometry | [76](machine-learning/mathematics-for-machine-learning.pdf#page=76) |
| 3.1 Norms | [77](machine-learning/mathematics-for-machine-learning.pdf#page=77) |
| 3.2 Inner Products | [78](machine-learning/mathematics-for-machine-learning.pdf#page=78) |
| 3.3 Lengths and Distances | [81](machine-learning/mathematics-for-machine-learning.pdf#page=81) |
| 3.4 Angles and Orthogonality | [82](machine-learning/mathematics-for-machine-learning.pdf#page=82) |
| 3.5 Orthonormal Basis | [84](machine-learning/mathematics-for-machine-learning.pdf#page=84) |
| 3.6 Orthogonal Complement | [85](machine-learning/mathematics-for-machine-learning.pdf#page=85) |
| 3.7 Inner Product of Functions | [86](machine-learning/mathematics-for-machine-learning.pdf#page=86) |
| 3.8 Orthogonal Projections | [87](machine-learning/mathematics-for-machine-learning.pdf#page=87) |
| 3.9 Rotations | [97](machine-learning/mathematics-for-machine-learning.pdf#page=97) |
| 4 Matrix Decompositions | [104](machine-learning/mathematics-for-machine-learning.pdf#page=104) |
| 4.1 Determinant and Trace | [105](machine-learning/mathematics-for-machine-learning.pdf#page=105) |
| 4.2 Eigenvalues and Eigenvectors | [111](machine-learning/mathematics-for-machine-learning.pdf#page=111) |
| 4.3 Cholesky Decomposition | [120](machine-learning/mathematics-for-machine-learning.pdf#page=120) |
| 4.4 Eigendecomposition and Diagonalization | [121](machine-learning/mathematics-for-machine-learning.pdf#page=121) |
| 4.5 Singular Value Decomposition | [125](machine-learning/mathematics-for-machine-learning.pdf#page=125) |
| 4.6 Matrix Approximation | [135](machine-learning/mathematics-for-machine-learning.pdf#page=135) |
| 4.7 Matrix Phylogeny | [140](machine-learning/mathematics-for-machine-learning.pdf#page=140) |
| 5 Vector Calculus | [145](machine-learning/mathematics-for-machine-learning.pdf#page=145) |
| 5.1 Differentiation of Univariate Functions | [147](machine-learning/mathematics-for-machine-learning.pdf#page=147) |
| 5.2 Partial Differentiation and Gradients | [152](machine-learning/mathematics-for-machine-learning.pdf#page=152) |
| 5.3 Gradients of Vector-Valued Functions | [155](machine-learning/mathematics-for-machine-learning.pdf#page=155) |
| 5.4 Gradients of Matrices | [161](machine-learning/mathematics-for-machine-learning.pdf#page=161) |
| 5.5 Useful Identities for Computing Gradients | [164](machine-learning/mathematics-for-machine-learning.pdf#page=164) |
| 5.6 Backpropagation and Automatic Differentiation | [165](machine-learning/mathematics-for-machine-learning.pdf#page=165) |
| 5.7 Higher-Order Derivatives | [170](machine-learning/mathematics-for-machine-learning.pdf#page=170) |
| 5.8 Linearization and Multivariate Taylor Series | [171](machine-learning/mathematics-for-machine-learning.pdf#page=171) |
| 6 Probability and Distributions | [178](machine-learning/mathematics-for-machine-learning.pdf#page=178) |
| 6.1 Construction of a Probability Space | [178](machine-learning/mathematics-for-machine-learning.pdf#page=178) |
| 6.2 Discrete and Continuous Probabilities | [184](machine-learning/mathematics-for-machine-learning.pdf#page=184) |
| 6.3 Sum Rule, Product Rule, and Bayes’ Theorem | [189](machine-learning/mathematics-for-machine-learning.pdf#page=189) |
| 6.4 Summary Statistics and Independence | [192](machine-learning/mathematics-for-machine-learning.pdf#page=192) |
| 6.5 Gaussian Distribution | [203](machine-learning/mathematics-for-machine-learning.pdf#page=203) |
| 6.6 Conjugacy and the Exponential Family | [211](machine-learning/mathematics-for-machine-learning.pdf#page=211) |
| 6.7 Change of Variables/Inverse Transform | [220](machine-learning/mathematics-for-machine-learning.pdf#page=220) |
| 7 Continuous Optimization | [231](machine-learning/mathematics-for-machine-learning.pdf#page=231) |
| 7.1 Optimization Using Gradient Descent | [233](machine-learning/mathematics-for-machine-learning.pdf#page=233) |
| 7.2 Constrained Optimization and Lagrange Multipliers | [239](machine-learning/mathematics-for-machine-learning.pdf#page=239) |
| 7.3 Convex Optimization | [242](machine-learning/mathematics-for-machine-learning.pdf#page=242) |
| 8 When Models Meet Data | [257](machine-learning/mathematics-for-machine-learning.pdf#page=257) |
| 8.1 Data, Models, and Learning | [257](machine-learning/mathematics-for-machine-learning.pdf#page=257) |
| 8.2 Empirical Risk Minimization | [264](machine-learning/mathematics-for-machine-learning.pdf#page=264) |
| 8.3 Parameter Estimation | [271](machine-learning/mathematics-for-machine-learning.pdf#page=271) |
| 8.4 Probabilistic Modeling and Inference | [278](machine-learning/mathematics-for-machine-learning.pdf#page=278) |
| 8.5 Directed Graphical Models | [284](machine-learning/mathematics-for-machine-learning.pdf#page=284) |
| 8.6 Model Selection | [289](machine-learning/mathematics-for-machine-learning.pdf#page=289) |
| 9 Linear Regression | [295](machine-learning/mathematics-for-machine-learning.pdf#page=295) |
| 9.1 Problem Formulation | [297](machine-learning/mathematics-for-machine-learning.pdf#page=297) |
| 9.2 Parameter Estimation | [298](machine-learning/mathematics-for-machine-learning.pdf#page=298) |
| 9.3 Bayesian Linear Regression | [309](machine-learning/mathematics-for-machine-learning.pdf#page=309) |
| 9.4 Maximum Likelihood as Orthogonal Projection | [319](machine-learning/mathematics-for-machine-learning.pdf#page=319) |
| 10 Dimensionality Reduction with Principal Component Analysis | [323](machine-learning/mathematics-for-machine-learning.pdf#page=323) |
| 10.1 Problem Setting | [324](machine-learning/mathematics-for-machine-learning.pdf#page=324) |
| 10.2 Maximum Variance Perspective | [326](machine-learning/mathematics-for-machine-learning.pdf#page=326) |
| 10.3 Projection Perspective | [331](machine-learning/mathematics-for-machine-learning.pdf#page=331) |
| 10.4 Eigenvector Computation and Low-Rank Approximations | [339](machine-learning/mathematics-for-machine-learning.pdf#page=339) |
| 10.5 PCA in High Dimensions | [341](machine-learning/mathematics-for-machine-learning.pdf#page=341) |
| 10.6 Key Steps of PCA in Practice | [342](machine-learning/mathematics-for-machine-learning.pdf#page=342) |
| 10.7 Latent Variable Perspective | [345](machine-learning/mathematics-for-machine-learning.pdf#page=345) |
| 11 Density Estimation with Gaussian Mixture Models | [354](machine-learning/mathematics-for-machine-learning.pdf#page=354) |
| 11.1 Gaussian Mixture Model | [355](machine-learning/mathematics-for-machine-learning.pdf#page=355) |
| 11.2 Parameter Learning via Maximum Likelihood | [356](machine-learning/mathematics-for-machine-learning.pdf#page=356) |
| 11.3 EM Algorithm | [366](machine-learning/mathematics-for-machine-learning.pdf#page=366) |
| 11.4 Latent-Variable Perspective | [369](machine-learning/mathematics-for-machine-learning.pdf#page=369) |
| 12 Classification with Support Vector Machines | [376](machine-learning/mathematics-for-machine-learning.pdf#page=376) |
| 12.1 Separating Hyperplanes | [378](machine-learning/mathematics-for-machine-learning.pdf#page=378) |
| 12.2 Primal Support Vector Machine | [380](machine-learning/mathematics-for-machine-learning.pdf#page=380) |
| 12.3 Dual Support Vector Machine | [389](machine-learning/mathematics-for-machine-learning.pdf#page=389) |
| 12.4 Kernels | [394](machine-learning/mathematics-for-machine-learning.pdf#page=394) |
| 12.5 Numerical Solution | [396](machine-learning/mathematics-for-machine-learning.pdf#page=396) |

### Pattern recognition and machine learning

`machine-learning/pattern-recognition-and-machine-learning.pdf`, 749 pages. Christopher M. Bishop, *Pattern Recognition and Machine Learning*, Springer, 2006
(first edition, Information Science and Statistics series). A Bayesian treatment of machine learning:
probability distributions (chapter 2 holds the Gaussian in full, with conditionals, marginals and Bayes'
theorem for Gaussians), linear models, neural networks, kernels, graphical models, EM, variational
inference, sampling, latent-variable models and sequential data. Was `Pattern Recogniton And Machine
Learning.pdf`. The embedded outline has chapters only; the section rows come from the printed contents
and each page is the printed page plus 19, so the printed page number is the PDF page minus 19. Appendix
rows are the outline's own pages.

| Chapter or section | PDF page |
| --- | --- |
| 1 Introduction | [20](machine-learning/pattern-recognition-and-machine-learning.pdf#page=20) |
| 1.1 Example: Polynomial Curve Fitting | [23](machine-learning/pattern-recognition-and-machine-learning.pdf#page=23) |
| 1.2 Probability Theory | [31](machine-learning/pattern-recognition-and-machine-learning.pdf#page=31) |
| 1.3 Model Selection | [51](machine-learning/pattern-recognition-and-machine-learning.pdf#page=51) |
| 1.4 The Curse of Dimensionality | [52](machine-learning/pattern-recognition-and-machine-learning.pdf#page=52) |
| 1.5 Decision Theory | [57](machine-learning/pattern-recognition-and-machine-learning.pdf#page=57) |
| 1.6 Information Theory | [67](machine-learning/pattern-recognition-and-machine-learning.pdf#page=67) |
| 2 Probability Distributions | [86](machine-learning/pattern-recognition-and-machine-learning.pdf#page=86) |
| 2.1 Binary Variables | [87](machine-learning/pattern-recognition-and-machine-learning.pdf#page=87) |
| 2.2 Multinomial Variables | [93](machine-learning/pattern-recognition-and-machine-learning.pdf#page=93) |
| 2.3 The Gaussian Distribution | [97](machine-learning/pattern-recognition-and-machine-learning.pdf#page=97) |
| 2.4 The Exponential Family | [132](machine-learning/pattern-recognition-and-machine-learning.pdf#page=132) |
| 2.5 Nonparametric Methods | [139](machine-learning/pattern-recognition-and-machine-learning.pdf#page=139) |
| 3 Linear Models for Regression | [156](machine-learning/pattern-recognition-and-machine-learning.pdf#page=156) |
| 3.1 Linear Basis Function Models | [157](machine-learning/pattern-recognition-and-machine-learning.pdf#page=157) |
| 3.2 The Bias-Variance Decomposition | [166](machine-learning/pattern-recognition-and-machine-learning.pdf#page=166) |
| 3.3 Bayesian Linear Regression | [171](machine-learning/pattern-recognition-and-machine-learning.pdf#page=171) |
| 3.4 Bayesian Model Comparison | [180](machine-learning/pattern-recognition-and-machine-learning.pdf#page=180) |
| 3.5 The Evidence Approximation | [184](machine-learning/pattern-recognition-and-machine-learning.pdf#page=184) |
| 3.6 Limitations of Fixed Basis Functions | [191](machine-learning/pattern-recognition-and-machine-learning.pdf#page=191) |
| 4 Linear Models for Classification | [198](machine-learning/pattern-recognition-and-machine-learning.pdf#page=198) |
| 4.1 Discriminant Functions | [200](machine-learning/pattern-recognition-and-machine-learning.pdf#page=200) |
| 4.2 Probabilistic Generative Models | [215](machine-learning/pattern-recognition-and-machine-learning.pdf#page=215) |
| 4.3 Probabilistic Discriminative Models | [222](machine-learning/pattern-recognition-and-machine-learning.pdf#page=222) |
| 4.4 The Laplace Approximation | [232](machine-learning/pattern-recognition-and-machine-learning.pdf#page=232) |
| 4.5 Bayesian Logistic Regression | [236](machine-learning/pattern-recognition-and-machine-learning.pdf#page=236) |
| 5 Neural Networks | [244](machine-learning/pattern-recognition-and-machine-learning.pdf#page=244) |
| 5.1 Feed-forward Network Functions | [246](machine-learning/pattern-recognition-and-machine-learning.pdf#page=246) |
| 5.2 Network Training | [251](machine-learning/pattern-recognition-and-machine-learning.pdf#page=251) |
| 5.3 Error Backpropagation | [260](machine-learning/pattern-recognition-and-machine-learning.pdf#page=260) |
| 5.4 The Hessian Matrix | [268](machine-learning/pattern-recognition-and-machine-learning.pdf#page=268) |
| 5.5 Regularization in Neural Networks | [275](machine-learning/pattern-recognition-and-machine-learning.pdf#page=275) |
| 5.6 Mixture Density Networks | [291](machine-learning/pattern-recognition-and-machine-learning.pdf#page=291) |
| 5.7 Bayesian Neural Networks | [296](machine-learning/pattern-recognition-and-machine-learning.pdf#page=296) |
| 6 Kernel Methods | [310](machine-learning/pattern-recognition-and-machine-learning.pdf#page=310) |
| 6.1 Dual Representations | [312](machine-learning/pattern-recognition-and-machine-learning.pdf#page=312) |
| 6.2 Constructing Kernels | [313](machine-learning/pattern-recognition-and-machine-learning.pdf#page=313) |
| 6.3 Radial Basis Function Networks | [318](machine-learning/pattern-recognition-and-machine-learning.pdf#page=318) |
| 6.4 Gaussian Processes | [322](machine-learning/pattern-recognition-and-machine-learning.pdf#page=322) |
| 7 Sparse Kernel Machines | [344](machine-learning/pattern-recognition-and-machine-learning.pdf#page=344) |
| 7.1 Maximum Margin Classifiers | [345](machine-learning/pattern-recognition-and-machine-learning.pdf#page=345) |
| 7.2 Relevance Vector Machines | [364](machine-learning/pattern-recognition-and-machine-learning.pdf#page=364) |
| 8 Graphical Models | [378](machine-learning/pattern-recognition-and-machine-learning.pdf#page=378) |
| 8.1 Bayesian Networks | [379](machine-learning/pattern-recognition-and-machine-learning.pdf#page=379) |
| 8.2 Conditional Independence | [391](machine-learning/pattern-recognition-and-machine-learning.pdf#page=391) |
| 8.3 Markov Random Fields | [402](machine-learning/pattern-recognition-and-machine-learning.pdf#page=402) |
| 8.4 Inference in Graphical Models | [412](machine-learning/pattern-recognition-and-machine-learning.pdf#page=412) |
| 9 Mixture Models and EM | [442](machine-learning/pattern-recognition-and-machine-learning.pdf#page=442) |
| 9.1 K-means Clustering | [443](machine-learning/pattern-recognition-and-machine-learning.pdf#page=443) |
| 9.2 Mixtures of Gaussians | [449](machine-learning/pattern-recognition-and-machine-learning.pdf#page=449) |
| 9.3 An Alternative View of EM | [458](machine-learning/pattern-recognition-and-machine-learning.pdf#page=458) |
| 9.4 The EM Algorithm in General | [469](machine-learning/pattern-recognition-and-machine-learning.pdf#page=469) |
| 10.1 Variational Inference | [481](machine-learning/pattern-recognition-and-machine-learning.pdf#page=481) |
| 10.2 Illustration: Variational Mixture of Gaussians | [493](machine-learning/pattern-recognition-and-machine-learning.pdf#page=493) |
| 10.3 Variational Linear Regression | [505](machine-learning/pattern-recognition-and-machine-learning.pdf#page=505) |
| 10.4 Exponential Family Distributions | [509](machine-learning/pattern-recognition-and-machine-learning.pdf#page=509) |
| 10.5 Local Variational Methods | [512](machine-learning/pattern-recognition-and-machine-learning.pdf#page=512) |
| 10.6 Variational Logistic Regression | [517](machine-learning/pattern-recognition-and-machine-learning.pdf#page=517) |
| 10.7 Expectation Propagation | [524](machine-learning/pattern-recognition-and-machine-learning.pdf#page=524) |
| 11.1 Basic Sampling Algorithms | [545](machine-learning/pattern-recognition-and-machine-learning.pdf#page=545) |
| 11.2 Markov Chain Monte Carlo | [556](machine-learning/pattern-recognition-and-machine-learning.pdf#page=556) |
| 11.3 Gibbs Sampling | [561](machine-learning/pattern-recognition-and-machine-learning.pdf#page=561) |
| 11.4 Slice Sampling | [565](machine-learning/pattern-recognition-and-machine-learning.pdf#page=565) |
| 11.5 The Hybrid Monte Carlo Algorithm | [567](machine-learning/pattern-recognition-and-machine-learning.pdf#page=567) |
| 11.6 Estimating the Partition Function | [573](machine-learning/pattern-recognition-and-machine-learning.pdf#page=573) |
| 12.1 Principal Component Analysis | [580](machine-learning/pattern-recognition-and-machine-learning.pdf#page=580) |
| 12.2 Probabilistic PCA | [589](machine-learning/pattern-recognition-and-machine-learning.pdf#page=589) |
| 12.3 Kernel PCA | [605](machine-learning/pattern-recognition-and-machine-learning.pdf#page=605) |
| 12.4 Nonlinear Latent Variable Models | [610](machine-learning/pattern-recognition-and-machine-learning.pdf#page=610) |
| 13.1 Markov Models | [626](machine-learning/pattern-recognition-and-machine-learning.pdf#page=626) |
| 13.2 Hidden Markov Models | [629](machine-learning/pattern-recognition-and-machine-learning.pdf#page=629) |
| 13.3 Linear Dynamical Systems | [654](machine-learning/pattern-recognition-and-machine-learning.pdf#page=654) |
| 14.1 Bayesian Model Averaging | [673](machine-learning/pattern-recognition-and-machine-learning.pdf#page=673) |
| 14.2 Committees | [674](machine-learning/pattern-recognition-and-machine-learning.pdf#page=674) |
| 14.3 Boosting | [676](machine-learning/pattern-recognition-and-machine-learning.pdf#page=676) |
| 14.4 Tree-based Models | [682](machine-learning/pattern-recognition-and-machine-learning.pdf#page=682) |
| 14.5 Conditional Mixture Models | [685](machine-learning/pattern-recognition-and-machine-learning.pdf#page=685) |
| Appendix A Data Sets | [692](machine-learning/pattern-recognition-and-machine-learning.pdf#page=692) |
| Appendix B Probability Distributions | [699](machine-learning/pattern-recognition-and-machine-learning.pdf#page=699) |
| Appendix C Properties of Matrices | [708](machine-learning/pattern-recognition-and-machine-learning.pdf#page=708) |
| Appendix D Calculus of Variations | [715](machine-learning/pattern-recognition-and-machine-learning.pdf#page=715) |
| Appendix E Lagrange Multipliers | [718](machine-learning/pattern-recognition-and-machine-learning.pdf#page=718) |
| References | [722](machine-learning/pattern-recognition-and-machine-learning.pdf#page=722) |
| Index | [740](machine-learning/pattern-recognition-and-machine-learning.pdf#page=740) |

### Probabilistic machine learning: an introduction

`machine-learning/probabilistic-machine-learning-an-introduction.pdf`, 863 pages. Kevin P. Murphy, *Probabilistic Machine Learning: An Introduction*, MIT Press,
copyright 2021, published 2022 (the first of two volumes; the second is *Probabilistic Machine Learning:
Advanced Topics*, which is not on the shelf). The book builds machine learning from probability: Part I
covers probability, statistics, decision theory, information theory, linear algebra and optimisation;
Part II linear models; Part III neural networks; Part IV nonparametric models; Part V dimensionality
reduction, clustering and more. Sections marked with a star are optional. Was `Probabilistic Machine
Learning.pdf`. The table is from the PDF's own outline, with sections numbered in the printed order; the
printed page number is the PDF page minus 28. The notation appendix is listed as one row.

| Chapter or section | PDF page |
| --- | --- |
| Preface | [27](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=27) |
| 1 Introduction | [29](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=29) |
| 1.1 What is machine learning? | [29](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=29) |
| 1.2 Supervised learning | [29](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=29) |
| 1.3 Unsupervised learning | [41](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=41) |
| 1.4 Reinforcement learning | [44](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=44) |
| 1.5 Data | [46](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=46) |
| 1.6 Discussion | [53](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=53) |
| Part: I Foundations | [57](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=57) |
| 2 Probability: univariate models | [59](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=59) |
| 2.1 Introduction | [59](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=59) |
| 2.2 Random variables | [61](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=61) |
| 2.3 Bayes' rule | [69](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=69) |
| 2.4 Bernoulli and binomial distributions | [73](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=73) |
| 2.5 Categorical and multinomial distributions | [77](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=77) |
| 2.6 Univariate Gaussian (normal) distribution | [81](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=81) |
| 2.7 Some other common univariate distributions * | [85](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=85) |
| 2.8 Transformations of random variables * | [90](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=90) |
| 2.9 Exercises | [97](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=97) |
| 3 Probability: multivariate models | [101](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=101) |
| 3.1 Joint distributions for multiple random variables | [101](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=101) |
| 3.2 The multivariate Gaussian (normal) distribution | [104](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=104) |
| 3.3 Linear Gaussian systems * | [109](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=109) |
| 3.4 Mixture models | [112](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=112) |
| 3.5 Probabilistic graphical models * | [118](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=118) |
| 3.6 Exercises | [125](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=125) |
| 4 Statistics | [127](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=127) |
| 4.1 Introduction | [127](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=127) |
| 4.2 Maximum likelihood estimation (MLE) | [127](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=127) |
| 4.3 Empirical risk minimization (ERM) | [135](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=135) |
| 4.4 Other estimation methods * | [136](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=136) |
| 4.5 Regularization | [140](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=140) |
| 4.6 Bayesian statistics * | [149](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=149) |
| 4.7 Frequentist statistics * | [174](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=174) |
| 4.8 Exercises | [182](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=182) |
| 5 Decision theory | [187](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=187) |
| 5.1 Bayesian decision theory | [187](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=187) |
| 5.2 A/B testing * | [199](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=199) |
| 5.3 Bandit problems * | [204](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=204) |
| 5.4 Bayesian hypothesis testing | [212](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=212) |
| 5.5 Frequentist decision theory | [220](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=220) |
| 5.6 Empirical risk minimization | [224](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=224) |
| 5.7 Frequentist hypothesis testing * | [229](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=229) |
| 5.8 Exercises | [234](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=234) |
| 6 Information theory | [237](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=237) |
| 6.1 Entropy | [237](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=237) |
| 6.2 Relative entropy (KL divergence) * | [243](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=243) |
| 6.3 Mutual information * | [247](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=247) |
| 6.4 Exercises | [256](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=256) |
| 7 Linear algebra | [259](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=259) |
| 7.1 Introduction | [259](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=259) |
| 7.2 Matrix multiplication | [272](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=272) |
| 7.3 Matrix inversion | [279](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=279) |
| 7.4 Eigenvalue decomposition (EVD) | [282](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=282) |
| 7.5 Singular value decomposition (SVD) | [287](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=287) |
| 7.6 Other matrix decompositions * | [292](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=292) |
| 7.7 Solving systems of linear equations * | [294](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=294) |
| 7.8 Matrix calculus | [297](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=297) |
| 7.9 Exercises | [305](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=305) |
| 8 Optimization | [307](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=307) |
| 8.1 Introduction | [307](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=307) |
| 8.2 First-order methods | [314](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=314) |
| 8.3 Second-order methods | [320](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=320) |
| 8.4 Stochastic gradient descent | [327](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=327) |
| 8.5 Constrained optimization | [335](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=335) |
| 8.6 Proximal gradient method * | [342](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=342) |
| 8.7 Bound optimization * | [345](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=345) |
| 8.8 Blackbox and derivative free optimization | [356](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=356) |
| 8.9 Exercises | [358](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=358) |
| Part: II Linear models | [359](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=359) |
| 9 Linear discriminant analysis | [361](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=361) |
| 9.1 Introduction | [361](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=361) |
| 9.2 Gaussian discriminant analysis | [361](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=361) |
| 9.3 Naive Bayes classifiers | [370](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=370) |
| 9.4 Generative vs discriminative classifiers | [374](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=374) |
| 9.5 Exercises | [376](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=376) |
| 10 Logistic regression | [377](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=377) |
| 10.1 Introduction | [377](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=377) |
| 10.2 Binary logistic regression | [377](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=377) |
| 10.3 Multinomial logistic regression | [388](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=388) |
| 10.4 Robust logistic regression * | [397](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=397) |
| 10.5 Bayesian logistic regression * | [400](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=400) |
| 10.6 Exercises | [404](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=404) |
| 11 Linear regression | [407](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=407) |
| 11.1 Introduction | [407](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=407) |
| 11.2 Standard linear regression | [407](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=407) |
| 11.3 Ridge regression | [417](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=417) |
| 11.4 Robust linear regression * | [421](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=421) |
| 11.5 Lasso regression | [425](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=425) |
| 11.6 Bayesian linear regression * | [437](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=437) |
| 11.7 Exercises | [444](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=444) |
| 12 Generalized linear models * | [447](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=447) |
| 12.1 Introduction | [447](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=447) |
| 12.2 The exponential family | [447](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=447) |
| 12.3 Generalized linear models (GLMs) | [456](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=456) |
| 12.4 Probit regression | [460](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=460) |
| Part: III Deep neural networks | [465](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=465) |
| 13 Neural networks for unstructured data | [467](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=467) |
| 13.1 Introduction | [467](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=467) |
| 13.2 Multilayer perceptrons (MLPs) | [468](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=468) |
| 13.3 Backpropagation | [479](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=479) |
| 13.4 Training neural networks | [492](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=492) |
| 13.5 Regularization | [500](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=500) |
| 13.6 Other kinds of feedforward networks | [505](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=505) |
| 13.7 Exercises | [510](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=510) |
| 14 Neural networks for images | [511](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=511) |
| 14.1 Introduction | [511](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=511) |
| 14.2 Common layers | [512](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=512) |
| 14.3 Common architectures for image classification | [523](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=523) |
| 14.4 Other forms of convolution * | [528](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=528) |
| 14.5 Solving other discriminative vision tasks with CNNs | [531](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=531) |
| 14.6 Generating images by inverting CNNs * | [535](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=535) |
| 14.7 Adversarial Examples * | [542](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=542) |
| 15 Neural networks for sequences | [551](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=551) |
| 15.1 Introduction | [551](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=551) |
| 15.2 Recurrent neural networks (RNNs) | [551](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=551) |
| 15.3 1d CNNs | [564](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=564) |
| 15.4 Attention | [566](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=566) |
| 15.5 Transformers | [574](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=574) |
| 15.6 Efficient transformers * | [580](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=580) |
| 15.7 Language models and unsupervised representation learning | [584](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=584) |
| Part: IV Nonparametric models | [591](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=591) |
| 16 Exemplar-based methods | [593](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=593) |
| 16.1 K nearest neighbor (KNN) classification | [593](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=593) |
| 16.2 Learning distance metrics | [597](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=597) |
| 16.3 Kernel density estimation (KDE) | [605](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=605) |
| 17 Kernel methods | [613](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=613) |
| 17.1 Inferring functions from data | [613](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=613) |
| 17.2 Mercer kernels | [616](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=616) |
| 17.3 Gaussian processes | [622](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=622) |
| 17.4 Scaling GPs to large datasets | [630](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=630) |
| 17.5 Support vector machines (SVMs) | [633](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=633) |
| 17.6 Sparse vector machines | [646](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=646) |
| 17.7 Optimizing in function space * | [649](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=649) |
| 17.8 Exercises | [653](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=653) |
| 18 Trees, forests, bagging and boosting | [655](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=655) |
| 18.1 Classification and regression trees (CART) | [655](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=655) |
| 18.2 Ensemble learning | [660](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=660) |
| 18.3 Bagging | [661](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=661) |
| 18.4 Random forests | [662](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=662) |
| 18.5 Boosting | [663](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=663) |
| 18.6 Interpreting tree ensembles | [672](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=672) |
| Part: V Beyond supervised learning | [675](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=675) |
| 19 Learning with fewer labeled examples | [677](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=677) |
| 19.1 Data augmentation | [677](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=677) |
| 19.2 Transfer learning | [678](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=678) |
| 19.3 Semi-supervised learning | [684](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=684) |
| 19.4 Active learning | [696](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=696) |
| 19.5 Meta-learning * | [698](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=698) |
| 19.6 Few-shot learning * | [699](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=699) |
| 19.7 Exercises | [701](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=701) |
| 20 Dimensionality reduction | [703](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=703) |
| 20.1 Principal components analysis (PCA) | [703](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=703) |
| 20.2 Factor analysis * | [712](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=712) |
| 20.3 Autoencoders | [725](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=725) |
| 20.4 Manifold learning * | [734](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=734) |
| 20.5 Word embeddings | [751](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=751) |
| 20.6 Exercises | [758](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=758) |
| 21 Clustering | [761](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=761) |
| 21.1 Introduction | [761](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=761) |
| 21.2 Hierarchical agglomerative clustering | [763](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=763) |
| 21.3 K means clustering | [767](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=767) |
| 21.4 Clustering using mixture models | [775](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=775) |
| 21.5 Spectral clustering * | [780](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=780) |
| 21.6 Biclustering * | [783](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=783) |
| 22 Recommender systems | [787](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=787) |
| 22.1 Explicit feedback | [787](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=787) |
| 22.2 Implicit feedback | [792](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=792) |
| 22.3 Leveraging side information | [795](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=795) |
| 22.4 Exploration-exploitation tradeoff | [796](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=796) |
| 23 Graph embeddings * | [799](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=799) |
| 23.1 Introduction | [799](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=799) |
| 23.2 Graph Embedding as an Encoder/Decoder Problem | [800](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=800) |
| 23.3 Shallow graph embeddings | [802](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=802) |
| 23.4 Graph Neural Networks | [807](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=807) |
| 23.5 Deep graph embeddings | [811](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=811) |
| 23.6 Applications | [815](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=815) |
| Part: VI Appendix | [821](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=821) |
| Notation | [823](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=823) |
| Bibliography | [831](machine-learning/probabilistic-machine-learning-an-introduction.pdf#page=831) |

### Deep learning textbook

`machine-learning/deep-learning-textbook.pdf`, 801 pages. Ian Goodfellow, Yoshua Bengio and Aaron
Courville, *Deep Learning*, MIT Press, 2016 (the draft released on the book's website). A published
textbook in three parts: the applied maths a deep network rests on (linear algebra, probability and
information theory, numerical optimisation), modern practice (feedforward networks and back-propagation,
regularisation, optimisation, convolutional and recurrent nets), and research topics (autoencoders,
structured probabilistic models, Monte Carlo methods, score matching, approximate inference, Boltzmann
machines and other generative models). It predates diffusion models and does not cover them. Was
`Deep Learning.pdf`. No embedded outline; this table is from the printed contents, and each page was
checked against the heading printed on it. The printed page number is the PDF page minus 16, except the
Index, which starts at PDF page 794.

| Chapter or section | PDF page |
| --- | --- |
| 1 Introduction | [17](machine-learning/deep-learning-textbook.pdf#page=17) |
| 1.1 Who Should Read This Book? | [24](machine-learning/deep-learning-textbook.pdf#page=24) |
| 1.2 Historical Trends in Deep Learning | [27](machine-learning/deep-learning-textbook.pdf#page=27) |
| Part I: Applied Math and Machine Learning Basics | [45](machine-learning/deep-learning-textbook.pdf#page=45) |
| 2 Linear Algebra | [47](machine-learning/deep-learning-textbook.pdf#page=47) |
| 2.1 Scalars, Vectors, Matrices and Tensors | [47](machine-learning/deep-learning-textbook.pdf#page=47) |
| 2.2 Multiplying Matrices and Vectors | [50](machine-learning/deep-learning-textbook.pdf#page=50) |
| 2.3 Identity and Inverse Matrices | [52](machine-learning/deep-learning-textbook.pdf#page=52) |
| 2.4 Linear Dependence and Span | [53](machine-learning/deep-learning-textbook.pdf#page=53) |
| 2.5 Norms | [55](machine-learning/deep-learning-textbook.pdf#page=55) |
| 2.6 Special Kinds of Matrices and Vectors | [56](machine-learning/deep-learning-textbook.pdf#page=56) |
| 2.7 Eigendecomposition | [58](machine-learning/deep-learning-textbook.pdf#page=58) |
| 2.8 Singular Value Decomposition | [60](machine-learning/deep-learning-textbook.pdf#page=60) |
| 2.9 The Moore-Penrose Pseudoinverse | [61](machine-learning/deep-learning-textbook.pdf#page=61) |
| 2.10 The Trace Operator | [62](machine-learning/deep-learning-textbook.pdf#page=62) |
| 2.11 The Determinant | [63](machine-learning/deep-learning-textbook.pdf#page=63) |
| 2.12 Example: Principal Components Analysis | [64](machine-learning/deep-learning-textbook.pdf#page=64) |
| 3 Probability and Information Theory | [69](machine-learning/deep-learning-textbook.pdf#page=69) |
| 3.1 Why Probability? | [70](machine-learning/deep-learning-textbook.pdf#page=70) |
| 3.2 Random Variables | [72](machine-learning/deep-learning-textbook.pdf#page=72) |
| 3.3 Probability Distributions | [72](machine-learning/deep-learning-textbook.pdf#page=72) |
| 3.4 Marginal Probability | [74](machine-learning/deep-learning-textbook.pdf#page=74) |
| 3.5 Conditional Probability | [75](machine-learning/deep-learning-textbook.pdf#page=75) |
| 3.6 The Chain Rule of Conditional Probabilities | [75](machine-learning/deep-learning-textbook.pdf#page=75) |
| 3.7 Independence and Conditional Independence | [76](machine-learning/deep-learning-textbook.pdf#page=76) |
| 3.8 Expectation, Variance and Covariance | [76](machine-learning/deep-learning-textbook.pdf#page=76) |
| 3.9 Common Probability Distributions | [78](machine-learning/deep-learning-textbook.pdf#page=78) |
| 3.10 Useful Properties of Common Functions | [83](machine-learning/deep-learning-textbook.pdf#page=83) |
| 3.11 Bayes’ Rule | [86](machine-learning/deep-learning-textbook.pdf#page=86) |
| 3.12 Technical Details of Continuous Variables | [87](machine-learning/deep-learning-textbook.pdf#page=87) |
| 3.13 Information Theory | [89](machine-learning/deep-learning-textbook.pdf#page=89) |
| 3.14 Structured Probabilistic Models | [91](machine-learning/deep-learning-textbook.pdf#page=91) |
| 4 Numerical Computation | [96](machine-learning/deep-learning-textbook.pdf#page=96) |
| 4.1 Overﬂow and Underﬂow | [96](machine-learning/deep-learning-textbook.pdf#page=96) |
| 4.2 Poor Conditioning | [98](machine-learning/deep-learning-textbook.pdf#page=98) |
| 4.3 Gradient-Based Optimization | [98](machine-learning/deep-learning-textbook.pdf#page=98) |
| 4.4 Constrained Optimization | [109](machine-learning/deep-learning-textbook.pdf#page=109) |
| 4.5 Example: Linear Least Squares | [112](machine-learning/deep-learning-textbook.pdf#page=112) |
| 5 Machine Learning Basics | [114](machine-learning/deep-learning-textbook.pdf#page=114) |
| 5.1 Learning Algorithms | [115](machine-learning/deep-learning-textbook.pdf#page=115) |
| 5.2 Capacity, Overﬁtting and Underﬁtting | [126](machine-learning/deep-learning-textbook.pdf#page=126) |
| 5.3 Hyperparameters and Validation Sets | [136](machine-learning/deep-learning-textbook.pdf#page=136) |
| 5.4 Estimators, Bias and Variance | [138](machine-learning/deep-learning-textbook.pdf#page=138) |
| 5.5 Maximum Likelihood Estimation | [147](machine-learning/deep-learning-textbook.pdf#page=147) |
| 5.6 Bayesian Statistics | [151](machine-learning/deep-learning-textbook.pdf#page=151) |
| 5.7 Supervised Learning Algorithms | [156](machine-learning/deep-learning-textbook.pdf#page=156) |
| 5.8 Unsupervised Learning Algorithms | [162](machine-learning/deep-learning-textbook.pdf#page=162) |
| 5.9 Stochastic Gradient Descent | [167](machine-learning/deep-learning-textbook.pdf#page=167) |
| 5.10 Building a Machine Learning Algorithm | [169](machine-learning/deep-learning-textbook.pdf#page=169) |
| 5.11 Challenges Motivating Deep Learning | [171](machine-learning/deep-learning-textbook.pdf#page=171) |
| Part II: Deep Networks: Modern Practices | [182](machine-learning/deep-learning-textbook.pdf#page=182) |
| 6 Deep Feedforward Networks | [184](machine-learning/deep-learning-textbook.pdf#page=184) |
| 6.1 Example: Learning XOR | [187](machine-learning/deep-learning-textbook.pdf#page=187) |
| 6.2 Gradient-Based Learning | [193](machine-learning/deep-learning-textbook.pdf#page=193) |
| 6.3 Hidden Units | [207](machine-learning/deep-learning-textbook.pdf#page=207) |
| 6.4 Architecture Design | [213](machine-learning/deep-learning-textbook.pdf#page=213) |
| 6.5 Back-Propagation and Other Diﬀerentiation Algorithms | [220](machine-learning/deep-learning-textbook.pdf#page=220) |
| 6.6 Historical Notes | [240](machine-learning/deep-learning-textbook.pdf#page=240) |
| 7 Regularization for Deep Learning | [244](machine-learning/deep-learning-textbook.pdf#page=244) |
| 7.1 Parameter Norm Penalties | [246](machine-learning/deep-learning-textbook.pdf#page=246) |
| 7.2 Norm Penalties as Constrained Optimization | [253](machine-learning/deep-learning-textbook.pdf#page=253) |
| 7.3 Regularization and Under-Constrained Problems | [255](machine-learning/deep-learning-textbook.pdf#page=255) |
| 7.4 Dataset Augmentation | [256](machine-learning/deep-learning-textbook.pdf#page=256) |
| 7.5 Noise Robustness | [258](machine-learning/deep-learning-textbook.pdf#page=258) |
| 7.6 Semi-Supervised Learning | [259](machine-learning/deep-learning-textbook.pdf#page=259) |
| 7.7 Multi-Task Learning | [260](machine-learning/deep-learning-textbook.pdf#page=260) |
| 7.8 Early Stopping | [262](machine-learning/deep-learning-textbook.pdf#page=262) |
| 7.9 Parameter Tying and Parameter Sharing | [269](machine-learning/deep-learning-textbook.pdf#page=269) |
| 7.10 Sparse Representations | [270](machine-learning/deep-learning-textbook.pdf#page=270) |
| 7.11 Bagging and Other Ensemble Methods | [272](machine-learning/deep-learning-textbook.pdf#page=272) |
| 7.12 Dropout | [274](machine-learning/deep-learning-textbook.pdf#page=274) |
| 7.13 Adversarial Training | [284](machine-learning/deep-learning-textbook.pdf#page=284) |
| 7.14 Tangent Distance, Tangent Prop, and Manifold Tangent Classiﬁer | [286](machine-learning/deep-learning-textbook.pdf#page=286) |
| 8 Optimization for Training Deep Models | [290](machine-learning/deep-learning-textbook.pdf#page=290) |
| 8.1 How Learning Diﬀers from Pure Optimization | [291](machine-learning/deep-learning-textbook.pdf#page=291) |
| 8.2 Challenges in Neural Network Optimization | [298](machine-learning/deep-learning-textbook.pdf#page=298) |
| 8.3 Basic Algorithms | [310](machine-learning/deep-learning-textbook.pdf#page=310) |
| 8.4 Parameter Initialization Strategies | [317](machine-learning/deep-learning-textbook.pdf#page=317) |
| 8.5 Algorithms with Adaptive Learning Rates | [322](machine-learning/deep-learning-textbook.pdf#page=322) |
| 8.6 Approximate Second-Order Methods | [326](machine-learning/deep-learning-textbook.pdf#page=326) |
| 8.7 Optimization Strategies and Meta-Algorithms | [333](machine-learning/deep-learning-textbook.pdf#page=333) |
| 9 Convolutional Networks | [346](machine-learning/deep-learning-textbook.pdf#page=346) |
| 9.1 The Convolution Operation | [347](machine-learning/deep-learning-textbook.pdf#page=347) |
| 9.2 Motivation | [351](machine-learning/deep-learning-textbook.pdf#page=351) |
| 9.3 Pooling | [355](machine-learning/deep-learning-textbook.pdf#page=355) |
| 9.4 Convolution and Pooling as an Inﬁnitely Strong Prior | [361](machine-learning/deep-learning-textbook.pdf#page=361) |
| 9.5 Variants of the Basic Convolution Function | [363](machine-learning/deep-learning-textbook.pdf#page=363) |
| 9.6 Structured Outputs | [374](machine-learning/deep-learning-textbook.pdf#page=374) |
| 9.7 Data Types | [376](machine-learning/deep-learning-textbook.pdf#page=376) |
| 9.8 Eﬃcient Convolution Algorithms | [378](machine-learning/deep-learning-textbook.pdf#page=378) |
| 9.9 Random or Unsupervised Features | [379](machine-learning/deep-learning-textbook.pdf#page=379) |
| 9.10 The Neuroscientiﬁc Basis for Convolutional Networks | [380](machine-learning/deep-learning-textbook.pdf#page=380) |
| 9.11 Convolutional Networks and the History of Deep Learning | [387](machine-learning/deep-learning-textbook.pdf#page=387) |
| 10 Sequence Modeling: Recurrent and Recursive Nets | [389](machine-learning/deep-learning-textbook.pdf#page=389) |
| 10.1 Unfolding Computational Graphs | [391](machine-learning/deep-learning-textbook.pdf#page=391) |
| 10.2 Recurrent Neural Networks | [394](machine-learning/deep-learning-textbook.pdf#page=394) |
| 10.3 Bidirectional RNNs | [410](machine-learning/deep-learning-textbook.pdf#page=410) |
| 10.4 Encoder-Decoder Sequence-to-Sequence Architectures | [412](machine-learning/deep-learning-textbook.pdf#page=412) |
| 10.5 Deep Recurrent Networks | [414](machine-learning/deep-learning-textbook.pdf#page=414) |
| 10.6 Recursive Neural Networks | [416](machine-learning/deep-learning-textbook.pdf#page=416) |
| 10.7 The Challenge of Long-Term Dependencies | [417](machine-learning/deep-learning-textbook.pdf#page=417) |
| 10.8 Echo State Networks | [420](machine-learning/deep-learning-textbook.pdf#page=420) |
| 10.9 Leaky Units and Other Strategies for Multiple Time Scales | [422](machine-learning/deep-learning-textbook.pdf#page=422) |
| 10.10 The Long Short-Term Memory and Other Gated RNNs | [424](machine-learning/deep-learning-textbook.pdf#page=424) |
| 10.11 Optimization for Long-Term Dependencies | [429](machine-learning/deep-learning-textbook.pdf#page=429) |
| 10.12 Explicit Memory | [432](machine-learning/deep-learning-textbook.pdf#page=432) |
| 11 Practical Methodology | [437](machine-learning/deep-learning-textbook.pdf#page=437) |
| 11.1 Performance Metrics | [438](machine-learning/deep-learning-textbook.pdf#page=438) |
| 11.2 Default Baseline Models | [441](machine-learning/deep-learning-textbook.pdf#page=441) |
| 11.3 Determining Whether to Gather More Data | [442](machine-learning/deep-learning-textbook.pdf#page=442) |
| 11.4 Selecting Hyperparameters | [443](machine-learning/deep-learning-textbook.pdf#page=443) |
| 11.5 Debugging Strategies | [452](machine-learning/deep-learning-textbook.pdf#page=452) |
| 11.6 Example: Multi-Digit Number Recognition | [456](machine-learning/deep-learning-textbook.pdf#page=456) |
| 12 Applications | [459](machine-learning/deep-learning-textbook.pdf#page=459) |
| 12.1 Large-Scale Deep Learning | [459](machine-learning/deep-learning-textbook.pdf#page=459) |
| 12.2 Computer Vision | [468](machine-learning/deep-learning-textbook.pdf#page=468) |
| 12.3 Speech Recognition | [474](machine-learning/deep-learning-textbook.pdf#page=474) |
| 12.4 Natural Language Processing | [477](machine-learning/deep-learning-textbook.pdf#page=477) |
| 12.5 Other Applications | [494](machine-learning/deep-learning-textbook.pdf#page=494) |
| Part III: Deep Learning Research | [502](machine-learning/deep-learning-textbook.pdf#page=502) |
| 13 Linear Factor Models | [505](machine-learning/deep-learning-textbook.pdf#page=505) |
| 13.1 Probabilistic PCA and Factor Analysis | [506](machine-learning/deep-learning-textbook.pdf#page=506) |
| 13.2 Independent Component Analysis (ICA) | [507](machine-learning/deep-learning-textbook.pdf#page=507) |
| 13.3 Slow Feature Analysis | [509](machine-learning/deep-learning-textbook.pdf#page=509) |
| 13.4 Sparse Coding | [512](machine-learning/deep-learning-textbook.pdf#page=512) |
| 13.5 Manifold Interpretation of PCA | [515](machine-learning/deep-learning-textbook.pdf#page=515) |
| 14 Autoencoders | [518](machine-learning/deep-learning-textbook.pdf#page=518) |
| 14.1 Undercomplete Autoencoders | [519](machine-learning/deep-learning-textbook.pdf#page=519) |
| 14.2 Regularized Autoencoders | [520](machine-learning/deep-learning-textbook.pdf#page=520) |
| 14.3 Representational Power, Layer Size and Depth | [524](machine-learning/deep-learning-textbook.pdf#page=524) |
| 14.4 Stochastic Encoders and Decoders | [525](machine-learning/deep-learning-textbook.pdf#page=525) |
| 14.5 Denoising Autoencoders | [526](machine-learning/deep-learning-textbook.pdf#page=526) |
| 14.6 Learning Manifolds with Autoencoders | [531](machine-learning/deep-learning-textbook.pdf#page=531) |
| 14.7 Contractive Autoencoders | [537](machine-learning/deep-learning-textbook.pdf#page=537) |
| 14.8 Predictive Sparse Decomposition | [539](machine-learning/deep-learning-textbook.pdf#page=539) |
| 14.9 Applications of Autoencoders | [540](machine-learning/deep-learning-textbook.pdf#page=540) |
| 15 Representation Learning | [542](machine-learning/deep-learning-textbook.pdf#page=542) |
| 15.1 Greedy Layer-Wise Unsupervised Pretraining | [544](machine-learning/deep-learning-textbook.pdf#page=544) |
| 15.2 Transfer Learning and Domain Adaptation | [552](machine-learning/deep-learning-textbook.pdf#page=552) |
| 15.3 Semi-Supervised Disentangling of Causal Factors | [557](machine-learning/deep-learning-textbook.pdf#page=557) |
| 15.4 Distributed Representation | [562](machine-learning/deep-learning-textbook.pdf#page=562) |
| 15.5 Exponential Gains from Depth | [569](machine-learning/deep-learning-textbook.pdf#page=569) |
| 15.6 Providing Clues to Discover Underlying Causes | [570](machine-learning/deep-learning-textbook.pdf#page=570) |
| 16 Structured Probabilistic Models for Deep Learning | [574](machine-learning/deep-learning-textbook.pdf#page=574) |
| 16.1 The Challenge of Unstructured Modeling | [575](machine-learning/deep-learning-textbook.pdf#page=575) |
| 16.2 Using Graphs to Describe Model Structure | [579](machine-learning/deep-learning-textbook.pdf#page=579) |
| 16.3 Sampling from Graphical Models | [596](machine-learning/deep-learning-textbook.pdf#page=596) |
| 16.4 Advantages of Structured Modeling | [598](machine-learning/deep-learning-textbook.pdf#page=598) |
| 16.5 Learning about Dependencies | [598](machine-learning/deep-learning-textbook.pdf#page=598) |
| 16.6 Inference and Approximate Inference | [600](machine-learning/deep-learning-textbook.pdf#page=600) |
| 16.7 The Deep Learning Approach to Structured Probabilistic Models | [601](machine-learning/deep-learning-textbook.pdf#page=601) |
| 17 Monte Carlo Methods | [606](machine-learning/deep-learning-textbook.pdf#page=606) |
| 17.1 Sampling and Monte Carlo Methods | [606](machine-learning/deep-learning-textbook.pdf#page=606) |
| 17.2 Importance Sampling | [608](machine-learning/deep-learning-textbook.pdf#page=608) |
| 17.3 Markov Chain Monte Carlo Methods | [611](machine-learning/deep-learning-textbook.pdf#page=611) |
| 17.4 Gibbs Sampling | [615](machine-learning/deep-learning-textbook.pdf#page=615) |
| 17.5 The Challenge of Mixing between Separated Modes | [615](machine-learning/deep-learning-textbook.pdf#page=615) |
| 18 Confronting the Partition Function | [621](machine-learning/deep-learning-textbook.pdf#page=621) |
| 18.1 The Log-Likelihood Gradient | [622](machine-learning/deep-learning-textbook.pdf#page=622) |
| 18.2 Stochastic Maximum Likelihood and Contrastive Divergence | [623](machine-learning/deep-learning-textbook.pdf#page=623) |
| 18.3 Pseudolikelihood | [631](machine-learning/deep-learning-textbook.pdf#page=631) |
| 18.4 Score Matching and Ratio Matching | [633](machine-learning/deep-learning-textbook.pdf#page=633) |
| 18.5 Denoising Score Matching | [635](machine-learning/deep-learning-textbook.pdf#page=635) |
| 18.6 Noise-Contrastive Estimation | [636](machine-learning/deep-learning-textbook.pdf#page=636) |
| 18.7 Estimating the Partition Function | [639](machine-learning/deep-learning-textbook.pdf#page=639) |
| 19 Approximate Inference | [647](machine-learning/deep-learning-textbook.pdf#page=647) |
| 19.1 Inference as Optimization | [649](machine-learning/deep-learning-textbook.pdf#page=649) |
| 19.2 Expectation Maximization | [650](machine-learning/deep-learning-textbook.pdf#page=650) |
| 19.3 MAP Inference and Sparse Coding | [651](machine-learning/deep-learning-textbook.pdf#page=651) |
| 19.4 Variational Inference and Learning | [654](machine-learning/deep-learning-textbook.pdf#page=654) |
| 19.5 Learned Approximate Inference | [667](machine-learning/deep-learning-textbook.pdf#page=667) |
| 20 Deep Generative Models | [670](machine-learning/deep-learning-textbook.pdf#page=670) |
| 20.1 Boltzmann Machines | [670](machine-learning/deep-learning-textbook.pdf#page=670) |
| 20.2 Restricted Boltzmann Machines | [672](machine-learning/deep-learning-textbook.pdf#page=672) |
| 20.3 Deep Belief Networks | [676](machine-learning/deep-learning-textbook.pdf#page=676) |
| 20.4 Deep Boltzmann Machines | [679](machine-learning/deep-learning-textbook.pdf#page=679) |
| 20.5 Boltzmann Machines for Real-Valued Data | [692](machine-learning/deep-learning-textbook.pdf#page=692) |
| 20.6 Convolutional Boltzmann Machines | [699](machine-learning/deep-learning-textbook.pdf#page=699) |
| 20.7 Boltzmann Machines for Structured or Sequential Outputs | [701](machine-learning/deep-learning-textbook.pdf#page=701) |
| 20.8 Other Boltzmann Machines | [702](machine-learning/deep-learning-textbook.pdf#page=702) |
| 20.9 Back-Propagation through Random Operations | [703](machine-learning/deep-learning-textbook.pdf#page=703) |
| 20.10 Directed Generative Nets | [708](machine-learning/deep-learning-textbook.pdf#page=708) |
| 20.11 Drawing Samples from Autoencoders | [727](machine-learning/deep-learning-textbook.pdf#page=727) |
| 20.12 Generative Stochastic Networks | [730](machine-learning/deep-learning-textbook.pdf#page=730) |
| 20.13 Other Generation Schemes | [732](machine-learning/deep-learning-textbook.pdf#page=732) |
| 20.14 Evaluating Generative Models | [733](machine-learning/deep-learning-textbook.pdf#page=733) |
| 20.15 Conclusion | [736](machine-learning/deep-learning-textbook.pdf#page=736) |
| Bibliography | [737](machine-learning/deep-learning-textbook.pdf#page=737) |
| Index | [794](machine-learning/deep-learning-textbook.pdf#page=794) |

### Understanding deep learning

`machine-learning/understanding-deep-learning.pdf`, 541 pages. Simon J. D. Prince, *Understanding Deep
Learning*, MIT Press, December 2023; this file is the author's open copy dated 3 April 2024. A published
textbook that builds up from linear regression and shallow networks through loss functions, gradients and
backpropagation, convolutional nets, residual nets and transformers, to generative models (GANs,
normalizing flows, variational autoencoders, diffusion models), reinforcement learning, and why deep
learning works. Appendix C covers the probability it uses. Was `Underestand Deep Learning.pdf`. The table
is from the PDF's own outline, chapters and their first-level sections. The printed page number is the PDF
page minus 14 from chapter 1 on; the front matter is numbered in roman.

| Chapter or section | PDF page |
| --- | --- |
| Preface | [5](machine-learning/understanding-deep-learning.pdf#page=5) |
| Acknowledgements | [11](machine-learning/understanding-deep-learning.pdf#page=11) |
| 1 Introduction | [15](machine-learning/understanding-deep-learning.pdf#page=15) |
| 1.1 Supervised learning | [15](machine-learning/understanding-deep-learning.pdf#page=15) |
| 1.2 Unsupervised learning | [21](machine-learning/understanding-deep-learning.pdf#page=21) |
| 1.3 Reinforcement learning | [25](machine-learning/understanding-deep-learning.pdf#page=25) |
| 1.4 Ethics | [26](machine-learning/understanding-deep-learning.pdf#page=26) |
| 1.5 Structure of book | [29](machine-learning/understanding-deep-learning.pdf#page=29) |
| 1.6 Other books | [29](machine-learning/understanding-deep-learning.pdf#page=29) |
| 1.7 How to read this book | [30](machine-learning/understanding-deep-learning.pdf#page=30) |
| 2 Supervised learning | [31](machine-learning/understanding-deep-learning.pdf#page=31) |
| 2.1 Supervised learning overview | [31](machine-learning/understanding-deep-learning.pdf#page=31) |
| 2.2 Linear regression example | [32](machine-learning/understanding-deep-learning.pdf#page=32) |
| 2.3 Summary | [36](machine-learning/understanding-deep-learning.pdf#page=36) |
| 3 Shallow neural networks | [39](machine-learning/understanding-deep-learning.pdf#page=39) |
| 3.1 Neural network example | [39](machine-learning/understanding-deep-learning.pdf#page=39) |
| 3.2 Universal approximation theorem | [43](machine-learning/understanding-deep-learning.pdf#page=43) |
| 3.3 Multivariate inputs and outputs | [44](machine-learning/understanding-deep-learning.pdf#page=44) |
| 3.4 Shallow neural networks: general case | [47](machine-learning/understanding-deep-learning.pdf#page=47) |
| 3.5 Terminology | [49](machine-learning/understanding-deep-learning.pdf#page=49) |
| 3.6 Summary | [50](machine-learning/understanding-deep-learning.pdf#page=50) |
| 4 Deep neural networks | [55](machine-learning/understanding-deep-learning.pdf#page=55) |
| 4.1 Composing neural networks | [55](machine-learning/understanding-deep-learning.pdf#page=55) |
| 4.2 From composing networks to deep networks | [57](machine-learning/understanding-deep-learning.pdf#page=57) |
| 4.3 Deep neural networks | [59](machine-learning/understanding-deep-learning.pdf#page=59) |
| 4.4 Matrix notation | [62](machine-learning/understanding-deep-learning.pdf#page=62) |
| 4.5 Shallow vs. deep neural networks | [63](machine-learning/understanding-deep-learning.pdf#page=63) |
| 4.6 Summary | [66](machine-learning/understanding-deep-learning.pdf#page=66) |
| 5 Loss functions | [70](machine-learning/understanding-deep-learning.pdf#page=70) |
| 5.1 Maximum likelihood | [70](machine-learning/understanding-deep-learning.pdf#page=70) |
| 5.2 Recipe for constructing loss functions | [74](machine-learning/understanding-deep-learning.pdf#page=74) |
| 5.3 Example 1: univariate regression | [75](machine-learning/understanding-deep-learning.pdf#page=75) |
| 5.4 Example 2: binary classification | [78](machine-learning/understanding-deep-learning.pdf#page=78) |
| 5.5 Example 3: multiclass classification | [81](machine-learning/understanding-deep-learning.pdf#page=81) |
| 5.6 Multiple outputs | [83](machine-learning/understanding-deep-learning.pdf#page=83) |
| 5.7 Cross-entropy loss | [85](machine-learning/understanding-deep-learning.pdf#page=85) |
| 5.8 Summary | [86](machine-learning/understanding-deep-learning.pdf#page=86) |
| 6 Fitting models | [91](machine-learning/understanding-deep-learning.pdf#page=91) |
| 6.1 Gradient descent | [91](machine-learning/understanding-deep-learning.pdf#page=91) |
| 6.2 Stochastic gradient descent | [97](machine-learning/understanding-deep-learning.pdf#page=97) |
| 6.3 Momentum | [100](machine-learning/understanding-deep-learning.pdf#page=100) |
| 6.4 Adam | [102](machine-learning/understanding-deep-learning.pdf#page=102) |
| 6.5 Training algorithm hyperparameters | [105](machine-learning/understanding-deep-learning.pdf#page=105) |
| 6.6 Summary | [105](machine-learning/understanding-deep-learning.pdf#page=105) |
| 7 Gradients and initialization | [110](machine-learning/understanding-deep-learning.pdf#page=110) |
| 7.1 Problem definitions | [110](machine-learning/understanding-deep-learning.pdf#page=110) |
| 7.2 Computing derivatives | [111](machine-learning/understanding-deep-learning.pdf#page=111) |
| 7.3 Toy example | [114](machine-learning/understanding-deep-learning.pdf#page=114) |
| 7.4 Backpropagation algorithm | [117](machine-learning/understanding-deep-learning.pdf#page=117) |
| 7.5 Parameter initialization | [121](machine-learning/understanding-deep-learning.pdf#page=121) |
| 7.6 Example training code | [125](machine-learning/understanding-deep-learning.pdf#page=125) |
| 7.7 Summary | [125](machine-learning/understanding-deep-learning.pdf#page=125) |
| 8 Measuring performance | [132](machine-learning/understanding-deep-learning.pdf#page=132) |
| 8.1 Training a simple model | [132](machine-learning/understanding-deep-learning.pdf#page=132) |
| 8.2 Sources of error | [134](machine-learning/understanding-deep-learning.pdf#page=134) |
| 8.3 Reducing error | [138](machine-learning/understanding-deep-learning.pdf#page=138) |
| 8.4 Double descent | [141](machine-learning/understanding-deep-learning.pdf#page=141) |
| 8.5 Choosing hyperparameters | [146](machine-learning/understanding-deep-learning.pdf#page=146) |
| 8.6 Summary | [147](machine-learning/understanding-deep-learning.pdf#page=147) |
| 9 Regularization | [152](machine-learning/understanding-deep-learning.pdf#page=152) |
| 9.1 Explicit regularization | [152](machine-learning/understanding-deep-learning.pdf#page=152) |
| 9.2 Implicit regularization | [155](machine-learning/understanding-deep-learning.pdf#page=155) |
| 9.3 Heuristics to improve performance | [158](machine-learning/understanding-deep-learning.pdf#page=158) |
| 9.4 Summary | [168](machine-learning/understanding-deep-learning.pdf#page=168) |
| 10 Convolutional networks | [175](machine-learning/understanding-deep-learning.pdf#page=175) |
| 10.1 Invariance and equivariance | [175](machine-learning/understanding-deep-learning.pdf#page=175) |
| 10.2 Convolutional networks for 1D inputs | [177](machine-learning/understanding-deep-learning.pdf#page=177) |
| 10.3 Convolutional networks for 2D inputs | [184](machine-learning/understanding-deep-learning.pdf#page=184) |
| 10.4 Downsampling and upsampling | [185](machine-learning/understanding-deep-learning.pdf#page=185) |
| 10.5 Applications | [188](machine-learning/understanding-deep-learning.pdf#page=188) |
| 10.6 Summary | [193](machine-learning/understanding-deep-learning.pdf#page=193) |
| 11 Residual networks | [200](machine-learning/understanding-deep-learning.pdf#page=200) |
| 11.1 Sequential processing | [200](machine-learning/understanding-deep-learning.pdf#page=200) |
| 11.2 Residual connections and residual blocks | [203](machine-learning/understanding-deep-learning.pdf#page=203) |
| 11.3 Exploding gradients in residual networks | [206](machine-learning/understanding-deep-learning.pdf#page=206) |
| 11.4 Batch normalization | [206](machine-learning/understanding-deep-learning.pdf#page=206) |
| 11.5 Common residual architectures | [209](machine-learning/understanding-deep-learning.pdf#page=209) |
| 11.6 Why do nets with residual connections perform so well? | [213](machine-learning/understanding-deep-learning.pdf#page=213) |
| 11.7 Summary | [213](machine-learning/understanding-deep-learning.pdf#page=213) |
| 12 Transformers | [221](machine-learning/understanding-deep-learning.pdf#page=221) |
| 12.1 Processing text data | [221](machine-learning/understanding-deep-learning.pdf#page=221) |
| 12.2 Dot-product self-attention | [222](machine-learning/understanding-deep-learning.pdf#page=222) |
| 12.3 Extensions to dot-product self-attention | [227](machine-learning/understanding-deep-learning.pdf#page=227) |
| 12.4 Transformer layers | [229](machine-learning/understanding-deep-learning.pdf#page=229) |
| 12.5 Transformers for natural language processing | [230](machine-learning/understanding-deep-learning.pdf#page=230) |
| 12.6 Encoder model example: BERT | [233](machine-learning/understanding-deep-learning.pdf#page=233) |
| 12.7 Decoder model example: GPT3 | [236](machine-learning/understanding-deep-learning.pdf#page=236) |
| 12.8 Encoder-decoder model example: machine translation | [240](machine-learning/understanding-deep-learning.pdf#page=240) |
| 12.9 Transformers for long sequences | [241](machine-learning/understanding-deep-learning.pdf#page=241) |
| 12.10 Transformers for images | [242](machine-learning/understanding-deep-learning.pdf#page=242) |
| 12.11 Summary | [246](machine-learning/understanding-deep-learning.pdf#page=246) |
| 13 Graph neural networks | [254](machine-learning/understanding-deep-learning.pdf#page=254) |
| 13.1 What is a graph? | [254](machine-learning/understanding-deep-learning.pdf#page=254) |
| 13.2 Graph representation | [257](machine-learning/understanding-deep-learning.pdf#page=257) |
| 13.3 Graph neural networks, tasks, and loss functions | [259](machine-learning/understanding-deep-learning.pdf#page=259) |
| 13.4 Graph convolutional networks | [262](machine-learning/understanding-deep-learning.pdf#page=262) |
| 13.5 Example: graph classification | [265](machine-learning/understanding-deep-learning.pdf#page=265) |
| 13.6 Inductive vs. transductive models | [266](machine-learning/understanding-deep-learning.pdf#page=266) |
| 13.7 Example: node classification | [267](machine-learning/understanding-deep-learning.pdf#page=267) |
| 13.8 Layers for graph convolutional networks | [270](machine-learning/understanding-deep-learning.pdf#page=270) |
| 13.9 Edge graphs | [274](machine-learning/understanding-deep-learning.pdf#page=274) |
| 13.10 Summary | [275](machine-learning/understanding-deep-learning.pdf#page=275) |
| 14 Unsupervised learning | [282](machine-learning/understanding-deep-learning.pdf#page=282) |
| 14.1 Taxonomy of unsupervised learning models | [282](machine-learning/understanding-deep-learning.pdf#page=282) |
| 14.2 What makes a good generative model? | [283](machine-learning/understanding-deep-learning.pdf#page=283) |
| 14.3 Quantifying performance | [285](machine-learning/understanding-deep-learning.pdf#page=285) |
| 14.4 Summary | [287](machine-learning/understanding-deep-learning.pdf#page=287) |
| 15 Generative Adversarial Networks | [289](machine-learning/understanding-deep-learning.pdf#page=289) |
| 15.1 Discrimination as a signal | [289](machine-learning/understanding-deep-learning.pdf#page=289) |
| 15.2 Improving stability | [294](machine-learning/understanding-deep-learning.pdf#page=294) |
| 15.3 Progressive growing, minibatch discrimination, and truncation | [300](machine-learning/understanding-deep-learning.pdf#page=300) |
| 15.4 Conditional generation | [302](machine-learning/understanding-deep-learning.pdf#page=302) |
| 15.5 Image translation | [304](machine-learning/understanding-deep-learning.pdf#page=304) |
| 15.6 StyleGAN | [309](machine-learning/understanding-deep-learning.pdf#page=309) |
| 15.7 Summary | [311](machine-learning/understanding-deep-learning.pdf#page=311) |
| 16 Normalizing flows | [317](machine-learning/understanding-deep-learning.pdf#page=317) |
| 16.1 1D example | [317](machine-learning/understanding-deep-learning.pdf#page=317) |
| 16.2 General case | [320](machine-learning/understanding-deep-learning.pdf#page=320) |
| 16.3 Invertible network layers | [322](machine-learning/understanding-deep-learning.pdf#page=322) |
| 16.4 Multi-scale flows | [330](machine-learning/understanding-deep-learning.pdf#page=330) |
| 16.5 Applications | [331](machine-learning/understanding-deep-learning.pdf#page=331) |
| 16.6 Summary | [334](machine-learning/understanding-deep-learning.pdf#page=334) |
| 17 Variational autoencoders | [340](machine-learning/understanding-deep-learning.pdf#page=340) |
| 17.1 Latent variable models | [340](machine-learning/understanding-deep-learning.pdf#page=340) |
| 17.2 Nonlinear latent variable model | [341](machine-learning/understanding-deep-learning.pdf#page=341) |
| 17.3 Training | [344](machine-learning/understanding-deep-learning.pdf#page=344) |
| 17.4 ELBO properties | [347](machine-learning/understanding-deep-learning.pdf#page=347) |
| 17.5 Variational approximation | [349](machine-learning/understanding-deep-learning.pdf#page=349) |
| 17.6 The variational autoencoder | [349](machine-learning/understanding-deep-learning.pdf#page=349) |
| 17.7 The reparameterization trick | [352](machine-learning/understanding-deep-learning.pdf#page=352) |
| 17.8 Applications | [353](machine-learning/understanding-deep-learning.pdf#page=353) |
| 17.9 Summary | [356](machine-learning/understanding-deep-learning.pdf#page=356) |
| 18 Diffusion models | [362](machine-learning/understanding-deep-learning.pdf#page=362) |
| 18.1 Overview | [362](machine-learning/understanding-deep-learning.pdf#page=362) |
| 18.2 Encoder (forward process) | [363](machine-learning/understanding-deep-learning.pdf#page=363) |
| 18.3 Decoder model (reverse process) | [369](machine-learning/understanding-deep-learning.pdf#page=369) |
| 18.4 Training | [370](machine-learning/understanding-deep-learning.pdf#page=370) |
| 18.5 Reparameterization of loss function | [374](machine-learning/understanding-deep-learning.pdf#page=374) |
| 18.6 Implementation | [376](machine-learning/understanding-deep-learning.pdf#page=376) |
| 18.7 Summary | [381](machine-learning/understanding-deep-learning.pdf#page=381) |
| 19 Reinforcement learning | [387](machine-learning/understanding-deep-learning.pdf#page=387) |
| 19.1 Markov decision processes, returns, and policies | [387](machine-learning/understanding-deep-learning.pdf#page=387) |
| 19.2 Expected return | [391](machine-learning/understanding-deep-learning.pdf#page=391) |
| 19.3 Tabular reinforcement learning | [395](machine-learning/understanding-deep-learning.pdf#page=395) |
| 19.4 Fitted Q-learning | [399](machine-learning/understanding-deep-learning.pdf#page=399) |
| 19.5 Policy gradient methods | [402](machine-learning/understanding-deep-learning.pdf#page=402) |
| 19.6 Actor-critic methods | [407](machine-learning/understanding-deep-learning.pdf#page=407) |
| 19.7 Offline reinforcement learning | [408](machine-learning/understanding-deep-learning.pdf#page=408) |
| 19.8 Summary | [409](machine-learning/understanding-deep-learning.pdf#page=409) |
| 20 Why does deep learning work? | [415](machine-learning/understanding-deep-learning.pdf#page=415) |
| 20.1 The case against deep learning | [415](machine-learning/understanding-deep-learning.pdf#page=415) |
| 20.2 Factors that influence fitting performance | [416](machine-learning/understanding-deep-learning.pdf#page=416) |
| 20.3 Properties of loss functions | [420](machine-learning/understanding-deep-learning.pdf#page=420) |
| 20.4 Factors that determine generalization | [424](machine-learning/understanding-deep-learning.pdf#page=424) |
| 20.5 Do we need so many parameters? | [428](machine-learning/understanding-deep-learning.pdf#page=428) |
| 20.6 Do networks have to be deep? | [431](machine-learning/understanding-deep-learning.pdf#page=431) |
| 20.7 Summary | [432](machine-learning/understanding-deep-learning.pdf#page=432) |
| 21 Deep learning and ethics | [434](machine-learning/understanding-deep-learning.pdf#page=434) |
| 21.1 Value alignment | [434](machine-learning/understanding-deep-learning.pdf#page=434) |
| 21.2 Intentional misuse | [440](machine-learning/understanding-deep-learning.pdf#page=440) |
| 21.3 Other social, ethical, and professional issues | [442](machine-learning/understanding-deep-learning.pdf#page=442) |
| 21.4 Case study | [444](machine-learning/understanding-deep-learning.pdf#page=444) |
| 21.5 The value-free ideal of science | [445](machine-learning/understanding-deep-learning.pdf#page=445) |
| 21.6 Responsible AI research as a collective action problem | [446](machine-learning/understanding-deep-learning.pdf#page=446) |
| 21.7 Ways forward | [447](machine-learning/understanding-deep-learning.pdf#page=447) |
| 21.8 Summary | [448](machine-learning/understanding-deep-learning.pdf#page=448) |
| Appendix A: Notation | [450](machine-learning/understanding-deep-learning.pdf#page=450) |
| Appendix B: Mathematics | [453](machine-learning/understanding-deep-learning.pdf#page=453) |
| Functions | [453](machine-learning/understanding-deep-learning.pdf#page=453) |
| Binomial coefficients | [455](machine-learning/understanding-deep-learning.pdf#page=455) |
| Vector, matrices, and tensors | [456](machine-learning/understanding-deep-learning.pdf#page=456) |
| Special types of matrix | [459](machine-learning/understanding-deep-learning.pdf#page=459) |
| Matrix calculus | [461](machine-learning/understanding-deep-learning.pdf#page=461) |
| Appendix C: Probability | [462](machine-learning/understanding-deep-learning.pdf#page=462) |
| Random variables and probability distributions | [462](machine-learning/understanding-deep-learning.pdf#page=462) |
| Expectation | [466](machine-learning/understanding-deep-learning.pdf#page=466) |
| Normal probability distribution | [470](machine-learning/understanding-deep-learning.pdf#page=470) |
| Sampling | [473](machine-learning/understanding-deep-learning.pdf#page=473) |
| Distances between probability distributions | [473](machine-learning/understanding-deep-learning.pdf#page=473) |
| Bibliography | [476](machine-learning/understanding-deep-learning.pdf#page=476) |
| Index | [527](machine-learning/understanding-deep-learning.pdf#page=527) |

## computer-vision/

### Computer vision textbook

`computer-vision/computer-vision-textbook.pdf`, 667 pages. Simon J. D. Prince, *Computer Vision: Models,
Learning, and Inference*, Cambridge University Press, 2012; this file is the author's draft of 7 July
2012. A published textbook that treats vision as probabilistic modelling: probability and the normal
distribution, learning and inference, regression and classification, graphical models, image
preprocessing, camera geometry, and models for shape, identity, tracking and visual words. Was
`Computer Vision.pdf`. The table is from the PDF's own outline for the parts and chapters, with each
section's page from the printed contents. The printed page number is the PDF page minus 2.

| Chapter or section | PDF page |
| --- | --- |
| 1 Introduction | [17](computer-vision/computer-vision-textbook.pdf#page=17) |
| Part I: Probability | [23](computer-vision/computer-vision-textbook.pdf#page=23) |
| 2 Introduction to probability | [27](computer-vision/computer-vision-textbook.pdf#page=27) |
| 2.1 Random variables | [27](computer-vision/computer-vision-textbook.pdf#page=27) |
| 2.2 Joint probability | [28](computer-vision/computer-vision-textbook.pdf#page=28) |
| 2.3 Marginalization | [29](computer-vision/computer-vision-textbook.pdf#page=29) |
| 2.4 Conditional probability | [30](computer-vision/computer-vision-textbook.pdf#page=30) |
| 2.5 Bayes’ rule | [32](computer-vision/computer-vision-textbook.pdf#page=32) |
| 2.6 Independence | [33](computer-vision/computer-vision-textbook.pdf#page=33) |
| 2.7 Expectation | [33](computer-vision/computer-vision-textbook.pdf#page=33) |
| 3 Common probability distributions | [37](computer-vision/computer-vision-textbook.pdf#page=37) |
| 3.1 Bernoulli distribution | [38](computer-vision/computer-vision-textbook.pdf#page=38) |
| 3.2 Beta distribution | [39](computer-vision/computer-vision-textbook.pdf#page=39) |
| 3.3 Categorical distribution | [40](computer-vision/computer-vision-textbook.pdf#page=40) |
| 3.4 Dirichlet distribution | [41](computer-vision/computer-vision-textbook.pdf#page=41) |
| 3.5 Univariate normal distribution | [42](computer-vision/computer-vision-textbook.pdf#page=42) |
| 3.6 Normal-scaled inverse gamma distribution | [42](computer-vision/computer-vision-textbook.pdf#page=42) |
| 3.7 Multivariate normal distribution | [43](computer-vision/computer-vision-textbook.pdf#page=43) |
| 3.8 Normal inverse Wishart distribution | [44](computer-vision/computer-vision-textbook.pdf#page=44) |
| 3.9 Conjugacy | [44](computer-vision/computer-vision-textbook.pdf#page=44) |
| 4 Fitting probability models | [51](computer-vision/computer-vision-textbook.pdf#page=51) |
| 4.1 Maximum likelihood | [51](computer-vision/computer-vision-textbook.pdf#page=51) |
| 4.2 Maximum a posteriori | [52](computer-vision/computer-vision-textbook.pdf#page=52) |
| 4.3 The Bayesian approach | [52](computer-vision/computer-vision-textbook.pdf#page=52) |
| 4.4 Worked example 1: univariate normal | [53](computer-vision/computer-vision-textbook.pdf#page=53) |
| 4.5 Worked example 2: categorical distribution | [62](computer-vision/computer-vision-textbook.pdf#page=62) |
| 5 The normal distribution | [71](computer-vision/computer-vision-textbook.pdf#page=71) |
| 5.1 Types of covariance matrix | [71](computer-vision/computer-vision-textbook.pdf#page=71) |
| 5.2 Decomposition of covariance | [73](computer-vision/computer-vision-textbook.pdf#page=73) |
| 5.3 Linear transformations of variables | [74](computer-vision/computer-vision-textbook.pdf#page=74) |
| 5.4 Marginal distributions | [74](computer-vision/computer-vision-textbook.pdf#page=74) |
| 5.5 Conditional distributions | [75](computer-vision/computer-vision-textbook.pdf#page=75) |
| 5.6 Product of two normals | [76](computer-vision/computer-vision-textbook.pdf#page=76) |
| 5.7 Change of variable | [77](computer-vision/computer-vision-textbook.pdf#page=77) |
| Part II: Machine learning for machine vision | [81](computer-vision/computer-vision-textbook.pdf#page=81) |
| 6 Learning and inference in vision | [85](computer-vision/computer-vision-textbook.pdf#page=85) |
| 6.1 Computer vision problems | [85](computer-vision/computer-vision-textbook.pdf#page=85) |
| 6.2 Types of model | [86](computer-vision/computer-vision-textbook.pdf#page=86) |
| 6.3 Example 1: regression | [87](computer-vision/computer-vision-textbook.pdf#page=87) |
| 6.4 Example 2: binary classification | [90](computer-vision/computer-vision-textbook.pdf#page=90) |
| 6.5 Which type of model should we use? | [93](computer-vision/computer-vision-textbook.pdf#page=93) |
| 6.6 Applications | [95](computer-vision/computer-vision-textbook.pdf#page=95) |
| 7 Modeling complex data densities | [103](computer-vision/computer-vision-textbook.pdf#page=103) |
| 7.1 Normal classification model | [103](computer-vision/computer-vision-textbook.pdf#page=103) |
| 7.2 Hidden variables | [107](computer-vision/computer-vision-textbook.pdf#page=107) |
| 7.3 Expectation maximization | [108](computer-vision/computer-vision-textbook.pdf#page=108) |
| 7.4 Mixture of Gaussians | [110](computer-vision/computer-vision-textbook.pdf#page=110) |
| 7.5 The t-distribution | [117](computer-vision/computer-vision-textbook.pdf#page=117) |
| 7.6 Factor analysis | [122](computer-vision/computer-vision-textbook.pdf#page=122) |
| 7.7 Combining models | [128](computer-vision/computer-vision-textbook.pdf#page=128) |
| 7.8 Expectation maximization in detail | [129](computer-vision/computer-vision-textbook.pdf#page=129) |
| 7.9 Applications | [134](computer-vision/computer-vision-textbook.pdf#page=134) |
| 8 Regression models | [145](computer-vision/computer-vision-textbook.pdf#page=145) |
| 8.1 Linear regression | [145](computer-vision/computer-vision-textbook.pdf#page=145) |
| 8.2 Bayesian linear regression | [149](computer-vision/computer-vision-textbook.pdf#page=149) |
| 8.3 Non-linear regression | [152](computer-vision/computer-vision-textbook.pdf#page=152) |
| 8.4 Kernels and the kernel trick | [157](computer-vision/computer-vision-textbook.pdf#page=157) |
| 8.5 Gaussian process regression | [158](computer-vision/computer-vision-textbook.pdf#page=158) |
| 8.6 Sparse linear regression | [159](computer-vision/computer-vision-textbook.pdf#page=159) |
| 8.7 Dual linear regression | [163](computer-vision/computer-vision-textbook.pdf#page=163) |
| 8.8 Relevance vector regression | [165](computer-vision/computer-vision-textbook.pdf#page=165) |
| 8.9 Regression to multivariate data | [167](computer-vision/computer-vision-textbook.pdf#page=167) |
| 8.10 Applications | [167](computer-vision/computer-vision-textbook.pdf#page=167) |
| 9 Classification models | [173](computer-vision/computer-vision-textbook.pdf#page=173) |
| 9.1 Logistic regression | [173](computer-vision/computer-vision-textbook.pdf#page=173) |
| 9.2 Bayesian logistic regression | [178](computer-vision/computer-vision-textbook.pdf#page=178) |
| 9.3 Non-linear logistic regression | [183](computer-vision/computer-vision-textbook.pdf#page=183) |
| 9.4 Dual logistic regression | [185](computer-vision/computer-vision-textbook.pdf#page=185) |
| 9.5 Kernel logistic regression | [187](computer-vision/computer-vision-textbook.pdf#page=187) |
| 9.6 Relevance vector classification | [188](computer-vision/computer-vision-textbook.pdf#page=188) |
| 9.7 Incremental fitting and boosting | [192](computer-vision/computer-vision-textbook.pdf#page=192) |
| 9.8 Classification trees | [196](computer-vision/computer-vision-textbook.pdf#page=196) |
| 9.9 Multi-class logistic regression | [199](computer-vision/computer-vision-textbook.pdf#page=199) |
| 9.10 Random trees, forests, and ferns | [200](computer-vision/computer-vision-textbook.pdf#page=200) |
| 9.11 Relation to non-probabilistic models | [202](computer-vision/computer-vision-textbook.pdf#page=202) |
| 9.12 Applications | [203](computer-vision/computer-vision-textbook.pdf#page=203) |
| Part III: Connecting local models | [215](computer-vision/computer-vision-textbook.pdf#page=215) |
| 10 Graphical models | [219](computer-vision/computer-vision-textbook.pdf#page=219) |
| 10.1 Conditional independence | [219](computer-vision/computer-vision-textbook.pdf#page=219) |
| 10.2 Directed graphical models | [221](computer-vision/computer-vision-textbook.pdf#page=221) |
| 10.3 Undirected graphical models | [225](computer-vision/computer-vision-textbook.pdf#page=225) |
| 10.4 Comparing directed and undirected graphical models | [227](computer-vision/computer-vision-textbook.pdf#page=227) |
| 10.5 Graphical models in computer vision | [229](computer-vision/computer-vision-textbook.pdf#page=229) |
| 10.6 Inference in models with many unknowns | [231](computer-vision/computer-vision-textbook.pdf#page=231) |
| 10.7 Drawing samples | [233](computer-vision/computer-vision-textbook.pdf#page=233) |
| 10.8 Learning | [235](computer-vision/computer-vision-textbook.pdf#page=235) |
| 11 Models for chains and trees | [245](computer-vision/computer-vision-textbook.pdf#page=245) |
| 11.1 Models for chains | [246](computer-vision/computer-vision-textbook.pdf#page=246) |
| 11.2 MAP inference for chains | [248](computer-vision/computer-vision-textbook.pdf#page=248) |
| 11.3 MAP inference for trees | [253](computer-vision/computer-vision-textbook.pdf#page=253) |
| 11.4 Marginal posterior inference for chains | [256](computer-vision/computer-vision-textbook.pdf#page=256) |
| 11.5 Marginal posterior inference for trees | [264](computer-vision/computer-vision-textbook.pdf#page=264) |
| 11.6 Learning in chains and trees | [264](computer-vision/computer-vision-textbook.pdf#page=264) |
| 11.7 Beyond chains and trees | [265](computer-vision/computer-vision-textbook.pdf#page=265) |
| 11.8 Applications | [268](computer-vision/computer-vision-textbook.pdf#page=268) |
| 12 Models for grids | [281](computer-vision/computer-vision-textbook.pdf#page=281) |
| 12.1 Markov random fields | [282](computer-vision/computer-vision-textbook.pdf#page=282) |
| 12.2 MAP inference for binary pairwise MRFs | [286](computer-vision/computer-vision-textbook.pdf#page=286) |
| 12.3 MAP inference for multi-label pairwise MRFs | [295](computer-vision/computer-vision-textbook.pdf#page=295) |
| 12.4 Multi-label MRFs with non-convex potentials | [298](computer-vision/computer-vision-textbook.pdf#page=298) |
| 12.5 Conditional random fields | [302](computer-vision/computer-vision-textbook.pdf#page=302) |
| 12.6 Higher order models | [305](computer-vision/computer-vision-textbook.pdf#page=305) |
| 12.7 Directed models for grids | [306](computer-vision/computer-vision-textbook.pdf#page=306) |
| 12.8 Applications | [306](computer-vision/computer-vision-textbook.pdf#page=306) |
| Part IV: Preprocessing | [323](computer-vision/computer-vision-textbook.pdf#page=323) |
| 13 Image preprocessing and feature extraction | [327](computer-vision/computer-vision-textbook.pdf#page=327) |
| 13.1 Per-pixel transformations | [327](computer-vision/computer-vision-textbook.pdf#page=327) |
| 13.2 Edges, corners, and interest points | [338](computer-vision/computer-vision-textbook.pdf#page=338) |
| 13.3 Descriptors | [343](computer-vision/computer-vision-textbook.pdf#page=343) |
| 13.4 Dimensionality reduction | [347](computer-vision/computer-vision-textbook.pdf#page=347) |
| Part V: Models for geometry | [357](computer-vision/computer-vision-textbook.pdf#page=357) |
| 14 The pinhole camera | [361](computer-vision/computer-vision-textbook.pdf#page=361) |
| 14.1 The pinhole camera | [361](computer-vision/computer-vision-textbook.pdf#page=361) |
| 14.2 Three geometric problems | [369](computer-vision/computer-vision-textbook.pdf#page=369) |
| 14.3 Homogeneous coordinates | [373](computer-vision/computer-vision-textbook.pdf#page=373) |
| 14.4 Learning extrinsic parameters | [375](computer-vision/computer-vision-textbook.pdf#page=375) |
| 14.5 Learning intrinsic parameters | [377](computer-vision/computer-vision-textbook.pdf#page=377) |
| 14.6 Inferring 3D world points | [378](computer-vision/computer-vision-textbook.pdf#page=378) |
| 14.7 Applications | [380](computer-vision/computer-vision-textbook.pdf#page=380) |
| 15 Models for transformations | [391](computer-vision/computer-vision-textbook.pdf#page=391) |
| 15.1 2D transformation models | [391](computer-vision/computer-vision-textbook.pdf#page=391) |
| 15.2 Learning in transformation models | [398](computer-vision/computer-vision-textbook.pdf#page=398) |
| 15.3 Inference in transformation models | [403](computer-vision/computer-vision-textbook.pdf#page=403) |
| 15.4 Three geometric problems for planes | [404](computer-vision/computer-vision-textbook.pdf#page=404) |
| 15.5 Transformations between images | [409](computer-vision/computer-vision-textbook.pdf#page=409) |
| 15.6 Robust learning of transformations | [412](computer-vision/computer-vision-textbook.pdf#page=412) |
| 15.7 Applications | [417](computer-vision/computer-vision-textbook.pdf#page=417) |
| 16 Multiple cameras | [425](computer-vision/computer-vision-textbook.pdf#page=425) |
| 16.1 Two-view geometry | [426](computer-vision/computer-vision-textbook.pdf#page=426) |
| 16.2 The essential matrix | [429](computer-vision/computer-vision-textbook.pdf#page=429) |
| 16.3 The fundamental matrix | [434](computer-vision/computer-vision-textbook.pdf#page=434) |
| 16.4 Two-view reconstruction pipeline | [437](computer-vision/computer-vision-textbook.pdf#page=437) |
| 16.5 Rectification | [441](computer-vision/computer-vision-textbook.pdf#page=441) |
| 16.6 Multi-view reconstruction | [445](computer-vision/computer-vision-textbook.pdf#page=445) |
| 16.7 Applications | [449](computer-vision/computer-vision-textbook.pdf#page=449) |
| Part VI: Models for vision | [459](computer-vision/computer-vision-textbook.pdf#page=459) |
| 17 Models for shape | [463](computer-vision/computer-vision-textbook.pdf#page=463) |
| 17.1 Shape and its representation | [464](computer-vision/computer-vision-textbook.pdf#page=464) |
| 17.2 Snakes | [465](computer-vision/computer-vision-textbook.pdf#page=465) |
| 17.3 Shape templates | [470](computer-vision/computer-vision-textbook.pdf#page=470) |
| 17.4 Statistical shape models | [473](computer-vision/computer-vision-textbook.pdf#page=473) |
| 17.5 Subspace shape models | [477](computer-vision/computer-vision-textbook.pdf#page=477) |
| 17.6 Three-dimensional shape models | [484](computer-vision/computer-vision-textbook.pdf#page=484) |
| 17.7 Statistical models for shape and appearance | [484](computer-vision/computer-vision-textbook.pdf#page=484) |
| 17.8 Non-Gaussian statistical shape models | [489](computer-vision/computer-vision-textbook.pdf#page=489) |
| 17.9 Articulated models | [494](computer-vision/computer-vision-textbook.pdf#page=494) |
| 17.10 Applications | [495](computer-vision/computer-vision-textbook.pdf#page=495) |
| 18 Models for style and identity | [505](computer-vision/computer-vision-textbook.pdf#page=505) |
| 18.1 Subspace identity model | [508](computer-vision/computer-vision-textbook.pdf#page=508) |
| 18.2 Probabilistic linear discriminant analysis | [516](computer-vision/computer-vision-textbook.pdf#page=516) |
| 18.3 Non-linear identity models | [519](computer-vision/computer-vision-textbook.pdf#page=519) |
| 18.4 Asymmetric bilinear models | [520](computer-vision/computer-vision-textbook.pdf#page=520) |
| 18.5 Symmetric bilinear and multilinear models | [526](computer-vision/computer-vision-textbook.pdf#page=526) |
| 18.6 Applications | [530](computer-vision/computer-vision-textbook.pdf#page=530) |
| 19 Temporal models | [539](computer-vision/computer-vision-textbook.pdf#page=539) |
| 19.1 Temporal estimation framework | [539](computer-vision/computer-vision-textbook.pdf#page=539) |
| 19.2 Kalman filter | [542](computer-vision/computer-vision-textbook.pdf#page=542) |
| 19.3 Extended Kalman filter | [552](computer-vision/computer-vision-textbook.pdf#page=552) |
| 19.4 Unscented Kalman filter | [556](computer-vision/computer-vision-textbook.pdf#page=556) |
| 19.5 Particle filtering | [560](computer-vision/computer-vision-textbook.pdf#page=560) |
| 19.6 Applications | [565](computer-vision/computer-vision-textbook.pdf#page=565) |
| 20 Models for visual words | [573](computer-vision/computer-vision-textbook.pdf#page=573) |
| 20.1 Images as collections of visual words | [573](computer-vision/computer-vision-textbook.pdf#page=573) |
| 20.2 Bag of words | [575](computer-vision/computer-vision-textbook.pdf#page=575) |
| 20.3 Latent Dirichlet allocation | [578](computer-vision/computer-vision-textbook.pdf#page=578) |
| 20.4 Single author-topic model | [584](computer-vision/computer-vision-textbook.pdf#page=584) |
| 20.5 Constellation models | [587](computer-vision/computer-vision-textbook.pdf#page=587) |
| 20.6 Scene models | [592](computer-vision/computer-vision-textbook.pdf#page=592) |
| 20.7 Applications | [592](computer-vision/computer-vision-textbook.pdf#page=592) |
| Part VII: Appendices | [599](computer-vision/computer-vision-textbook.pdf#page=599) |
| Appendix A Notation | [601](computer-vision/computer-vision-textbook.pdf#page=601) |
| Appendix B Optimization | [603](computer-vision/computer-vision-textbook.pdf#page=603) |
| Appendix C Linear algebra | [615](computer-vision/computer-vision-textbook.pdf#page=615) |
