#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - Linear Time

> Each time `a` iterates, it increments by `n * n`, growing in direct proportion to the increase in input size (`n`).

b) O(n\*log(n)) - Log-linear Time

> The `while` loop is nested in the `for` loop, causing the `for` loop to run input n times, and the `while` loop to run log(n) times.

c) O(n) - Linear Time

> It recursively calls on its own function n times and increments by 2 on each iteration.

## Exercise II

- n story building
- egg drop from all different floors
- if floor >= floor f: egg breaks
- else: egg does not break

* Use binary search to find the value of the floor, starting at the middle.
  (Since we're using BST to start at the middle on each iteration, the runtime is `O(log(n))` because it cuts the time in half.)
* Create an `egg drop` function that checks the value of the current floor.
* If the value of the egg returns `broken`, we will know we were above floor `f`, and eliminate those floor values above it, then use a while loop to keep checking lower and lower floor values until the egg does not return broken (probably using Boolean: broken = True/False).
