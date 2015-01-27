# Romnomnom

A simple REPL-Compiler-Interpreter example using Roman Numerals following the Project Euler 
[rules](https://projecteuler.net/about=roman_numerals).

This repo is supplemental material for project [pypethon](https://github.com/tsclausing/pypethon) with the goal of 
providing a _simple_ compiler and interpreter example. Romnomnom compiles Roman Numerals into Python bytecode and 
includes a tiny REPL for evaluating the compiled code interactively:

```bash
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

## Prefer to Work Through a Tutorial?

The Romnomnom project includes a [self-guided tutorial](https://github.com/tsclausing/romnomnom/tree/master/tutorial).
The tutorial provides the starting point for a Romnomnom implementation in a single [file](https://github.com/tsclausing/romnomnom/blob/master/tutorial/repl.py)
and encourages the reader to implement the full scope of Roman Numeral [rules](https://projecteuler.net/about=roman_numerals) 
that Romnomnom supports.

## Prefer to Read the Source? TL;DR. ¯&#92;&#95;(ツ)&#95;/¯ 

Romnomnom weighs in around 250 lines of code. Hopefully it's a nice, easy read. And maybe even easier after scrolling
through this README. The diagrams below explain what's happening in the code and provide plenty of context which will
be helpful before working through the [pypethon](https://github.com/tsclausing/pypethon) tutorial.

# The Romnomnom Compiler

> A compiler is a computer program (or set of programs) that transforms source code written in a programming language 
(the source language) into another computer language (the target language). - [wikipedia.org/Compiler](http://en.wikipedia.org/wiki/Compiler)

![compiler blackbox](https://cloud.githubusercontent.com/assets/542163/5695921/98f87dee-997d-11e4-9cde-82b4017c20f7.png)

That's it. In Romnomnom, our source language is the language of Roman Numerals and our target language is executable 
Python bytecode.

The three common patterns found in compilers that we'll explore in Romnomnom are 
[lexing](http://en.wikipedia.org/wiki/Lexical_analysis), 
[parsing](http://en.wikipedia.org/wiki/Parsing), 
and [code generation](http://en.wikipedia.org/wiki/Code_generation_%28compiler%29). These three patterns make up the 
three "phases" of the compiler and can be seen composed together plainly in `src/romnomnom/compiler.py`:

```python
def compile(source):
    return generate(parse(lex(source)))
```

Looking a little bit closer at each of the phases, here's how a simple compiler and
[interpreter](http://en.wikipedia.org/wiki/Interpreter_%28computing%29) might work together:

![compiler](https://cloud.githubusercontent.com/assets/542163/5695988/2b86ee9a-9981-11e4-8609-c86f853c012b.png)

This is actually _exactly_ how Romnomnom works (and, basically, how Python works). 

> There are two general approaches to programming language implementation:
> 
> * Interpretation: An interpreter takes as input a program in some language, and performs the actions written in that 
> language on some machine.
> * Compilation: A compiler takes as input a program in some language, and translates that program into some other 
> language, which may serve as input to another interpreter or another compiler.
> 
> Notice that a compiler does not directly execute the program. Ultimately, in order to execute a program via 
> compilation, it must be translated into a form that can serve as input to an interpreter. - [wikipedia.org/Programming_language_implementation](http://en.wikipedia.org/wiki/Programming_language_implementation)

Perfect! Let's work through the diagram above in detail using the following Romnomnom REPL session as an example:

```bash
$ python3 romnomnom
> XLII
42
> 
```

![repl](https://cloud.githubusercontent.com/assets/542163/5734994/645a0ad6-9b84-11e4-9747-b2f367a35dfc.png)

## 1. lex(source) -> tokens

Code: [src/romnomnom/lexer.py](https://github.com/tsclausing/romnomnom/blob/master/src/romnomnom/lexer.py)

Related terminology: 
Lexing, 
[Lexical Analysis](http://en.wikipedia.org/wiki/Lexical_analysis), 
Scanning, 
[Tokenization](http://en.wikipedia.org/wiki/Tokenization_%28lexical_analysis%29)

## 2. parse(tokens) -> ilr

Code: [src/romnomnom/parser.py](https://github.com/tsclausing/romnomnom/blob/master/src/romnomnom/parser.py)

Related terminology:
[Parsing](http://en.wikipedia.org/wiki/Parsing),
Syntactic Analysis, 
[Semantic Analysis](http://en.wikipedia.org/w/index.php?title=Semantic_analysis_%28compilers%29&redirect=no)

## 3. generate(ilr) -> target

Code: [src/romnomnom/generator.py](https://github.com/tsclausing/romnomnom/blob/master/src/romnomnom/generator.py)

Related terminology:
[Code Generation](http://en.wikipedia.org/wiki/Code_generation_%28compiler%29), 
[Intermediate Representation](http://en.wikipedia.org/wiki/Intermediate_language#Intermediate_representation)


# The Romnomnom REPL

Code: [./romnomnom](https://github.com/tsclausing/romnomnom/blob/master/romnomnom)

Related terminology: 
[Read Eval Print Loop](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop),
[Interpreter](http://en.wikipedia.org/wiki/Interpreter_%28computing%29)
