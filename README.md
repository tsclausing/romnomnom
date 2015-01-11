# Romnomnom

A simple compiler/interpreter example using Roman Numerals following the Project Euler 
[rules](https://projecteuler.net/about=roman_numerals).

This repo is supplemental material for project [pypethon](https://github.com/tsclausing/pypethon) with the goal of 
providing a _simple_ compiler and interpreter example. Romnomnom compiles Roman Numerals into Python bytecode and 
includes a tiny REPL for evaluating the compiled code interactively:

```
$ python3 romnomnom
> I
1
> II
2
> III
3
> IV
4
> V
5
```

## RTFS? TL;DR. ¯&#92;&#95;(ツ)&#95;/¯ 

Romnomnom weighs in around 250 lines of code. Hopefully it's a nice, easy read. And maybe even easier after scrolling
through this README. The diagram below explains what's happening in the code and provides plenty of context before
working through the [pypethon](https://github.com/tsclausing/pypethon) tutorial.

At a high level, here's how a simple compiler and/or interpreter might work:

![compiler](https://cloud.githubusercontent.com/assets/542163/5694503/56475658-9925-11e4-91af-0d6de3611c98.png)

Let's work through the diagram above using the following example from the REPL:

```
$ python3 romnomnom
> XLII
42
```

### 1. lex(source) -> tokens

Open `src/romnomnom/lexer.py`

### 2. parse(tokens) -> ilr

Open `src/romnomnom/parser.py`

### 3. translate(ilr) -> target

Open `src/romnomnom/translator.py`


## The REPL

Open `./romnomnom`
