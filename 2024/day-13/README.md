# Problem Setup

Each claw machine can be modeled as a system of two linear equations, based on the movement of buttons **A** and **B**, and the coordinates of the prize.

For example, consider this claw machine:

```yml
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
```

This gives us the equations:

$$
94a + 22b = 8400 \\
34a + 67b = 5400
$$

Here:

- `a` = number of times we press Button A
- `b` = number of times we press Button B

The goal: solve for `(a, b)`.

## Step-by-Step Solution

We start with:

$$
(1)\ 94a + 22b = 8400 \\
(2)\ 34a + 67b = 5400
$$

### 1. Eliminate `a`

Scale both equations so that the coefficients of `a` match:

$$
34 \cdot (1):\ 3196a + 748b = 285600 \\
94 \cdot (2):\ 3196a + 6298b = 507600
$$

Subtract the second from the first:

$$
(3196a - 3196a) + (748b - 6298b) = 285600 - 507600 \\
-5550b = -222000 \\
b = \frac{222000}{5550} = 40
$$

### 2. Solve for `a`

Substitute `b=40` into equation (1):

$$
94a + 22(40) = 8400 \\
94a + 880 = 8400 \\
94a = 7520 \\
a = \frac{7520}{94} = 80
$$

✅ Final solution:

$$
a = 80,\quad b = 40
$$

One thing to notice here is that the value of a and be can be negative and/or non integer number (e.g. 123.456) so we have to check that.
