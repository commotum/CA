#### Systems Based on Numbers

#### The Notion of Numbers

Much of science has in the past ultimately been concerned with trying to find ways to describe natural systems in terms of numbers.

Yet so far in this book I have said almost nothing about numbers. The purpose of this chapter, however, is to investigate a range of systems that are based on numbers, and to see how their behavior compares with what we have found in other kinds of systems.

The main reason that systems based on numbers have been so popular in traditional science is that so much mathematics has been developed for dealing with them. Indeed, there are certain kinds of systems based on numbers whose behavior has been analyzed almost completely using mathematical methods such as calculus.

Inevitably, however, when such complete analysis is possible, the final behavior that is found is fairly simple.

So can systems that are based on numbers ever in fact yield complex behavior? Looking at most textbooks of science and mathematics, one might well conclude that they cannot. But what one must realize is that the systems discussed in these textbooks are usually ones that are specifically chosen to be amenable to fairly complete analysis, and whose behavior is therefore necessarily quite simple.

And indeed, as we shall see in this chapter, if one ignores the need for analysis and instead just looks at the results of computer experiments, then one quickly finds that even rather simple systems based on numbers can lead to highly complex behavior.

But what is the origin of this complexity? And how does it relate to the complexity we have seen in systems like cellular automata?

One might think that with all the mathematics developed for studying systems based on numbers it would be easy to answer these kinds of questions. But in fact traditional mathematics seems for the most part to lead to more confusion than help.

One basic problem is that numbers are handled very differently in traditional mathematics from the way they are handled in computers and computer programs. For in a sense, traditional mathematics makes a fundamental idealization: it assumes that numbers are elementary objects whose only relevant attribute is their size. But in a computer, numbers are not elementary objects. Instead, they must be represented explicitly, typically by giving a sequence of digits.

The idea of representing a number by a sequence of digits is familiar from everyday life: indeed, our standard way of writing numbers corresponds exactly to giving their digit sequences in base 10. What base 10 means is that for each digit there are 10 possible choices:

Representations of the number 3829 in various bases. The most familiar case is base 10, where starting from the right successive digits correspond to units, tens, hundreds and so on. In base 10, there are 10 possible digits: 0 through 9. In other bases, there are a different number of possible digits. In base 2, as used in practical computers, there are just two possible digits: 0 and 1. And in this base, successive digits starting from the right have coefficients 1, 2, $4 = 2 \times 2$, $8 = 2 \times 2 \times 2$, etc.

- $3829 = 3 \times 1000 + 8 \times 100 + 2 \times 10 + 9 \times 1 = 3829_{10}$
- $3829 = 5 \times 729 + 2 \times 81 + 2 \times 9 + 4 \times 1 = 5224_{9}$
- $3829 = 7 \times 512 + 3 \times 64 + 6 \times 8 + 5 \times 1 = 7365_{8}$
- $3829 = 1 \times 2401 + 4 \times 343 + 1 \times 49 + 1 \times 7 + 0 \times 1 = 14110_{7}$
- $3829 = 2 \times 1296 + 5 \times 216 + 4 \times 36 + 2 \times 6 + 1 \times 1 = 25421_{6}$
- $3829 = 1 \times 3125 + 1 \times 625 + 0 \times 125 + 3 \times 25 + 0 \times 5 + 4 \times 1 = 110304_{5}$
- $3829 = 3 \times 1024 + 2 \times 256 + 3 \times 64 + 3 \times 16 + 1 \times 4 + 1 \times 1 = 323311_{4}$
- $3829 = 1 \times 2187 + 2 \times 729 + 0 \times 243 + 2 \times 81 + 0 \times 27 + 2 \times 9 + 1 \times 3 + 1 \times 1 = 12020211_{3}$
- $3829 = 1 \times 2048 + 1 \times 1024 + 1 \times 512 + 0 \times 256 + 1 \times 128 + 1 \times 64 + 1 \times 32 + 1 \times 16 + 0 \times 8 + 1 \times 4 + 0 \times 2 + 1 \times 1 = 111011110101_{2}$

So what this means is that in a computer numbers are represented by sequences of 0's and 1's, much like sequences of white and black cells in systems like cellular automata. And operations on numbers then correspond to ways of updating sequences of 0's and 1's.

In traditional mathematics, the details of how operations performed on numbers affect sequences of digits are usually considered quite irrelevant. But what we will find in this chapter is that precisely by looking at such details, we will be able to see more clearly how complexity develops in systems based on numbers.

In many cases, the behavior we find looks remarkably similar to what we saw in the previous chapter. Indeed, in the end, despite some confusing suggestions from traditional mathematics, we will discover that the general behavior of systems based on numbers is very similar to the general behavior of simple programs that we have already discussed.

#### Elementary Arithmetic

The operations of elementary arithmetic are so simple that it seems impossible that they could ever lead to behavior of any great complexity. But what we will find in this section is that in fact they can.

To begin, consider what is perhaps the simplest conceivable arithmetic process: start with the number 1 and then just progressively add 1 at each of a sequence of steps.

The result of this process is to generate the successive numbers 1, 2, 3, 4, 5, 6, 7, 8, ... The sizes of these numbers obviously form a very simple progression.

But if one looks not at these overall sizes, but rather at digit sequences, then what one sees is considerably more complicated. And in fact, as the picture on the right demonstrates, these successive digit sequences form a pattern that shows an intricate nested structure.

![](Images/_page_132_Figure_10.jpeg)

Digit sequences of successive numbers written in base 2. The overall pattern has an intricate nested form.

The pictures below show what happens if one adds a number other than 1 at each step. Near the right-hand edge, each pattern is somewhat different. But at an overall level, all the patterns have exactly the same basic nested structure.

![](Images/_page_133_Picture_2.jpeg)

Digit sequences in base 2 of numbers obtained by starting with 1 and then successively adding a constant at each step. All these patterns ultimately have the same overall nested form.

If instead of addition one uses multiplication, however, then the results one gets can be very different. The first picture at the top of the facing page shows what happens if one starts with 1 and then successively multiplies by 2 at each step.

It turns out that if one represents numbers as digit sequences in base 2, then the operation of multiplying by 2 has a very simple effect: it just shifts the digit sequence one place to the left, adding a 0 digit on the right. And as a result, the overall pattern obtained by successive multiplication by 2 has a very simple form.

![](Images/_page_134_Figure_2.jpeg)

![](Images/_page_134_Figure_3.jpeg)

Patterns produced by starting with the number 1, and then successively multiplying by a factor of 2, and a factor of 3. In each case, the digit sequence of the number obtained at each step is shown in base 2. Multiplication by 2 turns out to correspond just to shifting all digits in base 2 one position to the left, so that the overall pattern produced in this case is very simple. But multiplication by 3 yields a much more complicated pattern, as the picture on the right shows. Note that in these pictures the complete numbers obtained at each step correspond respectively to the successive integer powers of 2 and of 3.

But if the multiplication factor at each step is 3, rather than 2, then the pattern obtained is quite different, as the second picture above shows. Indeed, even though the only operation used was just simple multiplication, the final pattern obtained in this case is highly complex.

The picture on the next page shows more steps in the evolution of the system. At a small scale, there are some obvious triangular and other structures, but beyond these the pattern looks essentially random.

So just as in simple programs like cellular automata, it seems that simple systems based on numbers can also yield behavior that is highly complex and apparently random.

But we might imagine that the complexity we see in pictures like the one on the next page must somehow be a consequence of the fact that we are looking at numbers in terms of their digit sequences, and would not occur if we just looked at numbers in terms of their overall size.

A few examples, however, will show that this is not the case.

To begin the first example, consider what happens if one multiplies by 3/2, or 1.5, at each step. Starting with 1, the successive numbers that one obtains in this way are 1, 3/2 = 1.5, 9/4 = 2.25, 27/8 = 3.375, 81/16 = 5.0625, 243/32 = 7.59375, 729/64 = 11.390625, ...

![](Images/_page_135_Figure_2.jpeg)

The first 500 powers of 3, shown in base 2. Some small-scale structure is visible, but on a larger scale the pattern seems for all practical purposes random. Note that the pattern shown here has been truncated at the edge of the page on the left, although in fact the whole pattern continues to expand to the left forever with an average slope of $Log[2, 3] \approx 1.58$.

The picture below shows the digit sequences for these numbers given in base 2. The digits that lie directly below and to the left of the original 1 at the top of the pattern correspond to the whole number part of each successive number (e.g. 3 in 3.375), while the digits that lie to the right correspond to the fractional part (e.g. 0.375 in 3.375).

![](Images/_page_136_Figure_2.jpeg)

Successive powers of 3/2, shown in base 2. Multiplication by 3/2 can be thought of as multiplication by 3 combined with division by 2. But division by 2 just does the opposite of multiplication by 2, so in base 2 it simply shifts all digits one position to the right. The overall pattern is thus a shifted version of the pattern shown on the facing page.

And instead of looking explicitly at the complete pattern of digits, one can consider just finding the size of the fractional part of each successive number. These sizes are plotted at the top of the next page. And the picture shows that they too exhibit the kind of complexity and apparent randomness that is evident at the level of digits.

![](Images/_page_137_Figure_1.jpeg)

Sizes of the fractional parts of successive powers of 3/2. These sizes are completely independent of what base is used to represent the numbers. Only the dots are significant; the shading and lines between them are just included to make the plot easier to read.

The example just given involves numbers with fractional parts. But it turns out that similar phenomena can also be found in systems that involve only whole numbers.

As a first example, consider a slight variation on the operation of multiplying by 3/2 used above: if the number at a particular step is even (divisible by 2), then simply multiply that number by 3/2, getting a whole number as the result. But if the number is odd, then first add 1, so as to get an even number, and only then multiply by 3/2.

`1011010001101001101010101010101010100000`

Results of starting with the number 1, then applying the following rule: if the number at a particular step is even, multiply by 3/2; otherwise, add 1, then multiply by 3/2. This procedure yields a succession of whole numbers whose digit sequences in base 2 are shown at the right. The rightmost digits obtained at each step are shown above. The digit is 0 when the number is even and 1 when it is odd, and, as shown, the digits alternate in a seemingly random way. It turns out that the system described here is closely related to one that arose in studying the register machine shown on page 100. The system here can be represented by the rule $n \rightarrow If[EvenQ[n], 3\,n/2, 3\,(n+1)/2]$, while the one on page 100 follows the rule $n \rightarrow If[EvenQ[n], 3\,n/2, (3\,n+1)/2]$. After the first step these systems give the same sequence of numbers, except for an overall factor of 3.

![](Images/_page_137_Picture_7.jpeg)

This procedure is always guaranteed to give a whole number. And starting with 1, the sequence of numbers one gets is 1, 3, 6, 9, 15, 24, 36, 54, 81, 123, 186, 279, 420, 630, 945, 1419, 2130, 3195, 4794, ...

Some of these numbers are even, while some are odd. But as the results at the bottom of the facing page illustrate, the sequence of which numbers are even and which are odd seems to be completely random.

Despite this randomness, however, the overall sizes of the numbers obtained still grow in a rather regular way. But by changing the procedure just slightly, one can get much less regular growth.

As an example, consider the following procedure: if the number obtained at a particular step is even, then multiply this number by 5/2; otherwise, add 1 and then multiply the result by 1/2.

If one starts with 1, then this procedure simply gives 1 at every step. And indeed with many starting numbers, the procedure yields purely repetitive behavior. But as the picture below shows, it can also give more complicated behavior.

![](Images/_page_138_Figure_6.jpeg)

Results of applying the rule $n \rightarrow If[EvenQ[n], 5 n/2, (n+1)/2]$, starting with different initial choices of $n$. In many cases, the behavior obtained is purely repetitive. But in some cases it is not.

Starting for example with the number 6, the sizes of the numbers obtained on successive steps show a generally increasing trend, but there are considerable fluctuations, and these fluctuations seem to be essentially random. Indeed, even after a million steps, when the

![](Images/_page_139_Figure_1.jpeg)

The results of following the same rule as on the previous page, starting from the value 6. Plotted on the right are the overall sizes of the numbers obtained for the first thousand steps. The plot is on a logarithmic scale, so the height of each point is essentially the length of the digit sequence for the number that it represents, or the width of the row on the left.

number obtained has 48,554 (base 10) digits, there is still no sign of repetition or of any other significant regularity.

So even if one just looks at overall sizes of whole numbers it is still possible to get great complexity in systems based on numbers.

But while complexity is visible at this level, it is usually necessary to go to a more detailed level in order to get any real idea of why it occurs. And indeed what we have found in this section is that if one looks at digit sequences, then one sees complex patterns that are remarkably similar to those produced by systems like cellular automata.

The underlying rules for systems like cellular automata are however usually rather different from those for systems based on numbers. The main point is that the rules for cellular automata are always local: the new color of any particular cell depends only on the previous color of that cell and its immediate neighbors. But in systems based on numbers there is usually no such locality.

One knows from hand calculation that even an operation such as addition can lead to "carry" digits which propagate arbitrarily far to the left. And in fact most simple arithmetic operations have the property that a digit which appears at a particular position in their result can depend on digits that were originally far away from it.

But despite fundamental differences like this in underlying rules, the overall behavior produced by systems based on numbers is still very similar to what one sees for example in cellular automata.

So just like for the various kinds of programs that we discussed in the previous chapter, the details of underlying rules again do not seem to have a crucial effect on the kinds of behavior that can occur.

Indeed, despite the lack of locality in their underlying rules, the pictures below and on the pages that follow show that it is even possible to find systems based on numbers that exhibit something like the localized structures that we saw in cellular automata on page 32.

![](Images/_page_140_Picture_5.jpeg)

An example of a system defined by the following rule: at each step, take the number obtained at that step and write its base 2 digits in reverse order, then add the resulting number to the original one. For many possible starting numbers, the behavior obtained is very simple. This picture shows what happens when one starts with the number 16. After 180 steps, it turns out that all that survives are a few objects that one can view as localized structures.

![](Images/_page_141_Picture_2.jpeg)

A thousand steps in the evolution of a system with the same rule as on the previous page, but now starting with the number 512. Localized structures are visible, but the overall pattern never seems to take on any kind of simple repetitive form.

![](Images/_page_142_Picture_2.jpeg)

Continuation of the pattern on the facing page, starting at the millionth step. The picture shows the right-hand edge of the pattern; the complete pattern extends about 700 times the width of the page to the left.

#### Recursive Sequences

In the previous section, we saw that it is possible to get behavior of considerable complexity just by applying a variety of operations based on simple arithmetic. In this section what I will show is that with the appropriate setup just addition and subtraction turn out to be in a sense the only operations that one needs.

The basic idea is to consider a sequence of numbers in which there is a definite rule for getting the next number in the sequence from previous ones. It is convenient to refer to the first number in each sequence as f[1], the second as f[2], and so on, so that the $n^{th}$ number is denoted f[n]. And with this notation, what the rule does is to specify how f[n] should be calculated from previous numbers in the sequence.

In the simplest cases, f[n] depends only on the number immediately before it in the sequence, denoted f[n-1]. But it is also possible to set up rules in which f[n] depends not only on f[n-1], but also on f[n-2], as well as on numbers still earlier in the sequence.

The table below gives results obtained with a few specific rules. In all the cases shown, these results are quite simple, consisting of sequences that increase uniformly or fluctuate in a purely repetitive way.

![](Images/_page_143_Figure_6.jpeg)

Examples of some simple recursive sequences. The $n^{\text{th}}$ element in each sequence is denoted f[n], and the rule specifies how this element is determined from previous ones. With all the rules shown here, successive elements either increase smoothly or fluctuate in a purely repetitive way. Sequence (c) is the powers of two; (d) is the so-called Fibonacci sequence, related to powers of the golden ratio $(1 + \sqrt{5})/2 \approx 1.618$. All rules of the kind shown here lead to sequences where f[n] can be expressed in terms of a simple sum of powers of the form $a^n$.

But it turns out that with slightly more complicated rules it is possible to get much more complicated behavior. The key idea is to consider rules which look at numbers that are not just a fixed distance back in the sequence. And what this means is that instead of depending only on quantities like f[n-1] and f[n-2], the rule for f[n] can also for example depend on a quantity like $f[n - f[n - 1]]$.

There is some subtlety here because in the abstract nothing guarantees that $n - f[n-1]$ will necessarily be a positive number. And if it is not, then results obtained by applying the rule can involve meaningless quantities such as f[0], f[-1] and f[-2].

![](Images/_page_144_Figure_3.jpeg)

Examples of sequences generated by rules that do not depend only on elements a fixed distance back. Most such rules eventually end up involving meaningless quantities such as f[0] and f[-1], but the particular rules shown here all avoid this problem.

![](Images/_page_145_Figure_1.jpeg)

Fluctuations in the overall increase of sequences from the previous page. In cases (c) and (d), the fluctuations have a regular nested form, and turn out to be directly related to the base 2 digit sequence of $n$. In the other cases, the fluctuations are more complicated, and seem in many respects random. All the rules shown start with f[1] = f[2] = 1.

For the vast majority of rules written down at random, such problems do indeed occur. But it is possible to find rules in which they do not, and the pictures on the previous two pages show a few examples I have found of such rules. In cases (a) and (b), the behavior is fairly simple. But in the other cases, it is considerably more complicated.

There is a steady overall increase, but superimposed on this increase are fluctuations, as shown in the pictures on the facing page.

In cases (c) and (d), these fluctuations turn out to have a very regular nested form. But in the other cases, the fluctuations seem instead in many respects random. Thus in case (f), for example, the number of positive and negative fluctuations appears on average to be equal even after a million steps.

But in a sense one of the most surprising features of the facing page is that the fluctuations it shows are so violent. One might have thought that in going say from f[2000] to f[2001] there would only ever be a small change. After all, between n = 2000 and 2001 there is only a 0.05% change in the size of n.

But much as we saw in the previous section it turns out that it is not so much the size of n that seems to matter as various aspects of its representation. And indeed, in cases (c) and (d), for example, it so happens that there is a direct relationship between the fluctuations in f[n] and the base 2 digit sequence of n.

In case (d), the fluctuation in each f[n] turns out to be essentially just the number of 1's that occur in the base 2 digit sequence for n. And in case (c), the fluctuations are determined by the total number of 1's that occur in the digit sequences of all numbers less than n.

There are no such simple relationships for the other rules shown on the facing page. But in general one suspects that all these rules can be thought of as being like simple computer programs that take some representation of n as their input.

And what we have discovered in this section is that even though the rules ultimately involve only addition and subtraction, they nevertheless correspond to programs that are capable of producing behavior of great complexity.

#### The Sequence of Primes

In the sequence of all possible numbers 1, 2, 3, 4, 5, 6, 7, 8, ... most are divisible by others, so that for example 6 is divisible by 2 and 3. But this is not true of every number. And so for example 5 and 7 are not divisible by any other numbers (except trivially by 1). And in fact it has been known for more than two thousand years that there are an infinite sequence of so-called prime numbers which are not divisible by other numbers, the first few being 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, ...

The picture below shows a simple rule by which such primes can be obtained. The idea is to start out on the top line with all possible numbers. Then on the second line, one removes all numbers larger than 2 that are divisible by 2. On the third line one removes numbers divisible by 3, and so on. As one goes on, fewer and fewer numbers remain. But some numbers always remain, and these numbers are exactly the primes.

![](Images/_page_147_Figure_4.jpeg)

A filtering process that yields the prime numbers. One starts on the top line with all numbers between 1 and 100. Then on the second line, one removes numbers larger than 2 that are divisible by 2, as indicated by the gray dots. On the third line, one removes numbers larger than 3 that are divisible by 3. If one then continues forever, there are some numbers that always remain, and these are exactly the primes. The process shown is essentially the sieve of Eratosthenes, already known in 200 BC.

Given the simplicity of this rule, one might imagine that the sequence of primes it generates would also be correspondingly simple. But just as in so many other examples in this book, in fact it is not. And indeed the plots on the facing page show various features of this sequence which indicate that it is in many respects quite random.

![](Images/_page_148_Figure_1.jpeg)

Features of the sequence of primes. Despite the simplicity of the rule on the facing page that generates the primes, the actual sequence of primes that is obtained seems in many respects remarkably random.

The examples of complexity that I have shown so far in this book are almost all completely new. But the first few hundred primes were no doubt known even in antiquity, and it must have been evident that there was at least some complexity in their distribution.

However, without the whole intellectual structure that I have developed in this book, the implications of this observation, and its potential connection, for example, to phenomena in nature, were not recognized. And even though there has been a vast amount of mathematical work done on the sequence of primes over the course of many centuries, almost without exception it has been concerned not with basic issues of complexity but instead with trying to find specific kinds of regularities.

Yet as it turns out, few regularities have in fact been found, and often the results that have been established tend only to support the idea that the sequence has many features of randomness. And so, as one example, it might appear from the pictures on the previous page that (c), (d) and (e) always stay systematically above the axis. But in fact with considerable effort it has been proved that all of them are in a sense more random, and eventually cross the axis an infinite number of times, and indeed go any distance up or down.

So is the complexity that we have seen in the sequence of primes somehow unusual among sequences based on numbers? The pictures on the facing page show a few other examples of sequences generated according to simple rules based on properties of numbers.

And in each case we again see a remarkable level of complexity.

Some of this complexity can be understood if we look at each number not in terms of its overall size, but rather in terms of its digit sequence or set of possible divisors. But in most cases, often despite centuries of work in number theory, considerable complexity remains.

And indeed the only reasonable conclusion seems to be that just as in so many other systems in this book, such sequences of numbers exhibit complexity that somehow arises as a fundamental consequence of the rules by which the sequences are generated.

![](Images/_page_150_Figure_1.jpeg)

![](Images/_page_150_Figure_2.jpeg)

![](Images/_page_150_Figure_3.jpeg)

![](Images/_page_150_Figure_4.jpeg)

![](Images/_page_150_Figure_5.jpeg)

(d) The number of ways of expressing n as a sum of four squares

(e) The number of ways of expressing an even number n as the sum of two primes

Sequences based on various simple properties of numbers. Extensive work in number theory has managed to establish only a few properties of these. It is for example known that (d) never reaches zero, while curve (c) reaches zero only for numbers of the form $4^r (8 s + 7)$. Sequence (b) is zero at so-called perfect numbers. Even perfect numbers always have a known form, but whether any odd perfect numbers exist is a question that has remained unresolved for more than two thousand years. The claim that sequence (e) never reaches zero is known as Goldbach's Conjecture. It was made in 1742 but no proof or counterexample has ever been found.

#### Mathematical Constants

The last few sections have shown that one can set up all sorts of systems based on numbers in which great complexity can occur. But it turns out that the possibility of such complexity is already suggested by some well-known facts in elementary mathematics.

The facts in question concern the sequences of digits in numbers like $\pi$ (pi). To a very rough approximation, $\pi$ is 3.14. A more accurate approximation is 3.14159265358979323846264338327950288.

But how does this sequence of digits continue?

One might suppose that at some level it must be quite simple and regular. For the value of $\pi$ is specified by the simple definition of being the ratio of the circumference of any circle to its diameter.

But it turns out that even though this definition is simple, the digit sequence of $\pi$ is not simple at all. The facing page shows the first 4000 digits in the sequence, both in the usual case of base 10, and in base 2. And the picture below shows a pictorial representation of the first 20,000 digits in the sequence.

![](Images/_page_151_Figure_7.jpeg)

A pictorial representation of the first 20,000 digits of $\pi$ in base 2. The curve drawn goes up every time a digit is 1, and down every time it is 0. Great complexity is evident. If the curve were continued further, it would spend more time above the axis, and no aspect of what is seen provides any evidence that the digit sequence is anything but perfectly random.

`3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384`

`11.0010010000111111011010101000100010000.101101011110100011001101101101101100011001100111011110.0110000111010001000110011101110111011`

The first 4000 digits of $\pi$ in bases 10 and 2. Despite the simple definition of $\pi$ as the ratio of the circumference to the diameter of a circle, its digit sequence is sufficiently complicated as to seem for practical purposes random.

In no case are there any obvious regularities. Indeed, in all the more than two hundred billion digits of $\pi$ that have so far been computed, no significant regularity of any kind has ever been found. Despite the simplicity of its definition, the digit sequence of $\pi$ seems for practical purposes completely random.

But what about other numbers? Is $\pi$ a special case, or are there other familiar mathematical constants that have complicated digit sequences? There are some numbers whose digit sequences effectively have limited length. Thus, for example, the digit sequence of 3/8 in base 10 is 0.375. (Strictly, the digit sequence is 0.3750000000..., but the 0's do not affect the value of the number, so are normally suppressed.)

It is however easy to find numbers whose digit sequences do not terminate. Thus, for example, the exact value of 1/3 in base 10 is 0.333333333333333333333333333333333333...

Examples of repeating digit sequences:

- In base 10: $1/3 = 0.333333\ldots$, $1/7 = 0.142857142857\ldots$, $1/9 = 0.111111\ldots$, $1/11 = 0.090909\ldots$, $1/81 = 0.012345679012345679\ldots$
- In base 2: $1/3 = 0.0101010101\ldots$, $1/7 = 0.001001001001\ldots$

Continued fraction representations for several numbers:

- $\pi = \{3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1, 2, 2, 6, 3, 5, 1, 1, 6, 8, 1, 7, 1, 2, 3, 7, 1, 2, \ldots\}$
- $\pi^2 = \{9, 1, 6, 1, 2, 47, 1, 8, 1, 1, 2, 2, 1, 1, 8, 3, 1, 10, 5, 1, 3, 1, 2, 1, 1, 3, 15, 1, 1, 2, 2, 1, 3, 2, 7, 1, 9, 18, 30, 2, 145, 1, 1, 17, 9, 1, 1, 1, 1, 7, 12, 1, \ldots\}$
- $Sinh[1] = \{1, 5, 1, 2, 2, 2, 1, 2, 7, 5, 1, 1, 1, 2, 2, 19, 1, 2, 1, 7, 1, 1, 9, 1, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 5, 3, 5, 1, 3, 1, 1, 1, 2, 7, 1, 9, 1, 1, 2, 1, 21, 1, \ldots\}$
- $Tanh[1] = \{0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, \ldots\}$

Continued fraction representations for several numbers. Square roots yield repetitive sequences in this representation, but cube roots and higher roots yield seemingly random sequences.

> If one does this, then the typical experience is that in any particular representation, some class of numbers will have simple forms. But other numbers, even though they may be the result of simple mathematical operations, tend to have seemingly random forms.
>
> And from this it seems appropriate to conclude that numbers generated by simple mathematical operations are often in some intrinsic sense complex, independent of the particular representation that one uses to look at them.

#### Mathematical Functions

The last section showed that individual numbers obtained by applying various simple mathematical functions can have features that are quite complex. But what about the functions themselves?

The pictures below show curves obtained by plotting standard mathematical functions. All of these curves have fairly simple, essentially repetitive forms. And indeed it turns out that almost all the standard mathematical functions that are defined, for example, in *Mathematica*, yield similarly simple curves.

![](Images/_page_160_Figure_4.jpeg)

Plots of some standard mathematical functions. The top row shows three trigonometric functions. The bottom row shows three so-called special functions that are commonly encountered in mathematical physics and other areas of traditional science. In all cases the curves shown have fairly simple repetitive forms.

But if one looks at combinations of these standard functions, it is fairly easy to get more complicated results. The pictures on the next page show what happens, for example, if one adds together various sine functions. In the first picture, the curve one gets has a fairly simple repetitive structure. In the second picture, the curve is more complicated, but still has an overall repetitive structure. But in the third and fourth pictures, there is no such repetitive structure, and indeed the curves look in many respects random.

![](Images/_page_161_Figure_1.jpeg)

Curves obtained by adding together various sine functions. In the first two cases, the curves are ultimately repetitive; in the second two cases they are not. If viewed as waveforms for sounds, then these curves correspond to chords. The first curve yields a perfect fifth, while the third curve yields a diminished fifth (or tritone) in an equal temperament scale.

In the third picture, however, the points where the curve crosses the axis come in two regularly spaced families. And as the pictures on the facing page indicate, for any curve like $Sin[x] + Sin[\alpha x]$ the relative arrangements of these crossing points turn out to be related to the output of a generalized substitution system in which the rule at each step is obtained from a term in the continued fraction representation of $(\alpha - 1)/(\alpha + 1)$.

When $\alpha$ is a square root, then as discussed in the previous section, the continued fraction representation is purely repetitive,

![](Images/_page_162_Figure_1.jpeg)

Curves obtained by adding or subtracting exactly two sine or cosine functions turn out to have a pattern of axis crossings that can be reproduced by a generalized substitution system. In general there is an axis crossing within an interval when the corresponding element in the generalized substitution system is black, and there is not when the element is white. In the case of $Cos[x]-Cos[\alpha x]$ each step in the generalized substitution system has a rule determined as shown on the left from a term in the continued fraction representation of $(\alpha-1)/(\alpha+1)$. In the first two examples shown $\alpha$ is a quadratic irrational, so that the continued fraction is repetitive, and the pattern obtained is purely nested. (The second example is analogous to the Fibonacci substitution system on page 83.) In the last two examples, however, there is no such regularity. Note that successive terms in each continued fraction are shown alongside successive steps in the substitution system going up the page.

making the generated pattern nested. But when $\alpha$ is not a square root the pattern can be more complicated. And if more than two sine functions are involved there no longer seems to be any particular connection to generalized substitution systems or continued fractions.

Among all the various mathematical functions defined, say, in *Mathematica* it turns out that there are also a few, not traditionally common in natural science, which yield complex curves but which do not appear to have any explicit dependence on representations of individual numbers. Many of these are related to the so-called Riemann zeta function, a version of which is shown in the picture below.

The basic definition of this function is fairly simple. But in the end the function turns out to be related to the distribution of primes, and the curve it generates is quite complicated. Indeed, despite immense mathematical effort for over a century, it has so far been impossible even to establish for example the so-called Riemann Hypothesis, which in effect just states that all the peaks in the curve lie above the axis, and all the valleys below.

![](Images/_page_163_Figure_4.jpeg)

A curve associated with the so-called Riemann zeta function. The zeta function Zeta[s] is defined as $Sum[1/k^s, \{k, \infty\}]$. The curve shown here is the so-called Riemann-Siegel Z function, which is essentially Zeta[1/2 + it]. The celebrated Riemann Hypothesis in effect states that all peaks after the first one in this curve must lie above the axis.

#### Iterated Maps and the Chaos Phenomenon

The basic idea of an iterated map is to take a number between 0 and 1, and then in a sequence of steps to update this number according to a fixed rule or "map". Many of the maps I will consider can be expressed in terms of standard mathematical functions, but in general all that is needed is that the map take any possible number between 0 and 1 and yield some definite number that is also between 0 and 1.

The pictures on the next two pages show examples of behavior obtained with four different possible choices of maps.

Cases (a) and (b) on the first page show much the same kind of complexity that we have seen in many other systems in this chapter, in both digit sequences and sizes of numbers. Case (c) shows complexity in digit sequences, but the sizes of the numbers it generates rapidly tend to 0. Case (d), however, seems essentially trivial, and shows no complexity in either digit sequences or sizes of numbers.

On the first of the next two pages all the examples start with the number 1/2, which has a simple digit sequence. But the examples on the second of the next two pages instead start with the number $\pi/4$, which has a seemingly random digit sequence.

Cases (a), (b) and (c) look very similar on both pages, particularly in terms of sizes of numbers. But case (d) looks quite different. For on the first page it just yields 0's. But on the second page, it yields numbers whose sizes continually vary in a seemingly random way.

If one looks at digit sequences, it is rather clear why this happens. For as the picture illustrates, the so-called shift map used in case (d) simply serves to shift all digits one position to the left at each step. And this means that over the course of the evolution of the system, digits further to the right in the original number will progressively end up all the way to the left, so that insofar as these digits show randomness, this will lead to randomness in the sizes of the numbers generated.

It is important to realize, however, that in no real sense is any randomness actually being generated by the evolution of this system. Instead, it is just that randomness that was inserted in the digit sequence of the original number shows up in the results one gets.

![](Images/_page_165_Figure_1.jpeg)

Examples of iterated maps starting from simple initial conditions. At each step there is a number x between 0 and 1 that is updated by applying a fixed mapping. The four mappings considered here are given above both as formulas and in terms of plots. The pictures at the top of the page show the base 2 digit sequences of successive numbers obtained by iterating this mapping, while the pictures in the middle of the page plot the sizes of these numbers. In all cases, the initial conditions consist of the number 1/2, which has a very simple digit sequence. Yet despite this simplicity, cases (a) and (b) show considerable complexity in both the digit sequences and the sizes of the numbers produced (compare page 122). In case (c), the digit sequences are complicated but the sizes of the numbers tend rapidly to zero. And finally, in case (d), neither the digit sequences nor the sizes of numbers are anything but trivial. Note that in the pictures above each horizontal row of digits corresponds to a number, and that digits further to the left contribute progressively more to the size of this number.

![](Images/_page_166_Figure_2.jpeg)

$x \rightarrow FractionalPart[3/4 x]$

$x \rightarrow FractionalPart[2 x]$

$x \to If[x < 1/2, 3/2 x, 3/2 (1 - x)]$

$x \rightarrow FractionalPart[3/2 x]$

This is very different from what happens in cases (a) and (b). For in these cases complex and seemingly random results are obtained even on the first of the previous two pages, when the original number has a very simple digit sequence. And the point is that these maps actually do intrinsically generate complexity and randomness; they do not just transcribe it when it is inserted in their initial conditions.

In the context of the approach I have developed in this book this distinction is easy to understand. But with the traditional mathematical approach, things can get quite confused. The main issue, already mentioned at the beginning of this chapter, is that in this approach the only attribute of numbers that is usually considered significant is their size. And this means that any issue based on discussing explicit digit sequences for numbers, and whether for example they are simple or complicated, tends to seem at best bizarre.

Indeed, thinking about numbers purely in terms of size, one might imagine that as soon as any two numbers are sufficiently close in size they would inevitably lead to results that are somehow also close. And in fact this is for example the basis for much of the formalism of calculus in traditional mathematics.

But the essence of the so-called chaos phenomenon is that there are some systems where arbitrarily small changes in the size of a number can end up having large effects on the results that are produced. And the shift map shown as case (d) on the previous two pages turns out to be a classic example of this.

The pictures at the top of the facing page show what happens if one uses as the initial conditions for this system two numbers whose sizes differ by just one part in a billion billion. And looking at the plots of sizes of numbers produced, one sees that for quite a while these two different initial conditions lead to results that are indistinguishably close. But at some point they diverge and soon become quite different.

And at least if one looks only at the sizes of numbers, this seems rather mysterious. But as soon as one looks at digit sequences, it immediately becomes much clearer. For as the pictures at the top of the facing page show, the fact that the numbers which are used as initial conditions differ only by a very small amount in size just means that their first several digits are the same. And for a while these digits are

![](Images/_page_168_Picture_1.jpeg)

![](Images/_page_168_Picture_2.jpeg)

![](Images/_page_168_Picture_3.jpeg)

![](Images/_page_168_Figure_4.jpeg)

![](Images/_page_168_Figure_5.jpeg)

The effect of making a small change in the initial conditions for the shift map, shown as case (d) on pages 150 and 151. The first picture shows results for the same initial condition as on page 151. The second picture shows what happens if one changes the size of the number in this initial condition by just one part in a billion billion. The plots to the left indicate that for a while the sizes of numbers obtained by the evolution of the system in these two cases are indistinguishable. But suddenly the results diverge and become completely different. Looking at the digit sequences above shows why this happens. The point is that a small change in the size of the number in the initial conditions corresponds to a change in digits far to the right. But the evolution of the system progressively shifts digits to the left, so that the digits which differ eventually become important. The much-investigated chaos phenomenon consists essentially of this effect.

what is important. But since the evolution of the system continually shifts digits to the left, it is inevitable that the differences that exist in later digits will eventually become important.

The fact that small changes in initial conditions can lead to large changes in results is a somewhat interesting phenomenon. But as I will discuss at length in Chapter 7 one must realize that on its own this cannot explain why randomness, or complexity, should occur in any particular case. And indeed, for the shift map what we have seen is that randomness will occur only when the initial conditions that are given happen to be a number whose digit sequence is random.

But in the past what has often been confusing is that traditional mathematics implicitly tends to assume that initial conditions of this kind are in some sense inevitable. For if one thinks about numbers purely in terms of size, one should make no distinction between numbers that are sufficiently close in size. And this implies that in choosing initial conditions for a system like the shift map, one should therefore make no distinction between the exact number 1/2 and numbers that are sufficiently close in size to 1/2.

But it turns out that if one picks a number at random subject only to the constraint that its size be in a certain range, then it is overwhelmingly likely that the number one gets will have a digit sequence that is essentially random. And if one then uses this number as the initial condition for a shift map, the results will also be correspondingly random, just like those on the previous page.

In the past this fact has sometimes been taken to indicate that the shift map somehow fundamentally produces randomness. But as I have discussed above, the only randomness that can actually come out of such a system is randomness that was explicitly put in through the details of its initial conditions. And this means that any claim that the system produces randomness must really be a claim about the details of what initial conditions are typically given for it.

I suppose in principle it could be that nature would effectively follow the same idealization as in traditional mathematics, and would end up picking numbers purely according to their size. And if this were so, then it would mean that the initial conditions for systems like the shift map would naturally have digit sequences that are almost always random.

But this line of reasoning can ultimately never be too useful. For what it says is that the randomness we see somehow comes from randomness that is already present, but it does not explain where that randomness comes from. And indeed, as I will discuss in Chapter 7, if one looks only at systems like the shift map then it is not clear any new randomness can ever actually be generated.

But a crucial discovery in this book is that systems like (a) and (b) on pages 150 and 151 can show behavior that seems in many respects random even when their initial conditions show no sign of randomness and are in fact extremely simple.

Yet the fact that systems like (a) and (b) can intrinsically generate randomness even from simple initial conditions does not mean that they do not also show sensitive dependence on initial conditions. And indeed the pictures below illustrate that even in such cases changes in digit sequences are progressively amplified, just like in the shift map case (d).

![](Images/_page_170_Picture_2.jpeg)

Differences in digit sequences produced by a small change in initial conditions for the four iterated maps discussed in this section. Cases (a), (b) and (d) exhibit sensitive dependence on initial conditions, in the sense that a change in insignificant digits far to the right eventually grows to affect all digits. Case (c) does not show such sensitivity to initial conditions, but instead always evolves to 0, independent of its initial conditions.

But the crucial point that I will discuss more in Chapter 7 is that the presence of sensitive dependence on initial conditions in systems like (a) and (b) in no way implies that it is what is responsible for the randomness and complexity we see in these systems. And indeed, what looking at the shift map in terms of digit sequences shows us is that this phenomenon on its own can make no contribution at all to what we can reasonably consider the ultimate production of randomness.

#### Continuous Cellular Automata

Despite all their differences, the various kinds of programs discussed in the previous chapter have one thing in common: they are all based on elements that can take on only a discrete set of possible forms, typically just colors black and white. And in this chapter, we have introduced a similar kind of discreteness into our study of systems based on numbers by considering digit sequences in which each digit can again have only a discrete set of possible values, typically just 0 and 1.

So now a question that arises is whether all the complexity we have seen in the past three chapters somehow depends on the discreteness of the elements in the systems we have looked at.

And to address this question, what I will do in this section is to consider a generalization of cellular automata in which each cell is not just black or white, but instead can have any of a continuous range of possible levels of gray. One can update the gray level of each cell by using rules that are in a sense a cross between the totalistic cellular automaton rules that we discussed at the beginning of the last chapter and the iterated maps that we just discussed in the previous section.

The idea is to look at the average gray level of a cell and its immediate neighbors, and then to get the gray level for that cell at the next step by applying a fixed mapping to the result. The picture below shows a very simple case in which the new gray level of each cell is exactly the average of the one for that cell and its immediate neighbors. Starting from a single black cell, what happens in this case is that the gray essentially just diffuses away, leaving in the end a uniform pattern.

![](Images/_page_171_Picture_5.jpeg)

A continuous cellular automaton in which each cell can have any level of gray between white (0) and black (1). The rule shown here takes the new gray level of each cell to be the average of its own gray level and those of its immediate neighbors.

| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0.333 | 0.333 | 0.333 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0.111 | 0.222 | 0.333 | 0.222 | 0.111 | 0 | 0 | 0 |
| 0 | 0 | 0.037 | 0.111 | 0.222 | 0.259 | 0.222 | 0.111 | 0.037 | 0 | 0 |
| 0 | 0.012 | 0.049 | 0.123 | 0.198 | 0.235 | 0.198 | 0.123 | 0.049 | 0.012 | 0 |
| 0.004 | 0.021 | 0.062 | 0.123 | 0.185 | 0.21 | 0.185 | 0.123 | 0.062 | 0.021 | 0.004 |

The picture on the facing page shows what happens with a slightly more complicated rule in which the average gray level is multiplied by 3/2, and then only the fractional part is kept if the result of this is greater than 1.

![](Images/_page_172_Picture_1.jpeg)

| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0.5 | 0.5 | 0.5 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0.25 | 0.5 | 0.75 | 0.5 | 0.25 | 0 | 0 | 0 |
| 0 | 0 | 0.125 | 0.375 | 0.75 | 0.875 | 0.75 | 0.375 | 0.125 | 0 | 0 |
| 0 | 0.063 | 0.25 | 0 | 0.188 | 0 | 0.25 | 0.063 | 0 | 0 | 0 |
| 0.031 | 0.156 | 0.469 | 0.438 | 0.406 | 0.094 | 0.406 | 0.438 | 0.469 | 0.156 | 0.031 |

A continuous cellular automaton with a slightly more complicated rule. The rule takes the new gray level of each cell to be the fractional part of the average gray level of the cell and its neighbors multiplied by 3/2. The picture shows that starting from a single black cell, this rule yields behavior of considerable complexity. Note that the operation performed on individual average gray levels is exactly iterated map (a) from page 150.

And what we see is that despite the presence of continuous gray levels, the behavior that is produced exhibits the same kind of complexity that we have seen in many ordinary cellular automata and other systems with discrete underlying elements.

In fact, it turns out that in continuous cellular automata it takes only extremely simple rules to generate behavior of considerable complexity. So as an example the picture below shows a rule that determines the new gray level for a cell by just adding the constant 1/4 to the average gray level for the cell and its immediate neighbors, and then taking the fractional part of the result.

| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | 0.25 | 0.25 | 0.25 | 0.583 | 0.583 | 0.583 | 0.25 | 0.25 | 0.25 | 0.25 |
| 0.5 | 0.5 | 0.5 | 0 | 0.722 | 0.833 | 0.722 | 0 | 0.5 | 0.5 | 0.5 |
| 0.75 | 0.75 | 0.787 | 0.861 | 0.972 | 0.009 | 0.972 | 0.861 | 0.787 | 0.75 | 0.75 |
| 0 | 0.012 | 0.049 | 0.123 | 0.864 | 0.901 | 0.864 | 0.123 | 0.049 | 0.012 | 0 |
| 0.254 | 0.271 | 0.312 | 0.596 | 0.88 | 0.127 | 0.88 | 0.596 | 0.312 | 0.271 | 0.254 |

![](Images/_page_173_Picture_3.jpeg)

![](Images/_page_173_Picture_4.jpeg)

FractionalPart[x+1/4]

A continuous cellular automaton whose rule adds the constant 1/4 to the average gray level for a cell and its immediate neighbors, and takes the fractional part of the result. The background simply repeats every 4 steps, but the main pattern has a complex and in many respects random form.

The facing page and the one after show what happens when one chooses different values for the constant that is added. A remarkable diversity of behavior is seen. Sometimes the behavior is purely repetitive, but often it has features that seem effectively random.

And in fact, as the picture in the middle of page 160 shows, it is even possible to find cases that exhibit localized structures very much like those occasionally seen in ordinary cellular automata.

Continuous cellular automata with the same kind of rules as in the picture above, but with a variety of different constants being added. Note that it is not so much the size of the constant as properties like its digit sequence that seem to determine the overall form of behavior produced in each case.

![](Images/_page_174_Picture_2.jpeg)

![](Images/_page_175_Figure_2.jpeg)

More steps in the evolution of continuous cellular automata with the same kind of rules as on the previous page. In order to remove the uniform stripes, the picture in the middle shows the difference between the gray level of each cell and its immediate neighbor. Note the presence of discrete localized structures even though the underlying rules for the system involve continuous gray levels.

#### Partial Differential Equations

By introducing continuous cellular automata with a continuous range of gray levels, we have successfully removed some of the discreteness that exists in ordinary cellular automata. But there is nevertheless much discreteness that remains: for a continuous cellular automaton is still made up of discrete cells that are updated in discrete time steps.

So can one in fact construct systems in which there is absolutely no such discreteness? The answer, it turns out, is that at least in principle one can, although to do so requires a somewhat higher level of mathematical abstraction than has so far been necessary in this book.

The basic idea is to imagine that a quantity such as gray level can be set up to vary continuously in space and time. And what this means is that instead of just having gray levels in discrete cells at discrete time steps, one supposes that there exists a definite gray level at absolutely every point in space and every moment in time, as if one took the limit of an infinite collection of cells and time steps, with each cell being an infinitesimal size, and each time step lasting an infinitesimal time.

But how does one give rules for the evolution of such a system? Having no explicit time steps to work with, one must instead just specify the rate at which the gray level changes with time at every point in space. And typically one gives this rate as a simple formula that depends on the gray level at each point in space, and on the rate at which that gray level changes with position.

Such rules are known in mathematics as partial differential equations, and in fact they have been widely studied for about two hundred years. Indeed, it turns out that almost all the traditional mathematical models that have been used in physics and other areas of science are ultimately based on partial differential equations. Thus, for example, Maxwell's equations for electromagnetism, Einstein's equations for gravity, Schrödinger's equation for quantum mechanics and the Hodgkin-Huxley equation for the electrochemistry of nerve cells are all examples of partial differential equations.

It is in a sense surprising that systems which involve such a high level of mathematical abstraction should have become so widely used in practice. For as we shall see later in this book, it is certainly not that nature fundamentally follows these abstractions.

And I suspect that in fact the current predominance of partial differential equations is in many respects a historical accident, and that had computer technology been developed earlier in the history of mathematics, the situation would probably now be very different.

But particularly before computers, the great attraction of partial differential equations was that at least in simple cases explicit mathematical formulas could be found for their behavior. And this meant that it was possible to work out, for example, the gray level at a particular point in space and time just by evaluating a single mathematical formula, without having in a sense to follow the complete evolution of the partial differential equation.

The pictures on the facing page show three common partial differential equations that have been studied over the years.

The first picture shows the diffusion equation, which can be viewed as a limiting case of the continuous cellular automaton on page 156. Its behavior is always very simple: any initial gray progressively diffuses away, so that in the end only uniform white is left.

The second picture shows the wave equation. And with this equation, the initial lump of gray shown just breaks into two identical pieces which propagate to the left and right without change.

The third picture shows the sine-Gordon equation. This leads to slightly more complicated behavior than the other equations, though the pattern it generates still has a simple repetitive form.

Considering the amount of mathematical work that has been done on partial differential equations, one might have thought that a vast range of different equations would by now have been studied. But in fact almost all the work, at least in one dimension, has concentrated on just the three specific equations on the facing page, together with a few others that are essentially equivalent to them.

And as we have seen, these equations yield only simple behavior.

So is it in fact possible to get more complicated behavior in partial differential equations? The results in this book on other kinds of systems strongly suggest that it should be. But traditional mathematical methods give very little guidance about how to find such behavior.

![](Images/_page_178_Picture_2.jpeg)

![](Images/_page_178_Picture_3.jpeg)

diffusion equation: $\partial_t u[t, x] = 1/4 \partial_{xx} u[t, x]$

![](Images/_page_178_Picture_5.jpeg)

![](Images/_page_178_Picture_6.jpeg)

wave equation: $\partial_{tt} u[t, x] = \partial_{xx} u[t, x]$

![](Images/_page_178_Picture_8.jpeg)

![](Images/_page_178_Picture_9.jpeg)

sine-Gordon soliton equation: $\partial_{tt} u[t, x] = \partial_{xx} u[t, x] + Sin[u[t, x]]$

Three partial differential equations that have historically been studied extensively. Just like in other pictures in this book, position goes across the page, and time down the page. In each equation u is the gray level at a particular point, $\partial_t u$ is the rate of change (derivative) of the gray level with time, and $\partial_{tt}u$ is the rate of change of that rate of change (second derivative). Similarly, $\partial_x u$ is the rate of change with position in space, and $\partial_{xx}u$ is the rate of change of that rate of change. On this page and the ones that follow the initial conditions used are $u = e^{-x^2}$, $\partial_t u = 0$.

Indeed, it seems that the best approach is essentially just to search through many different partial differential equations, looking for ones that turn out to show complex behavior.

But an immediate difficulty is that there is no obvious way to sample possible partial differential equations. In discrete systems such as cellular automata there are always a discrete set of possible rules. But in partial differential equations any mathematical formula can appear.

Nevertheless, by representing formulas as symbolic expressions with discrete sets of possible components, one can devise at least some schemes for sampling partial differential equations.

But even given a particular partial differential equation, there is no guarantee that the equation will yield self-consistent results. Indeed, for a very large fraction of randomly chosen partial differential equations what one finds is that after just a small amount of time, the gray level one gets either becomes infinitely large or starts to vary infinitely quickly in space or time. And whenever such phenomena occur, the original equation can no longer be used to determine future behavior.

But despite these difficulties I was eventually able to find the partial differential equations shown on the next two pages.

The mathematical statement of these equations is fairly simple. But as the pictures show, their behavior is highly complex.

Indeed, strangely enough, even though the underlying equations are continuous, the patterns they produce seem to involve patches that have a somewhat discrete structure.

But the main point that the pictures on the next two pages make is that the kind of complex behavior that we have seen in this book is in no way restricted to systems that are based on discrete elements. It is certainly much easier to find and to study such behavior in these discrete systems, but from what we have learned in this section, we now know that the same kind of behavior can also occur in completely continuous systems such as partial differential equations.

![](Images/_page_180_Picture_2.jpeg)

![](Images/_page_180_Picture_3.jpeg)

$\partial_{tt}\,u[t,\,x]=\partial_{xx}\,u[t,\,x]+(1-u[t,\,x]^2)\,(1+u[t,\,x])$

![](Images/_page_180_Picture_5.jpeg)

![](Images/_page_180_Picture_6.jpeg)

$\partial_{tt} u[t, x] = \partial_{xx} u[t, x] + (1 - u[t, x]^2) (1 + 2 u[t, x])$

![](Images/_page_180_Picture_8.jpeg)

![](Images/_page_180_Picture_9.jpeg)

$\partial_{tt} \, u[t, \, x] = \partial_{xx} \, u[t, \, x] + (1 - u[t, \, x]^2) \, (1 + 4 \, u[t, \, x])$

Examples of partial differential equations I have found that have more complicated behavior. The background in each case is purely repetitive, but the main part of the pattern is complex, and reminiscent of what is produced by continuous cellular automata and many other kinds of systems discussed in this book.

![](Images/_page_181_Picture_2.jpeg)

$\partial_{tt} u[t, x] = \partial_{xx} u[t, x] + (1 - u[t, x]^2)(1 + u[t, x])$

![](Images/_page_181_Picture_4.jpeg)

$\partial_{tt} u[t, x] = \partial_{xx} u[t, x] + (1 - u[t, x]^2) (1 + 2 u[t, x])$

![](Images/_page_181_Picture_6.jpeg)

$\partial_{tt}\,u[t,\,x]=\partial_{xx}\,u[t,\,x]+(1-u[t,\,x]^2)\,(1+4\,u[t,\,x])$

#### Continuous Versus Discrete Systems

One of the most obvious differences between my approach to science based on simple programs and the traditional approach based on mathematical equations is that programs tend to involve discrete elements while equations tend to involve continuous quantities.

But how significant is this difference in the end?

One might have thought that perhaps the basic phenomenon of complexity that I have identified could only occur in discrete systems. But from the results of the last few sections, we know that this is not the case.

What is true, however, is that the phenomenon was immensely easier to discover in discrete systems than it would have been in continuous ones. Probably complexity is not in any fundamental sense rarer in continuous systems than in discrete ones. But the point is that discrete systems can typically be investigated in a much more direct way than continuous ones.

Indeed, given the rules for a discrete system, it is usually a rather straightforward matter to do a computer experiment to find out how the system will behave. But given an equation for a continuous system, it often requires considerable analysis to work out even approximately how the system will behave. And in fact, in the end one typically has rather little idea which aspects of what one sees are actually genuine features of the system, and which are just artifacts of the particular methods and approximations that one is using to study it.

With all the work that was done on continuous systems in the history of traditional science and mathematics, there were undoubtedly many cases in which effects related to the phenomenon of complexity were seen. But because the basic phenomenon of complexity was not known and was not expected, such effects were probably always dismissed as somehow not being genuine features of the systems being studied. Yet when I came to investigate discrete systems there was no possibility of dismissing what I saw in such a way. And as a result I was in a sense forced into recognizing the basic phenomenon of complexity.

But now, armed with the knowledge that this phenomenon exists, it is possible to go back and look again at continuous systems.

And although there are significant technical difficulties, one finds as the last few sections have shown that the phenomenon of complexity can occur in continuous systems just as it does in discrete ones.

It remains much easier to be sure of what is going on in a discrete system than in a continuous one. But I suspect that essentially all of the various phenomena that we have observed in discrete systems in the past several chapters can in fact also be found even in continuous systems with fairly simple rules.

<sup>◆</sup> Solutions to the same equations as on the previous page over a longer period of time. Note the appearance of discrete structures. Particularly in the last picture some details are sensitive to the numerical approximation scheme used in computing the solution to the equation.

![](Images/_page_184_Picture_0.jpeg)
