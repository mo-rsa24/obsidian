# The toy tables and worked moves of "Why The Normaliser Has No Slope In X", computed, never estimated.
import math

def h(u):                       # the N(3, 4) height without its front factor
    return math.exp(-(u - 3) ** 2 / 8)

def log_Z(beta):                # log sqrt(8 pi / beta)
    return 0.5 * (math.log(8 * math.pi) - math.log(beta))

def Z_by_rectangles(x, beta, du=0.01):     # x is handed in and never used
    return sum(h(-17 + k * du) ** beta for k in range(4001)) * du

print("table 1: log pi_2 with and without log Z_2")
for x in (3, 5, 5.01, 7):
    w = -(x - 3) ** 2 / 4
    print(f"  x {x:<5} without Z {w:.6f}  log Z_2 {log_Z(2):.6f}  log pi_2 {w - log_Z(2):.6f}  gap {w - (w - log_Z(2)):.6f}")

print("table 2: Z_beta by rectangles, handed a point it never uses")
for x, beta in ((0, 2), (5, 2), (7, 2), (5, 1), (5, 4)):
    Z = Z_by_rectangles(x, beta)
    print(f"  x {x}  beta {beta}  rectangles {Z:.6f}  sqrt(8 pi / beta) {math.sqrt(8 * math.pi / beta):.6f}  log Z {math.log(Z):.6f}")

print("table 3: difference quotients at x = 5, beta = 2")
for d in (1, 0.1, 0.01, 0.001):
    a, b = -(5 - 3) ** 2 / 4 - log_Z(2), -(5 + d - 3) ** 2 / 4 - log_Z(2)
    a0, b0 = -(5 - 3) ** 2 / 4, -(5 + d - 3) ** 2 / 4
    print(f"  step {d:<6} log pi(5+step) {b:.6f}  difference {b - a:.6f}  quotient {(b - a) / d:.6f}"
          f"  without Z {(b0 - a0) / d:.6f}  log Z quotient {(log_Z(2) - log_Z(2)) / d:.6f}  -1 - step/4 {-1 - d / 4:.6f}")

print("table 4: log Z_beta along beta, and the x-slope at 5 that never sees it")
for beta in (0.5, 1, 2, 2.01, 4):
    print(f"  beta {beta:<5} log Z {log_Z(beta):.6f}  slope -1/(2 beta) {-1 / (2 * beta):.6f}  beta * score(5) {beta * -(5 - 3) / 4:.6f}")

print("worked moves")
print(f"  score(5) {-(5 - 3) / 4:.6f}, times beta = 2: {2 * -(5 - 3) / 4:.6f}")
print(f"  area under h^2 without dividing by Z_2: {Z_by_rectangles(5, 2):.6f}; after dividing: {Z_by_rectangles(5, 2) / math.exp(log_Z(2)):.6f}")
print(f"  log Z_2 without the 1/2: {math.log(8 * math.pi) - math.log(2):.6f}, its beta-slope -1/beta at 2: {-1 / 2:.6f}")
print(f"  Z_2 = sqrt(8 pi / 2) {math.sqrt(4 * math.pi):.6f}; without the square root 8 pi / 2 = {4 * math.pi:.6f}, log {math.log(4 * math.pi):.6f}")
print(f"  2D: one factor sqrt(2 pi / 2) = {math.sqrt(math.pi):.6f}; two factors {math.pi:.6f}; one factor only, log {math.log(math.sqrt(math.pi)):.6f}")
print(f"  log Z_2 - log Z_2.01 = {log_Z(2) - log_Z(2.01):.6f}, ratio Z_2.01 / Z_2 = {math.exp(log_Z(2.01) - log_Z(2)):.6f}")
print(f"  ratio Z_4 / Z_1 = {math.exp(log_Z(4) - log_Z(1)):.6f}")
