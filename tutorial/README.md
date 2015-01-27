# Welcome to The Romnomnom Tutorial!

We begin with `/tutorial/repl.py` ... a _barely_ functioning Roman Numeral toy language implementation.

```
$ python3 tutorial/repl.py
tutorial> I
1
tutorial> IIIII
5
tutorial> IIIIIIIII
9
tutorial>
```

This tutorial will guide and hint you towards a rich, full-featured Roman Numeral toy language implementation like the
one found in the project `/src/` directory.

## Goals

Implement: 

- All the Numerals! The template works for the Numeral `I` out of the box, but what about the rest?
- All the [rules](https://projecteuler.net/about=roman_numerals)! The template doesn't enforce _any_ rules (characters, token order, frequency ...).
- Compiler Exceptions! What should happen when a rule is broken? Can your error message point to where it happened?
- A clean exit! Once the REPL starts ... can we exit it gracefully when we're done?

Feel free to refer to the `/src/` implementation for hints along the way, and compare results from running the tutorial
REPL to results with the same input from the reference implementation.

## No "right" in Compilers

There's no "right" solution to any of the goals, so experiment at will! There are only "correct" or "incorrect" results.
