The pictures below show (a) the first 500 steps of evolution, (b) the first million steps in compressed form and (c) the number of black cells obtained at each step. Perhaps not surprisingly for a system optimized to run as long as possible, the machine operates in a rather systematic and regular way. With 6 states, a machine is known that takes about 3.002 × 10<sup>1730</sup> steps to halt, and leaves about  $1.29 \times 10^{865}$  black cells. (See also page 1144.)

![](Images/_page_904_Picture_16.jpeg)

![](Images/_page_904_Picture_17.jpeg)

![](Images/_page_904_Figure_18.jpeg)

#### Substitution Systems

■ Implementation. The rule for a neighbor-independent substitution system such as the first one on page 82 can conveniently be given as  $\{1 \rightarrow \{1, 0\}, 0 \rightarrow \{0, 1\}\}$ . And with this representation, the evolution for t steps is given by

SSEvolveList[rule\_, init\_List, t\_Integer] := NestList[Flatten[# /. rule] &, init, t]

where in the first example on page 82, the initial condition is {1}.

An alternative approach is to use strings, representing the rule by  $\{"B" \to "BA", "A" \to "AB"\}$  and the initial condition by "B". In this case, the evolution can be obtained using

SSEvolveList[rule\_, init\_String, t\_Integer] := NestList[StringReplace[#, rule] &, init, t]

For a neighbor-dependent substitution system such as the first one on page 85 the rule can be given as

 $\{\{1, 1\} \rightarrow \{0, 1\}, \{1, 0\} \rightarrow \{1, 0\}, \{0, 1\} \rightarrow \{0\}, \{0, 0\} \rightarrow \{0, 1\}\}$ And with this representation, the evolution for t steps is given by

SS2EvolveList[rule\_, init\_List, t\_Integer] := NestList[Flatten[Partition[#, 2, 1] /. rule] &, init, t]

- Page 83 · Properties. The examples shown here all appear in quite a number of different contexts in this book. Note that each of them in effect yields a single sequence that gets progressively longer at each step; other rules make the colors of elements alternate on successive steps.
- (a) (Successive digits sequence) The sequence produced is repetitive, with the element at position n being black for n odd and white for n even. There are a total of  $2^t$  elements after t steps. The complete pattern formed by looking at all the steps together has the same structure as the arrangement of base 2 digits in successive numbers shown on page 117.

(b) (*Thue-Morse sequence*) The color s[n] of the element at position n is given by 1-Mod[DigitCount[n-1, 2, 1], 2]. These colors satisfy  $s[n_-] := If[EvenQ[n], 1-s[n/2], s[(n+1)/2]]$  with s[1] = 1. There are a total of  $2^t$  elements in the sequence after t steps. The sequence on step t can be obtained from  $Nest[Join[\#, 1-\#] \&, \{1\}, t-1]$ . The number of black and white elements at each step is always the same. All four possible pairs of successive elements occur, though not with equal frequency. Runs of three identical elements never occur, and in general no block of elements can ever occur more than twice. The first  $2^m$  elements in the sequence can be obtained from (see page 1081)

(CoefficientList[Product[ $1-z^{2^{s}}$ ,  $\{s, 0, m-1\}$ ], z]+1)/2

The first n elements can also be obtained from (see page 1092)  $Mod[CoefficientList[Series[(1+Sqrt[(1-3x)/(1+x)])/(2(1+x)), \{x, 0, n-1\}], x], 2]$ 

The sequence occurs many times in this book; it can for example be derived from a column of values in the rule 150 cellular automaton pattern discussed on page 885.

(c) (Fibonacci-related sequence) The sequence at step t can be obtained from  $a[t_-] := Join[a[t-1], a[t-2]]; a[1] = \{0\}; a[2] = \{0, 1\}.$  This sequence has length Fibonacci[t+1] (or approximately  $1.618^{t+1}$ ) (see note below). The color of the element at position n is given by 2-(Floor[(n+1)GoldenRatio]-Floor[nGoldenRatio]) (see page 904), while the position of the  $k^{th}$  white element is given by the so-called Beatty sequence Floor[kGoldenRatio]. The ratio of the number of white elements to black at step t is Fibonacci[t-1]/Fibonacci[t-2], which approaches GoldenRatio for large t. For all  $m \le Fibonacci[t-1]$ , the number of distinct blocks of m successive elements that actually appear out of the  $2^m$  possibilities is m+1 (making it a so-called Sturmian sequence as discussed on page 1084).

(d) (Cantor set) The color of the element at position n is given by If[FreeQ[IntegerDigits[n-1, 3], 1], 1, 0], which turns out to be equivalent to

If[OddQ[n], Sign[Mod[Binomial[n-1, (n-1)/2], 3]], 0, 1]

There are  $3^t$  elements after t steps, of which  $2^t$  are black. The picture below shows the number of black cells that occur before position n. The resulting curve has a nested form, with envelope  $n^Log[3, 2]$ .

![](Images/_page_905_Figure_8.jpeg)

■ Growth rates. The total number of elements of each color that occur at each step in a neighbor-independent substitution system can be found by forming the matrix m where m[[i, j]] gives the number of elements of color j + 1 that appear in the block that replaces an element of color i + 1. For case (c) above,  $m = \{\{1, 1\}, \{1, 0\}\}$ . A list that gives the number of elements of each color at step t can then be found from init . MatrixPower[m, t], where init gives the initial number of elements of each color— $\{1, 0\}$  for case (c) above. For large t, the total number of elements typically grows like  $\lambda^t$ , where  $\lambda$ is the largest eigenvalue of m; the relative numbers of elements of each color are given by the corresponding eigenvector. For case (c),  $\lambda$  is GoldenRatio, or  $(1 + \sqrt{5})/2$ . There are exceptional cases where  $\lambda = 1$ , so that the growth is not exponential. For the rule  $\{0 \rightarrow \{0, 1\}, 1 \rightarrow \{1\}\}$ ,  $m = \{\{1, 1\}, \{0, 1\}\}$ , and the number of elements at step t starting with  $\{0\}$  is just t. For  $\{0 \to \{0, 1\}, 1 \to \{1, 2\}, 2 \to \{2\}\}$ ,  $m = \{\{1, 1, 0\}, \{0, 1, 1\}, \{0, 0, 1\}\}$ , and the number of elements starting with  $\{0\}$  is  $(t^2 - t + 2)/2$ . For neighbor-independent rules, the growth for large t must follow an exponential or an integer power less than the number of possible colors. For neighbor-dependent rules, any form of growth can in principle

■ **Fibonacci numbers.** The Fibonacci numbers *Fibonacci*[n] (*f*[n] for short) can be generated by the recurrence relation

$$f[n_{-}] := f[n] = f[n-1] + f[n-2]$$
  
 $f[1] = f[2] = 1$ 

The first few Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377. For large n the ratio f[n]/f[n-1] approaches *GoldenRatio* or  $(1 + \sqrt{5})/2 \approx 1.618$ .

Fibonacci[n] can be obtained in many ways:

- $(GoldenRatio^n (-GoldenRatio)^{-n})/\sqrt{5}$
- Round[GoldenRatio<sup>n</sup>/√5]
- $2^{1-n}$  Coefficient[ $(1+\sqrt{5})^n$ ,  $\sqrt{5}$ ]
- MatrixPower[{{1, 1}, {1, 0}}, n-1][[1, 1]]
- Numerator[NestList[1/(1+#) &, 1, n]]
- Coefficient[Series[ $1/(1-t-t^2)$ , {t, 0, n}],  $t^{n-1}$ ]
- Sum[Binomial[n-i-1, i], {i, 0, (n-1)/2}]

A fast method for evaluating Fibonacci[n] is

First[Fold[f, {1, 0, -1}, Rest[IntegerDigits[n, 2]]]]

$$f[\{a_-, b_-, s_-\}, 0] = \{a(a+2b), s+a(2a-b), 1\}$$

$$f[\{a_-, b_-, s_-\}, 1] = \{-s+(a+b)(a+2b), a(a+2b), -1\}$$

Fibonacci numbers appear to have first arisen in perhaps 200 BC in work by Pingala on enumerating possible patterns of

poetry formed from syllables of two lengths. They were independently discussed by Leonardo Fibonacci in 1202 as solutions to a mathematical puzzle concerning rabbit breeding, and by Johannes Kepler in 1611 in connection with approximations to the pentagon. Their recurrence relation appears to have been understood from the early 1600s, but it has only been in the past very few decades that they have in general become widely discussed.

For m > 1, the value of n for which m == Fibonacci[n] is Round[Log[GoldenRatio,  $\sqrt{5}$  m]].

The sequence Mod[Fibonacci[n], k] is always purely repetitive; the maximum period is 6k, achieved when  $k = 105^{m}$  (compare page 975).

Mod[Fibonacci[n], n] has the fairly complicated form shown below. It appears to be zero only when n is of the form  $5^m$  or 12q, where q is not prime (q > 5).

![](Images/_page_906_Figure_6.jpeg)

The number GoldenRatio appears to have been used in art and architecture since antiquity. 1/GoldenRatio is the default AspectRatio for Mathematica graphics. In addition:

- Golden Ratio is the solution to x = 1 + 1/x or  $x^2 = x + 1$
- The right-hand rectangle in 
  is similar to the whole rectangle when the aspect ratio is GoldenRatio
- $Cos[\pi/5] == Cos[36^\circ] == GoldenRatio/2$
- The ratio of the length of the diagonal to the length of a side in a regular pentagon is GoldenRatio
- The corners of an icosahedron are at coordinates Flatten[Array[NestList[RotateRight, {0, (-1)<sup>#1</sup> GoldenRatio, (-1)<sup>#2</sup>}, 3] &, {2, 2}], 2]
- 1 + FixedPoint[N[1/(1+#), k] &, 1] approximates GoldenRatio to k digits, as does FixedPoint[N[Sqrt[1+#], k] &, 1]
- A successive angle difference of GoldenRatio radians yields points maximally separated around a circle (see page 1006).
- Lucas numbers. Lucas numbers Lucas[n] satisfy the same recurrence relation  $f[n_{-}] := f[n-1] + f[n-2]$  as Fibonacci numbers, but with the initial conditions f(1) = 1; f(2) = 3. Among the relations satisfied by Lucas numbers are:
- Lucas[n\_] := Fibonacci[n 1] + Fibonacci[n + 1]
- GoldenRatio<sup>n</sup> ==  $(Lucas[n] + Fibonacci[n] \sqrt{5})/2$
- Generalized Fibonacci sequences. Any linear recurrence relation yields sequences with many properties in common

with the Fibonacci numbers—though with GoldenRatio replaced by other algebraic numbers. The Perrin sequence  $f[n_{-}] := f[n-2] + f[n-3]; \ f[0] = 3; f[1] = 0; \ f[2] = 2$  has the peculiar property that Mod[f[n], n] == 0 mostly but not always only for n prime. (For more on recurrence relations see page 128.)

■ Connections with digit sequences. In a sequence generated by a neighbor-independent substitution system the color of the element at position n turns out always to be related to the digit sequence of the number n in an appropriate base. The basic reason for this is that as shown on page 84 the evolution of the substitution system always yields a tree, and the successive digits in n determine which branch is taken at each level in order to reach the element at position n. In cases (a) and (b) on pages 83 and 84, the tree has two branches at every node, and so the base 2 digits of *n* determine the successive left and right branches that must be taken. Given that a branch with a certain color has been reached, the color of the branch to be taken next is then determined purely by the next digit in the digit sequence of *n*. For case (b) on pages 83 and 84, the rule that gives the color of the next branch in terms of the color of the current branch and the next digit is  $\{\{0, 0\} \rightarrow 0, \{0, 1\} \rightarrow 1, \{1, 0\} \rightarrow 1, \{1, 1\} \rightarrow 0\}.$  In terms of this rule, the color of the element at position n is given by

Fold[Replace[{#1, #2}, rule] &, 1, IntegerDigits[n-1, 2]]

The rule used here can be thought of as a finite automaton with two states. In general, the behavior of any neighborindependent substitution system where each element is subdivided into exactly k elements can be reproduced by a finite automaton with k states operating on digit sequences in base k. The nested structure of the patterns produced is thus a direct consequence of the nesting seen in the patterns of these digit sequences, as shown on page 117.

Note that if the rule for the finite automaton is represented for example as {{1, 2}, {2, 1}} where each sublist corresponds to a particular state, and the elements of the sublist give the successor states with inputs Range[0, k-1], then the nth element in the output sequence can be obtained from

Fold[rule[[#1, #2]] &, 1, IntegerDigits[n-1, k]+1]-1 while the first  $k^m$  elements can be obtained from Nest[Flatten[rule[[#]]] &, 1, m] - 1

To treat examples such as case (c) where elements can subdivide into blocks of several different lengths one must generalize the notion of digit sequences. In base k a number is constructed from a digit sequence a[r], ..., a[1], a[0] (with  $0 \le a[i] < k$ ) according to  $Sum[a[i]k^i, \{i, 0, r\}]$ . But given a sequence of digits that are each 0 or 1, it is also possible for example to construct numbers according to

Sum[a[i] Fibonacci[i + 2], {i, 0, r}]. (As discussed on page 1070, this representation is unique so long as one does not allow any pairs of adjacent 1's in the digit sequence.) It then turns out that if one expresses the position n as a generalized digit sequence of this kind, then the color of the corresponding element in substitution system (c) is just the last digit in this sequence.

- **Connections with square roots.** Substitution systems such as (c) above are related to projections of lines with quadratic irrational slopes, as discussed on page 904.
- **Spectra of substitution systems.** See page 1080.
- Representation by paths. An alternative to representing substitution systems by 1D sequences of black and white squares is to use 2D paths consisting of sequences of left and right turns. The paths obtained at successive steps for rule (b) above are shown below.

The pictures below show paths obtained with the rule  $\{1 \rightarrow \{1\}, 0 \rightarrow \{0, 0, 1\}\}$ , starting from  $\{0\}$ . Note the similarity to the 2D system shown on page 190.

![](Images/_page_907_Picture_7.jpeg)

When the paths do not cross themselves, nested structure is evident. But in a case like the rule  $\{1 \rightarrow \{0, 0, 1\}, 0 \rightarrow \{1, 0\}\}$  starting with  $\{1\}$ , the presence of many crossings tends to hide such regularity, as in the pictures below.

![](Images/_page_907_Picture_9.jpeg)

■ **Paperfolding sequences.** The sequence of up and down creases in a strip of paper that is successively folded in half is given by a substitution system; after *t* steps the sequence turns out to be *NestList[Join[#, {0}, Reverse[1-#]] &, {0}, t]*. The corresponding path (effectively obtained by making each crease a right angle) is shown below. (See page 189.)

![](Images/_page_907_Picture_11.jpeg)

**2D** representations. Individual sequences from 1D substitution systems can be displayed in 2D by breaking them into a succession of rows. The pictures below show results for the substitution systems on page 83. In case (b), with rows chosen to be  $2^j$  elements in length, the leftmost column will always be identical to the beginning of the sequence, and in addition every interior element will be black exactly when the cell at the top of its column has the same color as the one at the beginning of its row. In case (c), stripes appear at angles related to *Golden Ratio*.

![](Images/_page_907_Figure_13.jpeg)

■ Page 84 · Other examples.

(a) (Period-doubling sequence) After t steps, there are a total of  $2^t$  elements, and the sequence is given by  $Nest[MapAt[1-\#\&, Join(\#, \#], -1]\&, \{0\}, t]$ . It contains a total of  $Round[2^t/3]$  black elements, and if the last element is dropped, it forms a palindrome. The  $n^{th}$  element is given by Mod[IntegerExponent[n, 2], 2]. As discussed on page 885, the sequence appears in a vertical column of cellular automaton rule 150. The Thue-Morse sequence discussed on page 890 can be obtained from it by applying

1 - Mod[Flatten[Partition[FoldList[Plus, 0, list], 1, 2]], 2]

- (b) The  $n^{th}$  element is simply Mod[n, 2].
- (c) Same as (a), after the replacement  $1 \rightarrow \{1, 1\}$  in each sequence. Note that the spectra of (a) and (c) are nevertheless different, as discussed on page 1080.
- (d) The length of the sequence at step t satisfies a[t] = 2a[t-1] + a[t-2], so that  $a[t] = Round[(1+\sqrt{2})^{t-1}/2]$  for t > 1. The number of white elements at step t is then  $Round[a[t]/\sqrt{2}]$ . Much like example (c) on page 83 there are m+1 distinct blocks of length m, and with  $f = Floor[(1-1/\sqrt{2})(\#+1/\sqrt{2})]$  & the n<sup>th</sup> element of the sequence is given by f[n+1] f[n] (see page 903).

- (e) For large t the number of elements increases like  $\lambda^t$  with  $\lambda = (\sqrt{13} + 1)/2$ ; there are always  $\lambda$  times as many white elements as black ones.
- (f) The number of elements at step t is  $Round[(1 + \sqrt{2})^t/2]$ , and the  $n^{\text{th}}$  element is given by  $Floor[\sqrt{2} (n+1)] - Floor[\sqrt{2} n]$  (see
- (g) The number of elements is the same as in (f).
- (h) The number of black elements is  $2^{t-1}$ ; the total number of elements is  $2^{t-2}(t+1)$ .
- (i) and (j) The total number of elements is 3<sup>t-1</sup>.
- History. In their various representations, 1D substitution systems have been invented independently many times for many different purposes. (For the history of fractals and 2D substitution systems see page 934.) Viewed as generators of sequences with certain combinatorial properties, substitution systems such as example (b) on page 83 appeared in the work of Axel Thue in 1906. (Thue's stated purpose in this work was to develop the science of logic by finding difficult problems with possible connections to number theory.) The sequence of example (b) was rediscovered by Marston Morse in 1917 in connection with his development of symbolic dynamics—and in finding what could happen in discrete approximations to continuous systems. Studies of general neighbor-independent substitution systems (sometimes under such names as sequence homomorphisms, iterated morphisms and uniform tag systems) have continued in this context to this day. In addition, particularly since the 1980s, they have been studied in the context of formal language theory and the so-called combinatorics of words. (Period-doubling phenomena also led to contact with physics starting in the late 1970s.)

Independent of work in symbolic dynamics, substitution systems viewed as generators of sequences were reinvented in 1968 by Aristid Lindenmayer under the name of L systems for the purpose of constructing models of branching plants (see page 1005). So-called 0L systems correspond to my neighbor-independent substitution systems; 1L systems correspond to the neighbor-dependent substitution systems on page 85. Work on L systems has proceeded along two quite different lines: modelling specific plant systems, and investigating general computational capabilities. In the mid-1980s, particularly through the work of Alvy Ray Smith, L systems became widely used for realistic renderings of plants in computer graphics.

The idea of constructing abstract trees such as family trees according to definite rules presumably goes back to antiquity. The tree representation of rule (c) from page 83 was for example probably drawn by Leonardo Fibonacci in 1202.

The first six levels of the specific pattern in example (a) on page 83 correspond exactly to the segregation diagram for the I Ching that arose in China as early as 2000 BC. Black regions represent yin and white ones yang. The elements on level six correspond to the 64 hexagrams of the I Ching. At what time the segregation diagram was first drawn is not clear, but it was almost certainly before 1000 AD, and in the 1600s it appears to have influenced Gottfried Leibniz in his development of base 2 numbers.

Viewed in terms of digit sequences, example (d) from page 83 was discussed by Georg Cantor in 1883 in connection with his investigations of the idea of continuity. General relations between digit sequences and sequences produced by neighborindependent substitution systems were found in the 1960s. Connections of sequences such as (c) to algebraic numbers (see page 903) arose in precursors to studies of wavelets.

Paths representing sequences from 1D substitution systems can be generated by 2D geometrical substitution systems, as on page 189. The "C" curve shown on the facing page and on page 190 was for example described by Paul Lévy in 1937, and was rediscovered as the output of a simple computer program by William Gosper in the 1960s. Paperfolding or so-called dragon curves (as shown above) were discussed by John Heighway in the mid-1960s, and were analyzed by Chandler Davis, Donald Knuth and others. These curves have the property that they eventually fill space. Space-filling curves based on slightly more complicated substitution systems were already discussed by Giuseppe Peano in 1890 and by David Hilbert in 1891 in connection with questions about the foundations of calculus.

Sequences from substitution systems have no doubt appeared over the years as incidental features of great many pieces of mathematical work. As early as 1851, for example, Eugène Prouhet showed that if sequences of integers were partitioned according to sequence (b) on page 83, then sums of powers of these integers would be equal: thus Apply[Plus, Flatten[Position[s, i]]<sup>k</sup>] is equal for i = 0 and i = 1 if s is a sequence of the form (b) on page 83 with length  $2^m$ , m > k. The optimal solution to the Towers of Hanoi puzzle invented in 1883 also turns out to be an example of a substitution system sequence.

#### Sequential Substitution Systems

■ Implementation. Sequential substitution systems can be implemented quite directly by using Mathematica's standard mechanism for applying transformation rules to symbolic

Attributes[s] = Flat

the state of a sequential substitution system at a particular step can be represented by a symbolic expression such as s[1, 0, 1, 0]. The rule on page 82 can then be given simply as  $s[1, 0] \rightarrow s[0, 1, 0]$ 

while the rule on page 85 becomes

```
\{s[0, 1, 0] \rightarrow s[0, 0, 1], s[0] \rightarrow s[0, 1, 0]\}
```

expressions. Having made the definition

The *Flat* attribute of s makes these rules apply not only for example to the whole sequence s[1, 0, 1, 0] but also to any subsequence such as s[1, 0]. (With s being Flat, s[s[1, 0], 1, s[0]] is equivalent to s[1, 0, 1, 0] and so on. A Flat function has the mathematical property of being associative.) And with this setup, t steps of evolution can be found with

```
SSSEvolveList[rule_, init_s, t_Integer] := 
NestList[# /. rule &, init, t]
```

Note that as an alternative to having s be Flat, one can explicitly set up rules based on patterns such as  $s[x_{--}, 1, 0, y_{--}] \rightarrow s[x, 0, 1, 0, y]$ . And by using rules such as  $s[x_{--}, 1, 0, y_{--}] \rightarrow s[s, 0, 1, 0, y]$ , Length[s[x]] one can keep track of the positions at which substitutions are made. (StringReplace replaces all occurrences of a given substring, not just the first one, so cannot be used directly as an alternative to having a flat function.)

- **Capabilities.** Even with the single rule  $\{s[1, 0] \rightarrow s[0, 1]\}$ , a sequential substitution system can sort its initial conditions so that all 0's occur before all 1's. (See also page 1113.)
- Order of replacements. For many sequential substitution systems the evolution effectively stops because a string is produced to which none of the replacements given apply. In most sequential substitution systems there is more than one possible replacement that can in principle apply at a particular step, so the order in which the replacements are tried matters. (Multiway systems discussed on page 497 are what result if all possible replacements are performed at each step.) There are however special sequential substitution systems (those with the so-called confluence property discussed on page 1036) in which in a certain sense the order of replacements does not matter.
- History. Sequential substitution systems are closely related to the multiway systems discussed on page 938, and are often considered examples of production systems or string rewriting systems. In the form I discuss here, they seem to have arisen first under the name "normal algorithms" in the work of Andrei Markov in the late 1940s on computability and the idealization of mathematical processes. Starting in

the 1960s text editors like TECO and ed used sequential substitution system rules, as have string-processing languages such as SNOBOL and perl. *Mathematica* uses an analog of sequential substitution system rules to transform general symbolic expressions. The fact that new rules can be added to a sequential substitution system incrementally without changing its basic structure has made such systems popular in studies of adaptive programming.

#### Tag Systems

■ **Implementation.** With the rules for case (a) on page 94 given for example by

 $\{2, \{\{0, 0\} \rightarrow \{1, 1\}, \{1, 0\} \rightarrow \{\}, \{0, 1\} \rightarrow \{1, 0\}, \{1, 1\} \rightarrow \{0, 0, 0\}\}\}$  the evolution of a tag system can be obtained from

 $TSEvolveList[\{n\_, rule\_\}, init\_, t\_] := NestList[If[Length[#] < n, {\}, Join[Drop[#, n], Take[#, n] /. rule]] &, init, t]$ 

An alternative implementation is based on applying to the list at each step rules such as

```
 \{\{0,\,0,\,s_{--}\} \to \{s,\,1,\,1\},\,\{1,\,0,\,s_{--}\} \to \{s\},\\ \{0,\,1,\,s_{--}\} \to \{s,\,1,\,0\},\,\{1,\,1,\,s_{--}\} \to \{s,\,0,\,0,\,0\}\}
```

There are a total of  $((k^{r+1}-1)/(k-1))^{k^n}$  possible rules if blocks up to length r can be added at each step and k colors are allowed. For r=3, k=2 and n=2 this is 50,625.

- Page 94 · Randomness. To get some idea of the randomness of the behavior, one can look at the sequence of first elements produced on successive steps. In case (a), the fraction of black elements fluctuates around 1/2; in (b) it approaches 3/4; in (d) it fluctuates around near 0.3548, while in (e) and (f) it does not appear to stabilize.
- **History.** The tag systems that I consider are generalizations of those first discussed by Emil Post in 1920 as simple idealizations of certain syntactic reduction rules in Alfred Whitehead and Bertrand Russell's Principia Mathematica (see page 1149). Post's tag systems differ from mine in that his allow the choice of block that is added at each step to depend only on the very first element in the sequence at that step (see however page 670). (The lag systems studied in 1963 by Hao Wang allow dependence on more than just the first element, but remove only the first element.) It turns out that in order to get complex behavior in such systems, one needs either to allow more than two possible colors for each element, or to remove more than two elements from the beginning of the sequence at each step. Around 1921, Post apparently studied all tag systems of his type that involve removal and addition of no more than two elements at each step, and he concluded that none of them produced complicated behavior. But then he looked at rules that

remove three elements at each step, and he discovered the rule  $\{3, \{\{0, -, -\} \rightarrow \{0, 0\}, \{1, -, -\} \rightarrow \{1, 1, 0, 1\}\}\}$ . As he noted, the behavior of this rule varies considerably with the initial conditions used. But at least for all the initial conditions up to length 28, the rule eventually just leads to behavior that repeats with a period of 1, 2, 6, 10, 28 or 40. With more than two colors, one finds that rules of Post's type which remove just two elements at each step can yield complex behavior, even starting from an initial condition such as {0, 0}. An example is  $\{2, \{\{0, \}\} \rightarrow \{2, 1\}, \{1, \}\} \rightarrow \{0\}, \{2, \}\} \rightarrow \{0, 2, 1, 2\}\}\}$ . (See also pages 1113 and 1141.)

#### Cyclic Tag Systems

■ Implementation. With the rules for the cyclic tag system on page 95 given as {{1, 1}, {1, 0}}, the evolution can be obtained from

```
CTEvolveList[rules_, init_, t_] :=
  Map[Last, NestList[CTStep, {rules, init}, t]]
CTStep[{{r_, s___}, {0, a___}}] := {{s, r}, {a}}
CTStep[\{\{r_{,s_{,s_{,s_{,s_{,s_{,s_{,s_{,s_{,s_{,s
CTStep[\{u_{-}, \{\}\}] := \{u, \{\}\}\}
```

The leading elements on many more than *t* successive steps can be obtained directly from

```
CTList[rules_, init_, t_] :=
  Flatten[Map[Last, NestList[CTListStep, {rules, init}, t]]]
CTListStep[{rules_, list_}] :=
  {RotateLeft[rules, Length[list]], Flatten[rules[
        Mod[Flatten[Position[list, 1]], Length[rules], 1]]]]}
```

■ Page 95 · Generalizations. The implementation above immediately allows cyclic tag systems which cycle through a list of more than two blocks. (With just one block the behavior is always repetitive.) Cyclic tag systems which allow any value for each element can be obtained by adding the rule

```
CTStep[{{r_, s___}, {n_, a___}}] :=
 {{s, r}, Flatten[{a, Table[r, {n}]}}}
```

The leading elements in this case can be obtained using CTListStep[{rules\_, list\_}] := {RotateLeft[rules, Length[list]], With[{n = Length[rules]}, Flatten[Apply[Table[#1, {#2}] &, Map[Transpose[ {rules, #}] &, Partition[list, n, n, 1, 0]], {2}]]]}

■ Mechanical implementation. Cyclic tag systems admit a particularly straightforward mechanical implementation. Black and white balls are kept in a trough as in the picture below. At each step the leftmost ball in the trough is released, and if this ball is black (as determined, for example, by size) a mechanism causes a new block of balls to be added at the right-hand end of the trough. This mechanism can work in several ways; typically it will involve a rotary element that determines which case of the rule to use at each step. Rule (e) from the main text allows a particularly simple supply of new balls. Note that the system will inevitably fail if the trough overflows with balls.

■ Page 96 · Properties. Assuming that black and white elements occur in an uncorrelated way, then the sequences in a cyclic tag system with n blocks should grow by an average of Count[Flatten[rules], 1]/n-1 elements at each step. With n = 2 blocks, this means that growth can occur only if the total number of black elements in both blocks is more than 3. Rules such as {{1, 0}, {0, 1}} and {{1, 1}, {0}} therefore yield repetitive behavior with sequences of limited length.

Note that if all blocks in a cyclic tag system with n blocks have lengths divisible by n, then one can tell in advance on which steps blocks will be added, and the overall behavior obtained must correspond to a neighbor-independent substitution system. The rules for the relevant substitution system may however depend on the initial conditions for the cyclic tag system.

Flatten[{1, 0, CTList[{{1, 0, 0, 1}, {0, 1, 1, 0}}, {0, 1}, t]}] gives for example the Thue-Morse substitution system  $\{1 \to \{1, 0\}, 0 \to \{0, 1\}\}.$ 

In example (a), the elements are correlated, so that slower growth occurs than in the estimate above. In example (c), the elements are again correlated: the growth is by an average of  $(\sqrt{5} - 1)/2 \approx 0.618$  elements at each step, and the first elements on alternate steps form the same nested sequence as obtained from the substitution system  $\{1 \rightarrow \{1, 0\}, 0 \rightarrow \{1\}\}$ . In example (d), the frequency of 1's among the first elements of the sequence is approximately 3/4; {0, 0} never occurs, and the frequency of {1, 1} is approximately 1/2. In example (e), the frequency of 1's is again about 3/4, but now {0, 0} occurs with frequency 0.05, {1, 1} occurs with frequency 0.55, while {0, 0, 0} and {0, 1, 0} cannot occur.

■ History. Cyclic tag systems were studied by Matthew Cook in 1994 in connection with working on the rule 110 cellular automaton for this book. The sequence {1, 2, 2, 1, 1, 2, ...} defined by the property list == Map[Length, Split[list]] was suggested as a mathematical puzzle by William Kolakoski in 1965 and is equivalent to

```
Join[{1, 2}, Map[First, CTEvolveList[{{1}, {2}}, {2}, t]]]
```

It is known that this sequence does not repeat, contains no more than two identical consecutive blocks, and has at least very close to equal numbers of 1's and 2's. Replacing 2 by 3 yields a sequence which has a fairly simple nested form.

#### Register Machines

■ **Implementation.** The state of a register machine at a particular step can be represented by the pair {n, list}, where n gives the position in the program of current instruction being executed (the "program counter") and list gives the values of the registers. The program for the register machine on page 99 can then be given as

```
{i[1], d[2, 1], i[2], d[1, 3], d[2, 1]} where i[\_] represents an increment instruction, and d[\_, \_] a decrement jump.
```

With this setup, the evolution of any register machine can be implemented using the functions (a typical initial condition is  $\{1, \{0, 0\}\}$ )

```
RMStep[prog_, {n_Integer, list_List}] := If{n > Length[prog],
```

The total number of possible programs of length n using k registers is  $(k(1+n))^n$ . Note that by prepending suitable i[r] instructions one can effectively set up initial conditions with arbitrary values in registers.

■ **Halting.** It is sometimes convenient to think of register machines as going into a special halt state if they try to execute instructions beyond the end of their program. (See page 1137.) The fraction of possible register machines that do this starting from initial condition  $\{1, \{0, 0\}\}$  decreases steadily with program length n, reaching about 0.76 for n = 8. The most common number of steps before halting is always n, while the maximum numbers of steps for n up to n is n0, n1, n2, n3, n3, n4, n5, n6, n7, n7, n8, n8, n9, where in the last case this is achieved by

```
{i[1], d[2, 7], d[2, 1], i[2], i[2], d[1, 4], i[1], d[2, 3]}
```

■ Page 101 · Extended instruction sets. One can consider also including instructions such as

```
RMExecute[eq[r1_, r2_, m_], {n_, list_}] :=
    If[list[[r1]] == list[[r2]], {m, list}, {n + 1, list}]

RMExecute[add[r1_, r2_], {n_, list_}] :=
    {n + 1, ReplacePart[list, list[[r1]] + list[[r2]], r1]}

RMExecute[jmp[r1_], {n_, list_}] := {list[[r1]], list}
```

Note that by being able to add and subtract only 1 at each step, the register machines shown in the main text necessarily operate quite slowly: they always take at least n steps to build up a number of size n. But while extending the instruction set can increase the speed of operations, it does not appear to yield a much larger density of machines with complex behavior.

- History. Register machines (also known as counter machines and program machines) are a fairly obvious idealization of practical computers, and have been invented in slightly different forms several times. Early uses of them were made by John Shepherdson and Howard Sturgis around 1959 and Marvin Minsky around 1960. Somewhat similar constructs were part of Kurt Gödel's 1931 work on representing logic within arithmetic (see page 1158).
- Page 102 · Random programs. See page 1182.

#### Symbolic Systems

- **Implementation.** The evolution for t steps of the first symbolic system shown can be implemented simply by  $NestList[\# /. e[x_{-}][y_{-}] \rightarrow x[x[y]] \&, init, t]$
- **Symbolic expressions.** Expressions like Log[x] and f[x] that give values of functions are familiar from mathematics and from typical computer languages. Expressions like f[g[x]]giving compositions of functions are also familiar. But in general, as in Mathematica, it is possible to have expressions in which the head h in h[x] can itself be any expression—not just a single symbol. Thus for example f(q)[x], f(q[h])[x] and f[g][h][x] are all possible expressions. And these kinds of expressions often arise in Mathematica when one manipulates functions as a whole before applying them to arguments.  $(\partial_{xx} f[x])$  for example gives f''[x] which is Derivative[2][f][x].) (In principle one can imagine representing all objects with forms such as f[x, y] by so-called currying as f[x][y], and indeed I tried this in the early 1980s in SMP. But although this can be convenient when f is a discrete function such as a matrix, it is inconsistent with general mathematical and other usage in which for example Gamma[x] and Gamma[a, x] are both treated as values of functions.)
- **Representations.** Among the representations that can be used for expressions are:

| ĺ | functional | a[b[c[d]]]                                  | a[b][c[d]]       | a[b[c][d]]            | a[b][c][d]            |
|---|------------|---------------------------------------------|------------------|-----------------------|-----------------------|
| ĺ | Polish     | {o, a, o, b, o, c, d} {o, o, a, b, o, c, d} |                  | {∘, a, ∘, ∘, b, c, d} | {o, o, o, a, b, c, d} |
|   | operator   | a                                           | (a∘b)∘ (c∘d)     | a                     | ((a∘b)∘c)∘d           |
|   | tree       | {a, {b, {c, d}}}                            | {{a, b}, {c, d}} | {a, {{b, c}, d}}      | {{{a, b}, c}, d}      |
|   |            | a b c d                                     | a b c d          | a b c                 | d c a b               |

Typical transformation rules are non-local in all these representations. Polish representation (whose reverse form has been used in HP calculators) for an expression can be obtained using (see also page 1173)

Flatten[expr //.  $x_[y_] \rightarrow \{\circ, x, y\}$ ]

The original expression can be recovered using

First[Reverse[list] //.  $\{w_{--}, x_{-}, y_{-}, o, z_{--}\} \rightarrow \{w, y[x], z\}$ ] (Pictures of symbolic system evolution made with Polish notation differ in detail but look qualitatively similar to those made as in the main text with functional notation.)

The tree representation of an expression can be obtained using  $expr //. x_{-}[y_{-}] \rightarrow \{x, y\}$ , and when each object has just one argument, the tree is binary, as in LISP.

If only a single symbol ever appears, then all that matters is the overall structure of an expression, which can be captured as in the main text by the sequence of opening and closing brackets, given by

```
Flatten[Characters[ToString[expr]]/.
    \{"[" \to 1, "]" \to 0, "e" \to \{\}\}\}
```

■ Possible expressions. LeafCount[expr] gives the number of symbols that appear anywhere in an expression, while Depth[expr] gives the number of closing brackets at the end of its functional representation—equal to the number of levels in the rightmost branch of the tree representation. (The maximum number of levels in the tree can be computed from  $expr /. \_Symbol \rightarrow 1 //. x_[y_] \rightarrow 1 + Max[x, y].)$ 

With a list s of possible symbols, c[s, n] gives all possible expressions with LeafCount[expr] == n:

```
c[s_{-}, 1] = s; c[s_{-}, n_{-}] := Flatten[
     Table[Outer[#1[#2] &, c[s, n-m], c[s, m]], {m, n-1}]]
```

There are a total of  $Binomial[2n-2, n-1]Length[s]^n/n$  such expressions. When Length[s] = 1 the expressions correspond to possible balanced sequences of opening and closing brackets (see page 989).

■ Page 103 · Properties. All initial conditions eventually evolve to expressions of the form Nest[e, e, m], which then remain fixed. The quantity expr //.  $\{e \rightarrow 0, x_{-}[y_{-}] \rightarrow 2^{x} + y\}$  turns out to remain constant through the evolution, so this gives the final value of m for any initial condition. The maximum is Nest[2# &, 0, n] (compare page 906), achieved for initial conditions of the form Nest[#[e] &, e, n]. (By analogy with page 1122 any e expression be interpreted as Church numeral  $u = \exp r / (\{e \to 2, x_{[v]} \to v^x\}) = 2^{2^m}$ , so that  $\exp [a][b]$ evolves to *Nest[a, b, u]*.) During the evolution the rule can apply only to the inner part  $FixedPoint[Replace[\#, e[x_{-}] \rightarrow x] \&, expr]$ of an expression. The depth of this inner part for initial condition e[e][e][e][e][e] is shown below. For all initial conditions this depth seems at first to increase linearly, then to decrease in a nested way according to

```
FoldList[Plus, 0, Flatten[Table[
```

{1, 1, Table[-1, {IntegerExponent[i, 2] + 1}]}, {i, m}]]] This quantity alternates between value 1 at position  $2^{j}$  and value j at position  $2^{j}$  – j + 1. It reaches a fixed point as soon as the depth reaches 0. For initial conditions of size n, this occurs after at most  $Sum[Nest[2^{\#} \&, 0, i] - 1, \{i, n\}] + 1$  steps. (See also page 1145.)

![](Images/_page_912_Figure_15.jpeg)

- Other rules. If only a single variable appears in the rule, then typically only nested behavior can be generatedthough in an example like  $e[x_{-}][_{-}] \rightarrow e[x[e[e][e]][e]]$  it can be quite complex. The left-hand side of each rule can consist of any expression;  $e[e[x_{-}]][y_{-}]$  and  $e[e][x_{-}[y_{-}]]$  are two possibilities. However, at least with small initial conditions it seems easier to achieve complex behavior with rules based on  $e[x_{-}][y_{-}]$ . Note that rules with no explicit e's on the lefthand side always give trees with regular nested structures;  $x_{-}[y_{-}] \rightarrow x[y][x[y]]$  (or  $x_{-} \rightarrow x[x]$  in Mathematica), for example, yields balanced binary trees.
- Long halting times. Symbolic systems with rules of the form  $e[x_{-}][y_{-}] \rightarrow Nest[x, y, r]$  always evolve to fixed points though with initial conditions of size n this can take of order  $Nest[r^{\#} \&, 0, n]$  steps (see above). In general there will be symbolic systems where the number of steps to evolve to a fixed point grows arbitrarily rapidly with n (see page 1145), and indeed I suspect that there are even systems with quite simple rules where proving that a fixed point is always reached in a finite number of steps is beyond, for example, the axiom system for arithmetic (see page 1163).
- Trees. The rules given on pages 103 and 104 correspond to the transformations on trees shown below.

![](Images/_page_912_Figure_19.jpeg)

The first few steps in evolution from two initial conditions of the system on page 103 correspond to the sequences of trees below.

![](Images/_page_912_Figure_21.jpeg)

■ **Order dependence.** The operation expr /.  $lhs \rightarrow rhs$  in Mathematica has the effect of scanning the functional representation of expr from left to right, and applying rules whenever possible while avoiding overlaps. (Standard evaluation in Mathematica is equivalent to expr //. rules and uses the same ordering, while Map uses a different order.) One can have a rule be applied only once using

 $Module[\{i = 1\}, expr /. lhs \rightarrow rhs /; i++ == 1]$ 

Many symbolic systems (including the one on page 103) have the so-called Church-Rosser property (see page 1036) which implies that if a fixed point is reached in the evolution of the system, this fixed point will be the same regardless of the order in which rules are applied.

■ **History.** Symbolic systems of the general type I discuss here seem to have first arisen in 1920 in the work of Moses Schönfinkel on what became known as combinators. As discussed on page 1121 Schönfinkel introduced certain specific rules that he suggested could be used to build up functions defined in logic. Beginning in the 1930s there were a variety of theoretical studies of how logic and mathematics could be set up with combinators, notably by Haskell Curry. For the most part, however, only Schönfinkel's specific rules were ever used, and only rather specific forms of behavior were investigated. In the 1970s and 1980s there was interest in using combinators as a basis for compilation of functional programming languages, but only fairly specific situations of immediate practical relevance were considered. (Combinators have also been used as logic recreations, notably by Raymond Smullvan.)

Constructs like combinators appear to have almost never been studied in mainstream pure mathematics. Most likely the reason is that building up functions on the basis of the structure of symbolic expressions has never seemed to have much obvious correspondence to the traditional mathematical view of functions as mappings. And in fact even in mathematical logic, combinators have usually not been considered mainstream. Most likely the reason is that ever since the work of Bertrand Russell in the early 1900s it has generally been assumed that it is desirable to distinguish a hierarchy of different types of functions and objects-analogous to the different types of data supported in most programming languages. But combinators are set up not to have any restrictions associated with types. And it turns out that among programming languages Mathematica is almost unique in also having this same feature. And from experience with Mathematica it is now clear that having a symbolic system which-like combinators-has no built-in notion of types allows great generality and flexibility. (One can always set up the analog of types by having rules only for expressions whose heads have particular structures.)

■ Operator systems. One can generalize symbolic systems by having rules that define transformations for any Mathematica pattern. Often these can be thought of as one-way versions of axioms for operator systems (see page 1172), but applied only once per step (as /. does), rather than in all possible ways (as in a multiway system)—so that the evolution is just given by *NestList[# /. rule &, init, t]*. The rule  $x_- \rightarrow x \circ x$  then for example generates a balanced binary tree. The pictures below show the patterns of opening and closing parentheses obtained from operator system evolution rules in a few cases.

![](Images/_page_913_Picture_8.jpeg)

![](Images/_page_913_Picture_9.jpeg)

![](Images/_page_913_Picture_10.jpeg)

![](Images/_page_913_Picture_11.jpeg)

■ Network analogs. The state of a symbolic system can always be viewed as corresponding to a tree. If a more general network is allowed then rules based on analogs of network substitution systems from page 508 can be used. (One can also construct an infinite tree from a general network by following all its possible paths, as on page 277, but in most cases there will be no simple way to apply symbolic system rules to such a tree.)

#### How the Discoveries in This Chapter Were Made

- Page 109 · Repeatability and numerical analysis. The discrete nature of the systems that I consider in most of this book makes it almost inevitable that computer experiments on them will be perfectly repeatable. But if, as in the past, one tries to do computer experiments on continuous mathematical systems, then the situation can be different. For in such cases one must inevitably make discrete approximations for the underlying representation of numbers and for the operations that one performs on them. And in many practical situations, one relies for these approximations on "machine arithmetic"—which can differ from one computer system to another.
- Page 109 · Studying simple systems. Over the years, I have watched with disappointment the continuing failure of most scientists and mathematicians to grasp the idea of doing computer experiments on the simplest possible systems. Those with physical science backgrounds tend to add features to their systems in an attempt to produce some kind of presumed realism. And those with mathematical backgrounds tend to add features to make their systems fit in with complicated and abstract ideas-often related to continuity-that exist in modern mathematics. The result of all this has been that remarkably few truly meaningful computer experiments have ended up ever being done.

- Page 111 · The relevance of theorems. Following traditional mathematical thinking, one might imagine that the best way to be certain about what could possibly happen in some particular system would be to prove a theorem about it. But in my experience, proofs tend to be subject to many of the same kinds of problems as computer experiments: it is easy to end up making implicit assumptions that can be violated by circumstances one cannot foresee. And indeed, by now I have come to trust the correctness of conclusions based on simple systematic computer experiments much more than I trust all but the simplest proofs.
- Attitudes of mathematicians. Mathematicians often seem to feel that computer experimentation is somehow less precise than their standard mathematical methods. It is true that in studying questions related to continuous mathematics, imprecise numerical approximations have often been made when computers are used (see above). But discrete or symbolic computations can be absolutely precise. And in a sense presenting a particular object found by experiment (such as a cellular automaton whose evolution shows some particular property) can be viewed as a constructive existence proof for such an object. In doing mathematics there is often the idea that proofs should explain the result they prove—and one might not think this could be achieved if one just presents an object with certain properties. But being able to look in detail at how such an object works will in many cases provide a much better understanding than a standard abstract mathematical proof. And inevitably it is much easier to find new results by the experimental approach than by the traditional approach based on proofs.
- History of experimental mathematics. The general idea of finding mathematical results by doing computational experiments has a distinguished, if not widely discussed, history. The method was extensively used, for example, by Carl Friedrich Gauss in the 1800s in his studies of number theory, and presumably by Srinivasa Ramanujan in the early 1900s in coming up with many algebraic identities. The Gibbs phenomenon in Fourier analysis was noticed in 1898 on a mechanical computer constructed by Albert Michelson. Solitons were rediscovered in experiments done around 1954 on an early electronic computer by Enrico Fermi and collaborators. (They had been seen in physical systems by John Scott Russell in 1834, but had not been widely
- investigated.) The chaos phenomenon was noted in a computer experiment by Edward Lorenz in 1962 (see page 971). Universal behavior in iterated maps (see page 921) was discovered by Mitchell Feigenbaum in 1975 by looking at examples from an electronic calculator. Many aspects of fractals were found by Benoit Mandelbrot in the 1970s using computer graphics. In the 1960s and 1970s a variety of algebraic identities were found using computer algebra, notably by William Gosper. (Starting in the mid-1970s I routinely did computer algebra experiments to find formulas in theoretical physics—though I did not mention this when presenting the formulas.) The idea that as a matter of principle there should be truths in mathematics that can only be reached by some form of inductive reasoning-like in natural science-was discussed by Kurt Gödel in the 1940s and by Gregory Chaitin in the 1970s. But it received little attention. With the release of Mathematica in 1988, mathematical experiments began to emerge as a standard element of practical mathematical pedagogy, and gradually also as an approach to be tried in at least some types of mathematical research, especially ones close to number theory. But even now, unlike essentially all other branches of science, mainstream mathematics continues to be entirely dominated by theoretical rather than experimental methods. And even when experiments are done, their purpose is essentially always just to provide another way to look at traditional questions in traditional mathematical systems. What I do in this book-and started in the early 1980s-is, however, rather different: I use computer experiments to look at questions and systems that can be viewed as having a mathematical character, yet have never in the past been considered in any way by traditional mathematics
- Page 113 · Practicalities. The investigations described in this chapter were done using Mathematica, mostly in 1992. For larger searches, I sometimes created optimized C programs that were controlled via MathLink from within Mathematica though with the versions of Mathematica that exist today this would now be unnecessary. For my very largest searches, I used Mathematica to dispatch programs to a large number of different computers on a network, then had the computers send me email whenever they found interesting results. (See also page 854.)

#### Systems Based on Numbers

#### The Notion of Numbers

■ **Implementation of digit sequences.** A whole number n can be converted to a sequence of digits in base k using IntegerDigits[n, k] or (see also page 1094)

Reverse[Mod[NestWhileList[Floor[#/k] &, n,  $\# \ge k$  &], k]] and from a sequence of digits using FromDigits[list, k] or Fold[#/k] + #/k2 &, #/k3, list]

For a number x between 0 and 1, the first m digits in its digit sequence in base k are given by RealDigits[x, k, m] or

Floor[k NestList[Mod[k#, 1] &, x, m-1]]

and from these digits one can reconstruct an approximation to the number using FromDigits[{list, 0}, k] or

Fold[#1/k + #2 &, 0, Reverse[list]]/k

■ **Gray code.** In looking at digit sequences, it is sometimes useful to consider ordering numbers by a criterion other than their size. An example is Gray code ordering, in which successive numbers are arranged to differ in only one digit. One possible such ordering for numbers with a total of *m* digits is

```
GrayCode[m_] :=
Nest[Join[#, Length[#] + Reverse[#]] &, {0}, m]
```

The succession of sizes and digit sequences of numbers ordered in this way are shown below. (Note that the digit sequence picture is turned on its side relative to those in the main text). The number which appears at position *i* is given by <code>BitXor[i, Floor[i/2]]</code>. (Iterating the related function <code>BitXor[i, 2i]</code> yields numbers whose digit sequences correspond to the rule 60 cellular automaton).

![](Images/_page_916_Figure_12.jpeg)

■ A note for mathematicians. Some mathematicians will at first find what I say in this chapter quite bizarre. It may help

however to point out that the traditional view of numbers already shows signs of breaking down in many studies of dynamical systems done over the past few decades. Thus for example, instead of getting results in terms of continuous functions, Cantor sets very often appear. Indeed, the symbolic dynamics approach that is often used in dynamical systems theory is quite close to the digit sequence approach I use here—Markov partitions in dynamical systems theory are essentially just generalizations of digit expansions.

However, in the cases that are analyzed in dynamical systems theory, only shifts and other very simple operations are typically performed on digit sequences. And as a result, most of the phenomena that I discuss in this chapter have not been seen in work done in dynamical systems theory.

■ History of numbers. Numbers were probably first used many thousands of years ago in commerce, and initially only whole numbers and perhaps rational numbers were needed. But already in Babylonian times, practical problems of geometry began to require square roots. Nevertheless, for a very long time, and despite some development of algebra, only numbers that could somehow in principle be constructed mechanically were ever considered. The invention of fluxions by Isaac Newton in the late 1600s, however, introduced the idea of continuous variablesnumbers with a continuous range of possible sizes. But while this was a convenient and powerful notion, it also involved a new level of abstraction, and it brought with it considerable confusion about fundamental issues. In fact, it was really only through the development of rigorous mathematical analysis in the late 1800s that this confusion finally began to clear up. And already by the 1880s Georg Cantor and others had constructed completely discontinuous functions, in which the idea of treating numbers as continuous variables where only the size matters was called into question. But until almost the 1970s, and the emergence of fractal geometry and chaos theory, these functions were largely considered as mathematical curiosities, of no practical relevance. (See also page 1168.)

Independent of pure mathematics, however, practical applications of numbers have always had to go beyond the abstract idealization of continuous variables. For whether one does calculations by hand, by mechanical calculator or by electronic computer, one always needs an explicit representation for numbers, typically in terms of a sequence of digits of a certain length. (From the 1930s to 1960s, some work was done on so-called analog computers which used electrical voltages to represent continuous variables, but such machines turned out not to be reliable enough for most practical purposes.) From the earliest days of electronic computing, however, great efforts were made to try to approximate a continuum of numbers as closely as possible. And indeed for studying systems with fairly simple behavior, such approximations can typically be made to work. But as we shall see later in this chapter, with more complex behavior, it is almost inevitable that the approximation breaks down, and there is no choice but to look at the explicit representations of numbers. (See also page 1128.)

■ History of digit sequences. On an abacus or similar device numbers are in effect represented by digit sequences. In antiquity however most systems for writing numbers were like the Roman one and not based on digit sequences. An exception was the Babylonian base 60 system (from which hours:minutes:seconds notation derives). The Hindu-Arabic base 10 system in its modern form probably originated around 600 AD, and particularly following the work of Leonardo Fibonacci in the early 1200s, became common by the 1400s. Base 2 appears to have first been considered explicitly in the early 1600s (notably by John Napier in 1617), and was studied in detail by Gottfried Leibniz starting in 1679. The possibility of arbitrary bases was stated by Blaise Pascal in 1658. Various bases were used in puzzles, but rarely in pure mathematics (work by Georg Cantor in the 1860s being an exception). The first widespread use of base 2 was in electronic computers, starting in the late 1940s. Even in the 1980s digit sequences were viewed by most mathematicians as largely irrelevant for pure mathematical purposes. The study of fractals and nesting, the appearance of many algorithms involving digit sequences and the routine use of long numbers in Mathematica have however gradually made digit sequences be seen as more central to mathematics.

#### **Elementary Arithmetic**

■ Page 117 · Substitution systems. There are many connections between digit sequences and substitution systems, as

discussed on page 891. The pattern shown here is essentially a rotated version of the pattern generated by the first substitution system on page 83.

■ **Page 117 · Digit counts.** The number of black squares on row n in the pattern shown here is given by DigitCount[n, 2, 1] and is plotted below. This function appeared on page 870 in the discussion of binomial coefficients modulo 2, and will appear again in several other places in this book. Note the inequality  $1 \le DigitCount[n, 2, 1] \le Log[2, n]$ . Formulas for DigitCount[n, 2, 1] include n - IntegerExponent[n!, 2] and

 $2n-Log[2, Denominator[Derivative[n]](1-\#)^{-1/2} \&][0]/n!]]$  Straightforward generalizations of *DigitCount* can be defined for integer and non-integer bases and by looking not only at the total number of digits but also at correlations between digits. In all cases the analogs of the picture below have a nested structure.

![](Images/_page_917_Figure_9.jpeg)

■ **Negative bases.** Given a suitable list of digits from 0 to k-1 one can obtain any positive or negative number using FromDigits[list, -k]. The picture below shows the digit sequences of successive numbers in base -2; the row j from the bottom turns out to consist of alternating black and white blocks of length  $2^j$ . (In ordinary base 2 a number -n can be represented as on a typical electronic computer by complementing each digit, including leading 0's.) (See also page 1093.)

![](Images/_page_917_Picture_11.jpeg)

- **Non-power bases.** One can consider representing numbers by  $Sum[a[n]f[n], \{n, 0, \infty\}]$  where the f[n] need not be  $k^n$ . So long as f[n] grows less rapidly than  $2^n$  (as when f = Fibonacci or f = Prime), digits 0 and 1 will suffice, though the representation is not generally unique. (See page 1070.)
- **Multiplicative digit sequences.** One can consider generalizations of digit sequences in which numbers are broken into parts combined not by addition but by multiplication. Since numbers can be factored uniquely into products of powers of primes, a number can be specified by a list in which 1's appear at the positions of the appropriate *Prime[m]*<sup>n</sup> (which can be sorted by size) and 0's appear elsewhere, as shown below. Note that unlike the case of ordinary additive digits, far more than *Log[m]* digits are required to specify a number *m*.

![](Images/_page_918_Figure_2.jpeg)

■ Page 120 · Powers of three in base 2. The  $n^{\text{th}}$  row in the pattern shown can be obtained simply as  $IntegerDigits[3^n, 2]$ . Even such individual rows seem in many respects random. The picture below shows the fraction of 1's that appear on successive rows. The fraction seems to tend to 1/2.

![](Images/_page_918_Figure_4.jpeg)

If one looks only at the rightmost s columns of the pattern, one sees repetition—but the period of the repetition grows like  $2^s$ . Typical vertical columns have one obvious deviation from randomness: it is twice as probable for the same colors to occur on successive steps than for opposite colors. (For multiplier m in base k, the relative frequencies of pairs  $\{i, j\}$  are given by Quotient[ai-j-1+m, k]-Quotient[mi-j-1, k].)

The sequence  $Mod[3^n, 2^s]$  obtained from the rightmost s digits corresponds to a simple linear congruential pseudorandom number generator. Such generators are widely used in practical computer systems, as discussed further on page 974. (Note that in the particular case used here, pairs of numbers  $Mod[\{3^n, 3^{n+1}\}, 2^s]$  always lie on lines; with multipliers other than 3, such regularities may occur for longer blocks of numbers.)

Note that if one uses base 6 rather than base 2, then as shown on page 614 powers of 3 still yield a complicated pattern, but all operations are strictly local, and the system corresponds to a cellular automaton with 6 possible colors for each cell and rule  $\{a_-, b_-, c_-\} \rightarrow 3 \, Mod[b, 2] + Floor[c/2]$  (see page 1093).

- **Leading digits.** In base *b* the leading digits of powers are not equally probable, but follow the logarithmic law from page 914.
- Page 122 · Powers of 3/2. The  $n^{th}$  value shown in the plot here is  $Mod[(3/2)^n, 1]$ . Measurements suggest that these values are uniformly distributed in the range 0 to 1, but despite a fair amount of mathematical work since the 1940s, there has been no substantial progress towards proving this.

In base 6,  $(3/2)^n$  is a cellular automaton with rule

 $\{a_-, b_-, c_-\} \rightarrow 3 \, Mod[a + Quotient[b, 2], 2] + Quotient[3 \, Mod[b, 2] + Quotient[c, 2], 2]$ 

(Note that this rule is invertible.) Looking at  $u(3/2)^n$  then corresponds to studying the cellular automaton with an initial

condition given by the base 6 digits of u. It is then possible to find special values of u (an example is 0.166669170371...) which make the first digit in the fractional part of u (3/2)<sup>n</sup> always nonzero, so that  $Mod[u(3/2)^n, 1] > 1/6$ . In general, it seems that  $Mod[u(3/2)^n, 1]$  can be kept as large as about 0.3 (e.g. with u = 0.38906669065...) but no larger.

- **General powers.** It has been known in principle since the 1930s that  $Mod[h^n, 1]$  is uniformly distributed in the range 0 to 1 for almost all values of h. However, no specific value of h for which this is true has ever been explicitly found. (Some attempts to construct such values were made in the 1970s.) Exceptions are known to include so-called Pisot numbers such as GoldenRatio,  $\sqrt{2} + 1$  and  $Root[\#^3 \# 1 \&$ , 1] (the numerically smallest of all Pisot numbers) for which  $Mod[h^n, 1]$  becomes 0 or 1 for large n. Note that  $Mod[x h^n, 1]$  effectively extracts successive digits of x in base h (see pages 149 and 919).
- Multiples of irrational numbers. Instead of powers one can consider successive multiples *Mod[h n, 1]* of a number *h*. The pictures below show results obtained as a function of *n* for various choices of *h*. (These correspond to positions of a particle bouncing around in an idealized box, as discussed on pages 971 and 1022.)

![](Images/_page_918_Figure_16.jpeg)

When h is a rational number, the sequence always repeats. But in all other cases, the sequence does not repeat, and in fact it is known that a uniform distribution of values is obtained. (The average difference of successive values is maximized for h = Golden Ratio, as mentioned on page 891.)

■ **Relation to substitution systems.** Despite the uniform distribution result in the note above, the sequence Floor[(n+1)h] - Floor[nh] is definitely not completely random, and can in fact be generated by a sequence of substitution rules. The first m rules (which yield far more than m elements of the original sequence) are obtained for any h that is not a rational number from the continued fraction form (see page 914) of h by

 $\begin{aligned} & \textit{Map}[(\{0 \rightarrow \textit{Join}[\#, \{1\}], 1 \rightarrow \textit{Join}[\#, \{1, 0\}]\} \&)[\textit{Table}[0, \\ & \{\#-1\}]] \&, \textit{Reverse}[\textit{Rest}[\textit{ContinuedFraction}[h, m]]]] \end{aligned}$ 

Given these rules, the original sequence is given by Floor[h] + Fold[Flatten[#1 /. #2] &, {0}, rules]

If *h* is the solution to a quadratic equation, then the continued fraction form is repetitive, and so there are a limited number

of different substitution rules. In this case, therefore, the original sequence can be found by a neighbor-independent substitution system of the kind discussed on page 82. For h = GoldenRatio the substitution system is  $\{0 \rightarrow \{1\}, 1 \rightarrow \{1, 0\}\}$  (see page 890), for  $h = \sqrt{2}$  it is  $\{0 \rightarrow \{0, 1\}, 1 \rightarrow \{0, 1, 0\}\}$  (see page 892) and for  $h = \sqrt{3}$  it is  $\{0 \rightarrow \{1, 1, 0\}, 1 \rightarrow \{1, 1, 0, 1\}\}$ . (The presence of nested structure is particularly evident in  $FoldList[Plus, 0, Table[Mod[hn, 1] - 1/2, \{n, max\}]]$ .) (See also pages 892, 916, 932 and 1084.)

- Other uniformly distributed sequences. Cases in which Mod[a[n], 1] is uniformly distributed include  $\sqrt{n}$ , nLog[n], Log[Fibonacci[n]], Log[n!],  $hn^2$  and hPrime[n] (h irrational) and probably nSin[n]. (See also page 914.)
- Page 122 · Implementation. The evolution for *t* steps of the system at the top of the page can be computed simply by NestList[If[EvenQ[#], 3#/2, 3(# + 1)/2] &, 1, t]
- Page 122 · The 3n+1 problem. The system described here is similar to the so-called 3n+1 problem, in which one looks at the rule  $n \rightarrow If[EvenQ[n], n/2, (3n+1)/2]$  and asks whether for any initial value of n the system eventually evolves to 1 (and thereafter simply repeats the sequence 1, 2, 1, 2, ...). It has been observed that this happens for all initial values of n up to at least  $10^{16}$ , but despite a fair amount of mathematical effort since the problem was first posed in the 1930s, no general proof for all values of n has ever been found. (For negative initial n, the evolution appears always to reach -1, -5 or -17, and then repeat with periods 1, 3 or 11 respectively.) An alternative formulation is to ask whether for all n

 $FixedPoint[(3#/2^IntegerExponent[#, 2] + 1)/2 \&, n] == 2$ 

With the rule  $n \rightarrow If[EvenQ[n], 5 n/2, (n+1)/2]$  used in the main text, the sequence produced repeats if n ever reaches 2, 4 or 40 (and possibly higher numbers). But with initial values of n up to 10,000, this happens in only 642 cases, and with values up to 100,000 it happens in only 2683 cases. In all other cases, the values of n in the sequence appear to grow forever.

To get some idea about the origin of this behavior, one can assume that successive values of n are randomly even and odd with equal probability. And with this assumption, n should increase by a factor of 5/2 half the time, and decrease by a factor close to 1/2 the rest of the time—so that after t steps it should be multiplied by an overall factor of about  $(\sqrt{5}/2)^t$ . Starting with n = 6, the effective exponents for  $t = 10 \, ^n$  Range[6] are (39.6, 245.1, 1202.8, 9250.7, 98269.8, 1002020.4). One reason that all sequences do not grow forever is that even with perfect randomness, there will be fluctuations, and occasionally n will reach a low value that makes it get stuck in a repetitive sequence.

If one applies the same kind of argument to the standard  $3\,n+1$  problem, then one concludes that n should on average decrease by a factor of  $\sqrt{3}/2$  at each step, making it unsurprising that at least in most cases n eventually reaches the value 1. Indeed, averaging over many initial values of n, there is good quantitative agreement between the predictions of the randomness approximation and the actual  $3\,n+1$  problem. But since there is no fundamental basis for the randomness approximation, it is still conceivable that a particular value of n exists that does not follow its predictions.

The pictures below show how many steps are needed to reach value 1 starting from different values of n. Case (a) is the standard 3n+1 problem. Cases (b) and (c) use somewhat different rules that yield considerably simpler behavior. In case (b), the number of steps is equal to the number of base 2 digits in n, while in case (c) it is determined by the number of 1's in the base 2 digit sequence of n.

![](Images/_page_919_Figure_10.jpeg)

■ 3*n*+1 **problem as cellular automaton.** If one writes the digits of *n* in base 6, then the rule for updating the digit sequence is a cellular automaton with 7 possible colors (color 6 works as an end marker that appears to the left and right of the actual digit sequence):

$$\{a_{-}, b_{-}, c_{-}\} \rightarrow If[b = 6, If[EvenQ[a], 6, 4], 3 Mod[a, 2] + Quotient[b, 2] /. 0 \rightarrow 6 /; a == 6]$$

The 3n+1 problem can then be viewed as a question about the existence of persistent structure in this cellular automaton

■ **Reconstructing initial conditions.** Given a particular starting value of *n*, it is difficult to predict what precise sequence of even and odd values will be obtained in the system on page 122. But given *t* steps in this sequence as a list of 0's and 1's, the

following function will reconstruct the rightmost t digits in the starting value of n:

IntegerDigits[First[Fold[{Mod[If[OddQ[#2], 2First[#1]-1, 2 First[#1] PowerMod[5, -1, Last[#1]]], Last[#1]] 2 Last[#1]} &, {0, 2}, Reverse[list]]], 2, Length[list]]

■ **A reversible system.** In both the ordinary 3n+1 problem and in the systems discussed in the main text different numbers often evolve to the same value so that there is no unique way to reverse the evolution. However, with the rule

 $n \rightarrow If[EvenQ[n], 3n/2, Round[3n/4]]$ 

it is always possible to go backwards by the rule  $n \rightarrow If[Mod[n, 3] == 0, 2n/3, Round[4n/3]]$ 

The picture shows the number of base 10 digits in numbers obtained by backward and forward evolution from n = 8. For n < 8, the system always enters a short cycle. Starting at n = 44, there is also a length 12 cycle. But apart from these cycles, the numbers produced always seem to grow without bound at an average rate of  $3/(2\sqrt{2})$  in the forward direction, and  $24^{1/3}/3$ in the backward direction (at least all numbers up to 10,000 grow to above 10<sup>100</sup>). Approximately one number in 20 has the property that evolution either backward or forward from it never leads to a smaller number.

![](Images/_page_920_Figure_8.jpeg)

■ Page 125 · Reversal-addition systems. The operation that is performed here is

 $n \rightarrow n + FromDigits[Reverse[IntegerDigits[n, 2]], 2]$ 

After a few steps, the digit sequence obtained is typically reversal symmetric (a generalized palindrome) except for the interchange of 0 and 1, and for the presence of localized structures. The sequence expands by at least one digit every two steps; more rapid expansion is typically correlated with increased randomness. For most initial n, the overall pattern obtained quickly becomes repetitive, with an effective period of 4 steps. But with the initial condition n = 512, no repetition occurs for at least a million steps, at which point n has 568418 base 2 digits. The plot below shows the lengths of the successive regions of regularity visible on the right-hand edge of the picture on page 126 over the course of the first million steps.

![](Images/_page_920_Figure_12.jpeg)

If one works directly with a digit sequence of fixed length, dropping any carries on the left, then a repetitive pattern is typically obtained fairly quickly. If one always includes one new digit on the left at every step, even when it is 0, then a rather random pattern is produced.

- History. Systems similar to the one described here (though often in base 10) were mentioned in the recreational mathematics literature at least as long ago as 1939. A few small computer experiments were done around 1970, but no largescale investigations seem to have previously been made.
- Digit reversal. Sequences of the form

Table[FromDigits[

Reverse[IntegerDigits[n, k, m]], k], {n, 0, k<sup>m</sup> - 1}]

shown below appear in algorithms such as the fast Fourier transform and, with different values of k for different coordinates, in certain quasi-Monte Carlo schemes. (See pages 1073 and 1085.) Such sequences were considered by Johannes van der Corput in 1935.

![](Images/_page_920_Picture_20.jpeg)

![](Images/_page_920_Picture_21.jpeg)

![](Images/_page_920_Picture_22.jpeg)

■ Iterated run-length encoding. Starting say with {1} consider repeatedly replacing list by (see page 1070)

Flatten[Map[{Length[#], First[#]} &, Split[list]]]

The resulting sequences contain only the numbers 1, 2 and 3, but otherwise at first appear fairly random. However, as noticed by John Conway around 1986, the sequences can actually be obtained by a neighbor-independent substitution system, acting on 92 subsequences, with rules such as  $\{3,\ 1,\ 1,\ 3,\ 3,\ 2,\ 2,\ 1,\ 1,\ 3\} \to \{\{1,\ 3,\ 2\},\ \{1,\ 2,\ 3,\ 2,\ 2,\ 2,\ 1,\ 1,\ 3\}\}.$ 

The system thus in the end produces patterns that are purely nested, though formed from rather complicated elements. The length of the sequence at the  $n^{th}$  step grows like  $\lambda^n$ , where  $\lambda \simeq 1.3$  is the root of a degree 71 polynomial, corresponding to the largest eigenvalue of the transition matrix for the substitution system.

■ Digit count sequences. Starting say with {1} repeatedly replace list by

Join[list, IntegerDigits[Apply[Plus, list], 2]]

The resulting sequences grow in length roughly like  $n \log[n]$ . The picture below shows the fluctuations around m/2 of the cumulative number of 1's up to position m in the sequence obtained at step 1000. A definite nested structure similar to picture (c) on page 130 is evident.

![](Images/_page_920_Figure_30.jpeg)

■ Iterated bitwise operations. The pictures below show digit sequences generated by repeatedly applying combinations of bitwise and arithmetic operations. The first example corresponds to elementary cellular automaton rule 60. Note that any cellular automaton rule can be reproduced by some appropriate combination of bitwise and arithmetic operations.

![](Images/_page_921_Picture_3.jpeg)

![](Images/_page_921_Picture_4.jpeg)

![](Images/_page_921_Picture_5.jpeg)

![](Images/_page_921_Picture_6.jpeg)

![](Images/_page_921_Picture_7.jpeg)

#### **Recursive Sequences**

■ Page 128 · Recurrence relations. The rules for the sequences given here all have the form of linear recurrence relations. An explicit formula for the  $n^{th}$  term in each sequence can be found by solving the algebraic equation obtained by applying the replacement  $f[m_{-}] \rightarrow t^{m}$  to the recurrence relation. (In case (e), for example, the equation is  $t^n = -t^{n-1} + t^{n-2}$ .) Note that (d) is the Fibonacci sequence, discussed on page 890.

Standard examples of recursive sequences that do not come from linear recurrence relations include factorial

$$f[1] = 1; f[n_{-}] := n f[n - 1]$$

and Ackermann functions (see below). These two sequences both grow rapidly, but smoothly.

A recurrence relation like

$$f[0] = x; f[n_{-}] := a f[n-1] (1-f[n-1])$$

corresponds to an iterated map of the kind discussed on page 920, and has complicated behavior for many rational *x*.

■ Ackermann functions. A convenient example is

$$f[1, n_{-}] := n; f[m_{-}, 1] := f[m - 1, 2]$$

$$f[m_-, n_-] := f[m-1, f[m, n-1] + 1]$$

The original function constructed by Wilhelm Ackermann around 1926 is essentially

$$f[1, x_-, y_-] := x + y;$$
  
 $f[m_-, x_-, y_-] := Nest[f[m-1, x, #] &, x, y-1]$ 

$$f[m_-, x_-, y_-] :=$$

Nest[Function[z, Nest[#1, x, z - 1]] &, x + # &, m - 1][y] For successive *m* (following the so-called Grzegorczyk hierarchy) this is x + y, xy,  $x^y$ ,  $Nest[x^\# \&, 1, y]$ , .... f[4, x, y]can also be written Array[x &, y, 1, Power] and is sometimes called tetration and denoted  $x \uparrow \uparrow y$ .

■ Page 129 · Computation of sequences. It is straightforward to compute the various sequences given here, but to avoid a rapid increase in computer time, it is essential to store all the values of f[n] that one has already computed, rather than recomputing them every time they are needed. This is achieved for example by the definitions

$$f[n_{-}] := f[n] = f[n-f[n-1]] + f[n-f[n-2]]$$
  
 $f[1] = f[2] = 1$ 

The question of which recursive definitions yield meaningful sequences can depend on the details of how the rules are applied. For example, f[-1] may occur, but if the complete expression is f[-1]-f[-1], then the actual value of f[-1] is irrelevant. The default form of evaluation for recursive functions implemented by all standard computer languages (including Mathematica) is the so-called leftmost innermost scheme, which attempts to find explicit values for each f[k] that occurs first, and will therefore never notice if f[k] in fact occurs only in the combination f[k] - f[k]. (The SMP system that I built around 1980 allowed different schemes—but they rarely seemed useful and were difficult to understand.)

■ Page 131 · Properties of sequences. Sequence (d) is given by

```
f[n_{-}] := (n + g[IntegerDigits[n, 2]])/2
```

$$g[\{(1)..\}] = 1; g[\{1, (0)..\}] = 0$$

 $g[\{1, s_{-}\}] := 1 + g[IntegerDigits[FromDigits[\{s\}, 2] + 1, 2]]$ 

The list of elements in the sequence up to value m is given by  $Flatten[Table[n, {IntegerExponent[n, 2] + 1}], {n, m}]]$ 

The differences between the first  $2(2^k - 1)$  of these elements is Nest[Replace[#,  $\{x_{--}\} \rightarrow \{x, 1, x, 0\}] \&, \{\}, k]$ 

The largest n for which f[n] = m is given by 2m+1-DigitCount[m, 2, 1] or IntegerExponent[(2m)!, 2]+1 (this satisfies h[1] = 2;  $h[m_{-}] := h[Floor[m/2]] + m$ ).

The form of sequence (c) is similar to that obtained from concatenation numbers on page 913. Hump *m* in the picture of sequence (c) shown is given by

```
FoldList[Plus, 0, Flatten[Nest[Delete[NestList[Rest, #
Length[#] - 1], 2] &, Append[Table[1, {m}], 0], m]] - 1/2]
```

The first  $2^m$  elements in the sequence can also be generated in terms of reordered base 2 digit sequences by

```
FoldList[Plus, 1, Map[Last[Last[#]] &,
    Sort[Table[({Length[#], Apply[Plus, #], 1-#} &)[
           IntegerDigits[i, 2]], {i, 2<sup>m</sup>}]]]]
```

Note that the positive and negative fluctuations in sequence (f) are not completely random: although the probability for individual fluctuations in each direction seems to be the same, the probability for two positive fluctuations in a row is smaller than for two negative fluctuations in a row.

In the sequences discussed here,  $f[n_{-}]$  always has the form f[p[n]] + f[q[n]]. The plots at the top of the next page show p[n] and q[n] as a function of n.

![](Images/_page_922_Figure_2.jpeg)

The process of evaluating f[n] for a particular n can be thought of as yielding a tree where each node is a particular f[k] which has two successors, f[p[k]] and f[q[k]]. The distinct nodes reached starting from f[12] for sequence (f) are then for example {{12}, {3, 7}, {1, 2, 4}, {1, 2}, {1}}. The total lengths of these chains (corresponding to the depth of the evaluation tree) seem to increase roughly like Log[n] for all the rules on this page. For the Fibonacci sequence, it is instead n-1. The maximum number of distinct nodes at any level in the tree has large fluctuations but its peaks seem to increase roughly linearly for all the rules on this page (in the Fibonacci case it is Ceiling[n/2]).

- History. The idea of sequences in which later terms are deduced from earlier ones existed in antiquity, notably in the method of induction and in various approximation schemes (compare page 918). The Fibonacci sequence also appears to have arisen in antiquity (see page 890). A fairly clear idea of integer recurrence relations has existed since about the 1600s, but until very recently mainstream mathematics has almost never investigated them. In the late 1800s and early 1900s issues about the foundations of mathematics (see note below) led to the formal definition of so-called recursive functions. But almost without exception the emphasis was on studying what such functions could in principle do, not on looking at the actual behavior of particular ones. And indeed, despite their simple forms, recursive sequences of the kind I discuss here do not for the most part ever appear to have been studied before-although sequence (c) was mentioned in lectures by John Conway around 1988, and the first 17 terms of sequence (e) were given by Douglas Hofstadter in 1979.
- **Primitive recursive functions.** As part of trying to formalize foundations of arithmetic Richard Dedekind began around 1888 to discuss possible functions that could be defined using recursion (induction). By the 1920s there had then emerged a definite notion of primitive recursive functions. The proof of Gödel's Theorem in 1931 made use of both primitive and general recursive functions—and by the mid-1930s emphasis had shifted to discussion of general recursive functions.

Primitive recursive functions are defined to deal with nonnegative integers and to be set up by combining the basic functions z = 0 & (zero), s = # + 1 & (successor) and p[i] := Slot[i] & (projection) using the operations of composition and primitive recursion

```
f[0, y\_\_Integer] := g[y]
  f[x_{integer}, y_{integer}] := h[f[x - 1, y], x - 1, y]
Plus and Times can then for example be defined as
  plus[0, y_{-}] = y; plus[x_{-}, y_{-}] := s[plus[x - 1, y]]
  times[0, y_{-}] = 0; times[x_{-}, y_{-}] := plus[times[x - 1, y], y]
```

Most familiar integer mathematical functions also turn out to be primitive recursive—examples being Power, Mod, Binomial, GCD and Prime. And indeed in the early 1900s it was thought that perhaps any function that could reasonably be computed would be primitive recursive (see page 1125). But the construction in the late 1920s of the Ackermann function f[m, x, y] discussed above showed that this was not correct. For any primitive recursive function can grow for large x at most like f[m, x, x] with fixed m. Yet f[x, x, x] will always eventually grow faster than this-demonstrating that the whole Ackermann function cannot be primitive recursive. (See page 1162.)

A crucial feature of primitive recursive functions is that the number of steps they take to evaluate is always limited, and can always in effect be determined in advance, since the basic operation of primitive recursion can be unwound simply as

```
f[x_{-}, y_{--}] := Fold[h[#1, #2, y] \&, g[y], Range[0, x-1]]
And what this means is that any computation that for
example fundamentally involves a search that might not
terminate cannot be implemented by a primitive recursive
function. General recursive functions, however, also allow
```

 $\mu[f_{-}] = NestWhile[\# + 1 \&, 0, Function[n, f[n, \##1] \neq 0]] \&$ which can perform unbounded searches. (Ordinary primitive recursive functions are always total functions, that give definite values for every possible input. But general recursive functions can be partial functions, that do not terminate for some inputs.) As discussed on page 1121 it turns out that general recursive functions are universal, so that they can be used to represent any possible computable function. (Note that any general recursive function can be expressed in the form  $c[f, \mu[g]]$  where f and g are primitive recursive.)

In enumerating recursive functions it is convenient to use symbolic definitions for composition and primitive recursion

```
c[g_{h}] = Apply[g, Through[h][##]] &
  r[g_{-}, h_{-}] =
    If[#1 == 0, g[##2], h[#0[#1 - 1, ##2], #1 - 1, ##2]] &
where the more efficient unwound form is
   r[g_{, h_{}}] = Fold[Function[\{u, v\}, h[u, v, ##2]],
                                 g[##2], Range[0, # - 1]] &
And in terms of these, for example, plus = r[p[1], s].
```

The total number of recursive functions grows roughly exponentially in the size (*LeafCount*) of such expressions, and roughly linearly in the number of arguments.

Most randomly selected primitive recursive functions show very simple behavior—either constant or linearly increasing when fed successive integers as arguments. The smallest examples that show other behavior are:

- r[z, r[s, s]], which is 1/2 # (# + 1) &, with quadratic growth
- r[z, r[s, c[s, s]]], which is  $2^{\#+1}$  # 2 &, with exponential growth
- r[z, r[s, p[2]]], which is 2^Ceiling[Log[2, # +2]] # 2 &, which shows very simple nesting
- r[z, r[c[s, z], z]], which is Mod[#, 2] &, with repetitive behavior
- r[z, r[s, r[s, s]]] which is
  Fold[1/2#1(#1+1)+#2 &, 0, Range[#]] &, growing like
  2<sup>2\*</sup>

r[s, r[s, r[s, p[2]]]] is the first function to show significantly more complex behavior, and indeed as the picture below indicates, it already shows remarkable randomness. From its definition, the function can be written as

Fold[Fold[2^Ceiling[Log[2, Ceiling[(#1+2)/(#2+2)]]] (#2+2)-2-#1 &, #2, Range[#1]] &, 0, Range[#]] & Its first zeros are at {4, 126, 813, 966, 1166, 1177, 1666, 1897}.

![](Images/_page_923_Figure_10.jpeg)

Each zero is immediately followed by a maximum equal to x, and as picture below shows, values tend to accumulate for example on lines of the form  $\pm x/2^u \pm (2m + 1)2^v$ .

![](Images/_page_923_Figure_12.jpeg)

Note that functions of the form Nest[r[c[s, z], #] &, c[s, s], n] are given in terms of the original Ackermann function in the note above by f[n + 1, 2, # + 1] - 1 &.

Before the example above one might have thought that primitive recursive functions would always have to show rather simple behavior. But already an immediate counterexample is *Prime*. And it turns out that if they never sample values below *f*[0] the functions in the main text are also all primitive recursive. (Their definitions have a

primitive recursive structure, but to operate correctly they must be given integers that are non-negative.)

Among functions with simple explicit definitions, essentially the only examples known fundamentally to be not primitive recursive are ones closely related to the Ackermann function. But given an enumeration of primitive recursive functions (say ordered first by LeafCount, then with Sort) in which the  $m^{th}$  function is w[m] diagonalization (see page 1128) yields the function w[x][x] shown below which cannot be primitive recursive. It is inevitable that the function shown must eventually grow faster than any primitive recursive function (at x = 356 its value is 63190, while at x = 1464 it is 1073844). But by reducing the results modulo 2 one gets a function that does not grow—and has seemingly quite random behavior—yet is presumably again not primitive recursive.

![](Images/_page_923_Figure_17.jpeg)

(Note that multiple arguments to a recursive function can be encoded as a single argument using functions like the  $\beta$  of page 1120—though the irregularity of such functions tends to make it difficult then to tell what is going on in the underlying recursive function.)

■ Ulam sequences. Slightly more complicated definitions in terms of numbers yield all sorts of sequences with very complicated forms. An example suggested by Stanislaw Ulam around 1960 (in a peculiar attempt to get a 1D analog of a 2D cellular automaton; see pages 877 and 928) starts with (1, 2), then successively appends the smallest number that is the sum of two previous numbers in just one way, yielding

{1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, ...} With this initial condition, the sequence is known to go on forever. At least up to  $n = 10^6$  terms, it increases roughly like  $13.5 \, n$ , but as shown below the fluctuations seem random.

![](Images/_page_923_Figure_21.jpeg)

#### The Sequence of Primes

■ **History of primes.** Whether the Babylonians had the notion of primes is not clear, but before 400 BC the Pythagoreans had introduced primes as numbers of objects that can be

arranged only in a single line, and not in any other rectangular array. Around 300 BC Euclid discussed various properties of primes in his Elements, giving for example a proof that there are an infinity of primes. The sieve of Eratosthenes was described in 200 BC, apparently following ideas of Plato. Then starting in the early 1600s various methods for factoring were developed, and conjectures about formulas for primes were made. Pierre Fermat suggested  $2^{2^n} + 1$  as a source for primes and Marin Mersenne 2 ^ Prime[n] - 1 (see page 911). In 1752 Christian Goldbach showed that no ordinary polynomial could generate only primes, though as pointed out by Leonhard Euler  $n^2 - n + 41$  does so for n < 40. (With If or Floor included there are at least complicated cases known where polynomial-like formulas can be set up whose evaluation corresponds to explicit prime-generating procedures—see page 1162.) Starting around 1800 extensive work was done on analytical approximations to the distribution of primes (see below). There continued to be slow progress in finding specific large primes; 231 - 1 was found prime around 1750 and  $2^{127}$  - 1 in 1876.  $(2^{2^5} + 1)$  was found composite in 1732, as have now all  $2^{2^n} + 1$  for  $n \le 32$ .) Then starting in the 1950s with the use of electronic computers many new large primes were found. The number of digits in the largest known prime has historically increased roughly exponentially with time over the past two decades, with a prime of over 4 million digits (213466917-1) now being known (see page 911).

- Page 132 · Finding primes. The sieve of Eratosthenes shown in the picture is an appropriate procedure if one wants to find every prime, but testing whether an individual number is prime can be done much more efficiently, as in PrimeQ[n] in Mathematica, for example by using Fermat's so-called little theorem that  $Mod[a^{p-1}, p] == 1$ whenever p is prime. The  $n^{th}$  prime Prime[n] can also be computed fairly efficiently using ideas from analytic number theory (see below).
- Decimation systems. A somewhat similar system starts with a line of cells, then at each step removes every kth cell that remains, as in the pictures below. The number of steps for which a cell at position n will survive can be computed as

 $Module[{q = n + k - 1, s = 1},$ While  $[Mod[q, k] \neq 0, q = Ceiling[(k-1)q/k]; s++]; s]$ 

If a cell is going to survive for s steps, then it turns out that this can be determined by looking at the last s digits in the base k representation of its position. For k = 2, a cell survives for s steps if these digits are all 0 (so that s==IntegerExponent[n, k]). But for k > 2, no such simple characterization appears to exist.

![](Images/_page_924_Figure_7.jpeg)

If the cells are arranged on a circle of size n, the question of which cell is removed last is the so-called Josephus problem. The solution is Fold[Mod[#1+k, #2, 1] &, 0, Range[n]], or FromDigits[RotateLeft[IntegerDigits[n, 2]], 2] for k = 2.

■ Page 132 · Divisors. The picture below shows as black squares the divisors of each successive number (which correspond to the gray dots in the picture in the main text). Primes have divisors 1 and n only. (See also pages 902 and 747.)

![](Images/_page_924_Picture_10.jpeg)

![](Images/_page_924_Picture_11.jpeg)

■ Page 133 · Results about primes. Prime[n] is approximately by nLog[n] + nLog[Log[n]]. (Prime[10<sup>9</sup>] is 22,801,763,489 while the approximation gives  $2.38 \times 10^{10}$ .) A first approximation to PrimePi[n] is n/Log[n]. A somewhat better approximation is LogIntegral[n], equal to Integrate[1/Log[t], {t, 2, n}]. This was found empirically by Carl Friedrich Gauss in 1792, based on looking at a table of primes. (PrimePi[109] is 50,847,534 while LogIntegral[109] is about 50,849,235.) A still better approximation is obtained by subtracting  $Sum[LogIntegral[n^{r_i}], \{i, -\infty, \infty\}]$  where the  $r_i$  are the complex zeros of the Riemann zeta function Zeta[s], discussed on page 918. According to the Riemann Hypothesis, the difference between PrimePi[n] and LogIntegral[n] is of order  $\sqrt{n}$  Log[n]. More refined analytical estimates of PrimePi[n] are good enough that they are used by Mathematica to compute Prime[n] for large n.

It is known that the ratio of the number of primes of the form 4k+1 and 4k+3 asymptotically approaches 1, but almost nothing has been proved about the fluctuations.

The gap between successive primes Prime[n] - Prime[n-1] is thought to grow on average at most like Log[Prime[n]]<sup>2</sup>. It is known that for sufficiently large n a gap of any size must exist. It is believed but not proved that there are an infinite number of "twin primes" with a gap of exactly 2.

■ History of number theory. Most areas of mathematics go from inception to maturity within at most a century. But in number theory there are questions that were formulated more than 2000 years ago (such as whether any odd perfect numbers exist) that have still not been answered. Of the principles that have been established in number theory, a great many were first revealed by explicit experiments. From its inception in classical times, through its development in the 1600s to 1800s, number theory was largely separate from other fields of mathematics. But starting at the end of the 1800s, increasing connections were found to other areas of both continuous and discrete mathematics. And through these connections, sophisticated proofs of such results as Fermat's Last Theorem-open for 350 years—have been constructed. Long considered a rather esoteric branch of mathematics, number theory has in recent years grown in practical importance through its use in areas such as coding theory, cryptography and statistical mechanics. Properties of numbers and certain elementary aspects of number theory have also always played a central role in amateur and recreational mathematics. And as this chapter indicates, number theory can also be used to provide many examples of the basic phenomena discussed in this book.

- Page 134 · Tables of primes. No explicit tables of primes appear to have survived from antiquity, but it seems likely that all primes up to somewhere between 5000 and 10000 were known. (In 348 BC, Plato mentioned divisors of 5040, and by 100 AD there is evidence that the fifth perfect number was known, requiring the knowledge that 8191 is prime.) In 1202 Leonardo Fibonacci explicitly gave as an example a list of primes up to 100. And by the mid-1600s there were printed tables of primes up to 100,000, containing as much data as in plots (c) and (d). In the 1700s and 1800s many tables of number factorizations were constructed; by the 1770s there was a table up to 2 million, and by the 1860s up to 100 million. A table of primes up to a trillion could now be generated fairly easily with current computer technologythough for most purposes computation of specific primes is more useful.
- Page 134 · Numbers of primes. The fact that curve (c) must cross the axis was proved by John Littlewood in 1914, and it is known to have at least one crossing below  $10^{317}$ . Somewhat related to the curves shown here is the function MoebiusMu[n], equal to 0 if n has a repeated prime factor and otherwise  $(-1)^Length[FactorInteger[n]]$ . The quantity  $FoldList[Plus, 0, Table[MoebiusMu[i], \{i, n\}]]$  behaves very much like a random walk. The so-called Mertens Conjecture from 1897 stated that the magnitude of this quantity is less than  $\sqrt{n}$ . But this was disproved in 1983, although the necessary n is not known explicitly.

- **Relative primes.** A single number is prime if it has no nontrivial factors. Two numbers are said to be relatively prime if they share no non-trivial factors. The pattern formed by numbers with this property is shown on page 613.
- **Page 135 · Properties.** (a) The number of divisors of n is given by DivisorSigma[0, n], equal to Length[DivisorS[n]]. For large n this number is on average of order Log[n] + 2 EulerGamma 1.
- (b) (Aliquot sums) The quantity that is plotted is DivisorSigma[1, n] 2n, equal to Apply[Plus, Divisors[n]] 2n. This quantity was considered of great significance in antiquity, particularly by the Pythagoreans. Numbers were known as abundant, deficient or perfect depending on whether the quantity was positive, negative or zero. (See notes on perfect numbers below.) For large n, DivisorSigma[1, n] is known to grow at most like Log[Log[n]]nExp[EulerGamma], and on average like  $\pi^2 n/6$  (see page 1093). As discovered by Srinivasa Ramanujan in 1918 its fluctuations (see below) can be obtained from the formula

1/6  $\pi^2$  n Sum[Apply[Plus, Cos[2  $\pi$  n Select[
Range[s], GCD[s, #] == 1 &]/s]]/s², {s,  $\infty$ }]

(c) Squares are taken to be of positive or negative integers, or zero. The number of ways of expressing an integer n as the sum of two such squares is  $4Apply[Plus, Im[i^Divisors[n]]]$ . This is nonzero when all prime factors of n of the form 4k + 3 appear with even exponents. There is no known simple formula for the number of ways of expressing an integer as a sum of three squares, although part of the condition in the main text for integers to be expressible in this way was established by René Descartes in 1638 and the rest by Adrien Legendre in 1798. Note that the total number of integers less than n which can be expressed as a sum of three squares increases roughly like 5n/6, with fluctuations related to IntegerDigits[n, 4]. It is known that the directions of all vectors  $\{x, y, z\}$  for which  $x^2 + y^2 + z^2 = n$  are uniformly distributed in the limit of large n.

The total number of ways that integers less than n can be expressed as a sum of d squares is equal to the number of integer lattice points that lie inside a sphere of radius  $\sqrt{n}$  in d-dimensional space. For d = 2, this approaches  $\pi n$  for large n, with an error of order  $n^c$ , where  $1/4 < c \le 0.315$ .

(d) All numbers n can be expressed as the sum of four squares, in exactly  $8 \text{ Apply}[Plus, Select[Divisors[n], Mod[#, 4] $\neq 0 \&]]}$  ways, as established by Carl Jacobi in 1829. Edward Waring stated in 1770 that any number can be expressed as a sum of at most 9 cubes and 19 fourth powers. Seven cubes appear to suffice for all but 17 numbers, the last of which is 455; four

cubes may suffice for all but 113936676 numbers, the last of which is 7373170279850. (See also page 1166.)

(e) Goldbach's Conjecture has been verified for all even numbers up to  $4 \times 10^{14}$ . In 1973 it was proved that any even number can be written as the sum of a prime and a number that has at most two prime factors, not necessarily distinct. The number of ways of writing an integer n as a sum of two primes can be calculated explicitly as Length[Select[n-Table[Prime[i], {i, PrimePi[n]}], PrimeQ]]. This quantity was conjectured by G. H. Hardy and John

2 n Apply[Times, Map[(# - 1)/(# - 2) &, Map[First, Rest[FactorInteger[n]]]]]/Log[n]<sup>2</sup>

Littlewood in 1922 to be proportional to

It was proved in 1937 by Ivan Vinogradov that any large odd integer can be expressed as a sum of three primes.

- **Trapezoidal primes.** If one lays out n objects in an  $a \times b$ rectangular array, then n is prime if either a or b must be 1. Following the Pythagorean idea of figurate numbers one can instead consider laying out objects in an array of b rows, containing successively a, a-1, ... objects. It turns out all numbers except powers of 2 can be represented this way.
- Other integer functions. IntegerExponent[n, k] gives nested behavior as for decimation systems on page 909, while MultiplicativeOrder[k, n] and EulerPhi[n] vield more complicated behavior, as shown on pages 257 and 1093.
- Spectra. The pictures below show frequency spectra obtained from the sequences in the main text. Some regularity is evident, and in cases (a) and (b) it can be understood from trigonometric sum formulas of Ramanujan discussed above (see also pages 586 and 1081).

![](Images/_page_926_Figure_9.jpeg)

■ Perfect numbers. Perfect numbers with the property that Apply[Plus, Divisors[n]] == 2n have been studied since at least the time of Pythagoras around 500 BC. The first few perfect numbers are {6, 28, 496, 8128, 33550336} (a total of 39 are currently known). It was shown by Euclid in 300 BC that  $2^{n-1}(2^n-1)$  is a perfect number whenever  $2^n-1$  is prime. Leonhard Euler then proved around 1780 that every even perfect number must have this form. The values of n for the known Mersenne primes  $2^n$  – 1 are shown below. These values can be found using the so-called Lucas-Lehmer test Nest[ $Mod[\#^2 - 2, 2^n - 1] \&, 4, n - 2] == 0$ , and in all cases n itself must be prime.

![](Images/_page_926_Figure_11.jpeg)

Whether any odd perfect numbers exist is probably the single oldest unsolved problem in mathematics. It is known that any odd perfect number must be greater than  $10^{300}$ , must have a factor of at least  $10^6$ , and must be less than  $4^{4^s}$  if it has only s prime factors. Looking at curve (b) on page 135, however, it does not seem inconceivable that an odd perfect number could exist. For odd n up to 500 million the only values near 0 that appear in the curve are {-6, -5, -4, -2, -1, 6, 18, 26, 30, 36}, with, for example, the first 6 occurring at n = 8925 and last 18 occurring at n = 159030135. Various generalizations of perfect numbers have been considered, for example IntegerQ[DivisorSigma[1, n]/n] (pluperfect) or Abs[DivisorSigma[1, n] - 2n] < r (quasiperfect).

■ Iterated aliquot sums. Related to case (b) above is a system which repeats the replacement  $n \rightarrow Apply[Plus, Divisors[n]] - n$ or equivalently  $n \rightarrow DivisorSigma[1, n] - n$ . The fixed points of this procedure are the perfect numbers (see above). Other numbers usually evolve to perfect numbers, or to short repetitive sequences of numbers. But if one starts, for example, with the number 276, then the picture below shows the number of base 10 digits in the value obtained at each step.

![](Images/_page_926_Figure_14.jpeg)

After 500 steps, the value is the 53-digit number 39448887705043893375102470161238803295318090278129552 The question of whether such values can increase forever was considered by Eugène Catalan in 1887, and has remained unresolved since.

#### **Mathematical Constants**

■ Page 137 · Digits of pi. The digits of  $\pi$  shown here can be obtained in less than a second from Mathematica on a typical current computer using  $N[\pi, 7000]$ . Historically, the number of decimal digits of  $\pi$  that have been computed is roughly as follows: 2000 BC (Babylonians, Egyptians): 2 digits; 200 BC (Archimedes): 5 digits; 1430 AD: 14 digits; 1610: 35 digits; 1706: 100 digits; 1844: 200 digits; 1855: 500 digits; 1949 (ENIAC computer): 2037 digits; 1961: 100,000 digits (IBM 7090); 1973: 1 million; 1983: 16 million; 1989: 1 billion; 1997: 50 billion; 1999: 206 billion. In the first 200 billion digits, the frequencies of 0 through 9 differ from 20 billion by

```
{30841, -85289, 136978, 69393, -78309, -82947, -118485, -32406, 291044, -130820}
```

An early approximation to  $\pi$  was

 $4 Sum[(-1)^{k}/(2k+1), \{k, 0, m\}]$ 

30 digits were obtained with

2 Apply[Times, 2/Rest[NestList[Sqrt[2 + #] &, 0, m]]]An efficient way to compute  $\pi$  to n digits of precision is

```
(\#[2]]^2/\#[3]] &)[NestWhile[Apply[Function[{a, b, c, d}, {(a+b)/2, Sqrt[ab], c-d(a-b)^2, 2d}], #] &, {1, 1/Sqrt[N[2, n]], 1/4, 1/4}, #[1]] \#[2] &]]
```

This requires about Log[2, n] steps, or a total of roughly  $nLog[n]^2$  operations (see page 1134).

■ Computing  $n^{th}$  digits directly. Most methods for computing mathematical constants progressively generate each additional digit. But following work by Simon Plouffe and others in 1995 it became clear that it is sometimes possible to generate, at least with overwhelming probability, the  $n^{th}$  digit without explicitly finding previous ones. As an example, the  $n^{th}$  digit of Log[2] in base 2 is formally given by  $Round[FractionalPart[2^n Sum[2^{-k}/k, \{k, \infty\}]]]$ . And in practice the  $n^{th}$  digit can be found just by computing slightly over n terms of the sum, according to

```
Round[FractionalPart[

Sum[FractionalPart[PowerMod[2, n-k, k]/k], \{k, n\}] + Sum[2^{n-k}/k, \{k, n+1, n+d\}]]
```

where several values of d can be tried to check that the result does not change. (Note that with finite-precision arithmetic, some exponentially small probability exists that truncation of numbers will lead to incorrect results.) The same basic approach as for Log[2] can be used to obtain base 16 digits in  $\pi$  from the following formula for  $\pi$ :

```
Sum[16<sup>-k</sup> (4/(8 k + 1) - 2/(8 k + 4) -
1/(8 k + 5) - 1/(8 k + 6)), {k, 0, ∞}]
```

A similar approach can also be used for many other constants that can be viewed as related to values of *PolyLog*.

![](Images/_page_927_Figure_14.jpeg)

■ **Page 139 · Rational numbers.** The pictures above show the base 2 digit sequences of numbers m/n for successive m.

The digits of 1/n in base b repeat with period

MultiplicativeOrder[b, FixedPoint[#/GCD[#, b] &, n]]

which is equal to MultiplicativeOrder[b, n] for prime n, and is

which is equal to MultiplicativeOrder[b, n] for prime n, and is at most n-1. Each repeating block of digits typically seems quite random, and has properties such as all possible subblocks of digits up to a certain length appearing (see page 1084).

■ Page 139 · Digit sequence properties. Empirical evidence for the randomness of the digit sequences of  $\sqrt{n}$ ,  $\pi$ , etc. has been accumulating since early computer experiments in the 1940s. The evidence is based on applying various standard statistical tests of randomness, and remains somewhat haphazard. (Already in 1888 John Venn had noted for example that the first 707 digits of  $\pi$  lead to an apparently typical 2D random walk.) (See page 1089.)

The fact that  $\sqrt{2}$  is not a rational number was discovered by the Pythagoreans. Numbers that arise as solutions of polynomial equations are called algebraic; those that do not are called transcendental. e and  $\pi$  were proved to be transcendental in 1873 and 1882 respectively. It is known that Exp[n] and Log[n] for whole numbers n (except 0 and 1 respectively) are transcendental. It is also known for example that Gamma[1/3] and Gamma[1/3] are transcendental. It is not known for example whether Gamma is even irrational.

A number is said to be "normal" in a particular base if every digit and every block of digits of any length occur with equal frequency. Note that the fact that a number is normal in one base does not imply anything about its normality in another base (unless the bases are related for example by both being powers of 2). Despite empirical evidence, no number expressed just in terms of standard mathematical functions has ever been rigorously proved to be normal. It has nevertheless been known since the work of Emile Borel in 1909 that numbers picked randomly on the basis of their value are almost always normal. And indeed with explicit constructions in terms of digits, it is quite straightforward to get numbers that are normal. An example of this is the number 0.1234567891011121314... obtained by concatenating the digits of successive integers in base 10 (see below). This number was discussed by David Champernowne in 1933, and is known to be transcendental. A few other results are also known. One based on gradual extension of work by Richard Stoneham from 1971 is that numbers of the form  $Sum[1/(p^n b^{p^n}), \{n, \infty\}]$  for prime p > 2 are normal in base b (for GCD[b, p] == 1), and are transcendental.

■ **Page 141 · Square roots.** A standard way to compute  $\sqrt{n}$  is Newton's method (actually used already in 2000 BC by the Babylonians), in which one takes an estimate of the value x and then successively applies the rule  $x \to 1/2(x + n/x)$ . After t steps, this method yields a result accurate to about  $t^2$  digits.

Another approach to computing square roots is based on the fact that the ratio of successive terms in for example the sequence f[i] = 2f[i-1] + f[i-2] with f[1] = f[2] = 1 tends to  $1 + \sqrt{2}$ . This method yields about 2.5 t base 2 digits after t steps.

The method of computing square roots shown in the main text is less efficient (it computes t digits in t steps), but illustrates more of the mechanisms involved. The basic idea is at every step t to maintain the relation  $s^2 + 4r = 4^t n$ , keeping *r* as small as possible so as to make  $s \le 2^t \sqrt{n} < s + 4$ . Note that the method works not only for integers, but for any rational number *n* for which  $1 \le n < 4$ .

■ Nested digit sequences. The number obtained from the substitution system  $\{1 \rightarrow \{1, 0\}, 0 \rightarrow \{0, 1\}\}$  is approximately 0.587545966 in base 10. It is certainly conceivable that a quantity such as Feigenbaum's constant (approximately 4.6692016091) could have a digit sequence with this kind of nested structure.

From the result on page 890, the number whose digits are from  $\{1 \rightarrow \{1, 0\}, 0 \rightarrow \{1\}\}$  is given  $Sum[2^{(-Floor[n Golden Ratio])}, \{n, \infty\}].$  This number is known to be transcendental. The  $n^{th}$  term in its continued fraction representation turns out to be 2 -Fibonacci[n-2].

The fact that nested digit sequences do not correspond to algebraic numbers follows from work by Alfred van der Poorten and others in the early 1980s. The argument is based on showing that an algebraic function always exists for which the coefficients in its power series correspond to any given nested sequence when reduced modulo some p. (See page 1092.) But then there is a general result that if a particular sequence of power series coefficients can be obtained from an algebraic (but not rational) function modulo a particular p, then it can only be obtained from transcendental functions modulo any other p—or over the integers.

■ Concatenation sequences. One can consider forming sequences by concatenating digits of successive integers in base k, as in Flatten[Table[IntegerDigits[i, k], {i, n}]]. In the limit, such sequences contain with equal frequency all possible blocks of any given length, but as shown on page 597, they exhibit other obvious deviations from randomness. The picture below shows the k = 2 sequence chopped into length 256 blocks.

![](Images/_page_928_Figure_9.jpeg)

Applying FoldList[Plus, 0, 2 list - 1] to the whole sequence yields the pattern shown below.

![](Images/_page_928_Figure_11.jpeg)

The systematic increase is a consequence of the leading 1 in each concatenated sequence. Dropping this 1 yields the pattern below.

![](Images/_page_928_Figure_13.jpeg)

This is similar to picture (c) on page 131, and is a digit-bydigit version of

Note that although the picture above has a nested structure, the original concatenation sequences are not nested, and so cannot be generated by substitution systems. The element at position n in the first sequence discussed above can however be obtained in about Log[n] steps using

```
((IntegerDigits[#3 + Quotient[#1, #2], 2][[
               Mod[#1, #2] + 1]] &)[n - (# - 2) 2^{#-1} - 2, #,
        2^{\#-1}] &)[NestWhile[# + 1 &, 0, (# - 1)2^{\#} + 1 < n &]]
```

where the result of the NestWhile can be expressed as Ceiling[1 + ProductLog[1/2(n-1)Log[2]]/Log[2]]

Following work by Maxim Rytin in the late 1990s about  $k^{n+1}$ digits of a concatenation sequence can be found fairly efficiently from

$$k/(k-1)^2 - (k-1) Sum[k^{(k^3-1)(1+s-s k/l(k-1))} (1/((k-1)(k^s-1)^2) - k/((k-1)(k^{s+1}-1)^2) + 1/(k^{s+1}-1)), \{s, n\}]$$

Concatenation sequences can also be generated by joining together digits from other representations of numbers; the picture below shows results for the Gray code representation from page 901.

![](Images/_page_928_Figure_22.jpeg)

- Specially constructed transcendental numbers. Numbers known to be transcendental include ones whose digit sequences contain 1's only at positions n!, 2<sup>n</sup> or Fibonacci[n]. Concatenation sequences, as well as generalizations formed by concatenating values of polynomials at successive integer points, are also known to yield numbers that are transcendental
- Runs of digits. One can consider any base 2 digit sequence as consisting of successive runs of 0's and 1's, constructed from the list of run lengths by

Fold[Join[#1, Table[1 - Last[#1], {#2}]] &, {0}, list]

This representation is related to so-called surreal numbers (though with the first few digits different). The number with run lengths corresponding to successive integers (so that the  $n^{th}$  digit is Mod[Floor[1/2 + Sqrt[2 n]], 2]) turns out to be  $(1-2^{1/4} EllipticTheta[2, 0, 1/2] + EllipticTheta[3, 0, 1/2])/2$ , and appears at least not to be algebraic.

- Leading digits. Even though in individual numbers generated by simple mathematical procedures all possible digits often appear to occur with equal frequency, leading digits in sequences of numbers typically do not. Instead it is common for a leading digit s in base b to occur with frequency Log[b, (s+1)/s] (so that in base 10 1's occur 30% of the time and 9's 4.5%). This will happen whenever FractionalPart[Log[b, a[n]]] is uniformly distributed, which, as discussed on page 903, is known to be true for sequences such as  $r^n$  (with Log[b, r] irrational),  $n^n$ , n!, Fibonacci[n], but not r n, Prime[n] or Log[n]. A logarithmic law for leading digits is also found in many practical numerical tables, as noted by Simon Newcomb in 1881 and Frank Benford in 1938.
- Page 143 · Continued fractions. The first n terms in the continued fraction representation for a number x can be found from the built-in *Mathematica* function *ContinuedFraction*, or from

Floor[NestList[1/Mod[#, 1] &, x, n-1]]

A rational approximation to the number *x* can be reconstructed from the continued fraction using *FromContinuedFraction* or by

Fold[1/#1+#2 &, Last[list], Rest[Reverse[list]]]

The pictures below show the digit sequences of successive iterates obtained from NestList[1/Mod[#, 1] &, x, n] for several numbers x.

![](Images/_page_929_Picture_11.jpeg)

![](Images/_page_929_Picture_12.jpeg)

![](Images/_page_929_Picture_13.jpeg)

![](Images/_page_929_Picture_14.jpeg)

![](Images/_page_929_Picture_15.jpeg)

![](Images/_page_929_Picture_16.jpeg)

Unlike ordinary digits, the individual terms in a continued fraction can be of any size. In the continued fraction for a randomly chosen number, the probability to find a term of size s is Log[2, (1+1/s)/(1+1/(s+1))], so that the probability of getting a 1 is about 41.50%, and the probability of getting a large term falls off like  $1/s^2$ . If one looks at many terms, then their geometric mean is finite, and approaches Khinchin's constant *Khinchin*  $\approx 2.68545$ .

In the first 1000 terms of the continued fraction for  $\pi$ , there are 412 1's, and the geometric mean is about 2.6656. The largest individual term is the 432th one, which is equal to 20,776. In the first million terms, there are 414,526 1's, the geometric mean is 2.68447, and the largest term is the 453,294th one, which is 12,996,958.

Note that although the usual continued fraction for  $\pi$  looks quite random, modified forms such as

 $4/(Fold[\#2/\#1 + 2 \&, 2, Reverse[Range[1, n, 2]^2]] - 1)$  can be very regular.

The continued fractions for Exp[2/k] and Tan[k/2] have simple forms (as discussed by Leonhard Euler in the mid-1700s); other rational powers of e and tangents do not appear to. The sequence of odd numbers gives the continued fraction for Coth[1]; the sequence of even numbers for Bessell[0, 1]/Bessell[1, 1]. In general, continued fractions whose  $n^{th}$  term is an+b correspond to numbers given by Bessell[b/a, 2/a]/Bessell[b/a + 1, 2/a]. Numbers whose continued fraction terms are polynomials in n can presumably also be represented in terms of suitably generalized hypergeometric functions. (All so-called Hurwitz numbers have continued fractions that consist of interleaved polynomial sequences—a property left unchanged by  $x \to (ax+b)/(cx+d)$ .)

As discovered by Jeffrey Shallit in 1979, numbers of the form  $Sum[1/k^{2^i}, \{i, 0, \infty\}]$  that have nonzero digits in base k only at positions  $2^i$  turn out to have continued fractions with terms of limited size, and with a nested structure that can be found using a substitution system according to

```
{0, k - 1, k + 2, k, k, k - 2, k, k + 2, k - 2, k}[[
Nest[Flatten[{{1, 2}, {3, 4}, {5, 6}, {7, 8}, {5, 6}, {3, 4},
{9, 10}, {7, 8}, {9, 10}, {3, 4}][[#]] &, 1, n]][
```

The continued fractions for square roots are always periodic; for higher roots they never appear to show any significant regularities. The first million terms in the continued fraction for  $2^{1/3}$  contain 414,983 1's, have geometric mean 2.68505, and have largest term 4,156,269 at position 484,709. Terms of any size presumably in the end always occur in continued fractions for higher roots, though this is not known for certain. Fairly large terms are sometimes seen quite early: in  $5^{1/3}$  term 19 is 3052, while in  $Root[10+8\#-\#^3\&,1]$  term 34

is 1,501,790. The presence of a large term indicates a close approximation to a rational number. In a few known cases simple formulas yield numbers that are close but not equal to integers. An example discovered by Srinivasa Ramanujan around 1913 is  $Exp[\pi \sqrt{163}]$ , which is an integer to one part in 1030, and has second continued fraction term 1,333,462,407,511. (This particular example can be understood from the fact that as d increases  $Exp[\pi \sqrt{d}]$  becomes extremely close to -1728 KleinInvariantJ[ $(1 + \sqrt{-d})/2$ ], which turns out to be an integer whenever there is unique factorization of numbers of the form  $a + b\sqrt{-d}$  —and d = 163is the largest of the 9 cases for which this is so.) Other less spectacular examples include  $Exp[\pi] - \pi$  and 163/Log[163].

Numbers with digits given by concatenation sequences in any base k (see note above) seem to have unusual continued fractions, in which most terms are fairly small, but some are extremely large. Thus with k = 2, term 30 is 4,534,532, term 64 is 4,682,854,730,443,938, term 152 is about  $2 \times 10^{34}$  and term 669,468 is about  $2 \times 10^{78902}$ . (For the k = 10 case of the original Champernowne number, even term 18 is already about  $5 \times 10^{165}$ .) The plots below of the numbers of digits in successive terms turn out to have patterns of peaks that show some signs of nesting.

![](Images/_page_930_Picture_4.jpeg)

In analogy to digits in a concatenation sequence the terms in the sequence

Flatten[Table[Rest[ContinuedFraction[a/b]], 
$$\{b, 2, n\}, \{a, b-1\}$$
]]

are known to occur with the same frequencies as they would in the continued fraction representation for a randomly

The pictures below show as a function of n the quantity  $With[{r = FromContinuedFraction[ContinuedFraction[x, n]]},$ -Log[Denominator[r], Abs[x-r]]]

which gives a measure of the closeness of successive rational approximations to x. For any irrational number this quantity cannot be less than 2, while for algebraic irrationals Klaus Roth showed in 1955 that it can only have finitely many peaks that reach above any specified level.

![](Images/_page_930_Figure_10.jpeg)

■ History. Euclid's algorithm states that starting from integers  $\{a, b\}$  iterating  $\{a_{-}, b_{-}\} \Rightarrow If[a > b, \{a - b, b\}, \{a, b - a\}]$ eventually leads to {GCD[a, b], 0}. (See page 1093.) The pictures below show how this works. The numbers of successively smaller squares (corresponding to the numbers of steps in the algorithm) turn out to be exactly ContinuedFraction[a/b].

![](Images/_page_930_Picture_12.jpeg)

It was discovered in antiquity that Euclid's algorithm starting with  $\{x, 1\}$  terminates only when x is rational. In all cases, however, the relationship with continued fractions remains, as below.

![](Images/_page_930_Picture_14.jpeg)

Infinite continued fractions appear to have first been explicitly written down in the mid-1500s, and to have become popular in many problems in number theory by the 1700s. Leonhard Euler studied many continued fractions, while Joseph Lagrange seems to have thought that it might be possible to recognize any algebraic number from its continued fraction. The periodicity of continued fractions for quadratic irrationals was proved by Evariste Galois in 1828. From the late 1800s interest in continued fractions as such waned; it finally increased again in the 1980s in connection with problems in dynamical systems theory.

- Egyptian fractions. Following the ancient Egyptian number system, rational numbers can be represented by sums of reciprocals, as in 3/7 = 1/3 + 1/11 + 1/231. With suitable distinct integers a[n] one can represent any number by  $Sum[1/a[n], \{n, \infty\}]$ . The representation is not unique;  $a[n] = 2^n$ , n(n+1) and (n+1)!/n all yield 1. Simple choices for a[n] yield many standard transcendental numbers: n!: e-1;  $n!^2$ : BesselI[0, 2]-1;  $n2^n$ : Log[2];  $n^2$ :  $\pi^2/6$ ; (2n-1)(2n-3):  $\pi\sqrt{3}/9$ ;  $3-16n+16n^2$ :  $\pi/8$ ; nn!: ExpIntegralEi[1] - EulerGamma. (See also page 902.)
- **Nested radicals.** Given a list of integers acting like digits one can consider representing numbers in the form Fold[Sqrt[#1 + #2] &, 0, Reverse[list]]. A sequence of identical digits d then corresponds to the number (1 + Sqrt[4d + 1])/2. (Note that  $Nest[Sqrt[\# + 2] \&, 0, n] = 2 Cos[\pi/2^{n+1}]$ .) Repeats of a digit block b give numbers that solve  $Fold[#1^2 - #2 \&, x, b] == x$ . It appears that digits 0, 1, 2 are

sufficient to represent uniquely all numbers between 1 and 2. For any number *x* the first *n* digits are given by

Ceiling[NestList[ $(2 - Mod[-#, 1])^2 \&, x^2, n-1]-2$ ]

Even rational numbers such as 3/2 do not yield simple digit sequences. For random x, digits 0, 1, 2 appear to occur with limiting frequencies Sqrt[2+d] - Sqrt[1+d].

■ Digital slope representation. One can approximate a line of any slope h as in the picture below by a sequence of segments on a square grid (such as a digital display device). The vertical distance moved at the  $n^{th}$  horizontal position is Floor[nh] - Floor[(n-1)h], and the sequence obtained from this (which contains only terms Floor[h] and Floor[h] + 1) provides a unique representation for h. As discussed on page 903 this sequence can be generated by applying substitution rules derived from the continued fraction form of h. If h is rational, the sequence is repetitive, while if h is a quadratic irrational, it is nested. Given a sequence of length n, an approximation to h can be reconstructed using

Max[MapIndexed[#1/First[#2] &, FoldList[Plus, First[list], Rest[list]]]]

The fractional part of the result obtained is always an element of the Farey sequence

Union[Flatten[Table[a/b, {b, n}, {a, 0, b}]]] (See also pages 892, 932 and 1084.)

![](Images/_page_931_Figure_9.jpeg)

![](Images/_page_931_Figure_10.jpeg)

![](Images/_page_931_Figure_11.jpeg)

![](Images/_page_931_Figure_12.jpeg)

![](Images/_page_931_Figure_13.jpeg)

- Representations for integers. See page 560.
- Operator representations. Instead of repeatedly applying an operation to a sequence of digits one can consider forming integers (or other numbers) by performing trees of operations on a single constant. Thus, for example, any integer m can be obtained by a tree of m-1 additions of 1's such as (1+(1+1))+1. Another operator that can be used to generate any integer is  $a \circ b = 2a + b - 1$ . In this case 6 is  $(1 \circ (1 \circ 1)) \circ 1$ , and an integer m can be obtained by Tr[1 + IntegerDigits[m, 2]] - 2or at most Log[2, m] applications of o. The operator ka+b-k+1 can be used for any k. It also turns out that BitXor[2a, b] + 1 works, though in this case even for 2 the smallest representation is  $(1 \circ 1) \circ (1 \circ ((1 \circ 1) \circ 1))$ . (For BitOr[2a, b]-1 the number of applications needed is  $With[\{i = IntegerDigits[m, 2]\}, \ Tr[i+1] + i[\![2]\!] \ (1+i[\![3]\!]) - 1].)$ The pictures below show the smallest number of operator applications required for successive integers. With the pair of operators a+b and  $a\times b$  (a case considered in recreational

mathematics for n-ary operators) numbers of the form  $3^s$  have particularly small representations. Note that in all cases the size of the smallest representation must at some level increase like Log[m] (compare pages 1067 and 1070), but there may be some "algorithmically simple" integers that have shorter representations.

![](Images/_page_931_Figure_17.jpeg)

■ Number classification. One can imagine classifying real numbers in terms of what kinds of operations are needed to obtain them from integers. Rational numbers require only division (or solving linear equations), while algebraic numbers require solving polynomial equations. Rather little is known about numbers that require solving transcendental equations—and indeed it can even be undecidable (see page 1138) whether two equations can yield the same number. Starting with integers and then applying arithmetic operations and fractional powers one can readily reproduce all algebraic numbers up to degree 4, but not beyond. The sets of numbers that can be obtained by applying elementary functions like Exp, Log and Sin seem in various ways to be disjoint from algebraic numbers. But if one applies multivariate elliptic or hypergeometric functions it was established in the late 1800s and early 1900s that one can in principle reach any algebraic number. One can also ask what numbers can be generated by integrals (or by solving differential equations). For rational functions f[x], Integrate  $[f[x], \{x, 0, 1\}]$  must always be a linear function of Log and ArcTan applied to algebraic numbers  $(f[x] = 1/(1 + x^2))$  for example yields  $\pi/4$ ). Multiple integrals of rational functions can be more complicated, as in

Integrate[
$$1/(1 + x^2 + y^2)$$
, {x, 0, 1}, {y, 0, 1}] ==   
HypergeometricPFQ[{1/2, 1, 1}, {3/2, 3/2}, 1/9]/6 +   
 $1/2 \pi ArcSinh[1] - Catalan$ 

and presumably often cannot be expressed at all in terms of standard mathematical functions. Integrals of rational functions over regions defined by polynomial inequalities have recently been discussed under the name "periods". Many numbers associated with Zeta and Gamma can readily be generated, though apparently for example e and EulerGamma cannot. One can also consider numbers obtained from infinite sums (or by solving recurrence equations). If f[n] is a rational function,  $Sum[f[n], \{n, \infty\}]$ must just be a linear combination of PolyGamma functions, but again the multivariate case can be much more complicated.

#### **Mathematical Functions**

- Page 145 · Mathematical functions. (See page 1091.) BesselJ[0, x] goes like  $Sin[x]/\sqrt{x}$  for large x while AiryAi[-x]goes like  $Sin[x^{3/2}]/x^{1/4}$ . Other standard mathematical functions that oscillate at large x include JacobiSN and MathieuC. Most hypergeometric-type functions either increase or decrease exponentially for large arguments, though in the directions of Stokes lines in the complex plane they can oscillate sinusoidally. (For AiryAi[x] the Stokes lines are in directions  $(-1)^{(1, 2, 3)/3}$ .
- Lissajous figures. Plotting multiple sine functions each on different coordinate axes yields so-called Lissajous or Bowditch figures, as illustrated below. If the coefficients inside all the sine functions are rational, then going from t = 0 to  $t = 2 \pi Apply[LCM, Map[Denominator, list]]$  yields a closed curve. Irrational ratios of coefficients lead to curves that never close and eventually fill space uniformly.

![](Images/_page_932_Figure_6.jpeg)

- **Page 146 · Two sine functions.** Sin[ax] + Sin[bx] can be rewritten as 2 Sin[1/2(a+b)x] Cos[1/2(a-b)x] (using TrigFactor), implying that the function has two families of equally spaced zeros:  $2 \pi n/(a+b)$  and  $2 \pi (n+1/2)/(b-a)$ .
- **Differential equations.** The function  $Sin[x] + Sin[\sqrt{2} x]$  can be obtained as the solution of the differential equation y''[x] + 2y[x] - Sin[x] == 0 with the initial conditions y[0] == 0, y'[0] == 2.
- Musical chords. In a so-called equal temperament scale the 12 standard musical notes that make up an octave have a progression of frequencies  $2^{n/12}$ . Most schemes for musical tuning use rational approximations to these numbers. Until the past century, and since at least the 1300s, diminished fifth or tritone chords that consist of two notes (such as C and Gb) with frequency ratio  $\sqrt{2}$  have generally been avoided as sounding discordant. (See also page 1079.)
- Page 146 · Three sine functions. All zeros of the function Sin[ax] + Sin[bx] lie on the real axis. But for Sin[ax] + Sin[bx] + Sin[cx], there are usually zeros off the

real axis (even say for a = 1, b = 3/2, c = 5/3), as shown in the pictures below.

![](Images/_page_932_Figure_12.jpeg)

 $Sin[z]+Sin[\sqrt{2} z]+Sin[\sqrt{3} z]$ 

If a, b and c are rational, Sin[ax] + Sin[bx] + Sin[cx] is periodic with period  $2\pi/GCD[a, b, c]$ , and there are a limited number of different spacings between zeros. But in a case like  $Sin[x] + Sin[\sqrt{2} x] + Sin[\sqrt{3} x]$  there is a continuous distribution of spacings between zeros, as shown on a logarithmic scale below. (For  $0 < x < 10^6$  there are a total of 448,494 zeros, with maximum spacing  $\simeq 4.6$  and minimum spacing  $\simeq 0.013$ .)

![](Images/_page_932_Picture_15.jpeg)

![](Images/_page_932_Figure_16.jpeg)

■ Page 147 · Substitution systems. Cos[ax] - Cos[bx] has two families of zeros:  $2\pi n/(a+b)$  and  $2\pi n/(b-a)$ . Assuming b > a > 0, the number of zeros from the second family which appear between the  $n^{th}$  and  $n + 1^{th}$  zero from the first family is (Floor[(n+1)#] - Floor[n#] &)[(b-a)/(a+b)]

and as discussed on page 903 this sequence can be obtained by applying a sequence of substitution rules. For Sin[ax] + Sin[bx] a more complicated sequence of substitution rules yields the analogous sequence in which -1/2 is inserted in each Floor.

■ Many sine functions. Adding many sine functions yields a so-called Fourier series (see page 1074). The pictures below show  $Sum[Sin[nx]/n, \{n, k\}]$  for various numbers of terms k. Apart from a glitch that gets narrower with increasing k (the so-called Gibbs phenomenon), the result has a simple triangular form. Other so-called Fourier series in which the coefficient of Sin[mx] is a smooth function of m for all integer m yield similarly simple results.

![](Images/_page_932_Figure_20.jpeg)

The pictures below show  $Sum[Sin[n^2 x]/n^2, \{n, k\}]$ , where in effect all coefficients of Sin[mx] other than those where m is

a perfect square are set to zero. The result is a much more complicated curve. Note that for x of the form  $p \pi/q$ , the  $k = \infty$  sum is just

 $(\pi/(2q))^2$  Sum[Sin[ $n^2 p \pi/q$ ]/Sin[ $n \pi/(2q)$ ]<sup>2</sup>, {n, q-1}]

![](Images/_page_933_Figure_3.jpeg)

The pictures below show  $Sum[Cos[2^n x], \{n, k\}]$  (as studied by Karl Weierstrass in 1872). The curves obtained in this case show a definite nested structure, in which the value at a point x is essentially determined directly from the base 2 digit sequence of x. (See also page 1080.)

![](Images/_page_933_Figure_5.jpeg)

The curves below are approximations to  $Sum[Cos[2^n x]/2^{an}, \{n, \infty\}]$ . They can be thought of as having dimensions 2-a and smoothed power spectra  $\omega^{-(1+2a)}$ .

![](Images/_page_933_Figure_7.jpeg)

- FM synthesis. More complicated curves can be obtained for example using FM synthesis, as discussed on page 1079.
- Page 148 · Zeta function. For real s the Riemann zeta function Zeta[s] is given by  $Sum[1/n^s, \{n, \infty\}]$  or  $Product[1/(1-Prime[n]^s), \{n, \infty\}]$ . The zeta function as analytically continued for complex s was studied by Bernhard Riemann in 1859, who showed that PrimePi[n] could be approximated (see page 909) up to order  $\sqrt{n}$  by  $LogIntegral[n] Sum[LogIntegral[n^r[i]], \{i, -\infty, \infty\}]$ , where the r[i] are the complex zeros of Zeta[s]. The Riemann Hypothesis then states that all r[i] satisfy Re[r[i]] = 1/2, which implies a certain randomness in the distribution of prime numbers, and a bound of order  $\sqrt{n}$  Log[n] on PrimePi[n] LogIntegral[n]. The Riemann Hypothesis is also equivalent to the statement that a bound of order  $\sqrt{n}$   $Log[n]^2$  exists on Abs[Log[Apply[LCM, Range[n]]] n].

The picture in the main text shows RiemannSiegelZ[t], defined as Zeta[1/2 + it] Exp[i RiemannSiegelTheta[t]], where RiemannSiegelTheta[t\_] =

 $Arg[Gamma[1/4 + it/2]] - 1/2t Log[\pi]$ 

The first term in an approximation to <code>RiemannSiegelZ[t]</code> is <code>2Cos[RiemannSiegelTheta[t]]</code>; to get results to a given precision requires summing a number of terms that

increases like  $\sqrt{t}$ , making routine computation possible up to  $t \sim 10^{10}$ .

It is known that:

- The average spacing between zeros decreases like 1/Log[t].
- The amplitude of wiggles grows with t, but more slowly than  $t^{0.16}$ .
- At least the first 10 billion zeros have Re[s] = 1/2.

The statistical distribution of zeros was studied by Andrew Odlyzko and others starting in the late 1970s (following ideas of David Hilbert and George Pólya in the early 1900s), and it was found that to a good approximation, the spacings between zeros are distributed like the spacings between eigenvalues of random unitary matrices (see page 977).

In 1972 Sergei Voronin showed that Zeta[z + (3/4 + it)] has a certain universality in that there always in principle exists some t (presumably in practice usually astronomically large) for which it can reproduce to any specified precision over say the region Abs[z] < 1/4 any analytic function without zeros.

#### Iterated Maps and the Chaos Phenomenon

■ History of iterated maps. Newton's method from the late 1600s for finding roots of polynomials (already used in specific cases in antiquity) can be thought of as a smooth iterated map (see page 920) in which a rational function is repeatedly applied (see page 1101). Questions of convergence led in the late 1800s and early 1900s to interest in iteration theory, particularly for rational functions in the complex plane (see page 933). There were occasional comments about complicated behavior (notably by Arthur Cayley in 1879) but no real investigation seems to have been made. In the 1890s Henri Poincaré studied so-called return maps giving for example positions of objects on successive orbits. Starting in the 1930s iterated maps were sometimes considered as possible models in fields like population biology and business cycle theory—usually arising as discrete annualized versions of continuous equations like the Verhulst logistic differential equation from the mid-1800s. In most cases the most that was noted was simple oscillatory behavior, although for example in 1954 William Ricker iterated empirical reproduction curves for fish, and saw more complex behavior—though made little comment on it. In the 1950s Paul Stein and Stanislaw Ulam did an extensive computer study of various iterated maps of nonlinear functions. They concentrated on questions of convergence, but nevertheless noted complicated behavior. (Already in the late 1940s John von Neumann had suggested using  $x \rightarrow 4x$  (1-x) as a random number generator, commenting on its extraction of initial condition digits, as mentioned on page 921.) Some detailed analytical studies of logistic maps of the form  $x \rightarrow ax(1-x)$  were done in the late 1950s and early 1960s—and in the mid-1970s iterated maps became popular, with much analysis and computer experimentation on them being done. But typically studies have concentrated on repetition, nesting and sensitive dependence on initial conditions—not on more general issues of complexity.

In connection with his study of continued fractions Carl Friedrich Gauss noted in 1799 complexity in the behavior of the iterated map  $x \to FractionalPart[1/x]$ . Beginning in the late 1800s there was number theoretical investigation of the sequence FractionalPart[anx] associated with the map  $x \rightarrow FractionalPart[ax]$  (see page 903), notably by G. H. Hardy and John Littlewood in 1914. Various features of randomness such as uniform distribution were established, and connections to smooth iterated maps emerged after the development of symbolic dynamics in the late 1930s.

- **History of chaos theory.** See page 971.
- Page 150 · Exact iterates. For any integer a the  $n^{th}$  iterate of  $x \to FractionalPart[ax]$  can be written as  $FractionalPart[a^n x]$ , or equivalently  $1/2 - ArcTan[Cot[a^n \pi x]]/\pi$ . In the specific case a = 2 the iterates of If[x < 1/2, ax, a(1-x)] have the form  $ArcCos[Cos[2^n \pi x]]/\pi$ . (See pages 903 and 1098.)
- Page 151 · Problems with computer experiments. defining characteristic of a system that exhibits chaos is that on successive steps the system samples digits which lie further and further to the right in its initial condition. But in a practical computer, only a limited number of digits can ever be stored. In Mathematica, one can choose how many digits to store (and in the pictures shown in the main text, enough digits were used to avoid the problems discussed in this note). But a lowlevel language such as FORTRAN, C or Java always stores a fixed number of digits, typically around 53, in its standard double-precision floating-point representation of numbers.

So what happens when a system one is simulating tries to sample digits in its initial conditions beyond the ones that are stored? The answer depends on the way that arithmetic is handled in the computer system one uses.

When doing high-precision arithmetic, Mathematica follows the principle that it should only ever give digits that are known to be correct on the basis of the input that was provided. This means that in simulating chaotic systems, the numbers produced will typically have progressively fewer digits: later digits cannot be known to be correct without more precise knowledge of this initial condition. (An example is  $NestList[Mod[2#, 1] \&, N[\pi/4, 40], 200]$ ; Map[Precision, list] gives the number of significant digits of each element in the list.)

But most current languages and hardware systems follow a rather different approach. (For low-precision machine arithmetic, Mathematica is also forced to follow this approach.) What they do is to give a fixed number of digits as the result of every computation, whether or not all those digits are known to be correct. It is then the task of numerical analysis to establish that in a particular computation, the final results obtained are not unduly affected by digits that are not known to be correct. And in practice, for many kinds of computations, this is to a large extent the case. But whenever chaos is involved, it is inevitably not.

As an example, consider the iterated map  $x \to Mod[2x, 1]$ discussed in the main text. At each step, this map shifts all the base 2 digits in x one position to the left. But if the computer gives a fixed number of digits at each step, then additional digits must be filled in on the right. On most computers, these additional digits are always 0. And so after some number of steps, all the digits in x are 0, and thus the value of x is simply 0.

But it turns out that a typical pocket calculator gives a different result. For pocket calculators effectively represent numbers in base 10 (actually so-called binary-coded decimal) not base 2, and fill in unknown digits with 0 in base 10. (Base 10 is used so that multiplying for example 1/3 by 3 gives exactly 1 rather than the more confusing result 0.9999... obtained with base 2.)

Pictures (a) and (c) below show simulations of the shift map on a typical computer, while pictures (b) and (d) show corresponding simulations on a pocket calculator. (Starting with initial condition x the digit sequence at step n is essentially

IntegerDigits[ $Mod[2^n Floor[2^{53} x], 2^{53}], 2, 53$ ] on the computer, and

Flatten[IntegerDigits[IntegerDigits[ Mod[2<sup>n</sup> Floor[10<sup>12</sup> x], 10<sup>12</sup>], 10, 12], 2, 4]]

on the calculator. In both cases the limited number of digits implies behavior that ultimately repeats-but only long after the other effects we discuss have occurred.)

![](Images/_page_934_Picture_17.jpeg)

For the first several steps, the results as shown at the top of each corresponding picture agree. But as soon as the effect of sampling beyond the digits explicitly stored in the initial condition becomes important, the results are completely different. The computer gives simply 0, but the pocket calculator yields apparently random sequences—which turn out to be analogous to those discussed on page 319.

Other chaotic systems have a similar sensitivity to the details of computer arithmetic. But the simple behavior of the shift map turns out to be rather rare: in most cases—such as the multiplication by 3/2 shown in the pictures below—apparent randomness is produced, even on a typical computer.

![](Images/_page_935_Picture_3.jpeg)

It is important to realize however that this randomness has little to do with the details of the initial conditions. Instead, just as in other examples in this book, the randomness arises from an intrinsic process that occurs even with the simple repetitive initial condition shown in pictures (c) and (d) above.

Computer simulations of chaotic systems have been done since the 1950s. And it has often been observed that the sequences generated in these simulations look quite random. But as we now see, such randomness cannot in fact be a consequence of the chaos phenomenon and of sensitive dependence on initial conditions.

Nevertheless, confusingly enough, even though it does not come from sensitive dependence on initial conditions, such randomness is what makes the overall properties of simulations typically follow the idealized mathematical predictions of chaos theory. The point is that the presence of randomness makes the system behave on different steps as if it were evolving from slightly different initial conditions. But statistical averages over different initial conditions typically yield essentially the results one would get by evolution from a single initial condition containing an infinite number of randomly chosen digits.

■ Page 152 · Mathematical perspectives. Mathematicians may be confused by my discussion of complexity in iterated maps.

The first point to make is that the issues I am studying are rather different from the ones that are traditionally studied in the mathematics of these systems. The next point is that I have specifically chosen not to make the idealizations about numbers and operations on numbers that are usually made in mathematics.

In particular, it is usually assumed that performing some standard mathematical operation, such as taking a square root, cannot have a significant effect on the system one is studying. But in trying to track down the origins of complex behavior, the effects of such operations can be significant. Indeed, as we saw on page 141, taking square roots can for example generate seemingly random digit sequences.

Many mathematicians may object that digit sequences are just too fragile an entity to be worth studying. They may argue that it is only robust and invariant concepts that are useful. But robustness with respect to mathematical operations is a different issue from robustness with respect to computational operations. Indeed, we will see later in this book that large classes of digit sequences can be considered equivalent with respect to computational operations, but these classes are quite different ones from those that are considered equivalent with respect to mathematical operations.

- Information content of initial conditions. Common sense suggests that it is a quite different thing to specify a simple initial condition containing, say, a single black cell on a white background, than to specify an initial condition containing an infinite sequence of randomly chosen cells. But in traditional mathematics no distinction is usually made between these kinds of specifications. And as a result, mathematicians may find it difficult to understand my distinction between randomness generated intrinsically by the evolution of a system and randomness from initial conditions (see page 299). The distinction may seem more obvious if one considers, for example, sequential substitution systems or cyclic tag systems. For such systems cannot meaningfully be given infinite random initial conditions, yet they can still perfectly well generate highly random behavior. (Their initial conditions correspond in a sense to integers rather than real numbers.)
- Smooth iterated maps. In the main text, all the functions used as mappings consist of linear pieces, usually joined together discontinuously. But the same basic phenomena seen with such mappings also occur when smooth functions are used. A particularly well-studied example (see page 918) is the so-called logistic map  $x \to ax(1-x)$ . The base 2 digit

sequences obtained with this map starting from x = 1/8 are shown below for various values of a. The quadratic nature of the map typically causes the total number of digits to double at each step. But at least for small a, progressively more digits on the left show purely repetitive behavior. As a increases, the repetition period goes through a series of doublings. The detailed behavior is different for every value of a, but whenever the repetition period is  $2^{j}$ , it turns out that with any initial condition the leftmost digit always eventually follows a sequence that consists of repetitions of step j in the evolution of the substitution system  $\{1 \rightarrow \{1, 0\}, 0 \rightarrow \{1, 1\}\}$  starting either from  $\{0\}$  or  $\{1\}$ . As a approaches 3.569946, the period doublings get closer and closer together, and eventually a point is reached at which the sequence of leftmost digits is no longer repetitive but instead corresponds to the nested pattern formed after an infinite number of steps in the evolution of the substitution system. (An important result discovered by Mitchell Feigenbaum in 1975 is that this basic setup is universal to all smooth maps whose functions have a single hump.) When a is increased further, there is usually no longer repetitive or nested behavior. And although there are typically some constraints, the behavior obtained tends to depend on the details of the digit sequence of the initial conditions. In the special case a = 4, it turns out that replacing x by  $Sin[\pi u]^2$ makes the mapping become just  $u \rightarrow FractionalPart[2u]$ , revealing simple shift map dependence on the initial digit sequence. (See pages 1090 and 1098.)

![](Images/_page_936_Picture_3.jpeg)

- Higher-dimensional generalizations. One can consider socalled Anosov maps such as  $\{x, y\} \rightarrow Mod[m.\{x, y\}, 1]$  where m is a matrix such as  $\{\{2, 1\}, \{1, 1\}\}$ . Any initial condition containing only rational numbers will then yield repetitive behavior, much as in the shift map. But as soon as m itself contains rational numbers, complicated behavior can be obtained even with an initial condition such as {1, 1}.
- Distribution of chaotic behavior. For iterated maps, unlike for discrete systems such as cellular automata, one can get continuous ranges of rules by varying parameters. With maps based on piecewise linear functions the regions of parameters in which chaotic behavior occurs typically have simple shapes; with maps based, say, on quadratic

functions, however, elaborate nested shapes can occur. (See page 934.)

- Page 155 · Lyapunov exponents. The number of new digits that are affected at each step by a small change in initial conditions gives the so-called Lyapunov exponent  $\lambda$  for the evolution. After t steps, the difference in size resulting from the change in initial conditions will be multiplied by approximately  $2^{\lambda t}$ —at least until this difference is of order 1. (See page 950.)
- Chaos in nature. See page 304.
- Bitwise operations. Cellular automata can be thought of as analogs of iterated maps in which bitwise operations such as BitXor are used instead of ordinary arithmetic ones. (See page 906.)

#### Continuous Cellular Automata

■ Implementation. The state of a continuous cellular automaton at a particular step can be represented by a list of numbers, each lying between 0 and 1. This list can then be updated using

```
CCAEvolveStep[f_, list_List] :=
 Map[f, (RotateLeft[list] + list + RotateRight[list])/3]
CCAEvolveList[f . init List. t Integer] :=
 NestList[CCAEvolveStep[f, #] &, init, t]
```

where for the rule on page 157 f is FractionalPart[3#/2]& while for the rule on page 158 it is FractionalPart[# + 1/4] &.

Note that in the definitions above, the elements of list can be either exact rational numbers, or approximate numbers obtained using N. For rough calculations, standard machineprecision numbers may sometimes suffice, but for detailed calculations exact rational numbers are essential. Indeed, the presence of exponentially increasing errors would make the bottom of the picture on page 157 qualitatively wrong if just 64-bit double-precision numbers had been used. On page 160 the effect is much larger, and almost all the pictures would be completely wrong-with the notable exception of the one that shows localized structures.

■ History. Continuous cellular automata have been introduced independently several times, under several different names. In all cases the rules have been at least slightly more complicated than the ones I consider here, and behavior starting from simple initial conditions does not appear to have been studied before. Versions of continuous cellular automata arose in the mid-1970s as idealizations of coupled ordinary differential equations for arrays of nonlinear oscillators, and implicitly in finite difference approximations to partial differential equations. They began

to be studied with extensive computer simulations in the early 1980s, probably following my work on ordinary cellular automata. Most often considered, notably by Kunihiko Kaneko and co-workers, were so-called "coupled map lattices" or "lattice dynamical systems" in which an iterated map (typically a logistic map) was applied at each step to a combination of neighboring cell value. A transition from regular class 2 to irregular class 3 behavior, with class 4 behavior involving localized structures in between, was observed, and was studied in detail by Hugues Chaté and Paul Manneville, starting in the late 1980s.

■ Page 158 · Properties. At step t the background is FractionalPart[at]. For rational a this always repeats, cycling through Denominator[a] possible values (compare page 255). In most patterns generated from initial conditions containing say a single black cell most cells whose values are not forced to be the same end up being at least slightly different—even in cases like a = 0.375. Note that in cases like a = 0.475 there is some trace of a pattern at every step—but it only becomes obvious when it makes values wrap around from 1 to 0. The pictures below show successive colors of (a) the background (compare page 950) and (b) the center cell for each a = n/500 from 0 to 1 for the systems on page 159. (Compare page 243.)

![](Images/_page_937_Picture_3.jpeg)

If *a* is not a rational number the background never repeats, but the main features of patterns obtained seem similar.

■ **Additive rules.** In the case a = 0 the systems on page 159 are purely additive. A simpler example is the rule

Mod[RotateLeft[list] + RotateRight[list], 1]

With a single nonzero initial cell with value 1/k the pattern produced is just Pascal's triangle modulo k. If k is a rational number only a limited set of values appear, and the pattern has a nested form analogous to those shown on page 870. If k is irrational then equidistribution of Mod[Binomial[t, x], k] implies that all possible values eventually appear; the corresponding patterns seem fairly irregular, as shown below. (Compare pages 953 and 1092.)

![](Images/_page_937_Picture_8.jpeg)

■ Probabilistic cellular automata. As an alternative to having continuous values at each cell, one can consider ordinary cellular automata with discrete values, but introduce probabilities for, say, two different rules to be applied at each cell. Examples of probabilistic cellular automata are shown on page 591; their behavior is typically quite similar to continuous cellular automata.

#### **Partial Differential Equations**

**Ordinary differential equations.** It is also possible to set up systems which have a finite number of continuous variables (say a[t], b[t], etc.) that change continuously with time. The rules for such systems correspond to ordinary differential equations. Over the past century, the field of dynamical systems theory has produced many results about such systems. If all equations are of the form a'[t] = f[a[t], b[t], ...], etc. then it is known for example that it is necessary to have at least three equations in order to get behavior that is not ultimately fixed or repetitive. (The Lorenz equations are an example.) If the function f depends explicitly on time, then two equations suffice. (The van der Pol equations are an example.)

Just as in iterated maps, a small change in the initial values a[0] etc. can often lead to an exponentially increasing difference in later values of a[t], etc. But as in iterated maps, the main part of this process that has been analyzed is simply the excavation of progressively less significant digits in the number a[0].

(Note that numerical simulations of ODEs on computers must approximate continuous time by discrete steps, making the system essentially an iterated map, and often yielding spurious complicated behavior.)

■ **Klein-Gordon equation.** The behavior of the Klein-Gordon equation  $\partial_{tt} u[t, x] = \partial_{xx} u[t, x] - u[t, x]$  is visually very similar to that shown for the sine-Gordon equation. For the Klein-Gordon equation, however, there is an exact solution:

 $u[t, x] = If[x^2 > t^2, 0, BesselJ[0, Sqrt[t^2 - x^2]]]$ 

• **Origins of the equations.** The diffusion equation arises in physics from the evolution of temperature or of gas density.

The wave equation represents the propagation of linear waves, for example along a compressible spring. The sine-Gordon equation represents nonlinear waves obtained for example as the limit of a very large number of pendulums all connected to a spring. The traditional name of the equation is a pun on the Klein-Gordon equation that appears in relativistic quantum mechanics and in describing strings in elastic media. It is notable that unlike with ODEs, essentially all PDEs that have been widely studied come quite directly from physics. My PDE on page 165 is however an exception.

■ Nonlinearity. The pictures below show behavior with initial conditions containing two Gaussians (and periodic boundary conditions). The diffusion and wave equations are linear, so that results are linear sums of those with single Gaussians. The sine-Gordon equation is nonlinear, but its solutions satisfy a generalized linear superposition principle. The equation from page 165 shows no such simple superposition principle. Note that even with a linear equation, fairly complicated patterns of behavior can sometimes emerge as a result of boundary conditions.

![](Images/_page_938_Picture_4.jpeg)

![](Images/_page_938_Picture_5.jpeg)

![](Images/_page_938_Picture_6.jpeg)

• Higher dimensions. The pictures below show as examples the solution to the wave equation in 1D, 2D and 3D starting from a stationary square pulse.

| 0 | 0.5 | 0.8 | 1.2 | 1.5 | 2 | 2.5 |
|---|-----|-----|-----|-----|---|-----|
| 0 | 0.5 | 0.8 | 1.2 | 1.5 | 2 | 2.5 |
| 0 | 0.5 | 0.8 | 1.2 | 1.5 | 2 | 2.5 |

In each case a 1D slice through the solution is shown, and the solution is multiplied by  $r^{d-1}$ . For the wave equation, and for a fair number of other equations, even and odd dimensions behave differently. In 1D and 3D, the value at the origin quickly becomes exactly 0; in 2D it is given by  $1-t/Sqrt[t^2-1]$ , which tends to zero only like  $-1/(2t^2)$ (which means that a sound pulse cannot propagate in a normal way in 2D).

■ Page 164 · Singular behavior. An example of an equation that yields inconsistent behavior is the diffusion equation with a negative diffusion constant:

$$\partial_t u[t, x] = -\partial_{xx} u[t, x]$$

This equation makes any variation in u as a function of xeventually become infinitely rapid.

Many equations used in physics can lead to singularities: the Navier-Stokes equations for fluid flow yield shock waves, while the Einstein equations yield black holes. At a physical level, such singularities usually indicate that processes not captured by the equations have become important. But at a mathematical level one can simply ask whether a particular equation always has solutions which are at least as regular as its initial conditions. Despite much work, however, only a few results along these lines are known.

■ Existence and uniqueness. Unlike systems such as cellular automata, PDEs do not have a built-in notion of "evolution" or "time". Instead, as discussed on page 940, a PDE is essentially just a constraint on the values of a function at different times or different positions. In solving a PDE, one is usually interested in determining values that satisfy this constraint inside a particular region, based on information about values on the edges. It is then a fundamental question how much can be specified on the edges in order to obtain a unique solution. If too little is specified, there may be many possible solutions, while if too much is specified there may be no consistent solution at all. For some very simple PDEs, the conditions for unique solutions are known. So-called hyperbolic equations (such as the wave equation, the sine-Gordon equation and my equation) work a little like cellular automata in that in at least one dimension information can propagate only at a limited speed, say c. The result is that in such equations, giving values for u[t, x] at t = 0 for -s < x < swill uniquely determine u[t, x] at larger t for -s + ct < x < s - ct. In other PDEs, such as so-called elliptic ones, there is no such limit on the rate of information propagation, and as a result, it is immediately necessary to know values of u[t, x] at all x, and on the boundaries of the region, in order to determine u[t, x] for any t > 0.

■ Page 165 · Field equations. Any equation of the form

 $\partial_{tt} u[t, x] = \partial_{xx} u[t, x] + f[u[t, x]]$ 

can be thought of as a classical field equation for a scalar field. Defining

v[u] = -Integrate[f[u], u]

the field then has Lagrangian density

 $((\partial_t u)^2 - (\partial_x u)^2)/2 - v[u]$ 

and conserves the Hamiltonian (energy function)

Integrate  $[((\partial_x u)^2 + (\partial_x u)^2)/2 + v[u], \{x, -\infty, \infty\}]$ 

With the choice for f[u] made here (with  $a \ge 0$ ), v[u] is bounded from below, and as a result it follows that no singularities ever occur in u[t, x].

■ **Equation for the background.** If u[t, x] is independent of x, as it is sufficiently far away from the main pattern, then the partial differential equation on page 165 reduces to the ordinary differential equation

$$u''[t] == (1 - u[t]^2)(1 + a u[t])$$
  
 $u[0] == u'[0] == 0$ 

For a = 0, the solution to this equation can be written in terms of Jacobi elliptic functions as

 $\sqrt{3} \ JacobiSN[t/3^{1/4}, 1/2]^2/(1 + JacobiCN[t/3^{1/4}, 1/2]^2)$  In general the solution is

 $b d JacobiSN[rt, s]^2/(b-d JacobiCN[rt, s]^2)$ where

r = -Sqrt[1/8ac(b-d)]

s = d(c-b)/(c(d-b))

and b, c, d are determined by the equation

$$(x-b)(x-c)(x-d) == -(12+6ax-4x^2-3ax^3)/(3a)$$

In all cases (except when  $-8/3 < a < -1/\sqrt{6}$ ), the solution is periodic and non-singular. For a = 0, the period is  $23^{1/4}$  EllipticK $[1/2] \simeq 4.88$ . For a = 1, the period is about 4.01; for a = 2, it is about 3.62; while for a = 4, it is about 3.18. For a = 8/3, the solution can be written without Jacobi elliptic functions, and is given by

 $3 Sin[Sqrt[5/6]t]^2/(2+3 Cos[Sqrt[5/6]t]^2)$ 

■ Numerical analysis. To find numerical solutions to PDEs on a digital computer one has no choice but to make approximations. In the typical case of the finite difference method one sets up a system with discrete cells in space and time that is much like a continuous cellular automaton, and then hopes that when the cells in this system are made small enough its behavior will be close to that of the continuous PDE.

Several things can go wrong, however. The pictures below show as one example what happens with the diffusion equation when the cells have size dt in time and dx in space. So long as the so-called Courant condition dt/dx < 1/2 is satisfied, the results are correct. But when dt/dx is made larger, an instability develops, and the discrete approximation yields completely different results from the continuous PDE.

![](Images/_page_939_Picture_14.jpeg)

Many methods beyond finite differences have been invented over the past 30 years for finding numerical solutions to PDEs. All however ultimately involve discretization, and can suffer from difficulties that are similar—though often more insidious—to those for finite differences.

For equations where one can come at least close to having explicit algebraic formulas for solutions, it has often been possible to prove that a certain discretization procedure will yield correct results. But when the form of the true solution is more complicated, such proofs are typically impossible.

And indeed in practice it is often difficult to tell whether complexity that is seen is actually a consequence of the underlying PDE, or is instead merely a reflection of the discretization procedure. I strongly suspect that many equations, particularly in fluid dynamics, that have been studied over the past few decades exhibit highly complex behavior. But in most publications such behavior is never shown, presumably because the authors are not sure whether the behavior is a genuine consequence of the equations they are studying.

■ Implementation. All the numerical solutions shown were found using the NDSolve function built into Mathematica. In general, finite difference methods, the method of lines and pseudospectral methods can be used. For equations of the form

$$\partial_{tt} u[t, x] == \partial_{xx} u[t, x] + f[u[t, x]]$$

one can set up a simple finite difference method by taking f in the form of pure function and creating from it a kernel with space step dx and time step dt:

PDEKernel[f\_, { $dx_{-}$ ,  $dt_{-}$ }] := Compile[{a, b, c, d}, Evaluate[(2b-d) + ((a+c-2b)/ $dx^2+f[b$ ])  $dt^2$ ]]

Iteration for *n* steps is then performed by

PDEEvolveList[ker\_, {u0\_, u1\_}, n\_] :=

Map[First, NestList[PDEStep[ker, #] &, {u0, u1}, n]]

PDEStep[ker\_, {u1\_, u2\_}] := {u2, Apply[ker, Transpose[ {RotateLeft[u2], u2, RotateRight[u2], u1}], {1}]}}

With this approach an approximation to the top example on page 165 can be obtained from

```
PDEEvolveList[PDEKernel[
(1-#²)(1+#) &, {0.1, 0.05}], Transpose[
Table[{1, 1}N[Exp[-x²]], {x, -20, 20, 0.1}]], 400]
```

For both this example and the middle one the results converge rapidly as dx decreases. But for the bottom example, the pictures below show that convergence is not so rapid, and indeed, as is typical in working with PDEs, despite having used large amounts of computer time I do not know whether the details of the picture in the main text are really correct. The energy function (see above) is at least roughly conserved, but it seems quite likely that the "shocks" visible are merely a consequence of the discretization procedure used.

![](Images/_page_939_Picture_29.jpeg)

![](Images/_page_939_Picture_30.jpeg)

![](Images/_page_939_Picture_31.jpeg)

■ **Different powers.** The equations

 $\partial_{tt}\,u[t,\,x] = \partial_{xx}\,u[t,\,x] + (1-u[t,\,x]^n)\,(1+a\,u[t,\,x])$ with n = 4, 6, 8, etc. appear to show similar behavior to the n = 2 equation in the main text.

![](Images/_page_940_Picture_4.jpeg)

 $\blacksquare$  Other PDEs. The pictures above show three PDEs that have been studied in recent years. All are of the so-called parabolic type, so that, unlike my equation, they have no limit on the rate of information propagation, and thus a solution in any region immediately depends on values on the boundary-which in the pictures below is taken to be periodic. (The deterministic Kardar-Parisi-Zhang equation  $\partial_t u[t, x] = a \partial_{xx} u[t, x] + 1/2 b (\partial_x u[t, x])^2$  yields behavior like Burger's equation, but symmetrical. Note that Abs[u] is plotted in the second picture, while for the last equation a common less symmetrical form replaces the last term by  $u[t, x] \partial_x u[t, x].$ 

#### **Continuous Versus Discrete Systems**

- History. From the late 1600s when calculus was invented it took about two centuries before mathematicians came to terms with the concepts of continuity that it required. And to do so it was necessary to abandon concrete intuition, and instead to rely on abstract mathematical theorems. (See page 1149.) The kind of discrete systems that I consider in this book allow a return to a more concrete form of mathematics, without the necessity for such abstraction.
- "Calculus". It is an irony of language that the word "calculus" now associated with continuous systems comes from the Latin word which means a small pebble of the kind used for doing discrete calculations (same root as "calcium").

#### Two Dimensions and Beyond

#### Introduction

- Other lattices. See page 929.
- Page 170 · 1D phenomena. Among the phenomena that cannot occur in one dimension are those associated with shape, winding and knotting, as well as traditional phase transitions with reversible evolution rules (see page 981).

#### Cellular Automata

■ **Implementation.** An *n*×*n* array of white squares with a single black square in the middle can be generated by PadLeft[{{1}}, {n, n}, 0, Floor[{n, n}/2]]

For the 5-neighbor rules introduced on page 170 each step can be implemented by

CAStep[rule\_, a\_] := Map[rule[[10-#]] &, ListConvolve[{{0, 2, 0}, {2, 1, 2}, {0, 2, 0}}, a, 2], {2}] where rule is obtained from the code number by IntegerDigits[code, 2, 10].

For the 9-neighbor rules introduced on page 177

CAStep[rule\_, a\_] := Map[rule|| 18 - #]| &,

ListConvolve[{{2, 2, 2}, {2, 1, 2}, {2, 2, 2}}, a, 2], {2}]

where rule is given by IntegerDigits[code, 2, 18].

In d dimensions with k colors, 5-neighbor rules generalize to (2d+1)-neighbor rules, with

```
CAStep[{rule_, d_}, a_] :=

Map[rule[[-1-#]] &, a + k AxesTotal[a, d], {d}]

AxesTotal[a_, d_] := Apply[Plus, Map[RotateLeft[a, #] +

RotateRight[a, #] &, IdentityMatrix[d]]]

with rule given by IntegerDigits[code, k, k (2 d (k - 1) + 1)].
```

9-neighbor rules generalize to 3<sup>d</sup> -neighbor rules, with

CAStep[{rule\_, d\_}, a\_] :=

Map[rule[[-1 - #]] &, a + k FullTotal[a, d], {d}]

FullTotal[a\_, d\_] :=

Array[RotateLeft[a, {##}] &, Table[3, {d}], -1, Plus] - a

with rule given by IntegerDigits[code, k, k ((3<sup>d</sup> - 1) (k - 1) + 1)].

In 3 dimensions, the positions of black cells can conveniently be displayed using  $\,$ 

Graphics3D[Map[Cuboid[-Reverse[#]] &, Position[a, 1]]]

■ **General rules.** One can specify the neighborhood for any rule in any dimension by giving a list of the offsets for the cells used to update a given cell. For 1D elementary rules the list is  $\{(-1, 0), \{0\}, \{1\}\}$ , while for 2D 5-neighbor rules it is  $\{(-1, 0), \{0, -1\}, \{0, 0\}, \{0, 1\}, \{1, 0\}\}$ . In this book such offset lists are always taken to be in the order given by *Sort*, so that for range r rules in d dimensions the order is the same as  $Flatten[Array[List, Table[2r+1, \{d\}], -r], d-1]$ . One can specify a neighborhood configuration by giving in the same order as the offset list the color of each cell in the neighborhood. With offset list os and k colors the possible neighborhood configurations are

```
Reverse[Table[IntegerDigits[i - 1,
k, Length[os]], {i, k^Length[os]}]]
```

(These are shown on page 53 for elementary rules and page 941 for 5-neighbor rules.) If a cellular automaton rule takes the new color of a cell with neighborhood configuration IntegerDigits[i, k, Length[os]] to be u[i+1]l, then one can define its rule number to be FromDigits[Reverse[u], k]. A single step in evolution of a general cellular automaton with state a and rule number num is then given by

```
Map[IntegerDigits[num, k, k^Length[os]][[-1-#]] &,
Apply[Plus, MapIndexed[k^(Length[os]-First[#2])
RotateLeft[a, #1] &, os]], (-1)]
```

or equivalently by

```
\label{eq:map_integer} \begin{split} &Map[&IntegerDigits[&num, k, k^Length[os]][-\#-1]] \&, \\ &ListCorrelate[&Fold[&ReplacePart[k\#1, 1, \#2+r+1]] \&, \\ &Array[0\&, Table[2r+1, \{d\}]], os], a, r+1], \{d\}] \end{split}
```

■ Numbers of possible rules. The table below gives the total number of 2D rules of various types with two possible colors for each cell. Given an initial pattern with a certain symmetry, a rule will maintain that symmetry if the rule is such that every neighborhood equivalent under the symmetry yields the same color of cell. Rules are considered rotationally

symmetric in the table below if they preserve any possible rotational symmetry consistent with the underlying arrangement of cells. Totalistic rules depend only on the total number of black cells in a neighborhood; outer totalistic rules (as in the previous note) also depend on the color of the center cell. Growth totalistic rules make any cell that becomes black remain black forever.

In such a rule, given a list of how many neighbors around a given cell (out of s possible) make the cell turn black the outer totalistic code for the rule can be obtained from

Apply[Plus, 2 ^ Join[2 list, 2 Range[s + 1] - 1]]

|                        | 5 - neighbor square           | 9 - neighbor square               | hexagonal                         |
|------------------------|-------------------------------|-----------------------------------|-----------------------------------|
| general                | $2^{32} \simeq 4 \times 10^9$ | $2^{512} \simeq 10^{154}$         | $2^{128} \simeq 3 \times 10^{38}$ |
| rotationally symmetric | $2^{12} = 4096$               | $2^{140} \simeq 10^{42}$          | $2^{28}\simeq 3\times 10^8$       |
| completely symmetric   | $2^{12} = 4096$               | $2^{102} \simeq 5 \times 10^{30}$ | $2^{26}\simeq 7\times 10^7$       |
| outer totalistic       | $2^{10} = 1024$               | $2^{18} \simeq 3 \times 10^5$     | $2^{14} = 16384$                  |
| totalistic             | $2^6 = 64$                    | $2^{10} = 1024$                   | $2^8 = 256$                       |
| growth totalistic      | $2^5 = 32$                    | $2^9 = 512$                       | $2^7 = 128$                       |

■ Symmetric 5-neighbor rules. Among the 32 possible 5-cell neighborhoods shown for example on page 941 there are 12 classes related by symmetries, given by

```
s = \{\{1\}, \{2, 3, 9, 17\}, \{4, 10, 19, 25\},
    {5}, {6, 7, 13, 21}, {8, 14, 23, 29}, {11, 18},
    {12, 20, 26, 27}, {15, 22}, {16, 24, 30, 31}, {28}, {32}}
```

Completely symmetric 5-neighbor rules can be numbered from 0 to 4095, with each digit specifying the new color of the cell for each of these symmetry classes of neighborhoods. Such rule numbers can be converted to general form using

FromDigits[Map[Last, Sort[Flatten[Map[Thread, Thread[{s, IntegerDigits[n, 2, 12]}]], 1]]], 2]

■ Growth rules. The pictures below show examples of rules in which a cell becomes black if it has exactly the specified numbers of black neighbors (the initial conditions used have the minimal number of black cells for growth). The code numbers in these cases are given by  $2/3(4^n-1) + Apply[Plus, 4^{list}]$  where n is the number of neighbors, here 5. (See also the 9-neighbor examples on page 373.)

![](Images/_page_943_Picture_11.jpeg)

![](Images/_page_943_Picture_12.jpeg)

![](Images/_page_943_Picture_13.jpeg)

![](Images/_page_943_Picture_14.jpeg)

![](Images/_page_943_Picture_15.jpeg)

■ Page 171 · Code 942 slices. The following is the result of taking vertical slices through the pattern with a sequence of offsets from the center:

![](Images/_page_943_Figure_17.jpeg)

- History. As indicated on pages 876–878, 2D cellular automata were historically studied more extensively than 1D ones—though rarely with simple initial conditions. The 5-cell neighborhood on page 170 was considered by John von Neumann in 1952; the 9-cell one on page 177 by Edward Moore in 1962. (Both are also common in finite difference approximations in numerical analysis.) (The 7-cell hexagonal neighborhood of page 369 was considered for image processing purposes by Marcel Golay in 1959.) Ever since the invention of the Game of Life around 1970 a remarkable number of hardware and software simulators have been built to watch its evolution. But until after my work in the 1980s simulators for more general 2D cellular automata were rare. A sequence of hardware simulators were nevertheless built starting in the mid-1970s by Tommaso Toffoli and later Norman Margolus. And as mentioned on page 1077, going back to the 1950s some image processing systems have been based on particular families of 2D cellular automaton rules.
- Ulam systems. Having formulated the system around 1960, Stanislaw Ulam and collaborators (see page 877) in 1967 simulated 120 steps of the process shown below, with black cells after t steps occurring at positions

```
Map[First.
  First[Nest[UStep[p[q[r[#1], #2]] &, {{1, 0}, {0, 1}, {-1, 0},
              \{0, -1\}\}, \#] \&, (\{\#, \#\} \&)[\{\{\{0, 0\}, \{0, 0\}\}\}], t]]]
UStep[f_, os_, {a_, b_}] := ({Join[a, #], #} &)[f[Flatten[
         Outer[{#1+#2, #1} &, Map[First, b], os, 1], 1], a]]
r[c_] := Map[First, Select[Split[Sort[c],
         First[#1] == First[#2] &], Length[#] == 1 &]]
q[c_-, a_-] := Select[c,
    Apply[And, Map[Function[u, qq[#1, u, a]], a]] &]
p[c_{-}] := Select[c,
    Apply[And, Map[Function[u, pp[#1, u]], c]] &]
pp[\{x_{-}, u_{-}\}, \{y_{-}, v_{-}\}] := Max[Abs[x - y]] > 1 || u == v
qq[\{x_{-}, u_{-}\}, \{y_{-}, v_{-}\}, a_{-}] := x == y || Max[Abs[x - y]] > 1 ||
    u == y \mid\mid First[Cases[a, \{u, z_{-}\} \rightarrow z]] == y
```

![](Images/_page_943_Picture_21.jpeg)

These rules are fairly complicated, and involve more history than ordinary cellular automata. But from the discoveries in this book we now know that much simpler rules can also yield very complicated behavior. And as the pictures below show, this is true even just for parts of the rules above (s alone yields outer totalistic code 686 in 2D, and rule 90 in 1D).

![](Images/_page_944_Picture_3.jpeg)

![](Images/_page_944_Picture_4.jpeg)

![](Images/_page_944_Picture_5.jpeg)

![](Images/_page_944_Picture_6.jpeg)

![](Images/_page_944_Picture_7.jpeg)

Ulam also in 1967 considered the pure 2D cellular automaton with outer totalistic code 12 (though he stated its rule in a complicated way). As shown in the pictures below, when started from blocks of certain sizes this rule yields complex patterns—although nothing like this was noted in 1967.

![](Images/_page_944_Picture_9.jpeg)

- Limiting shapes. When growth occurs at the maximum rate the outer boundaries of a cellular automaton pattern reflect the neighborhood involved in its underlying rule (in rough analogy to the Wulff construction for shapes of crystals). When growth occurs at a slower rate, a wide range of polygonal and other shapes can be obtained, as illustrated in the main text.
- Additive rules. See page 1092.
- Page 174 · Cellular automaton art. 2D cellular automata can be used to make a wide range of designs for rugs, wallpaper, and similar objects. Repeating squares of pattern can be produced by using periodic boundary conditions. Rules with more than two colors will sometimes be appropriate. For rugs, it is typically desirable to have each cell correspond to more than one tuft, since otherwise with most rules the rug looks too busy. (Compare page 872.)
- Page 177 · Code 175850. See also page 980.
- Page 178 · Code 746. The pattern generated is not perfectly circular, as discussed on page 979. Its interior is mostly fixed, but there are scattered small regions that cycle with a variety of periods.
- Page 181 · Code 174826. The pictures below show the upperright quadrant for more steps. Most of the lines visible are 8

cells across, and grow by 4 cells every 12 steps. They typically survive being hit by more complicated growth from the side. But occasionally runners 3 cells wide will start on the side of a line. And since these go 2 cells every 3 steps they always catch up with lines, producing complicated growth, often terminating the lines.

![](Images/_page_944_Picture_17.jpeg)

![](Images/_page_944_Picture_18.jpeg)

![](Images/_page_944_Picture_19.jpeg)

■ Page 183 · Projections from 3D. Looking from above, with closer cells shown darker, the following show patterns generated after 30 steps, by (a) the rule at the top of page 183, (b) the rule at the bottom of page 183, (c) the rule where a cell becomes black if exactly 3 out of 26 neighbors were black and (d) the same as (c), but with a  $3\times3\times1$  rather than a  $3\times1\times1$ initial block of black cells:

![](Images/_page_944_Picture_21.jpeg)

![](Images/_page_944_Picture_22.jpeg)

![](Images/_page_944_Picture_23.jpeg)

![](Images/_page_944_Picture_24.jpeg)

■ Other geometries. Systems like cellular automata can readily be set up on any geometrical structure in which a limited number of types of cells can be identified, with every cell of a given type having a similar neighborhood.

In the simplest case, the cells are all identical, and are laid out in the same orientation in a repetitive array. The centers of the cells form a lattice, with coordinates that are integer multiples of some set of basis vectors. The possible complete symmetries of such lattices are much studied in crystallography. But for the purpose of nearest-neighbor cellular automaton rules, what matters is not detailed geometry, but merely what cells are adjacent to a given cell. This can be determined by looking at the Voronoi region (see page 987) for each point in the lattice. In any given dimension, this region (variously known as a Dirichlet domain or Wigner-Seitz cell, and dual to the primitive cell, first Brillouin zone or Wulff shape) has a limited number of possible overall shapes. The most symmetrical versions of these shapes in 2D are the square (4 neighbors) and hexagon (6) and in 3D (as found by Evgraf Fedorov in 1885) the cube (6), hexagonal prism (8), rhombic dodecahedron (12) (e.g.

face-centered cubic crystals), rhombo-hexagonal or elongated dodecahedron (12) and truncated octahedron or tetradecahedron (14) (e.g. body-centered cubic crystals), as shown below. (In 4D, 8, 16 and 24 nearest neighbors are possible; in higher dimensions possibilities have been investigated in connection with sphere packing.) (Compare pages 1029 and 986.)

![](Images/_page_945_Picture_2.jpeg)

In general, there is no need for individual cells in a cellular automaton to have the same orientation. A triangular lattice is one example where they do not. And indeed, any tiling of congruent figures can readily be used to make a cellular automaton, as illustrated by the pentagonal example below. (Outer totalistic codes specify rules; the first rule makes a particular cell black when any of its five neighbors are black and has code 4094. Note that even though individual cells are pentagonal, large-scale cellular automaton patterns usually have 2-, 4- or 8-fold symmetry.)

![](Images/_page_945_Picture_4.jpeg)

There is even no need for the tiling to be repetitive; the picture below shows a cellular automaton on a nested Penrose tiling (see page 932). This tiling has two different shapes of tile, but here both are treated the same by the cellular automaton rule, which is given by an outer totalistic code number. The first example is code 254, which makes a particular cell become black when any of its three neighbors are black. (Large-scale cellular automaton patterns here can have 5-fold symmetry.) (See also page 1027.)

![](Images/_page_945_Picture_6.jpeg)

■ Networks. Cellular automata can be set up so that each cell corresponds to a node in a network. (See page 936.) The only requirement is that around each node the network must have the same structure (or at least a limited number of possible structures). For nearest-neighbor rules, it suffices that each node has the same number of connections. For longer-range rules, the network must satisfy constraints of the kind discussed on page 483. (Cayley graphs of groups always have the necessary homogeneity.) If the connections at each node are not labelled, then only totalistic cellular automaton rules can be implemented. Many topological and geometrical properties of the underlying network can affect the overall behavior of a cellular automaton on it.

#### **Turing Machines**

■ **Implementation.** With rules represented as a list of elements of the form  $\{s, a\} \rightarrow \{sp, ap, \{dx, dy\}\}$  (s is the state of the head and a the color of the cell under the head) each step in the evolution of a 2D Turing machine is given by

TM2DStep[rule\_, {s\_, tape\_, r : {x\_, y\_}}] := Apply[{#1, ReplacePart[tape, #2, {r}], r + #3} &, {s, tape[[x, y]]}/. rule]

■ History. At a formal level 2D Turing machines have been studied since at least the 1950s. And on several occasions systems equivalent to specific simple 2D Turing machines have also been constructed. In fact, much as for cellular automata, more explicit experiments have been done on 2D Turing machines than 1D ones. A tradition of early robotics going back to the 1940s-and leading for example to the Logo computer language—involved studying idealizations of mobile turtles. And in 1971 Michael Paterson and John Conway constructed what they described as an idealization of a prehistoric worm, which was essentially a 2D Turing machine in which the state of the head records the direction of the motion taken at each step. Michael Beeler in 1973 used a computer at MIT to investigate all 1296 possible worms with rules of the simplest type on a hexagonal grid, and he found several with fairly complex behavior. But this discovery does not appear to have been followed up, and systems equivalent to simple 2D Turing machines were reinvented again, largely independently, several times in the mid-1980s: by Christopher Langton in 1985 under the name "vants"; by Rudy Rucker in 1987 under the name "turmites"; and by Allen Brady in 1987 under the name "turning machines". The specific 4-state rule

 $\{s_{-}, c_{-}\}: With[\{sp = s (2c - 1)i\}, \{sp, 1 - c, \{Re[sp], Im[sp]\}\}]$ 

has been called Langton's ant, and various studies of it were done in the 1990s.

■ Visualization. The pictures below show the 2D position of the head at 500 successive steps for the rules on page 185.

![](Images/_page_946_Picture_4.jpeg)

Some 2D Turing machines exhibit elements of randomness at some steps, but then fill in every so often to form simple repetitive patterns. An example is the 3-state rule

- Rules based on turning. The rules used in the main text specify the displacement of the head at each step in terms of fixed directions in the underlying grid. An alternative is to specify the turns to make at each step in the motion of the head. This is how turtles in the Logo computer language are set up. (Compare the discussion of paths in substitution systems on page 892.)
- 2D mobile automata. Mobile automata can be generalized just like Turing machines. Even in the simplest case, however, with only four neighbors involved there are already  $(4k)^k$ possible rules, or nearly  $10^{29}$  even for k = 2.

#### **Substitution Systems and Fractals**

■ Implementation. With the rule on page 187 given for example by  $\{1 \to \{\{1, 0\}, \{1, 1\}\}, 0 \to \{\{0, 0\}, \{0, 0\}\}\}$  the result of t steps in the evolution of a 2D substitution system from an initial condition such as {{1}} is given by

```
SS2DEvolve[rule_, init_, t_1 :=
 Nest[Flatten2D[# /. rule] &, init, t]
Flatten2D[list_] :=
 Apply[Join, Map[MapThread[Join, #] &, list]]
```

■ Connection with digit sequences. Just as in the 1D case discussed on page 891, the color of a cell at position {i, j} in a 2D substitution system can be determined using a finite automaton from the digit sequences of the numbers *i* and *j*. At step *n*, the complete array of cells is

```
Table[If[FreeQ[Transpose[IntegerDigits[{i, i}, k, n]], form],
    1, 0], \{i, 0, k^n - 1\}, \{j, 0, k^n - 1\}]
```

where for the pattern on page 187, k = 2 and  $form = \{0, 1\}$ . For patterns (a) through (f) on page 188, k = 3 and form is given respectively by (a) {1, 1}, (b) {0/2, 0/2}, (c)  $\{0|2, 0|2\}|\{1, 1\}, (d) \{i_{-}, j_{-}\}/; j > i, (e) \{0, 2\}|\{1, 1\}|\{2, 0\}, (f)\}$ {0, 2}/{1, 1}. Note that the excluded pairs of digits are in exact correspondence with the positions of which squares are 0 in the underlying rules for the substitution systems. (See pages 608 and 1091.)

- Page 187 · Sierpiński pattern. Other ways to generate step n of the pattern shown here in various orientations include:
- Mod[Array[Binomial, {2, 2}<sup>n</sup>, 0], 2] (see pages 611 and 870)
- 1 Sign[Array[BitAnd, {2, 2}<sup>n</sup>, 0]] (see pages 608 and 871)
- NestList[Mod[RotateLeft[#]+#, 2] &, PadLeft[{1}, 2<sup>n</sup>], 2<sup>n</sup> - 1] (see page 870)
- NestList[Mod[ListConvolve[{1, 1}, #, -1], 2] &,  $PadLeft[{1}, 2^{n}], 2^{n} - 1]$ (see page 870)
- IntegerDigits[NestList[BitXor[2#, #] &, 1, 2<sup>n</sup> 1], 2, 2<sup>n</sup>] (see page 906)
- NestList[Mod[Rest[FoldList[Plus, 0, #]], 2] &, Table[1,  $\{2^n\}$ ],  $2^n - 1$ ] (see page 1034)
- Table[PadRight[  $Mod[CoefficientList[(1+x)^{t-1}, x], 2], 2^n - 1], \{t, 2^n\}]$ (see pages 870 and 951)
- Reverse[Mod[CoefficientList[Series[1/(1-(1+x)y),  $\{x,\,0,\,2^n-1\},\,\{y,\,0,\,2^n-1\}],\,\{x,\,y\}],\,2]]$ (see page 1091)
- Nest[Apply[Join, MapThread[ Join, {{#, #}, {0#, #}}, 2]] &, {{1}}, n] (compare page 1073)

The positions of black squares can be found from:

- Nest[Flatten[2# /.  $\{x_-, y_-\} \rightarrow \{\{x, y\}, \{x + 1, y\}, \{x, y + 1\}\},$ 11 &, {{0, 0}}, n]
- (Transpose[{Re[#], Im[#]}] &)[ Flatten[Nest[ $\{2\#, 2\# + 1, 2\# + i\} \&, \{0\}, n$ ]]] (compare page 1005)
- Position[Map[Split, NestList[Sort[Flatten[{#, # + 1}]] &, {0}, 2<sup>n</sup> - 1]], \_?(OddQ[Length[#]] &), {2}] (see page 358)
- Flatten[Table[Map[{t, #} &, Fold[Flatten[{#1, #1 + #2}] &, 0, Flatten[2^(Position[ Reverse[IntegerDigits[t, 2]], 1] - 1)]]],  $\{t, 2^n - 1\}$ ], 1] (see page 870)
- Map[Map[FromDigits[#, 2] &, Transpose[Partition[#, 2]]] &, Position[Nest[{{#, #}, {#}} &, 1, n], 1] - 1] (see page 509)

A formatting hack giving the same visual pattern is DisplayForm[Nest[SubsuperscriptBox[#, #, #] &, "1", n]]

■ Non-white backgrounds. The pictures below substitution systems in which white squares are replaced by blocks which contain black squares. There is still a nested structure but it is usually not visually as obvious as before. (See page 583.)

![](Images/_page_947_Figure_4.jpeg)

■ Higher-dimensional generalizations. The state of a ddimensional substitution system can be represented by a nested list of depth d. The evolution of the system for t steps can be obtained from

```
SSEvolve[rule_, init_, t_, d_Integer] :=
  Nest[FlattenArray[# /. rule, d] &, init, t]
FlattenArray [list . d ] :=
  Fold[Function[{a, n}, Map[MapThread[Join, #, n] &,
        a, -\{d+2\}]], list, Reverse[Range[d] - 1]]
```

The analog in 3D of the 2D rule on page 187 is  $\{1 \rightarrow Array[If[LessEqual[##], 0, 1] \&, \{2, 2, 2\}],$  $0 \rightarrow Array[0 \&, \{2, 2, 2\}]\}$ 

Note that in d dimensions, each black cell must be replaced by at least d+1 black cells at each step in order to obtain an object that is not restricted to a dimension d-1hyperplane.

■ Other shapes. The systems on pages 187 and 188 are based on subdividing squares into smaller squares. But one can also set up substitution systems that are based on subdividing other geometrical figures, as shown below.

![](Images/_page_947_Picture_10.jpeg)

The second example involves two distinct shapes: a square and a GoldenRatio aspect ratio rectangle. Labelling each shape and orientation with a different color, the behavior of this system can be reproduced with equal-sized squares using the rule  $\{3 \rightarrow \{\{1, 0\}, \{3, 2\}\}, 2 \rightarrow \{\{1\}, \{3\}\}, 1 \rightarrow \{\{3, 2\}\}, 0 \rightarrow \{\{3\}\}\}\}$  starting from initial condition {{3}}.

■ Penrose tilings. The nested pattern shown below was studied by Roger Penrose in 1974 (see page 943).

![](Images/_page_947_Picture_14.jpeg)

The arrangement of triangles at step t can be obtained from a substitution system according to

With[ $\{\phi = GoldenRatio\}$ , Nest[# /. a[p\_, q\_, r\_] :> With[ $\{s = (p + \phi q)(2 - \phi)\}, \{a[r, s, q], b[r, s, p]\}\}$ ]/.  $b[p_-, q_-, r_-] :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-, r_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi)\}, \{a[p, q, s], b[p_-, q_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi), b[p_-, q_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi), b[p_-, q_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi), b[p_-, q_-]\} :\rightarrow With[\{s = (p + \phi r)(2 - \phi),$ r, s, q}} &, a[{1/2, Sin[2  $\pi$ /5]  $\phi$ }, {1, 0}, {0, 0}], t]]

This pattern can be viewed as generalizations of the pattern generated by the 1D Fibonacci substitution system (c) on page 83. As discussed on page 903, this 1D sequence can be obtained by looking at how a line with GoldenRatio slope cuts through a 2D lattice of squares. Penrose tilings can be obtained by looking at how a 2D plane with slopes based on GoldenRatio cuts through a lattice of hypercubes in 5D. The tilings turn out to have approximate 5-fold symmetry. (See also page 943.)

In general, projections onto any regular lattice in any number of dimensions from hyperplanes with any quadratic irrational slopes will yield nested patterns that can be generated by subdividing some shape or another according to a substitution system. Despite some confusion in the literature, however, this procedure can reproduce only a tiny fraction of all possible nested patterns.

■ Page 189 · Dragon curve. The pattern shown here can be obtained in several related ways, including from numbers in base i-1 (see below) and from a doubled version of the paths generated by 1D paperfolding substitution systems (see page 892). Its boundary has fractal dimension  $2 \text{Log}[2, \text{Root}[2 + \#1^2 - \#1^3, 1]] \simeq 1.52$ .

■ Implementation. The most convenient approach is to represent each pattern by a list of complex numbers, with the center of each square being given in terms of each complex number z by  $\{Re[z], Im[z]\}$ . The pattern after n steps is then given by Nest[Flatten[f[#]] &, {0}, n], where for the rule on page 189  $f[z_{-}] = 1/2(1-i)\{z+1/2, z-1/2\}$   $(f[z_{-}] = (1-i)\{z+1, z\}$  gives a transformed version). For the rule on page 190,  $f[z_{-}] = 1/2(1-i)\{iz + 1/2, z - 1/2\}$ . For rules (a), (b) and (c) (Koch curve) on page 191 the forms of  $f[z_{-}]$  are respectively:

 $(0.296 - 0.57 i)z - 0.067 i - \{1.04, 0.237\}$  $N[1/40\{17(\sqrt{3}-i)z, -24+14z\}]$  $N[(1/2(1/\sqrt{3}-1)(i+\{1,-1\})-i-(1+\{i,-i\}/\sqrt{3})z)/2]$ 

■ Connection with digit sequences. Patterns after t steps can be viewed as containing all t-digit integers in an appropriate complex base. Thus the patterns on page 189 can be formed from t-digit integers in base i - 1 containing only digits 0 and 1, as given by

Table[FromDigits[IntegerDigits[s, 2, t], i-1], {s, 0,  $2^t-1$ }]

In the particular case of base i-q with digits 0 through  $q^2$ , it turns out that for sufficiently large t any complex integer can be represented, and will therefore be part of the pattern. (Compare page 1094.)

■ Visualization. The 3D pictures below show successive steps in the evolution of each of the geometric substitution systems from the main text

![](Images/_page_948_Picture_8.jpeg)

- Parameter space sets. See pages 407 and 1006 for a discussion of varying parameters in geometrical substitution
- Affine transformations. Any set of so-called affine transformations that take the vector for each point, multiply it by a fixed matrix and then add a fixed vector, will yield nested patterns similar to those shown in the main text. Linear operations on complex numbers of the kind discussed above correspond geometrically to rotations, translations and rescalings. General affine transformations also allow reflection and skewing. In addition, affine transformations can readily be generalized to any number of dimensions, while complex numbers represent only two dimensions.

- Complex maps. Many kinds of nonlinear transformations on complex numbers yield nested patterns. Sets of so-called Möbius transformations of the form  $z \rightarrow (az + b)/(cz + d)$ always yield such patterns (and correspond to so-called modular groups when ad-bc == 1). Transformations of the form  $z \rightarrow \{Sqrt[z-c], -Sqrt[z-c]\}$  yield so-called Julia sets which form nested patterns for many values of c (see note below). In fact, a fair fraction of all possible transformations based on algebraic functions will yield nested patterns. For typically the continuity of such functions implies that only a limited number of shapes not related by limited variations in local magnification can occur at any scale.
- Fractal dimensions. Certain features of nested patterns can be characterized by so-called fractal dimensions. The pictures below show five patterns with three successively finer grids superimposed. The dimension of a pattern can be computed by looking at how the number of grid squares that have any gray in them varies with the length a of the edge of each grid square. In the first case shown, this number varies like  $(1/a)^1$  for small a, while in the last case, it varies like  $(1/a)^2$ . In general, if the number varies like  $(1/a)^d$ , one can take d to be the dimension of the pattern. And in the intermediate cases shown, it turns out that d has non-integer values.

![](Images/_page_948_Picture_13.jpeg)

The grid in the pictures above fits over the pattern in a very regular way. But even when this does not happen, the limiting behavior for small a is still  $(1/a)^d$  for any nested pattern. This form is inevitable if the underlying pattern effectively has the same structure on all scales. For some of the more complex patterns encountered in this book, however, there continues to be different structure on different scales, so that the effective value of d fluctuates as the scale changes, and may not converge to any definite value. (Precise definitions of dimension based for example on the maximum ever achieved by d will often in general imply formally noncomputable values, as in the discussion of page 1138.)

Fractal dimensions characterize some aspects of nested patterns, but patterns with the same dimension can often look very different. One approach to getting better characterizations is to look at each grid square, and to ask not just whether there is any gray in it, but how much. Quantities derived from the mean, variance and other moments of the probability distribution can serve as generalizations of fractal dimension. (Compare page 959.)

■ History of fractals. The idea of using nested 2D shapes in art probably goes back to antiquity; some examples were shown on page 43. In mathematics, nested shapes began to be used at the end of the 1800s, mainly as counterexamples to ideas about continuity that had grown out of work on calculus. The first examples were graphs of functions: the curve on page 918 was discussed by Bernhard Riemann in 1861 and by Karl Weierstrass in 1872. Later came geometrical figures: example (c) on page 191 was introduced by Helge von Koch in 1906, the example on page 187 by Wacław Sierpiński in 1916, examples (a) and (c) on page 188 by Karl Menger in 1926 and the example on page 190 by Paul Lévy in 1937. Similar figures were also produced independently in the 1960s in the course of early experiments with computer graphics, primarily at MIT. From the point of view of mathematics, however, nested shapes tended to be viewed as rare and pathological examples, of no general significance. But the crucial idea that was developed by Benoit Mandelbrot in the late 1960s and early 1970s was that in fact nested shapes can be identified in a great many natural systems and in several branches of mathematics. Using early raster-based computer display technology, Mandelbrot was able to produce striking pictures of what he called fractals. And following the publication of Mandelbrot's 1975 book, interest in fractals increased rapidly. Quantitative comparisons of pure power laws implied by the simplest fractals with observations of natural systems have had somewhat mixed success, leading to the introduction of multifractals with more parameters, but Mandelbrot's general idea of the importance of fractals is now well established in both science and mathematics.

■ The Mandelbrot set. The pictures below show Julia sets produced by the procedure of taking the transformation  $z \rightarrow \{Sqrt[z-c], -Sqrt[z-c]\}$  discussed above and iterating it starting at z=0 for an array of values of c in the complex plane.

![](Images/_page_949_Figure_4.jpeg)

The Mandelbrot set introduced by Benoit Mandelbrot in 1979 is defined as the set of values of c for which such Julia sets are connected. This turns out to be equivalent to the set of values of c for which starting at z = 0 the inverse mapping  $z \rightarrow z^2 + c$  leads only to bounded values of z. The Mandelbrot set turns out to have many intricate features which have been widely reproduced for their aesthetic value, as well as studied by mathematicians. The first picture below shows the overall form of the set; subsequent pictures show successive magnifications of the regions indicated. All parts of the Mandelbrot set are known to be connected. The whole set is not self-similar. However, as seen in the third and fourth pictures, within the set are isolated small copies of the whole set. In addition, as seen in the last picture, near most values of c the boundary of the Mandelbrot set looks very much like the Julia set for that value of *c*.

![](Images/_page_949_Figure_6.jpeg)

On pages 407 and 1006 I discuss parameter space sets that are somewhat analogous to the Mandelbrot set, but whose properties are in many respects much clearer. And from this discussion there emerges the following interpretation of the Mandelbrot set that appears not to be well known but which I find most illuminating. Look at the array of Julia sets and ask for each c whether the Julia set includes the point c = 0.

The set of values of c for which it does corresponds exactly to the boundary of the Mandelbrot set. The pictures below show a generalization of this idea, in which gray level indicates the minimum distance  $Abs[z-z_0]$  of any point z in the Julia set from a fixed point  $z_0$ . The first picture shows the case  $z_0 = 0$ , corresponding to the usual Mandelbrot set.

![](Images/_page_950_Picture_3.jpeg)

![](Images/_page_950_Picture_4.jpeg)

![](Images/_page_950_Figure_5.jpeg)

■ Page 192 · Neighbor-dependent substitution systems. Given a list of individual replacement rules such as  $\{\{-, 1\}, \{0, 1\}\} \rightarrow \{\{1, 0\}, \{1, 1\}\}, \text{ each step in the evolution}$ shown corresponds to

Flatten2D[Partition[list, {2, 2}, 1, -1] /. rule]

One can consider rules in which some replacements lead to subdivision of elements but others do not. However, unlike for the 1D case, there will in general in 2D be an arbitrarily large set of different possible neighborhood configurations around any given cell.

■ Page 192 · Space-filling curves. One can conveniently scan a finite 2D grid just by going along each successive row in turn. One can scan a quadrant of an infinite grid using the  $\sigma$ function on page 1127, or one can scan a whole grid by for example going in a square spiral that at step t reaches position  $(1/2(-1)^{\#}(\{1,-1\}(Abs[\#^2-t]-\#)+\#^2-t-Mod[\#,2])\&)[$  $Round[\sqrt{t}]$ 

#### **Network Systems**

■ Implementation. The nodes in a network system can conveniently be labelled by numbers 1, 2, ... n, and the network obtained at a particular step can be represented by a list of pairs, where the pair at position i gives the numbers corresponding to the nodes reached by following the above and below connections from node i. With this setup, a network consisting of just one node is {{1, 1}} and a 1D array of n nodes can be obtained with

```
CyclicNet[n_] := RotateRight[
    Table[Mod[\{i-1, i+1\}, n] + 1, \{i, n\}]]
```

With above connections represented as 1 and the below connections as 2, the node reached by following a succession s of connections from node i is given by

Follow[list\_, i\_, s\_List] := Fold[list[[#1]][[#2]] &, i, s]

The total number of distinct nodes reached by following all possible succession of connections up to length *d* is given by

```
NeighborNumbers[list_, i_Integer, d_Integer] :=
   Map[Length, NestList[Union[Flatten[list[#]]]] &,
           Union[list[[i]]], d - 1]]
```

For each such list the rules for the network system then specify how the connections from node *i* should be rerouted. The rule  $\{2, 3\} \rightarrow \{\{2, 1\}, \{1\}\}$  specifies that when NeighborNumbers gives {2, 3} for a node i, the connections from that node should become {Follow[list, i, {2, 1}], Follow[list, i, {1}]}. The rule  $\{2, 3\} \rightarrow \{\{\{2, 1\}, \{1, 1\}\}, \{1\}\}$  specifies that a new node should be inserted in the above connection, and this new node should have connections {Follow[list, i, {2, 1}], Follow[list, i, {1, 1}]}. With rules set up in this way, each step in the evolution of a network system is given by

```
NetEvolveStep[{depth_Integer, rule_List}, list_List] := Block[
 {new = {}}, Join[Table[Map[NetEvolveStep1[#, list, i] &,
     Replace[NeighborNumbers[list, i, depth],
     rule]], {i, Length[list]}], new]]
NetEvolveStep1[s:{___Integer}, list_, i_] := Follow[list, i, s]
NetEvolveStep1[{s1:{___Integer}, s2:{___Integer}},
    list_, i_] := Length[list] + Length[
     AppendTo[new, {Follow[list, i, s1], Follow[list, i, s2]}]]
```

The set of nodes that can be reached from node *i* is given by

```
ConnectedNodes[list_, i_] :=
 FixedPoint[Union[Flatten[{#, list[[#]]}]] &, {i}]
```

and disconnected nodes can be removed using

```
RenumberNodes[list . sea 1 :=
 Map[Position[seq, #][[1, 1]] &, list[[seq]], {2}]
```

The sequence of networks obtained on successive steps by applying the rules and then removing all nodes not connected to node number 1 is given by

```
NetEvolveList[rule_, init_, t_Integer] :=
 NestList[(RenumberNodes[#, ConnectedNodes[#, 1]] &)[
       NetEvolveStep[rule, #]] &, init, t]
```

Note that the nodes in each network are not necessarily numbered in the order that they appear on successive lines in the pictures in the main text. Additional information on the origin of each new node must be maintained if this order is to be found

- Rule structure. For depth 1, the possible results from NeighborNumbers are {1} and {2}. For depth 2, they are {1, 1}, {1, 2}, {2, 1}, {2, 2}, {2, 3} and {2, 4}. In general, each successive element in a list from NeighborNumbers cannot be more than twice the previous element.
- Undirected networks. Networks with connections that do not have definite directions are discussed at length in Chapter 9, mainly as potential models for space in the universe. The rules for updating such networks turn out to be

somewhat more difficult to apply than those for the network systems discussed here.

- Page 199 · Computer science. The networks discussed here can be thought of as very simple analogs of data structures in practical computer programs. The connections correspond to pointers between elements of these data structures. The fact that there are two connections coming from each node is reminiscent of the LISP language, but in the networks considered here there are no leaves corresponding to atoms in LISP. Note that the process of dropping nodes that become disconnected is analogous to so-called "garbage collection" for data structures. The networks considered here are also related to the combinator systems discussed on page 1121.
- Page 202 · Properties. Random behavior seems to occur in a few out of every thousand randomly selected rules of the kind shown here. In case (c), the following gives a list of the numbers of nodes generated up to step *t*:

```
FoldList[Plus, 1, Join[{1, 4, 12, 10, -20, 6, 4}, Map[d, IntegerDigits[Range[4, t - 5], 2]]]]
d[{___, 1}] = 1
d[{1, p : ((0) ...), 0}] := -Apply[Plus, 4 Range[Length[{p}]] - 1] + 6
d[{__, 1, p : ((0) ...), 0}] := d[{1, p, 0}] - 7
d[{___, p : ((1) ...), q : ((0) ...), 1, 0}] := 4 Length[{p}] + 3 Length[{q}] + 2
d[{___, p : ((1) ...), 1, 0}] := 4 Length[{p}] + 2
```

■ Sequential network systems. In the network systems discussed in the main text, every node is updated in parallel at each step. It is however also possible to consider systems in which there is only a single active node, and operations are performed only on that node at any particular step. The active node can move by following its above or below connections, in a way that is determined by a rule which depends on the local structure of the network. The pictures below show examples of sequential network systems; the path of the active node is indicated by a thick black line.

![](Images/_page_951_Picture_6.jpeg)

![](Images/_page_951_Picture_7.jpeg)

![](Images/_page_951_Picture_8.jpeg)

It is rather common for the active node eventually to get stuck at a particular position in the network; the picture below shows the effect of this on the total number of nodes in the last case illustrated above. The rule for this system is

```
 \begin{aligned} &\{(1,1) \to \{(\{(\},\{1,1\}),\{2\}),2\},\{1,2\} \to \{\{(2,2\},\{\{\},\{2,2\})\},2\},\\ &\{2,1\} \to \{(\{\},\{2,2\}),2\},\{2,2\} \to \{\{\{1,2\},\{\{1\},\{2\}\}\},1\},\\ &\{2,3\} \to \{\{\{\{1,2\},\{1\}\},\{\{2\},\{2,1\}\}\}\},2\},\\ &\{2,4\} \to \{\{\{2,2\},\{\{2,1\},\{\}\}\},1\}\}. \end{aligned}
```

![](Images/_page_951_Figure_11.jpeg)

■ **Dimensionality of networks.** As discussed on page 479, if a sufficiently large network has a  $\sigma$ -dimensional form, then by following r connections in succession from a given node, one should reach about  $r^{\sigma}$  distinct nodes. The plots below show the actual numbers of nodes reached as a function of r for the systems on pages 202 and 203 at steps 1, 10, 20, ..., 200.

![](Images/_page_951_Figure_13.jpeg)

- Cellular automata on networks. The cellular automata that we have considered so far all have cells arranged in regular arrays. But one can also set up generalizations in which the cells correspond to nodes in arbitrary networks. Given a network of the kind discussed in the main text of this section, one can assign a color to each node, and then update this color at each step according to a rule that depends on the colors of the nodes to which the connections from that node go. The behavior obtained depends greatly on the form of the network, but with networks of finite size the results are typically like those obtained for other finite size cellular automata of the kind discussed on page 259.
- **Implementation.** Given a network represented as a list in which element i is  $\{a, i, b\}$ , where a is the node reached by the above connection from node i, and b is the node reached by the below connection, each step corresponds to

```
NetCAStep[{rule_, net_}, list_] :=
    Map[Replace[#, rule] &, list[[net]]]
```

■ **Boolean networks.** Several lines of development from the cybernetics movement (notably in immunology, genetics and management science) led in the 1960s to a study of random Boolean networks—notably by Stuart Kauffman and Crayton Walker. Such systems are like cellular automata on networks, except for the fact that when they are set up each node has a rule that is randomly chosen from all  $2^{2^s}$  possible ones with s inputs. With s = 2 class 2 behavior (see Chapter 6) tends to

dominate. But for s > 2, the behavior one sees quickly approaches what is typical for a random mapping in which the network representing the evolution of the  $2^m$  states of the m underlying nodes is itself connected essentially randomly (see page 963). (Attempts were made in the 1980s to study phase transitions as a function of s in analogy to ones in percolation and spin glasses.) Note that in almost all work on random Boolean networks averages are in effect taken over possible configurations, making it impossible to see anything like the kind of complex behavior that I discuss in cellular automata and many other systems in this book.

#### Multiway Systems

■ Implementation. It is convenient to represent the state of a multiway system at each step by a list of strings, where an individual string is for example "ABBAAB". The rules for the multiway system can then be given for example as

```
\{"AAB" \rightarrow "BB", "BA" \rightarrow "ABB"\}
```

The evolution of the system is given by the functions

```
MWStep[rule_List, slist_List] := Union[Flatten[
      Map[Function[s, Map[MWStep1[#, s] &, rule]], slist]]]
MWStep1[p\_String \rightarrow q\_String, s\_String] :=
  Map[StringReplacePart[s, q, #] &, StringPosition[s, p]]
MWEvolveList[rule_, init_List, t_Integer] :=
  NestList[MWStep[rule, #] &, init, t]
```

An alternative approach uses lists instead of strings, and in effect works by tracing the internal steps that Mathematica goes through in trying out possible matchings. With the rule from above written as

```
\{\{x_{--}, 0, 0, 1, y_{--}\} \rightarrow \{x, 1, 1, y\},\
     \{x_{--}, 1, 0, y_{--}\} \rightarrow \{x, 0, 1, 1, y\}\}
MWStep can be rewritten as
   MWStep[rule_List, slist_List] :=
      Union[Flatten[Map[ReplaceList[#, rule] &, slist], 1]]
```

The case shown on page 206 is

```
\{ "AB" \to "", "ABA" \to "ABBAB", "ABABBB" \to "AAAAABA" \}
starting with {"ABABAB"}. Note that the rules are set up so that
a string for which there are no applicable replacements at a
given step is simply dropped.
```

■ General properties. The merging of states (as done above by Union) is crucial to the behavior seen. Note that the pictures shown indicate only which states yield which states-not for example in how many ways the rules can be applied to a given state to yield a given new state.

If there was no merging, then if a typical state yielded more than one new state, then inevitably the total number of states would increase exponentially. But when there is merging, this need not occur-making it difficult to give probabilistic estimates of growth rates. Note that a given rule can yield very different growth rates with different initial conditions. Thus, for example, the growth rate for  $\{"A" \to "AA", "AB" \to "BA", "BA" \to "AB"\}$  is  $t^{n+1}$ , where n is the number of initial B's. With most rules, states that appear at one step can disappear at later steps. But if "A"  $\rightarrow$  "A" and its analogs are part of the rule, then every state will always be kept, almost inevitably leading to overall nesting in pictures like those on page 208.

In cases where all strings that appear both in rules and initial conditions are sorted—so that for example A's appear before B's-any string generated will also be sorted, so it can be specified just by giving a list of how many A's and how many B's appear in it. The rule for the system can then be stated in terms of a difference vector-which for  $\{"BA" \rightarrow "AAA", "BAA" \rightarrow "BBBA"\}$  is  $\{\{2, -1\}, \{-1, 2\}\}$ . Given a list of string specifications, a step in the evolution of the multiway system corresponds to

```
Select[Union[Flatten[Outer[Plus, diff, list, 1], 1]],
 Abs[#] == # &]
```

■ Page 206 · Properties. The total number of strings grows approximately quadratically; its differences repeat (offset by 1) with period 1071. The number of new strings generated at successive steps grows approximately linearly; its differences repeat with period 21. The third element of the rule is at first used only on some steps-but after step 50 it appears to be used somewhere in every step.

The pictures below show in stacked form (as on page 208) all sequences generated at various steps of evolution. Note that after just a few steps, the sequences produced always seem to consist of white elements followed by black, with possibly one block of black in the white region. Without this additional block of black, only the first case in the rule can ever apply.

![](Images/_page_952_Picture_19.jpeg)

![](Images/_page_952_Picture_20.jpeg)

![](Images/_page_952_Picture_21.jpeg)

![](Images/_page_952_Picture_22.jpeg)

In analogy with page 796 the picture below shows wh different strings with lengths up to 10 are reached in the evolution of the system.

![](Images/_page_952_Figure_24.jpeg)

Different initial conditions for this multiway system lead to behavior that either dies out (as for "ABA"), or grows exponentially forever (as for "ABAABABA").

- Frequency of behavior. Among multiway systems with randomly chosen rules, one finds about equal numbers that grow rapidly and die out completely. A few percent exhibit repetitive behavior, while only one in several million exhibit more complex behavior. One common form of more complex behavior is quadratic growth, with essentially periodic fluctuations superimposed—as on page 206.
- History. Versions of multiway systems have been invented many times in a variety of contexts. In mathematics specific examples of them arose in formal group theory (see below) around the end of the 1800s. Axel Thue considered versions with two-way rules (analogous to semigroups, as discussed below) in 1912, leading to the name semi-Thue systems sometimes being used for general multiway systems. Other names for multiway systems have included string and term rewrite systems, production systems and associative calculi. From the early 1900s various generalizations of multiway systems were used as idealizations of mathematical proofs (see page 1150); multiway systems with explicit pattern variables (such as  $s_{-}$ ) were studied under the name canonical systems by Emil Post starting in the 1920s. Since the 1950s, multiway systems have been widely used as generators of formal languages (see below). Simple analogs of multiway systems have also been used in genetic analysis in biology and in models for particle showers and other branching processes in physics and elsewhere.
- Semigroups and groups. The multiway systems that I discuss can be viewed as representations for generalized versions of familiar mathematical structures. Semigroups are obtained by requiring that rules come in pairs: with each rule such as "ABB"  $\rightarrow$  "BA" there must also be the reversed rule "BA" → "ABB". Such pairs of rules correspond to relations in the semigroup, specifying for example that "ABB" is equivalent to "BA". (The operation in the semigroup is concatenation of strings; "" acts as an identity element, so in fact a monoid is always obtained.) Groups require that not only rules but also symbols come in pairs. Thus, for example, in addition to a symbol A, there must be an inverse symbol a, with the rules "Aa"  $\rightarrow$  "", "aA"  $\rightarrow$  "" and their reversals.

In the usual mathematical approach, the objects of greatest interest for many purposes are those collections of sequences that cannot be transformed into each other by any of the rules given. Such collections correspond to distinct elements of the group or semigroup, and in general many different choices of underlying rules may yield the same elements with the same properties. In terms of multiway systems, each of the elements corresponds to a disconnected part of the network formed from all possible sequences.

Given a particular representation of a group or semigroup in terms of rules for a multiway system, an object that is often useful is the so-called Cayley graph—a network where each node is an element of the group, and the connections show what elements are reached by appending each possible symbol to the sequences that represent a given element. The so-called free semigroup has no relations and thus no rules, so that all strings of generators correspond to distinct elements, and the Cayley graph is a tree like the ones shown on page 196. The simplest non-trivial commutative semigroup has rules "AB"  $\rightarrow$  "BA" and "BA"  $\rightarrow$  "AB", so that strings of generators with A's and B's in different orders are equivalent and the Cayley graph is a 2D grid.

For some sets of underlying rules, the total number of distinct elements in a group or semigroup is finite. (Compare page 945.) A major mathematical achievement in the 1980s was the complete classification of all possible so-called simple finite groups that in effect have no factors. (For semigroups no such classification has yet been made.) In each case, there are many different choices of rules that yield the same group (and similar Cayley graphs). And it is known that even fairly simple sets of rules can yield large and complicated groups. The icosahedral group  $A_5$  defined by the rules  $x^2 = y^3 = (xy)^5 = 1$  has 60 elements. But in the most complicated case a dozen rules yield the Monster Group, where the number of elements is

808017424794512875886459904961710757005754368000000000 (See also pages 945 and 1032.)

Following work in the 1980s and 1990s by Mikhael Gromov and others, it is also known that for groups with randomly chosen underlying rules, the Cayley graph is usually either finite, or has a rapidly branching tree-like structure. But there are presumably also marginal cases that exhibit complex behavior analogous to what we saw in the main text. And indeed for example, despite conjectures to the contrary, it was found in the 1980s by Rostislav Grigorchuk that complicated groups could be constructed in which growth intermediate between polynomial and exponential can occur. (Note that different choices of generators can yield Cayley graphs with different local subgraphs; but the overall structure of a sufficiently large graph for a particular group is always the

■ Formal languages. The multiway systems that I discuss are similar to so-called generative grammars in the theory of formal languages. The idea of a generative grammar is that all possible expressions in a particular formal language can be produced by applying in all possible ways the set of replacement rules given by the grammar. Thus, for example, the rules  $\{"x" \rightarrow "xx", "x" \rightarrow "(x)", "x" \rightarrow "()"\}$  starting with "x" will generate all expressions that consist of balanced sequences of parentheses. (Final expressions correspond to those without the "non-terminal" symbol x.) The hierarchy described by Noam Chomsky in 1956 distinguishes four kinds of generative grammars (see page 1104):

Regular grammars. The left-hand side of each rule must consist of one non-terminal symbol, and the right-hand side can contain only one non-terminal symbol. An example is  $\{"x" \rightarrow "xA", "x" \rightarrow "yB", "y" \rightarrow "xA"\}$  starting with "x" which generates sequences in which no pair of B's ever appear together. Expressions in regular languages can be recognized by finite automata of the kind discussed on page 957.

Context-free grammars. The left-hand side of each rule must consist of one non-terminal symbol, but the right-hand side can contain several non-terminal symbols. Examples include the parenthesis language mentioned above,  $\{"x" \rightarrow "AxA", "x" \rightarrow "B"\}$  starting with "x", and the syntactic definitions of Mathematica and most other modern computer languages. Context-free languages can be recognized by a computer using only memory on a single last-in first-out stack. (See pages 1091 and 1103.)

Context-sensitive grammars. The left-hand side of each rule is no longer than the right, but is otherwise unrestricted. An example is  $\{"Ax" \rightarrow "AAxx", "xA" \rightarrow "BAA", "xB" \rightarrow "Bx"\}$  starting with "AAxBA", which generates expressions of the form  $Table["A", \{n\}] \iff Table["B", \{n\}] \iff Table["A", \{n\}].$ 

Unrestricted grammars. Any rules are allowed.

(See also page 944.)

- Multidimensional multiway systems. As a generalization of multiway systems based on 1D strings one can consider systems in which rules operate on arbitrary blocks of elements in an array in any number of dimensions. Still more general network substitution systems are discussed on page 508.
- Limited size versions. One can set up multiway systems of limited size by applying transformations cyclically to strings.
- Multiway tag systems. See page 1141.
- Multiway systems based on numbers. One can consider for example the rule  $n \rightarrow \{n+1, 2n\}$  implemented by

NestList[Union[Flatten[{# + 1, 2#}]] &, {0}, t]

In this case there are Fibonacci[t+2] distinct numbers obtained at step t. In general, rules based on simple arithmetic operations yield only simple nested structures. If the numbers n are allowed to have both real and imaginary parts then results analogous to those discussed for substitution systems on page 933 are obtained. (Somewhat related systems based on recursive sequences are discussed on page 907. Compare also sorted multiway systems on page 937.)

- Non-deterministic systems. Multiway systems are examples of what are often in computer science called nondeterministic systems. The general idea of a nondeterministic system is to have rules with several possible outcomes, and then to allow each of these outcomes to be followed. Non-deterministic Turing machines are a common example. For most types of systems (such as Turing machines) such non-deterministic versions do not ultimately allow any greater range of computations to be performed than deterministic ones. (But see page 766.)
- Fundamental physics. See page 504.
- Game systems. One can think of positions or configurations in a game as corresponding to nodes in a large network, and the possible moves in the game as corresponding to connections between nodes. Most games have rules which imply that if certain states are reached one player can be forced in the end to lose, regardless of what specific moves they make. And even though the underlying rules in the game may be simple, the pattern of such winning positions is often quite complex. Most games have huge networks whose structure is difficult to visualize (even the network for tic-tactoe, for example, has 5478 nodes). One example that allows easy visualization is a simplification of several common games known as nim. This has k piles of objects, and on alternate steps each of two players takes as many objects as they want from any one of the piles. The winner is the player who manages to take the very last object. With just two piles one player can force the other to lose by arranging that after each of their moves the two piles have equal heights. With more than two piles it was discovered in 1901 that one player can in general force the other to lose by arranging that after each of their moves Apply[BitXor, h] = 0, where h is the list of heights. For k > 1 this yields a nested pattern, analogous to those shown on page 871. If one allows only specific numbers of objects to be taken at each step a nested pattern is again obtained. With more general rules it seems almost inevitable that much more complicated patterns will occur.

#### **Systems Based on Constraints**

■ The notion of equations. In the mathematical framework traditionally used in the exact sciences, laws of nature are usually represented not by explicit rules for evolution, but rather by abstract equations. And in general what such equations do is to specify constraints that systems must satisfy. Sometimes these constraints just relate the state of a system at one time to its state at a previous time. And in such cases, the constraints can usually be converted into explicit evolution rules. But if the constraints relate different features of a system at one particular time, then they cannot be converted into evolution rules. In computer programs and other kinds of discrete systems, explicit evolution rules and implicit constraints usually work very differently. But in traditional continuous mathematics, it turns out that these differences are somewhat obscured. First of all, at a formal level, equations corresponding to these two cases can look very similar. And secondly, the equations are almost always so difficult to deal with at all that distinctions between the two cases are not readily noticed.

In the language of differential equations—the most widely used models in traditional science—the two cases we are discussing are essentially so-called initial value and boundary value problems, discussed on page 923. And at a formal level, the two cases are so similar that in studying partial differential equations one often starts with an equation, and only later tries to work out whether initial or boundary values are needed in order to get either any solution or a unique solution. For the specific case of secondorder equations, it is known in general what is needed. Elliptic equations such as the Laplace equation need boundary values, while hyperbolic and parabolic equations such as the wave equation and diffusion equation need initial values. But for higher-order equations it can be extremely difficult to work out what initial or boundary values are needed, and indeed this has been the subject of much research for many decades.

Given a partial differential equation with initial or boundary values, there is then the question of solving it. To do this on a computer requires constructing a discrete approximation. But it turns out that the standard methods used (such as finite difference and finite element) involve extremely similar computations for initial and for boundary value problems, leaving no trace of the significant differences between these cases that are so obvious in the discrete systems that we discuss in most of this book.

■ Linear and nonlinear systems. A vast number of different applications of traditional mathematics are ultimately based

on linear equations of the form  $u = m \cdot v$  where u and v are vectors (lists) and m is a matrix (list of lists), all containing ordinary continuous numbers. If v is known then such equations in essence provide explicit rules for computing u. But if only u is known, then the equations can instead be thought of as providing implicit constraints for v. However, it so happens that even in this case v can still be found fairly straightforwardly using LinearSolve[m, u]. With vectors of length n it generically takes about  $n^2$  steps to compute ugiven v, and a little less than  $n^3$  steps to compute v given u(the best known algorithms-which are based on matrix multiplication—currently involve about  $n^{2.4}$  steps). But as soon as the original equation is nonlinear, say  $u = m_1 \cdot v + m_2 \cdot v^2$ , the situation changes dramatically. It still takes only about  $n^2$  steps to compute u given v, but it becomes vastly more difficult to compute v given u, taking perhaps  $2^{2^n}$  steps. (Generically there are  $2^n$  solutions for v, and even for integer coefficients in the range -r to +r already in 95% of cases there are 4 solutions with n = 2 as soon as  $r \ge 6.$ 

- Explanations based on constraints. In some areas of science it is common to give explanations in terms of constraints rather than mechanisms. Thus, for example, in physics there are so-called variational principles which state that physical systems will behave in ways that minimize or maximize certain quantities. One such principle implies that atoms in molecules will tend to arrange themselves so as to minimize their energy. For simple molecules, this is a useful principle. But for complicated molecules of the kind that are common in living systems, this principle becomes much less useful. In fact, in finding out what configuration such molecules actually adopt, it is usually much more relevant to know how the molecule evolves in time as it is created than which of its configurations formally has minimum energy. (See pages 342 and 1185.)
- Page 211 · 1D constraints. The constraints in the main text can be thought of as specifying that only some of the  $k^n$  possible blocks of cells of length n (with k possible colors for each cell) are allowed. To see the consequences of such constraints consider breaking a sequence of colors into blocks of length n, with each block overlapping by n-1 cells with its predecessor, as in Partition[list, n, 1]. If all possible sequences of colors were allowed, then there would be k possibilities for what block could follow a given block, given by  $Map[Rest, Table[Append[list, i], \{i, 0, k-1\}]]$ . The possible sequences of length n blocks that can occur are conveniently represented by possible paths by so-called de Bruijn networks, of the kind shown for k = 2 and n = 2 through 5 below.

![](Images/_page_956_Picture_2.jpeg)

Given the network for a particular n, it is straightforward to see what happens when only certain length n blocks are allowed: one just keeps the arcs in the network that correspond to allowed blocks, and drops all other ones. Then if one can still form an infinite path by going along the arcs that remain, this path will correspond to a pattern that satisfies the constraints. Sometimes there will be a unique such path; in other cases there will be choices that can be made along the path. But the crucial point is that since there are only  $k^{n-1}$  nodes in the network, then if any infinite path is possible, there must be such a path that visits the same node and thus repeats itself after at most  $k^{n-1}$  cells. The constraint on page 210 has k = 2 and n = 3; the pattern that satisfies it repeats with period 4, thus saturating the bound. (See also page 266.)

- 1D cellular automata. In a cellular automaton with k colors and r neighbors, configurations that are left invariant after t steps of evolution according to the cellular automaton rule are exactly the ones which contain only those length 2r + 1blocks in which the center cell is the same before and after the evolution. Such configurations therefore obey constraints of the kind discussed in the main text. As we will see on page 225 some cellular automata evolve to invariant configurations from any initial conditions, but most do not. (See page 954.)
- Dynamical systems theory. Sets of sequences in which a finite collection of blocks are excluded are sometimes known as finite complement languages, or subshifts of finite type. (See page 958.)
- Page 215 · 2D constraints. The constraints shown here are minimal, in the sense that in each case removing any of the allowed templates prevents the constraint from ever being satisfied. Note that constraints which differ only by overall rotation, reflection or interchange of black and white are not explicitly shown. The number of allowed templates out of the total of 32 possible varies from 1 to 15 for the constraints shown, with 12 being the most common. Smaller sets of allowed templates typically seem to lead to constraints that can be satisfied by visually simpler patterns.

**Numbering scheme.** The constraint numbered n allows the templates at Position[IntegerDigits[n, 2, 32], 1] in the list below. (See also page 927.)

![](Images/_page_956_Picture_8.jpeg)

- Identifying the 171 patterns. The number of constraints to consider can be reduced by symmetries, by discarding sets of templates that are supersets of ones already known to be satisfiable, and by requiring that each template in the set be compatible with itself or with at least one other in each of the eight immediately adjacent positions. The remaining constraints can then be analyzed by attempting to build up explicit patterns that satisfy them, as discussed below.
- Checking constraints. A set of allowed templates can be specified by a Mathematica pattern of the form  $t_1/t_2/t_3$  etc. where the  $t_i$  are for example  $\{\{-, 1, -\}, \{0, 0, 1\}, \{-, 0, -\}\}\}$ . To check whether an array list contains only arrangements of colors corresponding to allowed templates one can then use

```
SatisfiedQ[list_, allowed_] :=
  Apply[And, Map[MatchQ[#, allowed] &,
      Partition[list, {3, 3}, {1, 1}], {2}], {0, 1}]
```

■ Representing repetitive patterns. Repetitive patterns are often most conveniently represented as tessellations of rectangles whose corners overlap. Pattern (a) on page 213 can be specified as

```
{{2, -1, 2, 3}, {{0, 0, 0, 0}, {1, 1, 0, 0}, {1, 0, 0, 0}}}
```

Given this, a complete nx by ny array filled with this pattern can be constructed from

```
c[{d1_, d2_, d3_, d4_}, {x_, y_}] :=
  With[{d = d1 d2 + d1 d4 + d3 d4}],
    Mod[\{\{d2x + d4x + d3y, d4x - d1y\}\}/d, 1]]
Fill[{dlist_, data_}, {nx_, ny_}] :=
 Array[c[dlist, {##}] &, {nx, ny}]/. Flatten[MapIndexed[
    c[dlist, Reverse[#2]] \rightarrow #1 \&, Reverse[data], \{2\}], 1]
```

• Searching for patterns. The basic approach to finding a pattern which satisfies a particular constraint on an infinite array of cells is to start with a pattern which satisfies the constraint in a small region, and then to try to extend the pattern. Often the constraint will immediately force a unique extension of the pattern, at least for some distance. But eventually there will normally be places where the pattern is not yet uniquely determined, and so a series of choices have to be made. The procedure used to find the results in this book attempts to extend patterns along a square spiral, making whatever choices are needed, and backtracking if these turn out to be inconsistent with the constraint. At every step in the procedure, regularities are tested for that would imply the possibility of an infinite repetitive pattern. In addition, whenever there is a choice, the first cases to be tried are set up to be ones that tend to extend whatever regularity has developed so far. And when backtracking is needed, the procedure always goes back to the most recent choice that actually affected whatever inconsistency was discovered. And in addition it remembers what has already been worked out, so as to avoid, for example, unnecessarily working out the pattern on the opposite side of the spiral again.

- Undecidability. The general problem of whether an infinite pattern exists that satisfies a particular constraint is formally undecidable (see page 1139). This means that in general there can be no upper bound on the size of region for which the constraints can be satisfied, even if they are not satisfiable for the complete infinite grid.
- **NP** completeness. The problem of whether a pattern can be found that satisfies a constraint even in a finite region is NPcomplete. (See page 1145.) This suggests that to determine whether a repetitive pattern with repeating blocks of size nexists may in general take a number of steps which grows more rapidly than any polynomial in n.
- Enumerating patterns. Compare page 959.
- **Page 219 · Non-periodic pattern.** The color at position x,y in the pattern is given by

```
a[x_{-}, y_{-}] := Mod[y + 1, 2]/; x + y > 0
a[x_{-}, y_{-}] := 0 /; Mod[x + y, 2] == 1
a[x_{-}, y_{-}] :=
  Mod[Floor[(x-y)2^{(x+y-6)/4}], 2]/; Mod[x+y, 4] == 2
a[x_{-}, y_{-}] := 1 - Sign[Mod[x - y + 2, 2^{(-x-y+8)/4}]]
```

The origin of the x,y coordinates is the only freedom in this pattern. The nested structure is like the progression of base 2 digit sequences shown on page 117. Negative numbers are effectively represented by complements of digit sequences, much as in typical practical computers. With the procedure described above for finding patterns that satisfy a constraint, generating the pattern shown here is straightforward once the appropriate constraint is identified.

■ Other types of constraints. Constraints based on smaller templates simply require smaller numbers of repetitive patterns: 1:4; 1:7; 1:17; 1:12. To extend the class of systems considered in the main text, one can increase the size of the templates, or increase the number of possible colors for each cell. For 3×3 templates with two colors extensive randomized searches have failed to discover examples where non-repetitive patterns are forced to occur. Another extension of the constraints in the main text is to require that not just a single template, but every template in the set, must occur somewhere in the pattern. Searches of such systems have also failed to discover examples of forced non-repetitive patterns beyond the one shown in the text.

■ Forcing nested patterns. It is straightforward to find constraints that allow nested patterns; the challenge is to find ones that force such patterns to occur. Many nested patterns (such as the one made by rule 90, for example) contain large areas of uniform white, and it is typically difficult to prevent pure repetition of that area. One approach to finding constraints that can be satisfied only by nested patterns is nevertheless to start from specific nested patterns, look at what templates occur, and then see whether these templates are such that they do not allow any purely repetitive patterns. A convenient way to generate a large class of nested patterns is to use 2D substitution systems of the kind discussed on page 188. But searching all 4 billion or so possible such systems with 2×2 blocks and up to four colors one finds not a single case in which a nested pattern is forced to occur. It can nevertheless be shown that with a sufficiently large number of extra colors any nested pattern can be forced to occur. And it turns out that a result from the mid-1970s by Robert Ammann for a related problem of tiling (see below) allows one to construct a specific system with 16 colors in which constraints of the kind discussed here force a nested pattern to occur. One starts from the substitution system with rules

```
\{1 \to \{\{3\}\}, 2 \to \{\{13, 1\}, \{4, 10\}\}, 3 \to \{\{15, 1\}, \{4, 12\}\},
                                4 \rightarrow \{\{14, 1\}, \{2, 9\}\}, 5 \rightarrow \{\{13, 1\}, \{4, 12\}\}, 6 \rightarrow \{\{13, 1\}, \{8, 9\}\},
                                7 \to \{\{15,\ 1\},\ \{4,\ 10\}\},\ 8 \to \{\{14,\ 1\},\ \{6,\ 10\}\},\ 9 \to \{\{14\},\ \{2\}\},
                                    10 \rightarrow \{\{16\}, \{7\}\}, 11 \rightarrow \{\{13\}, \{8\}\}, 12 \rightarrow \{\{16\}, \{3\}\}, \{3\}\}, \{10 \rightarrow \{\{16\}, \{16\}\}, \{16\}\}, \{11 \rightarrow \{\{16\}, \{16\}\}, \{11 \rightarrow \{16\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, \{11 \rightarrow \{11\}\}, 
                                        13 \rightarrow \{\{5, 11\}\}, 14 \rightarrow \{\{2, 9\}\}, 15 \rightarrow \{\{3, 11\}\}, 16 \rightarrow \{\{6, 10\}\}\}
```

This yields the nested pattern below which contains only 51 of the 65,536 possible 2×2 blocks of cells with 16 colors. It then turns out that with the constraint that the only 2×2 arrangements of colors that can occur are ones that match these 51 blocks, one is forced to get the nested pattern below.

![](Images/_page_957_Picture_14.jpeg)

■ Relation to 2D cellular automata. The kind of constraints discussed are exactly those that must be satisfied by configurations that remain unchanged in the evolution of a 2D cellular automaton. The argument for this is similar to the one on pages 941 and 954 for 1D cellular automata. The point is that of the 32 5-cell neighborhoods involved in the 2D cellular automaton rule, only some subset will have the property that the center cell remains unchanged after applying the rule. And any configuration which does not change must involve only these subsets. Using the results of this section it then follows that in the evolution of all 2D cellular automata of the type discussed on page 170 there exist purely repetitive configurations that remain unchanged.

Relation to 1D cellular automata. A picture that shows the evolution of a 1D cellular automaton can be thought of as a 2D array of cells in which the color of each cell satisfies a constraint that relates it to the cells above according to the cellular automaton rule. This constraint can then be represented in terms of a set of allowed templates; the set for rule 30 is as follows:

![](Images/_page_958_Picture_4.jpeg)

To reproduce an ordinary picture of cellular automaton evolution, one would have to specify in advance a whole line of black and white cells. Below this line there would then be a unique pattern corresponding to the application of the cellular automaton rule. But above the line, except for reversible rules, there is no guarantee that any pattern satisfying the constraints can exist.

If one specifies no cells in advance, or at most a few cells, as in the systems discussed in the main text, then the issue is different, however. And now it is always possible to construct a repetitive pattern which satisfies the constraints simply by finding repetitive behavior in the evolution of the cellular automaton from a spatially repetitive initial condition.

- Non-computable patterns. It is known to be possible to set up constraints that will force patterns in which finding the color of a particular cell can require doing something like solving a halting problem—which cannot in general be done by any finite computation. (See also page 1139.)
- Tiling. The constraints discussed here are similar to those encountered in covering the plane with tiles of various shapes. Of regular polygons, only squares, triangles and hexagons can be used to do this, and in these cases the tilings are always repetitive. For some time it was believed that any set of tiles that could cover the plane could be arranged to do so repetitively. But in 1964 Robert Berger demonstrated that this was not the case, and constructed a set of about 20,000 tiles that could cover the plane only in a nested fashion. Later Berger reduced the number of tiles needed to 104. Then Raphael Robinson in 1971 reduced the number tiles to six, and in 1974 Roger Penrose showed that just two tiles were necessary. Penrose's tiles can cover the plane only in a nested pattern that can be constructed from a substitution system that successively subdivides each tile, as shown on page 932. (Note that various dissections of these tiles can also be used. The edges of the particular shapes shown should strictly be distinguished in order to prevent trivial periodic arrangements.) The triangles in the construction have angles

which are multiples of  $\pi/5$ , so that the whole tiling has an approximate 5-fold symmetry (see page 994). Repetitive tilings of the plane can only have 3-, 4- or 6-fold symmetry.

No single shape is known which has the property that it can tile the plane only non-repetitively, although one strongly suspects that one must exist. In 3D, John Conway has found a single biprism that can fill space only in a sequence of layers with an irrational rotation angle between each layer.

In addition, in no case has a simple set of tiles been found which force a pattern more complicated than a nested one. The results on page 221 in this book can be used to constructed a complicated set of tiles with this property, but I suspect that a much simpler set could be found.

(See also page 1139.)

■ **Polyominoes.** An example of a tiling problem that is in some respects particularly close to the grid-based constraint systems discussed in the main text concerns covering the plane with polyominoes that are formed by gluing collections of squares together. Tiling by polyominoes has been investigated since at least the late 1950s, particularly by Solomon Golomb, but it is only very recently that sets of polyominoes which force non-periodic patterns have been found. The set (a) below was announced by Roger Penrose in 1994; the slightly smaller set (b) was found by Matthew Cook as part of the development of this book.

![](Images/_page_958_Picture_14.jpeg)

![](Images/_page_958_Picture_15.jpeg)

Both of these sets yield nested patterns. Steps in the construction of the pattern for set (b) are shown below. At stage n the number of polyominoes of each type is Fibonacci  $[2n - \{2, 0, 1\}]/\{1, 2, 1\}$ . Set (a) works in a roughly similar way, but with a considerably more complicated recursion.

![](Images/_page_958_Picture_17.jpeg)

- Ground states of spin systems. The constraints discussed in the main text are similar to those that arise in the physics of 2D spin systems. An example of such a system is the socalled Ising model discussed on page 981. The idea in all such systems is to have an array of spins, each of which can be either up or down. The energy associated with each spin is then given by some function which depends on the configuration of neighboring spins. The ground state of the system corresponds to an arrangement of spins with the smallest total energy. In the ordinary Ising model, this ground state is simply all spins up or all spins down. But in generalizations of the Ising model with more complicated energy functions, the conditions to get a state of the lowest possible energy can correspond exactly to the constraints discussed in the main text. And from the results shown one sees that in some cases random-looking ground states should occur. Note that a rather different way to get a somewhat similar ground state is to consider a spin glass, in which the standard Ising model energy function is used, but multiplied by -1 or +1 at random for each spin.
- Correspondence systems. For a discussion of a class of 1D systems based on constraints see page 757.
- **Sequence equations.** Another way to set up 1D systems based on constraints is by having equations like  $Flatten[\{x, 1, x, 0, y\}] === Flatten[\{0, y, 0, y, x\}]$ , where each variable stands for a list. Fairly simple such equations can force fairly complicated results, although as discussed on page 1141 there are known to be limits to this complexity.
- **Pattern-avoiding sequences.** As another form of constraint one can require, say, that no pair of identical blocks ever appear together in a sequence, so that the sequence does not match  $\{--, x_-, x_-, x_-, ...\}$ . With just two possible elements, no sequence above length 3 can satisfy this constraint. But with k = 3 possible elements, there are infinite nested sequences that can, such as the one produced by the substitution system  $\{0 \rightarrow \{0, 1, 2\}, 1 \rightarrow \{0, 2\}, 2 \rightarrow \{1\}\}$ , starting with  $\{0\}$ . One can find the sequences of length n that work by using

 $Nest[DeleteCases[Flatten[Map[Table[Append[\#, i-1], {i, k}] \&, \#], 1], \{\_\_, x\_, x\_, \_\_] \&, \{\{\}\}, n] \\ and the number of these grows roughly like <math>3^{n/4}$ .

The constraint that no triple of identical blocks appear together turns out to be satisfied by the Thue-Morse nested sequence from page 83—as already noted by Axel Thue in 1906. (The number of sequences that work seems to grow roughly like  $2^{n/2}$ .)

For any given k, many combinations of blocks will inevitably occur in sufficiently long sequences (compare page 1068). (For example, with k = 2,  $\{\_\_$ ,  $x\_\_$ ,  $y\_\_$ ,  $x\_\_$ ,  $y\_\_$ ,  $x\_\_$ ,  $y\_\_$ ,  $x\_\_$ ) always

matches any sequence with length more than 18.) But some patterns of blocks can be avoided. And for example it is known that for  $k \ge 2$  any pattern with length 6 or more (excluding the \_\_\_'s) and only two different variables (say  $x_{-}$  and  $y_{-}$ ) can always be avoided. But it also known that among the infinite sequences which do this, there are always nested ones (sometimes one has to iterate one substitution rule, then at the end apply once a different substitution rule). With more variables, however, it seems possible that there will be patterns that can be avoided only by sequences with a more complicated structure. And a potential sign of this would be patterns for which the number of sequences that avoid them varies in a complicated way with length.

- Formal languages. Formal languages of the kind discussed on page 938 can be used to define constraints on 1D sequences. The constraints shown on page 210 correspond to special cases of regular languages (see page 940). For both regular and context-free languages the so-called pumping lemmas imply that if any finite sequences satisfy the constraints, then so must an essentially repetitive infinite sequence.
- **Diophantine equations.** Any algebraic equation—such as  $x^3 + x + 1 = 0$ —can readily be solved if one allows the variables to have any numerical value. But if one insists that the variables are whole numbers, then the problem is more analogous to the discrete constraints in the main text, and becomes much more difficult. And in fact, even though such so-called Diophantine equations have been studied since well before the time of Diophantus around perhaps 250 AD, only limited results about them are known.

Linear Diophantine equations such as ax == by + c yield simple repetitive results, as in the pictures below, and can be handled essentially just by knowing *ExtendedGCD[a, b]*.

![](Images/_page_959_Picture_12.jpeg)

![](Images/_page_959_Picture_13.jpeg)

![](Images/_page_959_Picture_14.jpeg)

![](Images/_page_959_Picture_15.jpeg)

Even the simplest quadratic Diophantine equations can already show much more complex behavior. The equation  $x^2 = ay^2$  has no solution except when a is a perfect square. But the Pell equation  $x^2 = ay^2 + 1$  (already studied in antiquity) has infinitely many solutions whenever a is positive and not a perfect square. The smallest solution for x is given by

Numerator [FromContinuedFraction[ ContinuedFraction[ $\sqrt{a}$ , (If[EvenQ[#], #, 2#]&)[ Length[Last[ContinuedFraction[ $\sqrt{a}$ ]]]]]]]

This is plotted below; complicated variation and some very large values are seen (with a = 61 for example x == 1766319049).

![](Images/_page_960_Figure_3.jpeg)

In three variables, the equation  $x^2 + y^2 = z^2$  yields so-called Pythagorean triples {3, 4, 5}, {5, 12, 13}, etc. And even in this case the set of possible solutions for x and y in the pictures below looks fairly complicated—though after removing common factors, they are in fact just given by  $\{x = r^2 - s^2, y = 2rs, z = r^2 + s^2\}$ . (See page 1078.)

![](Images/_page_960_Figure_5.jpeg)

The pictures below show the possible solutions for *x* and *y* in various Diophantine equations. As in other systems based on numbers, nested patterns are not common—though page 1160 shows how they can in principle be achieved with an equation whose solutions satisfy Mod[Binomial(x, y), 2] == 1. (The equation (2x + 1)y = z also for example has solutions only when z is not of the form  $2^{j}$ .)

![](Images/_page_960_Picture_7.jpeg)

Many Diophantine equations have at most very sparse solutions. And indeed for example Fermat's Last Theorem states that  $x^n + y^n == z^n$  can never be satisfied for n > 2. With

four variables one has for example  $3^3 + 4^3 + 5^3 = 6^3$ ,  $1^3 + 6^3 + 8^3 = 9^3$ —but with fourth powers the smallest result is  $95800^4 + 217519^4 + 414560^4 == 422481^4$ .

(See pages 791 and 1164.)

- Matrices satisfying constraints. One can consider for example magic squares, Latin squares (quasigroup multiplication tables), and matrices having the Hadamard property discussed on page 1073. One can also consider matrices whose powers contain certain patterns. (See also page 805.)
- Finite groups and semigroups. Any finite group or semigroup can be thought of as defined by having a multiplication table which satisfies the constraints given on page 887. The total number of semigroups increases faster than exponentially with size in a seemingly quite uniform way. But the number of groups varies in a complicated way with size, as in the picture below. (The peaks are known to grow roughly like  $n^{(2/27 \text{Log}(2, n)^2)}$ —intermediate between polynomial and exponential.) As mentioned on page 938, through major mathematical effort, a complete classification of all finite so-called simple groups that in effect have no factors is known. Most such groups come in families that are easy to characterize; a handful of so-called sporadic ones are much more difficult to find. But this classification does not immediately provide a practical way to enumerate all possible groups. (See also pages 938 and 1032.)

![](Images/_page_960_Figure_13.jpeg)

Constraints on formulas. Many standard problems of algebraic computation can be viewed as consisting in finding formulas that satisfy certain constraints. An example is exact solution of algebraic equations. For quadratic equations the standard formula gives solutions for arbitrary coefficients in terms of square roots. Similar formulas in terms of n<sup>th</sup> roots have been known since the 1500s for equations with degrees n up to 4, although their *LeafCount* starting at n = 1 increases like 6, 25, 183, 718. For higher degrees it is known that such general formulas must involve other functions. For degrees 5 and 6 it was shown in the late 1800s that EllipticTheta or Hypergeometric2F1 are sufficient, although for degrees 5 and 6 respectively the necessary formulas have a LeafCount in the billions. (Sharing common subexpressions yields a LeafCount in the thousands.) (See also page 1129.)

#### Starting from Randomness

#### The Emergence of Order

■ Page 226 · Properties of patterns. For a random initial condition, the average density of black cells is exactly 1/2. For rule 126, the density after many steps is still 1/2. For rule 22, it is approximately 0.35095. For rule 30 and rule 150 it is exactly 1/2, while for rule 182 it is 3/4. And insofar as rule 110 converges to a definite density, the density is 4/7. (See page 953 for a method of estimating these densities.)

Even after many steps, individual lines in the patterns produced by rules 30 and 150 remain in general completely random. But in rule 126, black cells always tend to appear in pairs, while in rule 182, every white cell tends to be surrounded by black ones. And in rule 22, there are more complicated conditions involving blocks of 4 cells.

The density of triangles of size n goes roughly like  $2^{-n}$  for rules 126, 30 (see also page 871), 150 and 182 and roughly like  $1.3^{-n}$  for rule 22.

In the algebraic representation discussed on page 869, rule 22 is  $Mod[p+q+r+p\,q\,r,\,2]$ , rule 126 is  $Mod[(p+q)\,(q+r)+(p+r),\,2]$ , rule 150 is  $Mod[p+q+r,\,2]$  and rule 182 is  $Mod[p\,r\,(1+q)+(p+q+r),\,2]$ .

![](Images/_page_962_Picture_7.jpeg)

- Continual injection of randomness. In the main text we discuss what happens when one starts from random initial conditions and then evolves according to a definite cellular automaton rule. As an alternative one can consider starting with very simple initial conditions, such as all cells white, and then at each step randomly changing the color of the center cell. Some examples of what happens are shown at the bottom of the previous column. The results are usually very similar to those obtained with random initial conditions.
- History. The fact that despite initial randomness processes like friction can make systems settle down into definite configurations has been the basis for all sorts of engineering throughout history. The rise of statistical mechanics in the late 1800s emphasized the idea of entropy increase and the fundamental tendency for systems to become progressively more disordered as they evolve to thermodynamic equilibrium. Theories were nevertheless developed for a few cases of spontaneous pattern formation-notably in convection, cirrus clouds and ocean waves. When the study of feedback and stability became popular in the 1940s, there were many results about how specific simple fixed or repetitive behaviors in time could emerge despite random input. In the 1950s it was suggested that reaction-diffusion processes might be responsible for spontaneous pattern formation in biology (see page 1012)—and starting in the 1970s such processes were discussed as prime examples of the phenomenon of selforganization. But in their usual form, they yield essentially only rather simple repetitive patterns. Ever since around 1900 it tended to be assumed that any fundamental theory of systems with many components must be based on statistical mechanics. But almost all work in the field of statistical mechanics concentrated on systems in or very near thermal equilibrium-in which in a sense there is almost complete disorder. In the 1970s there began to be more discussion of phenomena far from equilibrium, although typically it got no further than to consider how external forces could lead to reaction-diffusion-like phenomena. My own work on cellular

automata in 1981 emerged in part from thinking about self-gravitating systems (see page 880) where it seemed conceivable that there might be very basic rules quite different from those usually studied in statistical mechanics. And when I first generated pictures of the behavior of arbitrary cellular automaton rules, what struck me most was the order that emerged even from random initial conditions. But while it was immediately clear that most cellular automata do not have the kind of reversible underlying rules assumed in traditional statistical mechanics, it still seemed initially very surprising that their overall behavior could be so elaborate—and so far from the complete orderlessness one might expect on the basis of traditional ideas of entropy maximization.

#### Four Classes of Behavior

- **Different runs.** The qualitative behavior seen with a given cellular automaton rule will normally look exactly the same for essentially all different large random initial conditions—just as it does for different parts of a single initial condition. And as discussed on page 597 any obvious differences could in effect be thought of as revealing deviations from randomness in the initial conditions.
- Page 232 · Elementary rules. The examples shown have rule numbers n for which IntegerDigits[n, 2, 8] matches  $\{-, i_-, -, j_-, i_-, -, j_-, 0\}$ .
- Page 235 · States of matter. As suggested by pages 944 and 1193, working out whether a particular substance at a particular temperature will be a solid, liquid or gas may in fact be computationally comparable in difficulty to working out what class of behavior a particular cellular automaton will exhibit.
- Page 235 · Class 4 rules. Other examples of class 4 totalistic rules with *k* = *3* colors include 357 (page 282), 438, 600, 792, 924, 1038, 1041, 1086, 1329 (page 282), 1572, 1599 (see page 70), 1635 (see page 67), 1662, 1815 (page 236), 2007 (page 237) and 2049 (see page 68).
- **Frequencies of classes.** The pie charts below show results for 1D totalistic cellular automata with *k* colors and range *r*. Class 3 tends to become more common as the number of elements in the rule increases because as soon as any of these elements yield class 3 behavior, that behavior dominates the system.

![](Images/_page_963_Picture_8.jpeg)

![](Images/_page_963_Picture_9.jpeg)

![](Images/_page_963_Picture_10.jpeg)

![](Images/_page_963_Picture_11.jpeg)

- History. I discovered the classification scheme for cellular automata described here late in 1983, and announced it in January 1984. Much work has been done by me and others on ways to make the classification scheme precise. The notion that class 4 can be viewed as intermediate between class 2 and class 3 was studied particularly by Christopher Langton, Wentian Li and Norman Packard in 1986 for ordinary cellular automata, by Hyman Hartman in 1985 for probabilistic cellular automata and by Hugues Chaté and Paul Manneville in 1990 for continuous cellular automata.
- Subclasses within class 4. Different class 4 systems can show localized structures with strikingly similar forms, and this may allow subclasses within class 4 to be identified. In addition, class 4 systems show varying levels of activity, and it is possible that there may be discrete transitions—perhaps analogous to percolation—that can be used to define boundaries between subclasses.
- Page 240 · Undecidability. Almost any definite procedure for determining the class of a particular rule will have the feature that in borderline cases it can take arbitrarily long, often formally showing undecidability, as discussed on page 1138. (An example would be a test for class 1 based on checking that no initial pattern of any size can survive. Including probabilities can help, but there are still always borderline cases and potential undecidability.)
- Page 244 · Continuous cellular automata. In ordinary cellular automata, going from one rule to the next in a sequence involves some discrete change. But in continuous cellular automata, the parameters of the rule can be varied smoothly. Nevertheless, it still turns out that there are discrete transitions in the overall behavior that is produced. In fact, there is often a complicated set of transitions that depends more on the digit sequence of the parameter than its size. And between these transitions there are usually ranges of parameter values that yield definite class 4 behavior. (Compare page 922.)
- **Nearby cellular automaton rules.** In a range *r* cellular automaton the new color of a particular cell depends only on cells at most a distance *r* away. One can make an equivalent cellular automaton of larger range by having a rule in which cells at distance more than *r* have no effect. One can then define nearby cellular automata to be those where the differences in the rule involve only cells close to the edge of the range. With larger and larger ranges one can then construct closer approximations to continuous sequences of cellular automata.
- 2D class 4 cellular automata. No 5- or 9-neighbor totalistic rules nor 5-neighbor outer totalistic ones appear to yield

class 4 behavior with a white background. But among 9neighbor outer totalistic rules there are examples with codes 224 (Game of Life), 226, 4320 (sometimes called HighLife), 5344, 6248, 6752, 6754 and 8416, etc. It turns out that the simplest moving structures are the same in codes 224, 226 and 4320

■ Page 249 · Game of Life. Invented by John Conway around 1970 (see page 877), the Life 2D cellular automaton has been much studied in recreational computing, and as described on page 964 many localized structures in it have been identified. Each step in its evolution can be implemented using

```
LifeStep[a_List] :=
  MapThread[If[#1 == 1 && #2 == 4 || #2 == 3, 1, 0] &,
    {a, Sum[RotateLeft[a, {i, j}], {i, -1, 1}, {j, -1, 1}]}, 2]
```

A more efficient implementation can be obtained by operating not on a complete array of black and white cells but rather just on a list of positions of black cells. With this setup, each step then corresponds to

```
LifeSten[list 1:=
  With[{p = Flatten[Array[List, {3, 3}, -1], 1]},
     With[{u = Split[Sort[Flatten[Outer[Plus, list, p, 1], 1]]]},
       Union[Cases[u, {x_-, _-, _-} \rightarrow x],
         Intersection[Cases[u, \{x_-, \_, \_, \_\} \rightarrow x], list]]]]
```

(A still more efficient implementation is based on finding runs of length 3 and 4 in Sort[u].)

■ 3D class 4 rules. With a cubic lattice of the type shown on page 183, and with updating rules of the form

```
LifeStep3D[\{p_-, q_-, r_-\}, a_List] := MapThread[If[
 #1 == 1 \&\&p \le #2 \le q \parallel #2 == r, 1, 0] \&, \{a, Sum[RotateLeft[
  a, {i, j, k}], {i, -1, 1}, {j, -1, 1}, {k, -1, 1}]-a}, 3]
```

Carter Bays discovered between 1986 and 1990 the three examples {5, 7, 6}, {4, 5, 5}, and {5, 6, 5}. The pictures below show successive steps in the evolution of a moving structure in the second of these rules.

![](Images/_page_964_Picture_11.jpeg)

Random initial conditions in other systems. Whenever the initial conditions for a system can involve an infinite sequence of elements these elements can potentially be chosen at random. In systems like mobile automata and Turing machines the colors of initial cells can be random, but the active cell must start at a definite location, and depending on the behavior only a limited region of initial cells near this location may ever be sampled. Ordinary substitution systems can operate on infinite sequences of elements chosen at random. Sequential substitution systems, however, rely on scanning limited sequences of elements, and so cannot readily be given infinite random initial conditions. The same is true of ordinary and cyclic tag systems. Systems based on continuous numbers involve infinite sequences of digits which can readily be chosen at random (see page 154). But systems based on integers (including register machines) always deal with finite sequences of digits, for which there is no unique definition of randomness. (See however the discussion of number representations on page 1070.) Random networks (see pages 963 and 1038) can be used to provide random initial conditions for network systems. Multiway systems cannot meaningfully be given infinite random initial conditions since these would typically lead to an infinite number of possible states. Systems based on constraints do not have initial conditions. (See also page 920.)

#### Sensitivity to Initial Conditions

■ Page 251 · Properties. In rule 126, the outer edges of the region of change always expand by exactly one cell per step. The same is true of the right-hand edge in rule 30—though the left-hand edge in this case expands only about 0.2428 cells on average per step. In rule 22, both edges expand about 0.7660 cells on average per step.

The motion of the right-hand edge in rule 30 can be understood by noting that with this rule the color of a particular cell will always change if the color of the cell to its left is changed on the previous step (see page 601). Nothing as simple is true for the left-hand edge, and indeed this seems to execute an essentially random walk-with an average motion of about 0.2428 cells per step. Note that in the approximation that the colors of all cells in the pattern are assumed completely independent and random there should be motion by 0.25 cells per step. Curiously, as discussed on page 871, the region of non-repetitive behavior in evolution from a single black cell according to rule 30 seems to grow at a similar but not identical rate of about 0.252 cells per step. (For rule 45, the left-hand edge of the difference pattern moves about 0.1724 cells per step; for rule 54 both edges move about 0.553 cells per step.)

■ Difference patterns. The maximum rate at which a region of change can grow is determined by the range of the underlying cellular automaton rule. If the rule involves up to r nearest neighbors, then at each step a change in the color of a given cell can affect cells up to r away—so that the edge of the region of change can move by r cells.

For most class 3 rules, once one is inside the region of change, the colors of cells usually become essentially uncorrelated. However, for additive rules the pattern of differences is just exactly the pattern that would be obtained by evolution from an initial condition consisting only of the changes made. In general the pattern of probabilities for changes can be thought of as being somewhat like a Green's function in mathematical physics-though the nonadditivity of most cellular automata makes this analogy less useful. (Note that the pattern of differences between two initial conditions in a rule with k possible colors can always be reproduced by looking at the evolution from a single initial condition of a suitable rule with 2 k colors.) In 2D class 3 cellular automata, the region of change usually ends up having a roughly circular shape—a result presumably related to the Central Limit Theorem (see page 976).

For any additive or partially additive class 3 cellular automaton (such as rule 90 or rule 30) any change in initial conditions will always lead to expanding differences. But in other rules it sometimes may not. And thus, for example, in rule 22, changing the color of a single cell has no effect after even one step if the cell has a me block on either side. But while there are a few other initial conditions for which differences can die out after several steps most forms of averaging will say that the majority of initial conditions lead to growing patterns of differences.

■ Lyapunov exponents. If one thinks of cells to the right of a point in a 1D cellular automaton as being like digits in a real number, then linear growth in the region of differences associated with a change further to the right is analogous to the exponentially sensitive dependence on initial conditions shown on page 155. The speed at which the region of differences expands in the cellular automaton can thus be thought of as giving a Lyapunov exponent (see page 921) that characterizes instability in the system.

#### Systems of Limited Size and Class 2 Behavior

■ Page 255 · Cyclic addition. After t steps, the dot will be at position Mod[mt, n] where n is the total number of positions, and m is the number of positions moved at each step. The repetition period is given by n/GCD[m, n]. The picture on page 613 shows the values of *m* and *n* for which this is equal to n.

An alternative interpretation of the system discussed here involves arranging the possible positions in a circle, so that at each step the dot goes a fraction m/n of the way around the circle. The repetition period is maximal when m/n is a fraction in lowest terms. The picture below shows the repetition periods as a function of the numerical size of the quantity m/n.

![](Images/_page_965_Figure_8.jpeg)

■ Page 257 · Cyclic multiplication. With multiplication by k at each step the dot will be at position  $Mod[k^t, n]$  after t steps. If k and n have no factors in common, there will be a t for which  $Mod[k^t, n] = 1$ , so that the dot returns to position 1. The smallest such t is given by MultiplicativeOrder[k, n], which always divides EulerPhi[n] (see page 1093), and has a value between Log[k, n] and n-1, with the upper limit being attained only if n is prime. (This value is related to the repetition period for the digit sequence of 1/n in base k, as discussed on page 912). When GCD[k, n] = 1 the dot can never visit position 0. But if  $n = k^s$ , the dot reaches 0 after s steps, and then stays there. In general, the dot will visit position  $m = k \cdot IntegerExponent[n, k] every MultiplicativeOrder[k, n/m]$ 

■ Page 260 · Maximum periods. A cellular automaton with ncells and k colors has  $k^n$  possible states, but if the system has cyclic boundary conditions, then the maximum repetition period is smaller than  $k^n$ . The reason is that different states of the cellular automaton have different symmetry properties, and thus cannot be on the same cycle. In particular, if a state of a cellular automaton has a certain spatial period, given by the minimum positive *m* for which *RotateLeft[list, m] == list*, then this state can never evolve to one with a larger spatial period. The number of states with spatial period m is given by

```
s[m_{-}, k_{-}] :=
     k^m - Apply[Plus, Map[s[#, k] &, Drop[Divisors[m], -1]]]
or equivalently
   s[m, k] := Applv[Plus]
       (MoebiusMu[m/#]k<sup>#</sup> &)[Divisors[m]]]
```

In a cellular automaton with a total of n cells, the maximum possible repetition period is thus s[n, k]. For k = 2, the maximum periods for *n* up to 10 are: {2, 2, 6, 12, 30, 54, 126, 240, 504, 990}. In all cases, s[n, k] is divisible by n. For prime n, s[n, k] is  $k^n - k$ . For large n, s[n, k] oscillates between about  $k^n - k^{n/2}$  and  $k^n - k$ . (See page 963.)

■ Additive cellular automata. In the case of additive rules such as rule 90 and rule 60, a mathematical analysis of the repetition periods can be given (as done by Olivier Martin, Andrew Odlyzko and me in 1983). One starts by converting the list of cell colors at each step to a polynomial FromDigits[list, x]. Then for the case of rule 60 with n cells and cyclic boundary conditions, the state obtained after tsteps is given by

PolynomialMod[ $(1+x)^t z$ ,  $\{x^n - 1, 2\}$ ]

where z is the polynomial representing the initial state, and z = 1 for a single black cell in the first position. The state z = 1evolves after one step to the state z = 1 + x, and for odd n this latter state always eventually appears again. Using the result that  $1 + x^{2^m} = (1 + x)^{2^m}$  modulo 2 for any m, one then finds that the repetition period always divides the quantity  $p[n] = 2 ^MultiplicativeOrder[2, n] - 1$ , which in turn is at most  $2^{n-1}$  - 1. The actual periods are often smaller than p[n], with the following ratios occurring:

|       |   |   | - 1 |    |    | 29  |       |    |   |         |
|-------|---|---|-----|----|----|-----|-------|----|---|---------|
| ratio | 3 | 5 | 27  | 41 | 19 | 565 | 21255 | 25 | 3 | 1266205 |

There appears to be no case for n > 5 where the period achieves the absolute maximum  $2^{n-1}$  – 1.

In the case of rule 90 a similar analysis can be given, with the 1+x used at each step replaced by 1/x+x. And now the repetition period for odd *n* divides

 $q[n] = 2 \cdot MultiplicativeOrder[2, n, {1, -1}] - 1$ 

The exponent here always lies between Log[k, n] and (n-1)/2, with the upper bound being attained only if n is prime. Unlike for the case of rule 60, the period is usually equal to q[n] (and is assumed so for the picture on page 260), with the first exception occurring at n = 37.

- Rules 30 and 45. Maximum periods are often achieved with initial conditions consisting of a single black cell. Particularly for rule 30, however, there are quite a few exceptions. For n = 13, for example, the maximum period is 832 but the period with a single black cell is 260. For rule 45, the maximum possible period discussed above is achieved for n = 9, but does not appear to be achieved for any larger n. (See page 962.)
- **Comparison of rules.** Rules 45, 30 and 60, together with their conjugates and reflections, yield the longest repetition periods of all elementary rules (see page 1087). The picture below compares their periods as a function of n.

![](Images/_page_966_Figure_12.jpeg)

■ Implementing boundary conditions. In the bitwise representation discussed on page 865, 0's outside of a width n can be implemented by applying  $BitAnd[a, 2^n - 1]$  at each step. Cyclic boundary conditions can be implemented efficiently in assembler on computers that support cyclic shift instructions.

#### Randomness in Class 3 Systems

- Page 263 · Rule 22. Randomness is obtained with initial conditions consisting of two black squares 4 m positions apart for any  $m \ge 2$ . The base 2 digit sequences for 19, 25, 37, 39, 41, 45, 47, 51, 57, 61, ... also give initial conditions that yield randomness. Despite its overall randomness there are some regularities in the pattern shown at the bottom of the page. The overall density of black cells is not 1/2 but is instead approximately 0.35, just as for random initial conditions. And if one looks at the center cell in the pattern one finds that it is never black on two successive steps, and the probability for white to follow white is about twice the probability for black to follow white. There is also a region of repetitive behavior on each side of the pattern; the random part in the middle expands at about 0.766 cells per step—the same speed that we found on page 949 that changes spread in this rule.
- Rule 225. With initial conditions consisting of a single black cell, this class 3 rule yields a regular nested pattern, as shown on page 58. But with the initial condition \_\_\_\_, it yields the much more complicated pattern shown below. With a background consisting of repetitions of the block ■, insertion of a single initial white cell yields a largely random pattern that expands by one cell per step. Rule 225 can be expressed as  $\neg p \supseteq (q \lor r)$ .

![](Images/_page_966_Figure_17.jpeg)

■ Rule 94. With appropriate initial conditions this class 2 rule can yield both nested and random behavior, as shown below.

![](Images/_page_966_Figure_19.jpeg)

- Rule 218. If pairs of adjacent black cells appear anywhere in its initial conditions this class 2 rule gives uniform black, but if none do it gives a rule 90 nested pattern.
- **Additive rules.** Of the 256 elementary cellular automata 8 are additive: {0, 60, 90, 102, 150, 170, 204, 240}. All of these are either trivial or essentially equivalent to rules 90 or 150.

Of all  $k^{k^{2r+1}}$  rules with k colors and range r it turns out that there are always exactly  $k^{2r+1}$  additive ones—each obtained by taking the cells in the neighborhood and adding them modulo k with weights between 0 and k-1. As discussed on page 955, any rule based on addition modulo k must yield a nested pattern, and it therefore follows that any rule that is additive must give a nested pattern, as in the examples below. (See also page 870.)

![](Images/_page_967_Picture_4.jpeg)

Note that each step in the evolution of any additive cellular automaton can be computed as

Mod[ListCorrelate[w, list, Ceiling[Length[w]/2]], k]

(See page 1087 for a discussion of partial additivity.)

■ **Page 264** • **Generalized additivity.** In general what it means for a system to be additive is that some addition operation  $\theta$  can be used to combine any set of evolution histories to yield another possible evolution history. If  $\phi$  is the rule for the system, this then requires for any states u and v the distributive property

 $\phi[u \oplus v] = \phi[u] \oplus \phi[v]$ 

(In mathematical terms this is equivalent to the statement that  $\phi$  is conjugate to itself under the action of  $\theta$ —or alternatively that  $\phi$  defines a homomorphism with respect to the  $\theta$  operation.) In the usual case,  $u \theta v$  is just Mod[u+v,k], yielding say for rule 90 the results below.

![](Images/_page_967_Picture_11.jpeg)

![](Images/_page_967_Picture_12.jpeg)

![](Images/_page_967_Picture_13.jpeg)

![](Images/_page_967_Picture_14.jpeg)

But it turns out that some elementary rules show additivity with respect to other addition operations. An example as shown below is rule 250 with  $u \oplus v$  taken as Max[u, v] (Or).

![](Images/_page_967_Picture_16.jpeg)

![](Images/_page_967_Picture_17.jpeg)

![](Images/_page_967_Picture_18.jpeg)

![](Images/_page_967_Picture_19.jpeg)

If a system is additive it means that one can work out how the system will behave from any initial condition just by combining the patterns ("Green's functions") obtained from certain basic initial conditions—say ones containing a single black cell. To get all the familiar properties of additivity one needs an addition operation that is associative (Flat) and commutative (Orderless), and has an identity element (white or 0 in the cases above)—so that it defines a commutative monoid. (Usually it is also convenient to be able to get all possible elements by combining a small number of basic generator elements.)

The inequivalent commutative monoids with up to k = 4 colors are (in total there are 1, 2, 5, 19, 78, 421, 2637, ... such objects):

![](Images/_page_967_Picture_22.jpeg)

For k = 2, r = 1 the number of rules additive with respect to these is respectively: {8, 9}; for k = 2, r = 2: {32, 33}; for k = 3,

r = 1: {28, 27, 35, 244, 28}; for k = 4, r = 1: {1001, 65, 540, 577, 126, 4225, 540, 9065, 757, 408, 65, 133, 862, 224, 72, 72, 91, 4096, 64}

It turns out to be possible to show that any rules  $\phi$  additive with respect to some addition operation  $\theta$  must work by applying that operation to values associated with cells in their neighborhood. The values are obtained by applying to cells at each position one of the unary operations (endomorphisms)  $\sigma$  that satisfy  $\sigma(a \oplus b) = \sigma(a) \oplus \sigma(b)$  for individual cell values a and b. (For Xor, there are 2 possible  $\sigma$ , while for Or there are 3.)

The basic examples are then rules of the form  $RotateLeft[a] \oplus RotateRight[a]$ —analogs of rule 90, but with other addition operations (compare page 886). The  $\sigma$  can be used to give analogs of the weights that appear in the note above. And rules that involve more than two cells can be obtained by having several instances of  $\theta$ —which can always be flattened. But in all cases the general results for associative rules on page 956 show that the patterns obtained must be at most nested.

If instead of an ordinary cellular automaton with a limited number of possible colors one considers a system in which every cell can have any integer value then additivity with respect to ordinary addition becomes just traditional linearity. And the only way to achieve this is to have a rule in which the new value of a cell is given by a linear form such as ax + by. If the values of cells are allowed to be any real number then

linear forms such as ax + by again yield additivity with respect to ordinary addition. But in general one can apply to each cell value any function  $\sigma$  that obeys the so-called Cauchy functional equation  $\sigma(x + y) = \sigma(x) + \sigma(y)$ . If  $\sigma(x)$  is required to be continuous, then the only form it can have is cx. But if one allows  $\sigma$  to be discontinuous then there can be some other exotic possibilities. It is inevitable that within any rationally related set of values x one must have  $\sigma[x] = cx$  with fixed c. But if one assumes the Axiom of Choice then in principle it becomes possible to construct  $\sigma[x]$  which have different c for different sets of x values. (Note however that I do not believe that such  $\sigma$  could ever actually be constructed in any explicit way by any real computational system-or in fact by any system in our universe.)

In general ⊕ need not be ordinary addition, but can be any operation that defines a commutative monoid—including an infinite one. An example is ordinary numbers modulo an irrational. And indeed a cellular automaton whose rule is based on  $Mod[x + y, \pi]$  will show additivity with respect to this operation (see page 922). If  $\theta$  has an inverse, so that it defines a group, then the only continuous (Lie group) examples turn out to be combinations of ordinary addition and modular addition (the group U(1)). This assumes, however, that the underlying cellular automaton has discrete cells. But one can also imagine setting up systems whose states are continuous functions of position.  $\phi$  then defines a mapping from one such function to another. To be analogous to cellular automata one can then require this mapping to be local, in which case if it is continuous it must be just a linear differential operator involving Derivative[n]—and at some level its behavior must be fairly simple. (Compare page 161.)

■ Probabilistic estimates. One way to get estimates for density and other properties of class 3 cellular automata is to make the assumption that the color of each cell at each step is completely random. And with this assumption, if the overall density of black cells at a particular step is p, then each cell at that step should independently have probability p to be black. This means that for example the probability to find a black cell followed by two white cells is  $p(1-p)^2$ . And in general, the probabilities for all 8 possible combinations of 3 cells are given by

```
probs = Apply[Times, Table[IntegerDigits[8 - i, 2, 3],
           \{i, 8\}\} /. \{1 \rightarrow p, 0 \rightarrow 1 - p\}, \{1\}
```

In terms of these probabilities the density at the next step in the evolution of cellular automaton with rule number m is then given by

Simplify[probs . IntegerDigits[m, 2, 8]]

For rule 22, for example, this means that if the density at a particular step is p, then the density on the next step should be  $3p(1-p)^2$ , and the densities on subsequent steps should be obtained by iterating this function. (At least for the 256 elementary cellular automata this iterated map is never chaotic.) The stable density after many steps is then given by Solve  $[3p(1-p)^2 = p, p]$ , so that  $p \to 1 - 1/\sqrt{3}$ approximately 0.42. The actual density for rule 22 is however 0.35095. The reason for the discrepancy is that the probabilities for different cells are in fact correlated. One can systematically include more such correlations by looking at more steps of evolution at once. For two steps, one must consider probabilities for all 32 combinations of 5 cells, and for rule 22 the function becomes  $p(1-p)^2(2+3p^2)$ , yielding density 0.35012; for three steps it is  $p(1-p)^2(p^4-18p^3+41p^2-22p+6)$  yielding density 0.379. The plot below shows what happens with more steps: the results seem to converge slowly to the exact result indicated by the gray line.

![](Images/_page_968_Figure_9.jpeg)

![](Images/_page_968_Figure_10.jpeg)

(For rules 90 and 30 the functions obtained after one step are respectively 2p(1-p) and  $p(2p^2-5p+3)$ , both of which turn out to imply correct final densities of 1/2).

Probabilistic approximation schemes like this are often used in statistical physics under the name of mean field theories. In general, such approximations tend to work better for systems in larger numbers of dimensions, where correlations tend to be less important.

Probabilistic estimates can also be used for other quantities, such as growth rates of difference patterns (see page 949). In most cases, however, buildup of correlations tends to prevent systematic improvement of such approximations.

■ **Density in rule 90.** From the superposition principle above and the number of black cells at step t in a pattern starting from a single black cell (see page 870) one can compute the density after t steps in the evolution of rule 90 with initial conditions of density *p* to be (see also page 602)

$$1/2(1-(1-2p))^{2}$$

■ Densities in other rules. The pictures below show how the densities on successive steps depend on the initial density. Densities are indicated by gray levels. Initial densities are shown across each picture. Successive steps are shown down the page. Rule 236 is class 2, and the density retains a memory of its initial value. But in the class 3 rules 126 and 30, the densities converge quickly to a fixed value.

Page 339 shows a cellular automaton with very different behavior

![](Images/_page_969_Figure_2.jpeg)

■ Density oscillations in rule 73. Although there are always some fluctuations, most rules yield densities that converge more or less uniformly to their final values. One exception is rule 73, which yields densities that continue to oscillate with a period of 3 steps forever. The origin of this phenomenon is that with completely random initial conditions rule 73 evolves to a collection of independent regions, as in the picture below, and many of these regions contain patterns that repeat with period 3. The boundaries between regions come from blocks of even numbers of black cells in the initial conditions, and if one does not allow any such blocks, the density oscillations no longer occur. (See also page 699.)

![](Images/_page_969_Picture_4.jpeg)

#### **Special Initial Conditions**

■ **Page 267 · Repeating blocks.** The discussion in the main text is mostly about repetition strictly every p steps, and no sooner. (If a system repeats for example every 3 steps, then it is inevitable that it will also repeat in the same way every 6, 9, 12, 15, etc. steps.) Finding configurations in a 1D cellular automaton that repeat with a particular period is equivalent to satisfying the kind of constraints we discussed on page 211. And as described there, if such constraints can be satisfied at all, then it must be possible to satisfy them with a configuration that consists of a repetition of identical blocks. Indeed, for period p, the length of blocks required is at most  $2^{2p}$  (or  $2^{2pr}$  for range r rules).

![](Images/_page_969_Picture_7.jpeg)

The pictures at the bottom of the previous column summarize which periods can be obtained with various rules. Periods from 1 to 15 are represented by different rows, with period 1 at the bottom. Within each row a gray bar indicates that a particular period can be obtained with blocks of some length. The black dots indicate specific block sizes up to 25 that work.

In rule 90 (as well as other additive rules such as 60 and 150) any period can occur, but all configurations that repeat must consist of a sequence of identical blocks. For periods up to 10, examples of such blocks in rule 90 are given by the digits of

{0, 40, 24, 2176, 107904, 640, 96, 8421376, 7566031296234863392, 15561286137}

For period 1 the possible blocks are  $\square$  and  $\blacksquare\square$ ; for period 2  $\blacksquare$  and  $\blacksquare$ . The total number of configurations in rule 90 that repeat with any period that divides p is always  $4^p$ .

Rules 30 and 45 (as well as other one-sided additive rules) also have the property that all configurations that repeat must consist of a sequence of identical blocks. The total number of configurations in rule 30 that repeat with periods that divide 1 through 10 are {3, 3, 15, 10, 8, 99, 18, 14, 30, 163}. In general for one-sided additive rules the number of such configurations increases for large p like  $k^{h_{tx}p}$ , where  $h_{tx}$  is the spacetime entropy of page 960. (This is the analog of a standard result in dynamical systems theory about expansive homeomorphisms.)

For rules that do not show at least one-sided additivity there can be an infinite number of configurations that repeat with a given period. To find them one considers all possible blocks of length 2pr+1 and picks out those that after p steps evolve so that their center cell ends up the same color as it was originally. The possible configurations that repeat with period p then correspond to the finite complement language (see page 958) obtained by stringing together these blocks. For p = 2, rule 18 leaves 20 of the 32 possible length 5 blocks invariant, but these blocks can only be strung together to yield repetitions of  $\{a, b, 0, 0\}$ , where now a and b are not fixed, but in every case can each be either  $\{1\}$  or  $\{0, 1\}$ .

(See also page 700.)

- Localized structures. See pages 281 and 1118.
- 2D cellular automata. As expected from the discussion of constraints on page 942, the problem of finding repeating configurations is much more difficult in two dimensions than in one dimension. Thus for example unlike in 1D there is no guarantee in 2D that among repeating configurations of a particular period there is necessarily one that consists just of a repetitive array of fixed blocks. Indeed, as discussed on page 1139, it is in a sense possible that the only repeating configurations are arbitrarily complex. Note that if one

considers configurations in 2D that consist only of infinitely long stripes, then the problem reduces again to the 1D case. (See also page 349.)

■ Systems based on numbers. An iterated map of the kind discussed on page 150 with rule  $x \rightarrow Mod[ax, 1]$  (with rational a) will yield repetitive behavior when its initial condition is a rational number. The same is true for higherdimensional generalizations such as so-called Anosov maps  $\{x, y\} \rightarrow Mod[m.\{x, y\}, 1]$ . The continued fraction map  $x \rightarrow Mod[1/x, 1]$  discussed on page 914 becomes repetitive whenever its initial condition is a solution to a quadratic equation.

For a map  $x \rightarrow f[x]$  where f[x] is a polynomial such as  $a \times (1-x)$  the real initial conditions that yield period p are

Select[x /. Solve[Nest[f, x, p] == x, x], Im[#] == 0 &]For  $x \rightarrow ax(1-x)$  the results usually cannot be expressed in terms of explicit radicals beyond period 2. (See page 961.)

■ Sarkovskii's theorem. For any iterated map based on a continuous function such as a polynomial it was shown in 1962 that if an initial condition exists that gives period 3, then other initial conditions must exist that give any other period. In general, if a period m is possible then so must all periods nfor which  $p = \{m, n\}$  satisfies

OrderedQ[(Transpose[If[MemberQ[p/#, 1], Map[Reverse, {p/#, #}], {#, p/#}]] &)[2^IntegerExponent[p, 2]]]

Extensions of this to other types of systems seem difficult to find, but it is conceivable that when viewed as continuous mappings on a Cantor set (see page 869) at least some cellular automata might exhibit similar properties.

- Page 269 · Rule emulations. See pages 702 and 1118.
- **Renormalization group.** The notion of studying systems by seeing the effect of changing the scale on which one looks at them has been widely used in physics since about 1970, and there is some analogy between this and what I do here with cellular automata. In the lattice version in physics one typically considers what happens to averages over all possible configurations of a system if one does a so-called blocking transformation that replaces blocks of elements by individual elements. And what one finds is that in certain cases—notably in connection with nesting at critical points associated with phase transitions (see page 981)-certain averages turn out to be the same as one would get if one did no blocking but just changed parameters ("coupling constants") in the underlying rules that specify the weighting of different configurations. How such effective parameters change with scale is then governed by so-called renormalization group differential equations. And when one

looks at large scales the versions of these equations that arise in practice essentially always show fixed points, whose properties do not depend much on details of the equationsleading to certain universal results across many different underlying systems (see page 983).

What I do in the main text can be thought of as carrying out blocking transformations on cellular automata. But only rarely do such transformations yield cellular automata whose rules are of the same type one started from. And in most cases such rules will not suffice even if one takes averages. And indeed, so far as I can tell, only in those cases where there is fairly simple nested behavior is any direct analog of renormalization group methods useful. (See page 989.)

- Page 271 · Self-similarity of additive rules. The fact that rule 90 can emulate itself can be seen fairly easily from a symbolic description of the rule. Given three cells  $\{a_1, a_2, a_3\}$  the rule specifies that the new value of the center cell will be  $Mod[a_1 + a_3, 2]$ . But given  $\{a_1, 0, a_2, 0, a_3, 0\}$  the value after one step is  $\{Mod[a_1 + a_2, 2], 0, Mod[a_2 + a_3, 2], 0\}$  and after two steps is again  $\{Mod[a_1 + a_3, 2], 0\}$ . It turns out that this argument generalizes (by interspersing k - 1 0's and going for k steps) to any additive rule based on reduction modulo k (see page 952) so long as k is prime. And it follows that in this case the pattern generated after a certain number of steps from a single non-white cell will always be the same as one gets by going k times that number of steps and then keeping only every kth row and column. And this immediately implies that the pattern must always have a nested form. If k is not prime the pattern is no longer strictly invariant with respect to keeping only every kth row and column—but is in effect still a superposition of patterns with this property for factor of k. (Compare page 870.)
- Fractal dimensions. The total number of nonzero cells in the first t rows of the pattern generated by the evolution of an additive cellular automaton with k colors and weights w (see page 952) from a single initial 1 can be found using

 $g[w_-, k_-, t_-] := Apply[Plus, Sign[NestList[Mod[$ ListCorrelate[w, #, {-1, 1}, 0], k] &, {1}, t-1]], {0, 1}]

The fractal dimension of this pattern is then given by the large m limit of

 $Log[k, g[w, k, k^{m+1}]/g[w, k, k^{m}]]$ 

When k is prime it turns out that this can be computed as d[w\_, k\_:2]:=Log[k, Max[Abs[Eigenvalues[With]  $\{s = Length[w] - 1\}, (Map[Function[u, Map[Count[u, #] &,$ #1]], Map[Flatten[Map[Partition[Take[#, k+s-1], s, 1] &,NestList[Mod[ListConvolve[w, #], k] &, #, k - 1]], 1] &,  $Map[Flatten[Map[{Table[0, {k-1}], \#} \&, Append[\#,$ 0]]] &, #]]] &)[Array[IntegerDigits[#, k, s] &, k<sup>s</sup> - 1]]]]]]

For rule 90 one gets  $d[\{1, 0, 1\}] = Log[2, 3] \approx 1.58$ . For rule 150  $d[\{1, 1, 1\}] = Log[2, 1 + \sqrt{5}] \approx 1.69$ . (See page 58.) For the other rules on page 952:

```
d[\{1, 1, 0, 1, 0\}] = \\ Log[2, Root[4 + 2 \# - 2 \#^2 - 3 \#^3 + \#^4 \&, 2]] \simeq 1.72
d[\{1, 1, 0, 1, 1\}] = \\ Log[2, Root[-4 + 4 \# + \#^2 - 4 \#^3 + \#^4 \&, 2]] \simeq 1.8
Other cases include (see page 870):
d[\{1, 0, 1\}, k] = 1 + Log[k, (k + 1)/2]
d[\{1, 1, 1\}, 3] = Log[3, 6] \simeq 1.63
```

d[{1, 1, 1}, 7] = Log[7, Root[-27136 + 23280#-

 $d[\{1, 1, 1\}, 5] = Log[5, 19] \approx 1.83$ 

■ General associative rules. With a cellular automaton rule in which the new color of a cell is given by  $f[a_1, a_2]$  (compare page 886) it turns out that the pattern generated by evolution from a single non-white cell is always nested if the function f has the property of being associative or Flat. In fact, for a system involving k colors the pattern produced will always be essentially just one of the patterns obtained from an additive rule with k or less colors. In general, the pattern produced by evolution for t steps is given by

 $7288 \, \#^2 + 1008 \, \#^3 - 59 \, \#^4 + \#^5 \, \&, \, 1]] \simeq 1.85$ 

```
NestList[
    Inner[f, Prepend[#, 0], Append[#, 0], List] &, {a}, t]

so that the first few steps yield
    {a}
    {f[0, a], f[a, 0]}
    {f[0, f[0, a]], f[f[0, a], f[a, 0]], f[f[a, 0], 0]}
    {f[0, f[0, f[0, a]]], f[f[0, f[0, a]], f[f[f[a, 0], 0]],
    f[f[f[0, a], f[a, 0]], f[f[a, 0], 0]], f[f[f[a, 0], 0], 0]}
```

If f is Flat, however, then the last two lines here become {f[0, 0, a], f[0, a, a, 0], f[a, 0, 0]} {f[0, 0, 0, a], f[0, 0, a, 0, a, a, 0], f[0, a, a, 0, a, 0, 0]}

and in general the number of a's that appear in a particular element is given as in Pascal's triangle by a binomial coefficient. If f is commutative (Orderless) then all that can ever matter to the value of an element is its number of a's. Yet since there are a finite set of possible values for each element it immediately follows that the resulting pattern must be essentially Pascal's triangle modulo some integer. And even if f is not commutative, the same result will hold so long as f[0, a] = a and f[a, 0] = a—since then any element can be reduced to f[a, a, a, ...]. The result can also be generalized to cellular automata with basic rules involving more than two elements—since if f is Flat,  $f[a_1, a_2, a_3]$  is always just  $f[f[a_1, a_2], a_3]$ .

If one starts from more than a single non- $\theta$  element, then it is still true that a nested pattern will be produced if f is both

associative and commutative. And from the discussion on page 952 this means that any rule that shows generalized additivity must always yield a nested pattern. But if f is not commutative, then even if it is associative, non-nested patterns can be produced. And indeed page 887 shows an example of this based on the non-commutative group  $S_3$ . (In general f can correspond to an almost arbitrary semigroup, but with a single initial element only a cyclic subgroup of it is ever explored.)

- Nesting in rule 45. As illustrated on page 701, starting from a single black cell on a background of repeated ■□ blocks, rule 45 yields a slanted version of the nested rule 90 pattern.
- Uniqueness of patterns. Starting from a particular initial condition, different rules can often yield the same pattern. The picture below shows in sorted order the configurations obtained at each successive step in the evolution of all 256 elementary cellular automata starting from a single black cell. After a large number of steps, between 94 and 105 distinct individual configurations are obtained, together with 143 distinct complete patterns. (Compare page 1186.)

![](Images/_page_971_Figure_11.jpeg)

- **Square root of rule 30.** Although rule 30 cannot apparently be decomposed into other k = 2, r = 1 cellular automata, it can be viewed as the square of the k = 3, r = 1/2 cellular automata with rule numbers 11736, 11739 and 11742.
- Page 272 · Nested initial conditions. The pictures below show patterns generated by rule 90 starting from the nested sequences on page 83. (See page 1091.)

![](Images/_page_971_Picture_14.jpeg)

![](Images/_page_971_Picture_15.jpeg)

![](Images/_page_971_Picture_16.jpeg)

#### The Notion of Attractors

■ Page 275 · Discrete systems. In traditional mathematics mechanical and other systems are assumed continuous, so that for example a pendulum may get exponentially close to

the attractor state where it has stopped, but it will never strictly reach this attractor. In discrete systems like cellular automata, however, there is no problem in explicitly reaching at least simple attractors.

■ Implementation. One can represent a network by a list such as  $\{\{1 \rightarrow 2\}, \{0 \rightarrow 3, 1 \rightarrow 2\}, \{0 \rightarrow 3, 1 \rightarrow 1\}\}$  where each element represents a node whose number corresponds to the position of the element, and for each node there are rules that specify to which nodes arcs with different values lead. Starting with a list of nodes, the nodes reached by following arcs with value a for one step are given by

```
NetStep[net_, i_, a_] :=
  Union[ReplaceList[a, Flatten[net[[i]]]]]
```

A list of values then corresponds to a path in the network starting from any node if

```
Fold[NetStep[net, #1, #2] &,
   Range[Length[net]], list] =!= {}
```

Given a set of sequences of values represented by a particular network, the set obtained after one step of cellular automaton evolution is given by

```
NetCAStep[{k_, r_, rtab_}, net_] := Flatten[
                            Map[Table[\# /. (a\_ \rightarrow s\_) :\rightarrow rtab[[i \ k + a + 1]] \rightarrow k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1) + k^{2r} \ (s - 1)
                                                                                                                                     1 + Mod[ik + a, k^{2r}], \{i, 0, k^{2r} - 1\}] \&, net], 1]
```

where here elementary rule 126 is specified for example by {2, 1, Reverse[IntegerDigits[126, 2, 8]]}. Starting from the set of all possible sequences, as given by

```
AllNet[k_{-}:2] := \{Thread[Range[k] - 1 \rightarrow 1]\}
this then yields for rule 126 the network
```

 $\{\{0\rightarrow 1,\ 1\rightarrow 2\},\ \{1\rightarrow 3,\ 1\rightarrow 4\},\ \{1\rightarrow 1,\ 1\rightarrow 2\},\ \{1\rightarrow 3,\ 0\rightarrow 4\}\}$ It is always possible to find a minimal network that represents a set of sequences. This can be done by first creating a "deterministic" network in which at most one arc of each value comes out of each node, then combining equivalent nodes. The whole procedure can be performed using

```
MinNet[net_, k_: 2] := Module[\{d = DSets[net, k], q, b\},
If[First[d] = != \{\}, AllNet[k], q = ISets[b = Map[Table[
    Position[d, NetStep[net, #, a]][[1, 1]], {a, 0, k - 1}] &, d]];
 DeleteCases[MapIndexed[#2[[2]] - 1 \rightarrow #1 &, Rest[
   Map[Position[q, #][[1, 1]] &, Transpose[Map[#[[Map[
     First, q]]] &, Transpose[b]]], \{2\}]] - 1, \{2\}], \_ \rightarrow 0, \{2\}]]]
DSets[net k : 21:=
  FixedPoint[Union[Flatten[Map[Table[NetStep[net, #, a],
             {a, 0, k - 1}] &, #], 1]] &, {Range[Length[net]]}]
ISets[list_] := FixedPoint[Function[g, Flatten[Map[
 Map[Last, Split[Sort[Transpose[{Map[Position[g, #][[1,
     1] &, list, {2}], Range[Length[list]]}][[#]], First[#1] ==
   First[#2] &], {2}] &, g], 1]], {{1}, Range[2, Length[list]]}]
```

If net has q nodes, then in general MinNet[net] can have as many as  $2^q - 1$  nodes. The form of MinNet given here can take

up to about  $n^2$  steps to generate a result with n nodes; an n Log[n] procedure is known. The result from MinNet for rule 126 is  $\{\{1 \to 3\}, \{0 \to 2, 1 \to 1\}, \{0 \to 2, 1 \to 3\}\}$ .

In general MinNet will yield a network with the property that any allowed sequence of values corresponds to a path which starts from node 1. In the main text, however, the networks allow paths that start at any node. To obtain such trimmed networks one can apply the function

```
TrimNet[net 1:=
 With[{m = Apply[Intersection, Map[FixedPoint[
         Union[#, Flatten[Map[Last, net][#]], {2}]]] &.
        #] &, Map[List, Range[Length[net]]]]],
  net[[m]] /. Table[(a_{-} \rightarrow m[[i]]) \rightarrow a \rightarrow i, \{i, Length[m]\}]]
```

■ Finite automata. The networks discussed in the main text can be viewed as finite automata (also known as finite state machines). Each node in the network corresponds to a state in the automaton, and each arc represents a transition that occurs when a particular value is given as input. NetCAStep above in general produces a non-deterministic finite automaton (NDFA) for which a particular sequence of values does not determine a unique path through the network. MinNet creates an equivalent DFA, then minimizes this. The Myhill-Nerode theorem ensures that a unique minimal DFA can always be found (though to do so is in general a PSPACEcomplete problem).

The total number of distinct minimal finite automata with k = 2 possible labels for each arc grows with the number of nodes as follows: 3, 7, 78, 1388, ... (The simple result  $(n + 1)^{nk}$ based on the number of ways to connect up n nodes is a significant overestimate because of equivalence between automata with different patterns of connections.)

- Regular languages. The set of sequences obtained by following possible paths through a finite network is often called a regular language, and appears in studies of many kinds of systems. (See page 939.)
- Regular expressions. The sequences in a regular language correspond to those that can be matched by Mathematica patterns that use no explicit pattern names. Thus for example {(0/1)...} corresponds to all possible sequences of 0's and 1's, while {1, 1, (1) ..., 0, (0) ...}... corresponds to the sequences that can occur after 2 steps in rule 126 and {(0)..., 1, {0, (0)..., 1, 1}|{1, (1)..., 0}}... to those that can occur after 2 steps in rule 110 (see page 279).
- Generating functions. The sequences in a regular language can be thought of as corresponding to products of noncommuting variables that appear as coefficients in a formal power series expansion of a generating function. A basic result is that for regular languages this generating function

is always rational. (Compare the discussion of entropies below.)

- History. Simple finite automata have implicitly been used in electromechanical machines for over a century. A formal version of them appeared in 1943 in McCulloch-Pitts neural network models. (An earlier analog had appeared in Markov chains.) Intensive work on them in the 1950s (sometimes under the name sequential machines) established many basic properties, including interpretation as regular languages and equivalence to regular expressions. Connections to formal power series and to substitution systems (see page 891) were studied in the 1960s. And with the development of the Unix operating system in the 1970s regular expressions began to be widely used in practical computing in lexical analysis (lex) and text searching (ed and grep). Regular languages also arose in dynamical systems theory in the early 1970s under the name of sofic systems.
- Page 278 · Network properties. The number of nodes and connections at step t > 1 are: rule 108: 8, 13; rule 128: 2t, 2t + 2; rule 132: 2t + 1, 3t + 3; rule 160:  $(t + 1)^2$ , (t + 1)(t + 3); rule 184: 2t, 3t + 1. For rule 126 the first few cases are  $\{(1, 2), (3, 5), (13, 23), (106, 196), (2866, 5474)\}$

and for rule 110 they are {{1, 2}, {5, 9}, {20, 38}, {206, 403}, {1353, 2666}}

The maximum size of network that can possibly be generated after t steps of cellular automaton evolution is  $2^{k^{27t}} - 1$ . For t = 1 the maximum of 15 (with 29 connections) is achieved for 16 out of the 256 possible elementary rules, including 22, 37, 73, 94, 104, 122, 146 and 164. For t = 2, rule 22 gives the largest network, with 280 nodes and 551 arcs. The k = 2, t = 2 totalistic rule with code 20 gives a network with 65535 nodes after just 1 step. Note that rules which yield maximal size networks are in a sense close to allowing all possible sequences. (The shortest excluded block for code 20 is of length 36.)

■ Excluded blocks. As the evolution of a cellular automaton proceeds, the set of sequences that can appear typically shrinks, with progressively more blocks being excluded. In some cases the set of allowed sequences forms a so-called finite complement language (or subshift of finite type) that can be characterized completely just by saying that some finite set of blocks are excluded. But whenever the overall behavior is at all complex, there tend to be an infinite set of blocks excluded, making it necessary to use a network of the kind discussed in the main text. If there are *n* nodes in such a network, then if any blocks are excluded, the shortest one of them must be of length less than *n*. And if there are going to be an infinite number of excluded blocks, there must be additional excluded blocks with lengths

between n and 2n. In rule 126, the lengths of the shortest newly excluded blocks on successive steps are 0, 3, 12, 13, 14, 14, 17, 15. It is common to see such lengths progressively increase, although in principle they can decrease by as much as 2r from one step to the next. (As an example, in rule 54 they decrease from 9 to 7 between steps 4 and 5.)

■ Entropies and dimensions. There are  $2^n$  sequences possible for n cells that are each either black or white. But as we have seen, in most cellular automata not all these sequences can occur except in the initial conditions. The number of sequences  $s_n$  of length n that can actually occur is given by

Apply[Plus, Flatten[MatrixPower[m, n]]] where the adjacency matrix *m* is given by

MapAt[1+# &, Table[0, {Length[net]}, {Length[net]}], Flatten[MapIndexed[{First[#2], Last[#1]} &, net, {2}], 1]]

For rule 32, for example,  $s_n$  turns out to be Fibonacci[n+3], so that for large n it is approximately  $GoldenRatio^n$ . For any rule,  $s_n$  for large n will behave like  $\kappa^n$ , where  $\kappa$  is the largest eigenvalue of m. For rule 126 after 1 step, the characteristic polynomial for m is  $\kappa^3 - 2\kappa^2 + \kappa - 1$ , giving  $\kappa \approx 1.755$ . After 2 steps, the polynomial is

$$x^{13} - 4x^{12} + 6x^{11} - 5x^{10} + 3x^{9} - 3x^{8} + 5x^{7} - 3x^{6} - x^{5} + 4x^{4} - 2x^{3} + x^{2} - x + 1$$

giving  $\kappa \simeq 1.732$ . Note that  $\kappa$  is always an algebraic number—or strictly a so-called Perron number, obtained from a polynomial with leading coefficient 1. (Note that any possible Perron number can be obtained for example from some finite complement language.)

It is often convenient to fit  $s_n$  for large n to the form  $2^{hn}$ , where h is the so-called spatial (topological) entropy (see page 1084), given by  $Log[2, \kappa]$ . The value of this for successive t never increases; for the first 3 steps in rule 126 it is for example approximately 1, 0.811, 0.793. The exact value of h after more steps tends to be very difficult to find, and indeed the question of whether its limiting value after infinitely many steps satisfies a given bound—say even being nonzero—is in general undecidable (see page 1138).

If one associates with each possible sequence of length n a number  $Sum[a_i 2^{-i}, \{i, n\}]$ , then the set of sequences that actually occur at a given step form a Cantor set (see note below), whose Hausdorff dimension turns out to be exactly h.

■ Cycles and zeta functions. The number of sequences of n cells that can occur repeatedly, corresponding to cycles in the network, is given in terms of the adjacency matrix m by Tr[MatrixPower[m, n]]. These numbers can also be obtained as the coefficients of  $x^n$  in the series expansion of

 $x \partial_x Log[\zeta[m, x]]$ , with the so-called zeta function, which is always a rational function of x, given by

 $\zeta[m_-, x_-] := 1/Det[IdentityMatrix[Length[m]] - mx]$ and corresponds to the product over all cycles of  $1/(1-x^n)$ .

- 2D generalizations. Above 1D no systematic method seems to exist for finding exact formulas for entropies (as expected from the discussion at the end of Chapter 5). Indeed, even working out for large n how many of the  $2^{n^2}$  possible configurations of a nxn grid of black and white squares contain no pair of adjacent black cells is difficult. Fitting the result to  $2^{hn^2}$  one finds  $h \approx 0.589$ , but no exact formula for h has ever been found. With hexagonal cells, however, the exact solution of the so-called hard hexagon lattice gas model in 1980 showed that  $h \simeq 0.481$  is the logarithm of the largest root of a degree 12 polynomial. (The solution of the so-called dimer problem in 1961 also showed that for complete coverings of a square grid by 2-cell dominoes  $h = Catalan/(\pi Log[2]) \simeq 0.421.$
- Probability-based entropies. This section has concentrated on characterizing what sequences can possibly occur in 1D cellular automata, with no regard to their probability. It turns out to be difficult to extend the discussion of networks to include probabilities in a rigorous way. But it is straightforward to define versions of entropy that take account of probabilities-and indeed the closest analog to the usual entropy in physics or information theory is obtained by taking the probabilities p[i] for the  $k^n$  blocks of length n(assuming k colors), then constructing

-Limit[Sum[p[i] Log[k, p[i]], {i,  $k^n$ }]/n,  $n \rightarrow \infty$ ]

I have tended to call this quantity measure entropy, though in other contexts, it is often just called entropy or information, and is sometimes called information dimension. The quantity  $Limit[Sum[UnitStep[p[i]], \{i, k^n\}]/n, n \rightarrow \infty]$ 

is the entropy discussed in the notes above, and is variously called set entropy, topological entropy, capacity and fractal dimension. An example of a generalization is the quantity given for blocks of size n by

 $h[q_{-}, n_{-}] := Log[k, Sum[p[i]^{q}, \{i, k^{n}\}]]/(n(q-1))$ where q = 0 yields set entropy, the limit  $q \rightarrow 1$  measure entropy, and q = 2 so-called correlation entropy. For any qthe maximum h[q, n] = 1 occurs when all  $p[i] = k^{-n}$ . It is always the case that  $h[q + 1, n] \le h[q, n]$ . The h[q] have been introduced in almost identical form several times, notably by Alfréd Rényi in the 1950s as information measures for probability distributions, in the 1970s as part of the thermodynamic formalism for dynamical systems, and in the 1980s as generalized dimensions for multifractals. (Related objects have also arisen in connection with Hölder exponents for discontinuous functions.)

- Entropy estimates. Entropies h[n] computed from blocks of size n always decrease with n; the quantity nh[n] is always convex (negative second difference) with respect to n. At least at a basic level, to compute topological entropy one needs in effect to count every possible sequence that can be generated. But one can potentially get an estimate of measure entropy just by sampling possible sequences. One problem, however, is that even though such sampling may give estimates of probabilities that are unbiased (and have Gaussian errors), a direct computation of measure entropy from them will tend to give a value that is systematically too small. (A potential way around this is to use the theory of unbiased estimators for polynomials just above and below p Log[p].
- Nested structure of attractors. Associating with each sequence of length n (and k possible colors for each element) a number  $Sum[a[i]k^{-i}, \{i, n\}]$ , the set of sequences that occur in the limit  $n \to \infty$  forms a Cantor set. For k = 3, the set of sequences where the second color never occurs corresponds to the standard middle-thirds Cantor set. In general, whenever the possible sequences correspond to paths through a finite network, it follows that the Cantor set obtained has a nested structure. Indeed, constructing the Cantor set in levels by considering progressively longer sequences is effectively equivalent to following successive steps in a substitution system of the kind discussed on page 83. (To see the equivalence first set up s kinds of elements in the substitution system corresponding to the s nodes in the network.) Note that if the possible sequences cannot be described by a network, then the Cantor set obtained will inevitably not have a strictly nested form.
- Surjectivity and injectivity. One can think of a cellular automaton rule as a mapping (endomorphism) from the space of possible states of the cellular automaton to itself. (See page 869.) Usually this mapping is contractive, so that not all the states which appear as input to the mapping can also appear as output. But in some cases, the mapping is surjective or onto, meaning that any state which appears as input can also appear as output. Among k = 2, r = 1elementary cellular automata it turns out that this happens precisely for those 30 rules that are additive with respect to at least the first or last position on which they depend (see pages 601 and 1087); this includes both rules 90 and 150 and rules 30 and 45. With k = 2, r = 2 there are a total of 4,294,967,296 possible rules. Out of these 141,884 are ontoand 11,388 of these turn out not to be additive with respect to any position. The easiest way to test whether a particular rule is onto seems to be essentially just to construct the minimal finite automaton discussed on page 957. The onto

k = 2, r = 2 rules were found in 1961 in a computer study by Gustav Hedlund and others; they later apparently provided input in the design of S-boxes for DES cryptography (see page 1085).

Even when a cellular automaton mapping is surjective, it is still often many-to-one, in the sense that several input states can yield the same output state. (Thus for example additive rules such as 90 and 150, as well as one-sided additive rules such as 30 and 45 are always 4-to-1.) But some surjective rules also have the property of being injective, so that different input states always yield different output states. And in such a case the cellular automaton mapping is one-to-one or bijective (an automorphism). This is equivalent to saying that the rule is reversible, as discussed on page 1017.

(In 2D such properties are in general undecidable; see page 1138.)

■ Temporal sequences. So far we have considered possible sequences of cells that can occur at a particular step in the evolution of a cellular automaton. But one can also consider sequences formed from the color of a particular cell on a succession of steps. For class 1 and 2 cellular automata, there are typically only a limited number of possible sequences of any length allowed. And when the length is large, the sequences are almost always either just uniform or repetitive. For class 3 cellular automata, however, the number of sequences of length n typically grows rapidly with n. For additive rules such as 60 and 90, and for partially additive rules such as 30 and 45, any possible sequence can occur if an appropriate initial condition is given. For rule 18, it appears that any sequence can occur that never contains more than one adjacent black cell. I know of no general characterization of temporal sequences analogous to the finite automaton one used for spatial sequences above. However, if one defines the entropy or dimension h, for temporal sequences by analogy with the definition for spatial sequences above, then it follows for example that  $h_t \le 2 \lambda h_x$ , where  $\lambda$  is the maximum rate at which changes grow in the cellular automaton. The origin of this inequality is indicated in the picture below. The basic idea is that the size of the region that can affect a given cell in the course of t steps is  $2 \lambda t$ . But for large sizes x the total number of possible configurations of this region is  $k^{h_x x}$ . (Inequalities between entropies and Lyapunov exponents are also common in dynamical systems based on numbers, but are more difficult to derive.) Note that in effect,  $h_x$  gives the information content of spatial sequences in units of bits per unit distance, while  $h_t$  gives the corresponding quantity for temporal sequences in units of bits per unit time. (One can also define directional entropies based on sequences at different slopes; the values of such entropies tend to change discontinuously when the slope crosses  $\lambda$ .)

![](Images/_page_975_Picture_7.jpeg)

Different classes of cellular automata show characteristically different entropy values. Class 1 has  $h_x = 0$  and  $h_t = 0$ . Class 2 has  $h_x \neq 0$  but  $h_t = 0$ . Class 3 has  $h_x \neq 0$  and  $h_t \neq 0$ . Class 4 tends to show fluctuations which prevent definite values of  $h_x$  and  $h_t$  from being found.

■ Spacetime patches. One can imagine defining entropies and dimensions associated with regions of any shape in the spacetime history of a cellular automaton. As an example, one can consider patches that extend x cells across in space and t cells down in time. If the color of every cell in such a patch could be chosen independently then there would be  $k^{tx}$  possible configurations of the complete patch. But in fact, having just specified a block of length x + 2rt in the initial conditions, the cellular automaton rule then uniquely determines the color of every cell in the patch, allowing a total of at most  $s[t, x] = k^{x+2rt}$  configurations. One can define a topological spacetime entropy  $h_{tx}$  as

 $Limit[Limit[Log[k, s[t, x]]/t, t \rightarrow \infty], x \rightarrow \infty]$ 

and a measure spacetime entropy  $h_{tx}^{\mu}$  by replacing s with p Log[p]. In general,  $h_t \le h_{tx} \le 2 \lambda h_x$  and  $h \le 2r h_t$ . For additive rules like rule 90 and rule 150 every possible configuration of the initial block leads to a different configuration for the patch, so that  $h_{tx} = 2r = 2$ . But for other rules many different configurations of the initial block can lead to the same configuration for the patch, yielding potentially much smaller values of  $h_{tx}$ . Just as for most other entropies, when a cellular automaton shows complicated behavior it tends to be difficult to find much more than upper bounds for  $h_{tx}$ . For rule 30,  $h_{tx}^{\mu} < 1.155$ , and there is some evidence that its true value may actually be 1. For rule 18 it appears that  $h_{tx}^{\mu} = 1$ , while for rule 22,  $h_{tx}^{\mu} < 0.915$  and for rule  $54 h_{tx}^{\mu} < 0.25$ .

■ History. The analysis of cellular automata given in this section is largely as I worked it out in the early 1980s. Parts of it, however, are related to earlier investigations, particularly in dynamical systems theory. Starting in the 1930s the idea of symbolic dynamics began to emerge, in which one partitions continuous values in a system into bins represented by discrete symbols, and then looks at the sequences of such symbols that can be produced by the evolution of the system. In connection with early work on chaos theory, it was noted that there are some systems that act like "full shifts", in the sense that the set of sequences they generate includes all possibilities—and corresponds to what one would get by starting with any possible number, then successively shifting digits to the left, and at each step picking off the leading digit. It was noted that some systems could also yield various kinds of subshifts that are subsets of full shifts. But since-unlike in cellular automata-the symbol sequences being studied were obtained by rather arbitrary partitionings of continuous values, the question arose of what effect using different partitionings would have. One approach was to try to find invariants that would remain unchanged in different partitionings-and this is what led, for example, to the study of topological entropy in the 1960s. Another approach was to look at actual possible transformations between partitionings, and this led from the late 1950s to various studies of so-called shift-commuting block maps (or sliding-block codes)—which turn out to be exactly 1D cellular automata (see page 878). The locality of cellular automaton rules was thought of as making them the analog for symbol sequences of continuous functions for real numbers (compare page 869). Of particular interest were invertible (reversible) cellular automaton rules, since systems related by these were considered conjugate or topologically equivalent.

In the 1950s and 1960s-quite independent of symbolic dynamics-there was a certain amount of work done in connection with ideas about self-reproduction (see page 876) on the question of what configurations one could arrange to produce in 1D and 2D cellular automata. And this led for example to the study of so-called Garden of Eden states that can appear only in initial conditions—as well as to some general discussion of properties such as surjectivity.

When I started working on cellular automata in the early 1980s I wanted to see how far one could get by following ideas of statistical mechanics and dynamical systems theory and trying to find global characterizations of the possible behavior of individual cellular automata. In the traditional symbolic dynamics of continuous systems it had always been assumed that meaningful quantities must be invariant under continuous invertible transformations of symbol sequences. It turns out that the spacetime (or "invariant") entropy defined in the previous note has this property. But the spatial and temporal entropies that I introduced do not—and indeed in studying specific cellular automata there seems to be no particular reason why such a property would

■ Attractors in systems based on numbers. Particularly for systems based on ordinary differential equations (see page 922) a geometrical classification of possible attractors exists. There are fixed points, limit cycles and so-called strange attractors. (The first two of these were identified around the end of the 1800s; the last with clarity only in the 1960s.) Fixed points correspond to zero-dimensional subsets of the space of possible states, limit cycles to one-dimensional subsets (circles, solenoids, etc.). Strange attractors often have a nested structure with non-integer fractal dimension. But even in cases where the behavior obtained with a particular random initial condition is very complicated the structure of the attractor is almost invariably quite simple.

- **Iterated maps.** For maps of the form  $x \rightarrow ax(1-x)$  discussed on page 920 the attractor for small a is a fixed point, then a period 2 limit cycle, then period 4, 8, 16, etc. There is an accumulation of limit cycles at  $a \approx 3.569946$  where the system has a special nested structure. (See pages 920 and 955.)
- Attractors in Turing machines. In theoretical studies Turing machines are often set up so that if their initial conditions follow a particular formal grammar (see page 938) then they evolve to "accept" states—which can be thought of as being somewhat like attractors.
- Systems of limited size. For any system with a limited total number of states, it is possible to create a finite network that gives a global representation of the behavior of the system. The idea of this network (which is very different from the finite automata networks discussed above) is to have each node represent a complete state of the system. At each step in the evolution of the system, every state evolves to some new state, and this process is represented in the network by an arc that joins each node to a new node. The picture below gives the networks obtained for systems of the kind shown on page 255. Each node is labelled by a possible position for the dot. In the first case shown, starting for example at position 4 the dot then visits positions 5, 0, 1, 2 and so on, at each step going from one node in the network to the next.

![](Images/_page_976_Figure_10.jpeg)

The pictures below give networks obtained from the system shown on page 257 for various values of n. For odd n, the networks consist purely of cycles. But for even n, there are also trees of states that lead to these cycles.

![](Images/_page_977_Figure_1.jpeg)

In general, any network that represents the evolution of a system with definite rules will have the same basic form. There are cycles which contain states that are visited repeatedly, and there can also be trees that represent transient states that can each only ever occur at most once in the evolution of the system.

The picture below shows the network obtained from a class 1 cellular automaton (rule 254) with 4 cells and thus 16 possible states. All but one of these 16 states evolve after at most two steps to state 15, which corresponds to all cells being black.

![](Images/_page_977_Picture_4.jpeg)

The pictures below show networks obtained when more cells are included in the cellular automaton above. The same convergence to a single fixed point is observed.

![](Images/_page_977_Picture_6.jpeg)

The pictures below give corresponding results for a class 2 cellular automaton (rule 132). The number of distinct cycles now increases with the size of the system. (As discussed below, identical pieces of the network are often related by symmetries of the underlying cellular automaton system.)

![](Images/_page_977_Figure_8.jpeg)

In class 3, larger cycles are usually obtained, and often the whole network is dominated by a single largest cycle. The second set of pictures below summarize the results for some larger cellular automata. Each distinct region corresponds to a disjoint part of the network, with the area of the region being proportional to the number of nodes involved. The dark blobs represent cycles. (See page 1087.)

![](Images/_page_977_Figure_10.jpeg)

![](Images/_page_978_Figure_2.jpeg)

For large sizes there is a rough correspondence with the infinite size case, but many features are still different. (To recover correct infinite size results one must increase size while keeping the number of steps of evolution fixed; the networks shown above, however, effectively depend on arbitrarily many steps of evolution.)

- Symmetries. Many of the networks above contain large numbers of identical pieces. Typically the reason is that the states in each piece are shifted copies of each other, and in such cases the number of pieces will be a divisor of n. (See page 950.) If the underlying cellular automaton rule exhibits an invariance—say under reflection in space or permutation of colors—this will also often lead to the presence of identical pieces in the final network, corresponding to cosets of the symmetry transformation.
- Shift rules. The pictures below show networks obtained with rule 170, which just shifts every configuration one position to the left at each step. With any such shift rule, all states lie on cycles, and the lengths of these cycles are the divisors of the size n. Every cycle corresponds in effect to a distinct necklace with *n* beads; with *k* colors the total number of these is

Apply[Plus, (EulerPhi[n/#] k# &)[Divisors[n]]]/n

The number of cycles of length exactly m is s[m, k]/m, where s[m, k] is defined on page 950. For prime k, each cycle (except all 0's) corresponds to a term in the product Factor [ $x^{k^n-1}$  - 1, Modulus  $\rightarrow k$ ]. (See page 975.)

![](Images/_page_978_Picture_8.jpeg)

![](Images/_page_978_Picture_9.jpeg)

![](Images/_page_978_Picture_10.jpeg)

![](Images/_page_978_Picture_11.jpeg)

■ Additive rules. The pictures below show networks obtained for the additive cellular automata with rules 60 and 90. The networks are highly regular and can be analyzed by the algebraic methods mentioned on page 951. The lengths of the longest cycles are given on page 951; all other cycles must have lengths which divide these. Rooted at every state on each cycle is an identical structure. When the number of cells n is odd this structure consists of a single arc, so that half of all states lie on cycles. When n is even, the structure is a balanced tree of depth 2^IntegerExponent[n, 2] and degree 2 for rule 60, and depth 2^IntegerExponent[n/2, 2] and degree 4 for rule 90. The total fraction of states on cycles is in both cases 2^(-2^IntegerExponent[n, 2]). States with a single black cell are always on the longest cycles. The state with no black cells always forms a cycle of length 1.

![](Images/_page_978_Figure_14.jpeg)

![](Images/_page_978_Picture_15.jpeg)

Random networks. The pictures below show networks in which each of a set of n nodes has as its successor a node that is chosen at random from the set. The total number of possible such networks is  $n^n$ . For large n, the average number of distinct cycles in all such networks is  $Sqrt[\pi/2]Log[n]$ , and the average length of these cycles is  $Sart[\pi n/8]$ . The average fraction of nodes that have no predecessor is  $(1 - 1/n)^n$  or 1/e in the limit  $n \to \infty$ . Note that processes such as cellular automaton evolution do not yield networks whose properties are particularly close to those of purely random ones.

![](Images/_page_979_Figure_1.jpeg)

#### Structures in Class 4 Systems

■ Page 283 · Survival data. The number of steps for which the pattern produced by each of the first 1000 initial conditions in code 20 survive are indicated in the picture below. 72 of these initial conditions lead to persistent structures. Among the first million initial conditions, 60,171 lead to persistent structures and among the first billion initial conditions the number is 71,079,205.

![](Images/_page_979_Figure_4.jpeg)

■ **Page 290 · Background.** At every step the background pattern in rule 110 consists of repetitions of the block  $b = \{1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0\}$ , as shown in the picture below. On step t the color of a cell at position x is given by b[[Mod[x+4t, 14]+1]].

![](Images/_page_979_Picture_6.jpeg)

■ **Page 292 · Structures.** The persistent structures shown can be obtained from the following  $\{n, w\}$  by inserting the sequences IntegerDigits[n, 2, w] between repetitions of the background block b:

{{152, 8}, {183, 8}, {18472955, 25}, {732, 10}, {129643, 18}, {0, 5}, {152, 13}, {39672, 21}, {619, 15}, {44, 7}, {334900605644, 39}, {8440, 15}, {248, 9}, {760, 11}, {38, 6}}

The repetition periods and distances moved in each period for the structures are respectively

{{4, -2}, {12, -6}, {12, -6}, {42, -14}, {42, -14}, {15, -4}, {15, -4}, {15, -4}, {30, -8}, {92, -18}, {36, -4}, {7, 0}, {10, 2}, {3, 2}}

Note that the periodicity of the background forces all rule 110 structures to have periods and distances given by  $\{4, -2\}r + \{3, 2\}s$  where r and s are non-negative integers. Extended versions of structures (d)–(i) can be obtained by collisions with (a). Extended versions of (b) and (c) can be obtained from

Flatten[{IntegerDigits[1468, 2], Table[
IntegerDigits[102524348, 2], {n}], IntegerDigits[v, 2]}]

where *n* is a non-negative integer and *v* is one of {1784, 801016, 410097400, 13304, 6406392, 3280778648}

Note that in most cases multiple copies of the same structure can travel next to each other, as seen on page 290.

- **Page 293 · Glider gun.** The initial conditions shown correspond to  $\{n, w\} = \{1339191737336, 41\}$ .
- Page 294 · Collisions. A fundamental result is that the sum of the widths of all persistent structures involved in an interaction must be conserved modulo 14.
- The Game of Life. The 2D cellular automaton described on page 949 supports a whole range of persistent structures, many of which have been given quaint names by its enthusiasts. With typical random initial conditions the most common structures to occur are:

![](Images/_page_979_Picture_18.jpeg)

The next most common moving structure is the so-called "spaceship":

![](Images/_page_979_Picture_20.jpeg)

The complete set of structures with less than 8 black cells that remain unchanged at every step in the evolution are:

![](Images/_page_979_Picture_22.jpeg)

More complicated repetitive and moving structures are shown in the pictures below. If one looks at the history of a single row of cells, it typically looks much like the complete histories we have seen in 1D class 4 cellular automata.

![](Images/_page_979_Picture_24.jpeg)

Structures with all repetition periods up to 18 have been found in Life; examples are shown in the pictures below.

![](Images/_page_980_Figure_3.jpeg)

Persistent structures with various speeds in the horizontal and vertical direction have also been found, as shown below.

![](Images/_page_980_Picture_5.jpeg)

The first example of unbounded growth in Life was the socalled "glider gun", discovered by William Gosper in 1970 and shown below. This object emits a glider every 30 steps. The simplest known initial condition which leads to a glider gun contains 21 black cells. The so-called "switch engine" discovered in 1971 generates unbounded growth by leaving a trail behind when it moves; it is now known that it can be obtained from an initial condition with 10 black cells, or black cells in just a 5×5 or 39×1 region. It is also known that from less than 10 initial black cells no unbounded growth is ever possible.

![](Images/_page_980_Picture_7.jpeg)

Many more elaborate structures similar to the glider gun were found in the 1970s and 1980s; two are illustrated below.

![](Images/_page_980_Picture_9.jpeg)

![](Images/_page_980_Picture_10.jpeg)

![](Images/_page_980_Picture_11.jpeg)

![](Images/_page_980_Picture_12.jpeg)

A simpler kind of unbounded growth occurs if one starts from an infinite line of black cells. In that case, the evolution is effectively 1D, and turns out to follow elementary rule 22, thus producing the infinitely growing nested pattern shown on page 263.

For a long time it was not clear whether Life would support any kind of uniform unbounded growth from a finite initial region of black cells. However, in 1993 David Bell found starting from 206 black cells the "spacefiller" shown below. This object is closely analogous to those shown for code 1329 on page 287.

![](Images/_page_980_Picture_15.jpeg)

![](Images/_page_980_Picture_16.jpeg)

![](Images/_page_980_Picture_17.jpeg)

As in other class 4 cellular automata, there are structures in Life which take a very long time to settle down. The so-called "puffer train" below which starts from 23 black cells becomes repetitive with period 140 only after more than 1100 steps.

![](Images/_page_980_Picture_19.jpeg)

![](Images/_page_980_Picture_20.jpeg)

![](Images/_page_980_Picture_21.jpeg)

![](Images/_page_980_Picture_22.jpeg)

- Other 2D cellular automata. The general problem of finding persistent structures is much more difficult in 2D than in 1D, and there is no completely general procedure, for example, for finding all structures of any size that have a certain repetition period.
- Structures in Turing machines. See page 888.

#### Mechanisms in Programs and Nature

#### Universality of Behavior

• History. That very different natural and artificial systems can show similar forms has been noted for many centuries. Informal studies have been done by a whole sequence of architects interested both in codifying possible forms and in finding ways to make structures fit in with nature and with our perception of it. Beginning in the Renaissance the point has also been noted by representational and decorative artists, most often in the context of developing a theory of the types of forms to be studied by students of art. The growth of comparative anatomy in the 1800s led to attempts at more scientific treatments, with analogies between biological and physical systems being emphasized particularly by D'Arcy Thompson in 1917. Yet despite all this, the phenomenon of similarity between forms remained largely a curiosity, discussed mainly in illustrated books with no clear basis in either art or science. In a few cases (such as work by Peter Stevens in 1974) general themes were however suggested. These included for example symmetry, the golden ratio, spirals, vortices, minimal surfaces, branching patterns, and-since the 1980s-fractals. The suggestion is also sometimes made that we perceive a kind of harmony in nature because we see only a limited number of types of forms in it. And particularly in classical architecture the idea is almost universally used that structures will seem more com fortable to us if they repeat in ornament or otherwise forms with which we have become familiar from nature. Whenever a scientific model has the same character for different systems this means that the systems will tend to show similar forms. And as models like cellular automata capable of dealing with complexity have become more widespread it has been increasingly popular to show that they can capture similar forms seen in very different systems.

#### Three Mechanisms for Randomness

- Page 299 · Definition. How randomness can be defined is discussed at length on page 552.
- History. In antiquity, it was often assumed that all events must be governed by deterministic fate—with any apparent randomness being the result of arbitrariness on the part of the gods. Around 330 BC Aristotle mentioned that instead randomness might just be associated with coincidences outside whatever system one is looking at, while around 300 BC Epicurus suggested that there might be randomness continually injected into the motion of all atoms. The rise of emphasis on human free will (see page 1135) eroded belief in determinism, but did not especially address issues of randomness. By the 1700s the success of Newtonian physics seemed again to establish a form of determinism, and led to the assumption that whatever randomness was actually seen must reflect lack of knowledge on the part of the observeror particularly in astronomy some form of error of measurement. The presence of apparent randomness in digit sequences of square roots, logarithms, numbers like  $\pi$ , and other mathematical constructs was presumably noticed by the 1600s (see page 911), and by the late 1800s it was being taken for granted. But the significance of this for randomness in nature was never recognized. In the late 1800s and early 1900s attempts to justify both statistical mechanics and probability theory led to ideas that perfect microscopic randomness might somehow be a fundamental feature of the physical world. And particularly with the rise of quantum mechanics it came to be thought that meaningful calculations could be done only on probabilities, not on individual random sequences. Indeed, in almost every area where quantitative methods were used, if randomness was observed, then either a different system was studied, or efforts were made to remove the randomness by averaging or some other statistical method. One case where there was occasional discussion of origins of randomness from at least

the early 1900s was fluid turbulence (see page 997). Early theories tended to concentrate on superpositions of repetitive motions, but by the 1970s ideas of chaos theory began to dominate. And in fact the widespread assumption emerged that between randomness in the environment, quantum randomness and chaos theory almost any observed randomness in nature could be accounted for. Traditional mathematical models of natural systems are often expressed in terms of probabilities, but do not normally involve anything one can explicitly consider as randomness. Models used in computer simulations, however, do very often use explicit randomness. For not knowing about the phenomenon of intrinsic randomness generation, it has normally been assumed that with the kinds of discrete elements and fairly simple rules common in such models, realistically complicated behavior can only ever be obtained if explicit randomness is continually introduced.

■ **Applications of randomness.** See page 1192.

■ Sources of randomness. Two simple mechanical methods for generating randomness seem to have been used in almost every civilization throughout recorded history. One is to toss an object and see which way up or where it lands; the other is to select an object from a collection mixed by shaking. The first method has been common in games of chance, with polyhedral dice already existing in 2750 BC. The second often called drawing lots-has normally been used when there is more at stake. It is mentioned several times in the Bible, and even today remains the most common method for large lotteries. (See page 969.) Variants include methods such as drawing straws. In antiquity fortune-telling from randomness often involved looking say at growth patterns of goat entrails or sheep shoulder blades; today configurations of tea leaves are sometimes considered. In early modern times the matching of fracture patterns in broken tally sticks was used to identify counterparties in financial contracts. Horse races and other events used as a basis for gambling can be viewed as randomness sources. Children's games like musical chairs in effect generate randomness by picking arbitrary stopping times. Games of chance based on wheels seem to have existed in Roman times; roulette developed in the 1700s. Card shuffling (see page 974) has been used as a source of randomness since at least the 1300s. Pegboards (as on page 312) were used to demonstrate effects of randomness in the late 1800s. An explicit table of 40,000 random digits was created in 1927 by Leonard Tippett from details of census data. And in 1938 further tables were generated by Ronald Fisher from digits of logarithms. Several tables based on physical processes were produced, with the RAND Corporation in 1955 publishing a table of a million random digits obtained from an electronic roulette wheel. Beginning in the 1950s, however, it became increasingly common to use pseudorandom generators whenever long sequences were needed-with linear feedback shift registers being most popular in standalone electronic devices, and linear congruential generators in programs (see page 974). There nevertheless continued to be occasional work done on mechanical sources of randomness for toys and games, and on physical electronic sources for cryptography systems (see page 969).

#### Randomness from the Environment

- Page 301 · Stochastic models. The mechanism randomness discussed in this section is the basis for so-called stochastic models now widely used in traditional science. Typically the idea of these models is to approximate those elements of a system about which one does not know much by random variables. (See also page 588.) In the early work along these lines done by James Clerk Maxwell and others in the 1880s, analytical formulas were usually worked out for the probabilities of different outcomes. But when electronic computers became available in the 1940s, the so-called Monte Carlo method became increasingly popular, in which instead explicit simulations are performed with different choices of random variables, and then statistical averages are found. Early uses of the Monte Carlo method were mostly in physics, particularly for studies of neutron diffusion and particle shower generation in high-energy collisions. But by the 1980s the Monte Carlo method had also become common in other fields, and was routinely used in studying for example message flows in communication networks and pricing processes in financial markets. (See also page 1192.)
- Page 301 · Ocean surfaces. See page 1001.
- Page 302 · Random walks. See page 328.
- Page 302 · Electronic noise. Three types of noise are commonly observed in typical devices:

Shot noise. Electric currents are not continuous but are ultimately made up from large numbers of moving charge carriers, typically electrons. Shot noise arises from statistical fluctuations in the flow of charge carriers: if a single bit of data is represented by 10,000 electrons, the magnitude of the fluctuations will typically be about 1%. When looked at as a waveform over time, shot noise has a flat frequency spectrum.

Thermal (Johnson) noise. Even though an electric current may have a definite overall direction, the individual charge carriers within it will exhibit random motions. In a material at nonzero temperature, the energy of these motions and thus the intensity of the thermal noise they produce is essentially proportional to temperature. (At very low temperatures, quantum mechanical fluctuations still yield random motion in most materials.) Like shot noise, thermal noise has a flat frequency spectrum.

Flicker (1/f) noise. Almost all electronic devices also exhibit a third kind of noise, whose main characteristic is that its spectrum is not flat, but instead goes roughly like 1/f over a wide range of frequencies. Such a spectrum implies the presence of large low-frequency fluctuations, and indeed fluctuations are often seen over timescales of many minutes or even hours. Unlike the types of noise described above, this kind of noise can be affected by details of the construction of individual devices. Although seen since the 1920s its origins remain somewhat mysterious (see below).

■ Power spectra. Many random processes in nature show power spectra Abs[Fourier[data]]<sup>2</sup> with fairly simple forms. Most common are white noise uniform in frequency and  $1/f^2$ noise associated with random walks. Other pure power laws  $1/f^{\alpha}$  are also sometimes seen; the pictures below show some examples. (Note that the correlations in such data in some sense go like  $t^{\alpha-1}$ .) Particularly over the past few decades all sorts of examples of "1/f noise" have been identified with  $\alpha \simeq 1$ , including flicker noise in resistors, semiconductor devices and vacuum tubes, as well as thunderstorms, earthquake and sunspot activity, heartbeat intervals, road traffic density and some DNA sequences. A pure  $1/f^{\alpha}$ spectrum presumably reflects some form of underlying nesting or self-similarity, although exactly what has usually been difficult to determine. Mechanisms that generally seem able to give  $\alpha \simeq 1$  include random walks with exponential waiting times, power-law distributions of step sizes (Lévy flights), or white noise variations of parameters, as well as random processes with exponentially distributed relaxation times (as from Boltzmann factors for uniformly distributed barrier heights), fractional integration of white noise, intermittency at transitions to chaos, and random substitution systems. (There was confusion in the late 1980s when theoretical studies of self-organized criticality failed correctly to take squares in computing power spectra.) Note that the Weierstrass function of page 918 yields a 1/f spectrum, and presumably suitable averages of spectra from any substitution system should also have  $1/f^{\alpha}$  forms (compare page 586).

![](Images/_page_984_Figure_5.jpeg)

![](Images/_page_984_Picture_6.jpeg)

![](Images/_page_984_Picture_7.jpeg)

![](Images/_page_984_Picture_8.jpeg)

![](Images/_page_984_Figure_9.jpeg)

- Page 303 · Spark chambers. The sensitivity of sparks to microscopic details of the environment is highlighted by the several devices which essentially use them to detect the passage of individual elementary particles such as protons. Such particles leave a tiny trail of ionized gas, which becomes the path of the spark. This principle was used in Geiger counters, and later in spark chambers and wire chambers.
- Physical randomness generators. It is almost universally assumed that at some level physical processes must be the best potential sources of true randomness. But in practice their record has actually been very poor. It does not help that unlike algorithms physical devices can be affected by their environment, and can also not normally be copied identically. But in almost every case I know where detailed analysis has been done substantial deviations from perfect randomness have been found. This has however typically been attributed to engineering mistakes-or to sampling data too quicklyand not to anything more fundamental that is for example worth describing in publications.
- Mechanical randomness. It takes only small imperfections in dice or roulette wheels to get substantially non-random results (see page 971). Gaming regulations typically require dice to be perfect cubes to within one part in a few thousand; casinos normally retire dice after a few hundred rolls.

In processes like stirring and shaking it can take a long time for correlations to disappear-as in the phenomenon of longtime tails mentioned on page 999. One notable consequence were traces of insertion order among the 366 capsules used in the 1970 draft lottery in the U.S. But despite such problems mixing of objects remains by far the most common way to generate randomness when there is a desire for the public to see randomization occur. And so for example all the state lotteries in the U.S. are currently based on mixing between 10 and 54 balls. (Numbers games were instead sometimes based on digits of financial data in newspapers.)

There have been a steady stream of inventions for mechanical randomness generation. Some are essentially versions of dice. Others involve complicated cams or linkages, particularly for mechanical toys. And still others involve making objects like balls bounce around as randomly as possible in air or other fluids.

■ Electronic randomness. Since the 1940s a steady stream of electronic devices for producing randomness have been invented, with no single one ever becoming widely used. An early example was the ERNIE machine from 1957 for British national lottery (premium bond) drawings, which worked by sampling shot noise from neon discharge

tubes-and perhaps because it extracted only a few digits per second no deviations from randomness in its output were found. (U.S. missiles apparently used a similar method to produce randomly spaced radar pulses for determining altitude.) Since the 1970s electronic randomness generators have typically been based on features of semiconductor devices-sometimes thermal noise, but more often breakdown, often in back-biased zener diodes. All sorts of schemes have been invented for getting unbiased output from such systems, and acceptable randomness can often be obtained at kilohertz rates, but obvious correlations almost always appear at higher rates. Macroscopic thermal diffusion undoubtedly underestimates the time for good microscopic randomization. For in addition to 1/f noise effects, solitons and other collective lattice effects presumably lead to power-law decay of correlations. It still seems likely however that some general inequalities should exist between the rate and quality of randomness that can be extracted from a system with particular thermodynamic properties.

- Quantum randomness. It is usually assumed that even if all else fails a quantum process such as radioactive decay will yield perfect randomness. But in practice the most accurate measurements show phenomena such as 1/f noise, presumably as a result of features of the detector and perhaps of electromagnetic fields associated with decay products. Acceptable randomness has however been obtained at rates of tens of bits per second. Recent attempts have also been made to produce quantum randomness at megahertz rates by detecting paths of single photons. (See also page 1064.)
- Randomness in computer systems. Most randomness needed in practical computer systems is generated purely by programs, as discussed on page 317. But to avoid having a particular program give exactly the same random sequence every time it is run, one usually starts from a seed chosen on the basis of some random feature of the environment. Until the early 1990s this seed was most often taken from the exact time of day indicated by the computer's clock at the moment when it was requested. But particularly in environments where multiple programs can start almost simultaneously other approaches became necessary. Versions of the Unix operating system, for example, began to support a virtual device (typically called /dev/random) to maintain a kind of pool of randomness based on details of the computer system. Most often this uses precise timings between interrupts generated by keys being pressed, a mouse being moved, or data being delivered from a disk, network, or other device. And to prevent the same state being reached every time a computer is

rebooted, some information is permanently maintained in a file. At the end of the 1990s standard microprocessors also began to include instructions to sample thermal noise from an on-chip resistor. (Any password or encryption key made up by a human can be thought of as a source of randomness; some systems look at details of biometric data, or scribbles drawn with a mouse.)

■ Randomness in biology. Thermal fluctuations in chemical reactions lead to many kinds of microscopic randomness in biological systems, sometimes amplified when organisms grow. For example, small-scale randomness in embryos can affect large-scale pigmentation patterns in adult organisms, as discussed on page 1013. Random changes in single DNA molecules can have global effects on the development of an organism. Standard mitotic cell division normally produces identical copies of DNA—with random errors potentially leading for example to cancers. But in sexual reproduction genetic material is rearranged in ways normally assumed by classical genetics to be perfectly random. One reason is that which sperm fertilizes a given egg is determined by random details of sperm and fluid motion. Another reason is that egg and sperm cells get half the genetic material of an organism, somewhat at random. In most cells, say in humans, there are two versions of all 23 chromosomes—one from the father and one from the mother. But when meiosis forms egg and sperm cells they get only one version of each. There is also exchange of DNA between paternal and maternal chromosomes, typically with a few crossovers per chromosome, at positions that seem more or less randomly distributed among many possibilities (the details affect regions of repeating DNA used for example in DNA fingerprinting).

In the immune system blocks of DNA—and joins between them—are selected at random by microscopic chemical processes when antibodies are formed.

Most animal behavior is ultimately controlled by electrical activity in nerve cells—and this can be affected by details of sensory input, as well as by microscopic chemical processes in individual cells and synapses (see page 1011).

Flagellated microorganisms can show random changes in direction as a result of tumbling when their flagella counterrotate and the filaments in them flail around.

(See also page 1011.)

#### **Chaos Theory and Randomness from Initial Conditions**

■ **Page 305 · Spinning and tossing.** Starting with speed v, the speed of the ball at time t is simply v-at, where a is the deceleration produced by friction. The ball thus stops at time

v/a. The distance gone by the ball at a given time is  $x = vt - at^2/2$ , and its orientation is  $Mod[x, 2\pi r]$ . For dice and coins there are some additional detailed effects associated with the shapes of these objects and the way they bounce. (Polyhedral dice have become more common since Dungeons & Dragons became popular in the late 1970s.) Note that in practice a coin tossed in the air will typically turn over between ten and twenty times while a die rolled on a table will turn over a few tens of times. A coin spun on a table can rotate several hundred times before falling over and coming to rest.

■ Billiards. A somewhat related system is formed by a billiard ball bouncing around on a table. The issue of which sequence of horizontal and vertical sides the ball hits depends on the exact slope with which the ball is started (in the picture below it is  $1/\sqrt{2}$ ). In general, it is given by the successive terms in the continued fraction form (see page 914) of this slope, and is related to substitution systems (see page 903). (See also page 1022.)

![](Images/_page_986_Picture_4.jpeg)

![](Images/_page_986_Picture_5.jpeg)

![](Images/_page_986_Picture_6.jpeg)

![](Images/_page_986_Picture_7.jpeg)

![](Images/_page_986_Picture_8.jpeg)

- Fluttering. If one releases a stationary piece of paper in air, then unlike a coin, it does not typically maintain the same orientation as it falls. Small pieces of paper spin in a repetitive way; but larger pieces of paper tend to flutter in a seemingly random way (as discussed, among others, by James Clerk Maxwell in 1853). A similar phenomenon can be seen if one drops a coin in water. I suspect that in these cases the randomness that occurs has an intrinsic origin, rather than being the result of sensitive dependence on initial conditions.
- History of chaos theory. The idea that small causes can sometimes have large effects has been noted by historians and others since antiquity, and captured for example in "for want of a nail ... a kingdom was lost". In 1860 James Clerk Maxwell discussed how collisions between hard sphere molecules could lead to progressive amplification of small changes and yield microscopic randomness in gases. In the 1870s Maxwell also suggested that mechanical instability and amplification of infinitely small changes at occasional critical points might explain apparent free will (see page 1135). (It was already fairly well understood that for example small changes could determine which way a beam would buckle.) In 1890 Henri Poincaré found sensitive dependence on initial conditions in a particular case of the

three-body problem (see below), and later proposed that such phenomena could be common, say in meteorology. In 1898 Jacques Hadamard noted general divergence of trajectories in spaces of negative curvature, and Pierre Duhem discussed the possible general significance of this in 1908. In the 1800s there had been work on nonlinear oscillators-particularly in connection with models of musical instruments-and in 1927 Balthazar van der Pol noted occasional "noisy" behavior in a vacuum tube oscillator circuit presumably governed by a simple nonlinear differential equation. By the 1930s the field of dynamical systems theory had begun to provide characterizations of possible forms of behavior in differential equations. And in the early 1940s Mary Cartwright and John Littlewood noted that van der Pol's equation could exhibit solutions somehow sensitive to all digits in its initial conditions. The iterated map  $x \rightarrow 4x(1-x)$ was also known to have a similar property (see page 918). But most investigations centered on simple and usually repetitive behavior-with any strange behavior implicitly assumed to be infinitely unlikely. In 1962, however, Edward Lorenz did a computer simulation of a set of simplified differential equations for fluid convection (see page 998) in which he saw complicated behavior that seemed to depend sensitively on initial conditions—in a way that he suggested was like the map  $x \to FractionalPart[2x]$ . In the mid-1960s, notably through the work of Steve Smale, proofs were given that there could be differential equations in which such sensitivity is generic. In the late 1960s there began to be all sorts of simulations of differential equations with complicated behavior, first mainly on analog computers, and later on digital computers. Then in the mid-1970s, particularly following discussion by Robert May, studies of iterated maps with sensitive dependence on initial conditions became common. Work by Robert Shaw in the late 1970s clarified connections between information content of initial conditions and apparent randomness of behavior. The term "chaos" had been used since antiquity to describe various forms of randomness, but in the late 1970s it became specifically tied to the phenomenon of sensitive dependence on initial conditions. By the early 1980s at least indirect signs of chaos in this sense (see note below) had been seen in all sorts of mechanical, electrical, fluid and other systems, and there emerged a widespread conviction that such chaos must be the source of all important randomness in nature. So in 1985 when I raised the possibility that intrinsic randomness might instead be a key phenomenon this was greeted with much hostility by some younger proponents of chaos theory. Insofar as what they had to say was of a scientific nature, their main point was that somehow what I

had seen in cellular automata must be specific to discrete systems, and would not occur in the continuous systems assumed to be relevant in nature. But from many results in this book it is now clear that this is not correct. (Note that James Gleick's 1987 popular book Chaos covers somewhat more than is usually considered chaos theory-including some of my results on cellular automata from the early 1980s.)

- Information content of initial conditions. See page 920.
- Recognizing chaos. Any system that depends sensitively on digits in its initial conditions must necessarily be able to show behavior that is not purely repetitive (compare page 955). And when it is said that chaos has been found in a particular system in nature what this most often actually means is just that behavior with no specific repetition frequency has been seen (compare page 586). To give evidence that this is not merely a reflection of continual injection of randomness from the environment what is normally done is to show that at least some aspect of the behavior of the system can be fit by a definite simple iterated map or differential equation. But inevitably the fit will only be approximate, so there will always be room for effects from randomness in the environment. And in general this kind of approach can never establish that sensitive dependence on initial conditions is actually the dominant source of randomness in a given system—say as opposed to intrinsic randomness generation. (Attempts are sometimes made to detect sensitive dependence directly by watching whether a system can do different things after it appears to return to almost exactly the same state. But the problem is that it is hard to be sure that the system really is in the same stateand that there are not all sorts of large differences that do not happen to have been observed.)
- Instability. Sensitive dependence on initial conditions is associated with a kind of uniform instability in systems. But vastly more common in practice is instability only at specific critical points—say bifurcation points—combined with either intrinsic randomness generation or randomness from the environment. (Note that despite its widespread use in discussions of chaos theory, this is also what usually seems to happen with the weather; see page 1177.)
- Page 313 · Three-body problem. The two-body problem was analyzed by Johannes Kepler in 1609 and solved by Isaac Newton in 1687. The three-body problem was a central topic in mathematical physics from the mid-1700s until the early 1900s. Various exact results were obtained-notably the existence of stable equilateral triangle configurations corresponding to so-called Lagrange points. Many

approximate practical calculations, particularly on the Earth-Moon-Sun system, were done using series expansions involving thousands of algebraic terms. (It is now possible to get most results just by direct numerical computation using for example NDSolve.) From its basic setup the three-body system conserves standard mechanical quantities like energy and angular momentum. But it was thought it might also conserve other quantities (or so-called integrals of the motion). In 1887, however, Heinrich Bruns showed that there could be no such quantities expressible as algebraic functions of the positions and velocities of the bodies (in standard Cartesian coordinates). In the mid-1890s Henri Poincaré then showed that there could also be no such quantities analytic in positions, velocities and mass ratios. And from these results the conclusion was drawn that the three-body problem could not be solved in terms of algebraic formulas and integrals. In 1912 Karl Sundman did however find an infinite series that could in principle be summed to give the solution-but which converges exceptionally slowly. And even now it remains conceivable that the three-body problem could be solved in terms of more sophisticated standard mathematical functions. But I strongly suspect that in fact nothing like this will ever be possible and that instead the three-body problem will turn out to show the phenomenon of computational irreducibility discussed in Chapter 12 (and that for example three-body systems are universal and in effect able to perform any computation). (See also page 1132.)

In Henri Poincaré's study of the collection of possible trajectories for three-body systems he identified sensitive dependence on initial conditions (see above), noted the general complexity of what could happen (particularly in connection with so-called homoclinic tangles), and developed topology to provide a simpler overall description. With appropriate initial conditions one can get various forms of simple behavior. The pictures below show some of the possible repetitive orbits of an idealized planet moving in the plane of a pair of stars that are in a perfect elliptical orbit.

![](Images/_page_987_Picture_9.jpeg)

![](Images/_page_987_Picture_10.jpeg)

![](Images/_page_987_Picture_11.jpeg)

![](Images/_page_987_Picture_12.jpeg)

![](Images/_page_987_Picture_13.jpeg)

The pictures below show results for a fairly typical sequence of initial conditions where all three bodies interact. (The two bodies at the bottom are initially at rest; the body at the top is given progressively larger rightward velocities.) What generically happens is that one of the bodies escapes from the other two (like t or sometimes  $t^{2/3}$ ). Often this happens quickly, but sometimes all three bodies show complex and

apparently random behavior for quite a while. (The delay before escaping is reminiscent of resonant scattering.)

![](Images/_page_988_Figure_3.jpeg)

■ Page 314 · Simple case. The position of the idealized planet in the case shown satisfies the differential equation

 $\partial_{tt} z[t] = -z[t]/(z[t]^2 + (1/2(1 + e Sin[2\pi t]))^2)^{3/2}$ 

where e is the eccentricity of the elliptical orbit of the stars (e = 0.1 in the picture). (Note that the physical situation is unstable: if the planet is perturbed so that there is a difference between its distance to each star, this will tend to increase.) Except when e = 0, the equation has no solution in terms of standard mathematical functions. It can be solved numerically in Mathematica using NDSolve, although a working precision of 40 decimal digits was used to obtain the results shown. Following work by Kirill Sitnikov in 1960 and by Vladimir Alekseev in 1968, it was established that with suitably chosen initial conditions, the equation yields any sequence Floor[t[i+1]-t[i]] of successive zero-crossing times t[i]. The pictures below show the dependence of z[t]on t and z[0]. As t increases, z[t] typically begins to vary more rapidly with z[0]—reflecting sensitive dependence on initial conditions.

![](Images/_page_988_Figure_7.jpeg)

■ Page 314 · Randomness in the solar system. Most motion observed in the solar system on human timescales is highly regular-though sometimes intricate, as in the sequence of numbers of days between successive new moons shown

below. In the mid-1980s, however, work by Jack Wisdom and others established that randomness associated with sensitive dependence on initial conditions could occur in certain current situations in the solar system, notably in the orbits of asteroids. Various calculations suggest that there should also be sensitive dependence on initial conditions in the orbits of planets in the solar system—with effects doubling every few million years. But there are so far no observational signs of randomness resulting from this, and indeed the planets-at least now-mostly just seem to have orbits that are within a few percent of circles. If a planet moved in too random a way then it would tend to collide or escape from the solar system. And indeed it seems quite likely that in the past there may have been significantly more planets in our solar systemwith only those that maintained regular orbits now being left. (See also page 1021.)

![](Images/_page_988_Figure_10.jpeg)

#### The Intrinsic Generation of Randomness

- Autoplectic processes. In the 1985 paper where I introduced intrinsic randomness generation I called processes that show this autoplectic, while I called processes that transcribe randomness from outside homoplectic.
- Page 316 · Algorithmic randomness. The idea of there being no simple procedure that can generate a particular sequence can be stated more precisely by saying that there is no program shorter than the sequence itself which can be used to generate the sequence, as discussed in more detail on page 1067.
- Page 317 · Randomness in Mathematica. SeedRandom[n] is the function that sets up the initial conditions for the cellular automaton. The idea of using this kind of system in general and this system in particular as a source of randomness was described in my 1987 U.S. patent number 4,691,291.
- Page 321 · Cellular automata. From the discussion here it should not be thought that in general there is necessarily anything better about generating randomness with cellular automata than with systems based on numbers. But the point is that the specific method used for making practical linear congruential generators does not yield particularly good randomness and has led to some incorrect intuition about the generation of randomness. If one goes beyond the specifics of linear congruential generators, then one can find many features of systems based on numbers that seem to be

perfectly random, as discussed in Chapter 4. In addition, one should recognize that while the complete evolution of the cellular automaton may effectively generate perfect randomness, there may be deviations from randomness introduced when one constructs a practical random number generator with a limited number of cells. Nevertheless, no such deviations have so far been found except when one looks at sequences whose lengths are close to the repetition period. (See however page 603.)

■ Page 321 · Card shuffling. Another rather poor example of intrinsic randomness generation is perfect card shuffling. In a typical case, one splits the deck of cards in two, then carefully riffles the cards so as to make alternate cards come from each part of the deck. Surprisingly enough, this simple procedure, which can be represented by the function

s[list\_] := Flattenf

Transpose[Reverse[Partition[list, Length[list]/2]]]]

with or without the Reverse, is able to produce orderings which at least in some respects seem quite random. But by doing Nest[s, Range[52], 26] one ends up with a simple reversal of the original deck, as in the pictures below.

![](Images/_page_989_Picture_7.jpeg)

■ Random number generators. A fairly small number of different types of random number generators have been used in practice, so it is possible to describe all the major ones here.

Linear congruential generators. The original suggestion made by Derrick Lehmer in 1948 was to take a number n and at each step to replace it by Mod[an, m]. Lehmer used a = 23and  $m = 10^8 + 1$ . Most subsequent implementations have used  $m = 2^{j}$ , often with j = 31. Such choices are particularly convenient on computers where machine integers are represented by 32 binary digits. The behavior of the linear congruential generator depends greatly on the exact choice of a. Starting with the so-called RANDU generator used on mainframe computers in the 1960s, a common choice made was a = 65539. But as shown in the main text, this choice leads to embarrassingly obvious regularities. Starting in the mid-1970s, another common choice was a = 69069. This was also found to lead to regularities, but only in six or more dimensions. (Small values of a also lead to an excess of runs of identical digits, as mentioned on page 903.)

The repetition period for a generator with rule  $n \rightarrow Mod[an, m]$  is given (for a and m relatively prime) by MultiplicativeOrder[a, m]. If m is of the form  $2^{j}$ , this implies a maximum period for any a of m/4, achieved when MemberQ[{3, 5}, Mod[a, 8]]. In general the maximum period is CarmichaelLambda[m], where the value m-1 can be achieved for prime m.

As illustrated in the main text, when  $m = 2^{j}$  the right-hand base 2 digits in numbers produced by linear congruential generators repeat with short periods; a digit k positions from the right will typically repeat with period no more than  $2^k$ . When  $m = 2^j - 1$  is prime, however, even the rightmost digit repeats only with period m-1 for many values of a.

More general linear congruential generators use the basic rule  $n \rightarrow Mod[an + b, m]$ , and in this case, n = 0 is no longer special, and a repetition period of exactly m can be achieved with appropriate choices of a, b and m. Note that if the period is equal to its absolute maximum of m, then every possible n is always visited, whatever n one starts from. Page 962 showed diagrams that represent the evolution for all possible starting values of *n*.

Each point in the 2D plots in the main text has coordinates of the form  $\{n[i], n[i+1]\}$  where n[i+1] = Mod[an[i], m]. If one could ignore the Mod, then the coordinates would simply be {n[i], an[i]}, so the points would lie on a single straight line with slope a. But the presence of the Mod takes the points off this line whenever  $a n[i] \ge m$ . Nevertheless, if a is small, there are long runs of n[i] for which the Mod is never important. And that is why in the case a = 3 the points in the plot fall on

In the case a = 65539, the points lie on planes in 3D. The reason for this is that

```
n[i+2] == Mod[65539^2 n[i], 2^{31}] ==
  Mod[6 n[i + 1] - 9 n[i], 2^{31}]
```

so that in computing n[i + 2] from n[i + 1] and n[i] only small coefficients are involved.

It is a general result related to finding short vectors in lattices that for some d the quantity n[i+d] can always be written in terms of the n[i+k]/; k < d using only small coefficients. And as a consequence, the points produced by any linear congruential generator must lie on regular hyperplanes in some number of dimensions.

(For cryptanalysis of linear congruential generators see page

Linear feedback shift registers. Used since the particularly in special-purpose electronic devices, these systems are effectively based on running additive cellular automata such as rule 60 in registers with a limited number of cells and with a certain type of spiral boundary conditions. In a typical case, each cell is updated using

LFSRStep[list ] := Append[Rest[list], Mod[list[[1]] + list[[2]], 2]]

with a step of cellular automaton evolution corresponding to the result of updating all cells in the register. As with additive cellular automata, the behavior obtained depends greatly on the length n of the register. The maximal repetition period of  $2^{n}$  - 1 can be achieved only if  $Factor[1 + x + x^{n}, Modulus \rightarrow 2]$ finds no factors. (For n < 512, this is true when n = 1, 2, 3, 4, 6, 7, 9, 15, 22, 28, 30, 46, 60, 63, 127, 153, 172, 303 or 471. Maximal period is assured when in addition  $PrimeQ[2^n - 1]$ .) The pictures below show the evolution obtained for n = 30with

NestList[Nest[LFSRStep, #, n] &. Append[Table[0, {n - 1}], 1], t]

![](Images/_page_990_Figure_6.jpeg)

Like additive cellular automata as discussed on page 951, states in a linear feedback shift register can be represented by a polynomial FromDigits[list, x]. Starting from a single 1, the state after t steps is then given by

PolynomialMod[ $x^t$ , {1 + x +  $x^n$ , 2}]

This result illustrates the analogy with linear congruential generators. And if the distribution of points generated is studied with the Cantor set geometry, the same kind of problems occur as in the linear congruential case (compare page 1094).

In general, linear feedback shift registers can have "taps" at any list of positions on the register, so that their evolution is given by

LFSRStep[taps\_List, list\_] := Append[Rest[list], Mod[Apply[Plus, list[[taps]]], 2]]

(With taps specified by the positions of 1's in a vector of 0's, the inside of the Mod can be replaced by vec . list as on page 1087.) For a register of size n the maximal period of  $2^n - 1$  is obtained whenever  $x^n + Apply[Plus, x^{taps-1}]$  is one of the  $EulerPhi[2^n-1]/n$  primitive polynomials that appear in Factor [Cyclotomic [ $2^n - 1$ , x], Modulus  $\rightarrow 2$ ]. (See pages 963) and 1084.)

One can also consider nonlinear feedback shift registers, as discussed on page 1088.

Generalized Fibonacci generators. It was suggested in the late 1950s that the Fibonacci sequence  $f[n_{-}] := f[n-1] + f[n-2]$ 

modulo  $2^k$  might be used with different choices of f[0] and f[1] as a random number generator (see page 891). This particular idea did not work well, but generalizations based on the recurrence  $f[n_{-}] := Mod[f[n-p] + f[n-q], 2^{k}]$  have been studied extensively, for example with p = 24, q = 55. Such generators are directly related to linear feedback shift registers, since with a list of length q, each step is simply

 $Append[Rest[list], Mod[list[[1]] + list[[q-p+1]], 2^k]]$ 

Cryptographic generators. As discussed on page 598, so-called stream cipher cryptographic systems work essentially by generating a repeatable random sequence. Practical stream cipher systems can thus be used as random number generators. Starting in the 1980s, the most common example has been the Data Encryption Standard (DES) introduced by the U.S. government (see page 1085). Unless special-purpose hardware is used, however, this method has not usually been efficient enough for practical random number generation applications.

Quadratic congruential generators. Several generalizations of linear congruential generators have been considered in which nonlinear functions of n are used at each step. In fact, the first known generator for digital computers was John von Neumann's "middle square method"

 $n \rightarrow FromDigits[Take[IntegerDigits[n^2, 10, 20], \{5, 15\}], 10]$ In practice this generator has too short a repetition period to be useful. But in the early 1980s studies of public key cryptographic systems based on number theoretical problems led to some reinvestigation of quadratic congruential generators. The simplest example uses the rule

 $n \rightarrow Mod[n^2, m]$ 

It was shown that for m = pq with p and q prime the sequence Mod[n, 2] was in a sense as difficult to predict as the number m is to factor (see page 1090). But in practice, the period of the generator in such cases is usually too short to be useful. In addition, there has been the practical problem that if n is stored on a computer as a 32-bit number, then  $n^2$  can be 64 bits long, and so cannot be stored in the same way. In general, the period divides CarmichaelLambda[CarmichaelLambda[m]]. When m is a prime, this implies that the period can then be as long as (m-3)/2. The largest m less than  $2^{16}$  for which this is true is 65063, and the sequence generated in this case appears to be fairly random.

Cellular automaton generators. I invented the rule 30 cellular automaton random number generator in 1985. Since that time the generator has become quite widely used for a variety of applications. Essentially all the other generators discussed here have certain linearity properties which allow for fairly complete analysis using traditional mathematical methods. Rule 30 has no such properties. Empirical studies, however, suggest that the repetition period, for example, is about  $2^{0.63n}$ , where n is the number of cells (see page 260). Note that rule 45 can be used as an alternative to rule 30. It has a somewhat longer period, but does not mix up nearby initial conditions as quickly as rule 30. (See also page 603.)

■ **Unequal probabilities.** Given a sequence a of n equally probable 0's and 1's, the following generates a single 0 or 1 with probabilities approximating  $\{1-p, p\}$  to n digits:

 $Fold[\{BitAnd, BitOr\}[1 + First[#2]][#1, Last[#2]] \&, 0, \\ Reverse[Transpose[\{First[Real Digits[p, 2, n, -1]], a\}]]]$ 

This can be generalized to allow a whole sequence to be generated with as little as an average of two input digits being used for each output digit.

- Page 323 · Sources of repeatable randomness. In using repeatability to test for intrinsic randomness generation, one must avoid systems in which there is essentially some kind of static randomness in the environment. Sources of this include the profile of a rough solid surface, or the detailed patterns of grains inside a solid.
- Page 324 · Probabilistic rules. There appears to be a discrete transition as a function of the size of the perturbations, similar to phase transitions seen in the phenomenon of directed percolation. Note that if one just uses the original cellular automata rules, then with any nonzero probability of reversing the colors of cells, the patterns will be essentially destroyed. With more complicated cellular automaton rules, one can get behavior closer to the continuous cellular automata shown here. (See also page 591.)
- Page 325 · Noisy cellular automata. In correspondence with electronics, the continuous cellular automata used here can be thought of as analog models for digital cellular automata. The specific form of the continuous generalization of the modulo 2 function used is

 $\lambda[x_{-}] := Exp[-10(x-1)^{2}] + Exp[-10(x-3)^{2}]$ 

Each cell in the system is then updated according to  $\lambda[a+c]$  for rule 90, and  $\lambda[a+b+c+bc]$  for rule 30. Perturbations of size  $\delta$  are then added using  $v + Sign[v - 1/2]Random[]\delta$ .

Note that the basic approach used here can be extended to allow discrete cellular automata to be approximated by partial differential equations where not only color but also space and time are continuous. (Compare page 464.)

■ Page 326 · Repeatably random experiments. Over the years, I have asked many experimental scientists about repeatability in seemingly random data, and in almost all cases they have told me that they have never looked for such a thing. But in a

few cases they say that in fact on thinking about it they remember various forms of repeatability.

Examples where I have seen evidence of repeatable randomness as a function of time in published experimental data include temperature differences in thermal convection in closed cells of liquid helium, reaction rates in oxidation of carbon monoxide on catalytic surfaces, and output voltages from firings of excited single nerve cells. Typically there are quite long periods of time where the behavior is rather accurately repeatable—even though it may wiggle tens or hundreds in a seemingly random way—interspersed with jumps of some kind. In most cases the only credible models seem to be ones based on intrinsic randomness generation. But insofar as there is any definite model, it is inevitable that looking in sufficient detail at sufficiently many components of the system will reveal regularities associated with the underlying mechanism.

#### The Phenomenon of Continuity

- Discreteness in computer programs. The reason for discreteness in computer programs is that the only real way we know how to construct such programs is using discrete logical structures. The data that is manipulated by programs can be continuous, as can the elements of their rules. But at some level one always gives discrete symbolic descriptions of the logical structure of programs. And it is then certainly more consistent to make both data and programs involve only discrete elements. In Chapter 12 I will argue that this approach is not only convenient, but also necessary if we are to represent our computations using processes that can actually occur in nature.
- **Central Limit Theorem.** Averages of large collections of random numbers tend to follow a Gaussian or normal distribution in which the probability of getting value *x* is

 $Exp[-(x - \mu)^2/(2\sigma^2)]/(Sqrt[2\pi]\sigma)$ 

The mean  $\mu$  and standard deviation  $\sigma$  are determined by properties of the random numbers, but the form of the distribution is always the same. The only conditions are that the random numbers should be statistically independent, and that their distribution should have bounded variance, so that, for example, the probability for very large numbers is rapidly damped. (The limit of an infinite collection of numbers gives  $\sigma \rightarrow 0$  in accordance with the law of large numbers.) The pictures at the top of the next page show how averages of successively larger collections of uniformly distributed numbers converge to a Gaussian distribution.

![](Images/_page_992_Picture_2.jpeg)

The Central Limit Theorem leads to a self-similarity property for the Gaussian distribution: if one takes n numbers that follow Gaussian distributions, then their average should also follow a Gaussian distribution, though with a standard deviation that is  $1/\sqrt{n}$  times smaller.

- History. That averages of random numbers follow bellshaped distributions was known in the late 1600s. The formula for the Gaussian distribution was derived by Abraham de Moivre around 1733 in connection with theoretical studies of gambling. In the late 1700s Pierre-Simon Laplace did this again to predict the distribution of comet orbits, and showed that the same results would be obtained for other underlying distributions. Carl Friedrich Gauss made connections to the distribution of observational errors, and the relevance of the Gaussian distribution to biological and social systems was noted. Progressively more general proofs of the Central Limit Theorem were given from the early 1800s to the 1930s. Many natural systems were found to exhibit Gaussian distributions—a typical example being height distributions for humans. (Weight distributions are however closer to lognormal; compare page 1003.) And when statistical methods such as analysis of variance became established in the early 1900s it became increasingly common to assume underlying Gaussian distributions. (Gaussian distributions were also found in statistical mechanics in the late 1800s.)
- Related results. Gaussian distributions arise when large numbers of random variables get added together. If instead such variables (say probabilities) get multiplied together what arises is the lognormal distribution

 $Exp[-(Log[x]-\mu)^2/(2\sigma^2)]/(Sqrt[2\pi]x\sigma)$ 

For a wide range of underlying distributions the extreme values in large collections of random variables follow the Fisher-Tippett distribution

 $Exp[(x-\mu)/\beta] Exp[-Exp[(x-\mu)/\beta]]/\beta$ 

related to the Weibull distribution used in reliability analysis.

For large symmetric matrices with random entries following a distribution with mean 0 and bounded variance the density of normalized eigenvalues tends to Wigner's semicircle law

 $2 \operatorname{Sqrt}[1-x^2] \operatorname{UnitStep}[1-x^2]/\pi$ 

while the distribution of spacings between tends to  $1/2(\pi x) Exp[1/4(-\pi)x^2]$ 

The distribution of largest eigenvalues can often be expressed in terms of Painlevé functions.

(See also 1/f noise on page 969.)

■ Page 328 · Random walks. In one dimension, a random walk with t steps of length 1 starting at position 0 can be generated

NestList[# + (-1) ^ Random[Integer] &, 0, t] or equivalently

FoldList[Plus, 0, Table[(-1) ^ Random[Integer], {t}]]

A generalization to d dimensions is then

FoldList[Plus, Table[0, {d}], Table[RotateLeft[PadLeft[ {(-1)^Random[Integer]}, d], Random[Integer, d - 1]], {t}]]

A fundamental property of random walks is that after *t* steps the root mean square displacement from the starting position is proportional to  $\sqrt{t}$ . In general, the probability distribution for the displacement of a particle that executes a random

With  $[\{\sigma = 1\}, (d/(2\pi\sigma t))^{d/2} \exp[-dr^2/(2\sigma t)]]$ 

The same results are obtained, with a different value of  $\sigma$ , for other random microscopic rules, so long as the variance of the distribution of step lengths is bounded (as in the Central Limit Theorem).

As mentioned on page 1082, the frequency spectrum Abs[Fourier[list]]<sup>2</sup> for a 1D random walk goes like  $1/\omega^2$ .

The character of random walks changes somewhat in different numbers of dimensions. For example, in 1D and 2D, there is probability 1 that a particle will eventually return to its starting point. But in 3D, this probability (on a simple cubic lattice) drops to about 0.341, and in d dimensions the probability falls roughly like 1/(2d). After a large number of steps t, the number of distinct positions visited will be proportional to t, at least above 2 dimensions (in 2D, it is proportional to t/Log[t] and in 1D  $\sqrt{t}$ ). Note that the outer boundaries of patterns like those on page 330 formed by n random walks tend to become rougher when t is much larger than Log[n].

To make a random walk on a lattice with k directions in two dimensions, one can set up

 $e = Table[\{Cos[2 \pi s/k], Sin[2 \pi s/k]\}, \{s, 0, k-1\}]$ then use

FoldList[Plus, {0, 0}, Table[e[[Random[Integer, {1, k}]]], {t}]]

It turns out that on any regular lattice, in any number of dimensions, the average behavior of a random walk is always isotropic. As discussed in the note below, this can be viewed as a consequence of the fact that the probability distribution in a random walk depends only on

Sum[Outer[Times, e[[s]], e[[s]]], {s, Length[e]}] and not on products of more of the e[[s]].

There are nevertheless some properties of random walks that are not isotropic. The picture below, for example, shows the

so-called extreme value distribution of positions furthest from the origin reached after 10 steps and 100 steps by random walks on various lattices.

![](Images/_page_993_Picture_2.jpeg)

![](Images/_page_993_Picture_3.jpeg)

![](Images/_page_993_Picture_4.jpeg)

![](Images/_page_993_Picture_5.jpeg)

![](Images/_page_993_Picture_6.jpeg)

In the pictures in the main text, all particles start out at a particular position, and progressively spread out from there. But in general, one can consider sources that emit new particles every step, or absorbers and reflectors of particles. The average distribution of particles is given in general by the diffusion equation shown on page 163. The solutions to this equation are always smooth and continuous.

A physical example of an approximation to a random walk is the spreading of ink on blotting paper.

■ Self-avoiding walks. Any walk where the probabilities for a given step depend only on a fixed number of preceding steps gives the same kind of limiting Gaussian distribution. But imposing the constraint that a walk must always avoid anywhere it has been before (as for example in an idealized polymer molecule) leads to correlations over arbitrary times. If one adds individual steps at random then in 2D one typically gets stuck after perhaps a few tens of steps. But tricks are known for generating long self-avoiding walks by combining shorter walks or successively pivoting pieces starting with a simple line. The pictures below show some 1000-step examples. They look in many ways similar to ordinary random walks, but their limiting distribution is no longer strictly Gaussian, and their root mean square displacement after t steps varies like  $t^{3/4}$ . (In  $d \le 4$ dimensions the exponent is close to the Flory mean field theory value 3/(2+d); for d>4 the results are the same as without self-avoidance.)

![](Images/_page_993_Picture_10.jpeg)

![](Images/_page_993_Picture_11.jpeg)

![](Images/_page_993_Picture_12.jpeg)

■ Page 331 · Basic aggregation model. This model appears to have first been described by Murray Eden in 1961 as a way of studying biological growth, and was simulated by him on a computer for clusters up to about 32,000 cells. By the mid-1980s clusters with a billion cells had been grown, and a very surprising slight anisotropy had been observed. The pictures below show which cells occur in more than 10% of 1000

randomly grown clusters. There is a 2% or so anisotropy that appears to remain essentially fixed for clusters above perhaps a million cells, tucking them in along the diagonal directions. The width of the region of roughness on the surface of each cluster varies with the radius of the cluster approximately like  $r^{1/3}$ . The most extensive use of the model in practice has been for studying tumor growth: currently a typical tumor at detection contains about a billion cells, and it is important to predict what protrusions there will be that can break off and form additional tumors elsewhere.

![](Images/_page_993_Picture_15.jpeg)

![](Images/_page_993_Picture_16.jpeg)

![](Images/_page_993_Picture_17.jpeg)

![](Images/_page_993_Figure_18.jpeg)

■ **Implementation.** One way to represent a cluster is by giving a list of the coordinates at which each black cell occurs. Then starting with a single black cell at the origin, represented by {{0, 0}}, the cluster can be grown for t steps as follows:

 $AEvolve[t_{-}] := Nest[AStep, \{\{0, 0\}\}, t]$ 

AStep[c\_] := (If[! MemberQ[c, #], Append[c, #], 

f[a\_] := a[[Random[Integer, {1, Length[a]}]]]

This implementation can easily be extended to any type of lattice and any number of dimensions. Even with various additional optimizations, it is remarkable how much slower it is to grow a cluster with a model that requires external random input than to generate similar patterns with models such as cellular automata that intrinsically generate their own randomness.

The implementation above is a so-called type B Eden model in which one first selects a cell in the cluster, then randomly selects one of its neighbors. One gets extremely similar results with a type A Eden model in which one just randomly selects a cell from all the ones adjacent to the cluster. With a grid of cells set up in advance, each step in this type of Eden model can be achieved with

AStep[a\_] := ReplacePart[a, 1, (#[[Random[ Integer, {1, Length[#]}]]] &)[Position[(1-a) Sign[ ListConvolve[{{0, 1, 0}, {1, 0, 1}, {0, 1, 0}}, a, {2, 2}]], 1]]]

This implementation can readily be extended to generalized aggregation models (see below).

■ Page 332 · Generalized aggregation models. One can in general have rules in which new cells can be added only at positions whose neighborhoods match specific templates (compare page 213). There are 32 possible symmetric such rules with just 4 immediate neighbors—of which 16 lead to growth (from any seed), and all seem to yield at least

approximately circular clusters (of varying densities). Without symmetry, all sorts of shapes can be obtained, as in the pictures below. (The rule numbers here follow the scheme on page 927 with offsets {{-1, 0}, {0, -1}, {0, 1}, {1, 0}}). Note that even though the underlying rule involves randomness definite geometrical shapes can be produced. An extreme case is rule 2, where only a single neighborhood with a single black cell is allowed, so that growth occurs along a single line.

![](Images/_page_994_Picture_3.jpeg)

![](Images/_page_994_Picture_4.jpeg)

![](Images/_page_994_Picture_5.jpeg)

![](Images/_page_994_Picture_6.jpeg)

![](Images/_page_994_Picture_7.jpeg)

If one puts conditions on where cells can be added one can in principle get clusters where no further growth is possible. This does not seem to happen for rules that involve 4 neighbors, but with 8 neighbors there are cases in which clusters can get fairly large, but end up having no sites where further cells can be added. The pictures below show examples for a rule that allows growth except when there are exactly 1, 3 or 4 neighbors (totalistic constraint 242).

![](Images/_page_994_Picture_9.jpeg)

![](Images/_page_994_Picture_10.jpeg)

![](Images/_page_994_Picture_11.jpeg)

![](Images/_page_994_Picture_12.jpeg)

![](Images/_page_994_Picture_13.jpeg)

The question of what ultimate forms of behavior can occur with any sequence of random choices, starting from a given configuration with a given rule, is presumably in general undecidable. (It has some immediate relations to tiling problems and to halting problems for non-deterministic Turing machines.) With the rule illustrated above, however, those clusters that do successfully grow exhibit complicated and irregular shapes, but nevertheless eventually seem to take on a roughly circular shape, as in the pictures below.

![](Images/_page_994_Picture_15.jpeg)

![](Images/_page_994_Picture_16.jpeg)

![](Images/_page_994_Picture_17.jpeg)

![](Images/_page_994_Picture_18.jpeg)

![](Images/_page_994_Picture_19.jpeg)

At some level the basic aggregation model of page 331 has a deterministic outcome: after sufficiently many steps every cell will be black. But most generalized aggregation models do not have this property: instead, the form of their internal patterns depends on the sequence of random choices made. Particularly with more than two colors it is however possible to arrange that the internal pattern always ends up being the same, or at least has patches that are the same—essentially by

using rules with the confluence property discussed on page

The pictures below show 1D generalized aggregation systems with various templates. The second one is the analog of the system from page 331.

![](Images/_page_994_Figure_23.jpeg)

![](Images/_page_994_Figure_24.jpeg)

![](Images/_page_994_Figure_25.jpeg)

![](Images/_page_994_Figure_26.jpeg)

■ Page 333 · Diffusion-limited aggregation (DLA). While many 2D cellular automata produce intricate nested shapes, the aggregation models shown here seem to tend to simple limiting shapes. Most likely there are some generalized aggregation models for which this is not the case. And indeed this phenomenon has been seen in other systems with randomness in their underlying rules. An example studied extensively in the 1980s is diffusion-limited aggregation (DLA). The idea of this model is to add cells to a cluster one at a time, and to determine where a cell will be added by seeing where a random walk that starts far from the cluster first lands on a square adjacent to the cluster. An example of the behavior obtained in this model is shown below:

![](Images/_page_994_Figure_28.jpeg)

![](Images/_page_994_Picture_29.jpeg)

The lack of smooth overall behavior in this case can perhaps be attributed to the global probing of the cluster that is effectively done by each incoming random walk. (See also page 994.)

■ Page 334 · Code 746. Much as in the aggregation model above, the pictures below show that there is a slight deviation from perfect circular growth, with an anisotropy that appears to remain roughly fixed at perhaps 4% above a few thousand steps (corresponding to patterns with a few million cells).

![](Images/_page_994_Figure_32.jpeg)

![](Images/_page_994_Figure_33.jpeg)

■ Other rules. The pictures below show patterns generated after 10,000 steps with several rules, starting respectively from rows of 7, 6, 7 and 11 cells (compare pages 177 and 181). The outer boundaries are somewhat smooth, though definitely not circular. In the second rule shown, the interior of the pattern always continues to change; in the others it remains essentially fixed.

![](Images/_page_995_Picture_2.jpeg)

![](Images/_page_995_Picture_3.jpeg)

![](Images/_page_995_Picture_4.jpeg)

![](Images/_page_995_Picture_5.jpeg)

■ **Isotropy.** Any pattern grown from a single cell according to rules that do not distinguish different directions on a lattice

must show the same symmetry as the lattice. But we have seen that in fact many rules actually yield almost circular patterns with much higher symmetry. One can characterize the symmetry of a pattern by taking the list *v* of positions of cells it contains, and looking at tensors of successive ranks *n*:

pply[Plus,

Map[Apply[Outer[Times, ##] &, Table[#, {n}]] &, v]]

For circular or spherical patterns that are perfectly isotropic in d dimensions these tensors must all be proportional to

(d-2)!! Array[Apply[Times, Map] (1 - Mod[#, 2]) (# - 1)!! &. Table[Count[{##}, i], {i, d}]]] &, Table[d, {n}]]/(d + n - 2)!! For odd n this is inevitably true for any lattice with mirror symmetry. But for even n it can fail. For a square lattice, it still nevertheless always holds up to n = 2 (so that the analogs of moments of inertia satisfy  $I_{xx} = I_{yy}$ ,  $I_{xy} = I_{yx} = 0$ ). And for a hexagonal lattice it holds up to n = 4. But when n = 4 isotropy requires the {1, 1, 1, 1} and {1, 1, 2, 2} tensor components to have ratio  $\beta = 3$ —while square symmetry allows these components to have any ratio. (In general there will be more than one component unless the representation of the lattice symmetry group carried by the rank n tensor is irreducible.) In 3D no regular lattice forces isotropy beyond n = 2, while in 4D the SO(8) lattice works up to n = 4, in 8D the E<sub>8</sub> lattice up to n = 6, and in 24D the Leech lattice up to n = 10. (Lattices that give dense sphere packings tend to show more isotropy.) Note that isotropy can also be characterized using analogs of multipole moments, obtained in 2D by summing  $r_i Exp[in \theta_i]$ , and in higher dimensions by summing appropriate SphericalHarmonicY or GegenbauerC functions. For isotropy, only the n = 0 moment can be nonzero. On a 2D lattice with m directions, all moments are forced to be zero except when m divides n. (Sums of squares of moments of given order in general provide rotationally invariant measures of anisotropy—equal to pair correlations weighted with LegendreP or GegenbauerC functions.)

Even though it is not inevitable from lattice symmetry, one might think that if there is some kind of effective randomness in the underlying rules then sufficiently large patterns would still often show some sort of average isotropy. And at least in the case of ordinary random walks, they do, so that for example, the ratio averaged over all possible walks of n = 4 tensor components after t steps on a square lattice is  $\beta = 3 + 2/(t - 1)$ , converging to the isotropic value 3, and the ratio of n = 6 components is 5 - 4/(t - 1) + 32/(3t - 4). For the aggregation model of page 331,  $\beta$  also decreases with t, reaching 4 around t = 10, but now its asymptotic value is around 3.07.

In continuous systems such as partial differential equations, isotropy requires that coordinates in effect appear only in  $\nabla$ . In most finite difference approximations, there is presumably isotropy in the end, but the rates of convergence are almost inevitably rather different in different directions relative to the lattice.

■ Page 336 · Domains. Some of the effective rules for interfaces between black and white domains are easy to state. Given a flat interface, the layer of cells immediately on either side of this interface behaves like the rule 150 1D cellular automaton. On an infinitely long interface, protrusions of cells with one color into a domain of the opposite color get progressively smaller, eventually leaving only a certain pattern of cells in the layer immediately on one side of the interface. 90 ° corners in an otherwise flat interface effectively act like reflective boundary conditions for the layer of cells on top of the interface.

The phenomenon of domains illustrated here is also found in various 2D cellular automata with 4-neighbor rather than 8-neighbor rules. One example is totalistic code 52, which is a direct analog in the 4-neighbor case of the rule illustrated here. Other examples are outer totalistic codes 111, 293, 295 and 920. The domain boundaries in these cases, however, are not as clear as for the 8-neighbor totalistic rule with code 976 that is shown here.

■ **Spinodal decomposition.** The separation into progressively larger black and white regions seen in the cellular automata shown here is reminiscent of the phenomena that occur for example in the separation of randomly mixed oil and water. Various continuous models of such processes have been proposed, notably the Cahn-Hilliard equation from 1958. One feature often found is that the average radius of "droplets" increases with time roughly like *t* <sup>1/3</sup>.

#### **Origins of Discreteness**

■ Page 339 · 1D transitions. There are no examples of the phenomenon shown here among the 256 rules with two possible colors and depending only on nearest neighbors. Among the 4,294,967,296 rules that depend on next-nearest neighbors, there are a handful of examples, including rules with numbers 4196304428, 4262364716, 4268278316 and 4266296876. The behavior obtained with the first of these rules is shown below. An example that depends on three neighbors on each side was discovered by Peter Gacs, Georgii Kurdyumov and Leonid Levin in 1978, following work on how reliable electronic circuits can be built from unreliable components by Andrei Toom:

$$\{a1_-, a2_-, a3_-, a4_-, a5_-, a6_-, a7_-\} \rightarrow If[If[a4 == 1, a1 + a3 + a4, a4 + a5 + a7] \ge 2, 1, 0]$$

The 4-color rule shown in the text is probably the clearest example available in one dimension. It has rule number 294869764523995749814890097794812493824.

![](Images/_page_996_Picture_6.jpeg)

![](Images/_page_996_Picture_7.jpeg)

![](Images/_page_996_Picture_8.jpeg)

![](Images/_page_996_Picture_9.jpeg)

- Page 340 · 2D transitions. The simplest symmetrical rules (such as 4-neighbor totalistic code 56) which make the new color of a cell be the same as the majority of the cells in its neighborhood do not exhibit the discrete transition phenomenon, but instead lead to fixed regions of black and white. The 4-neighbor rule with totalistic code 52 can be used as an alternative to the second rule shown here. A probabilistic version of the first rule shown here was discussed by Andrei Toom in 1980.
- Phase transitions. The discrete transitions shown in cellular automata in this section are examples of general phenomena known in physics as phase transitions. A phase transition can be defined as any discontinuous change that occurs in a system with a large number of components when a parameter associated with that system is varied. (Some physicists might argue for a somewhat narrower definition that allows only discontinuities in the so-called partition function of equilibrium statistical mechanics, but for many of the most interesting applications, the definition I use is the appropriate one.) Standard examples of phase transitions

include boiling, melting, sublimation (solids such as dry ice turning into gases), loss of magnetization when a ferromagnet is heated, alignment of molecules in liquid crystals above a certain electric field (the basis for liquid crystal displays), and the onset of superconductivity and superfluidity at low temperatures.

It is conventional to distinguish two kinds of phase transitions, often called first-order and higher-order. Firstorder transitions occur when a system has two possible states, such as liquid and gas, and as a parameter is varied, which of these states is the stable one changes. Boiling and melting are both examples of first-order transitions, as is the phenomenon shown in the cellular automaton in the main text. Note that one feature of first-order transitions is that as soon as the transition is passed, the whole system always switches completely from one state to the other.

Higher-order transitions are in a sense more gradual. On one side of the transition, a system is typically completely disordered. But when the transition is passed, the system does not immediately become completely ordered. Instead, its order increases gradually from zero as the parameter is varied. Typically the presence of order is signalled by the breaking of some kind of symmetry-say of rotational symmetry by the spontaneous selection of a preferred direction.

■ The Ising model. The 2D Ising model is a prototypical example of a system with a higher-order phase transition. Introduced by Wilhelm Lenz in 1920 as an idealization of ferromagnetic materials (and studied by Ernst Ising) it involves a square array s of spins, each either up or down (+1 or -1), corresponding to two orientations for magnetic moments of atoms. The magnetic energy of the system is taken to be

$$e[s_{-}] := -1/2 Apply[Plus, s ListConvolve[ {{0, 1, 0}, {1, 0, 1}, {0, 1, 0}, s, 2}, {0, 1}]$$

so that each pair of adjacent spins contributes -1 when they are parallel and +1 when they are not. The overall magnetization of the system is given by  $m[s_{-}] := Apply[Plus, s, \{0, 1\}].$ 

In physical ferromagnetic materials what is observed is that at high temperature, corresponding to high internal energy, there is no overall magnetization. But when the temperature goes below a critical value, spins tend to line up, and an overall magnetization spontaneously develops. In the context of the 2D Ising model this phenomenon is associated with the fact that those configurations of a large array of spins that have high total energy are overwhelmingly likely to have near zero overall magnetization, while those that have low

total energy are overwhelmingly likely to have nonzero overall magnetization. For an  $n \times n$  array s of spins there are a total of  $2^{n^2}$  possible configurations. The pictures below show the results of picking all configurations with a given energy e[s] (cyclic boundary conditions are assumed) and then working out their distribution of magnetization values m[s]. Even for small n the pictures demonstrate that for large e[s]the magnetization m[s] is likely to be close to zero, but for smaller e[s] two branches approaching +1 and -1 appear. In the limit  $n \to \infty$  the distribution of magnetization values becomes sharp, and a definite discontinuous phase transition is observed.

![](Images/_page_997_Figure_3.jpeg)

Following the work of Lars Onsager around 1944, it turns out that an exact solution in terms of traditional mathematical functions can be found in this case. (This seems to be true only in 2D, and not in 3D or higher.) Almost all spin configurations with  $e[s] > -\sqrt{2}$  (where here and below all quantities are divided by the total number of spins, so that  $-2 \le e[s] \le 2$  and  $-1 \le m[s] \le +1$ ) yield m[s] == 0. But for smaller e[s] one can show that

```
Abs[m[s]] == (1 - Sinh[2 \beta]^{-4})^{1/8}
where \beta can be deduced from
   e[s] = -(Coth2\beta
                     (-1 + 2 Tanh[2 \beta]^2)/\pi)
```

This implies that just below the critical point  $e_0 = -\sqrt{2}$  (which corresponds to  $\beta = Log[1 + \sqrt{2}]/2$ ) Abs[m]  $\sim (e_0 - e)^{1/8}$ , where here 1/8 is a so-called critical exponent. (Another analytical result is that for  $e \sim e_0$  correlations between pairs of spins can be expressed in terms of Painlevé functions.)

Despite its directness, the approach above of considering sets of configurations with specific energies e[s] is not how the Ising model has usually been studied. Instead, what has normally been done is to take the array of spins to be in thermal equilibrium with a heat bath, so that, following standard statistical mechanics, each possible spin configuration occurs with probability  $Exp[-\beta e[s]]$ , where  $\beta$  is inverse temperature. It nevertheless turns out that in the limit  $n \to \infty$  this so-called canonical ensemble approach yields the same results for most quantities as the microcanonical approach that I have used;  $\beta$ simply appears as a parameter, as in the formulas above.

About actual spin systems evolving in time the Ising model itself does not make any statement. But whenever the evolution is ergodic, so that all states of a given energy are visited with equal frequency, the average behavior obtained will at least eventually correspond to the average over all states discussed above.

In Monte Carlo studies of the Ising model one normally tries to sample states with appropriate probabilities by randomly flipping spins according to a procedure that can be thought of as emulating interaction with a heat bath. But in most actual physical spin systems it seems unlikely that there will be so much continual interaction with the environment. And from my discussion of intrinsic randomness generation it should come as no surprise that even a completely deterministic rule for the evolution of spins can make the system visit possible states in an effectively random way.

Among the simplest possible types of rules all those that conserve the energy e[s] turn out to have behavior that is too simple and regular. And indeed, of the 4096 symmetric 5neighbor rules, only identity and complement conserve e[s]. Of the  $2^{32}$  general 5-neighbor rules 34 conserve e[s]—but all have only very simple behavior. (Compositions of several such rules can nevertheless yield complex behavior. Note that as indicated on page 1022, 34 of the 256 elementary 1D rules conserve the analog of e[s].) Of the 262,144 9-neighbor outer totalistic rules the only ones that conserve e[s] are identity and complement. But among all  $2^{512}$  9-neighbor rules, there are undoubtedly examples that show effectively random behavior. One marginally more complicated case effectively involving 13 neighbors is

```
IsingEvolve[list_, t_Integer] :=
     First[Nest[IsingStep, {list, Mask[list]}, t]]
   IsingStep[{a_, mask_}] := {MapThread[
      If [#2 == 2 && #3 == 1, 1 - #1, #1] &, {a, ListConvolve[
         \{\{0,\,1,\,0\},\,\{1,\,0,\,1\},\,\{0,\,1,\,0\}\},\,a,\,2],\,mask\,\},\,2],\,1-mask\,\}
where
```

 $Mask[list_] := Array[Mod[#1 + #2, 2] &, Dimensions[list]]$ is set up so that alternating checkerboards of cells are updated on successive steps.

One can see a phase transition in this system by looking at the dependence of behavior on conserved total energy e[s]. If there are no correlations between spins, and a fraction p of them are +1, then m[s] = p and  $e[s] = -2(1-2p)^2$ . And since the evolution conserves e[s] changing the initial value of p allows one to sample different total energies. But since the evolution does not conserve m[s] the average of this after many steps can be expected to be typical of all possible states of given e[s].

The pictures at the top of the next page show the values of m[s] (densities of +1 cells) after 0, 10, 100 and 1000 steps for a  $500 \times 500$  system as a function of the initial values of m[s]and e[s]. Also shown is the result expected for an infinite system at infinite time. (The slow approach to this limit can be viewed as being a consequence of smallness of finite size scaling exponents in Ising-like systems.)

![](Images/_page_998_Figure_3.jpeg)

The phase transition in the Ising model is associated with a lack of smoothness in the dependence of the final m value on e or the initial value p of m in limiting cases of the pictures above. The transition occurs at  $e = -\sqrt{2}$ , corresponding to  $p = (1 \pm 2^{-1/4})/2$ . The pictures show typical configurations generated after 1000 steps from various initial densities, as well as slices through their evolution.

![](Images/_page_998_Figure_5.jpeg)

And what one sees at least roughly is that right around the phase transition there are patches of black and white of all sizes, forming an approximately nested random pattern. (See also pages 989 and 1149.)

■ General features of phase transitions. To reproduce the Ising model, a cellular automaton must have several special properties. In addition to conserving energy, its evolution must be reversible in the sense discussed on page 435. And with the constraint of reversibility, it turns out that it is impossible to get a non-trivial phase transition in any 1D system with the kind of short-range interactions that exist in a cellular automaton. But in systems whose evolution is not reversible, it is possible for phase transitions to occur in 1D, as the examples in the main text show.

One point to notice is that the sharp change which characterizes any phase transition can only be a true discontinuity in the limit of an infinitely large system. In the case of the system on page 339, for example, it is possible to find special configurations with a finite total number of cells which lead to behavior opposite to what one expects purely on the basis of their initial density of black cells. When the total number of cells increases, however, the fraction of such configurations rapidly decreases, and in the infinite size limit, there are no such configurations, and a truly discontinuous transition occurs exactly at density 1/2.

The discrete nature of phase transitions was at one time often explained as a consequence of changes in the symmetry of a system. The idea is that symmetry is either present or absent, and there is no continuous variation of level of symmetry possible. Thus, for example, above the transition, the Ising model treats up and down spins exactly the same. But below the transition, it effectively makes a choice of one spin direction or the other. Similarly, when a liquid freezes into a crystalline solid, it effectively makes a choice about the alignment of the crystal in space. But in boiling, as well as in a number of model examples, there is no obvious change of symmetry. And from studying phase transitions in cellular automata, it does not seem that an interpretation in terms of symmetry is particularly useful.

A common feature of phase transitions is that right at the transition point, there is competition between both phases, and some kind of nested structure is typically formed, as discussed on page 273 and above. The overall form and fractal dimension of this nested structure is typically independent of small-scale features of the system, making it fairly universal, and amenable to analysis using the renormalization group approach (see page 955).

■ Percolation. A simple example of a phase transition studied extensively since the 1950s involves taking a square lattice and filling in at random a certain density of black cells. In the limit of infinite size, there is a discrete transition at a density of about 0.592746, with zero probability below the transition to find a connected "percolating" cluster of black cells spanning the lattice, and unit probability above. (For a triangular lattice the critical density is exactly 1/2.) One can also study directed percolation in which one takes account of the connectivity of cells only in one direction on the lattice. (Compare the probabilistic cellular automata on pages 325 and 591. Note that the evolution of such systems is also analogous to the process of applying transfer matrices in studies of spin systems like Ising models.)

- Page 341 · Rate equations. In standard chemical kinetics one assumes that molecules are uniformly distributed in space, so that the rates for particular reactions are proportional to the products of the densities of the molecules that react in them. Conditions for equilibrium where rates balance thus tend to be polynomial equations for densities—with discontinuous jumps in solutions sometimes occurring as parameters are changed. Analogous equations arise in probabilistic approximations to systems like cellular automata, as on page 953. But here—as well as in fast chemical reactions—correlations in spatial arrangements of elements tend to be important, invalidating simple probabilistic approaches. (For the cellular automaton on page 339 the simple condition for equilibrium is  $p = p^2 (3-2p)$ , which correctly implies that 0, 1/2 and 1 are possible equilibrium densities.)
- Discreteness in space. Many systems with continuous underlying rules generate discrete cellular structures in space. One common mechanism is for a wave of a definite wavelength to form (see page 988), and then for some feature of each cycle of this wave to be picked out, as in the picture below. In Chladni figures of sand on vibrating plates and in cloud streets in the atmosphere what happens is that material collects at points of zero displacement. And when a stream of water breaks up into discrete drops what happens is that oscillation minima yield necks that break.

![](Images/_page_999_Picture_3.jpeg)

Superpositions of waves at different angles can lead to various 2D cellular structures, as in the pictures below (compare page 1078).

![](Images/_page_999_Picture_5.jpeg)

Various forms of focusing and accumulation can also lead to discreteness in continuous systems. The first picture below shows a caustic or catastrophe in which a continuous distribution of light rays are focused by a circular reflector onto a discrete line with a cusp. The second picture shows a shock wave produced by an accumulation of circular waves emanating from a moving object—as seen in wakes of ships, sonic booms from supersonic aircraft, and Cerenkov light from fast-moving charged particles.

![](Images/_page_999_Picture_7.jpeg)

![](Images/_page_999_Picture_8.jpeg)

#### The Problem of Satisfying Constraints

- Rules versus constraints. See page 940.
- NP completeness. Finding 2D patterns that satisfy the constraints in the previous section is in general a so-called NP-complete problem. And this means that no known algorithm can be expected to solve this problem exactly for a size *n* array (say with given boundaries) in much less than 2<sup>n</sup> steps (see page 1145). The same is true even if one allows a small fraction of squares to violate the constraints. However, the 1D version of the problem is not NP-complete, and in fact there is a specific rather efficient algorithm described on page 954 for solving it. Nevertheless, the procedures discussed in this section do not manage to make use of such specific algorithms, and in fact typically show little difference between problems that are and are not formally NP-complete.
- **Page 343** · **Distribution.** The distribution shown here rapidly approaches a Gaussian. (Note that in a  $5 \times 5$  array, there are 10 interior squares that are subject to the constraints, while in a  $10 \times 10$  array there are 65.) Very similar results seem to be obtained for constraints in a wide range of discrete systems.
- Page 346 · Implementation. The number of squares violating the constraint used here is given by

Cost[list\_] := Apply[Plus, Abs[list - RotateLeft[list]]]

When applied to all possible patterns, this function yields a distribution with Gaussian tails, but with a sharp point in the middle. Successive steps in the iterative procedure used on this page are given by

 $Move[list_] := (If[Cost[#] < Cost[list], #, list] &)[ \\ MapAt[1-# &, list, Random[Integer, {1, Length[list]}]]] \\ while those in the procedure on page 347 have <math>\leq$  in place of

 ${<}$  . The third curve shown on page 346 is obtained from

Table[Cost[IntegerDigits[i, 2, n]],  $\{i, 0, 2^n - 1\}$ ]

There is no single ordering that makes all states which can be reached by changing a single square be adjacent. However, the ordering defined by *GrayCode* from page 901 does do this for one particular sequence of single square changes. The resulting curve is very similar to what is already shown.

■ Page 347 · Iterative improvement. The borders of the regions of black and white in the picture shown here essentially

follow random walks and annihilate in pairs so that their number decreases with time like  $1/\sqrt{t}$ . In 2D the regions are more complicated and there is no such simple behavior. Indeed starting from a particular state it is for example not clear whether it is ever possible to reach all other states.

■ Gradient descent. A standard method for finding a minimum in a smooth function f[x] is to use

FixedPoint[# - a f'[#] &,  $x_0$ ]

If there are local minima, then which one is reached will depend on the starting point  $x_0$ . It will not necessarily be the one closest to  $x_0$  because of potentially complicated overshooting effects associated with the step size a. Newton's method for finding zeros of f[x] is related and is given by

FixedPoint[# - f[#]/f'[#] &,  $x_0$ ]

■ Combinatorial optimization. The problem of coming as close as possible to satisfying constraints in an arrangement of black and white squares is a simple example of a combinatorial optimization problem. In general, such problems involve minimization of a quantity that is determined by the arrangement of some set of discrete elements. A typical example is finding a placement of components in a 2D circuit so that the total length of wire necessary to the connect these components is minimized (related to the so-called travelling salesman problem). In using iterative procedures to solve combinatorial optimization problems, one issue is what kind of changes should be made at each step. In the main text we considered changing just one square at a time. But one can also change larger numbers of squares, or, for example, interchange whole blocks of squares. In general, the larger the changes made, the faster one can potentially approach a minimum, but the greater the chance is of overshooting. In the main text, we assumed that at each step we should always move closer to the minimum, or at least not get further away. But in trying to get over the kind of bumps shown in the third curve on page 346 it is sometimes better also to allow some probability of moving away from the minimum at a particular step. One approach is simulated annealing, in which one starts with this probability being large, and progressively decreases it. The notion is that at the beginning, one wants to move easily over the coarse features of a jagged curve, but then later home in on details. If the curve has a nested form, which appears to be the case in some combinatorial optimization problems, then this scheme can be expected to be at least somewhat effective. For the problems considered in the main text, simulated annealing provides some improvement but not much.

- Biologically motivated schemes. The process of biological evolution by natural selection can be thought of as an iterative procedure for optimization. Usually, however, what is being optimized is some aspect of the form or behavior of an organism, which represents a very complicated constraint on the underlying genetic material. (It is as if one is defining constraints on the initial conditions for a cellular automaton by looking at the pattern generated by the cellular automaton after a long time.) But the strategies of biological evolution can also be used in trying to satisfy simpler constraints. Two of the most important strategies are maintaining a whole population of individuals, not just the single best result so far, and using sex to produce large-scale mixing. But once again, while these strategies may in some cases lead to greater efficiency, they do not usually lead to qualitative differences. (See also page 1105.)
- History. Work on combinatorial optimization started in earnest in the late 1950s, but by the time NP completeness was discovered in 1971 (see page 1143) it had become clear that finding exact solutions would be very difficult. Approximate methods tended to be constructed for specific problems. But in the early 1980s, simulated annealing was suggested by Scott Kirkpatrick and others as one of the first potentially general approaches. And starting in the mid-1980s, extensive work was done on biologically motivated so-called genetic algorithms, which had been advocated by John Holland since the 1960s. Progress in combinatorial optimization is however often difficult to recognize, because there are almost no general results, and results that are quoted are often sensitive to details of the problems studied and the computer implementations used.
- Page 349 · 2D cellular automata. The rule numbers are specified as on page 927.
- Page 349 · Circle packings. Hexagonal packing of equal circles has been known since early antiquity (e.g. the fourth picture on page 43). It fills a fraction  $\pi/\sqrt{12} \approx 0.91$  of area which was proved maximal for periodic packings by Carl Friedrich Gauss in 1831 and for any packing by Axel Thue in 1910 and László Fejes Tóth in 1940. Much has been done to study densest packings of limited numbers of circles into various shapes, as well as onto surfaces of spheres (as in golf balls, pollen grains or radiolarians). Typically it has been found that with enough circles, patches of hexagonal packing always tend to form. (See page 987.)

For circles of unequal sizes rather little has been done. A procedure analogous to the one on page 350 was introduced by Charles Bennett in 1971 for 3D spheres (relevant for binary alloys). The picture below shows the network of contacts between circles in the cases from page 350. Note that with the procedure used, each new circle added must immediately touch two existing ones, though subsequently it may get touched by varying numbers of other circles.

![](Images/_page_1001_Picture_2.jpeg)

The distribution of numbers of circles that touch a given circle changes with the ratio of circle sizes, as in the picture below. The total filling fraction seems to vary fairly smoothly with this ratio, though I would not be surprised if some small-scale jumps were present.

![](Images/_page_1001_Picture_4.jpeg)

Note that even a single circle of different size in the center can have a large-scale effect on the results of the procedure, as illustrated in the pictures below.

![](Images/_page_1001_Picture_6.jpeg)

Finding densest packings of n circles is in general like solving quadratic programming problems with about  $n^2$  constraints. But at least for many size ratios I suspect that the final result will simply involve each kind of circle forming a separated hexagonally-packed region. This will not happen, however, for size ratios  $\leq 2/\sqrt{3} - 1 \approx 0.15$ , since then the small circles can fit into the interstices of an ordinary hexagonal pattern, yielding a filling fraction  $1/18(17\sqrt{13}-24)\pi \simeq 0.95$ . The picture below shows what happens if one repeatedly inserts circles to form a so-called Apollonian packing derived from the problem studied by Apollonius of finding a circle that touches three others. At step t,  $3^{t-1}$  circles are added for each original circle, and the network of tangencies among circles is exactly example (a) from page 509. Most of the circles added at a given step are not the same size, however, making the overall geometry not straightforwardly nested. (The total numbers of different sizes of circles for the first few steps are {2, 3, 5, 10, 24, 63, 178, 521}. At step 3, for example, the new circles have radii  $(25-12\sqrt{3})/193$  and  $(19-6\sqrt{3})/253$ . In general, the radius of a circle inscribed between three other touching circles that have radii p, q, r is pqr/(pq+pr+qr+2Sqrt[pqr(p+q+r)]).) In the limit of an infinite number of steps the filling fraction tends to 1, while the region left unfilled has a fractal dimension of about 1.3057.

![](Images/_page_1001_Picture_9.jpeg)

To achieve filling fraction 1 requires arbitrarily small circles, but there are many different arrangements of circles that will work, some not even close to nested. When actual granular materials are formed by crushing, there is probably some tendency to generate smaller pieces by following essentially substitution system rules, and the result may be a nested distribution of sizes that allows an Apollonian-like packing.

Apollonian packings turn out to correspond to limit sets invariant under groups of rational transformations in the complex plane. Note that as on page 1007 packings can be constructed in which the sizes of circles vary smoothly with position according to a harmonic function.

■ Sphere packings. The 3D face-centered cubic (fcc) packing shown in the main text has presumably been known since antiquity, and has been used extensively for packing fruit, cannon balls, etc. It fills space with a density  $\pi/\sqrt{18} \approx 0.74$ , which Johannes Kepler suggested in 1609 might be the maximum possible. This was proved for periodic packings by Carl Friedrich Gauss in 1831, and for any packing by Thomas Hales in 1998. (By offsetting successive layers hexagonal close packing (hcp) can be obtained; this has the same density as fcc, but has a trapezoid-rhombic dodecahedron Voronoi diagram—see note below and page 929—rather than an ordinary rhombic dodecahedron.)

Random packings of spheres typically have densities around 0.64 (compared to 0.74 for fcc). Many of their large pores appear to be associated with poor packing of tetrahedral clusters of 4 spheres. (Note that individual such clusters—as well as for example 13-sphere approximate icosahedra—represent locally dense packings.)

It is common for shaking to cause granular materials (such as coffee or sand grains) to settle and pack at least a few percent better. Larger objects normally come to the top (as with mixed nuts, popcorn or pebbles and sand), essentially because the smaller ones more easily fall through interstices.

■ Higher dimensions. In no dimension above 3 is it known for certain what configuration of spheres yields the densest packing. Cases in which spheres are arranged on repetitive lattices are related to error-correcting codes and groups. Up to 8D, the densest packings of this type are known to be ones obtained by successively adding layers individually

optimized in each dimension. And in fact up to 26D (with the exception of 11 through 13) all the densest packings known so far are lattices that work like this. In 8D and 24D these lattices are known to be ones in which each sphere touches the maximal number of others (240 and 196560 respectively). (In 8D the lattice also corresponds to the root vectors of the Lie group E<sub>8</sub>; in 24D it is the Leech lattice derived from a Golay code, and related to the Monster Group). In various dimensions above 10 packings in which successive layers are shifted give slightly higher densities than known lattices. In all examples found so far the densest packings can always be repetitive; most can also be highly symmetrical-though in high dimensions random lattices often do not yield much worse results.

■ Discrete packings. The pictures below show a discrete analog of circle packing in which one arranges as many circles as possible with a given diameter on a grid. (The grid is assumed to wrap around.)

![](Images/_page_1002_Figure_4.jpeg)

The pictures show all the distinct maximal cases that exist for a 7×7 grid, corresponding to possible circles with diameters  $Sqrt[m^2 + n^2]$ . Already some of these are difficult to find. And in fact in general finding such packings is an NPcomplete problem: it is equivalent to the problem of finding the maximum clique (completely connected set) in the graph whose vertices are joined whenever they correspond to grid points on which non-overlapping circles could be centered.

On large grids, optimal packings seem to approach rational approximations to hexagonal packings. But what happens if one generalizes to allow circles of different sizes is not clear.

■ Voronoi diagrams. The Voronoi diagram for a set of points shows the region around each point in which one is closer to that point than to any other. (The edges of the regions are thus like watersheds.) The pictures below show a few examples. In 2D the regions in a Voronoi diagram are always polygons, and in 3D polyhedra. If all the points lie on a repetitive lattice each region will always be the same, and is often known as a Wigner-Seitz cell or a Dirichlet domain. For a simple cubic lattice the regions are cubes with 6 faces. For an fcc lattice they are rhombic dodecahedra with 12 faces and for a bcc lattice they are truncated octahedra (tetradecahedra) with 14 faces. (Compare page 929.)

![](Images/_page_1002_Picture_9.jpeg)

Voronoi diagrams for irregularly distributed points have found many applications. In 2D they are used in studies of animal territories, retail store utilization and municipal districting. In 3D they are used as simple models of foams, grains in solids, assemblies of biological cells and selfgravitating regions in primordial galaxy formation. Voronoi diagrams are relevant whenever there is growth in all directions at an identical speed from a collection of seed points. (In high dimensions they also appear immediately in studying error-correcting codes.)

Modern computational geometry has provided efficient algorithms for constructing Voronoi diagrams, and has allowed them to be used in mesh generation, point location, cluster analysis, machining plans and many other computational tasks.

■ **Discrete Voronoi diagrams.** The k = 3, r = 1 cellular automaton

 $\{\{0 \mid 1, n : (0 \mid 1), 0 \mid 1\} \rightarrow n, \{\_, 0, \_\} \rightarrow 2, \{\_, n\_, \_\} \rightarrow n-1\}$ is an example of a system that generates discrete 1D Voronoi diagrams by having regions that grow from every initial black cell, but stop whenever they meet, as shown below.

![](Images/_page_1002_Picture_14.jpeg)

Analogous behavior can also be obtained in 2D, as shown for a 2D cellular automaton in the pictures below.

![](Images/_page_1002_Picture_16.jpeg)

■ Brillouin zones. A region in an ordinary Voronoi diagram shows where a given point is closest. One can also consider higher-order Voronoi diagrams in which each region shows where a given point is the  $k^{th}$  closest. The total area of each region is the same for every k, but some complexity in shape is seen, though for large k they always in a sense

approximate circles. 3D versions of such regions have been encountered in studies of quantum mechanical properties of crystals since the 1930s.

- Packing deformable objects. If one pushes together identical deformable objects in 2D they tend to arrange themselves in a regular hexagonal array-and this configuration is known to minimize total boundary length. In 3D the arrangement one gets is typically not very regular-although as noted at various times since the 1600s individual objects often have pentagonal faces suggestive of dodecahedra. (The average number of faces for each object depends on the details of the random process used to pack them, but is typically around 14. Note that for a 3D Voronoi diagram with randomly placed points, the average number of faces for each region is  $2 + 48 \pi^2/35 \approx 15.5$ .) It was suggested by William Thomson (Kelvin) in 1887 that an array of 14-faced tetradecahedra on a bcc lattice might yield minimum total face area. But in 1993 Denis Weaire and Robert Phelan discovered a layered repetitive arrangement of 12- and 14-faced polyhedra (average 13.5) that yields 0.003 times less total area. It seems likely that there are polyhedra which fill space in a less regular way and yield still smaller total area. (Note that if the surfaces minimize area like soap films they are slightly curved in all these cases. See also pages 1007 and 1039.)
- Page 351 · Protein folding. When the molecular structure of proteins was first studied in the 1950s it was assumed that given their amino acid sequences pure minimization of energy would determine their often elaborate overall shapes. But by the 1990s it was fairly clear that in fact many details of the actual processes by which proteins are assembled can greatly affect their specific pattern of folding. (Examples include effects of chaperone molecules and prions.) (See pages 1003 and 1184.)

#### Origins of Simple Behavior

- Previous approaches. Before the discoveries in this book, nested and sometimes even repetitive behavior were quite often considered complex, and it was assumed that elaborate theories were necessary to explain them. Most of the theories that have been proposed are ultimately equivalent to what I discuss in this section, though they are usually presented in vastly more complicated ways.
- Uniformity in frequency. As shown on page 587, a completely random sequence of cells yields a spectrum that is essentially uniform in frequency. Such uniformity in frequency is implied by standard quantum theory to exist in

the idealized zero-point fluctuations of a free quantum field—with direct consequences for such semiclassical phenomena as the Casimir effect and Hawking radiation. (See page 1062.)

- **Repetition in numbers.** A common source of repetition in systems involving numbers is the almost trivial fact that in a sequence of successive integers there is a repetitive pattern of cases at which a particular divisor occurs. Other examples include the repetitive structure of digits in rational numbers (see page 138) and continued fraction terms in square roots (see page 144).
- Repetition in continuous systems. A standard approach to partial differential equations (PDEs) used for more than a century is so-called linear stability analysis, in which one assumes that small fluctuations around some kind of basic solution can be treated as a superposition of waves of the form  $Exp[ikx]Exp[i\omega t]$ . And at least in a linear approximation any given PDE then typically implies that  $\omega$ is connected to the wavenumber k by a so-called dispersion relation, which often has a simple algebraic form. For some kthis yields a value of  $\omega$  that is real—corresponding to an ordinary wave that maintains the same amplitude. But for some k one often finds that  $\omega$  has an imaginary part. The most common case  $Im[\omega] > 0$  yields exponential damping. But particularly when the original PDE is nonlinear one often finds that  $Im[\omega] < 0$  for some range of k—implying an instability which causes modes with certain spatial wavelengths to grow. The mode with the most negative  $Im[\omega]$  will grow fastest, potentially leading to repetitive behavior that shows a particular dominant spatial wavelength. Repetitive patterns with this type of origin are seen in a number of situations, especially in fluids (and notably in connection with Kelvin-Helmholtz, Rayleigh-Taylor and other well-studied instabilities). Examples are ripples and swell on an ocean (compare page 1001), Bénard convection cells, cloud streets and splash coronas. Note that modes that grow exponentially inevitably soon become too large for a linear approximation—and when this approximation breaks down more complicated behavior with no sign of simple repetitive patterns is often seen.
- **Examples of nesting.** Examples in which a single element splits into others include branching in plants, particle showers, genealogical trees, river deltas and crushing of rocks. Examples in which elements merge include river tributaries and some cracking phenomena.
- Page 358 · Nesting in numbers. Chapter 4 contains several examples of systems based on numbers that exhibit nested behavior. Ultimately these examples can usually be traced to

nesting in the pattern of digits of successive integers, but significant translation is often required.

■ Nested lists. One can think of structures that annihilate in pairs as being like parentheses or other delimiters that come in pairs, as in the picture below.

![](Images/_page_1004_Picture_4.jpeg)

A string of balanced parentheses is analogous to a nested Mathematica list such as {{{}}, {{}}}, {{}}}. The Mathematica expression tree for this list then has a structure analogous to the nested pattern in the picture.

The set of possible strings of balanced parentheses forms a context-free language, as discussed on page 939. The number of such strings containing 2n characters is the  $n^{th}$  Catalan number Binomial[2n, n]/(n+1) (as obtained from the generating function (1 - Sqrt[1 - 4x])/(2x)). The number of strings of depth d (and thus taking d steps to annihilate completely) is given by  $c[\{n, n\}, d] - c[\{n, n\}, d - 1]$  where

Several types of structures are equivalent to strings of balanced parentheses, as illustrated below.

![](Images/_page_1004_Picture_9.jpeg)

- Phase transitions. Nesting in systems like rule 184 (see page 273) is closely related to the phenomenon of scaling studied in phase transitions and critical phenomena since the 1960s. As discussed on page 983 ordinary equilibrium statistical mechanics effectively samples configurations of systems like rule 184 after large numbers of steps of evolution. But the point is that when the initial number of black and white cells is exactly equal—corresponding to a phase transition point a typical configuration of rule 184 will contain domains with a nested distribution of sizes. The properties of such configurations can be studied by considering invariance under rescalings of the kind discussed on page 955, in analogy to renormalization group methods. A typical result is that correlations between colors of different cells fall off like a power of distance—with the specific power depending only on general features of the nested patterns formed, and not on most details of the system.
- Self-organized criticality. The fact that in traditional statistical mechanics nesting had been encountered only at the precise locations of phase transitions led in the 1980s to

the notion that despite its ubiquity in nature nesting must somehow require fine tuning of parameters. Already in the early 1980s, however, my studies on simple additive and other cellular automata (see page 26) had for example made it rather clear that this is not the case. But in the late 1980s it became popular to think that in many systems nesting (as well as the largely unrelated phenomenon of 1/f noise) might be the result of fine tuning of parameters achieved through some automatic process of self-regulation. Computer experiments on various cellular automata and related systems were given as examples of how this might work. But in most of these experiments mistakes and misinterpretations were found, and in the end little of value was learned about the origins of nesting (or 1/f noise). Nevertheless, a number of interesting systems did emerge, the best known being the idealized sandpile model from the 1987 work of Per Bak, Chao Tang and Kurt Wiesenfeld. This is a k = 8 2D cellular automaton in which toppling of sand above a critical slope is captured by updating an array of relative sand heights s according to the rule

```
SandStep[s_{-}] := s + ListConvolve[
      {{0, 1, 0}, {1, -4, 1}, {0, 1, 0}}, UnitStep[s-4], 2, 0]
```

Starting from any initial condition, the rule eventually yields a fixed configuration with all values less than 4, as in the picture below. (With an  $n \times n$  initial block of 4's, stabilization typically takes about  $0.4 n^2$  steps.).

![](Images/_page_1004_Picture_15.jpeg)

To model the pouring of sand into a pile one can consider a series of cycles, in which at each cycle one first adds 4 to the value of the center cell, then repeatedly applies the rule until a new fixed configuration FixedPoint[SandStep, s] is obtained. (The more usual version of the model adds to a random cell.) The picture below shows slices through the evolution at several successive cycles. Avalanches of different sizes occur, yielding activity that lasts for varying numbers of steps.

![](Images/_page_1004_Picture_17.jpeg)

The pictures at the top of the next page show some of the final fixed configurations, together with the number of steps needed to reach them. (The total value of s at cycle t is 4t; the radius of the nonzero region is about  $0.74\sqrt{t}$ .) The behavior one sees is fairly complicated—a fact which in the past resulted in much confusion and some bizarre claims, but which in the light of the discoveries in this book no longer seems surprising.

![](Images/_page_1005_Picture_2.jpeg)

![](Images/_page_1005_Picture_3.jpeg)

![](Images/_page_1005_Picture_4.jpeg)

![](Images/_page_1005_Figure_5.jpeg)

The system can be generalized to d dimensions as a k = 4d cellular automaton with 2d final values. The total value of s is always conserved. In 1D, the update rule is simply

SandStep[s\_] :=

s + ListConvolve[{1, -2, 1}, UnitStep[s - 2], 2, 0]

In this case the evolution obtained if one repeatedly adds to the center cell (as in the first picture below) is always quite simple. But as the pictures below illustrate, evolution from typical initial conditions yields behavior that often looks a little like rule 184. With a total initial s value of m, the number of steps before a fixed point is reached seems to increase roughly like  $m^2$ .

![](Images/_page_1005_Picture_10.jpeg)

When d > 1, more complicated behavior is seen for evolution from at least some initial conditions, as indicated above.

■ Random walks. It is a consequence of the Central Limit Theorem that the pattern of any random walk with steps of bounded length (see page 977) must have a certain nested or

self-similar structure, in the sense that rescaled averages of different numbers of steps will always yield patterns that look qualitatively the same. As emphasized by Benoit Mandelbrot in connection with a variety of systems in nature, the same is also true for random walks whose step lengths follow a power-law distribution, but are unbounded. (Compare page 969.)

- Structure of algorithms. The two most common overall frameworks that have traditionally been used in algorithms in computer science are iteration and recursion—and these correspond quite directly to having operations performed respectively in repetitive and nested ways. But while iteration is generally viewed as being quite easy to understand, until recently even recursion was usually considered rather difficult. No doubt the methods of this book will in the future lead to all sorts of algorithms based on much more complex patterns of behavior. (See page 1142.)
- Origins of localized structures. Much as with other features of behavior, one can identify several mechanisms that can lead to localized structures. In 1D, localized structures sometimes arise as defects in largely repetitive behavior, or more generally as boundaries between states with different properties—such as the different phases of the repetitive background in rule 110. In higher dimensions a common source—especially in systems that show some level of continuity—are point, line or other topological defects (see page 1045), of which vortices are a typical example.

#### Implications for Everyday Systems

#### Issues of Modelling

- Page 363 · Uncertainties of this chapter. In earlier chapters of this book what I have said can mostly be said with absolute certainty, since it is based on observations about the behavior of purely abstract systems that I have explicitly constructed. But in this chapter, I study actual systems that exist in nature, and as a result, most of what I say cannot be said with any absolute certainty, but instead must involve a significant component of hypothesis. For I no longer control the basic rules of the systems I am studying, and instead I must just try to deduce these rules from observation—with the potential that despite my best efforts my deductions could simply be incorrect.
- Experiences of modelling. Over the course of the past 25 years I have constructed an immense number of models for a wide range of scientific, technical and business purposes. But while these models have often proved extremely useful in practice, I have usually considered them intellectually quite unsatisfactory. For being models, they are inevitably incomplete, and it is never in any definitive sense possible to establish their validity.
- Page 363 · Notes on this chapter. Much of this book is concerned with topics that have never been discussed in any concrete form before, so that between the main text and these notes I have been able to include a large fraction of everything that is known about them. But in this chapter (as well as some of the ones that follow) the systems I consider have often had huge amounts written about them before, making any kind of complete summary quite impossible.
- Material for this chapter. Like the rest of this book, this chapter is strongly based on my personal work and observations. For almost all of the systems discussed I have personally collected extensive data and samples, often over the course of many years, and sometimes in quite unlikely and amusing circumstances. I have also tried to study the

- existing scientific literature, and indeed in working on this chapter I have looked at many thousands of papers and books—even though the vast majority of them tend to ignore overall issues, and instead concentrate on details of often excruciating specificity.
- Page 365 · Models versus experiments. In modern science it is usually said that the ultimate test of any model is its agreement with experiment. But this is often interpreted to mean that if an experiment ever disagrees with a model, then the model must be wrong. Particularly when the model is simple and the experiment is complex, however, my personal experience has been that it is quite common for it to be the experiment, rather than the model, that is wrong. When I started doing particle physics in the mid-1970s I assumedlike most theoretical scientists-that the results of experiments could somehow always be treated as rigid constraints on models. But in 1977 I worked on constructing the first model based on QCD for heavy particle production in high-energy proton-proton collisions. The model predicted a certain rate for the production of such particles. But an experiment which failed to see any of these particles implied that the rate must be much lower. And on the basis of this I spent great effort trying to see what might be wrong with the model-only to discover some time later that in fact the methodology of the experiment was flawed and its results were wrong. At first I thought that perhaps this was an isolated incident. But soon I had seen many examples where the stated results of physics experiments were incorrect, either through straightforward mistakes or through subtly prejudiced analysis. And outside of physics, I have tended to find still less reliability in the results of complex experiments.
- Page 366 · Models versus reality. Questions about the correspondence between models and reality have been much debated in the philosophy of science for many centuries, and were, for example, central to the disagreement between Galileo and the church in the early 1600s. Many successful

models are in practice first introduced as convenient calculational devices, but later turn out to have a direct correspondence to reality. Two examples are planets orbiting the Sun, and quarks being constituents of particles. It remains to be seen whether such models as the imaginary time statistical mechanics formalism for quantum mechanics (see page 1061) turn out to have any direct correspondence to reality.

- History of modelling. Creation myths can in a sense be viewed as primitive models. Early examples of models with more extensive structure included epicycles. Traditional mathematical models of the modern type originated in the 1600s. The success of such models in physics led to attempts to imitate them in other fields, but for the most part these did not succeed. The idea of modelling intricate patterns using programs arose to some extent in the study of fractals in the late 1970s. And the notion of models based on simple programs such as cellular automata was central to my work in the early 1980s. But despite quite a number of fairly wellknown successes, there is even now surprisingly little understanding among most scientists of the idea of models based on simple programs. Work in computer graphicswith its emphasis on producing pictures that look right—has made some contributions. And it seems likely that the possibility of computerized and especially image-based data taking will contribute further. (See also page 860.)
- Page 367 · Finding models. Even though a model may have a simple form, it may not be at all easy to find. Indeed, many of the models in this chapter took me a very long time to find. By far my most common mistake was trying to build too much into the basic structure of the model. Often I was sure that some feature of the behavior of a system must be built into the underlying model-yet I could see no simple way to do it. But eventually what happened was that I tried a few other very simple models, and to my great surprise one of them ended up showing the behavior I wanted, even though I had in no way explicitly built it in.
- Page 369 · Consequences of models. Given a program it is always possible to run the program to find out what it will do. But as I discuss in Chapter 12, when the behavior is complex it may take an irreducible amount of computational work to answer any given question about it. However, this is not a sign of imperfection in the model; it is merely a fundamental feature of complex behavior.
- Universality in models. With traditional models based on equations, it is usually assumed that there is a unique correct version of any model. But in the previous chapter we saw that it is possible for quite different programs to yield

essentially the same large-scale behavior, implying that with programs there can be many models that have the same consequences but different detailed underlying structure.

#### The Growth of Crystals

- Page 369 · Nucleation. In the absence of container walls or of other objects that can act as seeds, liquids and gases can typically be supercooled quite far below their freezing points. It appears to be extremely unlikely for spontaneous microscopic fluctuations to initiate crystal growth, and natural snowflakes, for example, presumably nucleate around dust or other particles in the air. Snowflakes in manmade snow are typically nucleated by synthetic materials. In this case and in experiments on cloud seeding it has been observed that the details of seeds can affect the overall shapes of crystals that grow from them.
- Page 369 · Implementation. One can treat hexagonal lattices as distorted square lattices, updated according to

CAStep[rule\_List, a\_] := Map[rule[[14-#]] &,

a + 2 ListConvolve[{{1, 1, 0}, {1, 0, 1}, {0, 1, 1}}, a, 2], {2}] where rule = IntegerDigits[code, 2, 14]. On this page the rule used is code 16382; on page 371 it is code 10926. The centers of an array of regular hexagons are given by Table[ $\{i\sqrt{3}, j\}, \{i, 1, m\}, \{j, Mod[i, 2], n, 2\}$ ].

- Page 372 · Identical snowflakes. The widespread claim that no two snowflakes are alike is not in practice true. It is however the case that as a result of turbulent air currents a collection of snowflakes that fall to the ground in a particular region will often have come from very different regions of a cloud, and therefore will have grown in different environments. Note that the reason that the six arms of a single snowflake usually look the same is that all of them have grown in essentially the same environment. Deviations are usually the result of collisions between falling snowflakes.
- History of snowflake studies. Rough sketches of snowflakes were published by Olaus Magnus of Uppsala around 1550. Johannes Kepler made more detailed pictures and identified hexagonal symmetry around 1611. Over the course of the next few centuries, following work by René Descartes, Robert Hooke and others, progressively more accurate pictures were made and correlations between weather conditions and snowflake forms were found. Thousands of photographs of snowflakes were taken by Wilson Bentley over the period 1884-1931. Beginning in 1932 an extensive study of snowflakes was made by Ukichiro Nakaya, who in 1936 also produced the first artificial snowflakes. Most of the fairly

small amount of more recent work on snowflakes has been done as part of more general studies on dendritic crystal growth. Note that tree-like snowflakes are what make snow fluffy, while simple hexagons make it denser and more slippery. The proportion of different types of snowflakes is important in understanding phenomena such as avalanches.

- History of crystal growth. The vast majority of work done on crystal growth has been concerned with practical methods rather than with theoretical analyses. The first synthetic gemstones were made in the mid-1800s, and methods for making high-quality crystals of various materials have been developed over the course of the past century. Since the mid-1970s such crystals have been crucial to the semiconductor industry. Systematic studies of the symmetries of crystals with flat facets began in the 1700s, and the relationship to internal structure was confirmed by X-ray crystallography in the 1920s. The many different possible external forms of crystals have been noted in mineralogy since Greek times, but although classification schemes have been given, these forms have apparently still not been studied in a particularly systematic way.
- Models of crystal growth. There are two common types of models for crystal growth: ones based on the physics of individual atoms, and ones based on continuum descriptions of large collections of atoms. In the former category, it was recognized in the 1940s that a single atom is very unlikely to stick to a completely flat surface, so growth will always tend to occur at steps on a crystal surface, often associated with screw dislocations in the crystal structure. In practice, however, as scanning tunnelling microscopes have revealed, most crystal surfaces that are not grown at an extremely slow rate tend to be quite rough at an atomic scale-and so it seems that for example the aggregation model from page 331 may be more appropriate. In snowflakes and other crystals features such as the branches of tree-like structures are much larger than atomic dimensions, so a continuum description can potentially be used. It is possible to write down a nonlinear partial differential equation for the motion of the solidification front, taking into account basic thermodynamic effects. The first result (discovered by William Mullins and Robert Sekerka in 1963) is that if every part of the front is at the same temperature, then any deviations from planarity in the front will tend to grow. The shape of the front is presumably stabilized by the Gibbs-Thomson effect, which implies that the freezing temperature is lower when the front is more curved. The characteristic length for deformations of the front turns out to be the geometric mean of a microscopic length associated with surface energy and a macroscopic length associated with diffusion. It is this characteristic

length that presumably determines the size of an individual cell in the cellular automaton model.

Dendritic crystals are commonly seen in ice formations on windows, and in pieces of aluminum of the kind found at typical hardware stores.

■ **Hopper crystals.** When a pool of molten bismuth solidifies it tends to form crystals like those in the first two pictures below. What seems to give these crystals their characteristic "hoppered" shapes is that there is more rapid growth at the edges of each face than at the center. (Spirals are probably associated with underlying screw dislocations.) Hoppering has not been much studied for scientific purposes, but has been noticed in many substances, including galena, rose quartz, gold, calcite, salt and ice.

![](Images/_page_1008_Picture_8.jpeg)

![](Images/_page_1008_Picture_9.jpeg)

![](Images/_page_1008_Picture_10.jpeg)

![](Images/_page_1008_Picture_11.jpeg)

- Page 373 · Other models. There are many ways to extend the simple cellular automata shown here. One possibility is to allow dependence on next-nearest as well as nearest neighbors. In this case it turns out that non-convex as well as convex faceted shapes can be obtained. Another possibility is to allow cells that have become black to turn white again. In this case all the various kinds of patterns that we saw in Chapter 5 can occur. A general feature of cellular automaton rules is that they are fundamentally local. Some models of crystal growth, however, call for longrange effects such as a temperature field which changes throughout the crystal in an effectively instantaneous way. It turns out, however, that many seemingly long-range effects can actually be captured quite easily in cellular automata. In a typical case, this can be done by introducing a third possible color for each cell, and then having rapidly changing arrangements of this color.
- Polycrystalline materials. When solids with complicated forms are seen, it has usually been assumed that they must be aggregates of many separate crystals, with each crystal having a simple faceted shape. But the results given here indicate that in fact individual crystals can yield highly complex shapes. There will nevertheless be cases however where multiple crystals are involved. These can be modelled by having a cellular automaton in which one starts from several separated seeds. Sometimes the regions associated with different seeds may have different characteristics; the boundaries between these regions then form a Voronoi diagram (see page 1038).

- Quasicrystals. In some special materials it was discovered in 1984 that atoms are arranged not on a purely repetitive grid, but instead in a pattern with the nested type of structure discussed on page 932. A characteristic feature of such patterns is that they can have approximate pentagonal or icosahedral symmetry, which is impossible for purely repetitive patterns. It has usually been assumed that the arrangement of atoms in a quasicrystal is determined by satisfying a constraint analogous to minimization of energy. And as we saw on page 932 it is indeed possible to get nested patterns by requiring that certain constraints be satisfied. But another explanation for such patterns is that they are the result of growth processes that are some kind of cross between those on pages 373 and 659.
- Amorphous materials. When solidification occurs fairly slowly, atoms have time to arrange themselves in a regular crystalline way. But if the cooling is sufficiently rapid, amorphous solids such as glasses are often formed. And in such cases, the packing of atoms is quite random—except that locally there is often approximate icosahedral structure, analogous to that discussed on page 943. (See also page 986.)
- Diffusion-limited aggregation (DLA). DLA is a model for a variety of natural growth processes that was invented by Thomas Witten and Leonard Sander in 1981, and which at first seems quite different from a cellular automaton. The basic idea of DLA is to build up a cluster of black cells by starting with a single black cell and then successively introducing new black cells far away that undergo random walks and stick to the cluster as soon as they come into contact with it. The patterns that are obtained by this procedure turn out for reasons that are still not particularly clear to have a random but on average nested form. (Depending on precise details of the underlying model, very large clusters may sometimes not have nested forms, at least in 2D.) The basic reason that DLA patterns are not very dense is that once arms have formed on the outside of the cluster. they tend to catch new cells before these cells have had a chance to go inside. It turns out that at a mathematical level DLA can be reproduced by solving the Laplace equation at each step with a constant boundary condition on the cluster, and then using the result to give the probability for adding a new cell at each point on the cluster. To construct a cellular automaton analog of DLA one can introduce gray as well as black and white cells, and then have the gray cells represent pieces of solid that have not yet become permanently attached to the main cluster. Rapid rearrangement of gray cells on successive steps can then have a similar effect to the random walks that occur in the usual DLA model. Whether a pattern with all the properties expected in DLA is produced

- seems to depend in some detail on the rules for the gray cells. But so long as there is effective randomness in the successive positions of these cells, and so long as the total number of them is conserved, then it appears that DLA-like results are usually obtained. No doubt there are also simpler cellular automaton rules that yield similar results. (See also page 979.)
- Boiling. The boiling of a liquid such as water involves a kind of growth inhibition that is in some ways analogous to that seen in dendritic crystal growth. When a particular piece of liquid boils-forming a bubble of gas-a certain latent heat is consumed, reducing the local temperature, and inhibiting further boiling. In the pictures below the liquid is divided into cells, with each cell having a temperature from 0 to 1, corresponding exactly to a continuous cellular automaton of the kind discussed on page 155. At each step, the temperature of every cell is given by the average of its temperature and the temperatures of its neighbors, representing the process of heat diffusion, with a constant amount added to represent external heating. If the temperature of any cell exceeds 1, then only the fractional part is kept, as in the systems on page 158, representing the consumption of latent heat in the boiling process. The pictures below illustrate the kind of seemingly random pattern of bubble formation that can be heard in the noise produced by boiling water.

![](Images/_page_1009_Picture_6.jpeg)

![](Images/_page_1009_Picture_7.jpeg)

#### The Breaking of Materials

■ Phenomenology of microscopic fracture. Different materials show rather different characteristics depending on how ductile or brittle they are. Ductile materials—such as taffy or mild steel-bend and smoothly neck before breaking. Brittle materials-such as chalk or glass-do not deform significantly before catastrophic failure. Ductile materials in effect flow slightly before breaking, and as a result their fracture surfaces tend to be less jagged. In addition, in response to stresses in the material, small voids often formperhaps nucleating around imperfections—yielding a pockmarked surface. In brittle materials, the beginning of the fracture surface typically looks quite mirror-like, then it starts to look misty, and finally, often at a sharply defined point, it begins to look complex and hackled. (This sequence is qualitatively not unlike the initiation of randomness in turbulent fluid flow and many other systems.) Cracks in brittle materials typically seem to start slowly, then accelerate to about half the Rayleigh speed at which small deformation waves on the surface would propagate. Brittle fracture involves violent breaking of atomic bonds; it usually leaves a jagged surface, and can lead to emission of both highfrequency sound as well as light. Directly around a crack complex patterns of stress are typically produced, though away from the crack they resolve quickly to a fairly smooth and simple form. It is known that ultrasound can affect the course of cracks, suggesting that crack propagation is affected by local stresses. There are many different detailed geometries for fracture, associated with snapping, tearing, shattering, pulling apart, and so on. In many situations, individual cracks will split into multiple cracks as they propagate, sometimes producing elaborate tree-like structures. The statistical properties of fracture surfaces have been studied fairly extensively. There is reasonable evidence of self-similarity, typically associated with a fractal dimension around 0.8 or slightly smaller.

- Models of microscopic fracture. Two kinds of models have traditionally been studied: ones based on looking at arrays of atoms, and ones based on continuum descriptions of materials. At the atomic level, a simple model suggested fairly recently is that atoms are connected by bonds with a random distribution of strengths, and that cracks follow paths that minimize the total strength of bonds to be broken. It is not clear why in a crystal bonds should be of different strengths, and there is some evidence that this model yields incorrect predictions for the statistical properties of actual cracks. A slightly better model, related to the one in the main text, is that the bonds between atoms are identical, and act like springs which break when they are stretched too far. In recent years, computer simulations with millions of atoms have been carried out—usually with realistic but complicated interatomic force laws-and some randomness has been observed, but its origins have not been isolated. A set of nonlinear partial differential equations known as the Lamé equations are commonly used as a continuum description of elastic materials. Various instabilities have been found in these equations, but the equations are based on small deformations, and presumably cannot be relied upon to provide information about fracture.
- **History.** Fracture has been a critical issue throughout the history of engineering. Its scientific study was particularly stimulated by failures of various types of ships and aircraft in the 1940s and 1950s, and many quantitative empirical results were obtained, so that by the 1960s ductile fracture as an engineering issue became fairly well understood. In the 1980s, ideas about fractals suggested new interpretations of

fracture surfaces, and in the past few years, various models of fracture based on ideas from statistical physics have been tried. Atomic-level computer experiments on fracture began in earnest in the late 1980s, but only very recently has it been possible to include enough atoms to even begin addressing questions about the structure of cracks.

- Page 375 · Experimental data. To investigate the model in the main text requires looking not only at the path of a crack, but also at dislocations of atoms near it. To do this dynamically is difficult, but in a perfect crystal final patterns of dislocations that remain at the edge of a region affected by fracture can be seen for example by electron diffraction. And it turns out that these often look remarkably like patterns made by 1D class 3 cellular automata. (Similar patterns may perhaps also be seen in recent detailed simulations of fracture processes in arrays of idealized atoms.)
- Large-scale fractures. It is remarkable to what extent very large-scale fractures can look like small-scale ones. If the path of a crack were, say, a perfect random walk, then one might imagine that large-scale cracks could simply be combinations of many small-scale segments. But when one looks at geological systems, for example, the smallest relevant scales for the cracks one sees are certainly no smaller than particles of soil. And as a result, one needs a more general mechanism, not just one that just relates to atoms and molecules.
- Alternate models. It is straightforward to set up 3-color cellular automata with the same basic idea as in the main text, but in which there is no need for a special cell to represent the crack. In addition, instead of modelling the displacement of atoms, one can try to model directly the presence or absence of atoms at particular positions. And then one can start from a repetitive array of cells, with a perturbation to represent the beginning of the crack.
- Electric breakdown. Somewhat related to fracture is the process of electric breakdown, visible for example in lightning, Lichtenberg figures or plasma-filled glass globes used as executive toys. At least in the case of lightning, there is some evidence that small inhomogeneities in the atmosphere can be important in producing at least some aspects of the apparent randomness that is seen. (With electric potential thought of like a diffusion field, models based on diffusion-limited aggregation are sometimes
- **Crushing.** For a rather wide range of cases it appears that in crushed solids such as rocks the probability of a particular fragment having a diameter larger than r is given approximately by  $r^{-2.5}$ . It seems likely that the origin of this is

that each rock has a certain probability to break into, say, two smaller rocks at each stage in the crushing process, much as in a substitution system.

■ Effects of microscopic roughness. The two most obvious features that are affected by the microscopic roughness of materials are visual appearance and sliding friction. A perfectly flat surface will reflect light like a mirror. Roughness will lead to more diffuse reflection, although the connection between observed properties of rough surfaces and typical parametrizations used in computer graphics is

The friction force that opposes sliding is usually assumed to be proportional purely to the force with which surfaces are pressed together. Presumably at least the beginning of the explanation for this slightly bizarre fact is that most of the friction force is associated with microscopic peaks in rough surfaces, and that the number of these peaks that come into close contact increases as surfaces are pushed together.

■ Crinkling. A question somewhat related to fracture concerns the generation of definite creases in crumpled or wrinkled objects such as pieces of paper or fabric. It is not too difficult to make various statements about details of the particular arrangements of creases that can occur, but nothing seems to be known about the origin of the overall randomness that is almost universally seen.

#### Fluid Flow

■ Page 376 · Reynolds numbers. If a system is to act like a continuum fluid, then almost by definition its behavior can involve only a limited number of macroscopic quantities, such as density and velocity. And from this it follows that patterns of flow should not depend separately on absolute speeds and sizes. Instead, the character of a flow should typically be determined by a single Reynolds number, Re = U L/v, where U is the characteristic speed of the flow (measured say in cm/sec), L is a characteristic size (measured say in cm), and v is the kinematic viscosity of the fluid. For water, v = 0.01, for air v = 0.15, and for glycerine v = 10000, all in units of  $cm^2/sec$ . In flow past a cylinder it is conventional to take L to be the diameter of the cylinder. But the fact that the form of flow should depend only on Reynolds number means that in the pictures in the main text for example it is not necessary to specify absolute sizes or speeds: one need only know the product UL that appears in the Reynolds number. In practice, moving one's finger slowly through water gives a Reynolds number of about 100 (so that a regular array of dimples corresponding to eddies are visible behind one's finger), walking in air about 10,000, a boat in the millions, and a large airplane in the billions.

The Reynolds number roughly measures the ratio of inertial to viscous effects. When the Reynolds number is small the viscous damping dominates, and the flow is laminar and smooth. When the Reynolds number is large, inertia associated with fluid motions dominates, and the flow is turbulent and complicated.

In different systems, the characteristic length used typically in the definition of Reynolds number is different. In most cases, however, the transition from laminar to turbulent flow occurs at Reynolds numbers around a hundred.

In some situations, however, Reynolds number alone does not appear to be sufficient to determine when a flow will become turbulent. Indeed, modern experiments on streams of dye in water (or rising columns of smoke) typically show a transition to turbulence at a significantly lower Reynolds number than the original experiments on these systems done by Osborne Reynolds in the 1880s. Presumably the reason for this is that the transition point can be lowered by perturbations from the environment, and such perturbations are more common in the modern mechanized world. If perturbations are indeed important, it implies that a traditional fluid description is not adequate. I suspect, however, that even though perturbations may determine the precise point at which turbulence begins, intrinsic randomness generation will dominate once turbulence has been initiated.

■ Navier-Stokes equations. The traditional model of fluids used in physics is based on a set of partial differential equations known as the Navier-Stokes equations. These equations were originally derived in the 1840s on the basis of conservation laws and first-order approximations. But if one assumes sufficient randomness in microscopic molecular processes they can also be derived from molecular dynamics, as done in the early 1900s, as well as from cellular automata of the kind shown on page 378, as I did in 1985 (see below). For very low Reynolds numbers and simple geometries, it is often possible to find explicit formulas for solutions to the Navier-Stokes equations. But even in the regime of flow where regular arrays of eddies are produced, analytical methods have never yielded complete explicit solutions. In this regime, however, numerical approximations are fairly easy to find. Since about the 1960s computers have been powerful enough to allow computations at least nominally to be extended to considerably higher Reynolds numbers. And indeed it has become increasingly common to see numerical results given far into the turbulent regime-leading sometimes to the assumption that turbulence has somehow been derived from the Navier-Stokes equations. But just what such numerical results actually have to do with detailed solutions to the Navier-Stokes equations is not clear. For in particular it ends up being almost impossible to distinguish whatever genuine instability and apparent randomness may be implied by the Navier-Stokes equations from artifacts that get introduced through the discretization procedure used in solving the equations on a computer. One of the key advantages of my cellular automaton approach to fluids is precisely that it does not require any such approximations.

At a mathematical level analysis of the Navier-Stokes has never established the formal uniqueness and existence of solutions. Indeed, there is even some evidence that singularities might almost inevitably form, which would imply a breakdown of the equations, and perhaps a need to account for underlying molecular processes.

In turbulent flow at higher Reynolds numbers there begin to be eddies with a wide range of sizes. And to capture all these eddies in a computation eventually involves prohibitively large amounts of information. In practice, therefore, semiempirical models of turbulence tend to be used-often "eddy viscosities"-with no direct relation to the Navier-Stokes equations. In airflow past an airplane there is however typically only a one-inch layer on each surface where such issues are important; the large-scale features of the remainder of the flow, which nevertheless accounts for only about half the drag on the airplane, can usually be studied without reference to turbulence.

The Navier-Stokes equations assume that all speeds are small compared to the speed of sound-and thus that the Mach number giving the ratio of these speeds is much less than one. In essentially all practical situations, Mach numbers close to one occur only at extremely high Reynolds numbers-where turbulence in any case would make it impossible to work out the detailed consequences of the Navier-Stokes equations. Nevertheless, in the case of cellular automaton fluids, I was able in 1985 to work out the rather complicated next order corrections to the Navier-Stokes

Above the speed of sound, fluids form shocks where density or velocity change over very small distances (see below). And by Mach 4 or so, shocks are typically so sharp that changes occur in less than the distance between molecular collisions-making it essential to go beyond the continuum fluid approximation, and account for molecular effects.

■ Models of turbulence. Traditional models typically view turbulence as consisting of some form of cascade of eddies.

This notion was already suggested in pictures by Leonardo da Vinci from around 1510, and in Japanese pictures (notably by Katsushika Hokusai) from around 1800 showing ocean waves breaking into precisely nested tongues of water. The theoretical study of turbulence began in earnest in the early 1900s, with emphasis on issues such as energy transfer among eddies and statistical correlations between velocities. Most published work became increasingly mathematical, but particularly following the ideas of Lewis Richardson in the 1920s, the underlying physical notion was that a large eddy, formed say by fluid flowing around an object, would be unstable, and would break up into smaller eddies, which in turn would break up into still smaller eddies, until eventually the eddies would be of such a size as to be readily damped by viscosity. An important step was taken in 1941 by Andrei Kolmogorov who argued that if the eddies in such a cascade were in a statistical equilibrium, then dimensional analysis would effectively imply that the spectrum of velocity fluctuations associated with the eddies must have a  $k^{-5/3}$ distribution, with k being wavenumber. This result has turned out to be in respectable agreement with a range of experimental data, but its physical significance has remained somewhat unclear. For there appear to be no explicit entities in fluids that can be directly identified as cascades of eddies. One possibility might be that an eddy could correspond to a local patch of vorticity or rotation in the fluid. And it is a general feature of fluids that interfaces between regions of different velocity are unstable, typically first becoming wavy and then breaking into separate pieces. But physical experiments and simulations in the past few years have suggested that vorticity in turbulent fluids in practice tends to become concentrated on a complicated network of lines that stretch and twist. Perhaps some interpretation can be made involving eddies existing only in a fractal region, or interacting with each other as well as branching. And perhaps new forms of definite localized structures can be identified. But no clear understanding has yet emerged, and indeed most of the analysis that is done-which tends to be largely statistical in nature—is not likely to shed much light on the general question of why there is so much apparent randomness in turbulence.

■ Chaos theory and turbulence. The full Navier-Stokes equations for fluid flow are far from being amenable to traditional mathematical analysis. But some simplified differential equations which potentially approximate various situations in fluid flow can be more amenable to analysis-and can exhibit the chaos phenomenon. Work in the 1950s by Lev Landau, Andrei Kolmogorov and others focused on equations with periodic and quasiperiodic behavior. But in 1962 Edward Lorenz discovered more complicated behavior in computer experiments on equations related to fluid flow (see page 971). Analysis of this behavior was closely linked to the chaos phenomenon of sensitive dependence on initial conditions. And by the late 1970s it had become popular to believe that the randomness in fluid turbulence was somehow associated with this phenomenon.

Experiments in very restricted situations showed correspondence with iterated maps in which the chaos phenomenon is seen. But the details of the connection with true turbulence remained unclear. And as I argue in the main text, the chaos phenomenon in the end seems quite unlikely to explain most of the randomness we see in turbulence. The basic problem is that a complex pattern of flow in effect involves a huge amount of information—and to extract this information purely from initial conditions would require for example going to a submolecular level, far below where traditional models of fluids could possibly apply.

Even within the context of the Lorenz equations there are already indications of difficulties with the chaos explanation. The Lorenz equations represent a first-order approximation to certain Navier-Stokes-like equations, in which viscosity is ignored. And when one goes to higher orders progressively more account is taken of viscosity, but the chaos phenomenon becomes progressively weaker. I suspect that in the limit where viscosity is fully included most details of initial conditions will simply be damped out, as physical intuition suggests. Even within the Lorenz equations, however, one can see evidence of intrinsic randomness generation, in which randomness is produced without any need for randomness in initial conditions. And as it turns out I suspect that despite subsequent developments the original ideas of Andrei Kolmogorov about complicated behavior in ordinary differential equations were probably more in line with my notion of intrinsic randomness generation than with the chaos phenomenon.

■ Flows past objects. By far the most experimental data has been collected for flows past cylinders. The few comparisons that have been done indicate that most results are extremely similar for plates and other non-streamlined or "bluff" objects. For spheres at infinitesimal Reynolds numbers a fairly simple exact analytical solution to the Navier-Stokes equations was found by George Stokes in 1851, giving a drag coefficient of  $6\pi/R$ . For a cylinder, there are difficulties with boundary conditions at infinity, but the drag coefficient was nevertheless calculated by William Oseen in 1915 to be  $8\pi/(R(1/2 + Log[8/R] - EulerGamma))$ . At infinitesimal Reynolds number the flow around a

symmetrical object is always symmetrical. As the Reynolds number increases, it becomes progressively more asymmetrical, and at  $R \simeq 6$  for a cylinder, closed eddies begin to appear behind the object. The length of the region associated with these eddies is found to grow almost perfectly linearly with Reynolds number. At  $R \simeq 30-40$  for a cylinder, oscillations are often seen in the eddies, and at  $R \simeq 46-49$ , a vortex street forms. Increasingly accurate numerical calculations based on direct approximations to the Navier-Stokes equations have been done in the regime of attached eddies since the 1930s. For a vortex street no analytical solution has ever been found, and indeed it is only recently that the general paths of fluid elements have even been accurately deduced. A simple model due to Theodore von Kármán from 1911 predicts a relative spacing of  $\pi/Log[1+\sqrt{2}]$  between vortices, and bifurcation theory analyses have provided some justification for some such result. Over the range  $50 \le R \le 150$  vortices are found to be generated at a cylinder with almost perfect periodicity at a dimensionless frequency (Strouhal number) that increases smoothly from about 0.12 to 0.19. But even though successive vortices are formed at fixed intervals, irregularities can develop as the array of vortices goes downstream, and such irregularities seem to occur at lower Reynolds numbers for flows past plates than cylinders. Some direct calculations of interactions between vortices have been done in the context of the Navier-Stokes equations, but the cellular automaton approach of page 378 seems to provide essentially the first reliable global results. In both calculations and experiments, there is often sensitivity to details of whatever boundary conditions are imposed on the fluid, even if they are far from the object. Results can also be affected by the history of the flow. In general, the early way the flow develops over time typically mirrors quite precisely the long-time behavior seen at successively greater Reynolds numbers. In experiments, the process of vortex generation at a cylinder first becomes irregular somewhere between R = 140 and R = 194. After this surprisingly few qualitative changes are seen even up to Reynolds numbers as high as 100,000. There is overall periodicity much like in a vortex street, but the detailed motion of the fluid is increasingly random. Typically the scale of the smallest eddies gets smaller in rough correspondence with the  $R^{-3/4}$  prediction of Kolmogorov's general arguments about turbulence. In flow past a cylinder, there are various quite sudden changes in the periodicity, apparently associated with 3D phenomena in which the flow is not uniform along the axis of the cylinder. The drag coefficient remains almost constant at a value around 1 until  $R \simeq 3 \times 10^5$ , at which point it drops precipitously for a while. This phenomenon is associated with details of flow close to the cylinder. At lower Reynolds numbers, the flow is still laminar when it first comes around the cylinder; but there is a transition to turbulence in this boundary layer after which the fluid can in effect slide more easily around the cylinder. When the speed of the flow passes the speed of sound in the fluid, shocks appear. Usually they form simple geometrical patterns (see below), and have the effect of forcing the turbulent wake behind the cylinder to become narrower.

- 2D fluids. The cellular automaton shown in the main text is purely two-dimensional. Experiments done on soap films since the 1980s indicate, however, that at least up to Reynolds numbers of several hundred, the patterns of flow around objects such as cylinders are almost identical to those seen in ordinary 3D fluids. The basic argument for Kolmogorov's  $k^{-5/3}$  result for the spectrum of turbulence is independent of dimension, but there are reasons to believe that in 2D eddies will tend to combine, so that after sufficiently long times only a small number of large eddies will be left. There is some evidence for this kind of process in the Earth's atmosphere, as well as in such phenomena as the Red Spot on Jupiter. At a microscopic level, there are some not completely unrelated issues in 2D about whether perturbations in a fluid made up of discrete molecules damp quickly enough to lead to ordinary viscosity. Formally, there is evidence that the Navier-Stokes equations in 2D might have a  $\nabla^2 \text{Log}[\nabla^2]$  viscosity term, rather than a  $\nabla^2$  one. But this effect, even if it is in fact present in principle, is almost certainly irrelevant on the scales of practical experiments.
- Cellular automaton fluids. A large number of technical issues can be studied in connection with cellular automaton fluids. Many were already discussed in my original 1985 paper. Others have been covered in some of the many papers that have appeared since then. Of particular concern are issues about how rotation and translation invariance emerge at the level of fluid processes even though they are absent in the underlying cellular automaton structure. The very simplest rules turn out to have difficulties in these regards (see page 1024), which is why the model shown in the main text, for example, is on a hexagonal rather than a square grid (compare page 980). The model can be viewed as a block cellular automaton of the type discussed on page 460, but on a 2D hexagonal grid. In general a block cellular automaton works by making replacements for overlapping blocks of cells on alternating steps. In the 1D case of page 460, the blocks that are replaced consist of pairs of adjacent cells with two different alignments. On a 2D square grid, one can use overlapping 2×2 square blocks. But on a 2D hexagonal grid,

one must instead alternate on successive steps between hexagons and their dual triangles.

- Vorticity-based models. As an alternative to models of fluids based on elements with discrete velocities, one can consider using elements with discrete vorticities.
- History of cellular automaton fluids. Following development of the molecular model for gases in the late 1800s (see page 1019), early mathematical derivations of continuum fluid behavior from underlying molecular dynamics were already complete by the 1920s. More streamlined approaches with the same basic assumptions continued to be developed over the next several decades. In the late 1950s Berni Alder and Thomas Wainwright began to do computer simulations of idealized molecular dynamics of 2D hard spheres-mainly to investigate transitions between solids, liquids and gases. In 1967 they observed so-called long-time tails not expected from existing calculations, and although it was realized that these were a consequence of fluid-like behavior not readily accounted for in purely microscopic approximations, it did not seem plausible that large-scale fluid phenomena could be investigated with molecular dynamics. The idea of setting up models with discrete approximations to the velocities of molecules appears to have arisen first in the work of James Broadwell in 1964 on the dynamics of rarefied gases. In the 1960s there was also interest in socalled lattice gases in which—by analogy with spin systems like the Ising model-discrete particles were placed in all possible configurations on a lattice subject to certain local constraints, and average equilibrium properties were computed. By the early 1970s more dynamic models were sometimes being considered, and for example Yves Pomeau and collaborators constructed idealized models of gases in which both positions and velocities of molecules were discrete. As it happens, in 1973, as one of my earliest computer programs, I created a simulation of essentially the same kind of system (see page 17). But it turned out that this particular kind of system, set up as it was on a square grid, was almost uniquely unable to generate the kind of randomness that we have seen so often in this book, and that is needed to obtain standard large-scale fluid behavior. And as a result, essentially no further development on discrete models of fluids was then done until after my work on cellular automata in the early 1980s. I had always viewed turbulent fluids as an important potential application for cellular automata. And in 1984, as part of work I was doing on massively parallel computing, I resolved to develop a practical approach to fluid mechanics based on cellular automata. I initiated discussions with

various members of the fluid dynamics community, who strongly discouraged me from pursuing my ideas. But I persisted, and by the summer of 1985 I had managed to produce pictures like those on page 378. Meanwhile, however, some of the very same individuals who had discouraged me had in fact themselves pursued exactly the line of research I had discussed. And by late 1985, cellular automaton fluids were generating considerable interest throughout the fluid mechanics community. Many claims were made that existing computational methods were necessarily far superior. But in practice over the years since 1985, cellular automaton methods have grown steadily in popularity, and are now widely used in physics and engineering. Yet despite all the work that has been done, the fundamental issues about the origins of turbulence that I had originally planned to investigate in cellular automaton fluids have remained largely untouched.

- Computational fluid dynamics. From its inception in the mid-1940s until the invention of cellular automaton fluids in the 1980s, essentially all computational fluid dynamics involved taking the continuum Navier-Stokes equations and then approximating these equations using some form of discrete mesh in space and time, and arguing that when the mesh becomes small enough, correct results would be obtained. Cellular automaton fluids start from a fundamentally discrete system which can be simulated precisely, and thus avoid the need for any such arguments. One issue however is that in the simplest cellular automaton fluids molecules are in effect counted in unary: each molecule is traced separately, rather than just being included as part of a total number that can be manipulated using standard arithmetic operations. A variety of tricks, however, maintain precision while in effect allowing a large number of molecules to be handled at the same time.
- Sound waves and shocks. Sound waves in a fluid correspond to periodic variations in density. The pictures below show how a density perturbation leads to a sound wave in a cellular automaton fluid. The sound wave turns out to travel at a fraction  $1/\sqrt{2}$  of the microscopic particle speed.

![](Images/_page_1015_Picture_5.jpeg)

![](Images/_page_1015_Picture_6.jpeg)

![](Images/_page_1015_Picture_7.jpeg)

![](Images/_page_1015_Picture_8.jpeg)

When the speed of a fluid relative to an object becomes comparable to the speed of sound, the fluid will inevitably

show variations in density. Typically shocks develop at the front and back of an object, as illustrated below.

![](Images/_page_1015_Picture_11.jpeg)

![](Images/_page_1015_Picture_12.jpeg)

![](Images/_page_1015_Picture_13.jpeg)

It turns out that when two shocks meet, they usually have little effect on each other, and when there are boundaries, shocks are usually reflected in simple ways. The result of this is that in most situations patterns of shocks generated have a fairly simple geometrical structure, with none of the randomness of turbulence.

- Splashes. Particularly familiar everyday examples of complex fluid behavior are splashes made by objects falling into water. When a water drop hits a water surface, at first a symmetrical crater forms. But soon its rim becomes unstable, and several peaks (often with small drops at the top) appear in a characteristic coronet pattern. If the original drop was moving quickly, a whole hemisphere of water then closes in above. But in any case a peak appears at the center, sometimes with a spherical drop at the top. If a solid object is dropped into water, the overall structure of the splash made can depend in great detail on its shape and surface roughness. Splashes were studied using flash photography by Arthur Worthington around 1900 (as well as Harold Edgerton in the 1950s), but remarkably little theoretical investigation of them has ever been made.
- Generalizations of fluid flow. In the simplest case the local state of a fluid is characterized by its velocity and perhaps density. But there are many situations where there are also other quantities relevant, notably temperature and chemical composition. And it turns out to be rather straightforward to generalize cellular automaton fluids to handle these.
- **Convection.** When there is a temperature difference between the top and bottom of a fluid, hot fluid tends to rise, and cold fluid then comes down again. At low temperature differences (characterized by a low dimensionless Rayleigh number) a regular pattern of hexagonal Bénard convection cells is formed (see page 377). But as the temperature difference increases, a transition to turbulence is seen, with most of the same characteristics as in flow past an object. A cellular automaton model can be made by allowing particles with more than one possible energy: the average particle energy in a region corresponds to fluid temperature.

- Atmospheric turbulence. Convection occurs because air near the ground is warmer than air at higher altitudes. On a clear night over flat terrain, air flow can be laminar near the ground. Usually, however, it is turbulent near the groundproducing, for example, random gusting in wind-but becomes laminar at higher altitudes. Turbulent convection nevertheless occurs in most clouds, leading to random billowing shapes. The "turbulence" that causes bumps in airplanes is often associated with clouds, though sometimes with larger-scale wave-like fluid motions such as the jet
- Ocean surfaces. At low wind speeds, regular ripples are seen; at higher wind speeds, a random pattern of creases occurs. It seems likely that randomness in the wind has little to do with the behavior of the ocean surface; instead it is the intrinsic dynamics of the water that is most important.
- Granular materials. Sand and other granular materials show many phenomena seen in fluids. (Sand dunes are the rough analog of ocean waves.) Vortices have recently been seen, and presumably under appropriate conditions turbulence will eventually also be seen.
- Geological structures. Typical landscapes on Earth are to a first approximation formed by regions of crust being uplifted through tectonic activity, then being sculpted by progressive erosion (and redeposition of sediment) associated with the flow of water. (Visually very different special cases include volcanos, impact craters and wind-sculpted deserts.) Eventually erosion and deposition will in effect completely smooth out a landscape. But at intermediate times one will see all sorts of potentially dramatic gullies that reflect the pattern of drainage, and the formation of a whole tree of streams and rivers. (Such trees have been studied since at least the early 1900s, with typical examples of concepts being Horton stream order, equal to Depth for trees given as Mathematica expressions.) If one imagines a uniform slope with discrete streams of water going randomly in each direction at the top, and then merging whenever they meet, one immediately gets a simple tree structure a little like in the pictures at the top of page 359. (More complicated models based for example on aggregation, percolation and energy minimization have been proposed in recent years-and perhaps because most random spanning trees are similar, they tend to give similar results.) As emphasized by Benoit Mandelbrot in the 1970s and 1980s, topography and contour lines (notably coastlines) seem to show apparently random structure on a wide range of scales—with definite power laws being measured in quite a few cases. And presumably at some level this is the result of the nested patterns in which erosion occurs. (An unrelated effect is that as a result of the

dynamics of flow in it, even a single river on a featureless landscape will typically tend to increase the curvature of its meanders, until they break off and form oxbow lakes.)

#### Fundamental Issues in Biology

■ Page 383 · History. The origins of biological complexity have been debated since antiquity. For a long time it was assumed that the magnitude of the complexity was so great that it could never have arisen from any ordinary natural process, and therefore must have been inserted from outside through some kind of divine plan. However, with the publication of Charles Darwin's Origin of Species in 1859 it became clear that there were natural processes that could in fact shape features of biological organisms. There was no specific argument for why natural selection should lead to the development of complexity, although Darwin appears to have believed that this would emerge somewhat like a principle in physics. In the century or so after the publication of Origin of Species many detailed aspects of natural selection were elucidated, but the increasing use of traditional mathematical methods largely precluded serious analysis of complexity. Continuing controversy about contradictions with religious accounts of creation caused most scientists to be adamant in assuming that every aspect of biological systems must be shaped purely by natural selection. And by the 1980s natural selection had become firmly enshrined as a force of practically unbounded power, assumed-though without specific evidence—to be capable of solving almost any problem and producing almost any degree of complexity.

My own work on cellular automata in the early 1980s showed that great complexity could be generated just from simple programs, without any process like natural selection. But although I and others believed that my results should be relevant to biological systems there was still a pervasive belief that the level of complexity seen in biology must somehow be uniquely associated with natural selection. In the late 1980s the study of artificial life caused several detailed computer simulations of natural selection to be done, and these simulations reproduced various known features of biological evolution. But from looking at such simulations, as well as from my own experiments done from 1980 onwards. I increasingly came to believe that almost any complexity being generated had its origin in phenomena similar to those I had seen in cellular automata-and had essentially nothing to do with natural selection.

■ Attitudes of biologists. Over the years, I have discussed versions of the ideas in this section with many biologists of different kinds. Most are quick to point out at least anecdotal cases in which features of organisms do not seem to have been shaped by natural selection. But if asked about complexity-either in specific examples or in general-the vast majority soon end up trying to give explanations based on natural selection. Those with a historical bent often recognize that the origins of complexity have always been somewhat mysterious in biology, and indeed sometimes state that this has laid the field open to many attacks. But generally my experience has been that the further one goes from those involved with specific molecular or other details of biological systems the more one encounters a fundamental conviction that natural selection must be the ultimate origin of any important feature of biological systems.

- Page 383 · Genetic programs. Genetic programs encoded as sequences of four possible nucleotide bases on strands of DNA or RNA. The simplest known viruses have programs that are a few thousand elements in length; bacteria typically have programs that are a few million elements; fruit flies a few hundred million; and humans around four billion. There is not a uniform correspondence between apparent sophistication of organisms and lengths of genetic programs: different species of amphibians, for example, have programs that can differ in length by a factor of a hundred, and can be as many as tens of billions of elements long. Genetic programs are normally broken into sections, many of which are genes that provide templates for making particular proteins. In humans, there are perhaps around 40,000 genes, specifying proteins for about 200 distinct cell types. Many of the low-level details of how proteins are produced is now known, but higher-level issues about organization into different cell types remain somewhat mysterious. Note that although most of the information necessary to construct an organism is encoded in its genetic program, other material in the original egg cell or the environment before birth can probably also sometimes be relevant.
- Page 386 · Tricks in evolution. Among the tricks used are: sexual reproduction, causing large-scale mixing of similar programs; organs, suborganisms, symbiosis and parasitism, allowing different parts of programs to be optimized separately; mutation rate enzymes, allowing parts that need change to be searched more quickly; learnability in individual organisms, allowing larger local deviations from optimality to be tried.
- Page 387 · Belief in optimality. The notion that features of biological organisms are always somehow optimized for a particular purpose has become extremely deep seated-and indeed it has been discussed since antiquity. Most modern biologists at least pay lip service to historical accidents and

developmental constraints, but if pressed revert surprisingly quickly to the notion of optimization for a purpose.

- Page 390 · Studying natural selection. From the basic description of natural selection one might have thought that it would correspond to a unique simple program. But in fact there are always many somewhat arbitrary details, particularly centering around exactly how to prune less fit organisms. And the consequence of this is that in my experience it is essentially impossible to come up with precise definitive conclusions about natural selection on the basis of specific simple computer experiments. Using the Principle of Computational Equivalence discussed in Chapter 12, however, I suspect that it will nevertheless be possible to develop a general theory of what natural selection typically can and cannot do.
- Page 391 · Other models. Sequential substitution systems are probably more realistic than cellular automata as models of genetic programs, since elements can explicitly be added to their rules at will. As a rather different approach, one can consider a fixed underlying rule—say a class 4 cellular automaton-with modifications in initial conditions. The notion of universality in Chapter 11 implies that under suitable conditions this should be equivalent to modifications in rules. As an alternative to modelling individual organisms, one can also consider substitution systems which directly generate genealogical trees for populations of organisms, somewhat like Leonardo Fibonacci's original model of a rabbit population.
- Page 391 · Adaptive value of complexity. One might think that the reason complexity is not more widespread in biology is that somehow it is too sensitive to perturbations. But in fact, as discussed in Chapter 7, randomness and complexity tend to lead to more, rather than less, robustness in overall behavior. Indeed, many even seemingly simple biological processes appear to be stabilized by randomness-leading, for example, to random fluctuations in interbeat intervals for healthy hearts. And some biological processes rely directly on complex or random phenomena-for example, finding good paths for foraging for food, avoiding predators or mounting suitable immune responses. (Compare page 1192.)
- Page 393 · Genetic algorithms. As mentioned on page 985, it is straightforward to apply natural selection to computer programs, and for certain kinds of practical tasks with appropriate continuity properties this may be a useful approach.
- Page 394 · Smooth variables. Despite their importance in understanding natural selection both in biology and in potential computational applications, the fundamental

origins of smooth variables or so-called quantitative traits seem to have been investigated rather little. Within populations of organisms such traits are often found to have Gaussian distributions (as, for example, in heights of humans), but this gives little clue as to their origin. (Weights of humans nevertheless have closer to a lognormal distribution.) It is generally assumed that smooth variables must be associated with so-called polygenes that effectively include a large number of individual discrete genes. In pre-Mendelian genetics, observations on smooth variables are presumably what led to the theory that traits of offspring are determined by smoothly mixing the blood of their parents.

- Page 395 · Species. One feature of biological organisms is that they normally occur in discrete species, with distinct differences between different species. It seems likely that the existence of such discreteness is related to the discreteness of underlying genetic programs. Currently there are a few million species known. Most are distinguished just by their habitats, visual appearance or various simple numerical characteristics. Sometimes, however, it is known that members of different species have the traditional defining characteristic that they cannot normally mate, though this may well be more a matter of the mechanics of mating and development than a fundamental feature.
- **Defining life.** See pages 823 and 1178.
- Page 397 · Analogies with thermodynamics. Over the past century there have been a number of attempts to connect the development of complexity in biological systems with the increase of entropy in thermodynamic systems. In fact, when it was first introduced the very term "entropy" was supposed to suggest an analogy with biological evolution. But despite this, no detailed correspondence between thermodynamics and evolution has ever been forthcoming. However, my statement here that complexity in biology can occur because natural selection cannot control complex behavior is rather similar to my statement in Chapter 9 that entropy can increase because physical experiments in a sense also cannot control complex behavior.
- Page 398 · Major new features. Traditional groupings of living organisms into kingdoms and phyla are typically defined by the presence of major new features. Standard examples from higher animals include regulation of body temperature and internal gestation of young. Important examples from earlier in the history of life include nuclear membranes, sexual reproduction, multicellularity, protective shells and photosynthesis.

Trilobites are a fairly clear example of organisms where over the course of a few hundred million years the fossil record

shows increases in apparent morphological complexity, followed by decreases. Something similar can be seen in the historical evolution of technological systems such as cars.

- Software statistics. Empirical analysis of the million or so lines of source code that make up Mathematica suggests that different functions-which are roughly analogous to different genes-rather accurately follow an exponential distribution of sizes, with a slightly elevated tail.
- Proteins. At a molecular level much of any living cell is made up of proteins formed from chains of tens to thousands of amino acids. Of the thousands of proteins now known some (like keratin and collagen) are fibrous, and have a simple repetitive underlying structure. But many are globular, and have at least a core in which the 3D packing of amino acids seems quite random. Usually there are some sections that consist of simple  $\alpha$  helices,  $\beta$  sheets, or combinations of these. But other parts—often including sites important for function—seem more like random walks. At some level the 3D shapes of proteins (tertiary structure) are presumably determined by energy minimization. But in practice very different shapes can probably have almost identical energies, so that in as much as a given protein always takes on the same shape this must be associated with the dynamics of the process by which the protein folds when it is assembled. (Compare page 988.) One might expect that biological evolution would have had obvious effects on proteins. But as mentioned on page 1184 the actual sequences of amino acids in proteins typically appear quite random. And at some level this is presumably why there seems to be so much randomness in their shapes. (Biological evolution may conceivably have selected for proteins that fold reliably or are more robust with respect to changes in single amino acids, but there is currently no clear evidence for this.)

#### Growth of Plants and Animals

■ **History.** The first steps towards a theory of biological form were already taken in Greek times with attempts-notably by Aristotle-to classify biological organisms and to understand their growth. By the 1600s extensive classification had been done, and many structural features had been identified as in common between different organisms. But despite hopes on the part of René Descartes, Galileo and others that biological processes might follow the same kind of rigid clockwork rules that were beginning to emerge in physics, no general principles were forthcoming. Rough analogies between the forms and functions of biological and non-biological systems were fairly common among both artists and scientists, but were rarely thought to

have much scientific significance. In the 1800s more detailed analogies began to emerge, sometimes as offshoots of the field of morphology named by Johann Goethe, and sometimes with mathematical interpretations, and in 1917 D'Arcy Thompson published the first edition of his book On Growth and Form which used mathematical methodsmostly from analytical geometry-to discuss a variety of biological processes, usually in analogy with ones in physics. But emphasis on evolutionary rather than mechanistic explanations for a long time caused little further work to be done along these lines. Much additional data was obtained, particularly in embryology, and by the 1930s it seemed fairly clear that at least some aspects of growth in the embryo were controlled by chemical messengers. In 1951 Alan Turing worked out a general mathematical model of this based on reaction-diffusion equations, and suggested that such a model might account for many pigmentation and structural patterns in biological systems (see page 1012). For nearly twenty years, however, no significant follow-up was done on this idea. There were quite a few attemptsoften misguided in my opinion-to use traditional ideas from physics and engineering to derive forms of biological organisms from constraints of mechanical or other optimality. And in the late 1960s, René Thom made an important attempt to use sophisticated methods from topology to develop a general theory of biological form. But the mathematics of his work was inaccessible to most natural scientists, and its popularized version, known as catastrophe theory, largely fell into disrepute.

The idea of comparing systems in biology and engineering dates back to antiquity, but for a long time it was mainly thought of just as an inspiration for engineering. In the mid-1940s, however, mostly under the banner of cybernetics, tools from the analysis of electrical systems began to be used for studying biological systems. And partly from this-with much reinforcement from the discovery of the genetic code-there emerged the idea of thinking about biological systems in purely abstract logical or computational terms. This led to an early introduction of 2D cellular automata (see page 876), but the emphasis was on ambitious general questions rather than specific models. Little progress was made, and by the 1960s most work along these lines had petered out. In the late 1970s, however, fractals and L systems (see below) began to provide examples where simple rules could be seen to yield biological-like branching behavior. And in the 1980s, interest in non-equilibrium physical processes, and in phenomena such as diffusion-limited aggregation, led to renewed interest in reaction-diffusion equations, and to somewhat more explicit models for various biological processes. My own work on cellular automata in the early 1980s started a number of new lines of computational modelling, some of which became involved in the rise and fall of the artificial life movement in the late 1980s and early 1990s.

- Page 400 · Growth in plants. At the lowest level, the growth of any organism proceeds by either division or expansion of cells, together with occasional formation of cavities between cells. In plants, cells typically expand—normally through intake of water-only for a limited period, after which the cellulose in their walls crystallizes to make them quite rigid. In most plants—at least after the embryonic stage—cells typically divide only in localized regions known as meristems, and each division yields one cell that can divide again, and one that cannot. Often the very tip of a stem consists of a single cell in the shape of an inverted tetrahedron, and in lower plants such as mosses this is essentially the only cell that divides. In flowering plants, cell division normally occurs around the edge of a region of size 0.2-1 mm containing many tens of cells. (Hearts of palm in palm trees can however be much larger.) The details of how cell division works in plants remain largely unknown. There is some evidence that orientation of new cells is in part controlled by microscopic fibers. Various small molecules that can diffuse between cells (such as socalled auxins) are known to affect growth and production of new stems (see below).
- Page 401 · Branching in plants. Almost all kinds of plants exhibit some form of branching, and particularly in smaller plants the branching is often extremely regular. In a plant as large as a typical tree-particularly one that grows slowlydifferent conditions associated with the growth of different branches may however destroy some of the regularity of branching. Among algae and more primitive plants such as whisk ferns, repeated splitting of a single branch into two is particularly common. Ferns and conifers both typically exhibit three-way branching. Among flowering plants socalled dicotyledons exhibit branching throughout the plant. Monocotyledons-of which palms and grasses are two examples-typically have only one primary site of growth, and thus do not exhibit repeated branching. (In grasses the growth site is at the bottom of the stem, and in bamboos there are multiple growth sites up the stem.)

The forms of branching in plants have been used as means of classification since antiquity. Alexander von Humboldt in 1808 identified 19 overall types of branching which have been used, with some modifications, by plant geographers and botanists ever since. Note that in the vast majority of cases, branches do not lie in a plane; often they are instead arranged in a spiral, as discussed on page 408. But when projected into two dimensions, the patterns obtained still look similar to those in the main text.

- Page 402 · Implementation. It is convenient to represent the positions of all tips by complex numbers. One can take the original stem to extend from the point -1 to 0; the rule is then specified by the list b of complex numbers corresponding to the positions of the new tip obtained after one step. And after *n* steps the positions of all tips generated are given simply by Nest[Flatten[Outer[Times, 1+#, b]] &, {0}, n]
- **Mathematical properties.** If an element *c* of the list *b* is real, so that there is a stem that goes straight up, then the limiting height of the center of the pattern is obtained by summing a geometric series, and is given by 1/(1-c). The overall limiting pattern will be finite so long as Abs[c] < 1 for all elements of b. After n steps the total length of all stems is given by Apply[Plus, Abs[b]]<sup>n</sup>. (See page 1006 for other properties.)
- Page 402 · Simple geometries. Page 357 shows how some of the nested patterns commonly seen in this book can be produced by the growth processes shown here.
- History of branching models. The concept of systematic rules for the way that stems-particularly those carrying flowers-are connected in a plant seems to have been clearly understood among botanists by the 1800s. Only with the advent of computer graphics in the 1970s, however, does the idea appear to have arisen of varying angles to get different forms. An early example was the work of Hisao Honda in 1970 on the structure of trees. Pictures analogous to the bottom row on page 402 were also generated by Benoit Mandelbrot in connection with his development of fractals. Starting in 1967 Aristid Lindenmayer emphasized the use of substitution or L systems (see page 893) as a way of modelling patterns of connections in plants. And beginning in the early 1980s—particularly through work by Alvy Ray Smith and later Przemyslaw Prusinkiewiczmodels based on L systems and fractals became routinely used for producing images of plants in practical computer graphics. Around the same time Michael Barnsley also used so-called iterated function systems to make pictures of ferns-but he appears to have viewed these more as a curiosity than a contribution to botany. Over the past decade or so, a few mentions have been made of using complicated models based on L systems to reproduce shapes of specific types of leaves, but so far as I can tell, nothing like the simple model that I describe in the main text has ever been considered before.

■ Page 404 · Leaf shapes. Leaves are usually put into categories like the ones below, with names mostly derived from Latin words for similar-looking objects.

![](Images/_page_1020_Figure_8.jpeg)

Some classification of leaf shapes was done by Theophrastus as early as 300 BC, and classifications similar to those above were in use by the early Renaissance period. (They appear for example in the first edition of the Encyclopedia Britannica from 1768.) Leaf shapes have been widely used since antiquity as a way of identifying plants-initially particularly for medicinal purposes. But there has been very little general scientific investigation of leaf shapes, and most of what has been done has concentrated on the expansion of leaves once they are out of their buds. Already in 1724 Stephen Hales looked at the motion of grids of marks on fig leaves, and noted that growth seemed to occur more or less uniformly throughout the leaf. Similar but increasingly quantitative studies have been made ever since, and have reported a variety of non-uniformities in growth. For a long time it was believed that after leaves came out of their buds growth was due mainly to cell expansion, but in the 1980s it became clear that many cell divisions in fact occur, both on the boundary and the interior. At the earliest stages, buds that will turn into leaves start as bumps on a plant stem, with a structure that is essentially impossible to discern. Surgically modifying such buds when they are as small as 0.1 mm can have dramatic effects on final leaf shape, suggesting that at least some aspects of the shape are already determined at that point. On a single plant different leaves can have somewhat different shapes-sometimes for example those lower on a tree are smoother, while those higher are pointier. It may nevertheless be that leaves on a single plant initially have a discrete set of possible shapes, with variations in final shape arising from differences in environmental conditions during expansion. My model for leaf shapes is presumably most relevant for initial shapes.

Traditional evolutionary explanations have not had much to say about detailed questions of leaf shape; one minor claim is that the pointed tips at the ends of many tropical leaves exist to allow moisture to drip off the leaves. The fossil record suggests that leaves first arose roughly 400 million years ago, probably when collections of branches which lay in a plane became joined by webbing. Early plants such as ferns have compound leaves in which explicit branching structure is still seen. Extremely few models for shapes of individual leaves appear to have ever been proposed. In 1917 D'Arcy Thompson mentioned that leaves might have growth rates that are simple functions of angle, and drew the first of the pictures shown below.

![](Images/_page_1021_Picture_2.jpeg)

![](Images/_page_1021_Picture_3.jpeg)

![](Images/_page_1021_Picture_4.jpeg)

![](Images/_page_1021_Picture_5.jpeg)

![](Images/_page_1021_Picture_6.jpeg)

With new tip positions as on page 400 given by  $\{p \, Exp[i \, \theta], \, p \, Exp[-i \, \theta], \, q\}$ , rough  $\{p, \, q, \, \theta\}$  for at least some versions of some common plants include: wild carrot (Queen Anne's lace)  $\{0.4, \, 0.7, \, 30^{\circ}\}$ , cypress  $\{0.4, \, 0.7, \, 45^{\circ}\}$ , coralbells  $\{0.5, \, 0.4, \, 0^{\circ}\}$ , ivy  $\{0.5, \, 0.6, \, 0^{\circ}\}$ , grape  $\{0.5, \, 0.6, \, 15^{\circ}\}$ , sycamore  $\{0.5, \, 0.6, \, 15^{\circ}\}$ , mallow  $\{0.5, \, 0.6, \, 30^{\circ}\}$ , goosefoot  $\{0.55, \, 0.8, \, 30^{\circ}\}$ , willow  $\{0.55, \, 0.8, \, 80^{\circ}\}$ , morning glory  $\{0.7, \, 0.8, \, 0^{\circ}\}$ , cucumber  $\{0.7, \, 0.8, \, 15^{\circ}\}$ , ginger  $\{0.65, \, 0.6, \, 15^{\circ}\}$ 

- Page 404 · Self-limiting growth. It is often said that in plants, unlike animals, there is no global control of growth. And one feature of the simple branching processes I describe is that for purely mathematical reasons, their rules always produce structures that are of limited size. Note that in fact it is known that there is some global control of growth even in plants: for example hormones produced by leaves can affect growth of roots.
- Page 407 · Parameter space sets. Points in the space of parameters can conveniently be labelled by a complex number c, where the imaginary direction is taken to increase to the right. The pattern corresponding to each point is the limit of  $Nest[Flatten[1 + \{c\#, Conjugate[c]\#\}] \&, \{1\}, n] \text{ when } n \to \infty.$ Such a limiting pattern exists only within the unit circle Abs[c] < 1. It then turns out that the limiting pattern is either completely connected or completely disconnected; which it is depends on whether it contains any points on the vertical axis Im[c] = 0. Every point in the pattern must correspond to some list of left and right branchings, represented by 0's and 1's respectively; in terms of this list the position of the point is given by Fold[1 + {c, Conjugate[c]}[[1 + #2]] #1 &, 1, Reverse[list]]. Patterns are disconnected if there is a gap between the parts obtained from lists starting with 0 and with 1. The magnitude of this gap turns out to be given by

```
With[{d = Conjugate[c], r = 1 - Abs[c]^2},

Which[Im[c] < 0, d, Im[c] == 0, 0,

Re[c] > 0, With[{n = Ceiling[\pi/2/Arg[c]]},

Im[c(1-d^))/(1-d)] + Im[cd^(1+d)]/r], Arg[c] >

3 \pi/4, Im[c+c<sup>2</sup>]/r, True, Im[c] + Im[c<sup>2</sup>+c<sup>3</sup>]/r]]
```

The picture below shows the region for which the gap is positive, corresponding to trees which are not connected. (This region was found by Michael Barnsley and others in the late 1980s.) The overall maximum gap occurs at  $c = 1/2 \, Sqrt[5 - \sqrt{17} \, ] \, i$ . The bottom boundary of the region lies along Re[c] = -1/2; the extremal point on the edge of the gap in this case corresponds to  $\{0, 0, 1, 0, 1, 0, 1, ...\}$  where the last two elements repeat forever. The rest of the boundary consists of a sequence of algebraic curves, with almost imperceptible changes in slope in between; the first corresponds to  $\{0, 0, 0, 1, 0, 1, 0, 1, ...\}$ , while subsequent ones correspond to  $\{0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, ...\}$ ,  $\{0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, ...\}$ , etc.

![](Images/_page_1021_Picture_13.jpeg)

![](Images/_page_1021_Picture_14.jpeg)

In the pictures in the main text, the black region is connected wherever it does not protrude into the shaded region, which corresponds to disconnected patterns, in the pictures above. And in general it turns out that near any particular value of c the sets shown in black in the main text always look at sufficient magnification like the pattern that would be obtained for that value of c. The reason for this is that if c changes only slightly, then the pattern to a first approximation deforms only slightly, so that the part seen through the peephole just shifts, and in a small region of c values the peephole in effect simply scans over different parts of the pattern.

A simple way to approximate the pictures in the main text would be to generate patterns by iterating the substitution system a fixed number of times. In practice, however, it is essential to prune the tree of points at each stage. And at least for <code>Abs[c]</code> not too close to 1, this can be done by discarding points that are so far away from the peephole that their descendents could not possibly return to it.

The parameter space sets discussed here are somewhat analogous to the Mandelbrot set discussed on page 934, though in many ways easier to understand.

(See also the discussion of universal objects on page 1127.)

■ Page 409 · Mathematics of phyllotaxis. A rotation by  $GoldenRatio = (1 + \sqrt{5})/2$  turns is equivalent to a rotation by  $2 - GoldenRatio = GoldenRatio^{-2} \simeq 0.38$  turns, or  $137.5^{\circ}$ . Successive approximations to this number are given by Fibonacci[n-2]/Fibonacci[n], so that elements numbered Fibonacci[n] (i.e. 1, 2, 3, 5, 8, 13, ...) will be the ones that come closest to being a whole number of turns apart, and thus to being lined up on the stem. As mentioned on page 891, having GoldenRatio turns between elements makes them in a

sense as evenly distributed as possible, given that they are added sequentially.

- History of phyllotaxis. The regularities of phyllotaxis were presumably noticed in antiquity, and were certainly recognized in the 1400s, notably by Leonardo da Vinci. By the 1800s various mathematical features of phyllotaxis were known, and in 1837 Louis and Auguste Bravais identified the presence of a golden ratio angle. In 1868 Wilhelm Hofmeister proposed that new elements form in the largest gap left by previous elements. And in 1913 Johannes Schoute argued that diffusion of a chemical creates fields of inhibition around new elements—a model in outline equivalent to mine. In the past century features of phyllotaxis have been rediscovered surprisingly many times, with work being done quite independently both in abstract mathematical settings, and in the context of specific models (most of which are ultimately very similar). One development in the 1990s is the generation of phyllotaxis-like patterns in superconductors, ferrofluids and other physical systems.
- Observed phyllotaxis. Many spiral patterns in actual plants converge to within a degree or less of 137.5°, though just as in the model in the main text, there are usually deviations for the first few elements produced. The angles are particularly accurate in, for example, flower heads—where it is likely the positions of elements are adjusted by mechanical forces after they are originally generated. Other examples of phyllotaxis-like patterns in biology include the scales of pangolins and surfaces of tooth-like structures in certain kinds of rays and sharks.
- **Projections of patterns.** The literature of phyllotaxis is full of baroque descriptions of the features of projections of patterns with golden ratio angles. In the pictures below, the  $n^{th}$  point has position  $(\sqrt{n} \{Sin[\#], Cos[\#]\} \&)[2 \pi n Golden Ratio]$ , and in such pictures regular spirals or parastichies emanating from the center are seen whenever points whose numbers differ by Fibonacci[m] are joined. Note that the tips of many growing stems seem to be approximately paraboloidal, making the  $n^{\text{th}}$  point a distance  $\sqrt{n}$  from the center.

![](Images/_page_1022_Picture_6.jpeg)

![](Images/_page_1022_Picture_7.jpeg)

- Page 410 · Implementation. It is convenient to consider a line of discrete cells, much as in a continuous cellular automaton. With a concentrations list c, the position p of a new element is given by Position[c, Max[c], 1, 1][[1, 1]], while the new list of concentrations is  $\lambda c + RotateRight[f, p]$ where f is a list of depletions associated with addition of a new element at position 1. In the main text a Gaussian form is used for f. Other smooth functions typically nevertheless yield identical results. Note that in order to get an accurate approximation to a golden ratio angle there must be a fairly large number of cells.
- Shapes of cells. Many types of cells are arranged like typical 3D packings of deformable objects (see page 988)—with considerable apparent randomness in individual shapes and positions, but definite overall statistical properties. Cells arranged on a surface—as in the retina or in skin—or that are intrinsically elongated—as in muscle—tend again to be arranged like typical packings, but now in 2D, where a regular hexagonal grid is formed.
- Page 412 · Symmetries. Biological systems often show definite discrete symmetry. (In monocotyledon plants there is usually 3-fold symmetry; in dicotyledons 4- or 5-fold. Animals like starfish often have 5-fold symmetry; higher animals usually only 2-fold symmetry. There are fossils with 7- and 9-fold symmetry. At microscopic levels there are sometimes other symmetries: cilia of eukaryotic cells can for example show 9- and 13-fold symmetry. In the phyllotaxis process discussed in the main text one new element is produced at a time. But if several elements are produced together the same basic mechanism will tend to make these elements be equally spaced in angle-leading to overall discrete symmetry. (Individual proteins sometimes also arrange themselves into overall structures that have discrete symmetries—which can then be reflected in shapes of cells or larger objects.) (See also page 1011.)
- Page 412 · Locally isotropic growth. A convenient way to see what happens if elements of a surface grow isotropically is to divide the surface into a collection of very small circles, and then to expand the circle at each point by a factor h[x, y]. If the local curvature of the surface is originally c[x, y], then after such growth, the curvature turns out to be (c[x, y] + Laplacian[Log[h[x, y]]])/h[x, y]where  $Laplacian[f_{-}] := \partial_{xx} f + \partial_{yy} f$ . In order for the surface to stay flat its growth rate Log[h[x, y]] must therefore solve Laplace's equation, and hence must be a harmonic function Re[f[x+iy]]. This is equivalent to saying that the growth must correspond to a conformal mapping which locally preserves angles. The pictures below show results for several growth rate functions; in the last case, the function

is not harmonic, and the surface cannot be drawn in the plane without tearing. Note that if the elements of a surface are allowed to change shape, then the surface can always remain flat, as in the top row of pictures on page 412. Harmonic growth rate functions can potentially be obtained from the large-time effects of a chemical subject to diffusion. And this may perhaps be related to the flatness observed in the growth of leaves. (See also page 1010.)

![](Images/_page_1023_Picture_2.jpeg)

![](Images/_page_1023_Picture_3.jpeg)

![](Images/_page_1023_Picture_4.jpeg)

![](Images/_page_1023_Picture_5.jpeg)

- Page 413 · Branching in animals. Capillaries, bronchioles and kidney ducts in higher animals typically seem to form trees in which each tip as it extends repeatedly splits into two branches. (In human lungs, for example, there are about 20 levels of branching.) The same kind of structure is seen in the digestive systems of lower animals—as visible externally, for example, in the arms of a basket star.
- Page 413 · Antlers. Like stems of plants antlers grow at their tips, and can thus exhibit branching. This is made possible by the fact that antlers, unlike horns, have a layer of soft tissue on the outside—which delivers the nutrients needed for growth to occur on the outer surface of the bone at their tips.
- Page 414 · Shells. Shells grow through the secretion of rigid material from the soft lip or mantle of the animal inside, and over periods of months to years they form coiled structures that normally follow rather accurate equiangular spirals, typically right-handed. The number of turns or whorls varies widely, from less than one in a typical bivalve, to more than thirty in a highly pointed univalve such as a screw shell. Usually the coiled structure is obvious from looking at the apex on the outside of the shell, but in cowries, for example, it is made less obvious by the fact that later whorls completely cover earlier ones, and at the opening of the shell some dissolving and resculpting of material occurs. In addition to smooth coiled overall structures, some shells exhibit spines. These are associated with tentacles of tissue which secrete shell material at their tips as they grow. Inside shells such as nautiluses, there are a sequence of sealed chambers, with septa between them laid down perhaps once a month. These septa in present-day species are smooth, but in fossil ammonites they can be highly corrugated. Typically the corrugations are accurately symmetrical, and I suspect that they in effect represent slices through a lettuce-leaf-like structure formed from a surface with tree-like internal growth.

■ **Shell model.** The center of the opening of a shell is taken to trace out a helix whose  $\{x, y, z\}$  coordinates are given as a function of the total angle of revolution t by  $a^t \{Cos[t], Sin[t], b\}$ . On row (a) of page 415 the parameter a varies from 1.05 to 1.65, while on row (b) b varies from 0 to 6. The complete surface of the shell is obtained by varying both t and  $\theta$  in

 $\begin{array}{l} a^t \left\{ Cos[t] (1+c \left(Cos[e] Cos[\theta] + d Sin[e] Sin[\theta] \right) \right), \\ Sin[t] (1+c \left(Cos[e] Cos[\theta] + d Sin[e] Sin[\theta] \right) \right), \\ b+c \left(Cos[\theta] Sin[e] - d Cos[e] Sin[\theta] \right) \end{array}$ 

where c varies from 0.4 to 1.6 on row (c), d from 1 to 4 on row (d) and e from 0 to 1.2 on row (e). For many values of parameters the surface defined by this formula intersects itself. However, in an actual shell material can only be added on the outside of what already exists, and this can be represented by restricting  $\theta$  to run over only part of the range  $-\pi$  to  $\pi$ . The effect of this on internal structure can be seen in the slice of the cone shell on row (b) of page 414. Most real shells follow the model described here with remarkable accuracy. There are, however, deviations in some species, most often as a result of gradual changes in parameters during the life of the organism. As the pictures in the main text show, shells of actual molluscs (both current and fossil) exist throughout a large region of parameter space. And in fact it appears that the only parameter values that are not covered are ones where the shell could not easily have been secreted by an animal because its shape is degenerate and leaves little useful room for the animal. Some regions of parameter space are more common than others, and this may be a consequence either of natural selection or of the detailed molecular biology of mollusc growth. Shells where successive whorls do not touch (as in the first picture on row (c) of page 415) appear to be significantly less common than others, perhaps because they have lower mechanical rigidity. They do however occur, though sometimes as internal rather than external shells.

■ History. Following Aristotle's notion of gnomon figures that keep the same shape when they grow, equiangular spirals were discussed by René Descartes in 1638, and soon thereafter Christopher Wren noted their relation to shells. A clear mathematical model of shell growth based on equiangular spirals was given by Henry Moseley in 1838, and the model used here is a direct extension of his. Careful studies from the mid-1800s to mid-1900s validated Moseley's basic model for a wide variety of shells, though an increasing emphasis was placed on shells that showed deviations from the model. In the mid-1960s David Raup used early computer graphics to generate pictures for various ranges of parameters, but perhaps because he considered only specific classes of molluscs there emerged from his work the belief

that parameters of shells are greatly constrained-with explanations being proposed based on optimization of such features as strength, relative volume, and stability when falling through water. But as discussed in the main text I strongly suspect that in fact there are no such global constraints, and instead almost all reasonable values of parameters from the simple model used do actually occur in real molluscs. In the past few decades, increasingly complex models for shells have been constructed, typically focusing on fairly specific or unusual cases. Most of these models have far more parameters than the simple one used here, and by varying these parameters it is almost always possible to get forms that probably do not correspond to real shells. And presumably the reason for this is just that such models represent processes that do not occur in the growth of actual molluscs. One widespread issue concerns the orientation of the opening to a shell. The model used here assumes that this opening always stays vertical—which appears to be what happens most often in practice. But following the notion of Frenet frames in differential geometry, it has often come to be supposed that the opening to a shell instead typically lies in a plane perpendicular to the helix traced out by the growth of the shell. This idea, however, leads to twisted shapes like those shown below that occur rarely, if ever, in actual shells. And in fact, despite elaborate efforts of computer graphics it has proved rather difficult with parametrizations based on Frenet frames to produce shells that have a reasonable range of realistic shapes.

![](Images/_page_1024_Picture_3.jpeg)

- Page 417 · Discrete folding. See page 892.
- Page 418 · Intrinsically defined curves. With curvature given by a function f[s] of the arc length s, explicit coordinates  $\{x[s], y[s]\}$  of points are obtained from (compare page 1048)

 $NDSolve[\{x'[s] = Cos[\theta[s]], \ y'[s] = Sin[\theta[s]], \ \theta'[s] =$  $f[s], x[0] = y[0] = \theta[0] = 0$ ,  $\{x, y, \theta\}, \{s, 0, s_{max}\}$ 

For various choices of f[s], formulas for  $\{x[s], y[s]\}$  can be found using DSolve:

f[s] = 1:  $\{Sin[\theta], Cos[\theta]\}$  $f[s] = s: \{FresnelS[\theta], FresnelC[\theta]\}$  $f[s] = 1/\sqrt{s} : \sqrt{\theta} \{Sin[\sqrt{\theta}], Cos[\sqrt{\theta}]\}$ f[s] = 1/s:  $\theta \{Cos[Log[\theta]], Sin[Log[\theta]]\}$  $f[s] = 1/s^2 : \theta \{Sin[1/\theta], Cos[1/\theta]\}$ 

 $f[s] = s^n$ : result involves  $Gamma[1/n, \pm i \theta^n/n]$ f[s] = Sin[s]: result involves  $Integrate[Sin[Sin[\theta]], \theta]$ , expressible in terms of generalized Kampé de Fériet hypergeometric functions of two variables.

When  $s_{max} \rightarrow \infty$ , f[s] = a s Sin[s] yields 2D shapes that are basically nested, with pieces overlapping for Abs[a] < 1.

The general idea of so-called natural equations for obtaining curves from local curvature appears to have been first considered by Leonhard Euler in 1736. Many examples with fairly simple behavior were studied in the 1800s. The case of f[s] = a Sin[b s] was studied by Eduard Lehr in 1932. Cases related to f[s] = s Sin[s] were studied by Alfred Gray around 1992 using Mathematica.

■ Multidimensional generalizations. Curvatures for surfaces and higher-dimensional objects can be defined in terms of the principal axes of approximating ellipsoids at each point. There are combinations of these curvatures—in 2D Gaussian curvature and mean curvature—which are independent of the coordinate system used. (Compare page 1049.) Given such curvatures, a surface can in principle be obtained by solving certain partial differential equations. But even in the case of zero mean curvature, which corresponds to minimal surfaces of the kind followed by an idealized soap film, this is already a mathematical problem of significant difficulty.

If one looks at projections of surfaces, it is common to see lines of discontinuity at which a surface goes, say, from having three sheets to one. Catastrophe theory provides a classification of such discontinuities—the simplest being a cusp. And as emphasized by René Thom in the 1960s, it is possible that some structures seen in animals may be related to such discontinuities.

■ Page 419 · Embryo development. Starting from a single egg cell, embryos first exhibit a series of geometrically quite precise cell divisions corresponding, I suspect, to a simple neighbor-independent substitution system. When the embryo consists of a definite number of cells-from tens to tens of thousands depending on species—the phenomenon of gastrulation occurs, and the hollow sphere of cells that has been produced folds in on itself so as to begin to form more tubular structures. In organisms with a total of just a few thousand cells, the final position and type of every cell seems to be determined directly by the genetic program of the organism; most likely what happens is that each cell division leads to some modification in genetic material, perhaps through rules like those in a multiway system. Beyond a few thousand cells, however, individual cells seem to be less relevant, and instead what appears to happen is that chemicals such as retinoic acid (a derivative of vitamin A) produced by particular cells diffuse to affect all cells in a region a tenth of a millimeter or so across. Probably as a result of chemical concentration gradients, different so-called homeobox genes are then activated in different parts of the region. Each of these genes—out of a total of 38 in humans—yields proteins which then in turn switch on or off large banks of genes, allowing different forms of behavior for cells in different places.

- History of embryology. General issues of embryology were already discussed in Greek times, notably by Hippocrates and Aristotle. But even in the 1700s it was still thought that perhaps every embryo started from a very small version of a complete organism. In the 1800s, however, detailed studies revealed the progressive development of complexity in the growth of an embryo. At the end of the 1800s experiments based on removing or modifying parts of early embryos began, and by the 1920s it had been discovered that there were definite pieces of embryos that were responsible for inducing various aspects of development to occur. That concentrations of diffusing chemicals might define where in an embryo different elements would form was first suggested in the early 1900s, but it was not until the 1970s and 1980s-after it was emphasized by Lewis Wolpert in 1969 under the name "positional information"—that there was clear experimental investigation of this idea. From the 1930s and before, it was known that different genes are involved in different aspects of embryo development. And with the advent of gene manipulation methods in the 1970s and 1980s, it became possible to investigate the genetic control of development in organisms such as fruit flies in tremendous detail. Among the important discoveries made were the homeobox genes (see note above).
- Page 420 · Bones. Precursors of bones can be identified quite early in the growth of most vertebrate embryos. Typically the cells involved are cartilage, with bone subsequently forming around them. In hardened bones growth normally occurs by replication of cartilage cells in plates perhaps a millimeter thick, with bone forming by a somewhat complicated process involving continual dissolving and redeposition of already hardened material. The rate at which bone grows depends on the pressure exerted on it, and presumably this allows feedback that for example prevents coiling. Quite how the complicated collection of tens of bones that make up a typical skull manage to grow so as to stay connected—often with highly corrugated suture lines—remains fairly mysterious.
- General constraints on growth. Given a system made from material with certain overall properties, one can ask what distributions of growth are consistent with those properties, and what kinds of shapes can be produced. With material

that is completely rigid growth can occur only at boundaries. With material where every part can deform arbitrarily any kind of growth can occur. With material where parts can locally expand, but cannot change their shape, page 1007 showed that a 2D surface will remain flat if the growth rate is a harmonic function. The Riemann mapping theorem of complex analysis then implies that even in this case, any smooth initial shape can grow into any other such shape with a suitable growth rate function. In a 3D system with locally isotropic growth the condition to avoid tearing is that the Ricci scalar curvature must vanish, and this is achieved if the local growth rate satisfies a certain partial differential equation. (See also page 1049.)

■ Parametrizations of growth. The idea that different objects-say different human bodies or faces-can be related by changing a small number of geometrical parameters was used by artists such as Albrecht Dürer in the 1500s, and may have been known to architects and others in antiquity. (In modern times this idea is associated for example with the notion that just a few measurements are sufficient to specify the fitting of clothes.) D'Arcy Thompson in 1917 suggested that shapes in many different species could also be related in this way. In the case of shells and horns he gave a fairly precise analysis, as discussed above. But he also drew various pictures of fishes and skulls, and argued that they were related by deformations of coordinates. Largely from this grew the field of morphometrics, in which the relative positions of features such as eyes or tips of fins are compared in different species. And although statistical significance is reduced by considering only discrete features, some evidence has emerged that different species do indeed have shapes related by changes in fairly small numbers of geometrical parameters. Such changes could be accounted for by changes in growth rates, but it is noteworthy that my results above on branching and folding make it clear that in general changes in growth rates can have much more dramatic effects.

As emphasized by D'Arcy Thompson, even a single organism will change shape if its parts grow at different rates. And in the 1930s and 1940s it became popular to study differential growth, typically under the name of allometry. Exponential growth was usually assumed, and there was much discussion about the details and correctness of this. Practical applications were made to farm animals, and later to changes in facial bone structure during childhood. But despite some work in the past twenty years using models based on fluids, solid mechanics and networks of rigid elements, much about differential growth remains unclear. (A better approach may be one similar to general relativity.)

- Schemes for growth. After the initial embryonic stage, many general features of the growth of different types of organisms can be viewed as consequences of the nature of the elements that make the organisms rigid. In plants, as we have discussed, essentially all cells have rigid cellulose walls. In vertebrate animals, rigidity comes mainly from bones that are internal to the organism. In arthropods and some other invertebrates, an exoskeleton is typically the main source of rigidity. Growth in such organisms usually then proceeds by adding soft tissue on the inside, then periodically moulting the exoskeleton. In a first approximation, the mechanical pressure of internal tissue will typically make the shape of the exoskeleton form an approximate minimal surface.
- Tumors. In both plants and animals tumors seem to grow mainly by fairly random addition of cells to their surfacemuch as in the aggregation models shown on page 332.
- Pollen. The grains of pollen produced by different species of plants have a remarkable range of different forms. Produced in groups of four, each grain is effectively a single cell (with two nuclei) between a few and few hundred microns across. At an overall level most grains seem to have regular polyhedral shapes, though often with bulges or dents. Perhaps such forms arise through grains effectively being made with small numbers of roughly spherical elements being either as tightly or loosely packed as possible. The outer walls of pollen grains are often covered with a certain density of tiny columns that can form spikes, or can have plates on top that can form cross-linkages and can join together to appear as patches.
- Radiolarians. The silicate skeletons of single-cell plankton organisms such as radiolarians and diatoms have been used for well over a century as examples of complex microscopic forms in biology. (See page 385.) Most likely their overall shapes are determined before they harden through minimization of area by surface tension. Their pores and cross-linkages presumably reflect packings of many roughly spherical elements on the surface during formation (as seen in the mid-1990s in aluminophosphates).
- Self-assembly. Some growth—particularly at a microscopic level-seems to be based on objects with particular shapes or affinities sticking together only in specific ways-much as in the systems based on constraints discussed on page 210 (and especially the network constraint systems of page 483). (See also page 1193.)
- **Animal behavior.** Simple repetitive behavior is common, as in circadian and brain rhythms, as well as peristalsis and walking. (In a millipede there are, for example, typically just two modes of locomotion, both simple, involving opposite

legs moving either together or oppositely.) Many structures built by animals have repetitive forms, as in beehives and spider webs; the more complex structures made for example by termites can perhaps be understood in terms of generalized aggregation systems (see page 978). (Typical models involve the notion of stigmergy: that elements are added at a particular point based only on features immediately around them; see also page 1184.) Nested patterns may occur in flocks of birds such as geese. Fairly regular nested space-filling curves are sometimes seen in the eating paths of caterpillars. Apparent randomness is common in physiological processes such as twitchings of muscles and microscopic eye motions, as well as in random walks executed during foraging. My suspicion is that just as there appear to be small collections of cells—so-called central pattern generators—that generate repetitive behavior, so also there will turn out to be small collections of cells that generate intrinsically random behavior.

#### **Biological Pigmentation Patterns**

- Collecting shells. The shells I show in this section are mostly from my fairly small personal collection, obtained at shops and markets around the world. (A few of the ones on page 416 are from the Field Museum.) The vast majority of shells on typical beaches do not have especially elaborate patterns. The Philippines are the largest current source of collectible shells: when molluscs intended as food are caught in nets interesting-looking shells are sometimes picked out before being discarded. Shell collecting as a hobby probably had its greatest popularity in the late 1700s and 1800s. In recent times one reason for studying animals that live in cone shells is that they produce potent neurotoxins that show promise as pain-control drugs.
- Shell patterns. The so-called mantle of soft tissue which covers the animal inside the shell is what secretes the shell and produces the pattern on it. Some species deposit material in a highly regular way every day; others seem to do it intermittently over periods of months or years. In many species the outer surface of the shell is covered by a kind of skin known as the periostracum, and in most cases this skin is opaque, thereby obscuring the patterns underneath until long after the animal has died. Note that if one makes a hole in a shell, the pattern is usually quite unaffected, suggesting that the pattern is primarily a consequence of features of the underlying mantle. In addition, patterns are often divided into three or four large bands, presumably in correspondence with features of the anatomy of the mantle. Sometimes physical ridges exist on shells in correspondence with their

pigmentation patterns. It is not clear whether multiple kinds of shell patterns can occur within one species, or whether they are always associated with genetically different species.

- Cowries. In cowries the outside of the shell is covered by the mantle of the animal. The patterns on the shell typically involve spots, and are typical of those obtained from 2D cellular automata of the kind shown on page 428. The mantle is normally in two parts; the boundary between them shows up as a discontinuity in the shell pattern.
- History. Elaborate patterns on shells have been noticed since antiquity, and have featured in a number of well-known works of art and literature. Since the late 1600s they have also been extensively used in classifying molluscs. But almost no efforts to understand the origins of such patterns seem to ever have been made. One study was done in 1969 by Conrad Waddington and Russell Cowe in which patterns on one particular kind of shell were reproduced by a specific computer simulation based on the idea of diverging waves of pigment. In 1982 I noticed that the patterns I had generated with 1D cellular automata looked remarkably similar to patterns on shells. I used this quite widely as an illustration of how cellular automata might be relevant to modelling natural systems. And I also made some efforts to do actual biological experiments, but I gave up when it seemed that the species of molluscs I wanted to study were difficult, if not impossible, to keep in captivity. Following my work, various other studies of shell patterns were done. Bard Ermentrout, John Campbell and George Oster constructed a model based on the idea that pigment-producing cells might act like nerve cells with a certain degree of memory. And Hans Meinhardt has constructed progressively more elaborate models based on reaction-diffusion equations.
- Page 426 · Animals shown. Flatworm, cuttlefish, honeycomb moray, spotted moray, foureye butterfly fish; emperor angelfish, suckermouth catfish, ornate cowfish, clown triggerfish, poison-dart frog; ornate horned frog, marbled salamander, spiny softshell, gila monster, ball python; graybanded kingsnake, guinea fowl, peacock, ring-tailed lemur, panda; cheetah, ocelot, leopard, tiger, spotted hyena; western spotted skunk, civet, zebra, brazilian tapir, giraffe.
- Animal coloration. Coloration can arise either directly through the presence of visible colored cells such as those in freckles, or indirectly by virtue of cells such as hair follicles imparting pigments to the non-living elements such as fur, feathers and scales that grow from them. In many cases such elements are arranged in a highly regular way, often in a repetitive hexagonal pattern. Evolutionary optimization is often used to explain observed pigmentation patterns—with

varying degrees of success. The notion that for example the stripes of a zebra are for camouflage may at first seem implausible, but there is some evidence that dramatic stripes do make it harder for a predator to recognize the overall shape of the zebra. Many of the pigments used by animals are by-products of metabolism, suggesting that at least at first pigmentation patterns were probably often incidental to the operation of the animal.

■ **Page 427 · Implementation.** Given a 2D array of values *a* and a list of weights *w*, each step in the evolution of the system corresponds to

```
WeightedStep[w\_List, a\_] := Map[If[\# > 0, 1, 0] \&, \\ Sum[w[[1+i]] Apply[Plus, Map[RotateLeft[a, \#] \&, \\ Layer[i]]], \{i, 0, Length[w] - 1\}], \{2\}] \\ Layer[n\_] := Layer[n] = Select[Flatten[Table[\{i, j\}, \\ \{i, -n, n\}, \{j, -n, n\}], 1], MemberQ[\#, n| -n] \&] \\ \end{cases}
```

■ **Features of the model.** The model is a totalistic 2D cellular automaton, as discussed on page 927. It shows class 2 behavior in which information propagates only over limited distances, so that except when the total size of the system is comparable to the range of the rule, boundary conditions are not crucial.

Similar models have been considered before. In the early 1950s (see below) Alan Turing used a model which effectively differed mainly in having continuous color levels. In 1979 Nicholas Swindale constructed a model with discrete levels to investigate ocular dominance stripes in the brain (see below). And following my work on cellular automata in the early 1980s, David Young in 1984 considered a model even more similar to the one I use here.

There are simple cellular automata—such as 8-neighbor outer totalistic code 196623—which eventually yield maze-like patterns even when started from simple initial conditions. The rule on page 336 gives dappled patterns with progressively larger spots.

■ **Reaction-diffusion processes.** The cellular automaton in the main text can be viewed as a discrete idealization of a reaction-diffusion process. The notion that diffusion might be important in embryo development had been suggested in the early 1900s (see page 1004), but it was only in 1952 that Alan Turing showed how it could lead to the formation of definite patterns. Diffusion of a single chemical always tends to smooth out distributions of concentration. But Turing pointed out that with two chemicals in which each can be produced from the other it is possible for separated regions to develop. If  $c = \{u[t, x], v[t, x]\}$  is a vector of chemical concentrations, then for suitable values of parameters even the standard linear diffusion equation  $\partial_t c = d \cdot \partial_{xx} c + m \cdot c$ 

can exhibit an instability which causes disturbances with certain spatial wavelengths to grow (compare page 988). In his 1952 paper Turing used a finite difference approximation to a pair of diffusion equations to show that starting from a random distribution of concentration values dappled regions could develop in which one or the other chemical was dominant. With purely linear equations, any instability will always eventually lead to infinite concentrations, but Turing noted that this could be avoided by using realistic nonlinear chemical rate equations. In the couple of years before his death in 1954, Turing appears to have tried to simulate such nonlinear equations on an early digital computer, but my cursory efforts to understand his programs-written as they are in a 32-character machine code—were not successful.

Following Turing's work, the fact that simple reactiondiffusion equations can yield spatially inhomogeneous patterns has been rediscovered-with varying degrees of independence—many times. In the early 1970s Ilya Prigogine termed the patterns dissipative structures. And in the mid-1970s, Hermann Haken considered the phenomenon a cornerstone of what he called synergetics.

Many detailed mathematical analyses of linear reactiondiffusion equations have been done since the 1970s; numerical solutions to linear and occasionally nonlinear such equations have also often been found, and in recent years explicit pictures of patterns-rather than just curves of related functions-have commonly been generated. In the context of biological pigmentation patterns detailed studies have been done particularly by Hans Meinhardt and James Murray.

- Scales of patterns. The visual appearance of a pattern on an actual animal depends greatly on the scale of the pattern relative to the whole animal. Pandas and anteaters, for example, typically have just a few regions of different color, while other animals can have hundreds of regions. Studies based on linear reaction-diffusion equations sometimes assume that patterns correspond to stationary modes of the equations, which inevitably depend greatly on boundary conditions. But in more realistic models patterns emerge from long time behavior with generic initial conditions, making boundary conditions—and effects such as changes in them associated with growth of an embryo-much less important.
- Excitable media. In many physical situations effects become decreasingly important as they propagate further away. But in active or excitable media such as heart, muscle and nerve tissue an effect can maintain its magnitude as it propagates, leading to the formation of a variety of spatial structures. An

early model of such media was constructed in 1946 by Norbert Wiener and Arturo Rosenblueth, based on a discrete array of continuous elements. Models with discrete elements were already considered in the 1960s, and in 1977 James Greenberg and Stuart Hastings introduced a simple 2D cellular automaton with three colors. The pictures below show what is probably the most complex feature of this cellular automaton and related systems: the formation of spiral waves. Such spiral waves were studied in 2D and 3D in the 1970s and 1980s, particularly by Arthur Winfree and others; they are fairly easy to observe in both inorganic chemical reactions (see below) and slime mold colonies.

![](Images/_page_1028_Picture_8.jpeg)

- Examples in chemistry. Overall concentrations in chemical reactions can be described by nonlinear ordinary differential equations. Reactions with oscillatory behavior were predicted by Alfred Lotka in 1910 and observed experimentally by William Bray in 1917, but for some reason they were not further investigated at that time. An example was found experimentally by Boris Belousov in 1951 and extensive investigations of it were begun by Anatol Zhabotinsky around 1960. In the early 1970s spiral waves were seen in the spatial distribution of concentrations in this reaction, and by the end of the 1970s images of such waves were commonly used as icons of the somewhat ill-defined notion of self-organization.
- Maze-like patterns. Maze-like patterns occur in several quite different kinds of systems. Cases in which the underlying mechanism is probably similar to that discussed in the main text include brain coral, large-scale vegetation bands seen in tropical areas, patterns of sand dunes, patterns in pre-turbulent fluid convection, and ocular dominance stripes consisting of regions of brain tissue that get marked when different dye is introduced into nerves from left and right eyes. Cases in which the underlying mechanism is probably more associated with folding of fixed amounts of material include human fingerprint patterns and patterns in ferrofluids consisting of suspensions of magnetic particles.
- **Origins of randomness.** The model in the main text assumes that randomness enters through initial conditions. If the two parts of a single animal—say opposite wings on a butterfly—

form together, then these initial conditions can be expected to be the same. But usually even the two sides of a single animal are never physically together, and they normally end up having quite uncorrelated random features. In cases such as fingerprints and zebra stripes there is some correlation between different sides, suggesting an intrinsic component to the randomness that occurs. (The fingerprints of identical twins are typically similar but not identical; iris patterns are quite different.) Note that at least sometimes random initial patterns are formed by cells that have the same type, but different lineages—as in cells expressing genes from the two different X chromosomes in a female animal such as a typical tortoiseshell cat. (In general, quite a few traits—particularly related to aging—can show significant variation in strains of organisms that are genetically identical.)

#### **Financial Systems**

- Laws of human behavior. Over the past century there have been a fair number of quantitative laws proposed for features of human behavior. Some are presumably a direct reflection of human biological construction. Thus for example, Weber's law that the perceived strength of a stimulus tends to vary logarithmically with its actual strength seems likely to be related to the electrochemistry of nerve cells. Of laws for more complicated cognitive or social phenomena the vast majority are statistical in nature. And of those that withstand scrutiny, most in my experience turn out to be transformed versions of statements that some quantity or another can be approximated by perfect randomness. Gaussian distributions typically arise when measurements involve sums of random quantities; other common distributions are obtained from products or other simple combinations of random quantities, or from the results of simple processes based on random quantities. Exponential distributions (as seen, for example, in learning curves) and power-law distributions (as in Zipf's law below) are both, for example, very easy to obtain. (Note that particularly in economics there are also various laws derived from calculus and game theory that are viewed as being quite successful, and are not fundamentally statistical.)
- **Zipf's law.** To a fairly good approximation the *n*<sup>th</sup> most common word in a large sample of English text occurs with frequency 1/n, as illustrated in the first picture below. This fact was first noticed around the end of the 1800s, and was attributed in 1949 by George Zipf to a general, though vague, Principle of Least Effort for human behavior. I suspect that in fact the law has a rather simple probabilistic origin. Consider generating a long piece of text by picking at random from *k* letters and a space. Now collect and rank all the "words"

delimited by spaces that are formed. When k = 1, the  $n^{\text{th}}$  most common word will have frequency  $c^{-n}$ . But when  $k \ge 2$ , it turns out that the  $n^{\text{th}}$  most common word will have a frequency that approximates c/n. If all k letters have equal probabilities, there will be many words with equal frequency, so the distribution will contain steps, as in the second picture below. If the k letters have non-commensurate probabilities, then a smooth distribution is obtained, as in the third picture. If all letter probabilities are equal, then words will simply be ranked by length, with all  $k^m$  words of length m occurring with frequency  $p^m$ . The normalization of probabilities then implies p = 1/(2k), and since the word at rank roughly  $k^m$  then has probability  $1/(2k)^m$ , Zipf's law follows.

![](Images/_page_1029_Figure_6.jpeg)

![](Images/_page_1029_Figure_7.jpeg)

![](Images/_page_1029_Figure_8.jpeg)

- Motion of people and cars. To a first approximation crowds of people seem to show aggregate fluid-like behavior similar to what is seen in gases. Fronts of people—as occur in riots or infantry battles—seem to show instabilities perhaps analogous to those in fluids. Road traffic that is constrained to travel along a line exhibits stop-start instabilities when its overall rate is reduced, say by an obstruction. This appears to be a consequence of the delay before one driver responds to changes in speed of cars in front of them. Fairly accurate cellular automaton models of this phenomenon were developed in the early 1990s.
- Growth of cities. In the absence of geographical constraints, such as terrain or oceans, cities typically have patchy, irregular, shapes. At first an aggregation system (see page 331) might seem to be an obvious model for their growth: each new development gets added to the exterior of the city at a random position. But actual cities look much more irregular. Most likely the reason is that embedded within the cities is a network of transportation routes, and these tend to have a tree- or vein-like structure (though not necessarily with a single center)—with major freeways etc. as trunks. The result of following this structure is to produce a much more irregular boundary.
- Randomness in markets. After the somewhat tricky process of correcting for overall trends, empirical price data from a wide range of markets seem to a first approximation to follow random walks and thus to exhibit Gaussian fluctuations, as noted by Louis Bachelier in 1900. However, particularly on timescales less than a day, it has in the past decade become clear that, as suggested by Benoit Mandelbrot in the early 1960s, large price fluctuations are significantly more common than a Gaussian distribution would imply.

Such an effect is easy to model with the approach used in the main text if different entities interact in clumps or herdswhich can be forced if they are connected in a hierarchical network rather than just a line.

The observed standard deviation of a price—or essentially so-called volatility or beta—can be considered as a measure of the risk of fluctuations in that price. The Capital Asset Pricing Model proposed in the early 1960s suggested that average rates of price increases should be proportional to such variances. And the Black-Scholes model from 1973 implies that prices of suitably constructed options should depend in a sense only on such variances. Over the past decade various corrections to this model have been developed based on non-Gaussian distributions of prices.

- Speculative markets. Cases of markets that seem to operate almost completely independent of objective value have occurred many times in economic history, particularly in connection with innovations in technology or finance. Examples range from tulip bulbs in the mid-1630s to railroads in the mid-1800s to internet businesses in the late 1990s. (Note however that in any particular case it can be claimed that certain speculation was rational, even if it did not work out-but usually it is difficult to get convincing evidence for this, and often effects are obscured by generalized money supply or bankruptcy issues.)
- Properties of markets. Issues of how averaging is done and how irrelevant trends are removed turn out to make unequivocal tests of almost any quantitative hypothesis about prices essentially impossible. The rational expectations theory that prices reflect discounted future earnings has for example been subjected to many empirical tests, but has never been convincingly proved or disproved.
- Efficient markets. In its strong form the so-called Efficient Market Hypothesis states that prices immediately adjust to reflect all possible information, so that knowing a particular piece of information can never be used to make a profit. It is now widely recognized-even in academia-that this hypothesis is a fairly poor representation of reality.
- Details of trading. Cynics might suggest that much of the randomness in practical markets is associated with details of trading. For much of the money actually made from markets on an ongoing basis comes from commissions on trades. And if prices quickly settled down to their final values, fewer

trades would tend to be made. (Different entities would nevertheless still often need liquidity at different times.)

■ Models of markets. When serious economic theory began in the 1700s arguments tended to be based purely on common sense. But with the work of Léon Walras in the 1870s mathematical models began to become popular. In the early 1900s, common sense again for a while became dominant. But particularly with the development of game theory in the 1940s the notion became established, at least in theoretical economics, that prices represent equilibrium points whose properties can be derived mathematically from requirements of optimality. In practical trading, partly as an outgrowth of theories of business cycles, there had emerged all sorts of elaborate so-called technical analysis in which patterns of price movements were supposed-often on the basis of almost mystical theories—to be indicators of future behavior. In the late 1970s, particularly after the work of Fischer Black and Myron Scholes on options pricing, new models of markets based on methods from statistical physics began to be used, but in these models randomness was taken purely as an assumption. In another direction, it was noticed that dynamic versions of game theory could yield iterated maps and ordinary differential equations which would lead to chaotic behavior in prices, but connections with randomness in actual markets were not established. By the mid-1980s, however, it began to be clear that the whole game-theoretical idea of thinking of markets as collections of rational entities that optimize their positions on the basis of complete information was quite inadequate. Some attempts were made to extend traditional mathematical models, and various highly theoretical analyses were done based on treating entities in the market as universal computers. But by the end of the 1980s, the idea had emerged of doing explicit computer simulations with entities in the market represented by practical programs. (See also page 1105.) Often these programs used fairly sophisticated algorithms intended to mimic human traders, but in competitions between programs simpler algorithms have never seemed to be at much of a disadvantage. The model in the main text is in a sense an ultimate idealization along these lines. It follows a sequence of efforts that I have made since the mid-1980s-though have never considered very satisfactory—to find minimal but accurate models of financial processes.

#### **Fundamental Physics**

#### The Notion of Reversibility

■ Page  $437 \cdot \text{Testing for reversibility.}$  To show that a cellular automaton is reversible it is sufficient to check that all configurations consisting of repetitions of different blocks have different successors. This can be done for blocks up to length n in a 1D cellular automaton with k colors using

ReversibleQ[rule\_, k\_, n\_] := Catch[Do[ If[Length[Union[Table[CAStep[rule, IntegerDigits[i, k, m]], {i, 0,  $k^m - 1$ }]]]  $\neq k^m$ , Throw[False]], {m, n}]; True]

For k = 2, r = 1 it turns out that it suffices to test only up to n = 4 (128 out of the 256 rules fail at n = 1, 64 at n = 2, 44 at n = 3 and 14 at n = 4); for k = 2, r = 2 it suffices to test up to n = 15, and for k = 3, r = 1, up to n = 9. But although these results suggest that in general it should suffice to test only up to  $n = k^{2r}$ , all that has so far been rigorously proved is that  $n = k^{2r}$  ( $k^{2r} - 1$ ) + 2r + 1 (or n = 15 for k = 2, r = 1) is sufficient.

For 2D cellular automata an analogous procedure can in principle be used, though there is no upper limit on the size of blocks that need to be tested, and in fact the question of whether a particular rule is reversible is directly equivalent to the tiling problem discussed on page 213 (compare page 942), and is thus formally undecidable.

- **Numbers of reversible rules.** For k = 2, r = 1, there are 6 reversible rules, as shown on page 436. For k = 2, r = 2 there are 62 reversible rules, in 20 families inequivalent under symmetries, out of a total of  $2^{32}$  or about 4 billion possible rules. For k = 3, r = 1 there are 1800 reversible rules, in 172 families. For k = 4, r = 1, some of the reversible rules can be constructed from the second-order cellular automata below. Note that for any k and r, no non-trivial totalistic rule can ever be reversible.
- **Inverse rules.** Some reversible rules are self-inverse, so that applying the same rule twice yields the identity. Other rules come in distinct pairs. Most often a rule that involves r neighbors has an inverse that also involves at most r neighbors. But for both k = 2, r = 2 and k = 3, r = 1 there turn out to be reversible rules whose inverses involve larger

numbers of neighbors. For any given rule one can define the neighborhood size s to be the largest block of cells that is ever needed to determine the color of a single new cell. In general  $s \le 2r + 1$ , and for a simple identity or shift rule, s = 1. For k = 2, r = 1, it then turns out that all the reversible rules and their inverses have s = 1. For k = 2, r = 2, the reversible rules have values of s from 1 to 5, but their inverses have values  $\overline{s}$  from 1 to 6. There are only 8 rules (the inequivalent ones being 16740555 and 3327051468) where  $\overline{s} > s$ , and in each case  $\overline{s} = 6$  while s = 5. For k = 3, r = 1, there are a total of 936 rules with this property: 576, 216 and 144 with  $\overline{s} = 4$ ,  $\overline{s}$  and  $\overline{s}$ , and in all cases s = 3. Examples with  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ ,  $\overline{s} = 3$ 

![](Images/_page_1032_Picture_10.jpeg)

![](Images/_page_1032_Picture_11.jpeg)

![](Images/_page_1032_Picture_12.jpeg)

![](Images/_page_1032_Picture_13.jpeg)

■ Surjectivity and injectivity. See page 959.

- **Directional reversibility.** Even if successive time steps in the evolution of a cellular automaton do not correspond to an injective map, it is still possible to get an injective map by looking at successive lines at some angle in the spacetime evolution of the system. Examples where this works include the surjective rules 30 and 90.
- Page 437 · Second-order cellular automata. Second-order celementary rules can be implemented using

CA2EvolveList[rule\_List, {a\_List, b\_List}, t\_Integer] := Map[First, NestList[CA2Step[rule, #] &, {a, b}, t]]
CA2Step[rule\_List, {a\_, b\_}}] := {b, Mod[a + rule][

$$\begin{split} &CA2Step[rule\_List, \{a\_, b\_\}] := \{b, Mod[a + rule[[\\ &8 - (RotateLeft[b] + 2 (b + 2 RotateRight[b]))]], 2]\} \end{split}$$

where *rule* is obtained from the rule number using *IntegerDigits[n, 2, 8]*.

The combination Drop[list, -1] + 2 Drop[list, 1] of the result from CA2EvolveList corresponds to evolution according to a first-order k = 4, r = 1 rule.

- History. The concept of getting reversibility in a cellular automaton by having a second-order rule was apparently first suggested by Edward Fredkin around 1970 in the context of 2D systems—on the basis of an analogy with second-order differential equations in physics. Similar ideas had appeared in numerical analysis in the 1960s in connection with so-called symmetric or self-adjoint discrete approximations to differential equations.
- Page 438 · Properties. The pattern from rule 67R with simple initial conditions grows irregularly, at an average rate of about 1 cell every 5 steps. The right-hand side of the pattern from rule 173R consists three triangles that repeat progressively larger at steps of the form  $2(9^s 1)$ . Rule 90R has the property that of the diamond of cells at relative positions  $\{\{-n, 0\}, \{0, -n\}, \{n, 0\}, \{0, n\}\}\}$  it is always true for any n that an even number are black.
- **Page 439 · Properties.** The initial conditions used here have a single black cell on two successive initial steps. For rule 150R, however, there is no black cell on the first initial step. The pattern generated by rule 150R has fractal dimension  $Log[2, 3 + \sqrt{17}] 1$  or about 1.83. In rule 154R, each diagonal stripe is followed by at least one 0; otherwise, the positions of the stripes appear to be quite random, with a density around 0.44.
- Generalized additive rules. Additive cellular automata of the kind discussed on page 952 can be generalized by allowing the new value of each cell to be obtained from combinations of cells on s previous steps. For rule 90 the combination c can be specified as  $\{(1, 0, 1)\}$ , while for rule 150R it can be specified as  $\{(0, 1, 0), (1, 1, 1)\}$ . All generalized additive rules ultimately yield nested patterns. Starting with a list of the initial conditions for s steps, the configurations for the next s steps are given by

Append[Rest[list], Map[Mod[Apply[Plus, Flatten[c #]], 2] &, Transpose[  $Table[RotateLeft[list, \{0, i\}], \{i, -r, r\}], \{3, 2, 1\}]]]$ where r = (Length[First[c]] - 1)/2.

Just as for ordinary additive rules on page 1091, an algebraic analysis for generalized additive rules can be given. The objects that appear are solutions to linear recurrences of order s, and in general involve  $s^{th}$  roots. For rule 150R, the configuration at step t as shown in the picture on page 439 is given by  $(u^t - v^t)/Sqrt[4 + h^2]$ , where  $\{u, v\} = z / . Solve[z^2 = hz + 1]$  and h = 1/x + 1 + x. (See also page 1078.)

- Page 440 · Rule 37R. Complicated structures are fairly easy to get with this rule. The initial condition {1, 0, 1} with all cells 0 on the previous step yields a structure that repeats but only every 666 steps. The initial condition {{0, 1, 1}, {1, 0, 0}} yields a pattern that grows sporadically for 3774 steps, then breaks into two repetitive structures. The typical background repeats every 3 steps.
- Classification of reversible rules. In a reversible system it is possible with suitable initial conditions to get absolutely any arrangement of cells to appear at any step. Despite this, however, the overall spacetime pattern of cells is not arbitrary, but is instead determined by the underlying rules. If one starts with completely random initial conditions then class 2 and class 3 behavior are often seen. Class 1 behavior can never occur in a reversible system. Class 4 behavior can occur, as in rule 37R, but is typically obvious only if one starts say with a low density of black cells.

For arbitrary rules, difference patterns of the kind shown on page 250 can get both larger and smaller. In a reversible rule, such patterns can grow and shrink, but can never die out completely.

- Emergence of reversibility. Once on an attractor, any system—even if it does not have reversible underlying rules—must in some sense show approximate reversibility. (Compare page 959.)
- Other reversible systems. Reversible examples can be found of essentially all the types of systems discussed in this book. Reversible mobile automata can for instance be constructed using

Table[(IntegerDigits[i, 2, 3]  $\rightarrow$  If[First[#] == 0, {#, -1}, {Reverse[#], 1}] &)[IntegerDigits[perm[ii], 2, 3]], {i, 8}] where perm is an element of Permutations[Range[8]]. An example that exhibits complex behavior is:

![](Images/_page_1033_Picture_14.jpeg)

Systems based on numbers are typically reversible whenever the mathematical operations they involve are invertible. Thus, for example, the system on page 121 based on successive multiplication by 3/2 is reversible by using division by 3/2. Page 905 gives another example of a reversible system based on numbers.

Multiway systems are reversible whenever both  $a \rightarrow b$  and  $b \rightarrow a$  are present as rules, so that the system corresponds mathematically to a semigroup. (See page 938.)

■ Reversible computation. Typical practical computers—and computer languages—are not even close to reversible: many inputs can lead to the same output, and there is no unique

way to undo the steps of a computation. But despite early confusion (see page 1020), it has been known since at least the 1970s that there is nothing in principle which prevents computation from being reversible. And indeed-just like with the cellular automata in this section-most of the systems in Chapter 11 that exhibit universal computation can readily be made reversible with only slight overhead.

#### Irreversibility and the Second Law of Thermodynamics

■ Time reversal invariance. The reversibility of the laws of physics implies that given the state of a physical system at a particular time, it is always possibly to work out uniquely both its future and its past. Time reversal invariance would further imply that the rules for going in each direction should be identical. To a very good approximation this appears to be true, but it turns out that in certain esoteric particle physics processes small deviations have been found. In particular, it was discovered in 1964 that the decay of the K<sup>0</sup> particle violated time reversal invariance at the level of about one part in a thousand. In current theories, this effect is not attributed any particularly fundamental origin, and is just assumed to be associated with the arbitrary setting of certain parameters. K<sup>0</sup> decay was for a long time the only example of time reversal violation that had explicitly been seen, although recently examples in B particle decays have probably also been seen. It also turns out that the only current viable theories of the apparent preponderance of matter over antimatter in the universe are based on the idea that a small amount of time reversal violation occurred in the decays of certain very massive particles in the very early universe.

The basic formalism used for particle physics assumes not only reversibility, but also so-called CPT invariance. This means that same rules should apply if one not only reverses the direction of time (T), but also simultaneously inverts all spatial coordinates (P) and conjugates all charges (C), replacing particles by antiparticles. In a certain mathematical sense, CPT invariance can be viewed as a generalization of relativistic invariance: with a speed faster than light, something close to an ordinary relativistic transformation is a CPT transformation.

Originally it was assumed that C, P and T would all separately be invariances, as they are in classical mechanics. But in 1957 it was discovered that in radioactive beta decay, C and P are in a sense each maximally violated: among other things, the correlation between spin and motion direction is exactly opposite for neutrinos and for antineutrinos that are emitted. Despite this, it was still assumed that CP and T would be true invariances. But in 1964 these too were found to be violated. Starting with a pure beam of K<sup>0</sup> particles, it turns out that quantum mechanical mixing processes lead after about 10<sup>-8</sup> seconds to a certain mixture of K<sup>0</sup> particles the antiparticles of the K<sup>0</sup>. And what effectively happens is that the amount of mixing differs by about 0.1% in the positive and negative time directions. (What is actually observed is a small probability for the long-lived component of a K<sup>0</sup> beam to decay into two rather than three pions. Some analysis is required to connect this with T violation.) Particle physics experiments so far support exact CPT invariance. Simple models of gravity potentially suggest CPT violation (as a consequence of deviations from pure special relativistic invariance), but such effects tend to disappear when the models are refined.

■ History of thermodynamics. Basic physical notions of heat and temperature were established in the 1600s, and scientists of the time appear to have thought correctly that heat is associated with the motion of microscopic constituents of matter. But in the 1700s it became widely believed that heat was instead a separate fluid-like substance. Experiments by James Joule and others in the 1840s put this in doubt, and finally in the 1850s it became accepted that heat is in fact a form of energy. The relation between heat and energy was important for the development of steam engines, and in 1824 Sadi Carnot had captured some of the ideas of thermodynamics in his discussion of the efficiency of an idealized engine. Around 1850 Rudolf Clausius and William Thomson (Kelvin) stated both the First Law-that total energy is conserved—and the Second Law Thermodynamics. The Second Law was originally formulated in terms of the fact that heat does not spontaneously flow from a colder body to a hotter. Other formulations followed quickly, and Kelvin in particular understood some of the law's general implications. The idea that gases consist of molecules in motion had been discussed in some detail by Daniel Bernoulli in 1738, but had fallen out of favor, and was revived by Clausius in 1857. Following this, James Clerk Maxwell in 1860 derived from the mechanics of individual molecular collisions the expected distribution of molecular speeds in a gas. Over the next several years the kinetic theory of gases developed rapidly, and many macroscopic properties of gases in equilibrium were computed. In 1872 Ludwig Boltzmann constructed an equation that he thought could describe the detailed time development of a gas, whether in equilibrium or not. In the 1860s Clausius had introduced entropy as a ratio of heat to temperature, and had stated the Second Law in terms of the increase of this quantity. Boltzmann then showed that his

equation implied the so-called H Theorem, which states that a quantity equal to entropy in equilibrium must always increase with time. At first, it seemed that Boltzmann had successfully proved the Second Law. But then it was noticed that since molecular collisions were assumed reversible, his derivation could be run in reverse, and would then imply the opposite of the Second Law. Much later it was realized that Boltzmann's original equation implicitly assumed that molecules are uncorrelated before each collision, but not afterwards, thereby introducing a fundamental asymmetry in time. Early in the 1870s Maxwell and Kelvin appear to have already understood that the Second Law could not formally be derived from microscopic physics, but must somehow be a consequence of human inability to track large numbers of molecules. In responding to objections concerning reversibility Boltzmann realized around 1876 that in a gas there are many more states that seem random than seem orderly. This realization led him to argue that entropy must be proportional to the logarithm of the number of possible states of a system, and to formulate ideas about ergodicity. The statistical mechanics of systems of particles was put in a more general context by Willard Gibbs, beginning around 1900. Gibbs introduced the notion of an ensemble-a collection of many possible states of a system, each assigned a certain probability. He argued that if the time evolution of a single state were to visit all other states in the ensemble-the so-called ergodic hypothesis-then averaged over a sufficiently long time a single state would behave in a way that was typical of the ensemble. Gibbs also gave qualitative arguments that entropy would increase if it were measured in a "coarse-grained" way in which nearby states were not distinguished. In the early 1900s the development of thermodynamics was largely overshadowed by quantum theory and little fundamental work was done on it. Nevertheless, by the 1930s, the Second Law had somehow come to be generally regarded as a principle of physics whose foundations should be questioned only as a curiosity. Despite neglect in physics, however, ergodic theory became an active area of pure mathematics, and from the 1920s to the 1960s properties related to ergodicity were established for many kinds of simple systems. When electronic computers became available in the 1950s, Enrico Fermi and others began to investigate the ergodic properties of nonlinear systems of springs. But they ended up concentrating on recurrence phenomena related to solitons, and not looking at general questions related to the Second Law. Much the same happened in the 1960s, when the first simulations of hard sphere gases were led to concentrate on the specific phenomenon of long-time tails. And by the 1970s, computer experiments were mostly oriented towards ordinary

differential equations and strange attractors, rather than towards systems with large numbers of components, to which the Second Law might apply. Starting in the 1950s, it was recognized that entropy is simply the negative of the information quantity introduced in the 1940s by Claude Shannon. Following statements by John von Neumann, it was thought that any computational process must necessarily increase entropy, but by the early 1970s, notably with work by Charles Bennett, it became accepted that this is not so (see page 1018), laying some early groundwork for relating computational and thermodynamic ideas.

■ Current thinking on the Second Law. The vast majority of current physics textbooks imply that the Second Law is well established, though with surprising regularity they say that detailed arguments for it are beyond their scope. More specialized articles tend to admit that the origins of the Second Law remain mysterious. Most ultimately attribute its validity to unknown constraints on initial conditions or measurements, though some appeal to external perturbations, to cosmology or to unknown features of quantum mechanics.

An argument for the Second Law from around 1900, still reproduced in many textbooks, is that if a system is ergodic then it will visit all its possible states, and the vast majority of these will look random. But only very special kinds of systems are in fact ergodic, and even in such systems, the time necessary to visit a significant fraction of all possible states is astronomically long. Another argument for the Second Law, arising from work in the 1930s and 1940s, particularly on systems of hard spheres, is based on the notion of instability with respect to small changes in initial conditions. The argument suffers however from the same difficulties as the ones for chaos theory discussed in Chapter 6 and does not in the end explain in any real way the origins of randomness, or the observed validity of the Second Law.

With the Second Law accepted as a general principle, there is confusion about why systems in nature have not all dissipated into complete randomness. And often the rather absurd claim is made that all the order we see in the universe must just be a fluctuation—leaving little explanatory power for principles such as the Second Law.

■ My explanation of the Second Law. What I say in this book is not incompatible with much of what has been said about the Second Law before; it is simply that I make more definite some key points that have been left vague before. In particular, I use notions of computation to specify what kinds of initial conditions can reasonably be prepared, and what kinds of measurements can reasonably be made. In a sense what I do is just to require that the operation of coarse graining correspond to a computation that is less sophisticated than the actual evolution of the system being studied. (See also Chapters 10 and 12.)

- Biological systems and Maxwell's demon. Unlike physical systems, biological systems typically seem capable of spontaneously organizing themselves. And as a result, even the original statements of the Second Law talked only about "inanimate systems". In the mid-1860s James Clerk Maxwell then suggested that a demon operating at a microscopic level could reduce the randomness of a system such as a gas by intelligently controlling the motion of molecules. For many years there was considerable confusion about Maxwell's demon. There were arguments that the demon must use a flashlight that generates entropy. And there were extensive demonstrations that actual biological systems reduce their internal entropy only at the cost of increases in the entropy of their environment. But in fact the main point is that if the evolution of the whole system is to be reversible, then the demon must store enough information to reverse its own actions, and this limits how much the demon can do, preventing it, for example, from unscrambling a large system of gas molecules.
- Self-gravitating systems. The observed existence of structures such as galaxies might lead one to think that any large number of objects subject to mutual gravitational attraction might not follow the Second Law and become randomized, but might instead always form orderly clumps. It is difficult to know, however, what an idealized selfgravitating system would do. For in practice, issues such as the limited size of a galaxy, its overall rotation, and the details of stellar collisions all seem to have major effects on the results obtained. (And it is presumably not feasible to do a small-scale experiment, say in Earth orbit.) There are known to be various instabilities that lead in the direction of clumping and core collapse, but how these weigh against effects such as the transfer of energy into tight binding of small groups of stars is not clear. Small galaxies such as globular clusters that contain less than a million stars seem to exhibit a certain uniformity which suggests a kind of equilibrium. Larger galaxies such as our own that contain perhaps 100 billion stars often have intricate spiral or other structure, whose origin may be associated with gravitational effects, or may be a consequence of detailed processes of star formation and explosion. (There is some evidence that older galaxies of a given size tend to develop more regularities in their structure.) Current theories of the early universe tend to assume that galaxies originally began to form as a result of density fluctuations of non-gravitational origin (and reflected

in the cosmic microwave background). But there is evidence that a widespread fractal structure develops-with a correlation function of the form  $r^{-1.8}$ —in the distribution of stars in our galaxy, galaxies in clusters and clusters in superclusters, perhaps suggesting the existence of general overall laws for self-gravitating systems. (See also page 973.)

As mentioned on page 880, it so happens that my original interest in cellular automata around 1981 developed in part from trying to model the growth of structure in selfgravitating systems. At first I attempted to merge and generalize ideas from traditional areas of mathematical physics, such as kinetic theory, statistical mechanics and field theory. But then, particularly as I began to think about doing explicit computer simulations, I decided to take a different tack and instead to look for the most idealized possible models. And in doing this I quickly came up with cellular automata. But when I started to investigate cellular automata, I discovered some very remarkable phenomena, and I was soon led away from self-gravitating systems, and into the process of developing the much more general science in this book. Over the years, I have occasionally come back to the problem of self-gravitating systems, but I have never succeeded in developing what I consider to be a satisfactory approach to them.

- Cosmology and the Second Law. In the standard big bang model it is assumed that all matter in the universe was initially in completely random thermal equilibrium. But such equilibrium implies uniformity, and from this it follows that the initial conditions for the gravitational forces in the universe must have been highly regular, resulting in simple overall expansion, rather than random expansion in some places and contraction in others. As I discuss on page 1026 I suspect that in fact the universe as a whole probably had what were ultimately very simple initial conditions, and it is just that the effective rules for the evolution of matter led to rapid randomization, whereas those for gravity did not.
- Alignment of time in the universe. Evidence astronomy clearly suggests that the direction of irreversible processes is the same throughout the universe. The reason for this is presumably that all parts of the universe are expanding—with the local consequence that radiation is more often emitted than absorbed, as evidenced by the fact that the night sky is dark. Olbers' paradox asks why one does not see a bright star in every direction in the night sky. The answer is that locally stars are clumped, and light from stars further away is progressively red-shifted to lower energy. Focusing a larger and larger distance away, the light one sees was emitted longer and longer ago. And eventually one sees light emitted when the universe was filled with hot opaque

gas—now red-shifted to become the 2.7K cosmic microwave background.

- Poincaré recurrence. Systems of limited size that contain only discrete elements inevitably repeat their evolution after a sufficiently long time (see page 258). In 1890 Henri Poincaré established the somewhat less obvious fact that even continuous systems also always eventually get at least arbitrarily close to repeating themselves. This discovery led to some confusion in early interpretations of the Second Law, but the huge length of time involved in a Poincaré recurrence makes it completely irrelevant in practice.
- Page 446 · Billiards. The discrete system I consider here is analogous to continuous so-called billiard systems consisting of circular balls in the plane. The simplest case involves one ball bouncing around in a region of a definite shape. In a rectangular region, the position is given by Mod[at, {w, h}] and every point will be visited if the parameters have irrational ratios. In a region that contains fixed circular obstructions, the motion can become sensitively dependent on initial conditions. (This setup is similar to a so-called Lorentz gas.) For a system of balls in a region with cyclic boundaries, a complicated proof due to Yakov Sinai from the 1960s purports to show that every ball eventually visits every point in the region, and that certain simple statistical properties of trajectories are consistent with randomness. (See also page 971.)
- Page 449 · Entropy of particles in a box. The number of possible states of a region of m cells containing q particles is Binomial[m, q]. In the large size limit, the logarithm of this can be approximated by qLog[m/q]/m.
- **Page 457** · **Periods in rule 37R.** With a system of size n, the maximum possible repetition period is  $2^{2n}$ . In actuality, however, the periods are considerably shorter. With all cells 0 on one step, and a block of nonzero cells on the next step, the periods are for example:  $\{1\}$ : 21;  $\{1, 1\}$ : 3n-8;  $\{1, 0, 1\}$ : 666;  $\{1, 1, 1\}$ : 3n-8;  $\{1, 0, 0, 1\}$ : irregular (<24n; peaks at 6j+1);  $\{1, 0, 0, 1, 0, 1\}$ : irregular ( $<2^n$ ; 857727 for n=26; 13705406 for n=100). With completely random initial conditions, there are great fluctuations, but a typical period is around  $2^{n/3}$ .

#### **Conserved Quantities and Continuum Phenomena**

■ **Physics.** The quantities in physics that so far seem to be exactly conserved are: energy, momentum, angular momentum, electric charge, color charge, lepton number (as well as electron number, muon number and  $\tau$  lepton number) and baryon number.

■ **Implementation.** Whether a k-color cellular automaton with range r conserves total cell value can be determined from

Catch[Do[

(If[Apply[Plus, CAStep[rule, #] + #] + 0, Throw[False]] &)[ IntegerDigits[i, k, m]], {m, w}, {i, 0, k<sup>m</sup> - 1}]; True]

where w can be taken to be  $k^{2r}$ , and perhaps smaller. Among the 256 elementary cellular automata just 5 conserve total cell value. Among the  $2^{32}$  k = 2, r = 2 rules 428 do, and of these 2 are symmetric, and 6 are reversible, and all these are just shift and identity rules.

■ More general conserved quantities. Some rules conserve not total numbers of cells with given colors, but rather total numbers of blocks of cells with given forms—or combinations of these. The pictures below show the simplest quantities of these kinds that end up being conserved by various elementary rules.

![](Images/_page_1037_Picture_13.jpeg)

Among the 256 elementary rules, the total numbers that have conserved quantities involving at most blocks of lengths 1 through 10 are (5, 38, 66, 88, 102, 108, 108, 114, 118, 118).

Rules that show complicated behavior usually do not seem to have conserved quantities, and this is true for example of rules 30, 90 and 110, at least up to blocks of length 10.

One can count the number of occurrences of each of the  $k^b$  possible blocks of length b in a given state using

BC[list\_] :=

 $With[{z = Map[FromDigits[\#, k] \&, Partition[list, b, 1, 1]]}, \\ Map[Count[z, \#] \&, Range[0, k^b - 1]]]$ 

Conserved quantities of the kind discussed here are then of the form q . BC[a] where q is some fixed list. A way to find candidates for q is to compute

$$\label{local_norm} \begin{split} & NullSpace[Table[With]\{u = Table[Random[Integer,\\ \{0, k-1\}], \{m\}]\}, BC[CAStep[u]] - BC[u]], \{s\}]] \end{split}$$

for progressively larger m and s, and to see what lists continue to appear. For block size b,  $k^{b-1}$  lists will always appear as a result of trivial conserved quantities. (With k=2, for b=1,  $\{1,1\}$  represents conservation of the total number of cells, regardless of color, while for b=2,  $\{1,1,1,1\}$  represents the same thing, while  $\{0,1,-1,0\}$  represents the fact that in going along in any state the number of black-to-white transitions must equal the number of white-to-black ones.) If more than  $k^{b-1}$  lists appear, however, then some must correspond to genuine non-trivial conserved quantities. To identify any such quantity with certainty, it turns out to be enough to look at the  $k^{b+2}$  states where no block of length

b+2r-1 appears more than once (and perhaps even just some fairly small subset of these).

(See also page 981.)

- Other conserved quantities. The conserved quantities discussed so far can all be thought of as taking values assigned to blocks of different kinds in a given state and then just adding them up as ordinary numbers. But one can also imagine using other operations to combine such values. Addition modulo n can be handled by inserting  $Modulus \rightarrow n$ in NullSpace in the previous note. And doing this shows for example that rule 150 conserves the total number of black cells modulo 2. But in general not many additional conserved quantities are found in this way. One can also consider combining values of blocks by the multiplication operation in a group-and seeing whether the conjugacy class of the result is conserved.
- PDEs. In the early 1960s it was discovered that certain nonlinear PDEs support an infinite number of distinct conserved quantities, associated with so-called integrability and the presence of solitons. Systematic methods now exist to find conserved quantities that are given by integrals of polynomials of any given degree in the dependent variables and their derivatives. Most randomly chosen PDEs appear, however, to have no such conserved quantities.
- Local conservation laws. Whenever a system like a cellular automaton (or PDE) has a global conserved quantity there must always be a local conservation law which expresses the fact that every point in the system the total flux of the conserved quantity into a particular region must equal the rate of increase of the quantity inside it. (If the conserved quantity is thought of like charge, the flux is then current.) In any 1D k = 2, r = 1 cellular automaton, it follows from the basic structure of the rule that one can tell what the difference in values of a particular cell on two successive steps will be just by looking at the cell and its immediate neighbor on each side. But if the number of black cells is conserved, then one can compute this difference instead by defining a suitable flux, and subtracting its values on the left and right of the cell. What the flux should be depends on the rule. For rule 184, it can be taken to be 1 for each ■ block, and to be 0 otherwise. For rule 170, it is 1 for both 

  and ■. For rule 150, it is 1 for  $\square$  and  $\blacksquare$ , with all computations done modulo 2. In general, if the global conserved quantity involves blocks of size b, the flux can be computed by looking at blocks of size b + 2r - 1. What the values for these blocks should be can be found by solving a system of linear equations; that a solution must exist can be seen by looking at the de Bruijn network (see page 941), with nodes labelled by size b + 2r - 1 blocks,

and connections by value differences between size b blocks at the center of the possible size b + 2r blocks. (Note that the same basic kind of setup works in any number of dimensions.)

■ Block cellular automata. With a rule of the form  $\{\{1, 1\} \rightarrow \{1, 1\}, \{1, 0\} \rightarrow \{1, 0\}, \{0, 1\} \rightarrow \{0, 0\}, \{0, 0\} \rightarrow \{0, 1\}\}$  the evolution of a block cellular automaton with blocks of size *n* can be implemented using

```
BCAEvolveList[{n_Integer, rule_}, init_, t_] :=
  FoldList[BCAStep[{n, rule}, #1, #2] &, init, Range[t]] /;
    Mod[Length[init], n] == 0
```

BCAStep[{n . rule }, a . d ] := RotateRight[ Flatten[Partition[RotateLeft[a, d], n] /. rule], d]

Starting with a single black cell, none of the k = 2, n = 2 block cellular automata generate anything beyond simple nested patterns. In general, there are  $k^{nk^n}$  possible rules for block cellular automata with *k* colors and blocks of size *n*. Of these,  $k^n$ ! are reversible. For k = 2, the number of rules that conserve the total number of black cells can be computed from q = Binomial[n, Range[0, n]] as  $Apply[Times, q^q]$ . The number of these rules that are also reversible is Apply[Times, q!]. In general, a block cellular automaton is reversible only if its rule simply permutes the  $k^n$  possible

Compressing each block into a single cell, and n steps into one, any block cellular automaton with k colors and block size n can be translated directly into an ordinary cellular automaton with  $k^n$  colors and range r = n/2.

■ Page 461 · Block rules. These pictures show the behavior of rule (c) starting from some special initial conditions.

![](Images/_page_1038_Picture_14.jpeg)

![](Images/_page_1038_Picture_15.jpeg)

![](Images/_page_1038_Picture_16.jpeg)

![](Images/_page_1038_Picture_17.jpeg)

![](Images/_page_1038_Picture_18.jpeg)

The repetition period with a total of n cells can be  $3^n$  steps. With random initial conditions, the period is typically up to about  $3^{n/2}$ . Starting with a block of q black cells, the period can get close to this. For n = 20, q = 17, for example, it is 31.300.

Note that even in rule (b) wraparound phenomena can lead to repetition periods that increase rapidly with n (e.g. 4820 for n = 20, q = 15), but presumably not exponentially.

In rule (d), the repetition periods can typically be larger than in rule (c): e.g. 803,780 for n = 20, q = 13.

■ Page 464 · Limiting procedures. Several different limiting procedures all appear to yield the same continuum behavior for the cellular automata shown here. In the pictures on this page a large ensemble of different initial conditions is considered, and the density of each individual cell averaged over this ensemble is computed. In a more direct analogy to actual physical systems, one would consider instead a very large number of cells, then compute the density in a single state of the system by averaging over regions that contain many cells but are nevertheless small compared to the size of the whole system.

- PDE approximations. Cellular automaton (d) in the main text can be viewed as minimal discrete approximations to the diffusion equation. The evolution of densities in the ensemble average is analogous to a traditional finite difference method with a real number at each site. The cellular automaton itself uses in effect a distributed representation of the density.
- **Diffusion equation.** In an appropriate limit the density distribution for cellular automaton (d) appears to satisfy the usual diffusion equation  $\partial_t f[x, t] = c \, \partial_{xx} f[x, t]$  discussed on page 163. The solution to this equation with an impulse initial condition is  $Exp[-x^2/t]$ , and with a block from -a to a it is  $(Erf[(a-x)/\sqrt{t}\ ] + Erf[(a+x)/\sqrt{t}\ ])/a$ .
- **Derivation of the diffusion equation.** With some appropriate assumptions, it is fairly straightforward to derive the usual diffusion equation from a cellular automaton. Let the density of black cells at position x and time t be f[x, t], where this density can conveniently be computed by averaging over many instances of the system. If we assume that the density varies slowly with position and time, then we can make series expansions such as

 $f[x + dx, t] = f[x, t] + \partial_x f[x, t] dx + 1/2 \partial_{xx} f[x, t] dx^2 + ...$  where the coordinates are scaled so that adjacent cells are at positions x - dx, x, x + dx, etc. If we then assume perfect underlying randomness, the density at a particular position must be given in terms of the densities at neighboring positions on the previous step by

 $f[x, t+dt] = p_1 f[x-dx, t] + p_2 f[x, t] + p_3 f[x+dx, t]$ Density conservation implies that  $p_1 + p_2 + p_3 = 1$ , while left-right symmetry implies  $p_1 = p_2$ . And from this it follows that

f[x, t+dt] = c (f[x-dx, t] + f[x+dx, t]) + (1-2c)f[x, t]Performing a series expansion then yields

 $f[x, t] + dt \partial_t f[x, t] = f[x, t] + c dx^2 \partial_{xx} f[x, t]$ 

which in turn gives exactly the usual 1D diffusion equation  $\partial_t f(x, t] = \xi \, \partial_{xx} f(x, t]$ , where  $\xi$  is the diffusion coefficient for the system. I first gave this derivation in 1986, together with extensive generalizations.

■ Page 464 · Non-standard diffusion. To get ordinary diffusion behavior of the kind that occurs in gases—and is described by the diffusion equation—it is in effect necessary to have

perfect uncorrelated randomness, with no structure that persists too long. But for example in the rule (a) picture on page 463 there is in effect a block of solid that persists in the middle—so that no ordinary diffusion behavior is seen. In rule (c) there is considerable apparent randomness, but it turns out that there are also fluctuations that last too long to yield ordinary diffusion. And thus for example whenever there is a structure containing s identical cells (as on page 462), this typically takes about  $s^2$  steps to decay away. The result is that on page 464 the limiting form of the average behavior does not end up being an ordinary Gaussian.

■ Conservation of vector quantities. Conservation of the total number of colored cells is analogous to conservation of a scalar quantity such as energy or particle number. One can also consider conservation of a vector quantity such as momentum which has not only a magnitude but also a direction. Direction makes little sense in 1D, but is meaningful in 2D. The 2D cellular automaton used as a model of an idealized gas on page 446 provides an example of a system that can be viewed as conserving a vector quantity. In the absence of fixed scatterers, the total fluxes of particles in the horizontal and the vertical directions are conserved. But in a sense there is too much conservation in this system, and there is no interaction between horizontal and vertical motions. This can be achieved by having more complicated underlying rules. One possibility is to use a hexagonal rather than square grid, thereby allowing six particle directions rather than four. On such a grid it is possible to randomize microscopic particle motions, but nevertheless conserve overall momenta. This is essentially the model used in my discussion of fluids on page 378.

#### **Ultimate Models for the Universe**

■ History of ultimate models. From the earliest days of Greek science until well into the 1900s, it seems to have often been believed that an ultimate model of the universe was not far away. In antiquity there were vague ideas about everything being made of elements like fire and water. In the 1700s, following the success of Newtonian mechanics, a common assumption seems to have been that everything (with the possible exception of light) must consist of tiny corpuscles with gravity-like forces between them. In the 1800s the notion of fields—and the ether—began to develop, and in the 1880s it was suggested that atoms might be knotted vortices in the ether (see page 1044). When the electron was discovered in 1897 it was briefly thought that it might be the fundamental constituent of everything. And later it was imagined that perhaps electromagnetic fields could underlie

everything. Then after the introduction of general relativity for the gravitational field in 1915, there were efforts, especially in the 1930s, to introduce extensions that would yield unified field theories of everything (see page 1028). By the 1950s, however, an increasing number of subatomic particles were being found, and most efforts at unification became considerably more modest. In the 1960s the quark model began to explain many of the particles that were seen. Then in the 1970s work in quantum field theory encouraged the use of gauge theories and by the late 1970s the so-called Standard Model had emerged, with the Weinberg-Salam SU(2) ⊗ U(1) gauge theory for weak interactions and electromagnetism, and the QCD SU(3) gauge theory for strong interactions. The discoveries of the c quark,  $\tau$  lepton and b quark were largely unexpected, but by the late 1970s there was widespread enthusiasm for the idea of a single "grand unified" gauge theory, based say on SU(5), that would explain all forces except gravity. By the mid-1980s failure to observe expected proton decay cast doubts on simple versions of such models, and various possibilities based on supersymmetry and groups like SO(10) were considered. Occasional attempts to construct quantum theories of gravity had been made since the 1930s, and in the late 1980s these began to be pursued more vigorously. In the mid-1980s the discovery that string theory could be given various mathematical features that were considered desirable made it emerge as the main hope for an ultimate "theory of everything". But despite all sorts of elegant mathematical work, the theory remains rather distant from observed features of our universe. In some parts of particle physics, it is still sometimes claimed that an ultimate theory is not far away, but outside it generally seems to be assumed that physics is somehow instead an endless frontier-that will continue to yield a stream of surprising and increasingly complex discoveries forever-with no ultimate theory ever being found.

- Theological implications. Some may view an ultimate model of the universe as "leaving no room for a god", while others may view it as a direct reflection of the existence of a god. In any case, knowing a complete and ultimate model does make it impossible to have miracles or divine interventions that come from outside the laws of the universe-though working out what will happen on the basis of these laws may nevertheless be irreducibly difficult.
- Origins of physical models. Considering the reputation of physics as an empirical science, it is remarkable how many significant theories were in fact first constructed on largely aesthetic grounds. Notable examples include Maxwell's equations for electromagnetism (1880s), general relativity

(1915), the Dirac equation for relativistic electrons (1928), and QCD (early 1970s). This history makes it seem more plausible that one might be able to come up with an ultimate model of physics on largely aesthetic grounds, rather than mainly by working from detailed experimental observations.

- Simplicity in scientific models. To curtail absurdly complicated early scientific models Occam's razor principle that "entities should not be multiplied beyond necessity" was introduced in the 1300s. This principle has worked well in physics, where it has often proven to be the case, for example, that out of all possible terms in an equation the only ones that actually occur are the very simplest. But in a field like biology, the principle has usually been regarded as much less successful. For many complicated features are seen in biological organisms, and when there have been guesses of simple explanations for them, these have often turned out to be wrong. Much of what is seen is probably a reflection of complicated details of the history of biological evolution. But particularly after the discoveries in this book it seems likely that at least some of what appears complicated may actually be produced by very simple underlying programs—which perhaps occur because they were the first to be tried, or are the most efficient or robust. Outside of natural science, Occam's principle can sometimes be useful—typically because simplicity is a good assumption in some aspect of human behavior or motivation. In looking at well-developed technological systems or human organizations simplicity is also quite often a reasonable assumption-since over the course of time parts that are complicated or difficult to understand will tend to have been optimized away.
- **Numerology.** Ever since the Pythagoreans many attempts to find truly ultimate models of the universe have ended up centering on derivations of numbers that are somehow thought to be characteristic of the universe. In the past century, the emphasis has been on physical constants such as the fine structure constant  $\alpha \simeq 1/137.0359896$ , and usually the idea is that such constants arise directly from counting objects of some specified type using traditional discrete mathematics. A notable effort along these lines was made by Arthur Eddington in the mid-1930s, and certainly over the past twenty or so years I have received a steady stream of mail presenting such notions with varying degrees of obscurity and mysticism. But while I believe that every feature of our universe does indeed come from an ultimate discrete model, I would be very surprised if the values of constants which happen to be easy for us to measure in the end turn out to be given by simple traditional mathematical formulas.
- Emergence of simple laws. In statistical physics it is seen that universal and fairly simple overall laws often emerge

even in systems whose underlying molecular or other structure can be quite complicated. The basic origin of this phenomenon is the averaging effect of randomness discussed in Chapter 7 (technically, it is the survival only of leading operators at renormalization group fixed points). The same phenomenon is also seen in quantum field theory, where it is essentially a consequence of the averaging effect of quantum fluctuations, which have a direct mathematical analog to statistical physics.

- Apparent simplicity. Given any rules it is always possible to develop a form of description in which these rules will be considered simple. But what is interesting to ask is whether the underlying rules of the universe will seem simple-or special, say in their elegance or symmetry-with respect to forms of description that we as humans currently use.
- Mechanistic models. Until quite recently, it was generally assumed that if one were able to get at the microscopic constituents of the universe they would look essentially like small-scale analogs of objects familiar from everyday life. And so, for example, the various models of atoms from the end of the 1800s and beginning of the 1900s were all based on familiar mechanical systems. But with the rise of quantum mechanics it came to be believed throughout mainstream physics that any true fundamental model must be abstract and mathematical-and never ultimately amenable to any kind of direct mechanistic description. Occasionally there have been mechanistic descriptions used—as in the parton and bag models, and various continuum models of highenergy collisions—but they have typically been viewed only as convenient rough approximations. (Feynman diagrams may also seem superficially mechanistic, but are really just representations of quite abstract mathematical formulas.) And indeed since at least the 1960s mechanistic models have tended to carry the stigma of uninformed amateur science.

With the rise of computers there began to be occasional discussion-though largely outside of mainstream sciencethat the universe might have a mechanism related to computers. Since the 1950s science fiction has sometimes featured the idea that the universe or some part of it—such as the Earth-could be an intentionally created computer, or that our perception of the universe could be based on a computer simulation. Starting in the 1950s a few computer scientists considered the idea that the universe might have components like a computer. Konrad Zuse suggested that it could be a continuous cellular automaton; Edward Fredkin an ordinary cellular automaton (compare page 1027). And over the past few decades-normally in the context of amateur science—there have been a steady stream of systems like cellular automata constructed to have elements reminiscent of observed particles or forces. From the point of view of mainstream physics, such models have usually seemed quite naive. And from what I say in the main text, no such literal mechanistic model can ever in the end realistically be expected to work. For if an ultimate model is going to be simple, then in a sense it cannot have room for all sorts of elements that are immediately recognizable in terms of everyday known physics. And instead I believe that what must happen relies on the phenomena discovered in this book—and involves the emergence of complex properties without any obvious underlying mechanistic set up. (Compare page 860.)

- The Anthropic Principle. It is sometimes argued that the reason our universe has the characteristics it does is because otherwise an intelligence such as us could not have arisen to observe it. But to apply such an argument one must among other things assume that we can imagine all the ways in which intelligence could conceivably operate. Yet as we have seen in this book it is possible for highly complex behaviorultimately not dissimilar to intelligence—to arise from simple programs in ways that we never came even close to imagining. And indeed, as we discuss in Chapter 12, it seems likely that above a fairly low threshold the vast majority of underlying rules can in fact in some way or another support arbitrarily complex computations-potentially allowing something one might call intelligence in a vast range of very different universes. (See page 822.)
- Physics versus mathematics. Theoretical physics can be viewed as taking physical input in the form of models and then using mathematics to work out the consequences. If I am correct that there is a simple underlying program for the universe, then this means that theoretical physics must at some level have only a very small amount of true physical input—and the rest must in a sense all just be mathematics.
- Initial conditions. To find the behavior of the universe one potentially needs to know not only its rule but also its initial conditions. Like the rule, I suspect that the initial conditions will turn out to be simple. And ultimately there should be traces of such simplicity in, say, the distribution of galaxies or the cosmic microwave background. But ideas like those on page 1055—as well as inflation—tend to suggest that we currently see only a tiny fraction of the whole universe, making it very difficult for example to recognize overall geometrical regularities. And it could also be that even though there might ultimately have been simple initial conditions, the current phase of our universe might be the result of some sequence of previous phases, and so effectively have much more complicated initial conditions. (Proposals discussed in quantum cosmology since the 1980s

that for example just involve requiring the universe to satisfy final but not initial boundary condition constraints do not fit well into my kinds of models.)

- Consequences of an ultimate model. Even if one knows an ultimate model for the universe, there will inevitably be irreducible difficulty in working out all its consequences. Indeed, questions like "does there exist a way to transmit information faster than light?" may boil down to issues analogous to whether it is possible to construct a configuration that has a certain property in, say, the rule 110 cellular automaton. And while some such questions may be answered by fairly straightforward computational or mathematical means, there will be no upper bound on the amount of effort that it could take to answer any particular question.
- Meaning of the universe. If the whole history of our universe can be obtained by following definite simple rules, then at some level this history has the same kind of character as a construct such as the digit sequence of  $\pi$ . And what this suggests is that it makes no more or less sense to talk about the meaning of phenomena in our universe as it does to talk about the meaning of phenomena in the digit sequence of  $\pi$ .

#### The Nature of Space

• History of discrete space. The idea that matter might be made up of discrete particles existed in antiquity (see page 876), and occasionally the notion was discussed that space might also be discrete—and that this might for example be a way of avoiding issues like Zeno's paradox. In 1644 René Descartes proposed that space might initially consist of an array of identical tiny discrete spheres, with motion then occurring through chains of these spheres going around in vortices-albeit with pieces being abraded off. But with the rise of calculus in the 1700s all serious fundamental models in physics began to assume continuous space. In discussing the notion of curved space, Bernhard Riemann remarked in 1854 that it would be easier to give a general mathematical definition of distance if space were discrete. But since physical theories seemed to require continuous space, the necessary new mathematics was developed and almost universally used-though for example in 1887 William Thomson (Kelvin) did consider a discrete foam-like model for the ether (compare page 988). Starting in 1930, difficulties with infinities in quantum field theory again led to a series of proposals that spacetime might be discrete. And indeed by the late 1930s this notion was fairly widely discussed as a possible inevitable feature of quantum mechanics. But there were problems with relativistic invariance, and after ideas of renormalization developed in the 1940s, discrete space seemed unnecessary, and has been out of favor ever since. Some non-standard versions of quantum field theory involving discrete space did however continue to be investigated into the 1960s, and by then a few isolated other initiatives had arisen that involved discrete space. The idea that space might be defined by some sort of causal network of discrete elementary quantum events arose in various forms in work by Carl von Weizsäcker (urtheory), John Wheeler (pregeometry), David Finkelstein (spacetime code), David Bohm (topochronology) and Roger Penrose (spin networks; see page 1055). General arguments for discrete space were also sometimes made-notably by Edward Fredkin, Marvin Minsky and to some extent Richard Feynman-on the basis of analogies to computers and in particular the idea that a given region of space should contain only a finite amount of information. In the 1980s approximation schemes such as lattice gauge theory and later Regge calculus (see page 1054) that take space to be discrete became popular, and it was occasionally suggested that versions of these could be exact models. There have been a variety of continuing initiatives that involve discrete space, with names like combinatorial physics—but most have used essentially mechanistic models (see page 1026), and none have achieved significant mainstream acceptance. Work on quantum gravity in the late 1980s and 1990s led to renewed interest in the microscopic features of spacetime (see page 1054). Models that involve discreteness have been proposed-most often based on spin networks-but there is usually still some form of continuous averaging present, leading for example to suggestions very different from mine that perhaps this could lead to the traditional continuum description through some analog of the wave-particle duality of elementary quantum mechanics. I myself became interested in the idea of completely discrete space in the mid-1970s, but I could not find a plausible framework for it until I started thinking about networks in the mid-1980s.

- Planck length. Even in existing particle physics it is generally assumed that the traditional simple continuum description of space must break down at least below about the Planck length  $Sqrt[\hbar G/c^3] \simeq 2 \times 10^{-35}$  meters—since at this scale dimensional analysis suggests that quantum effects should be comparable in magnitude to gravitational ones.
- Page 472 · Symmetry. A system like a cellular automaton that consists of a large number of identical cells must in effect be arranged like a crystal, and therefore must exhibit one of the limited number of possible crystal symmetries in any particular dimension, as discussed on page 929. And even a

generalized cellular automaton constructed say on a Penrose tiling still turns out to have a discrete spatial symmetry.

■ Page 474 · Space and its contents. A number of somewhat different ideas about space were discussed in antiquity. Around 375 BC Plato vaguely suggested that the universe might consist of large numbers of abstract polyhedra. A little later Aristotle proposed that space is set up so as to provide a definite place for everything—and in effect to force it there. But in geometry as developed by Euclid there was at least a mathematical notion of space as a kind of uniform background. And by sometime after 300 BC the Epicureans developed the idea of atoms of matter existing in a mostly featureless void of space. In the Middle Ages there was discussion about how the non-material character of God might fit in with ideas about space. In the early 1600s the concept of inertia developed by Galileo implied that space must have a certain fundamental uniformity. And with the formulation of mechanics by Isaac Newton in 1687 space became increasingly viewed as something purely abstract, quite different in character from material objects which exist in it. Philosophers had meanwhile discussed matter—as opposed to mind—being something characterized by having spatial extent. And for example in 1643 Thomas Hobbes suggested that the whole universe might be made of the same continuous stuff, with different densities of it corresponding to different materials, and geometry being just an abstract idealization of its properties. But in the late 1600s Gottfried Leibniz suggested instead that everything might consist of discrete monads, with space emerging from the pattern of relative distances between them. Yet with the success of Newtonian mechanics such ideas had by the late 1700s been largely forgotten—leading space almost always to be viewed just in simple abstract geometrical terms. The development of non-Euclidean geometry in the mid-1800s nevertheless suggested that even at the level of geometry space could in principle have a complicated structure. But in physics it was still assumed that space itself must have a standard fixed Euclidean form-and that everything in the universe must just exist in this space. By the late 1800s, however, it was widely believed that in addition to ordinary material objects, there must throughout space be a fluid-like ether with certain mechanical and electromagnetic properties. And in the 1860s it was even suggested that perhaps atoms might just correspond to knots in this ether (see page 1044). But this idea soon fell out of favor, and when relativity theory was introduced in 1905 it emphasized relations between material objects and in effect always treated space as just some kind of abstract background, with no real structure of its own. But in 1915 general relativity introduced the idea that space could actually have a varying non-Euclidean geometry-and that this could represent gravity. Yet it was still assumed that matter was something different—that for example had to be represented separately by explicit terms in the Einstein equations. There were nevertheless immediate thoughts that perhaps at least electromagnetism could be like gravity and just arise from features of space. And in 1918 Hermann Weyl suggested that this could happen through local variations of scale or "gauge" in space, while in the 1920s Theodor Kaluza and Oskar Klein suggested that it could be associated with a fifth spacetime dimension of invisibly small extent. And from the 1920s to the 1950s Albert Einstein increasingly considered the possibility that there might be a unified field theory in which all matter would somehow be associated with the geometry of space. His main specific idea was to allow the metric of spacetime to be non-symmetric (see page 1052) and perhaps complex—with its additional components yielding electromagnetism. And he then tried to construct nonlinear field equations that would show no singularities, but would have solutions (perhaps analogous to the geons discussed on page 1054) that would exhibit various discrete features corresponding to particles—and perhaps quantum effects. But with the development of quantum field theory in the 1920s and 1930s most of physics again treated space as fixed and featureless-though now filled with various types of fields, whose excitations were set up to correspond to observed types of particles. Gravity has never fit very well into this framework. But it has always still been expected that in an ultimate quantum theory of gravity space will have to have a structure that is somehow like a quantum field. But when quantum gravity began to be investigated in earnest in the 1980s (see page 1054) most efforts concentrated on the already difficult problem of pure gravity-and did not consider how matter might enter. In the development of ordinary quantum field theories, supergravity theories studied in the 1980s did nominally support particles identified with gravitons, but were still formulated on a fixed background spacetime. And when string theory became popular in the 1980s the idea was again to have strings propagating in a background spacetime—though it turned out that for consistency this spacetime had to satisfy the Einstein equations. Consistency also typically required the basic spacetime to be 10-dimensional—with the reduction to observed 4D spacetime normally assumed to occur through restriction of the other dimensions to some kind of so-called Calabi-Yau manifold of small extent, associated excitations with various particles through an analog of the Kaluza-Klein mechanism. It has always been hoped that this kind of seemingly arbitrary setup would somehow automatically

emerge from the underlying theory. And in the late 1990s there seemed to be some signs of this when dualities were discovered in various generalized string theories-notably for example between quantum particle excitations and gravitational black hole configurations. So while it remains impossible to work out all the consequences of string theories, it is conceivable that among the representations of such theories there might be ones in which matter can be viewed as just being associated with features of space.

#### Space as a Network

- **Page 476 · Trivalent networks.** With n nodes and 3 connections at each node a network must always have an even number of nodes, and a total of 3 n/2 connections. Of all possible such networks, most large ones end up being connected. The number of distinct such networks for even n from 2 to 10 is {2, 5, 17, 71, 388}. If no self connections are allowed then these numbers become {1, 2, 6, 20, 91}, while if neither self nor multiple connections are allowed (yielding what are often referred to as cubic or 3-regular graphs), the numbers become {0, 1, 2, 5, 19, 85, 509, 4060, 41301, 510489},  $(6 n)!/((3 n)!(2 n)!288^n e^2).$ asymptotically symmetric graphs see page 1032.) If one requires the planar numbers to be the {0, 1, 1, 3, 9, 32, 133, 681, 3893, 24809, 169206}. If one looks at subnetworks with dangling connections, the number of these up to size 10 is {2, 5, 7, 22, 43, 141, 373, 1270, 4053, 14671}, or {1, 1, 2, 6, 10, 29, 64, 194, 531, 1733} if no self or multiple connections are allowed (see also page 1039).
- Properties of networks. Over the past century or so a variety of global properties of networks have been studied. Typical ones include:
- Edge connectivity: the minimum number of connections that must be removed to make the network disconnected.
- Diameter: the maximum distance between any two nodes in the network. The pictures below show the largest planar trivalent networks with diameters 1, 2 and 3, and the largest known ones with diameters 4, 5 and 6.

![](Images/_page_1044_Picture_8.jpeg)

![](Images/_page_1044_Picture_9.jpeg)

![](Images/_page_1044_Picture_10.jpeg)

![](Images/_page_1044_Picture_11.jpeg)

![](Images/_page_1044_Picture_12.jpeg)

• Circumference: the length of the longest cycle in the network. Although difficult to determine in particular cases, many networks allow so-called Hamiltonian cycles that include every node. (Up to 8 nodes, all 8 trivalent networks have this property; up to 10 nodes 25 of 27 do.)

• Girth: the length of the shortest cycle in the network. The pictures below show the smallest trivalent networks with girths 3 through 8 (so-called cages). Girth can be relevant in seeing whether a particular cluster can ever occur in network.

![](Images/_page_1044_Picture_15.jpeg)

![](Images/_page_1044_Picture_16.jpeg)

![](Images/_page_1044_Picture_17.jpeg)

![](Images/_page_1044_Picture_18.jpeg)

![](Images/_page_1044_Picture_19.jpeg)

![](Images/_page_1044_Picture_20.jpeg)

- Chromatic number: the minimum of colors that can be assigned to nodes so that no adjacent nodes end up the same color. It follows from the Four-Color Theorem that the maximum for planar networks is 4. It turns out that for all trivalent networks the maximum is also 4, and is almost always 3.
- Regular polytopes. In 3D, of the five regular polyhedra, only the tetrahedron, cube and dodecahedron have three edges meeting at each vertex, corresponding to a trivalent network. (Of the 13 additional Archimedean solids, 7 vield trivalent networks.) In 4D the six regular polytopes have 4, 4, 6, 8, 4 and 12 edges meeting at each vertex, and in higher dimensions the simplex (d+1) vertices) and hypercube  $(2^d)$ vertices) have d edges meeting at each vertex, while the cocube (2d vertices) has 2(d-1). (See also symmetric graphs on page 1032, and page 929.)
- Page 476 · Generalizations. Almost any kind of generalized network can be emulated by a trivalent network just by introducing more nodes. As indicated in the main text, networks with more than three connections at each node can be emulated by combining nodes into groups, and looking only at the connections between groups. Networks with colored nodes can be emulated by representing each color of node by a fixed group of nodes. Going beyond ordinary networks, one can consider hypernetworks in which connections join not just pairs of nodes, but larger numbers of nodes. Such hypernetworks are specified by adjacency tensors rather than adjacency matrices. But it is possible to emulate any hypernetwork by having each generalized connection correspond to a group of connections in an ordinary trivalent network.
- Maintaining simple rules. An important reason for considering models based solely on trivalent networks is that they allow simpler evolution rules to be maintained (see page 508). If nodes can have more than three connections, then they will often be able to evolve to have any number of connections—in which case one must give what is in effect an infinite set of rules to specify what to do for each number of connections.

■ Page  $477 \cdot 3D$  network. The 3D network (c) can be laid out in space using  $Array[x{8 \#\#}] \&, \{n, n, n\}$  where

```
\begin{split} x[m:\{\_,\_,\_\}] &:= \{x_1[m], x_1[m+4], \\ x_2[m+\{4,2,0\}], x_2[m+\{0,6,4\}]\} \\ x_1[m:\{\_,\_,\_\}] &:= \text{Line}[\text{Map}[\#+m\&,\{\{1,0,0\},\{1,1,1\}, \{0,2,1\},\{1,1,1\},\{3,1,3\},\{3,0,4\},\{3,1,3\},\{4,2,3\}\}]]] \\ x_2[\{i\_,j\_,k\_\}] &:= \\ x_1[\{-i-4,-j-2,k\}] /. \{a\_,b\_,c\_\} \to \{-a,-b,c\} \end{split}
```

The resulting structure is a cubic array of blocks with each block containing 8 nodes. The shortest cycle that returns to a particular node turns out to involve 10 edges. The structure does not correspond to the way that chemical bonds are arranged in any common crystalline materials, probably because it would be likely to be mechanically unstable.

- Continuum limits. For all everyday purposes a region in a network with enough nodes and an appropriate pattern of connections can act just like ordinary continuous space. But at a formal mathematical level this can happen rigorously only in an infinite limit. And in general, there is no reason to expect that all properties of the system (notably for example the existence of particles) will be preserved by taking such a limit. But in understanding the structure of space and comparing to ordinary continuous space it is convenient to imagine taking such a limit. Inevitably there are several scales involved, and one can only expect continuum behavior if one looks at scales intermediate between individual connections in the underlying network and the overall size of the whole network. Yet as I will discuss on pages 534 and 1050 even at such scales it is far from straightforward to see how all the various well-studied properties of ordinary continuous space (as embodied for example in the theory of manifolds) can emerge from discrete underlying networks.
- Page 478 · Definitions of distance. Any measure of distance-whether in ordinary continuous space or elsewhere—takes a pair of points and yields a number. Several properties are normally assumed. First, that if the points are identical the distance is zero, and if they are different, it is a positive number. Second, that the distance between points A and B is the same as between B and A. And third, that the so-called triangle inequality holds, so that the distance AC is no greater than the sum of the distances AB and BC. With distance on a network defined as the length of shortest path between nodes one immediately gets all three of these properties. And even though all distances defined this way will be integers, they still make any network formally correspond in mathematical terms to a metric space (or strictly a path metric space). If the connections on the underlying network are one-way (as in causal networks) then one no longer necessarily gets the second property, and when

a continuum limit exists it can correspond to a (perhaps discontinuous) section through a fiber bundle rather than to a manifold. Note that as discussed on page 536 physical measures of distance will always end up being based not just on single paths in a network, but on the propagation of something like a particle, which typically in effect requires the presence of many paths. (See page 1048.)

■ Page 478 · Definitions of dimension. The most obvious way to define the dimension of a space is somehow to ask how many parameters-or coordinates-are needed to specify a point in it. But starting in the 1870s the discovery of constructs like space-filling curves (see page 1127) led to investigation of other definitions. And indeed there is some reason to believe that around 1884 Georg Cantor may have tried developing a definition based on essentially the idea that I use here of looking at growth rates of volumes of spheres (balls). But for standard continuous spaces this definition is hard to make robust—since unlike in discrete networks where one can define volume just by counting nodes, defining volume in a continuous space requires assigning a potentially arbitrary density function. And as a result, in the late 1800s and early 1900s other definitions of dimension were developed. What emerged as most popular is topological dimension, in which one fills space with overlapping balls, and asks what the minimum number that ever have to overlap at any point will be. Also considered was so-called Hausdorff dimension, which became popular in connection with fractals in the 1980s (see page 933), and which can have non-integer values. But for discrete networks the standard definitions for both topological and Hausdorff dimension give the trivial result 0. One can get more meaningful results by thinking about continuum limits, but the definition of dimension that I give in the main text seems much more straightforward. Even here, there are however some subtleties. For example, to find a definite volume growth rate one does still need to take some kind of limitand one needs to avoid sampling too many or too few nodes in the network. And just as with fractal dimensions discussed on page 933 there are issues about whether a definite power law for the growth rate will emerge, and how one should average over results for different parts of the network. There are some alternative approaches to defining dimension in which some of these issues at least become less explicit. For example, one can imagine not just forming a ball on the network, but instead growing something like a cellular automaton, and seeing how big a pattern it produces after some number of steps. And similarly, one can for example look at the statistics of random walks on the network. A slightly different but still related approach is to study the

density of eigenvalues of the Laplace operator-which can also be thought of as measuring the number of solutions to equations giving linear constraints on numbers assigned to connected nodes. More sophisticated versions of this involve looking at invariants studied in topological field theory. And there are potentially also definitions based for example on considering geodesics and seeing how many linearly independent directions can be defined with them. (Note that given explicit coordinates, one can check whether one is in d or more dimensions by asking for all possible points

 $Det[Table[(x[i]-x[j]), (x[i]-x[j]), \{i, d+3\}, \{j, d+3\}]] = 0$ and this should also work for sufficiently separated points on networks. Still another related approach is to consider coloring the edges of a network: if there are d+1 possible colors, all of which appear at every node, then it follows that d coordinates can consistently be assigned to each node.)

■ Page 478 · Counting of nodes. The number of nodes reached by going out to network distance r (with r > 1) from any node in the networks on page 477 is (a) 4r-4, (b)  $3r^2/2 - 3r/2 + 1$ , and (c)

```
First[Select[4r^3/9 + 2r^2/3 +
      {2, 5/3, 5/3}r - {10/9, 1, -4/9}, IntegerQ]]
```

In any trivalent network, the quantity f[r] obtained by adding up the numbers of nodes reached by going distance rfrom each node must satisfy f[0] = n and f[1] = 3n, where nis the total number of nodes in the network. In addition, the limit of f[r] for large r must be  $n^2$ . The values of f[r] for all other r will depend on the pattern of connections in the

- Page 479 · Cycle lengths. The lengths of the shortest cycles (girths) of the networks on page 479 are (a) 3, (b) 5, (c) 4, (d) 4, (e) 3, (f) 5, (g) 6, (h) 10, (i)  $\infty$ , (j) 3. Note that rules of the kind discussed on page 508 which involve replacing clusters of nodes can only apply when cycles in the cluster match those in the network.
- **Page 479 · Volumes of spheres.** See page 1050.
- Page 480 · Implementation. Networks are conveniently represented by assigning a number to each node, then having lists of rules which specify what nodes the connection from a particular node go to. The tetrahedron network from page 476 is for example given in this representation by

```
\{1 \rightarrow \{2, 3, 4\}, 2 \rightarrow \{1, 3, 4\}, 3 \rightarrow \{1, 2, 4\}, 4 \rightarrow \{1, 2, 3\}\}
```

The list of nodes reached by following up to n connections from node *i* are then given by

```
NodeLists[g_, i_, n_] :=
  NestList[Union[Flatten[# /. g]] &, {i}, n]
```

The network distance corresponding to the length of the shortest path between two nodes is given by

Distance[g\_, {i\_, j\_}] := Length[NestWhileList[ Union[Flatten[# /. g]] &, {i}, ! MemberQ[#, j] &]] - 1

• Finding layouts. One way to lay out a network q so that network distances in it come as close as possible to ordinary distances in d-dimensional space, is just to search for values of the x[i, k] which minimize a quantity such as

```
With[{n = Length[g]}, Apply[Plus,
    Flatten[(Table[Distance[g, {i, j}], {i, n}, {j, n}])^2 - Table[ Sum[(x[i, k] - x[j, k])^2, \{k, d\}], \{i, n\}, \{j, n\}])^2]]]
```

using for example FindMinimum starting say with  $x[1, \_] \rightarrow 0$ and all the other  $x[\_,\_] \rightarrow Random[]$ . Rarely is there a unique minimum that can be found, but the approach nevertheless seems to work fairly well whenever a good layout exists in a particular number of dimensions. One can imagine weighting different network distances differently, but usually I have found that equal weightings work best. If one ignores all constraints beyond network distance 1, then one is in effect just trying to build the network out of identical rigid rods. It turns out that this is almost always possible even in 2D (though not in 1D); the only exception is the tetrahedron network. And in fact very few trivalent structures are rigid, in the sense the angles between rods are uniquely determined. (In 3D, for example, this is true only for the tetrahedron.)

- Hamming distances. In the so-called loop switching method of routing messages in communications systems one lays out a network on an m-dimensional Boolean hypercube so that the distance on the hypercube (equal to Hamming distance) agrees with distance in the network. It is known that to achieve this exactly, m must be at the least the number of either positive or negative eigenvalues of the distance matrix for the network, and can need to be as much as n-1, where nis the total number of nodes.
- Continuous mathematics. Even though networks are discrete, it is conceivable that network-based models can also be formulated in terms of continuous mathematics, with a network-like structure emerging for example from the pattern of singularities or topology of continuous surfaces or functions.

#### The Relationship of Space and Time

■ **History.** The idea of representing time graphically like space has a long history-and was used for example by Nicholas Oresme in the mid-1300s. In the 1700s and 1800s the idea of position and time as just two coordinates was widespread in mathematical physics-and this then led to notions like "travelling in time" in H. G. Wells's 1895 The Time Machine. The mathematical framework developed for relativity theory in the early 1900s (see page 1042) treated space and time very symmetrically, leading popular accounts of the theory to emphasize a kind of fundamental equivalence between them and to try to make this seem inevitable through rather confusing thought experiments on such topics as idealized trains travelling near the speed of light.

In the context of traditional mathematical equations there has never been much reason to consider the possibility that space and time might be fundamentally different. For typically space and time are both just represented by abstract symbolic variables, and the formal process of solving equations as a function of position in space and as a function of time is essentially identical. But as soon as one tries to construct more explicit models of space and time one is immediately led to consider the possibility that they may be quite different.

- Page 482 · Discreteness in time. In present-day physics, time, like space, is always assumed to be perfectly continuous. But experiments—the most direct of which are based on looking for quantization in the measured decay times of very short-lived particles—have only demonstrated continuity on scales longer than about 10<sup>-26</sup> seconds, and there is nothing to say that on shorter scales time is not in fact discrete. (The possibility of a discrete quantum of time was briefly discussed in the 1920s when quantum mechanics was first being developed.)
- Page 483 · Network constraint systems. Cases (a), (f) and (p) allow all networks that do not contain respectively cycles of length 1 (self-loops), cycles of length 3 or less, and cycles of length 5 or less. In cases where an infinite sequence of networks is allowed, there are typically particular subnetworks that can occur any number of times, making the sizes of allowed networks form arithmetic progressions. In cases (m), (n) and (o) respectively triangle, pentagon and square subnetworks can be repeated.

The main text excludes templates that have no dangling connections, and are thus themselves already complete networks. There are 5 such templates involving nodes out to distance one, but of these only 3 correspond to networks that satisfy the constraint that around each node the network has the same form as the template. Among templates involving nodes out to distance two there are 106 that have no dangling connections, and of these only 8 satisfy the constraints.

The main text considers only constraints based on a single template. One can also allow each node to have a neighborhood that corresponds to any of a set of templates. For templates involving nodes out to distance one, there are 13 minimal sets in the sense of page 941, of which only 6 contain just one template, 6 contain two and 1 contains three.

If one does allow dangling connections to be joined within a single template, the results are similar to those discussed so far. There are 52 possible templates involving nodes out to distance two, of which 12 allow complete networks to be formed, none forced to be larger than 12 nodes. There are 46 minimal sets, with the largest containing 4 templates, but none forcing a network larger than 16 nodes.

• Symmetric graphs. The constraints in a network constraint system require that the structure around each node agrees with a template that contains some number of nodes. A symmetric graph satisfies the same type of constraint, but with the template being the whole network. The pictures below show the smallest few symmetric graphs with 3 connections at each node (with up to 100 nodes there are still only 37 such graphs; compare page 1029).

![](Images/_page_1047_Picture_11.jpeg)

- Cayley graphs. As discussed on page 938, the structure of a group can be represented by a Cayley graph where nodes correspond to elements in the group, and connections specify results of multiplying by generators. The transitivity of group multiplication implies that Cayley graphs always have the property of being symmetric (see above). The number of connections at each node is fixed, and given by the number of distinct generators and inverses. In cases such as the tetrahedral group  $A_4$  there are 3 connections at each node. The relations among the generators of a group can be thought of as constraints defining the Cayley graph. As mentioned on page 938, there are finite groups that have simple relations but at least very large Cayley graphs. For infinite groups, it is known (see page 938) that in most cases Cayley graphs are locally like trees, and so do not have finite dimension. It appears that only when the group is nilpotent (so that certain combinations of elements commute much as they do on a lattice) is there polynomial growth in the Cayley graph and thus finite dimension.
- **Page 485 · Spacetime symmetric rules.** With k = 2 and the neighborhoods shown here, only the additive rules 90R, 105R, 150R and 165R are space-time symmetric. For larger kand larger neighborhoods, there presumably begin to be nonadditive rules with this property.

#### Time and Causal Networks

■ Causal networks. The idea of using networks to represent interdependencies of events seems to have developed with the systematization of manufacturing in the early 1900snotably in the work of Frank and Lillian Gilbreth-and has been popular since at least the 1940s. Early applications included switching circuits, logistics planning, decision analysis and general flowcharting. In the last few decades causal networks have been widely used in system specification methods such as Petri nets, as well as in schemes for medical and other diagnosis. Since at least the 1960s, causal networks have also been discussed as representations of connections between events in spacetime, particularly in quantum mechanics (see page 1027).

Causal networks like mine that are ultimately associated with some evolution or flow of activity always have certain properties. In particular, they can never contain loops, and thus correspond to directed acyclic graphs. And from this it follows for example that even the most circuitous path between two nodes must be of finite length.

Causal networks can also be viewed as Hasse diagrams of partially ordered sets, as discussed on page 1040.

■ Implementation. Given a list of successive positions of the active cell, as from Map[Last, MAEvolveList[rule, init, t]] (see page 887), the network can be generated using

```
MAToNet[list_] := Module[\{u, j, k\}, u[_] = \infty; Reverse[
       Table[j = list[[i]]; k = \{u[j-1], u[j], u[j+1]\}; u[j-1] = 0
            u[j] = u[j + 1] = i; i \rightarrow k, \{i, Length[list], 1, -1\}]]
```

where nodes not yet found by explicit evolution are indicated by  $\infty$ .

- Page 488 · Mobile automata. The special structure of mobile automata of the type used here leads to several special features in the causal networks derived from them. One of these is that every node always has exactly 3 incoming and 3 outgoing connections. Another feature is that there is always a path of doubled connections (associated with the active cell) that visits every node in some order. And in addition, the final network must always be planar—as it is whenever it is derived from the evolution of a local underlying 1D system.
- Computational compression. In the model for time described here, it is noteworthy that in a sense an arbitrary amount of underlying computation can take place between successive moments in perceived time.
- Page 496 · 2D mobile automata. As in 2D random walks, active cells in 2D mobile automata often do not return to positions they have visited before, with the result that no causal connections end up being created.

#### The Sequencing of Events in the Universe

■ Implementation. Sequential substitution systems in which only one replacement is ever done at each step can just be implemented using /. as described on page 893. Substitution systems in which all replacements are done that are found to fit in a left-to-right scan can be implemented as follows

```
GSSEvolveList[rule_, s_, n_] :=
     NestList[GSSStep[rule, #] &, s, n]
  GSSStep[rule\_, s\_] :=
     g[rule, s, f[StringPosition[s, Map[First, rule]]]]
   f[\{\}] = \{\}; f[s_] := Fold[If[Last[Last[#1]] \ge First[#2],
           #1, Append[#1, #2]] &, {First[s]}, Rest[s]]
  g[rule\_, s\_, \{\}] := s; g[rule\_, s\_, pos\_] := StringReplacePart[
       s, Map[StringTake[s, #] &, pos] /. rule, pos]
with rules given as \{"ABA" \rightarrow "BAAB", "BBBB" \rightarrow "AA"\}.
```

■ Generating causal networks. If every element generated in the evolution of a generalized substitution system is assigned a unique number, then events can be represented for example by  $\{4, 5\} \rightarrow \{11, 12, 13\}$ —and from a list of such events a causal network can be built up using

```
With[{u = Map[First, list]}, MapIndexed[Function[
      \{e, i\}, First[i] \rightarrow Map[(If[\# === \{\}, \infty, \#[1, 1]]] \&)[
                Position[u, #]] &, Last[e]]], list]]
```

- **The sequential limit.** Even when the order of applying rules does not matter, using the scheme of a sequential substitution system will often give different results. If there is a tree of possible replacements (as in "A"  $\rightarrow$  "AA"), then the sequential substitution system in a sense does depth-first recursion in the infinite tree, never returning from the single path it takes. Other schemes are closer to breadth-first recursion.
- Page 502 · Rule (b). The maximum number of steps for which the rule can be applied occurs with initial conditions consisting of a white element followed by n black elements, and in this case the number of steps is  $2^n + n$ .
- String theory. The sequences of symbols I call strings here have absolutely no direct connection to the continuous deformable 1D objects known as strings in string theory.
- String overlaps. The total numbers of strings with length nand k colors that cannot overlap themselves are given by

```
a[0] = 1; a[n_{-}] := k a[n-1] - If[EvenQ[n], a[n/2], 0]
Up to reversal and interchange of A and B, the first few overlap-
```

free strings with 2 colors are A, AB, AAB, AAAB, AABB. The shortest pairs of strings of 2 elements with no self- or

overlaps are {"A", "B"}, {"AABB", "AABAB"}, {"AABB", "ABABB"}; there are a total of 13 such pairs with strings up to length 5, and 85 with strings up to length 6.

The shortest non-overlapping triple of strings {"AAABB", "ABABB", "ABAABB"} and its variants. There are a total of 36 such triples with no string having length more than 6.

■ Simulating mobile automata. Given a mobile automaton like the one from page 73 with rules in the form used on page

887-and behavior of any complexity-the following will yield a causal-invariant substitution system that emulates it: Map[StringJoin, Map[{"AAABB", "ABABB", "ABAABB"}][ # + 1]] &, Map[Insert[#[[1]], 2, 2] -Insert[#[[2, 1]], 2, 2 + #[[2, 2]]] &, rule], {2}], {2}]

■ Sequential cellular automata. Ordinary cellular automata are set up so that every cell is updated in parallel at each step, based on the colors of neighboring cells on the previous step. But in analogy with generalized substitution systems, one can also consider sequential cellular automata, in which cells are updated sequentially rather than in parallel. The behavior of such systems is usually very different from that of corresponding ordinary cellular automata, mainly because in sequential cellular automata the new color of a particular cell can depend on new rather than old colors of neighboring cells.

The pictures below show the behavior of several sequential cellular automata with k = 2, r = 1 elementary rules. In the top picture of each pair every individual update is indicated by a black dot. In the bottom picture each line represents one complete step of evolution, including one update of each cell. Note that in this representation, effects can propagate all the way across the system in a single step.

![](Images/_page_1049_Picture_5.jpeg)

Size dependence. Because effects can propagate all the way across the system in a single step, the overall size, as well as boundary conditions, for the system can be significant after just a few steps, as illustrated in the pictures of rule 60 below.

![](Images/_page_1049_Picture_7.jpeg)

![](Images/_page_1049_Picture_8.jpeg)

![](Images/_page_1049_Picture_9.jpeg)

Additive rules. Among elementary sequential cellular automata, those with additive rules turn out to yield some of the most complex behavior, as illustrated below. The top row shows evolution with the boundary forced to be white; the bottom row shows cyclic boundary conditions. Even though the basic rule is additive, there seems to be no simple traditional mathematical description of the results.

![](Images/_page_1049_Picture_11.jpeg)

![](Images/_page_1049_Picture_12.jpeg)

Updating orders. Somewhat different results are typically obtained if one allows different updating orders. For each complete update of a rule 90 sequential cellular automaton, the pictures below show results with (a) left-to-right scan, (b) random ordering of all cells, the same for each pass through the whole system, (c) random ordering of all cells, different for different passes, (d) completely random ordering, in which a particular cell can be updated twice before other cells have even been updated once.

![](Images/_page_1049_Figure_14.jpeg)

History. Sequential cellular automata have a similar relationship to ordinary cellular automata as implicit updating schemes in finite difference methods have to explicit ones, or as infinite impulse response digital filters have to finite ones. There were several studies of sequential or asynchronous cellular automata done following my work on ordinary cellular automata in the early 1980s.

Implementation. The following will update triples of cells in the specified order by using the function *f*:

```
OrderedUpdate[f_, a_, order_] := Fold[ReplacePart[
       #1, f[Take[#1, {#2 - 1, #2 + 1}]], #2] &, a, order]
```

A random ordering of n cells corresponds to a random permutation of the form

Fold[Insert[#1, #2, Random[Integer, Length[#1]] + 1] &, {}, Range[n]]

■ Intrinsic synchronization in cellular automata. Taking the rules for an ordinary cellular automaton and applying them sequentially will normally yield very different results. But it turns out that there are variants on cellular automata in which the rules can be applied in any order and the overall behavior obtained—or at least the causal network—is always the same. The picture below shows how this works for a simple block cellular automaton. The basic idea is that to each cell is added an arrow, and any pair of cells is updated only when their arrows point at each other. This in a sense forces cells to wait to be updated until the data they need is ready. Note that the rules can be thought of as replacements such as "A > < B"  $\rightarrow$  "< AB >" for blocks of length 4 with 4 colors.

![](Images/_page_1050_Picture_8.jpeg)

![](Images/_page_1050_Picture_9.jpeg)

"Firing squad" synchronization. By choosing appropriate rules it is possible to achieve many forms of synchronization directly within cellular automata. One version posed as a problem by John Myhill in 1957 consists in setting up a rule in which all cells in a region go into a special state after exactly the same number of steps. The problem was first solved in the early 1960s; the solution using 6 colors and a minimal number of steps shown on the right below was found in 1988 by Jacques Mazover, who also determined that no similar 4-color solutions exist. Note that this solution in effect constructs a nested pattern of any width (it does this by optionally including or excluding one additional cell at each nesting level, using a mechanism related to the decimation systems of page 909). If one drops the requirement of cells

going into a special state, then even the 2-color elementary rule 60 shown on the left can be viewed as solving the problem—but only for widths that are powers of 2.

![](Images/_page_1050_Picture_12.jpeg)

![](Images/_page_1050_Picture_13.jpeg)

![](Images/_page_1050_Picture_14.jpeg)

![](Images/_page_1050_Picture_15.jpeg)

Distributed computing. Many of the basic issues about the progress of time in a universe consisting of many separate elements have analogs in the progress of computations that are distributed across many separate computing elements. In practice, such computations are most often done by requiring explicit synchronization of all elements at appropriate points, and implementing this using a mechanism that is outside of the computation. But more theoretical investigations of formal concurrent systems, temporal logics, dataflow systems, Petri nets and so on have led to ideas about distributed computing that are somewhat closer to the ones I discuss here for the universe. And, as it happens, in the mid-1980s I tried hard, though at the time without much success, to use updating rules for networks as the basis for a new kind of programming language intended for massively parallel computers.

#### Uniqueness and Branching in Time

- Page 506 · String transformations. An example of a rule that allows one to go from any string of A's and B's to any other is  $\{"A" \rightarrow "AA", \ "AA" \rightarrow "A", \ "A" \rightarrow "B", \ "B" \rightarrow "A"\}$ (Compare page 1038.)
- Parallel universes. The idea of parallel universes which somehow interact with each other has been much explored in science fiction. And one might think that if the history of each universe corresponds to one path in a multiway system then the convergence of paths might represent interactions between universes. But in fact, much as in the case of time travel, such connections do not represent additional observable effects; they simply imply consistency conditions, in this case between universes whose paths converge.
- Many-worlds models. The notion of "many-figured time" has been discussed since the 1950s in the context of the manyworlds interpretation of quantum mechanics. There are some similarities to the multiway systems that I consider here. But an important difference is that while in the many-worlds

approach, branchings are associated with possible observation or measurement events, what I suggest here is that they could be an intrinsic feature of even the very lowest-level rules for the universe. (See also page 1063.)

■ Spacetime networks from multiway systems. The main text considers models in which the steps of evolution in a multiway system yield a succession of events in time. An alternative kind of model, somewhat analogous to the ones based on constraints on page 483, is to take the pattern of evolution of a multiway system to define directly a complete spacetime network. Instead of looking separately at strings produced at each step, one instead maintains just a single copy of each distinct string ever produced, and makes that correspond to a node in the network. Each node is then connected to the nodes associated with the strings reached by one application of the multiway rule, as on page 209.

It is fairly straightforward to generate in this way networks of any dimension. For example, starting with n A's the rule  $\{"A" \rightarrow "AB", "AB" \rightarrow "A"\}$  yields a regular *n*-dimensional grid, as shown below.

![](Images/_page_1051_Picture_5.jpeg)

![](Images/_page_1051_Picture_6.jpeg)

If each node in a network is associated with a point in spacetime, then one slightly peculiar feature is that every such point would have an associated string-something like an encoded position coordinate. And it then becomes somewhat difficult to understand why different regions of spacetime seem to behave so similarly-and do not, for example, seem to depend on the details of their coordinates.

- Page 507 · Commuting operations. If replacements on strings are viewed as mathematical operations, then when the replacements give the same result if applied in any order, the corresponding operations commute.
- Conditions for convergence. One way to guarantee that there is convergence after one step is to require as in the previous section that blocks to be replaced cannot overlap with themselves or each other. And of the 196 possible rules involving two colors and blocks of length at most three, 112 have this property. But there are also an additional 20 rules which allow some overlap but which nevertheless yield convergence after one step. Examples are "AAA"  $\rightarrow$  "A" and "AA"  $\rightarrow$  "ABA". In these rules some of the elements essentially just supply context, but are not affected by the replacement. These elements can then overlap while not affecting the

result. Note that unless one excludes the context elements from events, paths in the multiway system will converge, but the causal networks on these paths will be locally slightly different.

Much as in the previous section, even if paths do not converge for every possible string, it can still be true that paths converge for all strings that are actually generated from a particular initial string.

In general, one can consider convergence after any number of steps, requiring that any two strings which have a common ancestor must at some point also have a common successor. Note that a rule such as  $\{"A" \rightarrow "B", "A" \rightarrow "C", "B" \rightarrow "A", "B" \rightarrow "D"\}$ exhibits convergence for all paths that have diverged for only one step, but not for all those that have diverged for longer. In general it is formally undecidable whether a particular multiway system will eventually exhibit convergence of all paths.

■ Confluence. As mentioned on page 938, multiway systems have been studied in mathematical logic, typically under names such as rewrite systems, since the early 1900s. The property of path convergence discussed in the main text has been considered since the 1930s, usually under the name of confluence, or sometimes the Church-Rosser property. (Also considered is strong confluence—that paths can always converge in at most one step, and local confluence—that paths can converge after diverging for one step but not necessarily more. Early in its history confluence was most often studied for symbolic systems and lambda calculus rather than ordinary multiway systems.)

Confluence is important in defining a notion of equivalence for strings. One can say that two strings are equivalent if they can both be transformed to the same string by using the rules of the multiway system. And with such a definition, confluence is what is needed to obtain transitivity for equality, so that p == q and q == r implies p == r.

Most often confluence is studied in the context of terminating multiway systems-multiway systems in which eventually strings are produced to which no further replacements apply. If a terminating multiway system has the confluence property, then this implies that regardless of the path taken, a given string will always evolve to a unique string that can be thought of as giving a canonical or normal form for the original string. Examples (a) through (c) below have this property; (d) does not. In example (a), the canonical form is all elements black; in (b) it is a single black element, and in (c) all elements are black, except the last one, which is white if there were any initial white elements. Note that the first example on page 507 has a canonical form consisting of a sorted string.

![](Images/_page_1052_Picture_2.jpeg)

![](Images/_page_1052_Picture_3.jpeg)

![](Images/_page_1052_Picture_4.jpeg)

The process of evaluation in mathematics or in a computer language such as Mathematica can be thought of as involving the application of a sequence of replacement rules. Only if these rules have the confluence property will the results always be unique, and independent of the order of rule application.

The evaluation of functions with attribute Flat in Mathematica provides an example of confluence. If f is Flat, then in evaluating f[a, b, c] one can equally well start with f[f[a, b], c] or f[a, f[b, c]]. Showing only the arguments to f, the pictures below illustrate how the flat functions Xor and And are confluent, while the non-flat function Implies is not.

![](Images/_page_1052_Picture_7.jpeg)

![](Images/_page_1052_Picture_8.jpeg)

![](Images/_page_1052_Picture_9.jpeg)

■ Completion. If one has a multiway system that terminates but is not confluent then it turns out often to be possible to make it confluent by adding a finite set of new rules. Given a string p which gets transformed either to q or r by the original rules, one can always imagine adding a new rule  $q \rightarrow r$  or  $r \rightarrow q$  that makes the paths from p immediately converge. To do this explicitly for all possible p that can occur would however entail having infinitely many new rules. But as noted by Donald Knuth and Peter Bendix in 1970 it turns out often to be sufficient just iteratively to add new rules only for each so-called critical pair q, r that is obtained from strings p that represent minimal overlaps in the left-hand sides of the rules one has. To decide whether to add  $q \rightarrow r$  or  $r \rightarrow q$  in each case one can have some kind of ordering on strings. For the procedure to work this ordering must be such that the strings generated on successive steps in every possible evolution of the multiway system follow the ordering. A number of variations of the basic procedureusing different orderings and with different schemes for dropping redundant rules—have been proposed for systems arising in different kinds of applications. The original Knuth-Bendix procedure was for equations (of the form  $a \leftrightarrow b$ ) had the feature that it could terminate yet not give a confluent multiway system. But in the 1980s so-called unfailing completion algorithms (see page 1158) were developed that-if they terminate-guarantee to give confluent systems. (The question of whether any procedure of this type will terminate in a particular case is nevertheless in general undecidable.)

The basic idea of so-called critical pair completion procedures has arisen several times—notably in the Gröbner basis approach of Bruno Buchberger from 1965 to finding canonical forms for systems of polynomials.

■ Relationships between types of networks. Each arrow on each path in a multiway system corresponds to a node in a causal network. Each element in each string in a multiway system corresponds to a connection in a causal network. Each complete string in a multiway system corresponds to a possible slice that goes through all connections across a causal network. Such a slice can be considered in traditional physics terms as a spacelike hypersurface (see page 1041).

#### **Evolution of Networks**

- Page 509 · Neighbor-independent rules. Even though the same replacement is performed at each node at each step, the networks produced are not homogeneous. In the first case shown, the picture produced after t steps has  $4 \times 3^{t-k-1}$ regions with  $3 \times 2^k$  edges. In the limit  $t \to \infty$ , the picture has the geometrical form of an Apollonian circle packing (see page 986). The number of nodes at distance up to r from a given node is at most  $1 + Sum[c[i] + c[i-1], \{i, n\}]$  where  $c[i_{-}] := 2 \cdot DigitCount[i_{+}, 2]$ . In practice this number fluctuates greatly with r, making pictures like those on page 479 not exhibit smooth profiles. Averaged over all nodes, however, the number of nodes at distance up to r approximates r^Log[2, 3], implying an effective dimension of Log[2, 3]. Note that there is no upper limit on the dimension that can be obtained with appropriate neighbor-independent rules.
- Implementation. For many practical purposes the best representation for networks is the one given on page 1031. But in updating networks a particularly straightforward implementation of one scheme can be obtained if one uses instead a more explicit symbolic representation such as

 $u[1 \to v[2,\,3,\,4],\,2 \to v[1,\,3,\,4],\,3 \to v[1,\,2,\,4],\,4 \to v[1,\,2,\,3]]$ This allows one to capture the basic character of networks by Attributes[u] = {Flat, Orderless}; Attributes[v] = Orderless

Updating rules can then be written in terms of ordinary Mathematica patterns. A slight complication is that the patterns have to include all nodes whose connections go to nodes whose labels are changed by the update. The rule at the top of page 509 must therefore be written out as

and this corresponds to the Mathematica rule

$$\begin{split} u[i1\_ \to v[i2\_, i3\_, i4\_], i3\_ \to v[i1\_, i5\_, i6\_], \\ i4\_ \to v[i1\_, i7\_, i8\_]] & \mapsto u[i1 \to v[i2, \text{new}[1], \text{new}[2]], \\ \text{new}[1] \to v[i1, \text{new}[2], i3], \text{new}[2] \to v[i1, \text{new}[1], i4], \\ i3 \to v[\text{new}[1], i5, i6], i4 \to v[\text{new}[2], i7, i8]] \end{split}$$

(Strictly there also need to be additional rules to cover where for example nodes 3 and 4 are actually the same.) With rules in this form the network update is simply

NetStep[rule\_, net\_] := Block[{new},

net /. rule /. new  $[n_-] \rightarrow n + Apply[Max, Map[First, net]]]$ Note that just as we discussed for strings on page 1033 the direct use of /. here corresponds to a particular scheme for applying the update rule.

- **Identifying subnetworks.** The problem of finding where in a network a given subnetwork can occur turns out in general to be computationally difficult. For strings the analogous problem is straightforward, since in a string of length n one can ultimately just try each of the n possible starting points for the substring and see for which of them a match occurs. But for a network with n nodes, a similar procedure would require one to check  $n^k$  possible configurations in order to find out where a subnetwork of size k occurs. In practice, however, for fixed subnetworks, one can devise fairly efficient procedures. But the general problem of so-called subgraph isomorphism is formally NP-complete.
- Page 509 · Number of replacements. The total number of distinct replacements that maintain planarity, involve clusters with up to five nodes and have from 3 to 7 dangling connections is {16, 8, 125, 24, 246}. Not maintaining planarity, the numbers are {14, 5, 13, 2, 2}. (See page 1039.)
- Cycles in networks. See page 1031.
- **Planar networks.** One feature of a planar network is that it is always possible to identify definite regions or faces bounded by connections in the network. And from Euler's formula f + n = e + 2, it then follows that the average number of edges of each face is always 6(1-2/f), where f is the total number of faces. Note that with my definition of dimension for networks, the fact that a network is planar does not necessarily mean that it has be two-dimensional—and for example the networks on page 509 are not.
- **Arbitrary transformations.** By applying the string transformation rules on page 1035 at appropriate locations, it

is possible to transform any string of *A*'s and *B*'s to any other. And the analog of this for networks is that by applying the rules shown below at appropriate locations it is possible to transform any network into any other. These rules correspond to the moves invented by James Alexander in 1923 in connection with transforming one knot into another. (Note that the first two rules suffice for all planar networks, and are sometimes called respectively T2 and T1.)

![](Images/_page_1053_Picture_14.jpeg)

As an example, the pictures below show how a tetrahedron network can be transformed into a cube.

![](Images/_page_1053_Picture_16.jpeg)

■ **Random networks.** One way to generate the connections for a "completely random" trivalent network with *n* nodes is just to apply a random permutation:

RandomNetwork[n\_?EvenQ] := Partition[ Fold[Insert[#1, #2, Random[Integer, Length[#1]] + 1] &, {}, Floor[Range[1, n + 2/3, 1/3]]], 2]

Networks obtained in this way are usually connected, but will almost always contain self-loops and multiple edges. Properties of random networks are discussed on page 963. A convenient way to get somewhat random planar networks is from 2D Voronoi diagrams of the kind discussed on page 987.

■ Random replacements. As indicated in the note above, applying the second rule (T1, shown as (b) on page 511) at an appropriate sequence of positions can transform one planar network into any other with the same number of nodes. The pictures below show what happens if this rule is repeatedly applied at random positions in a network. Each time it is applied, the rule adds two edges to one face, and removes them from another. After many steps the pictures below show that faces with large numbers of edges appear. The average number of edges must always be 6 (see note above), but in a sufficiently large network the probability for a face to have n edges eventually approaches an equilibrium value of  $8(n-2)(2n-3)!!(3/8)^n/n!$ . (For large *n* this is approximately  $\lambda^n$  with  $\lambda = 3/4$ ; if 1- and 2-edged regions are allowed then  $\lambda = (3 + \sqrt{3})/6 \approx 0.79$ .) There may be some easy way to derive such results, but so far it has only been done using fairly sophisticated techniques from quantum field theory developed in the late 1970s. The starting point is to look at a  $\phi^3$  field theory with SU(n) internal symmetry and to note that in the limit  $n \to \infty$  what dominates are Feynman diagrams that have the structure of planar trivalent networks (see page 1040). And it then turns out that in zero spacetime dimensions the complete path integral for the theory can be evaluated exactly—yielding in effect a generating function for the number of possible networks. Parametric differentiation (to yield n-point correlation functions) then gives results for n-sided regions. Another result that has been derived is that the average total number m[n] of edges of all faces around a given face with n edges is 7n + 3 + 9/(n + 1). Note that the networks obtained always have dimension 2 according to my definitions.

![](Images/_page_1054_Figure_3.jpeg)

■ Cellular structures. There are many systems in nature that consist of assemblies of discrete regions-and the lines that define the interfaces between these regions form networks. In many cases the regions are fixed once established (compare page 988). But in other cases there is continuing evolution, as for example in soap and other foams and froths, grains in metals and perhaps some biological tissues. In 2D situations the lines between regions generically form a trivalent planar network. In a soap foam, the geometrical layout of this network is determined by surface tension forces-with connections meeting at 120° at each node, though being slightly curved and of different lengths. Pressure differences lead to diffusion of gas and on average to von Neumann's Law that the area of an *n*-sided region changes linearly with time, at a rate proportional to n-6. Typically the network topology of a foam continually rearranges itself through cascades of seemingly random T1 processes (rule (b) from page 511), with regions that reach zero size disappearing through T2 processes (reversed rule (a)). And as noted for example by Cyril Smith in the early 1950s there is a characteristic coarsening that occurs. Something similar is already visible in the pure T1 pictures in the note above. But results such as the so-called Aboav-Weaire law that m[n] from the note above is in practice about 5n + c suggest that T2 processes are also important. (Processes like cell division in 2D biological tissue in effect directly add connections to a network. But this can again be thought of as a combination of T1 and T2 processes, and in appropriate idealizations can lead to very similar results.)

■ Page 514 · Cluster numbers. The following tables give the total numbers of distinct clusters-with number of nodes going across the page, and number of dangling connections going down. (See also page 1038.)

|   | 1 | 2 | 3 | 4 | 5 | 6 | 7  | 8  | 9   | 10  |
|---|---|---|---|---|---|---|----|----|-----|-----|
| 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0  | 5  | 0   | 19  |
| 1 | 0 | 0 | 0 | 0 | 1 | 0 | 4  | 0  | 19  | 0   |
| 2 | 0 | 0 | 0 | 1 | 0 | 5 | _  | 23 | 0   | 132 |
| 3 | 1 | 0 | 1 | 0 | 3 | 0 | 15 | 0  | 91  | 0   |
| 4 | 0 | 1 | 0 | 2 |   | 9 | 0  | 54 | 0   | 390 |
| 5 | 0 | 0 | 1 | 0 |   | 0 |    | 0  | 166 | 0   |
| 6 | 0 | 0 | 0 | 2 | 0 | 9 | 0  | 63 | 0   | 551 |

|    | -1 | 2 | 2 | 4 | _ | _ | 7  | 0  | _   | 10  |
|----|----|---|---|---|---|---|----|----|-----|-----|
|    | 1  | - | 3 | 4 | 5 | О | /  | 8  | 9   | 10  |
| 7  | 0  | 0 | 0 | 0 | 2 | 0 | 17 | 0  | 157 | 0   |
| 8  | 0  | 0 | 0 | 0 | 0 | 4 | 0  | 38 | 0   | 424 |
| 9  | 0  | 0 | 0 | 0 | 0 | 0 | 6  | 0  | 80  | 0   |
| 10 | 0  | 0 | 0 | 0 | 0 | 0 | 0  | 11 | 0   | 180 |
| 11 | 0  | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 18  | 0   |
| 12 | 0  | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0   | 37  |
|    |    |   |   |   |   |   |    |    |     |     |

■ Page 515 · Non-overlapping clusters. The picture shows all distinct clusters with 3 dangling connections and 9 nodes that are not self-overlapping. The only smaller cluster with the same property is the trivial one with just a single node.

Most clusters that can overlap will be able to do so in an infinite number of possible networks. (One can see this by noting that they can overlap inside clusters with dangling connections, not just closed networks.) But there are some clusters that can overlap only in a few small networks. The pictures below show examples where this happens. The pictures in the main text still treat such clusters as nonoverlapping.

![](Images/_page_1054_Picture_11.jpeg)

![](Images/_page_1054_Picture_12.jpeg)

![](Images/_page_1054_Picture_13.jpeg)

If two clusters overlap, then this means that there is some network in which there are copies of these clusters that involve some of the same nodes. And it is possible to search for such a network by starting from a single node and then sequentially trying to take corresponding pieces from the two clusters.

- 1- and 2-connection clusters. Clusters with just one or two dangling connections can always in effect be thought of just as adding extra structure to single connections in a network. But this extra structure can be important in the application of other rules-and can for example emulate something like having multiple colors of connections.
- Connectedness. It is not clear whether a network that represents the universe must remain globally connected, or whether pieces can break off. But any replacements that take connected clusters and yield connected clusters must always maintain the connectedness of any network.

- Reversibility. By including both forward and backward versions of every transformation it is straightforward to set up reversible rules for network evolution. It is not clear, however, whether the basic rules for the universe are really reversible. It could well be that the apparent reversibility we see arises because the universe is effectively on an attractor, as discussed on page 1018. Note that if pieces of the universe can break off, but cannot reconnect, then there will inevitably be an irreversible loss of information.
- 1/n expansion. If there are n possible colors for each connection in a network, then for large n it turns out that the vast majority of networks will be planar. This idea was used in the 1980s as a way of simplifying the Feynman diagrams to consider in QCD and other quantum field theories. (See page 1039.)
- Feynman diagrams. In the standard approach to particle physics, possible interaction processes are represented by networks in which each node corresponds to an elementary interaction, and the nodes are joined by connections which correspond to the propagation of particles in spacetime. I can see no direct physical relationship between such diagrams and the networks I consider. However, at a mathematical level, the set of trivalent networks with n nodes formally corresponds to the set of n<sup>th</sup> order Feynman diagrams in a  $\phi$   $^3$  field theory. (Compare page 1039.)
- Chemical analogy. The evolution of a network can be thought of as an idealized version of a chemical process in which molecules are networks of bonds. (See page 1193.)
- Symbolic representations. Expressions in which common subexpressions are shared correspond to networks, as do collections of relations between objects representing nodes.
- **Graph grammars.** The notion of generalizing substitutions for strings to the case of networks has been discussed in computer science since the 1960s-and a fair amount of formal work has been done on so-called graph grammars for specifying formal languages whose elements are networks. Even a good analog of regular languages has, however, not yet been found. But applications to constructing or verifying practical network-based system description schemes are quite often discussed. In mathematics rather little is usually done with anything but very trivial network substitutions. In mathematics, rather little is usually done with network substitutions, though the proof of the Four-Color Theorem in 1976 was for example based on showing that 300 or so possible replacement rules-if applied in an appropriate sequence-can transform any graph to have one of 1936 smaller subgraphs that require the same number of colors. (32 rules and 633 subgraphs are now known to be sufficient.)

■ **Network mobile automata.** The analog of a mobile automaton can be defined for networks by setting up a single active node, then having rules which replace clusters of nodes around this active node, and move its position. The pictures below show two simple examples.

![](Images/_page_1055_Picture_8.jpeg)

The total number of replacements that can be used in the rules of a network mobile automaton and which involve clusters with up to four nodes and have from 1 to 4 dangling connections is (14, 10, 2727, 781). Despite looking at several hundred thousand cases I have not been able to find network mobile automata with especially complicated behavior.

Note that by having a cluster of nodes with a unique form it is possible to emulate a network mobile automaton using an ordinary network substitution system.

■ **Directed network systems.** If one adds directionality to the connections in a network it becomes particularly easy to set up rules for clusters of nodes that cannot overlap. For no two clusters whose dangling connections all point inwards can ever overlap, at least so long as neither of these clusters themselves contain subclusters whose dangling connections similarly all point inwards. The pictures below show a few examples of such clusters. Note that in a random network of *n* nodes, about *n*/8 such clusters typically occur.

![](Images/_page_1055_Picture_12.jpeg)

#### Space, Time and Relativity

■ Page 516 · Posets. The way I set things up, collections of events can be thought of as partially ordered sets (posets). If all events occurred in a definite sequence in time, this would define a total linear ordering for them. But with the setup I use, there is only a partial ordering of events, defined by causal connections. The causal networks I draw are so-called Hasse or order diagrams of the posets of events. If a connection goes directly from x to y in this network then x is said to cover y. And in general if there is a path from x to y then one writes x > y. The collection of all events that will lead to a given set of events (the union of their past light cones) is known as the filter of that set. Within a poset, there

can be sequences of elements that are totally ordered, and these are called chains. (The maximum length of any chain is sometimes called the dimension of a poset, but this is unrelated to the notions of dimension I consider.) There can also be sets of elements between which no ordering relations at all are defined, and these are called antichains.

Standard examples of posets include subsets of a set ordered by the subset relation, complex numbers ordered by magnitude, and integers ordered by divisibility. Posets first arose as general concepts in the late 1800s in connection with the development of mathematical logic, and to some extent abstract algebra. They became somewhat popular in the mid-1900s, both as formal generalizations in lattice theory, and as structures in various combinatorics applications. It was already noted in the 1920s that events in relativity theory formed posets.

The pictures below show the first few distinct possible Hasse diagrams for posets. For successive numbers of elements the total numbers of these are 1, 2, 5, 16, 63, 318, 2045, 16999, ...

![](Images/_page_1056_Picture_5.jpeg)

- Page 517 · Spacelike slices. The definition of spacelike slices used here is directly analogous to what is used in traditional relativity theory (typically under names like spacelike hypersurfaces and Cauchy surfaces). There will normally be many different possible choices of spacelike slices, but in all cases a particular such slice is set up to represent what can consistently be thought of as all of space at a given time. One definition of a spacelike slice is then a maximal set of points in which no pair are causally related (corresponding to a maximal antichain in a poset). Another definition (equivalent for any connected causal network) is that spacelike slices are what consistently divide a causal network into a past and a future. And an intermediate definition is that a spacelike slice contains points that are not themselves causally related, but which appear in either the past or the future of every other point. Given a spacelike slice in a causal network, it is always possible to construct another such slice by finding all those points whose immediate predecessors are all included either in the original slice or its predecessors.
- Page 518 · Speed of light. In a vacuum the speed of light is 299,792,458 meters/second (and this is actually what is taken to define a meter). In materials light mostly travels

slower-basically because there are delays when it is absorbed and reemitted by atoms. In a first approximation, the slowdown factor is the refractive index. But particularly in materials which can amplify light a whole sequence of peculiar effects have been observed-and it is fairly subtle to account correctly for incoming and outgoing signals, and to show that at least no energy or information is transmitted faster than c. The standard mathematical framework of relativity theory implies that any massless particle must propagate at c in a vacuum—so that not only light but also gravitational waves presumably go at this speed (and the same is at least approximately true of neutrinos). The effective mass for massive particles increases by a factor  $1/Sqrt[1-v^2/c^2]$  at speed v, making it take progressively more energy to increase v. At a formal mathematical level it is possible to imagine tachyons which always travel faster than c. But the structure of modern physics would find it difficult to accommodate interactions between these and ordinary particles.

■ Page 522 · History of relativity. (See also page 1028.) The idea that mechanical processes should work the same regardless of how fast one is moving was expressed by Galileo in the early 1600s, particularly in connection with the motion of the Earth-and was incorporated in the laws of mechanics formulated by Isaac Newton in 1687. But when the wave theory of light finally became popular in the mid-1800s it seemed to imply that no similar principle could be true for light. For it was generally assumed that waves of light must correspond to explicit disturbances in a medium or ether that fills space. And it was thus expected that for example the apparent speed of light would depend on how fast one was moving with respect to this ether. And indeed in particular this was what the equations electromagnetism developed by James Maxwell in the 1860s seemed to suggest. But in 1881 an experiment by Albert Michelson (repeated more accurately in 1887 as the Michelson-Morley experiment and now done to the 10<sup>-20</sup> level) showed that in fact this was not correct. Already in 1882 George FitzGerald and Hendrik Lorentz noted that if there was a contraction in length by a factor  $Sqrt[1-v^2/c^2]$ in any object moving at speed v (with c being the speed of light) then this would explain the result. And in 1904 Lorentz pointed out that Maxwell's equations are formally invariant under a so-called Lorentz transformation of space and time coordinates (see note below). Then in 1905 Albert Einstein proposed his so-called special theory of relativity-which took as its basic postulates not only that the laws of mechanics and electrodynamics are independent of how fast one is moving, but that this is also true of the speed of light.

And while at first these postulates might seem incompatible, what Einstein showed was that they are not-at least if modifications are made to the basic laws of mechanics. In the few years that followed, various formulations of this result were given, with Hermann Minkowski in 1908 showing that it could be derived if one just assumes that space and time enter all physical laws together in a certain kind of 4D vector. In the late 1800s Ernst Mach had emphasized the idea of formulating science and particularly mechanics in terms only of concepts that can actually be measured by observers. And in this framework Einstein and others gave what seemed to be almost purely deductive arguments for relativity theorywith the result that it generally came to be assumed that there was no meaningful sense in which one could ever imagine deriving relativity from anything more fundamental. Yet as I discussed earlier in the chapter, if a complete theory of physics is to be as simple as possible, then most things like relativity theory must in effect be derived from more basic features of the theory—as I start to try to do in the main text of this section.

■ Standard treatment. In a standard treatment of relativity theory one way to begin is to consider setting up a square grid of points in space and time-and then to ask what kind of transformed grid corresponds to this same set of points if one is moving at some velocity v. At first one might assume that the answer would just be a grid that has been sheared by the simple transformation  $\{t, x\} \rightarrow \{t, x-vt\}$ , as in the first row of pictures below. And indeed for purposes of Newtonian mechanics this so-called Galilean transformation is exactly what is needed. But as the pictures below illustrate, it implies that light cones tip as v increases, so that the apparent speed of light changes, and for example Maxwell's equations must change their form. But the key point is that with an appropriate transformation that affects both space and time, the speed of light can be left the same. The necessary transformation is the so-called Lorentz transformation

$$\{t, x\} \rightarrow \{t - v x/c^2, x - v t\}/Sqrt[1 - v^2/c^2]$$

And from this the time dilation factor  $1/Sqrt[1-v^2/c^2]$ shown on page 524 follows, as well as the length contraction factor  $Sqrt[1-v^2/c^2]$ . An important feature of the Lorentz transformation is that it preserves the quantity  $c^2 t^2 - x^2$  with the result that as v changes in the pictures below a given point in the grid traces out a hyperbola whose asymptotes lie on a light cone. Note that on a light cone  $c^2 t^2 - x^2$  always vanishes. Note also that the intersection of the past and future light cones for two events separated by a distance x in space and t in time always has a volume proportional exactly to  $c^2 t^2 - x^2$ .

![](Images/_page_1057_Figure_6.jpeg)

■ Inferences from relativity. The pictures on page 524 show that an idealized clock based on bouncing light between mirrors will exhibit relativistic time dilation. And from such derivations it is often assumed that the same result must hold for any possible clock system. But as a practical matter it does not. And indeed for example the clocks in GPS satellites are specifically set up so as to remove the effects of time dilation. And in the twin paradox one can certainly imagine that each twin could have an accelerometer whose readings they use to correct their clocks. Indeed, even when it comes to individual particles there are subtle effects associated with acceleration and radiation (see page 1062)—so that in the end not entirely clear that something like a biological system would actually in practice exhibit just standard time dilation.

One feature of relativity is that it implies that only relative motion is ultimately ever detectable. (This was also implied by Newtonian mechanics for purely mechanical systems.) And from this it is often concluded that there can be nothing like an ether that one can consider as defining an absolute state of rest in the universe. But in fact the cosmic microwave background in effect does exactly this. For in standard cosmological models it fills the universe, but is everywhere at rest relative to the global center of mass of the universe. And from the anisotropies we have observed in the microwave background it is thus possible to conclude that the Earth is moving at an absolute speed of about  $c/10^3$  relative to the center of mass of the universe. In particle physics standard models also in effect introduce things that are assumed to be at rest relative to the center of mass of the universe. One example is the Higgs condensate discussed in connection with particle masses (see page 1047). Other possible examples include zero-point fluctuations in quantum fields.

Outside of science, relativity theory is sometimes given as evidence for various general ideas of cultural relativism (compare page 1131)—which have existed since well before relativity theory in physics, and seem in the end to have no meaningful connection to it.

- Particle physics. Relativity theory was originally formulated just for mechanics and electromagnetism. But its predictions like  $E = mc^2$  were immediately applied for example to radioactivity, and soon it came to be assumed that the theory would work for any system at all—unless it involved gravity. So this has meant that in particle physics  $c^2 t^2 - x^2 - y^2 - z^2$  is at some level the only quantity that ever appears. And to make mathematical work easier, what is very often done is to carry out the so-called Wick rotation  $t \rightarrow it$ —so relativistic invariance is just independence on 4D orientation. (See page 1061.) But except in rather simple cases there is practically no evidence that results obtained after Wick rotation have anything to do with physical reality-and certainly the transformation removes some very basic phenomena such as particle propagation. One feature of it, however, is that it maps the equation for quantum mechanical time evolution into the equation for probabilities in statistical mechanics, with imaginary time corresponding to inverse temperature. And while it is conceivable that this mapping may have some deep significance, none has so far ever been identified.
- Time travel. The idea that space and time are similar suggests that it might be possible to move backwards and forwards in time just like it is possible to move backwards and forwards in space. And indeed in the partial differential equations that define general relativity, it is formally possible for the motion of particles to achieve this, at least when there is sufficient negative energy density from matter or a cosmological constant. But even in this case there is no real progression in which one travels backwards in time. Instead, the possibility of motion that leads to earlier times simply implies a requirement of consistency between behavior at earlier and later times.

#### **Elementary Particles**

■ Note for physicists. My goal in the remainder of this chapter is not to present a specific ultimate model for physics, but rather to discuss at a fairly general level some features that I believe such a model will have, given the overall discoveries of this book, and the specific results I have described in this chapter. I am certainly aware that many physicists will want to know more details. But particularly in making contact with existing physics it is almost inevitable that all sorts of technical formalism will be needed—and to maintain balance in this book I have not included this here. (Given my own personal background in theoretical physics it will come as no surprise that I have often used such formalism in the process of working out what I describe in these sections.)

■ Page 525 · Types of particles. Current particle physics identifies three basic types of known elementary particles: leptons, quarks and gauge bosons. The known leptons are the electron (e), muon ( $\mu$ ) and tau lepton ( $\tau$ ), and their corresponding neutrinos  $(v_e, v_\mu, v_\tau)$ . Quarks exist inside hadrons like the proton and pion, but never seem to occur as ordinary free particles. Six types are known: u, d, c (charm), s (strange), t (top), b. Gauge bosons are associated with forces. Those currently known are the photon  $(\gamma)$  for electromagnetism (QED), W and Z for so-called weak interactions, and the gluon (g) for QCD interactions between quarks. Gravitons associated with gravitational forces presumably also exist. In ordinary matter, the only particles that contribute in direct ways to everyday physical, chemical and even nuclear properties are electrons, photons and effectively u and d quarks, and gluons. (These, together presumably with some type of neutrino, are the only types of particles that never seem to decay.) The first reasonably direct observations of the various types of particles were as follows (some were predicted in advance): e (1897),  $\gamma$  (~1905), u, d $(1914/\sim1970)$ ,  $\mu$  (1937), s (1946),  $\nu_e$  (1956),  $\nu_u$  (1962), c (1974),  $\tau$ ,  $v_{\tau}$  (1975), b (1977), g (~1979), W (1983), Z (1983), t (1995).

Most particles exist in several variations. Apart from the photon (and graviton), all have distinct antiparticles. Each quark has 3 possible color configurations; the gluon has 8. Most particles also have multiple spin states. Quarks and leptons have spin 1/2, yielding 2 spin states (neutrinos could have only 1 if they were massless). Gauge bosons normally have spin 1 (the graviton would have spin 2) yielding 3 spin states for massive ones. Real massless ones such as the photon always have just 2. (See page 1046.)

In the Standard Model the idea of spontaneous symmetry breaking (see page 1047) allows particles with different masses to be viewed as manifestations of single particles, and this is effectively done for W, Z,  $\gamma$ , as well as for each of the 3 so-called families of quarks and leptons: u, d; c, s; t, b and e,  $v_e$ ;  $\mu$ ,  $\nu_{\mu}$ ;  $\tau$ ,  $\nu_{\tau}$ . Grand unified models typically do this for all known gauge bosons (except gravitons) and for corresponding families of quarks and leptons-and inevitably imply the existence of various additional particles more massive than those known, but with properties that are somehow intermediate. Some models also unify different families, and supersymmetric models unify quarks and leptons with gauge bosons.

■ History. The idea that matter—and light—might be made up of discrete particles was already discussed in antiquity (see page 876). But it was only in the mid-1800s that there started to be real evidence for the existence of some kind of discrete atoms of matter. Yet at the time, the idea of fields was popular, and it was believed that the universe must be filled with a continuous fluid-like ether responsible at least for light and other electromagnetic phenomena. So for example following ideas of William Rankine from 1849 William Thomson (Kelvin) in 1867 suggested that perhaps atoms might be like knotted stable vortex rings in the ether-with different knots corresponding to different chemical elements. But though it initiated the mathematical classification of knots, and now has certain conceptual similarities to what I discuss in this book, the details of this model did not work out-and it had been largely abandoned even before the electron was discovered in 1897. Ernest Rutherford's work in the 1910s on scattering from atoms introduced the idea of an atomic nucleus, and after the discovery of the neutron in 1932 it became clear that the main constituents of nuclei were protons and neutrons. The positron and the muon were discovered in cosmic rays in the 1930s, followed in the 1940s by a handful of other particles. By the 1960s particle accelerators were finding large numbers of new particles every year. And the hypothesis was then suggested that all these particles might actually be composed of just three more fundamental particles that became known as quarks. An alternative so-called democratic or bootstrap hypothesis was also suggested: that somehow any particle could just be viewed as a composite of all others with the same overall properties—with everything being determined consistency in the web of interactions between particles, and no particles in a sense being more fundamental than others. But by the early 1970s experiments on so-called deep inelastic scattering had given increasingly direct evidence for pointlike constituents inside particles like protons-and by the mid-1970s these were routinely identified with quarks.

As soon as the electron was discovered there were questions about its possible size. For if its charge was distributed over a sphere of radius r, this was expected to lead to electrostatic repulsion energy proportional to 1/r. And although it was suggested around 1900 that effects associated with this might account for the mass of the electron, this ran into problems with relativity theory, and it also remained mysterious just what might hold the electron together. (A late suggestion made in 1953 by Hendrik Casimir was that it could be forces associated with zero-point fluctuations in quantum fieldsbut at least with the simplest setup these turned out to have wrong sign.)

The development of quantum theory in the 1920s showed that discrete particles will inevitably exhibit continuous wave-like features in their spatial distribution of probability amplitudes. But traditional quantum mechanics and quantum field theory are both normally formulated with the assumption that the basic particles they describe have zero intrinsic spatial size. Sometimes nonzero size is taken into account by inserting additional interaction parameters—as done in the 1950s with magnetic moments and form factors of protons and neutrons. But for example in quantum electrodynamics the definite assumption is made that electrons are intrinsically of zero size. Quantum fluctuations make any particle in an interacting field theory effectively be surrounded by virtual particles. Yet not unlike in classical electrodynamics having zero intrinsic size for the electron still immediately suggests that an electron should have infinite self-energy. In the 1930s ideas about avoiding this centered around modifying basic laws of electrodynamics or the structure of spacetime (see page 1027). But the development of renormalization in the 1940s showed that these infinities could in effect just be factored out. And by the 1960s a long series of successes in the predictions of QED had led to the almost universal belief that its assumption of pointlike electrons must be correct. It was occasionally suggested that the muon might be some kind of composite object. But experiments seemed to indicate that it was in every way identical to the electron, except in mass. And although no reasonable explanation for its existence was found, it came to be generally assumed by the 1970s that it was just another point-like particle. And indeed-apart from few rare suggestions to the contrary—the same is now assumed throughout mainstream practical particle physics for all of the basic particles that appear in the Standard Model. (Actual experiments based on high-energy scattering and precision magnetic moment measurements have shown only that electrons and muons must have sizes smaller than about  $\hbar c/(10 \text{ TeV}) \simeq 10^{-20} \text{ m}$ —or about  $10^{-5}$  times the size of a proton. One can make arguments that composite particles this small should have masses much larger than are observed—but it is easy to find theories that avoid these.)

In the 1980s superstring theory introduced the idea that particles might actually be tiny 1D strings-with different types of particles corresponding essentially just to strings in different modes of vibration. Since the 1960s it has been noted in many simplified quantum field theories that there can be a kind of duality in which a soliton or other extended field configuration in one representation becomes what acts like an elementary particle in another representation. And in the late 1990s there were indications that such phenomena could occur in generalized string theories-leading to suggestions of at least an abstract correspondence between for example particles like electrons and gravitational configurations like black holes.

- Page 526 · Topological defects. An idealized vortex in a 2D fluid involves velocity vectors that in effect wind around a point-and can never be unwound by making a series of small local perturbations. The result is a certain kind of stability that can be viewed as being of topological origin. One can classify forms of stability like this in terms of the mathematics of homotopy. Most common are point and line defects in vector fields, but more complicated defects can occur, notably in liquid crystals, models of condensates in the early universe, and certain nonlinear field theories. Analogs of homotopy can presumably be devised to represent certain forms of stability in systems like the networks I consider.
- Page 527 · Kuratowski's theorem. Any network can be laid out in 3D space. (This is related to the Whitney embedding theorem that any d-dimensional manifold can be embedded in (2d+1)-dimensional space.) When one says that a network is planar what one means is that it can be laid out in ordinary 2D space without any lines crossing. Kuratowski's theorem that planarity is associated with the absence of specific subgraphs in a network is an important result in graph theory established in the late 1920s. A subgraph is formally defined to be what one gets by selecting just some subset of connections in a network-and with this definition Kuratowski's theorem must allow extensions of  $K_5$  and  $K_{3,3}$  where extra nodes have been inserted in the middle of connections. (K5 and K33 are examples of socalled complete graphs, obtained by taking sets of specified numbers of nodes and connecting them in all possible ways.) Another approach is to consider reducing whole networks to so-called minors by deleting connections or merging connected nodes, and in this case Wagner's theorem shows that any non-planar network must be exactly reducible to either K5 or K33.

One can generalize the question of planarity to asking whether networks can be laid out on 2D surfaces with various topological structures-and in fact the genus of a graph can be defined to be the number of handles that must be added to a plane to embed the graph without crossings. But even on a torus it turns out that there is no finite set of (extended) subgraphs whose absence guarantees that a network can successfully be laid out. Nevertheless, if one considers minors a finite list does suffice-though for example on a torus it is known that at least 800 (and perhaps vastly more) are needed. (There is in fact a general theorem established since the 1980s that absolutely any list of networks-say for example ones that cannot be laid on a given surface—must actually in effect always all be reducible

to some finite list of minors.) Note that finding the genus for a particular trivalent network is in general NP-complete.

- Page 527 · Gauge invariance. It is often convenient to define quantities for which only differences or derivatives matter. In classical physics an example is electric potential, which can be shifted by any constant amount without affecting voltage differences or the electric field given by its gradient. In the mid-1800s the idea emerged of a vector potential whose curl gives the magnetic field, and it was soon recognized—notably by James Clerk Maxwell-that any function whose curl vanishes (and that can therefore normally be written as a gradient) could be added to the vector potential without affecting the magnetic field. By the end of the 1800s the general conditions on electromagnetic potentials for invariance of fields were known, though were not thought particularly significant. In 1918 Hermann Weyl tried to reproduce electromagnetism by adding the notion of an arbitrary scale or gauge to the metric of general relativity (see page 1028)-and noted the "gauge invariance" of his theory under simultaneous transformation of electromagnetic potentials and multiplication of the metric by a position-dependent factor. Following the introduction of the Schrödinger equation in quantum mechanics in 1926 it was almost immediately noticed that the equations for a charged particle in an electromagnetic field were invariant under gauge transformations in which the wave function was multiplied by a position-dependent phase factor. The idea then arose that perhaps some kind of gauge invariance could also be used as the basis for formulating theories of forces other than electromagnetism. And after a few earlier attempts, Yang-Mills theories were introduced in 1954 by extending the notion of a phase factor to an element of an arbitrary non-Abelian group. In the 1970s the Standard Model then emerged, based entirely on such theories. In mathematical terms, gauge theories can be viewed as describing fiber bundles in which connections between values of group elements in fibers at neighboring spacetime points are specified by gauge potentials-and curvatures correspond to gauge fields. (General relativity is in effect a special case in which the group elements are themselves related to spacetime coordinates.)
- lacktriangle Page 527 · Identifying particles. In something like a class 4 cellular automaton it is quite straightforward to start enumerating possible persistent structures—as we saw in Chapter 6. But in a network system it can be much more difficult. Ultimately what one wants to do is to find what possible types of forms for local regions are inequivalent under the application of the underlying rules. But in general it may be undecidable even whether two such forms are actually equivalent (compare the notes below and on page

1051)—since to tell this one might need to be able to apply the rules infinitely many times. In specific cases, however, generalizations of concepts like planarity and homotopy may provide useful guides. And a first step may be to look at small closed networks and try to determine which of these can be transformed into each other by a given set of rules.

■ Knot theory. Somewhat analogous to the problem in the note above is the problem of classifying knots. The pictures below show some of the simplest distinct knots. But given presentations of two knots, no finite procedure is known that determines in general whether the knots are equivalent (or constructs a sequence of Reidemeister moves that transform one into the other). Quite probably this is in general undecidable, though since the 1920s a few polynomial invariants have been discovered—with recent ones being related to ideas from quantum field theory—that have allowed some progress to be made. (Even the problem of determining whether a knot specified by line segments is trivial is known to be NP-complete.)

![](Images/_page_1061_Picture_3.jpeg)

- Page 528 · Charge quantization. It is an observed fact that the electric and other charges of all particles are simple rational multiples of each other. In the context of electromagnetism alone, there would be no particular reason to expect this (unless magnetic monopoles exist). But as soon as different particles are related by a non-Abelian symmetry group, then the discreteness of the representations of such a group immediately implies that all charges must be rational multiples of each other.
- **Spin.** Even when they appear to be of zero size, particles exhibit intrinsic angular momentum known as spin. The total spin is always a fixed multiple of the basic unit  $\hbar$ : 1/2 for quarks and leptons, 1 for photons and other ordinary gauge bosons, 2 for gravitons, and in theory 0 for Higgs particles. (Observed mesons have spins up to perhaps 5 and nuclei up to more than 50.) Particles of higher spin in effect require more information to specify their orientation (or polarization or its analog). And in the context of network models it could be that spin is somehow related to something as simple as the number of places at which the core of a particle is attached to the rest of the network. Spin values can be thought of as specifying which irreducible representation of the group of symmetries of spacetime is needed to describe a particle after momentum has been factored out. For ordinary massive

particles in d-dimensional space the group is Spin(d), while for massless particles it is E(d-1) (the Euclidean group). (For tachyons, it would be fundamentally non-compact, forcing continuous spin values.) For small transformations, Spin(d) is just the ordinary rotation group SO(d), but globally it is its universal cover, or SU(2) in 3D. And this can be thought of as what allows half-integer spins, which must be described by spinors rather than vectors or tensors. Such objects have the property that they are not left invariant by 360 ° rotations, but only by 720° ones—a feature potentially fairly easy to reproduce with networks, perhaps even without definite integer dimensions. In the standard formalism of quantum field theory it can be shown that (above 2D) half-integer spins must always be associated with fermions (which for example satisfy the exclusion principle), and integer spins with bosons. (This spin-statistics connection also seems to hold for various kinds of objects defined by extended field configurations.)

■ Page 528 · Particle masses. The measured masses of known elementary particles in units of GeV (roughly equal to the proton mass) are: photon: 0, electron: 0.000510998902; muon: 0.1056583569;  $\tau$  lepton: 1.77705; W: 80.4; Z: 91.19. Recent evidence suggests a mass of about 10<sup>-11</sup> GeV for at least one type of neutrino. Quarks and gluons presumably never occur as free particles, but still act in many ways as if they have definite masses. For all of them their confinement contributes perhaps 0.3 GeV of effective mass. Then there is also a direct mass: gluons 0; *u* : ~0.005; *d* ~0.01; *s*: ~0.2; *c* : 1.3; *b* : 4.4; *t* : 176 GeV. Note that among sets of particles that have the same quantum numbers—like d, s, b or  $\gamma$ , Z—mixing occurs that makes states of definite mass-that would propagate unchanged as free particles-differ by a unitary transformation from states that are left unchanged by interactions. When one sets up a quantum field theory one can typically in effect insert various mass parameters for particles. Self-interactions normally introduce formally infinite corrections—but if a theory is renormalizable then this means that there are only a limited number of independent such corrections, with the result that relations between masses of different particles are preserved. In quantum field theory any particle is always surrounded by a kind of cloud of virtual particles interacting with it. And following the Uncertainty Principle phenomena involving larger momentum scales will then to probe progressively smaller parts of this cloud-yielding different effective masses. (The masses tend to go up or down logarithmically with momentum scale-following so-called renormalization group equations.)

The Standard Model starts off with certain symmetries that force the masses of all ordinary particles to be zero. But then one assumes that nonzero masses are generated by spontaneous symmetry breaking. One starts by taking each particle to be coupled to a so-called Higgs field. Then one introduces self-interactions in this field so as to make its stable state be one that has constant nonzero value throughout the universe. But this means that as particles propagate, their interactions with the background give them an effective mass. And by having Higgs couplings be proportional to observed particle masses, it becomes inevitable that these will be the masses of particles. One prediction of the usual version of this mechanism for mass is that a definite Higgs particle should exist-which in the minimal Standard Model experiments should observe fairly soon. At times there have been hopes of so-called dynamical symmetry breaking giving the same effective results as the Higgs mechanism, but without an explicit Higgs fieldperhaps through something similar to various phenomena in condensed matter physics. String theory, like the Standard Model, tends to start with zero mass particles—and then hopes that an appropriate Higgs-like mechanism will generate nonzero ones.

■ More particles. To produce more massive particles requires higher-energy particle collisions, and today's accelerators only allow one to search up to masses of perhaps 200 GeV. (Sufficiently stable particles could have survived from the early universe, and a few cosmic ray interactions in principle give higher energies—but are normally too rare to be useful.) I am not sure whether in my approach one should expect an infinite series of progressively more massive particles. The example of nonplanarity might suggest not, but even in the class 4 cellular automata discussed in Chapter 6 it is not clear whether fundamentally different progressively larger structures will appear forever. In quantum field theory particles of any mass can always in principle exist for short times in virtual form. But normally their effects decrease like powers of their mass-making them hard to measure. In two kinds of cases, however, this does not happen: one is socalled anomalies, the other interactions with the Higgs field, in which couplings are proportional to mass. In the minimal Standard Model it turns out to be impossible to get quarks or leptons with masses much above about 200 GeV without destabilizing the vacuum (a fact pointed out by David Politzer and me in 1979). But with more complicated models one can avoid this constraint. In supersymmetric modelsand string theory-there are typically also all sorts of other types of particles, assumed to have high masses since they have not been observed. There is evidence against any more

than the three known generations of quarks and leptons in that the decay process  $Z^0 \rightarrow \nu \overline{\nu}$  has a rate that rather accurately agrees with what is expected from just three types of low-mass neutrinos.

■ **Page 530 · Expansion of the universe.** See page 1055.

#### The Phenomenon of Gravity

■ History. With the Earth believed to be the center of the universe, gravity did not seem to require much explanation: it was just a force bringing things to a natural place. But with the advent of Copernican astronomy in the 1500s something more was needed. In the early 1600s Galileo noted that the force of gravity seems to depend only on the mass of an object, and not on any of its other features. In 1687 Isaac Newton then suggested a universal inverse square law of gravity between objects. In the 1700s and 1800s all sorts of celestial mechanics was done on the basis of this-with occasional observational anomalies being resolved for example by the discovery of new planets. Starting in the mid-1800s there were attempts to formulate gravity in the same way as electromagnetism-and in 1900 it was for example suggested that gravitational effects might propagate at the speed of light. Following his introduction of relativity theory in 1905, Albert Einstein began to seek a theory of gravity that would fit in with it. Ordinary special relativity has the feature that it assumes that systems behave the same regardless of their overall velocity-but not regardless of their acceleration. In 1907 Einstein then suggested the equivalence principle that gravity always locally has the same effect as an acceleration. (This principle requires only slightly more than Galileo's idea of the equivalence of gravitational and inertial mass, which has now been verified to the 10<sup>-12</sup> level.) But by 1912 Einstein realized that if the effective laws of physics were somehow to remain the same in systems with different accelerations (or in different gravitational fields) then this would require a change in their perceived geometry. And building on ideas of differential geometry and tensor calculus from the late 1800s Einstein then began to formulate the concept that gravity is associated with curvature of space. In the late 1800s Ernst Mach had argued that phenomena like acceleration and rotation could ultimately be defined only relative to matter in the universe. And partly on this basis Einstein used the idea that curvature in space must be like a field produced by matter—leading eventually to his formulation in 1915 of the standard Einstein equations for general relativity. An immediate prediction of these was a deviation from the inverse square law, explaining an observed precession in the orbit of Mercury. After a dramatic verification in 1919 of predicted bending of light by

the Sun, general relativity began to be widely accepted. In the 1920s expansion of the universe was discovered, and this was seen to be consistent with general relativity. In the 1940s study of the evolution of stars then led to discussion of what became known as black holes. But for the most part general relativity was still viewed as being highly elegant though of little practical relevance. In the 1960s, however, more work began to be done on it. The discovery of the cosmic microwave background in 1965 led to increasing interest in cosmology. Precision tests—particularly with spacecraft—were designed. In calculations it was sometimes difficult to tell what was a genuine effect, and what was just a feature of the particular coordinates used. But a variety of increasingly abstract mathematical methods were developed, leading notably to general theorems about inevitability of singularities. Detailed calculations tended to require complicated symbolic tensor manipulation (with some associated problems being NPcomplete), but with the development of computer algebra this gradually became more feasible-and by the mid-1970s approximate numerical methods were also being used. Various alternative formulations of general relativity were proposed, based for example on tetrads, spinors and twistors (and more recently on connection, loop and non-commutative geometry methods)—but none led to any great simplification. Meanwhile, there continued to be ever more accurate experimental tests of general relativity in the solar systemand at least in the weak gravitational fields available there (with metrics differing from the identity by at most one part in 10<sup>6</sup>), all have worked out to around the 10<sup>-3</sup> level. Starting in the 1960s, more and more ambitious gravitational wave detectors have been built-although none as yet have actually observed anything. Measurements done on a binary pulsar system are nevertheless consistent at a 10-3 level with the emission of gravitational radiation in a fairly strong gravitational field at the rate implied by general relativity. And since the 1980s there has been increasing conviction that at least indirect effects of black holes associated with very strong gravitational fields are being observed.

Over the years, some variants of general relativity have been proposed. At least when formulated in terms of tensors, none have quite the simplicity of the original theory—but some lead to rather different predictions, such as an absence of singularities like black holes. Ever since quantum theory began in the early 1900s there has been discussion of quantum gravity-and almost every major method developed for handling other quantum phenomena has been tried on gravity. Starting in the 1980s a variety of methods more specific to quantum gravity were also pursued, but none have yet had convincing success. (See page 1054.)

■ Differential geometry. Standard descriptions of properties like curvature—as used for example in general relativity are normally based on differential geometry. In its usual formulation this assumes that space is continuous, and can always effectively be treated as some kind of deformed version of ordinary Euclidean space—thus forming what is known as a manifold. The result of this is that points in space can always be specified by lists of coordinates-although historically one of the objectives of differential geometry has been to find ways to define properties like curvature so that they do not depend on the choice of such coordinates. The geometrical properties of a space are in general specified by its so-called metric—and this metric allows one to compute quantities based on lengths and angles from coordinates. The metric can be written as a matrix g, defined so that the analog for infinitesimal vectors u and v of u.v in ordinary Euclidean space is u.g.v. (This is essentially equivalent to saying that infinitesimal arc length is related to infinitesimal coordinate distances by  $ds^2 = g_{i,j} dx_i dx_j$ .) In *d* dimensions the metric g for a so-called Riemannian space can in general be any dxd positive-definite symmetric matrix—and can vary with position. But for ordinary flat Euclidean space it is always just IdentityMatrix[d] (at least with Cartesian coordinates). Within say a surface whose points  $\{x_1, x_2, ...\}$ are obtained by evaluating an expression e as a function of parameters p (so that for example  $e = \{x, y, f[x, y]\},$  $p = \{x, y\}$  for a *Plot3D* surface) the metric turns out to be given by

(Transpose[#].#&)[Outer[D, e, p]]

In ordinary Euclidean space a defining feature of geometry is that the shortest path between two points is a straight line. But in an arbitrary space things can be more complicated, and in general such a path will be a geodesic (see note below) which can have a more complicated form. If the coordinates along a path are given by an expression s (such as  $\{t, 1+t, t^2\}$ ) that depends on a parameter t, and the metric at position p is q[p], then the length of a path turns out to be

Integrate[ $Sqrt[\partial_t s.g[s].\partial_t s]$ , {t, t<sub>1</sub>, t<sub>2</sub>}]

and geodesics then correspond to paths that extremize this quantity. In ordinary Euclidean space, such paths are straight lines, so that the length of a path between points with lists of coordinates a and b is just the ordinary Euclidean distance Sqrt[(a-b), (a-b)]. But in general, even though geodesics are not straight lines their lengths can still be used to define a so-called geodesic distance—which turns out to have all the various properties of a distance discussed on page 1030.

If one draws a circle of radius *r* on a page, then the smaller *r* is, the more curved the circle will be—and one can define the circle to have a constant curvature equal to 1/r. If one draws a more general curve on a page, one can define its curvature at every point by seeing what size of circle fits it best at that point-or equivalently what the coefficients are in a quadratic approximation. (Compare page 418.) With a 2D surface in ordinary 3D space, one can imagine fitting quadrics (generalized ellipsoids). But these are now specified by two radii, yielding two principal curvatures. And in general these curvatures depend on the way the surface is laid out in 3D space. But a crucial point noted by Carl-Friedrich Gauss in the 1820s is that the product of such curvatures—the so-called Gaussian curvature—is always independent of how the surface is laid out, and can thus be viewed as intrinsic to the surface itself, and for example determined purely from the metric for the 2D space corresponding to the surface.

In a 2D space, intrinsic curvature is completely specified just by Gaussian curvature. In higher-dimensional spaces, there are more components, but in general they are all part of the so-called Riemann tensor-a rank-4 tensor introduced by Bernhard Riemann in 1854. (In Mathematica, the explicit form of such a tensor can be represented as a nested list for which TensorRank[list] == 4.) Several descriptions of the Riemann tensor can be given. One is based on looking at infinitesimal vectors u, v and w and asking how much w differs when transported two ways around the edges of a parallelogram, from x to x + u + v via x + u and via x + v. In ordinary flat space there is no difference, but in general the difference is a vector that is defined to be Riemann. u.v.w. (The Riemann that appears here is formally  $R_{iik}^{l}$ .) Another description of the Riemann tensor is based on geodesics. In flat Euclidean space any two geodesics that start parallel always remain so. But a defining feature of general non-Euclidean spaces is that this is not in general so. And it turns out that the Riemann tensor is what determines the rate at which geodesics deviate from being parallel. Still another description of the Riemann tensor is as the coefficient of the quadratic terms in an expansion of the metric about a particular point, using so-called normal coordinates set up to make linear terms vanish. In general the Riemann tensor can always be computed from the metric, though it is somewhat complicated. If p is a list of coordinate parameters that appear in a d-dimensional metric g, then

```
Riemann = Table[\partial_{p[[j]]} \Gamma[[i, k]] - \partial_{p[[i]]} \Gamma[[j, k]] +
                Γ[[i, k]] . Γ[[j]] - Γ[[j, k]] . Γ[[i]], {i, d}, {j, d}, {k, d}]
where the so-called Christoffel symbol \Gamma_{ii}^{\ k} is
     \Gamma = With[\{gi = Inverse[g]\}, TableSum[
                        gi\llbracket[l,k\rrbracket,
                        {I, d}], {i, d}, {j, d}, {k, d}]]/2
```

There are d4 elements in the nested lists for Riemann, but symmetries and the so-called Bianchi identity reduce the number of independent components to  $1/12 d^2 (d^2 - 1)$ —or 20 for d = 4. One can then compute the Ricci tensor  $(R_{ik} = R_{iik}^{\ j})$  using

RicciTensor = Map[Tr, Transpose[Riemann, {1, 3, 2, 4}], {2}] and this has 1/2d(d+1) independent components in d>2dimensions. (The parts of the Riemann tensor not captured by the Ricci tensor correspond to the so-called Weyl tensor; for d = 2 the Ricci tensor has only one independent component, equal to the negative of the Gaussian curvature.) Finally, the Ricci scalar curvature is given by

RicciScalar = Tr[RicciTensor . Inverse[g]]

■ Page 531 · Geodesics. On a sphere all geodesics are arcs of great circles. On a surface of constant negative curvature (like (c)) geodesics diverge exponentially, as noted in early work on chaos theory (see page 971). The path of a geodesic can in general be found by requiring that the analog of acceleration vanishes for it. In the case of a surface defined by z = f[x, y]this is equivalent to solving

```
 \begin{aligned} x''[t] &= -\{f^{(1,0)}[x[t], y[t]](y'[t]^2 f^{(0,2)}[x[t], y[t]] + \\ &2x'[t]y'[t]f^{(1,1)}[x[t], y[t]] + x'[t]^2 f^{(2,0)}[x[t], y[t]]))/\\ &(1 + f^{(0,1)}[x[t], y[t]]^2 + f^{(1,0)}[x[t], y[t]]^2) \end{aligned}
```

together with the corresponding equation for y'', as already noted by Leonhard Euler in 1728 in connection with his development of the calculus of variations.

■ Page 532 · Spherical networks. One can construct networks of constant positive curvature by approximating the surface of a sphere-starting with a dodecahedron and adding hexagons. (Euler's theorem implies that at any stage there must always be exactly 12 pentagonal faces.) The following are examples with 20, 60, 80, 180 and 320 nodes:

![](Images/_page_1064_Picture_13.jpeg)

![](Images/_page_1064_Picture_14.jpeg)

![](Images/_page_1064_Picture_15.jpeg)

![](Images/_page_1064_Picture_16.jpeg)

![](Images/_page_1064_Picture_17.jpeg)

The object with 60 nodes is a truncated icosahedron—the shape of a standard soccer ball, as well the shape of the fullerene molecule  $C_{60}$ . (Note that in  $C_{60}$  one of the connections at each node is always a double chemical bond, since carbon has valence 4.) Geodesic domes are typically duals of such networks-with three edges on each face.

■ **Hyperbolic networks.** Any surface that always has positive curvature must eventually close up to form something like a sphere. But a surface that has negative curvature (and no holes) must in some sense be infinite-more like cases (c) and (d) on page 412. Yet even in such a case one can always define coordinates that nominally allow the surface to be drawn in a finite way-and the Poincaré disk model used in the pictures below is the standard way of doing this. In ordinary flat space, regular polygons with more than 6

sides can never form a tessellation. But in a space with negative curvature this is possible for polygons with arbitrarily many sides—and the networks that result have been much studied as Cayley graphs of Fuchsian groups. One feature of these networks is that the number of nodes reached in them by following r connections always grows like  $2^r$ . But if one intersperses hexagons in the networks (as in the main text) then one finds that for small r the number of nodes just grows like  $r^2$ —as one would expect for something like a 2D surface. But if one tries to look at growth rates on scales that are not small compared to characteristic lengths associated with curvature then one again sees exponential growth—just as in the case of a uniform tessellation without hexagons.

![](Images/_page_1065_Picture_2.jpeg)

![](Images/_page_1065_Picture_3.jpeg)

![](Images/_page_1065_Picture_4.jpeg)

![](Images/_page_1065_Picture_5.jpeg)

■ **Page 533 · Sphere volumes.** In ordinary flat Euclidean space the area of a 2D circle is  $\pi r^2$ , and the volume of a 3D sphere  $4 \pi r^3/3$ . In general, the volume of a sphere in d-dimensional Euclidean space is  $s[d]r^d$  where  $s[d] = \pi^{d/2}/(d/2)!$  (the surface area is  $ds[d]r^{d-1}$ ). (The function s[d] has a maximum around d = 5.26, then decreases rapidly with d.)

If instead of flat space one considers a space defined by the surface of a 3D sphere—say with radius a—one can ask about areas of circles in this space. Such circles are no longer flat, but instead are like caps on the sphere—with a circle of radius r containing all points that are geodesic (great circle) distance less than r from its center. Such a circle has area

 $2 \pi a^2 (1 - Cos[r/a]) = \pi r^2 (1 - r^2/(12a^2) + r^4/(360a^4) - ...)$  In the *d*-dimensional space corresponding to the surface of a (*d*+1)-dimensional sphere of radius *a*, the volume of a *d*-dimensional sphere of radius *r* is similarly given by

```
\begin{aligned} d\,s[d\,]\,a^d\,& \text{Integrate}[Sin[\theta\,]^{d-1},\,\{\theta,\,0,\,r/a\}] = \\ s[d\,]\,r^d\,\,(1-d\,(d-1)\,r^2/((6\,(d+2))\,a^2)\,+ \\ & (d\,(5\,d^2-12\,d+7))\,r^4/((360\,(d+4))\,a^4)\,+\ldots) \end{aligned}
```

where

Integrate[ $Sin[x]^{d-1}$ , x] = -Cos[x]Hypergeometric2F1[1/2, (2 - d)/2, 3/2,  $Cos[x]^2$ ]

In an arbitrary *d*-dimensional space the volume of a sphere can depend on position, but in general it is given by

```
s[d]r^d (1 - RicciScalar r^2/(6(d+2)) + ...)
```

where the Ricci scalar curvature is evaluated at the position of the sphere. (The space corresponding to a (d+1)-dimensional sphere has  $RicciScalar = d (d-1)/a^2$ .) The d=2 version of this formula was derived in 1848; the general case in 1917 and 1939. Various derivations can be given. One can

start from the fact that the volume density in any space is given in terms of the metric by *Sqrt[Det[g]]*. But in normal coordinates the first non-trivial term in the expansion of the metric is proportional to the Riemann tensor, yet the symmetry of a spherical volume makes it inevitable that the Ricci scalar is the only combination of components that can appear at lowest order. To next order the result is

```
s[d]r<sup>d</sup> (1 - RicciScalar r<sup>2</sup>/(6 (d + 2)) +
(5 RicciScalar<sup>2</sup> - 3 RiemannNorm + 8 RicciNorm -
18 Laplacian[RicciScalar])r<sup>4</sup>/(360 (d + 2) (d + 4)) + ...)
where the new quantities involved are
RicciNorm = Norm[RicciTensor, {g, g}]
RiemannNorm = Norm[Riemann, {g, g, g, Inverse[g]}]
Norm[t_, gl_] := Tr[Flatten[t Dual[t, gl]]]
Dual[t_, gl_] := Fold[Transpose[#1. Inverse[#2], RotateLeft[
Range[TensorRank[t]]]] &, t, Reverse[gl]]
Laplacian[f_] := Inner[D, Sqrt[Det[g]]
```

In general the series in r may not converge, but it is known that at least in most cases only flat space can give a result that shows no correction to the basic  $r^d$  form. It is also known that if the Ricci tensor is non-negative, then the volume never grows faster than  $r^d$ .

(Inverse[g] .  $Map[\partial_{\#}f \&, p]$ ), p]/Sqrt[Det[g]]

■ **Cylinder volumes.** In any d-dimensional space, the volume of a cylinder of length x and radius r whose direction is defined by a unit vector v turns out to be given by

 $s[d-1]r^{d-1}x$   $(1-(d-1)(RicciScalar - RicciTensor \cdot v \cdot v)r^2/(d+1) + ...)$ Note that what determines the volume of the cylinder is curvature orthogonal to its direction—and this is what leads

to the combination of Ricci scalar and tensor that appears.

■ Page 533 · Discrete spaces. Most work with surfaces done on computers—whether for computer graphics, computer-aided design, solving boundary value problems or otherwise—makes use of discrete approximations. Typically surfaces are represented by collections of patches—with a simple mesh of triangles often being used. The triangles are however normally specified not so much by their network of connections as by the explicit coordinates of their vertices. And while there are various triangulation methods that for example avoid triangles with small angles, no standard method yields networks analogous to the ones I consider in which all triangle edges are effectively the same length.

In pure mathematics a basic idea in topology has been to look for finite or discrete ways to capture essential features of continuous surfaces and spaces. And as an early part of this Henri Poincaré in the 1890s introduced the concept of approximating manifolds by cell complexes consisting of collections of generalized polyhedra. By the 1920s there was

then extensive work on so-called combinatorial topology, in which spaces are thought of as being decomposed into abstract complexes consisting say of triangles, tetrahedra and higher-dimensional simplices. But while explicit coordinates and lengths are not usually discussed, it is still imagined that one knows more information than in the networks I consider: not only how vertices are connected by edges, but also how edges are arranged around faces, faces around volumes, and so on. And while in 2D and 3D it is possible to set up such an approximation to any manifold in this way, it turns out that at least in 5D and above it is not. Before the 1960s it had been hoped that in accordance with the Hauptvermutung of combinatorial topology it would be possible to tell whether a continuous mapping and thus topological equivalence exists between manifolds just by seeing whether subdivisions of simplicial complexes for them could be identical. But in the 1960s it was discovered that at least in 5D and above this will not always work. And largely as a result of this, there has tended to be less interest in ideas like simplicial complexes.

And indeed a crucial point for my discussion in the main text is that in formulating general relativity one actually does not appear to need all the structure of a simplicial complex. In fact, the only features of manifolds that ultimately seem relevant are ones that in appropriate limits are determined just from the connectivity of networks. The details of the limits are mathematically somewhat intricate (compare page 1030), but the basic approach is straightforward. One can find the volume of a sphere (geodesic ball) in a network just by counting the number of nodes out to a given network distance from a certain node. And from the limiting growth rate of this one can immediately get the Ricci scalar curvature-just as in the continuous case discussed above. To get the Ricci tensor one also needs a direction. But one can get this from a geodesic-which is in effect the analog of a straight line in the network. Note that unlike in a continuous space there is however usually no obvious way to continue a geodesic in a network. And in general, some-but not all-of the standard constructions used in continuous spaces can also immediately be used in networks. So for example it is straightforward to construct a triangle in a network: one just starts from a particular node, follows geodesics to two others, then joins these with a geodesic. But to extend the triangle into a parallelogram is not so easy-since there is no immediate notion of parallelism in the network. And this means that neither the Riemann tensor, nor a so-called Schild ladder for parallel transport, can readily be constructed.

Since the 1980s there has been increasing interest in formulating notions of continuous geometry for objects like Cayley graphs of groups—which are fundamentally discrete but have infinite limits analogous to continuous systems. (Compare page 938.)

- Manifold undecidability. Given a particular set of network substitution rules there is in general no finite way to decide whether any sequence of such rules exists that will transform particular networks into each other. (Compare undecidability in multiway systems on page 779.) And although one might not expect it on the basis of traditional mathematical intuition, there is an analog of this even for topological equivalence of ordinary continuous manifolds. For the fundamental groups that represent how basic loops can be combined must be equivalent for equivalent manifolds. Yet it turns out that in 4D and above the fundamental group can have essentially any set of generators and relations—so that the undecidability of the word problem for arbitrary groups (see page 1141) implies undecidability of equivalence of manifolds. (In 2D it is straightforward to decide equivalence, and in 3D it is known that only some fundamental groups can be obtained—roughly because not all networks can be embedded in 2D-and it is expected that it will ultimately be possible to decide equivalence.)
- Non-integer dimensions. Unlike in traditional differential geometry (and general relativity) my formulation of space as a network potentially allows concepts like curvature to be defined even outside of integers numbers of dimensions.
- Page 534 · Lorentzian spaces. In ordinary Euclidean space distance is given by  $Sqrt[x^2 + y^2 + z^2]$ . In setting up relativity theory it is convenient (see page 1042) to define an analog of distance (so-called proper time) in 4D spacetime by  $Sqrt[c^2t^2-x^2-y^2-z^2]$ . And in terms of differential geometry such Minkowski space can be specified by the metric DiagonalMatrix[ $\{+1, -1, -1, -1\}$ ] (now taking c = 1). To set up general relativity one then considers not Riemannian manifolds but instead Lorentzian ones in which the metric is not positive definite, but instead has the signature of Minkowski space.

In such Lorentzian spaces, however, there is no useful immediate analog of a sphere. For given any point, even the light cone that corresponds to points at zero spacetime distance from it has an infinite volume. But with an appropriate definition one can still set up cones that have finite volume. To do this in general one starts by picking a vector e in a timelike direction, then normalizes it to be a unit vector so that e.g.e = -1. Then one defines a cone of height t whose apex is a given point to be those points whose displacement vector v satisfies 0 > e.g. v > -t (and 0 > v.g. v). And the volume of such a cone then turns out to be

 $s[d]t^{d+1}(1-t^2(d+1)(dRicciScalar+$ 2(d+1)(RicciTensor . e . e))/((d+2)(d+3)) + ...)/(d+1)

- Torsion. In standard geometry, one assumes that the distance from one point to another is the same as the distance back, so that the metric tensor can be taken to be symmetric, and there is zero so-called torsion. But in for example a causal network, connections have definite directions, and there is in general no such symmetry. And if one looks at the volume of a cone this can then introduce a correction proportional to r. But as soon as there is enough uniformity to define a reasonable notion of static space, it seems that this effect must vanish. (Note that in pure mathematics there are several different uses of the word "torsion". Here I use it to refer to the antisymmetric parts of the metric tensor.)
- Random causal networks. If one assumes that there are events at random positions in continuous spacetime, then one can construct an effective causal network for them by setting up connections between each event and all events in its future light cone-then deleting connections that are redundant in the sense that they just provide shortcuts to events that could otherwise be reached by following multiple connections. The pictures below show examples of causal networks obtained in this way. The number of connections generally increases faster than linearly with the number of events. Most links end up being at angles that are close to the edge of the light cone.

![](Images/_page_1067_Picture_6.jpeg)

![](Images/_page_1067_Picture_7.jpeg)

![](Images/_page_1067_Picture_8.jpeg)

■ Page 534 · Einstein equations. In the absence of matter, the standard statement of the Einstein equations is that all components of the Ricci tensor-and thus also the Ricci scalar—must be zero (or formally that  $R_{ii} = 0$ ). But since the vanishing of all components of a tensor must be independent of the coordinates used, it follows that the vacuum Einstein equations are equivalent to the statement RicciTensor. e.e = 0 for all timelike unit vectors e-astatement that can readily be applied to networks of the kind I consider in the main text. (A related statement is that the 3D Ricci scalar curvature of all spacelike hypersurfaces must vanish wherever these have vanishing extrinsic curvature.)

Another way to state the Einstein equations-already discussed by David Hilbert in 1915-is as the constraint that the integral of RicciScalar Sqrt[Det[g]] (the so-called Einstein-Hilbert action) be an extremum. (An idealized soap film or other minimal surface extremizes the integral of the intrinsic volume element Sqrt[Det[g]], without a RicciScalar factor.) In the discrete Regge calculus that I mention on page 1054 this variational principle turns out to have a rather simple form.

The Einstein-Hilbert action—and the Einstein equations can be viewed as having the simplest forms that do not ultimately depend on the choice of coordinates. Higher-order terms—say powers of the Ricci scalar curvature—could well arise from underlying network systems, but would not contribute noticeably except in very high gravitational fields.

Various physical interpretations can be given of the vanishing of the Ricci tensor implied by the ordinary vacuum Einstein equations. Closely related to my discussion of the absence of  $t^2$  terms in volume growth for 4D spacetime cones is the statement that if one sets up a small 3D ball of comoving test particles then the volume it defines must have zero first and second derivatives with time.

Below 4D the vanishing of the Ricci tensor immediately implies the vanishing of all components of the Riemann tensor-so that the vacuum Einstein equations force space at least locally to have its ordinary flat form. (Even in 2D there can nevertheless still be non-trivial global topology-for example with flat space having its edges identified as on a torus. In the Euclidean case there were for a long time no non-trivial solutions to the Einstein equations known in any number of dimensions, but in the 1970s examples were found, including large families of Calabi-Yau manifolds.)

In the presence of matter, the typical formal statement of the full Einstein equations is  $R_{\mu\nu}$  -  $Rg_{\mu\nu}/2 = 8\pi G T_{\mu\nu}/c^4$ , where  $T_{\mu\nu}$  is the energy-momentum (stress-energy) tensor for matter and G is the gravitational constant. (An additional socalled cosmological term  $\lambda g_{\mu\nu}$  is sometimes added on the right to adjust the effective overall energy density of the universe, and thus its expansion rate. Note that the equation can also be written  $R_{\mu\nu} = 8 \pi G (T_{\mu\nu} - 1/2 T^{\mu}_{\mu} g_{\mu\nu})/c^4$ .) The  $\mu$ ,  $\nu$  component of  $T_{\mu\nu}$  gives the flux of the  $\mu$  component of 4-momentum (whose components are energy and ordinary 3momentum) in the  $\nu$  direction. The fact that  $T_{00}$  is energy density implies that for static matter (where  $E = mc^2$ ) the equation is in a sense a minimal extension of Poisson's equation of Newtonian gravity theory. Note that conservation of energy and momentum implies that  $T_{\mu\nu}$ must have zero divergence-a result guaranteed in the Einstein equations by the structure of the left-hand side.

In the variational approach to gravity mentioned above, the RicciScalar plays the role of a Lagrangian density for pure gravity-and in the presence of matter the Lagrangian density for matter must be added to it. At a physical level, the full Einstein equations can be interpreted as saying that the volume v of a small ball of comoving test particles satisfies

$$\partial_{tt} v[t]/v[t] = -1/2(\rho + 3p)$$

where  $\rho$  is the total energy density and  $\rho$  is the pressure averaged over all space directions.

To solve the full Einstein equations in any particular physical situation requires a knowledge of Tuy-and thus of properties of matter such as the relation between pressure and energy density (equation of state). Quite a few global results about the formation of singularities and the absence of paths looping around in time can nevertheless be obtained just by assuming certain so-called energy conditions for  $T_{mv}$ . (A fairly stringent example is  $0 \le p \le \rho/3$ —and whether this is actually true for non-trivial interacting quantum fields remains unclear.)

In their usual formulation, the Einstein equations are thought of as defining constraints on the structure of 4D spacetime. But at some level they can also be viewed as defining how 3D space evolves with time. And indeed the so-called initial value formulations constructed in the 1960s allow one to start with a 3D metric and various extrinsic curvatures defined for a 3D spacelike hypersurface, and then work out how these change on successive hypersurfaces. But at least in terms of tensors, the equations involved show nothing like the simplicity of the usual 4D Einstein equations. One can potentially view the causal networks that I discuss in the main text as providing another approach to setting up an initial value formulation of the Einstein equations.

■ Page 536 · Pure gravity. In the absence of matter, the Einstein equations always admit ordinary flat Minkowski space as a solution. But they also admit other solutions that in effect represent configurations of pure gravitational field. And in fact the 4D vacuum Einstein equations are already a sophisticated set of nonlinear partial differential equations that can support all sorts of complex behavior. Several tens of families of solutions to the equations have been found—some with obvious physical interpretations, others without.

Already in 1916 Karl Schwarzschild gave the solution for a spherically symmetric gravitational field. He imagined that this field itself existed in a vacuum—but that it was produced by a mass such as a star at its center. In its original form the metric becomes singular at radius  $2 G m/c^2$  (or 3 m km with m in solar masses). At first it was assumed that this would always be inside a star, where the vacuum Einstein equations would not apply. But in the 1930s it was suggested that stars could collapse to concentrate their mass in a smaller radius. The singularity was then interpreted as an event horizon that separates the interior of a black hole from the ordinary space around it. In 1960 it was realized, however, that appropriate coordinates allowed smooth continuation across the event horizon-and that the only genuine singularity was infinite curvature at a single point at the center. Sometimes it was said that this must reflect the presence of a point mass, but soon it was typically just said to be a point at which the Einstein equations—for whatever reason—do not apply. Different choices of coordinates led to different apparent locations and forms of the singularity, and by the late 1970s the most common representation was just a smooth manifold with a topology reflecting the removal of a point-and without any specific reference to the presence of matter.

Appealing to ideas of Ernst Mach from the late 1800s it has often been assumed that to get curvature in space always eventually requires the presence of matter. But in fact even the vacuum Einstein equations for complete universes (with no points left out) have solutions that show curvature. If one assumes that space is both homogeneous and isotropic then it turns out that only ordinary flat Minkowski space is allowed. (When matter or a cosmological term is present one gets different solutions—that always expand or contract, and are much studied in cosmology.) If anisotropy is present, however, then there can be all sorts of solutionsclassified for example as having different Bianchi symmetry types. And a variety of inhomogeneous solutions with no singularities are also known—an example being the 1962 Ozsváth-Schücking rotating vacuum. But in all cases the structure is too simple to capture much that seems relevant for our present universe.

One form of solution to the vacuum Einstein equations is a gravitational wave consisting of a small perturbation propagating through flat space. No solutions have vet been found that represent complete universes containing emitters and absorbers of such waves (or even for example just two massive bodies). But it is known that combinations of gravitational waves can be set up that will for example evolve to generate singularities. And I suspect that nonlinear interactions between such waves will also inevitably lead to the analog of turbulence for pure gravity. (Numerical simulations often show all sorts of complex behavior—but in the past this has normally been attributed just to the approximations used. Note that for example Bianchi type IX solutions for a complete universe show sensitive dependence on initial conditions-and no doubt this can also happen with nonlinear gravitational waves.)

As mentioned on page 1028, Albert Einstein considered the possibility that particles of matter might somehow just be localized structures in gravitational and electromagnetic fields. And in the mid-1950s John Wheeler studied explicit simple examples of such so-called geons. But in all cases they were found to be unstable—decaying into ordinary gravitational waves. The idea of having purely gravitational localized structures has also occasionally been considered—but so far no stable field configuration has been found. (And no purely repetitive solutions can exist.)

The equivalence principle (see page 1047) might suggest that anything with mass-or energy-should affect the curvature of space in the same way. But in the Einstein equations the energy-momentum tensor is not supposed to include contributions from the gravitational field. (There are alternative and seemingly inelegant theories of gravity that work differently-and notably do not yield black holes. The setup is also somewhat different in recent versions of string theory.) The very definition of energy for the gravitational field is not particularly straightforward in general relativity. But perhaps a definition could be found that would allow localized structures in the gravitational field to make effective contributions to the energy-momentum tensor that would mimic those from explicit particles of matter. Nevertheless, there are quite a few phenomena associated with particles that seem difficult to reproduce with pure gravity—at least say without extra dimensions. One example is parity violation; another is the presence of long-range forces other than gravity.

• Quantum gravity. That there should be quantum effects in gravity was already noted in the 1910s, and when quantum field theory began to develop in the 1930s, there were immediately attempts to apply it to gravity. The first idea was to represent gravity as a field that exists in flat spacetime, and by analogy with photons in quantum electrodynamics to introduce gravitons (at one point identified with neutrinos). By the mid-1950s a path integral (see page 1061) based on the Einstein-Hilbert action had been constructed, and by the early 1960s Feynman diagram rules had been derived, and it had been verified that tree diagrams involving gravitons gave results that agreed with general relativity for small gravitational fields. But as soon as loop diagrams were considered, infinities began to appear. And unlike for quantum electrodynamics there did not seem to be only a finite number of these-that could be removed by renormalization. And in fact by 1973 gravity coupled to matter had been shown for certain not to be renormalizableand the same was finally shown for pure gravity in 1986. There was an attempt in the 1970s and early 1980s to look directly at the path integral—without doing an expansion in terms of Feynman diagrams. But despite the fact that at least in Euclidean spacetime a variety of seemingly relevant field configurations were identified, many mathematical difficulties were encountered. And in the late-1970s there began to be interest in the idea that supersymmetric field theories might make infinities associated with gravitons be cancelled by ones associated with other particles. But in the end this did not work out. And then in the mid-1980s one of the great attractions of string theory was that it seemed to support graviton excitations without the problem of infinities seen in point-particle field theories. But it had other problems, and to avoid these, supersymmetry had to be introduced, leading to the presence of many other particles that have so far not been observed. (See also page 1029.)

Starting in the 1950s a rather different approach to quantum gravity involved trying to find a representation of the structure of spacetime in which a quantum analog of the Einstein equations could be obtained by the formal procedure of canonical quantization (see page 1058). Yet despite a few signs of progress in the 1960s there was great difficulty in finding appropriately independent variables to use. In the late 1980s, however, it was suggested that variables could be used corresponding roughly to gravitational fluxes through loops in space. And in terms of these loop variables it was at least formally possible to write down a version of quantum gravity. Yet while this was found in the 1990s to have a correspondence with spin networks (see below), it has remained impossible to see just how it might yield ordinary general relativity as a limit.

Even if one assumes that spacetime is in a sense ultimately continuous one can imagine investigating quantum gravity by doing some kind of discrete approximation. And in 1961 Tullio Regge noted that for a simplicial complex (see page 1050) the Einstein-Hilbert action has a rather simple form in terms of angles between edges. Starting in the 1980s after the development of lattice gauge theories, simulations of random surfaces and higher-dimensional spaces set up in this way were done-often using so-called dynamic triangulation based on random sequences of generalized Alexander moves from page 1038. But there were difficulties with Lorentzian spaces, and when large-scale average behavior was studied, it seemed difficult to reproduce observed smooth spacetime. Analytical approaches (that happened to be like 0D string theory) were also found for 2D discrete spacetimes (compare page 1038)—but they were not successfully extended to higher dimensions.

Over the years, various attempts have been made to derive quantum gravity from fundamentally discrete models of spacetime (compare page 1027). In recent times the most widely discussed have been spin networks-which despite their name ultimately seem to have fairly little to do with the systems I consider. Spin networks were introduced in 1964 by Roger Penrose as a way to set up an intrinsically quantum mechanical model of spacetime. A simple analog involves a 2D surface made out of triangles whose edges have integer lengths  $j_i$ . If one computes the product of  $Exp[i(j_1 + j_2 - j_3)]$  for all triangles, then it turns out for example that this quantity is extremized exactly when the whole surface is flat. In 3D one imagines breaking space into tetrahedra whose edge lengths correspond to discrete quantum spin values. And in 1968 Tullio Regge and Giorgio Ponzano suggested-almost as an afterthought in technical work on 6 j symbols—that the quantum probability amplitude for any form of space might perhaps be given by the product of 6 j symbols for the spins on each tetrahedron. The  $SixJSymbol[\{j_1, j_2, j_3\}, \{j_4, j_5, j_6\}]$  are slightly esoteric objects that correspond to recoupling coefficients for the 3D rotation group SO(3), and that arose in 1940s studies of combinations of three angular momenta in atomic physics and were often represented graphically as networks. For large j, they are approximated by  $Cos[\theta + \pi/4]/Sqrt[12 \pi v]$ , where v is the volume of the tetrahedron and  $\theta$  is a deficit angle. And from this it turns out that limits of products of 6j symbols correspond essentially to Exp[is], where s is the discrete form of the Einstein-Hilbert action-extremized by flat 3D space. (The picture below shows for example Abs[SixJSymbol[ $\{j, j, j\}, \{j, j, j\}$ ]]. Note that for any j the 6jsymbols can be given in terms of HypergeometricPFQ.)

![](Images/_page_1070_Figure_3.jpeg)

In the early 1990s there was again interest in spin networks when the Turaev-Viro invariant for 3D spaces was discovered from a topological field theory involving triangulations weighted with 6 j symbols of the quantum group SU(2),and it was seen that invariance under Alexander moves on the triangulation corresponded to the Biedenharn-Elliott identity for 6 j symbols. In the mid-1990s it was then found that states in 3D loop quantum gravity (see above) could be represented in terms of spin networks—leading for example to quantization of all areas and volumes. In attempting extensions to 4D, spin foams have been introduced-and variously interpreted in terms of simplified Feynman diagrams, constructs in multidimensional category theory, and possible evolutions of spin networks. In all cases, however, spin networks and spin foams seem to be viewed

just as calculational constructs that must be evaluated and added together to get quantum amplitudes-quite different from my idea of associating an explicit evolution history for the universe with the evolution of a network.

 Cosmology. On a large scale our universe appears to show a uniform expansion that makes progressively more distant galaxies recede from us at progressively higher speeds. In general relativity this is explained by saying that the initial conditions must have involved expansion-and that there is not enough in the way of matter or gravitational fields to produce the gravity to slow down this expansion too much. (Note that as soon as objects get gravitationally bound—like galaxies in clusters-there is no longer expansion between them.) The standard big bang model assumes that the universe starts with matter at what is in effect an arbitrarily high temperature. One issue much discussed in cosmology since the late 1970s is how the universe manages to be so uniform. Thermal equilibrium should eventually lead to uniformity but different parts of the universe cannot come to equilibrium until there has at least been time for effects to propagate between them. Yet there seems for example to be overall uniformity in what we see if we look in opposite directions in the sky-even though extrapolating from the current rate of expansion there has not been enough time since the beginning of the universe for anything to propagate from one side to the other. But starting in the early 1980s it has been popular to think that early in its history the universe must have undergone a period of exponential expansion or so-called inflation. And what this would do is to take just a tiny region and make it large enough to correspond to everything we can now see in the universe. But the point is that a sufficiently tiny region will have had time to come to thermal equilibriumand so will be approximately uniform, just as the cosmic microwave background is now observed to be. The actual process of inflation is usually assumed to reflect some form of phase transition associated with decreasing temperature of matter in the universe. Most often it is assumed that in the present universe a delicate balance must exist between energy density from a background Higgs field (see page 1047) and a cosmological term in the Einstein equations (see page 1052). But above a critical temperature thermal fluctuations should prevent the background from forming-leading to at least some period in which the universe is dominated by a cosmological term which yields exponential expansion. There tend to be various detailed problems with this scenario, but at least with a sufficiently complicated setup it seems possible to get results that are consistent with observations made so far.

In the context of the discoveries in this book, my expectation is that the universe started from a simple small network, then

progressively added more and more nodes as it evolved, until eventually on a large scale something corresponding to 4D spacetime emerged. And with this setup, the observed uniformity of the universe becomes much less surprising. Intrinsic randomness generation always tends to lead to a certain uniformity in networks. But the crucial point is that this will not take long to happen throughout any network if it is appropriately connected. Traditional models tend to assume that there are ultimately a fixed number of spacetime dimensions in the universe. And with this assumption it is inevitable that if the universe in a sense expands at the speed of light, then regions on opposite sides of it can essentially never share any common history. But in a network model the situation is different. The causal network always captures what happens. And in a case like page 518—with spacetime always effectively having a fixed finite dimension-points that are a distance t apart tend to have common ancestors only at least t steps back. But in a case like (a) on page 514 where spacetime has the structure of an exponentially growing tree—points a distance t apart typically have common ancestors just Log[t] steps back. And in fact many kinds of causal networks-say associated with early randomly connected space networks-will inevitably yield common ancestors for distant parts of the universe. (Note that such phenomena presumably occur at around the Planck scale of 1019 GeV rather than at the 1015 GeV or lower scale normally discussed in connection with inflation. They can to some extent be captured in general relativity by imagining an effective spacetime dimension that is initially infinite, then gradually decreases to 4.)

#### **Quantum Phenomena**

• History. In classical physics quantities like energy were always assumed to correspond to continuous variables. But in 1900 Max Planck noticed that fits to the measured spectrum of electromagnetic radiation produced by hot objects could be explained if there were discrete quanta of electromagnetic energy. And by 1910 work by Albert Einstein, notably on the photoelectric effect and on heat capacities of solids, had given evidence for discrete quanta of energy in both light and matter. In 1913 Niels Bohr then made the suggestion that the discrete spectrum of light emitted by hydrogen atoms could be explained as being produced by electrons making transitions between orbits with discrete quantized angular momenta. By 1920 ideas from celestial mechanics had been used to develop a formalism for quantized orbits which successfully explained various features of atoms and chemical elements. But it was not clear how to extend the formalism say to a problem like propagation of light through a crystal. In 1925, however, Werner Heisenberg suggested a new and more general formalism that became known as matrix mechanics. The original idea was to imagine describing the state of an atom in terms of an array of amplitudes for virtual oscillators with each possible frequency. Particular conditions amounting to quantization were then imposed on matrices of transitions between these, and the idea was introduced that only certain kinds of amplitude combinations could ever be observed. In 1923 Louis de Broglie had suggested that just as light—which in optics was traditionally described in terms of wavesseemed in some respects to act like discrete particles, so conversely particles like electrons might in some respects act like waves. In 1926 Erwin Schrödinger then suggested a partial differential equation for the wave functions of particles like electrons. And when effectively restricted to a finite region, this equation allowed only certain modes, corresponding to discrete quantum states—whose properties turned out to be exactly the same as implied by matrix mechanics. In the late 1920s Paul Dirac developed a more abstract operator-based formalism. And by the end of the 1920s basic practical quantum mechanics was established in more or less the form it appears in textbooks today. In the period since, increasing computational capabilities have allowed coupled Schrödinger equations for progressively more particles to be solved (reasonably accurate solutions for hundreds of particles can now be found), allowing ever larger studies in atomic, molecular, nuclear and solid-state physics. A notable theoretical interest starting in the 1980s was so-called quantum chaos, in which it was found that modes (wave functions) in regions like stadiums that did not yield simple analytical solutions tended to show complicated and seemingly random forms.

Basic quantum mechanics is set up to describe how fixed numbers of particles behave-say in externally applied electromagnetic or other fields. But to describe things like fields one must allow particles to be created and destroyed. In the mid-1920s there was already discussion of how to set up a formalism for this, with an underlying idea again being to think in terms of virtual oscillators—but now one for each possible state of each possible one of any number of particles. At first this was just applied to a pure electromagnetic field of non-interacting photons, but by the end of the 1920s there was a version of quantum electrodynamics (QED) for interacting photons and electrons that is essentially the same as today. To find predictions from this theory a so-called perturbation expansion was made, with successive terms representing progressively more interactions, and each having a higher power of the so-called coupling constant  $\alpha \simeq 1/137$ . It was immediately noticed, however, that selfinteractions of particles would give rise to infinities, much as in classical electromagnetism. At first attempts were made to avoid this by modifying the basic theory (see page 1044). But by the mid-1940s detailed calculations were being done in which infinite parts were just being dropped—and the results were being found to agree rather precisely with experiments. In the late 1940s this procedure was then essentially justified by the idea of renormalization: that since in all possible QED processes only three different infinities can ever appear, these can in effect systematically be factored out from all predictions of the theory. Then in 1949 Feynman diagrams were introduced (see note below) to represent terms in the QED perturbation expansion—and the rules for these rapidly became what defined QED in essentially all practical applications. Evaluating Feynman diagrams involved extensive algebra, and indeed stimulated the development of computer algebra (including my own interest in the field). But by the 1970s the dozen or so standard processes discussed in OED had been calculated to order  $\alpha^2$ —and by the mid-1980s the anomalous magnetic moment of the electron had been calculated to order  $\alpha^4$ , and nearly one part in a trillion (see note below).

But despite the success of perturbation theory in QED it did not at first seem applicable to other issues in particle physics. The weak interactions involved in radioactive beta decay seemed too weak for anything beyond lowest order to be relevant—and in any case not renormalizable. And the strong interactions responsible for holding nuclei together (and associated for example with exchange of pions and other mesons) seemed too strong for it to make sense to do an expansion with larger numbers of individual interactions treated as less important. So this led in the 1960s to attempts to base theories just on setting up simple mathematical constraints on the overall so-called S matrix defining the mapping from incoming to outgoing quantum states. But by the end of the 1960s theoretical progress seemed blocked by basic questions about functions of several complex variables, and predictions that were made did not seem to work well.

By the early 1970s, however, there was increasing interest in so-called gauge or Yang-Mills theories formed in essence by generalizing QED to operate not just with a scalar charge, but with charges viewed as elements of non-Abelian groups. In 1972 it was shown that spontaneously broken gauge theories of the kind needed to describe weak interactions were renormalizable-allowing meaningful use of perturbation theory and Feynman diagrams. And then in 1973 it was discovered that QCD-the gauge theory for quarks and

gluons with SU(3) color charges—was asymptotically free (it was known to be renormalizable), so that for processes probing sufficiently small distances, its effective coupling was small enough for perturbation theory. By the early 1980s first-order calculations of most basic QCD processes had been done-and by the 1990s second-order corrections were also known. Schemes for adding up all Feynman diagrams with certain very simple repetitive or other structures were developed. But despite a few results about large-distance analogs of renormalizability, the question of what QCD might imply for processes at larger distances could not really be addressed by such methods.

In 1941 Richard Feynman pointed out that amplitudes in quantum theory could be worked out by using path integrals that sum with appropriate weights contributions from all possible histories of a system. (The Schrödinger equation is like a diffusion equation in imaginary time, so the path integral for it can be thought of as like an enumeration of random walks. The idea of describing random walks with path integrals was discussed from the early 1900s.) At first the path integral was viewed mostly as a curiosity, but by the late 1970s it was emerging as the standard way to define a quantum field theory. Attempts were made to see if the path integral for QCD (and later for quantum gravity) could be approximated with a few exact solutions (such as instantons) to classical field equations. By the early 1980s there was then extensive work on lattice gauge theories in which the path integral (in Euclidean space) was approximated by randomly sampling discretized field configurations. But-I suspect for reasons that I discuss in the note below-such methods were never extremely successful. And the result is that beyond perturbation theory there is still no real example of a definitive success from standard relativistic quantum field theory. (In addition, even efforts in the context of so-called axiomatic field theory to set up mathematically rigorous formulations have run into many difficulties—with the only examples satisfying all proposed axioms typically in the end being field theories without any real interactions. In condensed matter physics there are nevertheless cases like the Kondo model where exact solutions have been found, and where the effective energy function for electrons happens to be roughly the same as in a relativistic theory.)

As mentioned on page 1044, ordinary quantum field theory in effect deals only with point particles. And indeed a recurring issue in it has been difficulty with constraints and redundant degrees of freedom-such as those associated with extended objects. (A typical goal is to find variables in which one can carry out what is known as canonical quantization: essentially applying the same straightforward transformation of equations that happens to work in ordinary elementary quantum mechanics.) One feature of string theory and its generalizations is that they define presumably consistent quantum field theories for excitations of extended objects—though an analog of quantum field theory in which whole strings can be created and destroyed has not yet been developed.

When the formalism of quantum mechanics was developed in the mid-1920s there were immediately questions about its interpretation. But it was quickly suggested that given a wave function  $\psi$  from the Schrödinger equation  $Abs[\psi]^2$ should represent probability—and essentially all practical applications have been based on this ever since. From a conceptual point of view it has however often seemed peculiar that a supposedly fundamental theory should talk only about probabilities. Following the introduction of the uncertainty principle and related formalism in the 1920s one idea that arose was that—in rough analogy to relativity theory—it might just be that there are only certain quantities that are observable in definite ways. But this was not enough, and by the 1930s it was being suggested that the validity of quantum mechanics might be a sign that whole new general frameworks for philosophy or logic were needed—a notion supported by the apparent need to bring consciousness into discussions about measurement in quantum mechanics (see page 1063). The peculiar character of quantum mechanics was again emphasized by the idealized experiment of Albert Einstein, Boris Podolsky and Nathan Rosen in 1935. But among most physicists the apparent lack of an ordinary mechanistic way to think about quantum mechanics ended up just being seen as another piece of evidence for the fundamental role of mathematical formalism in physics.

One way for probabilities to appear even in deterministic systems is for there to be hidden variables whose values are unknown. But following mathematical work in the early 1930s it was usually assumed that this could not be what was going on in quantum mechanics. In 1952 David Bohm did however manage to construct a somewhat elaborate model based on hidden variables that gave the same results as ordinary quantum mechanics-though involved infinitely fast propagation of information. In the early 1960s John Bell then showed that in any hidden variables theory of a certain general type there are specific inequalities that combinations of probabilities must satisfy (see page 1064). And by the early 1980s experiments had shown that such inequalities were indeed violated in practice-so that there were in fact correlations of the kind suggested by quantum mechanics. At first these just seemed like isolated esoteric effects, but by the mid-1990s they were being codified in the field of quantum information theory, and led to constructions with names like quantum cryptography and quantum teleportation.

Particularly when viewed in terms of path integrals the standard formalism of quantum theory tends to suggest that quantum systems somehow do more computation in their evolution than classical ones. And after occasional discussion as early as the 1950s, this led by the late 1980s to extensive investigation of systems that could be viewed as quantum analogs of idealized computers. In the mid-1990s efficient procedures for integer factoring and a few other problems were suggested for such systems, and by the late 1990s small experiments on these were beginning to be done in various types of physical systems. But it is becoming increasingly unclear just how the idealizations in the underlying model really work, and to what extent quantum mechanics is actually in the end even required—as opposed, say, just to classical wave phenomena. (See page 1147.)

Partly as a result of discussions about measurement there began to be questions in the 1980s about whether ordinary quantum mechanics can describe systems containing very large numbers of particles. Experiments in the 1980s and 1990s on such phenomena as macroscopic superposition and Bose-Einstein condensation nevertheless showed that standard quantum effects still occur with trillions of atoms. But inevitably the kinds of general phenomena that I discuss in this book will also occur—leading to all sorts of behavior that at least cannot readily be foreseen just from the basic rules of quantum mechanics.

- **Quantum effects.** Over the years, many suggested effects have been thought to be characteristic of quantum systems:
  - Basic quantization (1913): mechanical properties of particles in effectively bounded systems are discrete;
  - Wave-particle duality (1923): objects like electrons and photons can be described as either waves or particles;
  - Spin (1925): particles can have intrinsic angular momentum even if they are of zero size;
- Non-commuting measurements (1926): one can get different results doing measurements in different orders;
- Complex amplitudes (1926): processes are described by complex probability amplitudes;
- Probabilism (1926): outcomes are random, though probabilities for them can be computed;
- Amplitude superposition (1926): there is a linear superposition principle for probability amplitudes;
- State superposition (1926): quantum systems can occur in superpositions of measurable states;

- Exclusion principle (1926): amplitudes cancel for fermions like electrons to go in the same state;
- Interference (1927): probability amplitudes for particles can interfere, potentially destructively;
- Uncertainty principle (1927): quantities like position and momenta have related measurement uncertainties;
- Hilbert space (1927): states of systems are represented by vectors of amplitudes rather than individual variables;
- Field quantization (1927): only discrete numbers of any particular kind of particle can in effect ever exist;
- Quantum tunnelling (1928): particles have amplitudes to go where no classical motion would take them;
- Virtual particles (1932): particles can occur for short times without their usual energy-momentum relation;
- Spinors (1930s): fermions show rotational invariance under SU(2) rather than SO(3);
- Entanglement (1935): separated parts of a system often inevitably behave in irreducibly correlated ways;
- Quantum logic (1936): relations between events do not follow ordinary laws of logic;
- Path integrals (1941): probabilities for behavior are obtained by summing contributions from many paths;
- Imaginary time (1947): statistical mechanics is like quantum mechanics in imaginary time;
- Vacuum fluctuations (1948): there are continual random field fluctuations even in the vacuum;
- Aharanov-Bohm effect (1959): magnetic fields can affect particles even in regions where they have zero strength;
- Bell's inequalities (1964): correlations between events can be larger than in any ordinary probabilistic system;
- Anomalies (1969): virtual particles can have effects that violate the original symmetries of a system;
- Delayed choice experiments (1978): whether particle or wave features are seen can be determined after an event;
- Quantum computing (1980s): there is the potential for fundamental parallelism in computations.

All of these effects are implied by the standard mathematical formalism of quantum theory. But it has never been entirely clear which of them are in a sense true defining features of quantum phenomena, and which are somehow just details. It does not help that most of the effects—at least individually can be reproduced by mechanisms that seem to have little to do with the usual structure of quantum theory. So for example there will tend to be quantization whenever the underlying elements of a system are discrete. Similarly, features like the uncertainty principle and path integrals tend to be seen whenever things like waves are involved. And probabilistic effects can arise from any of the mechanisms for randomness discussed in Chapter 7. Complex amplitudes can be thought of just as vector quantities. And it is straightforward to set up rules that will for example reproduce the detailed evolution of amplitudes according say to the Schrödinger equation (see note below). It is somewhat more difficult to set up a system in which such amplitudes will somehow directly determine probabilities. And indeed in recent times consequences of this-such as violations of Bell's inequalities—are what have probably most often been quoted as the most unique features of quantum systems. It is however notable that the vast majority of traditional applications of quantum theory do not seem to have anything to do with such effects. And in fact I do not consider it at all clear just what is really essential about them, and what is in the end just a consequence of the extreme limits that seem to need to be taken to get explicit versions of them.

- Reproducing quantum phenomena. Given dynamics it is much easier to see how to reproduce fluid mechanics than rigid-body mechanics-since to get rigid bodies with only a few degrees of freedom requires taking all sorts of limits of correlations between underlying molecules. And I strongly suspect that given a discrete underlying model of the type I discuss here it will similarly be much easier to reproduce quantum field theory than ordinary quantum mechanics. And indeed even with traditional formalism, it is usually difficult to see how quantum mechanics can be obtained as a limit of quantum field theory. (Classical limits are slightly easier: they tend to be associated with stationary features or caustics that occur at large quantum numbers-or coherent states that represent eigenstates of raising or particle creation operators. Note that the exclusion principle makes classical limits for fermions difficult—but crucial for the stability of bulk matter.)
- **Discrete quantum mechanics.** While there are many issues in finding a complete underlying discrete model for quantum phenomena, it is quite straightforward to set up continuous cellular automata whose limiting behavior reproduces the evolution of probability amplitudes in standard quantum mechanics. One starts by assigning a continuous complex number value to each cell. Then given the list of such values the crucial constraint imposed by the standard formalism of quantum mechanics is unitarity: that the quantity Tr[Abs[list]<sup>2</sup>] representing total probability should be conserved. This is in a sense analogous to conservation of total density in diffusion processes. From

the discussion of page 1024 one can reproduce the 1D diffusion equation with a continuous block cellular automaton in which the new value of each block is given by  $\{\{1-\xi, \xi\}, \{\xi, 1-\xi\}\}, \{a_1, a_2\}$ . So in the case of quantum mechanics one can consider having each new block be given by  $\{\{Cos[\theta], iSin[\theta]\}, \{iSin[\theta], Cos[\theta]\}\}, \{a_1, a_2\}$ . The pictures below show examples of behavior obtained with this rule. (Gray levels represent magnitude for each cell, and arrows phase.) And it turns out that in suitable limits one generally gets essentially the behavior expected from either the Dirac or Klein-Gordon equations for relativistic particles, or the Schrödinger equation for non-relativistic particles. (Versions of this were noticed by Richard Feynman in the 1940s in connection with his development of path integrals, and were pointed out again several times in the 1980s and 1990s.)

![](Images/_page_1075_Picture_3.jpeg)

One might hope to be able to get an ordinary cellular automaton with a limited set of possible values by choosing a suitable  $\theta$ . But in fact in non-trivial cases most of the cells generated at each step end up having distinct values. One can generalize the setup to more dimensions or to allow  $n \times n$ matrices that are elements of SU(n). Such matrices can be viewed in the context of ordinary quantum formalism as S matrices for elementary evolution events—and can in general represent interactions. (Note that all rules based on matrices are additive, reflecting the usual assumption of linearity at the level of amplitudes in quantum mechanics. Non-additive unitary rules can also be found. The analog of an external potential can be introduced by progressively changing values of certain cells at each step. Despite their basic setup the systems discussed here are not direct analogs of standard quantum spin systems, since these normally have local Hamiltonians and non-local evolution functions, while the systems here have local evolution functions but seem always to require non-local Hamiltonians.)

■ Page 540 · Feynman diagrams. The pictures below show a typical set of Feynman diagrams used to do calculations in QED-in this case for so-called Compton scattering of a photon by an electron. The straight lines in the diagrams represent electrons; the wavy ones photons. At some level each diagram can be thought of as representing a process in which an electron and photon come in from the left, interact in some way, then go out to the right. The incoming and outgoing lines correspond to real particles that propagate to infinity. The lines inside each diagram correspond to virtual particles that in effect propagate only a limited distance, and have a distribution of energy-momentum and polarization properties that can differ from real particles. (Exchanges of virtual photons can be thought of as producing familiar electromagnetic forces; exchanges of virtual electrons as yielding an analog of covalent forces in chemistry.)

![](Images/_page_1075_Picture_7.jpeg)

To work out the total probability for a process from Feynman diagrams, what one does is to find the expression corresponding to each diagram, then one adds these up, and squares the result. The first two blocks of pictures above show all the diagrams for Compton scattering that involve 2 or 3 photons—and contribute through order  $\alpha^3$ . Since for QED  $\alpha \simeq 1/137$ , one might expect that this would give quite an accurate result-and indeed experiments suggest that it does. But the number of diagrams grows rapidly with order, and in fact the  $k^{th}$  order term can be about  $(-1)^k \alpha^k (k/2)!$ , yielding a series that formally diverges. In simpler examples where exact results are known, however, the first few terms typically still seem to give numerically accurate results for small  $\alpha$ . (The high-order terms often seem to be associated with asymptotic series for things like  $Exp[-1/\alpha]$ .)

The most extensive calculation made so far in QED is for the magnetic moment of the electron. Ignoring parts that depend on particle masses the result (derived in successive orders from 1, 1, 7, 72, 891 diagrams) is

```
2(1 + \alpha/(2\pi) + (3 Zeta[3]/4 - 1/2\pi^2 Log[2] + \pi^2/12 +
      197/144)(\alpha/\pi)^2 + (83/72 \pi^2 Zeta[3] - 215 Zeta[5]/24 -
      239 \pi^4 / 2160 + 139 Zeta[3] / 18 + 25 / 18 (24 PolyLog[
        4, 1/2] + Log[2]<sup>4</sup> - \pi^2 Log[2]<sup>2</sup>) - 298/9 \pi^2 Log[2] +
      17101 \pi^2 / 810 + 28259 / 5184) (\alpha / \pi)^3 - 1.4 (\alpha / \pi)^4 + ...)
or roughly
```

 $2. + 0.32 \alpha - 0.067 \alpha^2 + 0.076 \alpha^3 - 0.029 \alpha^4 + ...$ 

The comparative simplicity of the symbolic forms here (which might get still simpler in terms of suitable generalized polylogarithm functions) may be a hint that methods much more efficient than explicit Feynman diagram evaluation could be used. But it seems likely that there would be limits to this, and that in the end QED will exhibit the kind of computational irreducibility that I discuss in Chapter 12.

Feynman diagrams in QCD work at the formal level very much like those in QED-except that there are usually many more of them, and their numerical results tend to be larger, with expansion parameters often effectively being  $\alpha \pi$  rather than  $\alpha/\pi$ . For processes with large characteristic momentum transfers in which the effective  $\alpha$  in QCD is small, remarkably accurate results are obtained with first and perhaps second-order Feynman diagrams. But as soon as the effective  $\alpha$  becomes larger, Feynman diagrams as such rapidly seem to stop being useful.

 Quantum field theory. In standard approaches to quantum field theory one tends to think of particles as some kind of small perturbations in a field. Normally for calculations these perturbations are on their own taken to be plane waves of definite frequency, and indeed in many ways they are direct analogs of waves in classical field theories like those of electromagnetism or fluid mechanics. To investigate collisions between particles, one thus looks at what happens with multiple waves. In a system described by linear equations, there is always a simple superposition principle, and waves just pass through each other unchanged. But what in effect leads to non-trivial interactions between particles is the presence of nonlinearities. If these are small enough then it makes sense to do a perturbation expansion in which one approximates field configurations in terms of a succession of arrangements of ordinary waves—as in Feynman diagrams. But just as one cannot expect to capture fully turbulent fluid flow in terms of a few simple waves, so in general as soon as there is substantial nonlinearity it will no longer be sufficient just to do perturbation expansions. And indeed for example in QCD there are presumably many cases in which it is necessary to look at something closer to actual complete field configurations—and correlations in them.

The way the path integral for a quantum field theory works, each possible configuration of the field is in effect taken to make a contribution  $Exp[is/\hbar]$ , where s is the so-called action for the field configuration (given by the integral of the Lagrangian density—essentially a modified energy density), and  $\hbar$  is a basic scale factor for quantum effects (Planck's constant divided by  $2\pi$ ). In most places in the space of all possible field configurations, the value of s will vary quite quickly between nearby configurations. And assuming this variation is somehow random, the contributions of these nearby configurations will tend to cancel out. But inevitably there will be some places in the space where s is stationary (has zero variational derivative) with respect to changes in fields. And in some approximation the field configurations in these places can be expected to dominate the path integral. But it turns out that these field configurations are exactly the ones that satisfy the partial differential equations for the classical version of the field theory. (This is analogous to what happens for example in classical diffraction theory, where there is an analog of the path integral—with  $\hbar$ replaced by inverse frequency-whose stationary points correspond through the so-called eikonal approximation to rays in geometrical optics.) In cases like QED and QCD the most obvious solutions to the classical equations are ones in which all fields are zero. And indeed standard perturbation theory is based on starting from these and then looking at the expansion of Exp[is/ħ] in powers of the coupling constant. But while this works for QED, it is only adequate for QCD in situations where the effective coupling is small. And indeed in other situations it seems likely that there will be all sorts of other solutions to the classical equations that become important. But apart from a few special cases with high symmetry, remarkably little is known about solutions to the classical equations even for pure gluon fields. No doubt the analog of turbulence can occur, and certainly there is sensitive dependence on initial conditions (even non-Abelian plane waves involve iterated maps that show this). Presumably much like in fluids there are various coherent structures such as color flux tubes and glueballs. But I doubt that states involving organized arrangements of these are common. And in general when there is strong coupling the path integral will potentially be dominated by large numbers of configurations not close to classical solutions.

In studying quantum field theories it has been common to consider effectively replacing time coordinates t by it to go from ordinary Minkowski space to Euclidean space (see page 1043). But while there is no problem in doing this at a formal mathematical level-and indeed the expressions one gets from Feynman diagrams can always be analytically continued in this way—what general correspondence there is for actual physical processes is far from clear. Formally continuing to Euclidean space makes path integrals easier to define with traditional mathematics, and gives them weights of the form Exp[-βs]—analogous to constant temperature systems in statistical mechanics. Discretizing yields lattice gauge theories with energy functions involving for example  $Cos[\theta_i - \theta_i]$  for color directions at adjacent sites. And Monte Carlo studies of such theories suggest all sorts of complex behavior, often similar in outline from what appears to occur in the corresponding classical field theories. (It seems conceivable that asymptotic freedom could lead to an analog of damping at small scales roughly like viscosity in turbulent fluids.)

One of the apparent implications of OCD is the confinement of quarks and gluons inside color-neutral hadrons. And at some level this is presumably a reflection of the fact that QCD forces get stronger rather than weaker with increasing distance. The beginnings of this are visible in perturbation

theory in the increase of the effective coupling with distance associated with asymptotic freedom. (In QED effective couplings decrease slightly with distance because fields get screened by virtual electron-positron pairs. The same happens with virtual quarks in QCD, but a larger effect is virtual gluon pairs whose color magnetic moments line up with a color field and serve to increase it.) At larger distances something like color flux tubes that act like elastic strings may form. But no detailed way to get confinement with purely classical gluon fields is known. In the quantum case, a sign of confinement would be exponential decrease with spacetime area of the average phase of color flux through socalled Wilson loops—and this is achieved if there is in a sense maximal randomness in field configurations. (Note that it is not inconceivable that the formal problem of whether quarks and gluons can ever escape to infinity starting from some given class of field configurations may in general be undecidable.)

■ Vacuum fluctuations. As an analog of the uncertainty principle, one of the implications of the basic formalism of quantum theory is that an ordinary quantum field can in a sense never maintain precisely zero value, but must always show certain fluctuations—even in what one considers the vacuum. And in terms of Feynman diagrams the way this happens is by virtual particle-antiparticle pairs of all types and all energy-momenta continually forming and annihilating at all points in the vacuum. Insofar as such vacuum fluctuations are always exactly the same, however, they presumably cannot be detected. (In the formalism of quantum field theory, they are usually removed by so-called normal ordering. But without this every mode of any quantum system will show a zero-point energy  $\hbar \omega/2$ —positive in sign for bosons and negative for fermions, cancelling for perfect supersymmetry. Quite what gravitational effects such zero-point energy might have has never been clear.) If one somehow changes the space in which a vacuum exists, there can be directly observable effects of vacuum fluctuations. An example is the 1948 Casimir effect—in which the absence of low-energy (long wavelength) virtual particle pairs in the space between two metal plates (but not in the infinite space outside) leads to a small but measurable force of attraction between them. The different detailed patterns of modes of different fields in different spaces can lead to very different effective vacuum energiesoften negative. And at least with the idealization of impermeable classical conducting boundaries one predicts (based on work of mine from 1981) the peculiar effect that closed cycles can be set up that systematically extract energy from vacuum fluctuations in a photon field.

If one has moving boundaries it turns out that vacuum fluctuations can in effect be viewed as producing real particles. And as known since the 1960s, the same is true for expanding universes. What happens in essence is that the modes of fields in different background spacetime structures differ to the point where zero-point excitations seem like actual particle excitations to a detector or observer calibrated to fields in ordinary fixed flat infinite spacetime. And in fact just uniform acceleration turns out to make detectors register real particles in a vacuum-in this case with a thermal spectrum at a temperature proportional to the acceleration. (Uniform rotation also leads to real particles, but apparently with a different spectrum.) As expected from the equivalence principle, a uniform gravitational field should produce the same effect. (Uniform electric fields lead in a formally similar way to production of charged particles.) And as pointed out by Stephen Hawking in 1974, black holes should also generate thermal radiation (at a temperature  $\hbar c^3/(8\pi G \, k \, M)$ ). A common interpretation is that the radiated particles are somehow ones left behind when the other particle in a virtual pair goes inside the event horizon. (A similar explanation can be given for uniform acceleration—for which there is also an event horizon.) There has been much discussion of the idea that Hawking radiation somehow shows pure quantum states spontaneously turning into mixed ones, more or less as in quantum measurements. But presumably this is just a reflection of the idealization involved in looking at quantum fields in a fixed background classical spacetime. And indeed work in string theory in the mid-1990s may suggest ways in which quantum gravity configurations of black hole surfaces could maintain the information needed for the whole system to act as a pure state.

■ Page 542 · Quantum measurement. The basic mathematical formalism used in standard quantum theory to describe pure quantum processes deals just with vectors of probability amplitudes. Yet our everyday experience of the physical world is that we observe definite things to happen. And the way this is normally captured is by saying that when an observation is made the vector of amplitudes is somehow replaced by its projection s into a subspace corresponding to the outcome seen-with the probability of getting the outcome being taken to be determined by s. Conjugate[s].

At the level of pure quantum processes, the standard rules of quantum theory say that amplitudes should be added as complex numbers—with the result that they can for example potentially cancel each other, and generally lead to wave-like interference phenomena. But after an observation is made, it is in effect assumed that a system can be described by ordinary real-number probabilities—so that for example no interference is possible. (At a formal level, results of pure quantum processes are termed pure quantum states, and are characterized by vectors of probability amplitudes; results of all possible observations are termed mixed states, and are in effect represented as mixtures of pure states.)

Ever since the 1930s there have been questions about just what should count as an observation. To explain everyday experience, conscious perception presumably always must. But it was not clear whether the operation of inanimate measuring devices of various kinds also should. And a major apparent problem was that if everything-including the measuring device—is supposed to be treated as part of the same quantum system, then all of it must follow the rules for pure quantum processes, which do not explicitly include any reduction of the kind supposed to occur in observations.

One approach to getting around this suggested in the late 1950s is the many-worlds interpretation (see page 1035): that there is in a sense a universal pure quantum process that involves all possible outcomes for every conceivable observation, and that represents the tree of all possible threads of history—but that in a particular thread, involving a particular sequence of tree branches, and representing a particular thread of experience for us, there is in effect a reduction in the pure quantum process at each branch point. Similar schemes have been popular in quantum cosmology since the early 1990s in connection with studying wave functions for the complete universe.

A quite different—and I think much more fruitful—approach is to consider analyzing actual potential measurement processes in the context of ordinary quantum mechanics. For even if one takes these processes to be pure quantum ones, what I believe is that in almost all cases appropriate idealized limits of them will reproduce what are in effect the usual rules for observations in quantum theory. A key point is that for one to consider something a reasonable measurement it must in a sense yield a definitive result. And in the context of standard quantum theory this means that somehow all the probability amplitudes associated with the measuring device must in effect be concentrated in specific outcomes—with no significant interference between different outcomes.

If one has just a few quantum particles—governed say by an appropriate Schrödinger equation—then presumably there can be no such concentration. But with a sufficiently large number of particles-and appropriate interactions-one expects that there can be. At first this might seem impossible. For the basic rules for pure quantum processes are entirely reversible (unitary). So one might think that if the evolution of a system leads to concentration of amplitudes, then it should equally well lead to the reverse. But the crucial point is that while this may in principle be possible, it may essentially never happen in practice—just like classical reversible systems essentially never show behavior that goes against the Second Law of thermodynamics. As suggested by the main text, the details in the quantum measurement case are slightly more complicated-since to represent multiple outcomes measuring devices typically have to have the analogs of multiple equilibrium states. But the basic phenomena are ultimately very similar-and both are in effect based on the presence of microscopic randomness. (In a quantum system the randomness serves to give collections of complex numbers whose average is essentially always zero.)

This so-called decoherence approach was discussed in the 1930s, and finally began to become popular in the 1980s. But to make it work there needs to be some source of appropriate randomness. And almost without exception what has been assumed is that this must come through the first mechanism discussed in Chapter 7: that there is somehow randomness present in the environment that always gets into the system one is looking at. Various different specific mechanisms for this have been suggested, including ones based on ambient low-frequency photons, background quantum vacuum fluctuations and background spacetime metric fluctuations. (A somewhat related proposal involves quantum gravity effects in which irreversibility is assumed to be generated through analogs of the black hole processes mentioned in the previous note.) And indeed in recent practical experiments where simple pure quantum states have carefully been set up, they seem to be destroyed by randomness from the environment on timescales of at most perhaps microseconds. But this does not mean that in more complicated systems more characteristic of real measuring devices there may not be other sources of randomness that end up dominating.

One might imagine that a possibility would be the second mechanism for randomness from Chapter 7, based on ideas of chaos theory. For certainly in the standard formalism, quantum probability amplitudes are taken to be continuous quantities in which an arbitrary number of digits can be specified. But at least for a single particle, the Schrödinger equation is in all ways linear, and so it cannot support any kind of real sensitivity to initial conditions, or even to parameters. But when many particles are involved the situation can presumably be different, as it definitely can be in quantum field theory (see page 1061).

I suspect, however, that in fact the most important source of randomness in most cases will instead be the phenomenon of intrinsic randomness generation that I first discovered in systems like the rule 30 cellular automaton. Just like in so many other areas, the emphasis on traditional mathematical methods has meant that for the most part fundamental studies have been made only on quantum systems that in the end turn out to have fairly simple behavior. Yet even within the standard formalism of quantum theory there are actually no doubt many closed systems that intrinsically manage to produce complex and seemingly random behavior even with very simple parameters and initial conditions. And in fact some clear signs of this were already present in studies of socalled quantum chaos in the 1980s-although most of the specific cases actually considered involved time-independent constraint satisfaction, not explicit time evolution. Curiously, what the Principle of Computational Equivalence suggests is that when quantum systems intrinsically produce apparent randomness they will in the end typically be capable of doing computations just as sophisticated as any other system-and in particular just as sophisticated as would be involved in conscious perception.

As a practical matter, mechanisms like intrinsic randomness generation presumably allow systems involving macroscopic numbers of particles to yield behavior in which interference becomes astronomically unlikely. But to reproduce the kind of exact reduction of probability amplitudes that is implied by the standard formalism of quantum theory inevitably requires taking the limit of an infinite system. Yet the Principle of Computational Equivalence suggests that the results of such a limit will typically be non-computable. (Using quantum field theory to represent infinite numbers of particles presumably cannot help; after appropriate analysis of the fairly sophisticated continuous mathematics involved, exactly the same computational issues should arise.)

It is often assumed that quantum systems should somehow easily be able to generate perfect randomness. But any sequence of bits one extracts must be deduced from a corresponding sequence of measurements. And certainly in practice—as mentioned on pages 303 and 970—correlations in the internal states of measuring devices between successive measurements will tend to lead to deviations from randomness. Whatever generates randomness and brings measuring devices back to equilibrium will eventually damp out such correlations. But insofar as measuring devices must formally involve infinite numbers of particles this process will formally require infinitely many steps. So this means that in effect an infinite computation is actually being done to generate each new bit. But with this amount of computation there are many ways to generate random bits. And in fact an infinite computation could even in principle produce algorithmic randomness (see page 1067) of the kind that is implicitly suggested by the traditional continuous mathematical formalism of quantum theory. So what this suggests is that there may in the end be no clear way to tell whether randomness is coming from an underlying quantum process that is being measured, or from the actual process of measurement. And indeed when it comes to more realistic finite measuring devices I would not be surprised if most of the supposed quantum randomness they measure is actually more properly attributed to intrinsic randomness generation associated with their internal mechanisms.

■ Page 543 · Bell's inequalities. In classical physics one can set up light waves that are linearly polarized with any given orientation. And if these hit polarizing ("anti-glare") filters whose orientation is off by an angle  $\theta$ , then the waves transmitted will have intensity  $Cos[\theta]^2$ . In quantum theory the quantization of particle spin implies that any photon hitting a polarizing filter will always either just go through or be absorbed-so that in effect its spin measured relative to the orientation of the polarizer is either +1 or -1. A variety of atomic and other processes give pairs of photons that are forced to have total spin 0. And in what is essentially the Einstein-Podolsky-Rosen setup mentioned on page 1058 one can ask what happens if such photons are made to hit polarizers whose orientations differ by angle  $\theta$ . In ordinary quantum theory, a straightforward calculation implies that the expected value of the product of the two measured spin values will be  $-Cos[\theta]$ . But now imagine instead that when each photon is produced it is assigned some "hidden variable"  $\phi$  that in effect explicitly specifies the angle of its polarization. Then assume that a polarizer oriented at  $0^{\circ}$ will measure the spin of such a photon to have value  $f[\phi]$ for some fixed function f. Now the expected value of the product of the two measured spin values is found just by averaging over  $\phi$  as

Integrate  $[f[\phi]f[\theta-\phi], \{\phi, 0, 2\pi\}]/(2\pi)$ 

A version of Bell's inequalities is then that this integral can decrease with  $\theta$  no faster than  $\theta/(2\pi)$ –1—as achieved when f=Sign. (In 3D  $\phi$  must be extended to a sphere, but the same final result holds.) Yet as mentioned on page 1058, actual experiments show that in fact the decrease with  $\theta$  is more rapid—and is instead consistent with the quantum theory result  $-Cos[\theta]$ . So what this means is that there is in a sense more correlation between measurements made on separated photons than can apparently be explained by the individual photons carrying any kind of explicit hidden property. (In the standard formalism of quantum theory this is normally explained by saying that the two photons can only meaningfully be considered as part of a single "entangled" state. Note that because of the probabilistic nature of the

correlations it turns out to be impossible to use them to do anything that would normally be considered communicating information faster than the speed of light.)

A basic assumption in deriving Bell's inequalities is that the choice of polarizer angle for measuring one photon is not affected by the choice of angle for the other. And indeed experiments have been done which try to enforce this by choosing the angles for the polarizers only just before the photons reach them—and too close in time for a light signal to get from one to the other. Such experiments again show violations of Bell's inequalities. But inevitably the actually devices that work out choices of polarizer angles must be in causal contact as part of setting up the experiment. And although it seems contrived, it is thus at least conceivable that with a realistic model for their time evolution such devices could end up operating in just such a way as to yield observed violations of Bell's inequalities.

Another way to get violations of Bell's inequalities is to allow explicit instantaneous propagation of information. But traditional models involving for example a background quantum potential again seem quite contrived, and difficult to generalize to relativistic cases. The approach I discuss in the main text is guite different, in effect using the idea that in a network model of space there can be direct connections between particles that do not in a sense ever have to go through ordinary intermediate points in space.

When set up for pairs of particles, Bell's inequalities tend just to provide numerical constraints on probabilities. But for

triples of particles, it was noticed in the late 1980s that they can give constraints that force probabilities to be 0 or 1, implying that with the assumptions made, certain configurations of measurement results are simply impossible.

In quantum field theory the whole concept of measurement is much less developed than in quantum mechanics-not least because in field theory it is much more difficult to factor out subsystems, and so to avoid having to give explicit descriptions of measuring devices. But at least in axiomatic quantum field theory it is typically assumed that one can somehow measure expectation values of any suitably smeared product of field operators. (It is possible that these could be reconstructed from combinations of idealized scattering experiments). And to get a kind of analog of Bell's inequalities one can look at correlations defined by such expectation values for field operators at spacelike-separated points (too close in time for light signals to get from one to another). And it then turns out that even in the vacuum state the vacuum fluctuations that are present show nonzero such correlations—an analog of ordinary quantum mechanical entanglement. (In a non-interacting approximation these correlations turn out to be as large as is mathematically possible, but fall off exponentially outside the light cone, with exponents determined by the smallest particle mass or the measurement resolution.) In a sense, however, the presence of such correlations is just a reflection of the idealized way in which the vacuum state is set up—with each field mode determined all at once for the whole system.

#### Processes of Perception and Analysis

#### **Defining the Notion of Randomness**

■ Page 554 · Algorithmic information theory. A description of a piece of data can always be thought of as some kind of program for reproducing the data. So if one could find the shortest program that works then this must correspond to the shortest possible description of the data—and in algorithmic information theory if this is no shorter than the data itself then the data is considered to be algorithmically random.

How long the shortest program is for a given piece of data will in general depend on what system is supposed to run the program. But in a sense the program will on the whole be as short as possible if the system is universal (see page 642). And between any two universal systems programs can differ in length by at most a constant: for one can always just add a fixed interpreter program to the programs for one system in order to make them run on the other system.

As mentioned in the main text, any data generated by a simple program can by definition never be algorithmically random. And so even though algorithmic randomness is often considered in theoretical discussions (see note below) it cannot be directly relevant to the kind of randomness we see in so many systems in this book—or, I believe, in nature.

If one considers all  $2^n$  possible sequences (say of 0's and 1's) of length n then it is straightforward to see that most of them must be more or less algorithmically random. For in order to have enough programs to generate all  $2^n$  sequences most of the programs one uses must themselves be close to length n. (In practice there are subtleties associated with the encoding of programs that make this hold only for sufficiently large n.) But even though one knows that almost all long sequences must be algorithmically random, it turns out to be undecidable in general whether any particular sequence is algorithmically random. For in general one can give no upper limit to how much computational effort one might have to expend in order to find out whether any given short

program—after any number of steps—will generate the sequence one wants.

But even though one can never expect to construct them explicitly, one can still give formal descriptions of sequences that are algorithmically random. An example due to Gregory Chaitin is the digits of the fraction  $\Omega$  of initial conditions for which a universal system halts (essentially a compressed version—with various subtleties about limits—of the sequence from page 1127 giving the outcome for each initial condition). As emphasized by Chaitin, it is possible to ask questions purely in arithmetic (say about sequences of values of a parameter that yield infinite numbers of solutions to an integer equation) whose answers would correspond to algorithmically random sequences. (See page 786.)

As a reduced analog of algorithmic information theory one can for example ask what the simplest cellular automaton rule is that will generate a given sequence if started from a single black cell. Page 1186 gives some results, and suggests that sequences which require more complicated cellular automaton rules do tend to look to us more complicated and more random.

■ History. Randomness and unpredictability were discussed as general notions in antiquity in connection both with questions of free will (see page 1135) and games of chance. When probability theory emerged in the mid-1600s it implicitly assumed sequences random in the sense of having limiting frequencies following its predictions. By the 1800s there was extensive debate about this, but in the early 1900s with the advent of statistical mechanics and measure theory the use of ensembles (see page 1020) turned discussions of probability away from issues of randomness in individual sequences. With the development of statistical hypothesis testing in the early 1900s various tests for randomness were proposed (see page 1084). Sometimes these were claimed to have some kind of general significance, but mostly they were just viewed as simple practical methods. In many fields

outside of statistics, however, the idea persisted even to the 1990s that block frequencies (or flat frequency spectra) were somehow the only ultimate tests for randomness. In 1909 Emile Borel had formulated the notion of normal numbers (see page 912) whose infinite digit sequences contain all blocks with equal frequency. And in the 1920s Richard von Mises-attempting to capture the observed lack of systematically successful gambling schemes—suggested that randomness for individual infinite sequences could be defined in general by requiring that "collectives" consisting of elements appearing at positions specified by any procedure should show equal frequencies. To disallow procedures say specially set up to pick out all the infinite number of 1's in a sequence Alonzo Church in 1940 suggested that only procedures corresponding to finite computations be considered. (Compare page 1021 on coarse-graining in thermodynamics.) Starting in the late 1940s the development of information theory began to suggest connections between randomness and inability to compress data, but emphasis on pLog[p] measures of information content (see page 1071) reinforced the idea that block frequencies are the only real criterion for randomness. In the early 1960s, however, the notion of algorithmic randomness (see note above) was introduced by Gregory Chaitin, Andrei Kolmogorov and Ray Solomonoff. And unlike earlier proposals the consequences of this definition seemed to show remarkable consistency (in 1966 for example Per Martin-Löf proved that in effect it covered all possible statistical tests)so that by the early 1990s it had become generally accepted as the appropriate ultimate definition of randomness. In the 1980s, however, work on cryptography had led to the study of some slightly weaker definitions of randomness based on inability to do cryptanalysis or make predictions with polynomial-time computations (see page 1089). But quite what the relationship of any of these definitions might be to natural science or everyday experience was never much discussed. Note that definitions of randomness given in dictionaries tend to emphasize lack of aim or purpose, in effect following the common legal approach of looking at underlying intentions (or say at physical construction of dice) rather than trying to tell if things are random from their observed behavior.

■ Inevitable regularities and Ramsey theory. One might have thought that there could be no meaningful type of regularity that would be present in all possible data of a given kind. But through the development since the late 1920s of Ramsey theory it has become clear that this is not the case. As one example, consider looking for runs of *m* equally spaced squares of the same color embedded in sequences of black

and white squares of length n. The pictures below show results with m=3 for various n. For n<9 there are always some sequences in which no runs of length 3 exist. But it turns out that for  $n \ge 9$  every single possible sequence contains at least one run of length 3. For any m the same is true for sufficiently large n; it is known that m=4 requires  $n \ge 35$  and m=5 requires  $n \ge 178$ . (In problems like this the analog of n often grows extremely rapidly with m.) If one has a sufficiently long sequence, therefore, just knowing that a run of equally spaced identical elements exists in it does not narrow down at all what the sequence actually is, and can so cannot ultimately be considered a useful regularity.

![](Images/_page_1083_Figure_4.jpeg)

(Compare pattern-avoiding sequences on page 944.)

#### **Defining Complexity**

■ Page 557 · History. There have been terms for complexity in everyday language since antiquity. But the idea of treating complexity as a coherent scientific concept potentially amenable to explicit definition is quite new: indeed this became popular only in the late 1980s-in part as a result of my own efforts. That what one would usually call complexity can be present in mathematical systems was for example already noted in the 1890s by Henri Poincaré in connection with the three-body problem (see page 972). And in the 1920s the issue of quantifying the complexity of simple mathematical formulas had come up in work on assessing statistical models (compare page 1083). By the 1940s general comments about biological, social and occasionally other systems being characterized by high complexity were common, particularly in connection with the cybernetics movement. Most often complexity seems to have been thought of as associated with the presence of large numbers of components with different types or behavior, and typically also with the presence of extensive interconnections or interdependencies. But occasionally-especially in some areas of social science—complexity was instead thought of as being characterized by somehow going beyond what human minds can handle. In the 1950s there was some discussion in pure mathematics of notions of complexity associated variously with sizes of axioms for logical theories, and with numbers of ways to satisfy such axioms. The development of information theory in the late 1940s-followed by the discovery of the structure of DNA in 1953-led to the idea that perhaps complexity might be related to information content. And when the notion of algorithmic information content as the length of a shortest program (see page 1067) emerged in the 1960s it was suggested that this might be an appropriate definition for complexity. Several other definitions used in specific fields in the 1960s and 1970s were also based on sizes of descriptions: examples were optimal orders of models in systems theory, lengths of logic expressions for circuit and program design, and numbers of factors in Krohn-Rhodes decompositions of semigroups. Beginning in the 1970s computational complexity theory took a somewhat different direction, defining what it called complexity in terms of resources needed to perform computational tasks. Starting in the 1980s with the rise of complex systems research (see page 862) it was considered important by many physicists to find a definition that would provide some kind of numerical measure of complexity. It was noted that both very ordered and very disordered systems normally seem to be of low complexity, and much was made of the observation that systems on the border between these extremes—particularly class 4 cellular automata—seem to have higher complexity. In addition, the presence of some kind of hierarchy was often taken to indicate higher complexity, as was evidence of computational capabilities. It was also usually assumed that living systems should have the highest complexity—perhaps as a result of their long evolutionary history. And this made informal definitions of complexity often include all sorts of detailed features of life (see page 1178). One attempt at an abstract definition was what Charles Bennett called logical depth: the number of computational steps needed to reproduce something from its shortest description. Many simpler definitions of complexity were proposed in the 1980s. Quite a few were based just on changing  $p_i Log[p_i]$  in the definition of entropy to a quantity vanishing for both ordered and disordered  $p_i$ . Many others were based on looking at correlations and mutual information measures-and using the fact that in a system with many interdependent and potentially hierarchical parts this should go on changing as one looks at more and more. Some were based purely on fractal dimensions or dimensions associated with strange attractors. Following my 1984 study of minimal sizes of finite automata capable of reproducing states in cellular automaton evolution (see page 276) a whole series of definitions were developed based on minimal sizes of descriptions in terms of deterministic and probabilistic finite automata (see page 1084). In general it is possible to imagine setting up all sorts of definitions for quantities that one chooses to call complexity. But what is most relevant for my purposes in this

book is instead to find ways to capture everyday notions of complexity—and then to see how systems can produce these. (Note that since the 1980s there has been interest in finding measures of complexity that instead for example allow maintainability and robustness of software and management systems to be assessed. Sometimes these have been based on observations of humans trying to understand or verify systems, but more often they have just been based for example on simple properties of networks that define the flow of control or data-or in some cases on the length of documentation needed.) (The kind of complexity discussed here has nothing directly to do with complex numbers such as  $\sqrt{-1}$  introduced into mathematics since the 1600s.)

#### **Data Compression**

- Practicalities. Data compression is important in making maximal use of limited information storage and transmission capabilities. One might think that as such capabilities increase, data compression would become less relevant. But so far this has not been the case, since the volume of data always seems to increase more rapidly than capabilities for storing and transmitting it. In the future, compression is always likely to remain relevant when there are physical constraints—such as transmission by electromagnetic radiation that is not spatially localized.
- History. Morse code, invented in 1838 for use in telegraphy, is an early example of data compression based on using shorter codewords for letters such as "e" and "t" that are more common in English. Modern work on data compression began in the late 1940s with the development of information theory. In 1949 Claude Shannon and Robert Fano devised a systematic way to assign codewords based on probabilities of blocks. An optimal method for doing this was then found by David Huffman in 1951. Early implementations were typically done in hardware, with specific choices of codewords being made as compromises between compression and error correction. In the mid-1970s. the idea emerged of dynamically updating codewords for Huffman encoding, based on the actual data encountered. And in the late 1970s, with online storage of text files becoming common, software compression programs began to be developed, almost all based on adaptive Huffman coding. In 1977 Abraham Lempel and Jacob Ziv suggested the basic idea of pointer-based encoding. In the mid-1980s, following work by Terry Welch, the so-called LZW algorithm rapidly became the method of choice for most general-purpose compression systems. It was used in programs such as PKZIP, as well as in hardware devices

such as modems. In the late 1980s, digital images became more common, and standards for compressing them emerged. In the early 1990s, lossy compression methods (to be discussed in the next section) also began to be widely used. Current image compression standards include: FAX CCITT 3 (run-length encoding, with codewords determined by Huffman coding from a definite distribution of run lengths); GIF (LZW); JPEG (lossy discrete cosine transform, then Huffman or arithmetic coding); BMP (run-length encoding, etc.); TIFF (FAX, JPEG, GIF, etc.). Typical compression ratios currently achieved for text are around 3:1, for line diagrams and text images around 3:1, and for photographic images around 2:1 lossless, and 20:1 lossy. (For sound compression see page 1080.)

- **Page 560 · Number representations.** The sequence of 1's and 0's representing a number *n* are obtained as follows:
- (a) Unary. Table[0, {n}]. (Not self-delimited.)
- (b) Ordinary base 2. IntegerDigits [n, 2]. (Not self-delimited.)
- (c) Length prefixed. Starting with an ordinary base 2 digit sequence, one prepends a unary specification of its length, then a specification of that length specification, and so on:

(Flatten[{Sign[-Range[1-Length[#], 0]], #}] &)[
Map[Rest, IntegerDigits[Rest[Reverse[NestWhileList[
Floor[Log[2, #]] &, n + 1, # > 1 &]]], 2]]]

(d) *Binary-coded base 3*. One takes base 3 representation, then converts each digit to a pair of base 2 digits, handling the beginning and end of the sequence in a special way.

```
Flatten[IntegerDigits[
Append[2 - With[{w = Floor[Log[3, 2 n]]},
IntegerDigits[n - (3^{w+1} - 1)/2, 3, w]], 3], 2, 2]]
```

(e) *Fibonacci encoding*. Instead of decomposing a number into a sum of powers of an integer base, one decomposes it into a sum of Fibonacci numbers (see page 902). This decomposition becomes unique when one requires that no pair of 1's appear together.

```
Apply[Take, RealDigits[(N[#, N[Log[10, #] + 3]] &)[ n\sqrt{5} /GoldenRatio<sup>2</sup> + 1/2], GoldenRatio]]
```

The representations of all the first Fibonacci[n]-1 numbers can be obtained from (the version in the main text has Rest[RotateLeft[Join[#, {0, 1}]]] & applied)

```
Apply[Join, Map[Last,
NestList[{#[[2]], Join[Map[Join[{1, 0}, Rest[#]] &, #[[2]]],
Map[Join[{1, 0}, #] &, #[[1]]]] &, {{}, {{1}}}, n-3]]]
```

■ Lengths of representations. (a) n, (b) Floor[Log[2, n] + 1], (c) Tr[FixedPointList[Max[0, Ceiling[Log[2, #]]] &, n + 2]] - n - 3, (d) 2 Ceiling[Log[3, 2 n + 1]], (e) Floor[Log[GoldenRatio. √5 (n + 1/2)]]. Large n approximations:

(a) n, (b) Log[2, n], (c) Log[2, n] + Log[2, Log[2, n]] + ..., (d) 2 Log[3, n], (e) Log[GoldenRatio, n].

Shown on a logarithmic scale, representations (b) through (e) (given here for numbers 1 through 500) all grow roughly linearly:

![](Images/_page_1085_Figure_16.jpeg)

■ Completeness. If one successively reads 0's and 1's from an infinite sequence then the representations (c), (d) and (e) have the property that eventually one will always accumulate a valid representation for some number or another. The pictures below show which sequences of 0's and 1's correspond to complete numbers in these representations. Every vertical column is a possible sequence of 0's and 1's, and the column is shown to terminate when a complete number is obtained.

![](Images/_page_1085_Picture_18.jpeg)

With an infinite random sequence of 0's and 1's, different number representations yield different distributions of sizes of numbers. Representation (b), for example, is more weighted towards large numbers, while (c) is more weighted towards small numbers. Maximal compression for a sequence of numbers with a particular distribution of sizes is obtained by choosing a representation that yields a matching such distribution. (See also page 949.)

- **Practical computing.** Numbers used for arithmetic in practical computing are usually assumed to have a fixed length of, say, 32 bits, and thus do not need to be self-delimiting. In *Mathematica*, where integers can be of essentially any size, a representation closer to (b) above is used.
- Page 561 · Run-length encoding. Data can be converted to run lengths by Map[Length, Split[data]]. Each number is then replaced by its representation.

With completely random input, the output will on average be longer by a factor  $Sum[2^{-(n+1)} r[n], \{n, 1, \infty\}]$  where r[n] is the length of the representation for n. For the Fibonacci encoding used in the main text, this factor is approximately 1.41028. (In base 2 this number has 1's essentially at positions Fibonacci[n]; as discussed on page 914, the number is transcendental.)

■ **Page 563 · Huffman coding.** From a list p of probabilities for blocks, the list of codewords can be generated using

```
Map[Drop[Last[#], -1] &, Sort[
                                        Flatten[MapIndexed[Rule, FixedPoint[Replace[Sort[#],
                                                                                                                  \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0 + p1, \{i0, i1\}\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i0_-\}, \{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p1_-, i1_-\}, pi_{---}\} \rightarrow \{\{p0_-, i1_-\}, pi_{---}\}, pi_{---}\} \rightarrow \{\{p0_-, i1_-\}, pi_{---}\}, pi_{---}\} \rightarrow \{\{p1_-, i1_-\}, pi_{---}\}, pi_{---}\} \rightarrow \{\{p1_-, i1_-\}, pi_{---}\}, pi_{---}\} \rightarrow \{\{p1_-, i1_-\}, pi_{---}\}, pi_{---}\} \rightarrow \{\{p1_-, i1_-\}, pi_{---}\}, pi_{---}\} \rightarrow \{\{p1_-, i1_-\}, pi_{---}\}, pi_{---}\}, pi_{---}\} \rightarrow \{\{p1_-, i1_-\}, pi_{---}\}, pi_{---}\} \rightarrow \{\{p1_-, i1_-\}, pi_{---}\}, pi_{---}\}, pi_{---}\} \rightarrow \{\{p1_-, i1_-\}, pi_{---}\}, pi_{---}\}, pi_{---}\} \rightarrow \{\{p1_-, i1_-\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{----}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{---}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{----}\}, pi_{-----}\}, pi_{----}\}, pi_{-----}\}, pi_{-----}\}, pi_{-----}\}, pi_{------}\}, pi_{-----}\}, pi_{------}\}, pi_{------------------------------------
                                                                                                                                           pi}] &, MapIndexed[List, p]][[1, 2]], {-1}]]]]-1
```

Given the list of codewords *c*, the sequence of blocks that occur in encoded data d can be uniquely reconstructed using First[{{}, d} //. MapIndexed[

```
\{\{r\_\_\}, Flatten[\{\#1, s\_\_\}]\} \rightarrow \{\{r, \#2[[1]]\}, \{s\}\} \&, c]\}
```

Note that the encoded data can consist of any sequence of 0's and 1's. If all  $2^b$  possible blocks of length b occur with equal probability, then the Huffman codewords will consist of blocks equivalent to the original ones. In an opposite extreme, blocks with probabilities 1/2, 1/4, 1/8, ... will yield codewords of lengths 1, 2, 3, ...

In practical applications, Huffman coding is sometimes extended to allow the choice of codewords to be updated dynamically as more data is read.

- Maximal block compression. If one has data that consists of a long sequence of blocks, each of length b, and each independently chosen with probability p[i] to be of type i, then as argued by Claude Shannon in the late 1940s, it turns out that the minimum number of base 2 bits needed on average to represent each block in such a sequence is  $h = -Sum[p[i]Log[2, p[i]], \{i, 2^b\}]$ . If all blocks occur with an equal probability of  $2^{-b}$ , then h takes on its maximum possible value of b. If only one block occurs with nonzero probability then h = 0. Following Shannon, the quantity h (whose form is analogous to entropy in physics, as discussed on page 1020) is often referred to as "information content". This name, however, is very misleading. For certainly h does not in general give the length of the shortest possible description of the data; all it does is to give the shortest length of description that is obtained by treating successive blocks as if they occur with independent probabilities. With this assumption one then finds that maximal compression occurs if a block of probability p[i] is represented by a codeword of length -Log[2, p[i]]. Huffman coding with a large number of codewords will approach this if all the p[i] are powers of 1/2. (The self-delimiting of codewords leads to deviations for small numbers of codewords.) For p[i] that are not powers of 1/2, non-integer length codewords would be required. The method of arithmetic coding provides an alternative in which the output does not consist of separate codewords concatenated together. (Compare algorithmic information content discussed on pages 554 and 1067.)
- **Arithmetic coding.** Consider dividing the interval from 0 to 1 into a succession of bins, with each bin having a width equal to the probability for some sequence of blocks to occur.

The idea of arithmetic coding is to represent each such bin by the digit sequence of the shortest number within the binafter trailing zeros have been dropped. For any sequence s this can be done using

```
Module[\{c, m = 0\},
Map[c[\#] = \{m, m += Count[s, \#]/Length[s]\} \&, Union[s]];
Function[x, (First[RealDigits[2^{\#} Ceiling[2^{-\#} Min[x]],
   2, -#, -1]] &)[Floor[Log[2, Max[x] - Min[x]]]]][
Fold[(Max[#1]-Min[#1])c[#2]+Min[#1]&, {0, 1}, s]]]
```

Huffman coding of a sequence containing a single 0 block together with n 1 blocks will yield output of length about n; arithmetic coding will yield length about Log[n]. Compression in arithmetic coding still relies, however, on unequal block probabilities, just like in Huffman coding. Originally suggested in the early 1960s, arithmetic coding reemerged in the late 1980s when high-speed floating-point computation became common, and is occasionally used in practice.

■ Page 565 · Pointer-based encoding. One can encode a list of data d by generating pointers to the longest and most recent copies of each subsequence of length at least b using

```
PEncode[d_, b_: 4] := Module[\{i, a, u, v\}]
  i = 2; a = \{First[d]\}; While[i \le Length[d], \{u, v\} =
     Last[Sort[Table[{MatchLength[d, i, j], j}, {j, i-1}]]];
    If [u \ge b, AppendTo[a, p[i-v, u]]; i += u,
     AppendTo[a, d[[i]]]; i++]]; a]
MatchLength[d_i, i_j] := With[\{m = Length[d] - i\}, Catch[
 Do[If[d[i+k]] = != d[j+k]], Throw[k]], \{k, 0, m\}]; m+1]]
```

The process of encoding can be made considerably faster by keeping a dictionary of previously encountered subsequences. One can reproduce the original data using

```
PDecode[a_] := Module[\{d = Flatten[
   a /. p[j_{-}, r_{-}] :→ Table[p[j], {r}]]}, Flatten[MapIndexed[
  If [Head[#1] === p, d[#2]] = d[#2 - First[#1]], #1] &, d]]]
```

To get a representation purely in terms of 0 and 1, one can use a self-delimiting representation for each integer that appears. (Knowing the explicit representation one could then determine whether each block would be shorter if encoded literally or using a pointer.) The encoded version of a purely repetitive sequence of length n has a length that grows like Log[n]. The encoded version of a purely nested sequence grows like  $Log[n]^2$ . The encoded version of a sufficiently random sequence grows like n (with the specific encoding used in the text, the length is about 2n). Note that any sequence of 0's and 1's corresponds to the beginning of the encoding for some sequence or another.

It is possible to construct sequences whose encoded versions grow roughly like fractional powers of n. An example is the sequence Table[Append[Table[0, {r}], 1], {r, s}] whose encoded version grows like  $\sqrt{n} Log[n]$ . Cyclic tag systems often seem to produce sequences whose encoded versions grow like fractional powers of n. Sequences produced by concatenation sequences are not typically compressed by pointer encoding.

With completely random input, the probability that the length b subsequence which begins at element n is a repeat of a previous subsequence is roughly  $1-(1-2^{-b})^{n-1}$ . The overall fraction of a length n input that consists of repeats of length at least b is greater than  $1-2^b/n$  and is essentially

 $1 - Sum[(1 - 2^{-b})^{i} Product[1 + (1 - 2^{-b})^{j} - (1 - 2^{-b-1})^{j}]$  ${j, i-b+1, i-1}, {i, b, n-b}/{n-2b+1}$ 

![](Images/_page_1087_Picture_5.jpeg)

![](Images/_page_1087_Picture_6.jpeg)

![](Images/_page_1087_Picture_7.jpeg)

![](Images/_page_1087_Picture_8.jpeg)

![](Images/_page_1087_Picture_9.jpeg)

![](Images/_page_1087_Picture_10.jpeg)

- LZW algorithms. Practical implementations of pointer-based encoding can maintain only a limited dictionary of possible repeats. Various schemes exist for optimizing the construction, storage and rewriting of such dictionaries.
- Page 568 · Recursive subdivision. In one dimension, encoding can be done using

Subdivide[a_] := Flatten[If[Length[a] == 2, a, If[Apply[SameQ, a], {1, First[a]}, {0, Map[Subdivide, Partition[a, Length[a]/2]]}]]]

In n dimensions, it can be done using

Subdivide[a_, n_] := With[{s = Table[1, {n}]}, Flatten[If[Dimensions[a] == 2 s, a, If[Apply[SameQ, Flatten[a]], {1, First[Flatten[a]]}, {0, Map[Subdivide[#, n] &, Partition[a, 1/2 Length[a] s], {n}]}]]]]

■ 2D run-length encoding. A simple way to generalize run-length encoding to two dimensions is to scan data one row after another, always finding the largest rectangle of uniform color that starts at each particular point. The pictures below show regions with an area of more than 10 cells found in this way. The presence of so many thin and overlapping regions prevents good compression.

![](Images/_page_1087_Picture_17.jpeg)

![](Images/_page_1087_Picture_18.jpeg)

2D run-length encoding can also be done by scanning the data according to a more complicated space-filling curve, of the kind discussed on page 893.

#### Irreversible Data Compression

■ History. The idea of creating sounds by adding together pure tones goes back to antiquity. At a mathematical level, following work by Joseph Fourier around 1810 it became clear by the mid-1800s how any sufficiently smooth function could be decomposed into sums of sine waves with frequencies corresponding to successive integers. Early telephony and sound recording in the late 1800s already used the idea of compressing sounds by dropping high- and lowfrequency components. From the early days of television in the 1950s, some attempts were made to do similar kinds of compression for images. Serious efforts in this direction were not made, however, until digital storage and processing of images became common in the late 1980s.

■ Orthogonal bases. The defining feature of a set of basic forms is that it is complete, in the sense that any piece of data can be built up by adding the basic forms with appropriate weights. Most sets of basic forms used in practice also have the feature of being orthogonal, which turns out to make it particularly easy to work out the weights for a given piece of data. In 1D, a basic form a[[i]] is just a list. Orthogonality is then the property that  $a[[i]] \cdot a[[j]] == 0$  for all  $i \neq j$ . And when this property holds, the weights are given essentially just by data.a.

The concept of orthogonal bases was historically worked out first in the considerably more difficult case of continuous functions. Here a typical orthogonality property is Integrate[ $f[r, x]f[s, x], \{x, 0, 1\}$ ] == KroneckerDelta[r, s]. As discovered by Joseph Fourier around 1810, this is satisfied for basis functions such as  $Sin[2n\pi x]/\sqrt{2}$ .

■ Page 573 · Walsh transforms. The basic forms shown in the main text are 2D Walsh functions—represented as ±1 matrices. Each collection of such functions can be obtained from lists of vectors representing 1D Walsh functions by using Outer[Outer[Times, ##] &, b, b, 1, 1], or equivalently Map[Transpose, Map[#b &, b, {2}]].

The pictures below show how 1D arrays of data values can be built up by adding together 1D Walsh functions. At each step the Walsh function used is given underneath the array of values obtained so far.

![](Images/_page_1087_Figure_27.jpeg)

The components of the vectors for 1D Walsh functions can be ordered in many ways. The pictures below show the complete matrices of basis vectors obtained with three common orderings.

![](Images/_page_1088_Picture_3.jpeg)

![](Images/_page_1088_Picture_4.jpeg)

![](Images/_page_1088_Picture_5.jpeg)

The matrices for size  $n = 2^s$  can be obtained from

Nest[Apply[Join, f[{Map[Flatten[Map[{#, #} &, #]] &, #], Map[Flatten[Map[{#, -#} &, #]] &, g[#]]}]] &, {{1}}, s]

with (a) f = Identity, g = Reverse, (b) f = Transpose, g = Identity, and (c) f = g = Identity. (a) is used in the main text. Known as sequency order, it has the property that each row involves one more change of color than the previous row. (b) is known as natural or Hadamard order. It exhibits a nested structure, and can be obtained as in the pictures below from the evolution of a 2D substitution system, or equivalently from a Kronecker product as in

Nest[Flatten2D[Map[# {{1, 1}, {1, -1}} &, #, {2}]] &, {{1}}, s]

Flatten2D[a_] := Apply[Join, Apply[Join, Map[Transpose, a], {2}]]

![](Images/_page_1088_Picture_11.jpeg)

![](Images/_page_1088_Picture_12.jpeg)

![](Images/_page_1088_Picture_13.jpeg)

![](Images/_page_1088_Picture_14.jpeg)

![](Images/_page_1088_Picture_15.jpeg)

(c) is known as dyadic or Paley order. It is related to (a) by Gray code reordering of the rows, and to (b) by reordering according to (see page 905)

BitReverseOrder[a_] := With[{n = Length[a]}, a[[Map[FromDigits[Reverse[#], 2] &, IntegerDigits[Range[0, n - 1], 2, Log[2, n]]] + 1]]]

It is also given by

Array[Apply[Times, (-1)^(IntegerDigits[#1, 2, s] Reverse[IntegerDigits[#2, 2, s]])] &, {2^s, 2^s}, 0]

where (b) is obtained simply by dropping the Reverse.

Walsh functions can correspond to nested sequences. The function at position  $2/3(1+4^{-(Floor[s/2]+1/2))})2^{s}$  in basis (a), for example, is exactly the Thue-Morse sequence (with 0 replaced by -1) from page 83.

Given the matrix m of basis vectors, the Walsh transform is simply data . m. Direct evaluation of this for length n takes  $n^2$ steps. However, the nested structure of m in natural order allows evaluation in only about n Log[n] steps using

Nest[Flatten[Transpose[Partition[#, 2]. {{1, 1}, {1, -1}}]] &, data, Log[2, Length[data]]]

This procedure is similar to the fast Fourier transform discussed below. Transforms of 2D data are equivalent to 1D transforms of flattened data.

Walsh functions were used by electrical engineers such as Frank Fowle in the 1890s to find transpositions of wires that minimized crosstalk; they were introduced into mathematics by Joseph Walsh in 1923. Raymond Paley introduced the dyadic basis in 1932. Mathematical connections with harmonic analysis of discrete groups were investigated from the late 1940s. In the 1960s, Walsh transforms became fairly widespread in discrete signal and image processing.

■ Page 575 · Walsh spectra. The arrays of absolute values of weights of basic forms for successive images are as follows:

![](Images/_page_1088_Picture_26.jpeg)

■ Hadamard matrices. Hadamard matrices are nxn matrices with elements -1 and +1, whose rows are orthogonal, so that m. Transpose[m] == n IdentityMatrix[n]. The matrices used in Walsh transforms are special cases with  $n = 2^s$ . There are thought to be Hadamard matrices with every size n = 4k(and for n > 2 no other sizes are possible); the number of distinct such matrices for each k up to 7 is 1, 1, 1, 5, 3, 60, 487. The so-called Paley family of Hadamard matrices for n = 4k = p + 1 with p prime are given by

PadLeft[Array[JacobiSymbol[#2-#1, n-1] &, {n, n}-1]- $IdentityMatrix[n-1], \{n, n\}, 1]$ 

Originally introduced by Jacques Hadamard in 1893 as the matrices with elements  $Abs[a] \le 1$  which attain the maximal possible determinant  $\pm n^{n/2}$ , Hadamard matrices appear in various combinatorial problems, particularly design of exhaustive combinations of experiments and Reed-Muller error-correcting codes.

■ Image averaging. Walsh functions yield significantly better compression than simple successive averaging of 2×2 blocks of cells, as shown below.

![](Images/_page_1088_Picture_31.jpeg)

- Practical image compression. Two basic phenomena contribute to our ability to compress images in practice. First, that typical images of relevance tend to be far from random—indeed they often involve quite limited numbers of distinct objects. And second, that many fine details of images go unnoticed by the human visual system (see the next section).
- Fourier transforms. In a typical Fourier transform, one uses basic forms such as  $Exp[i\pi r x/n]$  with r running from 1 to n. The weights associated with these forms can be found using Fourier, and given these weights the original data can also be reconstructed using InverseFourier. The pictures below show what happens in such a so-called discrete cosine transform when different fractions of the weights are kept, and others are effectively set to zero. High-frequency wiggles associated with the so-called Gibbs phenomenon are typical near edges.

![](Images/_page_1089_Picture_3.jpeg)

Fourier[data] can be thought of as multiplication by the  $n \times n$  matrix  $Array[Exp[2\pi i\#1\#2/n]\&, \{n, n\}, 0]$ . Applying BitReverseOrder to this matrix yields a matrix which has an essentially nested form, and for size  $n = 2^s$  can be obtained from

Nest[With[{c = BitReverseOrder[Range[0, Length[#]-1]/ Length[#]]}, Flatten2D[MapIndexed[#1{{1, 1}, {1, -1}(-1)^c[[Last[#2]]]} &, #, {2}]]] &, {{1}}, s]

Using this structure, one obtains the so-called fast Fourier transform which operates in n Log[n] steps and is given by

 $\label{eq:with} With $\{ n = \text{Length}[data] \}$, $Fold[Flatten[Map[With[\ \{k = \text{Length}[\#]/2\}, \{\{1, 1\}, \{1, -1\} \}, \{\text{Take}[\#, k], Drop\ \#, k^(Range[0, k-1]/k) \}] \&, $Partition[\#\#]]] \&, $BitReverseOrder[data], $2^Range[Log[2, n]]]/\sqrt{n}$ $(See also page 1080.)$ 

- JPEG compression. In common use since the early 1990s JPEG compression works by first assigning color values to definite bins, then applying a discrete Fourier cosine transform, then applying Huffman encoding to the resulting weights. The "quality" of the image is determined by how many weights are kept; a typical default quality factor, used say by Export in Mathematica, is 75.
- Wavelets. Each basic form in an ordinary Walsh or Fourier transform has nonzero elements spread throughout. With wavelets the elements are more localized. As noted in the late

1980s basic forms can be set up by scaling and translating just a single appropriately chosen underlying shape. The (a) Haar and (b) Daubechies wavelets  $\psi[x]$  shown below both have the property that the basic forms  $2^{m/2} \psi[2^m x - n]$  (whose 2D analogs are shown as on page 573) are orthogonal for every different m and n.

![](Images/_page_1089_Figure_11.jpeg)

The pictures below show images built up by keeping successively more of these basic forms. Sharp edges have fewer wiggles than with Fourier transforms.

![](Images/_page_1089_Figure_13.jpeg)

■ **Sound compression.** See page 1080.

#### **Visual Perception**

■ **Color vision.** The three types of color-sensitive cone cells on the human retina each have definite response curves as a function of wavelength. The perceived color of light with a given wavelength distribution is basically determined by the three numbers obtained by integrating these responses. For any wavelength distribution it turns out that if one scales these numbers to add up to one, then the chromaticity values obtained must lie within a certain region. Mixing n specific colors in different proportions allows one to reach any point in an n-cornered polytope. For n = 3 this polytope comes close to filling the region of all possible colors, but for no n can it completely fill it—which is why practical displays and printing processes can produce only limited ranges of colors.

An important observation, related to the fact that limitations in color ranges are usually not too troublesome, is that the perceived colors of objects stay more or less constant even when viewed in very different lighting, corresponding to very different wavelength distributions. In recent years it has become clear that the origin of this phenomenon is that

beyond the original cone cells, most color-sensitive cells in our visual system respond not to absolute color levels, but instead to differences in color levels at slightly different positions. (Responses to nearby relative values rather than absolute values seem to be common in many forms of human perception.)

The fact that white light is a mixture of colors was noticed by Isaac Newton in 1704, and it became clear in the course of the 1700s that three primaries could reproduce most colors. Thomas Young suggested in 1802 that there might be three types of color receptors in the eye, but it was not until 1959 that these were actually identified—though on the basis of perceptual experiments, parametrizations of color space were already well established by the 1930s. While humans and primates normally have three types of cone cells, it has been found that other mammals normally have two, while birds, reptiles and fishes typically have between 3 and 5.

- Nerve cells. In the retina and the brain, nerve cells typically have an irregular tree-like structure, with between a few and a few thousand dendrites carrying input signals, and one or more axons carrying output signals. Nerve cells can respond on timescales of order milliseconds to changes in their inputs by changing their rate of generating output electrical spikes. As has been believed since the 1940s, most often nerve cells seem to operate at least roughly by effectively adding up their inputs with various positive or negative weights, then going into an excited state if the result exceeds some threshold. The weights seem to be determined by detailed properties of the synapses between nerve cells. Their values can presumably change to reflect certain aspects of the activity of the cell, thus forming a basis for memory (see page 1102). In organisms with a total of only a few thousand nerve cells, each individual cell typically has definite connections and a definite function. But in humans with perhaps 100 billion nerve cells, the physical connections seem quite haphazard, and most nerve cells probably develop their function as a result of building up weights associated with their actual pattern of behavior, either spontaneous or in response to external stimuli.
- The visual system. Connected to the 100 million or so light-sensitive photoreceptor cells on the retina are roughly two layers of nerve cells, with various kinds of cross-connections, out of which come the million fibers that form the optic nerve. After essentially one stop, most of these go to the primary visual cortex at the back of the brain, which itself contains more than 100 million nerve cells. Physical connections between nerve cells have usually been difficult to map. But starting in the 1950s it became possible to record electrical activity in single cells, and from this the discovery

was made that many cells respond to rather specific visual stimuli. In the retina, most common are center-surround cells, which respond when there is a higher level of light in the center of a roughly circular region and a lower level outside, or vice versa. In the first few layers of the visual cortex about half the cells respond to elongated versions of similar stimuli, while others seem sensitive to various forms of change or motion. In the fovea at the center of the retina, a single center-surround cell seems to get input from just a few nearby photoreceptors. In successive layers of the visual cortex cells seem to get input from progressively larger regions. There is a very direct mapping of positions on the retina to regions in the visual cortex. But within each region there are different cells responding to stimuli at different angles, as well as to stimuli from different eyes. Cells with particular kinds of responses are usually found to be arranged in labyrinthine patterns very much like those shown on page 427. And no doubt the processes which produce these patterns during the development of the organism can be idealized by simple 2D cellular automata. Quite what determines the pattern of illumination to which a given cell will respond is not yet clear, although there is some evidence that it is the result of adaptation associated with various kinds of test inputs. Since the late 1970s, it has been common to assume that the response of a cell can be modelled by derivatives of Gaussians such as those shown below, or perhaps by Gabor functions given by products of trigonometric functions and Gaussians. Experiments have determined responses to these and other specific stimuli, but inevitably no experiment can find all the stimuli to which a cell is sensitive.

![](Images/_page_1090_Picture_7.jpeg)

The visual systems of a number of specific higher and lower organisms have now been studied, and despite a few differences (such as cross-connections being behind the photoreceptors on the retinas of octopuses and squids, but in front in most higher animals), the same general features are usually seen. In lower organisms, there tend to be fewer layers of cells, with individual cells more specialized to particular visual stimuli of relevance to the organism.

■ Feedback. Most of the lowest levels of visual processing seem to involve only signals going successively from one layer in the eye or brain to the next. But presumably there is at least some feedback to previous layers, yielding in effect iteration of rules like the ones used in the main text. The

resulting evolution process is likely to have attractors, potentially explaining the fact that in images such as "Magic Eye" random dot stereograms features can pop out after several seconds or minutes of scrutiny, even without any conscious effort.

- Scale invariance. In a first approximation our recognition of objects does not seem to be much affected by overall size or overall light level. For light level—as with color constancy this is presumably achieved by responding only to differences between levels at different positions. Probably the same effect contributes to scale invariance by emphasizing only edges and corners. And if one is looking at objects like letters, it helps that one has learned them at many different sizes. But also similar cells most likely receive inputs from regions with a range of different sizes on the retina-making even unfamiliar textures seem the same over at least a certain range of scales. When viewed at a normal reading distance of 12 inches each square in the picture on page 578 covers a region about 5 cells across on the retina. With good lighting and good eyesight the textures in the picture can still be distinguished at a distance of 5 feet, where each square covers only one cell. But if the picture is enlarged by a factor of 3 or more then at normal reading distance it can become difficult to distinguish the textures-perhaps because the squares cover regions larger than the templates used at the lowest levels in our visual system.
- History. Ever since antiquity the visual arts have yielded practical schemes and sometimes also fairly abstract frameworks for determining what features of images will have what impact. In fact, even in prehistoric times it seems to have been known, for example, that edges are often sufficient to communicate visual forms, as in the pictures below.

![](Images/_page_1091_Picture_4.jpeg)

![](Images/_page_1091_Picture_5.jpeg)

![](Images/_page_1091_Picture_6.jpeg)

![](Images/_page_1091_Picture_7.jpeg)

Visual perception has been used for centuries as an example in philosophical discussions about the nature of experience. Traditional mathematical methods began to be applied to it in the second half of the 1800s, particularly through the development of psychophysics. Studies of visual illusions around the end of the 1800s raised many questions that were not readily amenable to numerical measurement or traditional mathematical analysis, and this led in part to the Gestalt approach to psychology which attempted to formulate various global principles of visual perception.

In the 1940s and 1950s, the idea emerged that visual images might be processed using arrays of simple elements. At a largely theoretical level, this led to the perceptron model of the visual system as a network of idealized neurons. And at a practical level it also led to many systems for image processing (see below), based essentially on simple cellular automata (see page 928). Such systems were widely used by the end of the 1960s, especially in aerial reconnaissance and biomedical applications.

Attempts to characterize human abilities to perceive texture appear to have started in earnest with the work of Bela Julesz around 1962. At first it was thought that the visual system might be sensitive only to the overall autocorrelation of an image, given by the probability that randomly selected points have the same color. But within a few years it became clear that images could be constructed—notably with systems equivalent to additive cellular automata (see below)—that had the same autocorrelations but looked completely different. Julesz then suggested that discrimination between textures might be based on the presence of "textons", loosely defined as localized regions like those shown below with some set of distinct geometrical or topological properties.

![](Images/_page_1091_Picture_11.jpeg)

In the 1970s, two approaches to vision developed. One was largely an outgrowth of work in artificial intelligence, and concentrated mostly on trying to use traditional mathematics to characterize fairly high-level perception of objects and their geometrical properties. The other, emphasized particularly by David Marr, concentrated on lower-level processes, mostly based on simple models of the responses of single nerve cells, and very often effectively applying <code>ListConvolve</code> with simple kernels, as in the pictures below.

![](Images/_page_1091_Picture_13.jpeg)

![](Images/_page_1091_Picture_14.jpeg)

![](Images/_page_1091_Picture_15.jpeg)

![](Images/_page_1091_Picture_16.jpeg)

In the 1980s, approaches based on neural networks capable of learning became popular, and attempts were made in the context of computational neuroscience to create models combining higher- and lower-level aspects of visual perception.

The basic idea that early stages of visual perception involve extraction of local features has been fairly clear since the 1950s, and researchers from a variety of fields have invented and reinvented implementations of this idea many times. But mainly through a desire to use traditional mathematics, these

implementations have tended to be implicitly restricted to using elements with various linearity properties-typically leading to rather unconvincing results. My model is closer to what is often done in practical image processing, and apparently to how actual nerve cells work, and in effect assumes highly nonlinear elements.

- Page 581 · Implementation. The exact matches for a template  $\sigma$  in data containing elements 0 and 1 can be obtained from Sign[ListCorrelate[2 $\sigma$ - 1, data] - Count[$\sigma$, 1, 2]] + 1
- Testing the model. Although it is difficult to get good systematic data, the many examples I have tried indicate that the levels of discrimination between textures that we achieve with our visual system agree remarkably well with those suggested by my simple model. A practical issue that arises is that if one repeatedly tries experiments with the same set of textures, then after a while one learns to discriminate these particular textures better. Shifting successive rows or even just making an overall rotation seems, however, to avoid this
- Related models. Rather than requiring particular templates to be matched, one can consider applying arbitrary cellular automaton rules. The pictures below show results from a single step of the 16 even-numbered totalistic 5-neighbor rules. The results are surprisingly easy to interpret in terms of feature extraction.

![](Images/_page_1092_Picture_6.jpeg)

■ Image processing. The release of programs like Photoshop in the late 1980s made image processing operations such as smoothing, sharpening and edge detection widely available on general-purpose computers. Most of these operations are just done by applying ListConvolve with simple kernels. (Even before computers, such convolutions could be done using the fact that diffraction of light effectively performs Fourier transforms.) Ever since the 1960s all sorts of schemes for nonlinear processing of images have been discussed and used in particular communities. An example originally popular in the earth and environmental sciences is so-called mathematical morphology, based on "dilation" of data consisting of 0's and 1's with a "structuring element"  $\sigma$ according to  $Sign[ListConvolve[\sigma, data, 1, 0]]$  (as well as the dual operation of "erosion"). Most schemes like this can ultimately be thought of as picking out templates or applying simple cellular automaton rules.

- Real textures. The textures I consider in the main text are all based on arrays of discrete black and white squares. One can also consider textures associated, say, with surface roughness of physical objects. Models of these are often needed for realistic computer graphics. Common approaches are to assume that the surfaces are random with some frequency spectrum, or can be generated as fractals using substitution systems with random parameters. In recent times, models based on wavelets have also been used.
- Statistical methods. Even though they do not appear to correspond to how the human visual system works, statistical methods are often used in trying to discriminate textures automatically. Correlations, conditional entropies and fractal dimensions are commonly computed. Often it is assumed that different parts of a texture are statistically independent, so that the texture can be characterized by probabilities for local patterns, as in a so-called Markov random field or generalized autoregressive moving average (ARMA) process.
- Camouflage. On both animals and military vehicles it is often important to have patterns that cannot be distinguished from a background by the visual systems of predators. And in most cases this is presumably best achieved by avoiding differences in densities of certain local features. Note that in a related situation almost any fairly random overlaid pattern containing many local features can successfully be used to mask the contents of a paper envelope.
- Halftoning. In printed books like this one, gray levels are usually obtained by printing small dots of black with varying sizes. On displays consisting of fixed arrays of pixels, gray levels must be obtained by having only a certain density of pixels be black. One way to achieve this is to break the array into  $2^n \times 2^n$  blocks, then successively to fill in pixels in each block until the appropriate gray level is reached, as in the pictures below, in an order given for example by

Nest[Flatten2D[{{4# + 0, 4# + 2}, {4# + 3, 4# + 1}}] &, {{0}}, n]
