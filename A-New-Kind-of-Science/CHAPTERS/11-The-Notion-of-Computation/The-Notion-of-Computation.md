#### The Notion of Computation

#### Computation as a Framework

In earlier parts of this book we saw many examples of the kinds of behavior that can be produced by cellular automata and other systems with simple underlying rules. And in this chapter and the next my goal is to develop a general framework for thinking about such behavior.

Experience from traditional science might suggest that standard mathematical analysis should provide the appropriate basis for any such framework. But as we saw in the previous chapter, such analysis tends to be useful only when the overall behavior one is studying is fairly simple.

So what can one do when the behavior is more complex?

If traditional science was our only guide, then at this point we would probably be quite stuck. But my purpose in this book is precisely to develop a new kind of science that allows progress to be made in such cases. And in many respects the single most important idea that underlies this new science is the notion of computation.

Throughout this book I have referred to systems such as cellular automata as simple computer programs. So now the point is actually to think of these systems in terms of the computations they can perform.

In a typical case, the initial conditions for a system like a cellular automaton can be viewed as corresponding to the input to a computation, while the state of the system after some number of steps corresponds to the output. And the key idea is then to think in purely abstract terms about the computation that is performed, without necessarily looking at all the details of how it actually works.

Why is such an abstraction useful? The main reason is that it potentially allows one to discuss in a unified way systems that have completely different underlying rules. For even though the internal workings of two systems may have very little in common, the computations the systems perform may nevertheless be very similar.

And by thinking in terms of such computations, it then becomes possible to imagine formulating principles that apply to a very wide variety of different systems, quite independent of the detailed structure of their underlying rules.

#### Computations in Cellular Automata

I have said that the evolution of a system like a cellular automaton can be viewed as a computation. But what kind of computation is it, and how does it compare to computations that we typically do in practice?

The pictures below show an example of a cellular automaton whose evolution can be viewed as performing a particular simple computation.

If one starts this cellular automaton with an even number of black cells, then after a few steps of evolution, no black cells are left. But if instead one starts it with an odd number of black cells, then a single black cell survives forever. So in effect this cellular automaton can be viewed as computing whether a given number is even or odd.

![](Images/_page_653_Picture_9.jpeg)

![](Images/_page_653_Picture_10.jpeg)

A simple cellular automaton whose evolution effectively computes the remainder after division of a number by 2. Starting from a row of n black cells, 0 black cells survive if n is even, and 1 black cell survives if n is odd. The cellular automaton follows elementary rule 132, as shown on the left.

One specifies the input to the computation by setting up an appropriate number of initial black cells. And then one determines the result of the computation by looking at how many black cells survive in the end.

Testing whether a number is even or odd is by most measures a rather simple computation. But one can also get cellular automata to do more complicated computations. And as an example the pictures below show a cellular automaton that computes the square of any number. If one starts say with 5 black squares, then after a certain number of steps the cellular automaton will produce a block of exactly $5 \times 5 = 25$ black squares.

![](Images/_page_654_Figure_3.jpeg)

A cellular automaton that computes the square of any number. The cellular automaton effectively works by adding the original number n together n times. The underlying rule used here involves eight possible colors for each cell.

At first it might seem surprising that a system with the simple underlying structure of a cellular automaton could ever be made to perform such a computation. But as we shall see later in this chapter, cellular automata can in fact perform what are in effect arbitrarily sophisticated computations. And as one example of a somewhat more sophisticated computation, the picture on the next page shows a cellular automaton that computes the successive prime numbers: 2, 3, 5, 7, 11, 13, 17, etc.

The rule for this cellular automaton is somewhat complicated. It involves a total of sixteen colors possible for each cell, but the example demonstrates the point that in principle a cellular automaton can compute the primes.

![](Images/_page_655_Picture_2.jpeg)

A cellular automaton constructed to compute the prime numbers. The system generates a dark gray stripe on the left at all positions that correspond to any product of numbers other than 1. White gaps then remain at positions that correspond to the prime numbers 2, 3, 5, 7, 11, 13, 17, etc. The cellular automaton effectively does its computation using the standard sieve of Eratosthenes method. The structures on the right bounce backwards and forwards with repetition periods corresponding to successive odd numbers. Once in each period they produce a gray stripe which propagates to the left, so that in the end there is a gray stripe corresponding to every multiple of every number. The rule for the cellular automaton shown here involves 16 possible colors for each cell.

So what about the cellular automata that we discussed earlier in this book? What kinds of computations can they perform?

At some level, any cellular automaton, or for that matter, any system whatsoever, can be viewed as performing a computation that determines what its future behavior will be.

But for the cellular automata that I have discussed in this section, it so happens that the computations they perform can also conveniently be described in terms of traditional mathematical notions.

And this turns out to be possible for some of the cellular automata that I discussed earlier in this book. Thus, for example, as shown below, rule 94 can effectively be described as enumerating even numbers. Similarly, rule 62 can be thought of as enumerating numbers that are multiples of 3, while rule 190 enumerates numbers that are multiples of 4. And if one looks down the center column of the pattern it produces, rule 129 can be thought of as enumerating numbers that are powers of 2.

![](Images/_page_656_Figure_5.jpeg)

![](Images/_page_656_Figure_6.jpeg)

![](Images/_page_656_Figure_7.jpeg)

![](Images/_page_656_Figure_8.jpeg)

Examples of simple cellular automata whose evolution corresponds to computations that can easily be described in traditional mathematical terms. In analogy to the previous page, the positions of white cells at the bottom of the rule 94 picture correspond to even numbers, on the left in rule 62 to multiples of 3, in rule 190 to multiples of 4, and in the center column of rule 129 to powers of 2.

But what kinds of computations are cellular automata like the ones on the right performing? If we compare the patterns they produce to the patterns we have seen so far in this section, then immediately we suspect that we cannot describe these computations by anything as simple as saying, for example, that they generate primes.

So how then can we ever expect to describe these computations? Traditional mathematics is not much help, but what we will see is that there are a collection of ideas familiar from practical computing that provide at least the beginnings of the framework that is needed.

Examples of cellular automata that have simple underlying rules but whose overall behavior does not seem to correspond to computations with any kind of simple description in standard mathematical or other terms.

![](Images/_page_656_Picture_13.jpeg)

![](Images/_page_656_Picture_14.jpeg)

Rule 45

![](Images/_page_656_Picture_16.jpeg)

Rule 73

#### The Phenomenon of Universality

In the previous section we saw that it is possible to get cellular automata to perform some fairly sophisticated computations. But for each specific computation we wanted to do, we always set up a cellular automaton with a different set of underlying rules. And indeed our everyday experience with mechanical and other devices might lead us to assume that in general in order to perform different kinds of tasks we must always use systems that have different underlying constructions.

But the remarkable discovery that launched the computer revolution is that this is not in fact the case. And instead, it is possible to build universal systems whose underlying construction remains fixed, but which can be made to perform different tasks just by being programmed in different ways.

And indeed, this is exactly how practical computers work: the hardware of the computer remains fixed, but the computer can be programmed for different tasks by loading different pieces of software.

The idea of universality is also the basis for computer languages. For in each language, there are a certain set of primitive operations, which are then strung together in different ways to create programs for different tasks.

The details of a particular computer system or computer language will certainly affect how easy it is to perform a particular task. But the crucial fact that is by now a matter of common knowledge is that with appropriate programming any computer system or computer language can ultimately be made to perform exactly the same set of tasks.

One way to see that this must be true is to note that any particular computer system or computer language can always be set up by appropriate programming to emulate any other one.

Typically the way this is done is by having each individual action in the system that is to be emulated be reproduced by some sequence of actions in the other system. And indeed this is ultimately how, for example, *Mathematica* works. For when one enters a command such as `Log[15]`, what actually happens is that the program which implements the *Mathematica* language interprets this command by executing the appropriate sequence of machine instructions on whatever computer system one is using.

And having now identified the phenomenon of universality in the context of practical computing, one can immediately see various analogs of it in other areas of common experience. Human languages provide an example. For one knows that given a single fixed underlying language, it is possible to describe an almost arbitrarily wide range of things. And given any two languages, it is for the most part always possible to translate between them.

So what about natural science? Is the phenomenon of universality also relevant there? Despite its great importance in computing and elsewhere, it turns out that universality has in the past never been considered seriously in relation to natural science.

But what I will show in this chapter and the next is that in fact universality is for example quite crucial in finding general ways to characterize and understand the complexity we see in natural systems.

The basic point is that if a system is universal, then it must effectively be capable of emulating any other system, and as a result it must be able to produce behavior that is as complex as the behavior of any other system. So knowing that a particular system is universal thus immediately implies that the system can produce behavior that is in a sense arbitrarily complex.

But now the question is what kinds of systems are in fact universal.

Most present-day mechanical devices, for example, are built only for rather specific tasks, and are not universal. And among electronic devices there are examples such as simple calculators and electronic address books that are not universal. But by now the vast majority of practical electronic devices, despite all their apparent differences, are based on computers that are universal.

At some level, however, these computers tend to be extremely similar. Indeed, essentially all of them are based on the same kinds of logic circuits, the same basic layout of data paths, and so on. And knowing this, one might conclude that any system which was universal must include direct analogs of these specific elements. But from experience with computer languages, there is already an indication that the range of systems that are universal might be somewhat broader.

Indeed, *Mathematica* turns out to be a particularly good example, in which one can pick very different sets of operations to use, and yet still be able to implement exactly the same kinds of programs.

So what about cellular automata and other systems with simple rules? Is it possible for these kinds of systems to be universal?

At first, it seems quite implausible that they could be. For the intuition that one gets from practical computers and computer languages seems to suggest that to achieve universality there must be some fundamentally fairly sophisticated elements present.

But just as we found that the intuition which suggests that simple rules cannot lead to complex behavior is wrong, so also the intuition that simple rules cannot be universal also turns out to be wrong. And indeed, later in this chapter, I will show an example of a cellular automaton with an extremely simple underlying rule that can nevertheless in the end be seen to be universal.

In the past it has tended to be assumed that universality is somehow a rare and special quality, usually possessed only by systems that are specifically constructed to have it. But one of the results of this chapter is that in fact universality is a much more widespread phenomenon. And in the next chapter I will argue that for example it also occurs in a wide range of important systems that we see in nature.

#### A Universal Cellular Automaton

As our first specific example of a system that exhibits universality, I discuss in this section a particular universal cellular automaton that has been set up to make its operation as easy to follow as possible.

The rules for this cellular automaton itself are always the same. But the fact that it is universal means that if it is given appropriate initial conditions it can effectively be programmed to emulate for example any possible cellular automaton, with any set of rules.

The next three pages show three examples of this.

![](Images/_page_660_Picture_1.jpeg)

![](Images/_page_660_Picture_2.jpeg)

The universal cellular automaton emulating elementary rule 254. Each cell in rule 254 is represented by a block of 20 cells in the universal cellular automaton. Each of these blocks encodes both the color of the cell it represents, and the rule for updating this color.

![](Images/_page_660_Figure_4.jpeg)

![](Images/_page_661_Picture_2.jpeg)

The universal cellular automaton emulating elementary rule 90. The underlying rules for the universal cellular automaton are exactly the same as on the previous page. But each block in the initial conditions now contains a representation of rule 90 rather than rule 254.

![](Images/_page_661_Picture_4.jpeg)

![](Images/_page_661_Picture_5.jpeg)

![](Images/_page_662_Picture_1.jpeg)

![](Images/_page_662_Picture_2.jpeg)

The universal cellular automaton emulating rule 30. A total of 848 steps in the evolution of the universal cellular automaton are shown, corresponding to 16 steps in the evolution of rule 30.

![](Images/_page_662_Picture_4.jpeg)

On each page the underlying rules for the universal cellular automaton are exactly the same. But on the first page, the initial conditions are set up so as to make the universal cellular automaton emulate rule 254, while on the second page they are set up to make it emulate rule 90, and on the third page rule 30.

The pages that follow show how this works. The basic idea is that a block of 20 cells in the universal cellular automaton is used to represent each single cell in the cellular automaton that is being emulated. And within this block of 20 cells is encoded both a specification of the current color of the cell that is being represented, as well as the rule by which that color is to be updated.

![](Images/_page_663_Picture_3.jpeg)

The rules for the universal cellular automaton. There are 19 possible colors for each cell, represented here by 19 different icons. Since the new color of each cell depends on the previous colors of a total of five cells, there are in principle 2,476,099 cases to cover. But by using a symbol to stand for a cell with any possible color, many cases are combined. Note that the cases shown are in a definite order reading down successive columns, with special cases given before more general ones. With the initial conditions used, there are some combinations of cells that can never occur, and these are not covered in the rules shown.

![](Images/_page_664_Picture_1.jpeg)

Details of how the universal cellular automaton emulates rule 254. Each of the blocks in the universal cellular automaton represents a single cell in rule 254, and encodes both the current color of the cell and the form of the rule used to update it.

![](Images/_page_664_Picture_3.jpeg)

![](Images/_page_665_Figure_1.jpeg)

Details of how the universal cellular automaton emulates rule 90. The only difference in initial conditions from the picture on the previous page is that each block now encodes rule 90 instead of rule 254.

![](Images/_page_665_Figure_3.jpeg)

![](Images/_page_666_Figure_1.jpeg)

Details of how the universal cellular automaton emulates rule 30. Once again, the only difference in initial conditions from the facing page is that each block now encodes rule 30 instead of rule 90.

![](Images/_page_666_Figure_3.jpeg)

In the examples shown, the cellular automata being emulated have 8 cases in their rules, with each case giving the outcome for one of the 8 possible combinations of colors of a cell and its immediate neighbors. In every block of 20 cells in the universal cellular automaton, these rules are encoded in a very straightforward way, by listing in order the outcomes for each of the 8 possible cases.

To update the color of the cell represented by a particular block, what the universal cellular automaton must then do is to determine which of the 8 cases applies to that cell. And it does this by successively eliminating cases that do not apply, until eventually only one case remains. This process of elimination can be seen quite directly in the pictures on the previous pages. Below each large black or white triangle, there are initially 8 vertical dark lines. Each of these lines corresponds to one of the 8 cases in the rule, and the system is set up so that a particular line ends as soon as the case to which it corresponds has been eliminated.

It so happens that in the universal cellular automaton discussed here the elimination process for a given cell always occurs in the block immediately to the left of the one that represents that cell. But the process itself is not too difficult to understand, and indeed it works in much the way one might expect of a practical electronic logic circuit.

There are three basic stages, visible in the pictures as three stripes moving to the left across each block. The first stripe carries the color of the left-hand neighbor, and causes all cases in the rule where that neighbor does not have the appropriate color to be eliminated. The next two stripes then carry the color of the cell itself and of its right-hand neighbor. And after all three stripes have passed, only one of the 8 cases ever survives, and this case is then the one that gives the new color for the cell.

The pictures on the last few pages have shown how the universal cellular automaton can in effect be programmed to emulate any cellular automaton whose rules involve nearest neighbors and two possible colors for each cell. But the universal cellular automaton is in no way restricted to emulating only rules that involve nearest neighbors. And thus on the facing page, for example, it is shown emulating a rule that involves next-nearest as well as nearest neighbors.

![](Images/_page_668_Figure_2.jpeg)

The universal cellular automaton emulating one step in the evolution of the rule shown above, which involves next-nearest as well as nearest-neighbor cells. The rule now covers a total of 32 cases, corresponding to the possible arrangements of colors of a cell and its nearest and next-nearest neighbors. The picture shows the evolution of five cells according to the rule shown, with each cell now being represented by a block of 70 cells in the universal cellular automaton.

The blocks needed to represent each cell are now larger, since they must include all 32 cases in the rule. There are also five elimination stages rather than three. But despite these differences, the underlying rule for the universal cellular automaton remains exactly the same.

What about rules that have more than two possible colors for each cell? It turns out that there is a general way of emulating such rules by using rules that have just two colors but a larger number of neighbors. The picture on the facing page shows an example. The idea is that each cell in the three-color cellular automaton is represented by a block of three cells in the two-color cellular automaton. And by looking at neighbors out to distance five on each side, the two-color cellular automaton can update these blocks at each step in direct correspondence with the rules of the three-color cellular automaton.

The same basic scheme can be used for rules with any number of colors. And the conclusion is therefore that the universal cellular automaton can ultimately emulate a cellular automaton with absolutely any set of rules, regardless of how many neighbors and how many colors they may involve.

This is an important and at first surprising result. For among other things, it implies that the universal cellular automaton can emulate cellular automata whose rules are more complicated than its own. If one did not know about the basic phenomenon of universality, then one would most likely assume that by using more complicated rules one would always be able to produce new and different kinds of behavior.

But from studying the universal cellular automaton in this section, we now know that this is not in fact the case. For given the universal cellular automaton, it is always in effect possible to program this cellular automaton to emulate any other cellular automaton, and therefore to produce whatever behavior the other cellular automaton could produce.

In a sense, therefore, what we can now see is that nothing fundamental can ever be gained by using rules that are more complicated than those for the universal cellular automaton. For given the universal cellular automaton, more complicated rules can always be emulated just by setting up appropriate initial conditions.

![](Images/_page_670_Figure_1.jpeg)

An example of how a cellular automaton with three possible colors and nearest-neighbor rules can be emulated by a cellular automaton with only two possible colors but a larger number of neighbors (in this case five on each side). The basic idea is to represent each cell in the three-color rule by a block of three cells in the two-color rule, according to the correspondence given on the left. The three-color rule illustrated here is totalistic code 1599 from page 70.

Looking at the specific universal cellular automaton that we have discussed in this section, however, we would probably be led to assume that while the phenomenon of universality might be important in principle, it would rarely be relevant in practice. For the rules of the universal cellular automaton in this section are quite complicated, involving 19 possible colors for each cell, and next-nearest as well as nearest neighbors. And if such complication was indeed necessary in order to achieve universality, then one would not expect that universality would be common, for example, in the systems we see in nature.

But what we will discover later in this chapter is that such complication in underlying rules is in fact not needed. Indeed, in the end we will see that universality can actually occur in cellular automata with just two colors and nearest neighbors. The operation of such cellular automata is considerably more difficult to follow than the operation of the universal cellular automaton discussed in this section. But the existence of universal cellular automata with such simple underlying rules makes it clear that the basic results we have obtained in this section are potentially of very broad significance.

#### Emulating Other Systems with Cellular Automata

The previous section showed that a particular universal cellular automaton could emulate any possible cellular automaton. But what about other types of systems? Can cellular automata also emulate these?

With their simple and rather specific underlying structure one might think that cellular automata would never be capable of emulating a very wide range of other systems. But what I will show in this section is that in fact this is not the case, and that in the end cellular automata can actually be made to emulate almost every single type of system that we have discussed in this book.

As a first example of this, the picture on the facing page shows how a cellular automaton can be made to emulate a mobile automaton.

The main difference between a mobile automaton and a cellular automaton is that in a mobile automaton there is a special active cell that moves around from one step to the next, while in a cellular automaton all cells are always effectively treated as being exactly the same.

![](Images/_page_672_Picture_1.jpeg)

An example of a mobile automaton (see page 71) being emulated by a cellular automaton. In the mobile automaton shown on the left each cell has two possible colors. In the cellular automaton shown on the right, the cells have four possible colors, with two darker colors corresponding to the active cell in the mobile automaton. The rules for the mobile automaton and the cellular automaton are shown below. In the rules for the cellular automaton, $\boxminus$ indicates a cell of any color.

![](Images/_page_672_Picture_3.jpeg)

![](Images/_page_672_Picture_4.jpeg)

And to emulate a mobile automaton with a cellular automaton it turns out that all one need do is to divide the possible colors of cells in the cellular automaton into two sets: lighter ones that correspond to ordinary cells in the mobile automaton, and darker ones that correspond to active cells. And then by setting up appropriate rules and choosing initial conditions that contain only one darker cell, one can produce in the cellular automaton an exact emulation of every step in the evolution of a mobile automaton, as in the picture above.

The same basic approach can be used to construct a cellular automaton that emulates a Turing machine, as illustrated on the next page. Once again, lighter colors in the cellular automaton represent ordinary cells in the Turing machine, while darker colors represent the cell under the head, with a specific darker color corresponding to each possible state of the head.

One might think that the reason that mobile automata and Turing machines can be emulated by cellular automata is that they both consist of fixed arrays of cells, just like cellular automata. So then one may wonder what happens with substitution systems, for example, where there is no fixed array of elements.

![](Images/_page_673_Figure_1.jpeg)

![](Images/_page_673_Figure_2.jpeg)

![](Images/_page_673_Figure_3.jpeg)

The pictures on the facing page demonstrate that in fact these can also be emulated by cellular automata. But while one can emulate each step in the evolution of a mobile automaton or a Turing machine with a single step of cellular automaton evolution, this is no longer in general true for substitution systems.

That this must ultimately be the case one can see from the fact that the total number of elements in a substitution system can be multiplied by a factor from one step to the next, while in a cellular automaton the size of a pattern can only ever increase by a fixed amount at each step. And what this means is that it can take progressively larger numbers of cellular automaton steps to reproduce each successive step in the evolution of the substitution system, as illustrated in the pictures on the facing page.

The same kind of problem occurs in sequential substitution systems, as well as in tag systems. But once again, as the pictures on page 660 demonstrate, it is still perfectly possible to emulate systems like these using cellular automata.

But just how broad is the set of systems that cellular automata can ultimately emulate? All the examples of systems that I have shown so far can at some level be thought of as involving sequences of elements that are fairly directly analogous to the cells in a cellular automaton.

![](Images/_page_674_Picture_2.jpeg)

![](Images/_page_675_Figure_1.jpeg)

A cellular automaton set up to emulate a sequential substitution system. The cellular automaton involves 28 colors and nearest-neighbor rules. The strings produced by the sequential substitution system appear on successive diagonal stripes indicated by arrows in the evolution of the cellular automaton on the right.

But one example where there is no such direct analogy is a register machine. And at the outset one might not imagine that such a system could ever readily be emulated by a cellular automaton.

But in fact it turns out to be fairly straightforward to do so, as illustrated at the top of the facing page. The basic idea is to have the cellular automaton produce a pattern that expands and contracts on each side in a way that corresponds to the incrementing and decrementing of the sizes of numbers in the first and second registers of the register machine.

![](Images/_page_676_Picture_1.jpeg)

![](Images/_page_676_Picture_2.jpeg)

An example of a register machine being emulated by a cellular automaton. The cellular automaton has 12 possible colors for each cell. Of these, 5 are used by the center cell to represent the point that has been reached in the register machine program. The other 7 are used to implement signals that propagate out to the left and right to do the analog of incrementing and decrementing each register.

In the center of the cellular automaton is then a cell whose possible colors correspond to possible points in the program for the register machine. And as the cell makes transitions from one color to another, it effectively emits signals that move to the left or right modifying the pattern in the cellular automaton in a way that follows each instruction in the register machine program.

So what about systems based on numbers? Can these also be emulated by cellular automata? As one example the picture on the right shows how a cellular automaton can be set up to perform repeated multiplication by 3 of numbers in base 2. And the only real difficulty in this case is that carries generated in the process of multiplication may need to be propagated from one end of the number to the other.

So what about practical computers? Can these also be emulated by cellular automata? From the examples just discussed of register machines and systems based on numbers, we already know that cellular automata can emulate some of the low-level operations typically found in computers. And the pictures on the next two pages show how cellular automata can also be made to emulate two other important aspects of practical computers.

![](Images/_page_676_Figure_7.jpeg)

Repeated multiplication by 3 in base 2 being performed by a cellular automaton with 11 colors.

The pictures below show how a cellular automaton can evaluate any logic expression that is given in a certain form. And the picture on the facing page then shows how a cellular automaton can retrieve data from a numbered location in what is effectively a random-access memory.

![](Images/_page_677_Figure_2.jpeg)

A cellular automaton which emulates basic logic circuits. The underlying rules for the cellular automaton are exactly the same in each case, and involve nearest neighbors and five possible colors for each cell. But the initial condition can represent a logic expression that involves any number of variables together with the operations of AND, OR and Not. In the examples above, two variables, p and q, are used, and in each case the behavior obtained with all four possible combinations of values for p and q are shown.

![](Images/_page_678_Figure_1.jpeg)

A cellular automaton set up to emulate random-access memory in a computer. The memory is on the right, and can be of any size. Instructions come in from the left, with memory locations specified by addresses consisting of binary digits.

The details for any particular case are quite complicated, but in the end it turns out that it is in principle possible to construct a cellular automaton that emulates a practical computer in its entirety.

And as a result, one can conclude that any of the very wide range of computations that can be performed by practical computers can also be done by cellular automata.

From the previous section we know that any cellular automaton can be emulated by a universal cellular automaton. But now we see that a universal cellular automaton is actually much more universal than we saw in the previous section. For not only can it emulate any cellular automaton: it can also emulate any of a wide range of other systems, including practical computers.

#### Emulating Cellular Automata with Other Systems

In the previous section we discovered the rather remarkable fact that cellular automata can be set up to emulate an extremely wide range of other types of systems. But is this somehow a special feature of cellular automata, or do other systems also have similar capabilities?

In this section we will discover that in fact almost all of the systems that we considered in the previous section, and in Chapter 3, have the same capabilities. And indeed just as we showed that each of these various systems could be emulated by cellular automata, so now we will show that these systems can emulate cellular automata.

As a first example, the pictures below show how mobile automata can be set up to emulate cellular automata. The basic idea is to have the active cell in the mobile automaton sweep backwards and forwards, updating cells as it goes, in such a way that after each complete sweep it has effectively performed one step of cellular automaton evolution.

![](Images/_page_679_Figure_5.jpeg)

Examples of mobile automata emulating cellular automata. In case (a) the rules for the mobile automaton are set up to emulate the rule 90 elementary cellular automaton; in case (b) they are set up to emulate rule 30. The pictures on the right are obtained by keeping only the steps indicated by arrows on the left, corresponding to times when the active cell in the mobile automaton is further to the left than it has ever been before. The mobile automata used here involve 7 possible colors for each cell.

The specific pictures at the bottom of the facing page are for elementary cellular automata with two possible colors for each cell and nearest-neighbor rules. But the same basic idea can be used for cellular automata with rules of any kind. And this implies that it is possible to construct for example a mobile automaton which emulates the universal cellular automata that we discussed a couple of sections ago.

Such a mobile automaton must then itself be universal, since the universal cellular automaton that it emulates can in turn emulate a wide range of other systems, including all possible mobile automata.

A similar scheme to the one for mobile automata can also be used for Turing machines, as illustrated in the pictures below. And once again, by emulating the universal cellular automaton, it is then possible to construct a universal Turing machine.

But as it turns out, a universal Turing machine was already constructed in 1936, using somewhat different methods. And in fact that universal Turing machine provided what was historically the very first clear example of universality seen in any system.

![](Images/_page_680_Figure_5.jpeg)

Examples of Turing machines that emulate cellular automata with rules 90 and 30. The pictures on the right are obtained by keeping only the steps indicated by arrows on the left. The Turing machines have 6 states and 3 possible colors for each cell.

Continuing with the types of systems from the previous section, we come next to substitution systems. And here, for once, we find that at least at first we cannot in general emulate cellular automata. For as we discussed on page 83, neighbor-independent substitution systems can generate only patterns that are either repetitive or nested, so they can never yield the more complicated patterns that are, for example, needed to emulate rule 30.

But if one generalizes to neighbor-dependent substitution systems then it immediately becomes very straightforward to emulate cellular automata, as in the pictures below.

![](Images/_page_681_Figure_3.jpeg)

Neighbor-dependent substitution systems that emulate cellular automata with rules 90 and 30. The systems shown are simple examples of neighbor-dependent substitution systems with highly uniform rules always yielding just one cell and corresponding quite directly to cellular automata.

What about sequential substitution systems? Here again it turns out to be fairly easy to emulate cellular automata, as the pictures at the top of the facing page demonstrate.

Perhaps more surprisingly, the same is also true for ordinary tag systems. And even though such systems operate in an extremely simple underlying way, the pictures at the bottom of the facing page demonstrate that they can still quite easily emulate cellular automata.

What about symbolic systems? The structure of these systems is certainly vastly different from cellular automata. But once again, as the picture at the top of page 668 shows, it is quite easy to get these systems to emulate cellular automata.

![](Images/_page_682_Figure_2.jpeg)

![](Images/_page_682_Figure_3.jpeg)

Sequential substitution systems that emulate cellular automata with rules 90 and 30. The pictures at the top above are obtained by keeping only the steps indicated by arrows on the left. The sequential substitution systems involve elements with 3 possible colors.

![](Images/_page_682_Figure_5.jpeg)

![](Images/_page_682_Figure_6.jpeg)

Tag systems that emulate the rule 90 and rule 30 cellular automata. The pictures at the top above are obtained by keeping only the steps indicated by arrows on the left. Both tag systems involve 6 colors.

![](Images/_page_683_Figure_1.jpeg)

Symbolic systems set up to emulate cellular automata that have rules 90 and 30. Unlike the examples of symbolic systems in Chapter 3, which involve only one symbol, these symbolic systems involve three symbols, p, q and r.

And as soon as one knows that any particular type of system is capable of emulating any cellular automaton, it immediately follows that there must be examples of that type of system that are universal.

So what about the other types of systems that we considered in Chapter 3? One that we have not yet discussed here are cyclic tag systems. And as it turns out, we will end up using just such systems later in this chapter as part of establishing a dramatic example of universality.

But to demonstrate that cyclic tag systems can manage to emulate cellular automata is not quite as straightforward as to do this for the various kinds of systems we have discussed so far. And indeed we will end up doing it in several stages. The first stage, illustrated in the picture at the top of the facing page, is to get a cyclic tag system to emulate an ordinary tag system with the property that its rules depend only on the very first element that appears at each step.

![](Images/_page_684_Figure_1.jpeg)

A cyclic tag system emulating a tag system that depends only on the first element at each step. In the expanded tag system evolution, successive colors of elements are encoded by having a black cell at successive positions inside a fixed block of white cells.

And having done this, the next stage is to get such a tag system to emulate a Turing machine. The pictures on the next page illustrate how this can be done. But at least with the particular construction shown, the resulting Turing machine can only have cells with two possible colors. The pictures below demonstrate, however, that such a Turing machine can readily be made to emulate a Turing machine with any number of colors. And through the construction of page 665 this then finally shows that a cyclic tag system can successfully emulate any cellular automaton, and can thus be universal.

![](Images/_page_684_Figure_4.jpeg)

![](Images/_page_684_Picture_5.jpeg)

Turing machines with two colors emulating ones with more colors.

![](Images/_page_685_Figure_2.jpeg)

Tag system compressed evolution (1500 steps)

Emulating a Turing machine with a tag system that depends only on the first element at each step. The configuration of cells on each side of the head in the Turing machine is treated as a base 2 number. At the steps indicated by arrows the tag system yields sequences of dark cells with lengths that correspond to each of these numbers.

This leaves only one remaining type of system from Chapter 3: register machines. And although it is again slightly complicated, the pictures on the next page, and below, show how even these systems can be made to emulate Turing machines and thus cellular automata.

![](Images/_page_686_Picture_3.jpeg)

So what about systems based on numbers, like those we discussed in Chapter 4? As an example, one can consider a generalization of the arithmetic systems discussed on page 122, in which one has a whole number n, and at each step one finds the remainder after dividing by a constant, and based on the value of this remainder one then applies some specified arithmetic operation to n.

![](Images/_page_687_Figure_1.jpeg)

An example of a register machine set up to emulate a Turing machine. The Turing machine used here has two states for the head; the register machine program has 72 instructions and uses three registers. The register machine compressed evolution keeps only steps corresponding to every other time the third register gets incremented from zero.

The picture below shows that such a system can be set up to emulate a register machine. And from the fact that register machines are universal it follows that so too are such arithmetic systems.

And indeed the fact that it is possible to set up a universal system using essentially just the operations of ordinary arithmetic is closely related to the proof of Gödel's Theorem discussed on page 784.

But from what we have learned in this chapter, it no longer seems surprising that arithmetic should be capable of achieving universality. Indeed, considering all the kinds of systems that we have found can exhibit universality, it would have been quite peculiar if arithmetic had somehow not been able to support it.

![](Images/_page_688_Figure_4.jpeg)

![](Images/_page_688_Picture_5.jpeg)

An example of how a simple arithmetic system can emulate a register machine. The arithmetic system takes the value n that it obtains at each step, computes `Mod[n, 30]`, and then depending on the result applies to n one of the arithmetic operations specified by the rule on the left below. The rule is set up so that if the value of n is written in the form $i + 5 \cdot 2^a \cdot 3^b$ then the values of i, a and b on successive steps correspond respectively to the position of the register machine in its program, and to the values of the two registers (2 and 3 appear because they are the first two primes; 5 appears because it is the length of the register machine program). The values of n in the pictures on the left are indicated on a logarithmic scale.

| 2 n + 1 | (n - 1)/3 | 3 (n - 1) | (n + 1)/2 | (n - 4)/3 | 2 n + 1 | n + 1 | 3 (n - 1) | n + 1 | n + 1 |
|---------|-----------|-----------|-----------|-----------|---------|-------|-----------|-------|-------|
| 0       | 1         | 2         | 3         | 4         | 5       | 6     | 7         | 8     | 9     |
| 2 n + 1 | n + 1     | 3 (n - 1) | (n + 1)/2 | n + 1     | 2 n + 1 | (n - 1)/3 | 3 (n - 1) | n + 1 | (n - 4)/3 |
| 10      | 11        | 12        | 13        | 14        | 15      | 16    | 17        | 18    | 19    |
| 2 n + 1 | n + 1     | 3 (n - 1) | (n + 1)/2 | n + 1     | 2 n + 1 | n + 1 | 3 (n - 1) | n + 1 | n + 1 |
| 20      | 21        | 22        | 23        | 24        | 25      | 26    | 27        | 28    | 29    |

#### Implications of Universality

When we first discussed cellular automata, Turing machines, substitution systems, register machines and so on in Chapter 3, each of these kinds of systems seemed rather different. But already in Chapter 3 we discovered that at the level of overall behavior, all of them had certain features in common. And now, finally, by thinking in terms of computation, we can begin to see why this might be the case.

The main point, as the previous two sections have demonstrated, is that essentially all of these various kinds of systems, despite their great differences in underlying structure, can ultimately be made to emulate each other.

This is a very remarkable result, and one which will turn out to be crucial to the new kind of science that I develop in this book.

In a sense its most important consequence is that it implies that from a computational point of view a very wide variety of systems, with very different underlying structures, are at some level fundamentally equivalent. For one might have thought that every different kind of system that we discussed for example in Chapter 3 would be able to perform completely different kinds of computations.

But what we have discovered here is that this is not the case. And instead it has turned out that essentially every single one of these systems is ultimately capable of exactly the same kinds of computations.

And among other things, this means that it really does make sense to discuss the notion of computation in purely abstract terms, without referring to any specific type of system. For we now know that it ultimately does not matter what kind of system we use: in the end essentially any kind of system can be programmed to perform the same computations. And so if we study computation at an abstract level, we can expect that the results we get will apply to a very wide range of actual systems.

But it should be emphasized that among systems of any particular type, say cellular automata, not all possible underlying rules are capable of supporting the same kinds of computations.

Indeed, as we saw at the beginning of this chapter, some cellular automata can perform only very simple computations, always yielding for example purely repetitive patterns. But the crucial point is that as one looks at cellular automata with progressively greater computational capabilities, one will eventually pass the threshold of universality. And once past this threshold, the set of computations that can be performed will always be exactly the same.

One might assume that by using more and more sophisticated underlying rules, one would always be able to construct systems with ever greater computational capabilities. But the phenomenon of universality implies that this is not the case, and that as soon as one has passed the threshold of universality, nothing more can in a sense ever be gained.

In fact, once one has a system that is universal, its properties are remarkably independent of the details of its construction. For at least as far as the computations that it can perform are concerned, it does not matter how sophisticated the underlying rules for the system are, or even whether the system is a cellular automaton, a Turing machine, or something else. And as we shall see, this rather remarkable fact forms the basis for explaining many of the observations we made in Chapter 3, and indeed for developing much of the conceptual framework that is needed for the new kind of science in this book.

#### The Rule 110 Cellular Automaton

In previous sections I have shown that a wide variety of different kinds of systems can in principle be made to exhibit the phenomenon of universality. But how complicated do the underlying rules need to be in a specific case in order actually to achieve universality?

The universal cellular automaton that I described earlier in this chapter had rather complicated underlying rules, involving 19 possible colors for each cell, depending on next-nearest as well as nearest neighbors. But this cellular automaton was specifically constructed so as to make its operation easy to understand. And by not imposing this constraint, one might expect that one would be able to find universal cellular automata that have at least somewhat simpler underlying rules.

Fairly straightforward modifications to the universal cellular automaton shown earlier in this chapter allow one to reduce the number of colors from 19 to 17. And in fact in the early 1970s, it was already known that cellular automata with 18 colors and nearest-neighbor rules could be universal. In the late 1980s, with some ingenuity, examples of universal cellular automata with 7 colors were also constructed.

But such rules still involve 343 distinct cases and are by almost any measure very complicated. And certainly rules this complicated could not reasonably be expected to be common in the types of systems that we typically see in nature. Yet from my experiments on cellular automata in the early 1980s I became convinced that very much simpler rules should also show universality. And by the mid-1980s I began to suspect that even among the very simplest possible rules, with just two colors and nearest neighbors, there might be examples of universality.

The leading candidate was what I called rule 110, a cellular automaton that we have in fact discussed several times before in this book. Like any of the 256 so-called elementary rules, rule 110 can be specified as below by giving the outcome for each of the eight possible combinations of colors of a cell and its nearest neighbors.

![](Images/_page_691_Picture_5.jpeg)

The underlying rules for the rule 110 cellular automaton discussed in this section. As elsewhere in the book, each of the eight cases shows what the new color of a cell should be based on its own previous color, and on the previous colors of its neighbors. Despite the extreme simplicity of its underlying rules, what this section will demonstrate is that the rule 110 cellular automaton is in fact universal, and is thus in a sense capable of arbitrarily complex behavior. If the values of the cells in each block are labelled p, q and r, then rule 110 can be written as `Mod[(1 + p) q r + q + r, 2]` or $\neg (p \land q \land r) \land (q \lor r)$.

Looking just at this very simple specification, however, it seems at first quite absurd to think that rule 110 might be universal. But as soon as one looks at a picture of how rule 110 actually behaves, the idea that it could be universal starts to seem much less absurd. For despite the simplicity of its underlying rules, rule 110 supports a whole variety of localized structures that move around and interact in many complicated ways. And from pictures like the one on the facing page, it begins to seem not unreasonable that perhaps these localized structures could be arranged so as to perform meaningful computations.

![](Images/_page_692_Picture_1.jpeg)

A typical example of the behavior of rule 110 with random initial conditions. From looking at pictures like these one can begin to imagine that it could be possible to arrange localized structures in rule 110 so as to be able to perform meaningful computations. Note that page 292 already showed many of the types of localized structures that can occur in rule 110.

In the universal cellular automaton that we discussed earlier in this chapter, each of the various kinds of components involved in its operation had properties that were explicitly built into the underlying rules. Indeed, in most cases each different type of component was simply represented by a different color of cell. But in rule 110 there are only two possible colors for each cell. So one may wonder how one could ever expect to represent different kinds of components.

The crucial idea is to build up components from combinations of localized structures that the rule in a sense already produces. And if this works, then it is in effect a very economical solution. For it potentially allows one to get a large number of different kinds of components without ever needing to increase the complexity of the underlying rules at all.

But the problem with this approach is that it is typically very difficult to see how the various structures that happen to occur in a particular cellular automaton can be assembled into useful components.

And indeed in the case of rule 110 it took several years of work to develop the necessary ideas and tools. But finally it has turned out to be possible to show that the rule 110 cellular automaton is in fact universal.

It is truly remarkable that a system with such simple underlying rules should be able to perform what are in effect computations of arbitrary sophistication, but that is what its universality implies.

So how then does the proof of universality proceed?

The basic idea is to show that rule 110 can emulate any possible system in some class of systems where there is already known to be universality. And it turns out that a convenient such class of systems are the cyclic tag systems that we introduced on page 95.

Earlier in this chapter we saw that it is possible to construct a cyclic tag system that can emulate any given Turing machine. And since we know that at least some Turing machines are universal, this fact then establishes that universal cyclic tag systems are possible.

So if we can succeed in demonstrating that rule 110 can emulate any cyclic tag system, then we will have managed to prove that rule 110 is itself universal. The sequence of pictures on the facing page shows the beginnings of what is needed. The basic idea is to start from the usual representation of a cyclic tag system, and then progressively to change this representation so as to get closer and closer to what can actually be emulated directly by rule 110.

Picture (a) shows an example of the evolution of a cyclic tag system in the standard representation from pages 95 and 96. Picture (b) then shows another version of this same evolution, but now rearranged so that each element stays in the same position, rather than always shifting to the left at each step.

![](Images/_page_694_Picture_1.jpeg)

![](Images/_page_694_Picture_2.jpeg)

![](Images/_page_694_Picture_3.jpeg)

![](Images/_page_694_Picture_4.jpeg)

Four views of a cyclic tag system with rules as shown above, drawn so as to be progressively closer to what can be emulated directly in rule 110. Picture (a) shows the cyclic tag system in the same form as on pages 95 and 96. Picture (b) shows the system with sequences on successive steps rearranged so that they do not shift to the left when the first element is removed. Picture (c) is a skewed version of (b) in which the way information is used from the underlying rules at each step is explicitly indicated. Picture (d) shows a more definite mechanism for the evolution of the system in which different lines effectively indicate the motions of different pieces of information.

![](Images/_page_694_Picture_6.jpeg)

A cyclic tag system in general operates by removing the first element from the sequence that exists at each step, and then adding a new block of elements to the end of the sequence if this element is black. A crucial feature of cyclic tag systems is that the choice of what block of elements can be added does not depend in any way on the form of the sequence. So, for example, on the previous page, there are just two possibilities, and these possibilities alternate on successive steps.

Pictures (a) and (b) on the previous page illustrate the consequences of applying the rules for a cyclic tag system, but in a sense give no indication of an explicit mechanism by which these rules might be applied. In picture (c), however, we see the beginnings of such a mechanism.

The basic idea is that at each step in the evolution of the system, there is a stripe that comes in from the left carrying information about the block that can be added at that step. Then when the stripe hits the first element in the sequence that exists at that step, it is allowed to pass only if the element is black. And once past, the stripe continues to the right, finally adding the block it represents to the end of the sequence.

But while picture (c) shows the effects of various lines carrying information around the system, it gives no indication of why the lines should behave in the way they do. Picture (d), however, shows a much more explicit mechanism. The collections of lines coming in from the left represent the blocks that can be added at successive steps. The beginning of each block is indicated by a dashed line, while the elements within the block are indicated by solid black and gray lines.

When a dashed line hits the first element in the sequence that exists at a particular step, it effectively bounces back in the form of a line propagating to the left that carries the color of the first element.

When this line is gray, it then absorbs all other lines coming from the left until the next dashed line arrives. But when the line is black, it lets lines coming from the left through. These lines then continue until they collide with gray lines coming from the right, at which point they generate a new element with the same color as their own.

By looking at picture (d), one can begin to see how it might be possible for a cyclic tag system to be emulated by rule 110: the basic idea is to have each of the various kinds of lines in the picture be emulated by some collection of localized structures in rule 110.

![](Images/_page_696_Picture_2.jpeg)

Objects constructed from localized structures in rule 110, used for the emulation of cyclic tag systems. Each of the pictures shown is 500 cells wide. The objects in the top two pictures correspond to the thick vertical black and gray lines in picture (d) on page 679. The objects in the next two pictures correspond to the dark and light gray lines that come in from the left in picture (d). (Note that all the structures are left-right reversed in rule 110.) The third pair of pictures correspond to two versions of the dashed lines in picture (d). And the fourth pair of pictures correspond to right-going lines on the right-hand side of picture (d). All the localized structures involved in the pictures above were shown individually on page 292. Note that the spacings between structures are crucial in determining the objects they represent.

But at the outset it is by no means clear that collections of localized structures can be found that will behave in appropriate ways.

With some effort, however, it turns out to be possible to find the necessary constructs, and indeed the previous page shows various objects formed from localized structures in rule 110 that can be used to emulate most of the types of lines in picture (d) on page 679.

The first two pictures show objects that correspond to the black and white elements indicated by thick vertical lines in picture (d). Both of these objects happen to consist of the same four localized structures, but the objects are distinguished by the spacings between these structures.

The second two pictures on the previous page use the same idea of different spacings between localized structures to represent the black and gray lines shown coming in from the left in picture (d) on page 679.

Note that because of the particular form of rule 110, the objects in the second two pictures on the previous page move to the left rather than to the right. And indeed in setting up a correspondence with rule 110, it is convenient to left-right reverse all pictures of cyclic tag systems. But using the various objects from the previous page, together with a few others, it is then possible to set up a complete emulation of a cyclic tag system using rule 110.

The diagram on the facing page shows schematically how this can be done. Every line in the diagram corresponds to a single localized structure in rule 110, and although the whole diagram cannot be drawn completely to scale, the collisions between lines correctly show all the basic interactions that occur between structures.

The next several pages then give details of what happens in each of the regions indicated by circles in the schematic diagram.

Region (a) shows a block separator, corresponding to a dashed line in picture (d) on page 679, hitting the single black element in the sequence that exists at the first step. Because the element hit is black, an object must be produced that allows information from the block at this step to pass through. Most of the activity in region (a) is concerned with producing such an object. But it turns out that as a side-effect two additional localized structures are produced that can be seen propagating to the left. These structures could later cause trouble, but looking at region (b) we see that in fact they just pass through other structures that they meet without any adverse effect.

![](Images/_page_698_Picture_1.jpeg)

A schematic diagram of how rule 110 can be made to emulate a cyclic tag system. Each line in this diagram corresponds to one localized structure in rule 110. Note that the relative slopes of the structures are reproduced faithfully here, but their spacings are not. Note also that lines shown in different colors here often correspond to the same structure in rule 110.

![](Images/_page_699_Picture_1.jpeg)

Close-ups of circled regions shown schematically on the previous page. Each picture is 320 cells wide and shows 1200 evolution steps.

![](Images/_page_700_Picture_1.jpeg)

Close-ups (continued).

![](Images/_page_701_Picture_1.jpeg)

Region (c) shows what happens when the information corresponding to one element in a block passes through the kind of object produced in region (a). The number of localized structures that represent the element is reduced from twelve to four, but the spacings of these structures continue to specify its color. Region (d) then shows how the object in region (c) comes to an end when the beginning of the block separator from the next step arrives.

Region (e) shows how the information corresponding to a black element in a block is actually converted to a new black element in the sequence produced by the cyclic tag system. What happens is that the four localized structures corresponding to the element in the block collide with four other localized structures travelling in the opposite direction, and the result is four stationary structures that correspond to the new element in the sequence.

Region (f) shows the same process as region (e) but for a white element. The fact that the element is white is encoded in the wider spacing of the structures coming from the right, which results in narrower spacing of the stationary structures.

Region (g) shows the analog of region (a), but now for a white element instead of a black one. The region begins much like region (a), except that the four localized structures at the top are more narrowly spaced. Starting around the middle of the region, however, the behavior becomes quite different from region (a): while region (a) yields an object that allows information to pass through, region (g) yields one that stops all information, as shown in regions (h) and (i).

Note that even though they begin very differently, regions (d) and (i) end in the same way, reflecting the fact that in both cases the system is ready to handle a new block, whatever that block may be.

The pictures on the last few pages were all made for a cyclic tag system with a specific underlying rule. But exactly the same principles can be used whatever the underlying rule is. And the pictures below show schematically what happens with a few other choices of rules.

The way that the lines interact in the interior of each picture is always exactly the same. But what changes when one goes from one rule to another is the arrangement of lines entering the picture.

In the way that the pictures are drawn below, the blocks that appear in each rule are encoded in the pattern of lines coming in from the left edge of the picture. But if each picture were extended sufficiently far to the left, then all these lines would eventually be seen to start from the top. And what this means is that the arrangement of lines can therefore always be viewed as an initial condition for the system.

![](Images/_page_703_Picture_5.jpeg)

Schematic diagrams of how cyclic tag systems with four different underlying rules can be emulated. The lines in each diagram correspond essentially to collections of localized structures in rule 110. The processes that occur in the interior of each picture are always the same; the different cyclic tag system rules are implemented by different arrangements of lines entering each picture.

This is then finally how universality is achieved in rule 110. The idea is just to set up initial conditions that correspond to the blocks that appear in the rule for whatever cyclic tag system one wants to emulate.

The necessary initial conditions consist of repetitions of blocks of cells, where each of these blocks contains a pattern of localized structures that corresponds to the block of elements that appear in the rule for the cyclic tag system. The blocks of cells are always quite complicated, for the cyclic tag system discussed in most of this section they are each more than 3000 cells wide, but the crucial point is that such blocks can be constructed for any cyclic tag system. And what this means is that with suitable initial conditions, rule 110 can in fact be made to emulate any cyclic tag system.

It should be mentioned at this point however that there are a few additional complications involved in setting up appropriate initial conditions to make rule 110 emulate many cyclic tag systems. For as the pictures earlier in this section demonstrate, the way we have made rule 110 emulate cyclic tag systems relies on many details of the interactions between localized structures in rule 110. And it turns out that to make sure that with the specific construction used the appropriate interactions continue to occur at every step, one must put some constraints on the cyclic tag systems being emulated.

In essence, these constraints end up being that the blocks that appear in the rule for the cyclic tag system must always be a multiple of six elements long, and that there must be some bound on the number of steps that can elapse between the addition of successive new elements to the cyclic tag system sequence.

Using the ideas discussed on page 669, it is not difficult, however, to make a cyclic tag system that satisfies these constraints, but that emulates any other cyclic tag system. And as a result, we may therefore conclude that rule 110 can in fact successfully emulate absolutely any cyclic tag system. And this means that rule 110 is indeed universal.

#### The Significance of Universality in Rule 110

Practical computers and computer languages have traditionally been the only common examples of universality that we ever encounter. And from the fact that these kinds of systems tend to be fairly complicated in their construction, the general intuition has developed that any system that manages to be universal must somehow also be based on quite complicated underlying rules.

But the result of the previous section shows in a rather spectacular way that this is not the case. It would have been one thing if we had found an example of a cellular automaton with say four or five colors that turned out to be universal. But what in fact we have seen is that a cellular automaton with one of the very simplest possible 256 rules manages to be universal.

So what are the implications of this result? Most important is that it suggests that universality is an immensely more common phenomenon than one might otherwise have thought. For if one knew only about practical computers and about systems like the universal cellular automaton discussed early in this chapter, then one would probably assume that universality would rarely if ever be seen outside of systems that were specifically constructed to exhibit it.

But knowing that a system like rule 110 is universal, the whole picture changes, and now it seems likely that instead universality should actually be seen in a very wide range of systems, including many with rather simple rules.

A couple of sections ago we discussed the fact that as soon as one has a system that is universal, adding further complication to its rules cannot have any fundamental effect. For by virtue of its universality the system can always ultimately just emulate the behavior that would be obtained with any more complicated set of rules.

So what this means is that if one looks at a sequence of systems with progressively more complicated rules, one should expect that the overall behavior they produce will become more complex only until the threshold of universality is reached. And as soon as this threshold is passed, there should then be no further fundamental changes in what one sees.

The practical importance of this phenomenon depends greatly however on how far one has to go to get to the threshold of universality.

But knowing that a system like rule 110 is universal, one now suspects that this threshold is remarkably easy to reach. And what this means is that beyond the very simplest rules of any particular kind, the behavior that one sees should quickly become as complex as it will ever be.

Remarkably enough, it turns out that this is essentially what we already observed in Chapter 3. Indeed, not only for cellular automata but also for essentially all of the other kinds of systems that we studied, we found that highly complex behavior could be obtained even with rather simple rules, and that adding further complication to these rules did not in most cases noticeably affect the level of complexity that was produced.

So in retrospect the results of Chapter 3 should already have suggested that simple underlying rules such as rule 110 might be able to achieve universality. But what the elaborate construction in the previous section has done is to show for certain that this is the case.

#### Class 4 Behavior and Universality

If one looks at the typical behavior of rule 110 with random initial conditions, then the most obvious feature of what one sees is that there are a large number of localized structures that move around and interact with each other in complicated ways. But as we saw in Chapter 6, such behavior is by no means unique to rule 110. Indeed, it is in fact characteristic of all cellular automata that lie in what I called class 4.

The pictures on the next page show a few examples of such class 4 systems. And while the details are different in each case, the general features of the behavior are always rather similar.

So what does this mean about the computational capabilities of such systems? I strongly suspect that it is true in general that any cellular automaton which shows overall class 4 behavior will turn out, like rule 110, to be universal.

We saw at the end of Chapter 6 that class 4 rules always seem to yield a range of progressively more complicated localized structures. And my expectation is that if one looks sufficiently hard at any particular rule, then one will always eventually be able to find a set of localized structures that is rich enough to support universality.

![](Images/_page_707_Figure_1.jpeg)

Examples of cellular automata with class 4 overall behavior, as discussed in Chapter 6. I strongly suspect that all class 4 rules, like rule 110, will turn out to be universal.

The final demonstration that a given rule is universal will no doubt involve the same kind of elaborate construction as for rule 110.

But the point is that all the evidence I have so far suggests that for any class 4 rule such a construction will eventually turn out to be possible.

So what kinds of rules show class 4 behavior?

Among the 256 so-called elementary cellular automata that allow only two possible colors for each cell and depend only on nearest neighbors, the only clear immediate example is rule 110, together with rules 124, 137 and 193 obtained by trivially reversing left and right or black and white. But as soon as one allows more than two possible colors, or allows dependence on more than just nearest neighbors, one immediately finds all sorts of further examples of class 4 behavior.

In fact, as illustrated in the pictures on the facing page, it is sufficient in such cases just to use so-called totalistic rules in which the new color of a cell depends only on the average color of cells in its neighborhood, and not on their individual colors.

In two dimensions class 4 behavior can occur with rules that involve only two colors and only nearest neighbors, as shown on page 249. And indeed one example of such a rule is the so-called Game of Life that has been popular in recreational computing since the 1970s.

The strategy for demonstrating universality in a two-dimensional cellular automaton is in general very much the same as in one dimension. But in practice the comparative ease with which streams of localized structures can be made to cross in two dimensions can reduce some of the technical difficulties involved. And as it turns out there was already an outline of a proof given even in the 1970s that the Game of Life two-dimensional cellular automaton is universal.

Returning to one dimension, one can ask whether among the 256 elementary cellular automata there are any apart from rule 110 that show even signs of class 4 behavior. As we will see in the next section, one possibility is rule 54. And if this rule is in fact class 4 then it is my expectation that by looking at interactions between the localized structures it supports it will in the end, with enough effort, be possible to show that it too exhibits the phenomenon of universality.

#### The Threshold of Universality in Cellular Automata

By showing that rule 110 is universal, we have established that universality is possible even among cellular automata with the very simplest kinds of underlying rules. But there remains the question of what is ultimately needed for a cellular automaton, or any other kind of system, to be able to achieve universality.

In general, if a system is to be universal, then this means that by setting up an appropriate choice of initial conditions it is possible to get the system to emulate any type of behavior that can occur in any other system. And as a consequence, cellular automata like the ones in the pictures below are definitely not universal, since they always produce just simple uniform or repetitive patterns of behavior, whatever initial conditions one uses.

![](Images/_page_709_Picture_4.jpeg)

![](Images/_page_709_Picture_5.jpeg)

![](Images/_page_709_Picture_6.jpeg)

![](Images/_page_709_Picture_7.jpeg)

Examples of elementary cellular automata which only ever show purely uniform or purely repetitive behavior, and which therefore definitely cannot be universal. These cellular automata are necessarily all class 1 or class 2 systems.

In a sense the fundamental reason for this, as we discussed on page 252, is that such class 1 and class 2 cellular automata never allow any transmission of information except over limited distances. And the result of this is that they can only support processes that involve the correlated action of a limited number of cells.

In cellular automata like the ones at the top of the facing page some information can be transmitted over larger distances. But the way this occurs is highly constrained, and in the end these systems can only produce patterns that are in essence purely nested, so that it is again not possible for universality to be achieved.

What about additive rules such as 90 and 150?

With simple initial conditions these rules always yield very regular nested patterns. But with more complicated initial conditions, they produce more complicated patterns of behavior, as the pictures at the bottom of this page illustrate. As we saw on page 264, however, these patterns never in fact really correspond to more than rather simple transformations of the initial conditions. Indeed, even after say 1,048,576 steps, or any number of steps that is a power of two, the array of cells produced always turns out to correspond just to a simple superposition of two or three shifted copies of the initial conditions.

![](Images/_page_710_Picture_1.jpeg)

Examples of cellular automata that do allow information to be transmitted over large distances, but only in very restricted ways. The overall patterns produced by such cellular automata are essentially nested. No cellular automata of this kind can ever be universal.

![](Images/_page_710_Picture_4.jpeg)

Examples of cellular automata with additive rules. The repetitive occurrence of states that correspond to simple transformations of the initial conditions prevent such cellular automata from ever being universal.

And since there are many kinds of behavior that do not return to such predictable forms after any limited number of steps, one must conclude that additive rules cannot be universal.

At the end of the last section I mentioned rule 54 as another elementary cellular automaton besides rule 110 that might be class 4. The pictures below show examples of the typical behavior of rule 54.

![](Images/_page_711_Picture_4.jpeg)

![](Images/_page_711_Picture_5.jpeg)

![](Images/_page_711_Picture_6.jpeg)

Two views of the evolution of rule 54 from typical random initial conditions. The top view shows the color of every cell at every step. The bottom groups together pairs of cells, and shows only every other step. There are various localized structures, and hints of class 4 behavior.

Some localized structures are definitely seen. But are they enough to support class 4 behavior and universality? The pictures below show what happens if one starts looking in turn at each of the possible initial conditions for rule 54. At first one sees only simple repetitive behavior. At initial condition 291 one sees a very simple form of nesting. And as one continues one sees various other repetitive and nested forms. But at least up to the hundred millionth initial condition one sees nothing that is fundamentally any more complicated.

![](Images/_page_712_Picture_2.jpeg)

Forms of behavior seen in the first 100 million initial conditions for rule 54. With initial condition 291 the $n^{th}$ new stripe on the right is produced at step $2 n^2 + 8 n - 9$. Even in the last case shown, the arrangement of stripes eventually becomes completely regular, with the $n^{th}$ new stripe being produced at step $n^2 + 21 n/2 - \{6, 5, -4, 3\}[[\text{Mod}[n, 4] + 1]]/2$ . Pairs of cells are grouped together in each picture, as at the bottom of the facing page.

So can rule 54 achieve universality? I am not sure. It could be that if one went just a little further in looking at initial conditions one would see more complicated behavior. And it could be that even the structures shown above can be combined to produce all the richness that is needed for universality. But it could also be that whatever one does rule 54 will always in the end just show purely repetitive or nested behavior, which cannot on its own support universality.

What about other elementary cellular automata?

As I will discuss in the next chapter, my general expectation is that more or less any system whose behavior is not somehow fundamentally repetitive or nested will in the end turn out to be universal. But I suspect that this fact will be very much easier to establish for some systems than for others, with rule 110 being one of the easiest cases.

In general what one needs to do in order to prove universality is to find a procedure for setting up initial conditions in one system so as to make it emulate some general class of other systems. And at some level the main challenge is that our experience from programming and engineering tends to provide us with only a limited set of methods for coming up with such a procedure. Typically what we are used to doing is constructing things in stages. Usually we start by building components, and then we progressively assemble these into larger and larger structures. And the point is that at each stage, we need think directly only about the scale of structures that we are currently handling, and not for example about all the pieces that make up these structures.

In proving the universality of rule 110, we were able to follow essentially the same basic approach. We started by identifying various localized structures, and then we used these structures as components in building up the progressively larger structures that we needed.

What was in a sense crucial to our approach was therefore that we could readily control the transmission of information in the system. For this is what allowed us to treat different localized structures as being separate and independent objects.

And indeed in any system with class 4 behavior, things will typically always work in more or less the same way. But in class 3 systems they will not. For what usually happens in such systems is that a change made even to a single cell will eventually spread to affect all other cells. And this kind of uncontrolled transmission of information makes it very difficult to identify pieces that could be used as definite components in a construction.

So what can be done in such cases? The most obvious possibility is that one might be able to find special classes of initial conditions in which transmission of information could be controlled. And an example where this can be potentially done is rule 73.

The pictures below show the typical behavior of rule 73, first with completely random initial conditions, and then with initial conditions in which no run of an even number of black squares occurs.

![](Images/_page_714_Picture_2.jpeg)

Two examples of rule 73. The top example uses completely random initial conditions; the bottom example uses initial conditions in which no run of an even number of black squares ever occurs. The bottom example is actually part of the pattern obtained from a single black cell, just to the right of the center column, starting with step 1000.

In the second case rule 73 exhibits typical class 3 behavior, with the usual uncontrolled transmission of information. In the first case, however, the black walls that are present seem to prevent any long-range transmission of information at all.

So can one then achieve something intermediate in rule 73, in which information is transmitted, but only in a controlled way?

The pictures at the top of the next page give some indication of how this might be done. For they show that with an appropriate background rule 73 supports various localized structures, some of which move. And while these structures may at first seem more like those in rule 54 than rule 110, I strongly suspect that the complexity of the typical behavior of rule 73 will be reflected in more sophisticated interactions between the structures, and will eventually provide what is needed to allow universality to be demonstrated in much the same way as in rule 110.

![](Images/_page_715_Figure_1.jpeg)

Examples of localized structures in rule 73. Note that in the last case shown, the background patterns on either side are mirror images.

So what about a case like rule 30? With strictly repetitive initial conditions, like any cellular automaton, this must yield purely repetitive behavior. But as soon as one perturbs such initial conditions, one normally seems to get only complicated and seemingly random behavior, as in the top row of pictures below.

![](Images/_page_715_Figure_4.jpeg)

Examples of patterns produced by rule 30 with repetitive backgrounds. The top row shows the effect of inserting a single extra black cell into various backgrounds. The bottom row shows all localized structures involving up to 25 cells supported by rule 30 on repetitive backgrounds with blocks of up to 25 cells. Note that these localized structures always move one cell to the right at each step, making it impossible for them to interact in non-trivial ways.

Yet it turns out still to be possible to get localized structures, as the bottom row of pictures above demonstrate. But these structures always seem to move at the same speed, and so can never interact. And even after searching many billions of cases, I have never succeeded in finding any useful set of localized structures in rule 30.

The picture below shows what happens in rule 45. Many possible perturbations to repetitive initial conditions again yield seemingly random behavior. But in one case a nested pattern is produced. And structures that remain localized are now fairly common, but just as in rule 30 always seem to move at the same speed.

![](Images/_page_716_Figure_3.jpeg)

![](Images/_page_716_Figure_4.jpeg)

![](Images/_page_716_Figure_5.jpeg)

![](Images/_page_716_Figure_6.jpeg)

Examples of patterns produced by inserting a single extra black cell into repetitive backgrounds for rule 45. Note the appearance of a slanted version of the nested pattern from rule 90. In rule 45, localized structures turn out to be fairly common, but as in rule 30 they always seem to move at the same speed, and so presumably cannot interact to produce any kind of class 4 behavior.

So although this means that the particular type of approach we used to demonstrate the universality of rule 110 cannot immediately be used for rule 30 or rule 45, it certainly does not mean that these rules are not in the end universal. And as I will discuss in the next chapter, it is my very strong belief that in fact they will turn out to be.

So how might we get evidence for this?

If a system is universal, then this means that with a suitable encoding of initial conditions its evolution must emulate the evolution of any other system. So this suggests that one might be able to get evidence about universality just by trying different possible encodings, and then seeing what range of other systems they allow one to emulate.

In the case of the 19-color universal cellular automaton on page 645 it turns out that encodings in which individual black and white cells are represented by particular 20-cell blocks are sufficient to allow the universal cellular automaton to emulate all 256 possible elementary cellular automata, with one step in the evolution of each of these corresponding to 53 steps in the evolution of the original system.

![](Images/_page_717_Figure_1.jpeg)

Examples of how the 19-color universal cellular automaton can emulate elementary cellular automata. In each case single cells are encoded as blocks of cells, and all distinct such encodings with blocks up to length 20 are shown.

So given a particular elementary cellular automaton one can then ask what other elementary cellular automata it can emulate using blocks up to a certain length.

The pictures on the facing page show a few examples.

The results are not particularly dramatic. No single rule is able to emulate many others, and the rules that are emulated tend to be rather simple. An example of a slight surprise is that rule 45 ends up being able to emulate rule 90. But at least with blocks up to length 25, rule 30 for example is not able to emulate any non-trivial rules at all.

From the proof of universality that we gave it follows that rule 110 must be able to emulate any other elementary cellular automaton with blocks of some size, but with the actual construction we discussed this size will be quite astronomical. And certainly in the picture on the facing page rule 110 does not seem to stand out.

But although it seems somewhat difficult to emulate the complete evolution of one cellular automaton with another, it turns out to be much easier to emulate fragments of evolution for limited numbers of steps. And as an example the picture below shows how rule 30 can be made to emulate the basic action of one step in rule 90.

![](Images/_page_718_Figure_6.jpeg)

![](Images/_page_718_Figure_7.jpeg)

Rule 30 set up to emulate a single XOR operation, as used in a step of rule 90 evolution. The initial conditions for rule 30 are fixed except at the two positions indicated, where input can effectively be given. The picture shows that for each possible combination of inputs, the result from the rule 30 evolution corresponds exactly to the output from the XOR.

The idea is to set up a configuration in rule 30 so that if one inserts input at particular positions the output from the underlying rule 30 evolution corresponds exactly to what one would get from a single step of rule 90 evolution. And in the particular case shown, this is achieved by having blocks 3 cells wide between each input position.

But as the picture on the next page indicates, by having appropriate blocks 5 cells wide rule 30 can actually be made to emulate one step in the evolution of every single one of the 256 possible elementary cellular automata.

![](Images/_page_719_Figure_1.jpeg)

Illustrations of how rule 30 can be set up to emulate a single step in the evolution of all elementary cellular automata.

So what about other underlying rules?

The picture on the facing page shows for several different underlying rules which of the 256 possible elementary rules can successfully be emulated with successively wider blocks. In cases where the underlying rules have only rather simple behavior, as with rules 90 and 184, it turns out that it is never possible to emulate more than a few of the 256 possible elementary rules. But for underlying rules that have more complex behavior, like rules 22, 30, or 110, it turns out that in the end it is always possible to emulate all 256 elementary rules.

![](Images/_page_720_Figure_2.jpeg)

Summaries of how various underlying cellular automata do in emulating a single step in the evolution of each of the 256 possible elementary cellular automata using the scheme from the facing page with blocks of successively greater widths.

The emulation here is, however, only for a single step. So the fact that it is possible does not immediately establish universality in any ordinary sense. But it does once again support the idea that almost any cellular automaton whose behavior seems to us complex can be made to do computations that are in a sense as sophisticated as one wants.

And this suggests that such cellular automata will in the end turn out to be universal, with the result that out of the 256 elementary rules one expects that perhaps as many as 27 will in fact be universal.

#### Universality in Turing Machines and Other Systems

From the results of the previous few sections, we now have some idea where the threshold for universality lies in cellular automata. But what about other kinds of systems, like Turing machines? How complicated do the rules need to be in order to get universality?

In the 1950s and early 1960s a certain amount of work was done on trying to construct small Turing machines that would be universal. The main achievement of this work was the construction of the universal machine with 7 states and 4 possible colors shown below.

![](Images/_page_721_Picture_4.jpeg)

The rule for a universal Turing machine with 7 states and 4 colors constructed in 1962. Until now, this was essentially the simplest known universal Turing machine. Note that one element of the rule can be considered as specifying that the Turing machine should "halt" with the head staying in the same location and same state.

![](Images/_page_721_Figure_6.jpeg)

An example of how the Turing machine above can emulate a tag system. A black element in the tag system is set up to correspond to a block of four cells in the Turing machine, while a white element corresponds to a single cell.

The picture at the bottom of the facing page shows how universality can be proved in this case. The basic idea is that by setting up appropriate initial conditions on the left, the Turing machine can be made to emulate any tag system of a certain kind. But it then turns out from the discussion of page 667 that there are tag systems of this kind that are universal.

It is already an achievement to find a universal Turing machine as comparatively simple as the one on the facing page. And indeed in the forty years since this example was found, no significantly simpler one has been found. So one might conclude from this that the machine on the facing page is somehow at the threshold for universality in Turing machines.

But as one might expect from the discoveries in this book, this is far from correct. And in fact, by using the universality of rule 110 it turns out to be possible to come up with the vastly simpler universal Turing machine shown below, with just 2 states and 5 possible colors.

The rule for the simplest Turing machine currently known to be universal, based on discoveries in this book. The machine has 2 states and 5 possible colors.

![](Images/_page_722_Figure_6.jpeg)

![](Images/_page_722_Figure_7.jpeg)

An example of how the Turing machine above manages to emulate rule 110. The compressed picture is made by keeping only the steps indicated at which the head is further to the right than ever before. To get the picture shown requires running the Turing machine for a total of 5000 steps.

As the picture at the bottom of the previous page illustrates, this Turing machine emulates rule 110 in a quite straightforward way: its head moves systematically backwards and forwards, at each complete sweep updating all cells according to a single step of rule 110 evolution. And knowing from earlier in this chapter that rule 110 is universal, it then follows that the 2-state 5-color Turing machine must also be universal.

So is this then the simplest possible universal Turing machine?

I am quite certain that it is not. And in fact I expect that there are some significantly simpler ones. But just how simple can they actually be?

If one looks at the 4096 Turing machines with 2 states and 2 colors it is fairly easy to see that their behavior is in all cases too simple to support universality. So between 2 states and 2 colors and 2 states and 5 colors, where does the threshold for universality in Turing machines lie?

![](Images/_page_723_Figure_6.jpeg)

The pictures at the bottom of the facing page give examples of some 2-state 4-color Turing machines that show complex behavior. And I have little doubt that most if not all of these are universal.

Among such 2-state 4-color Turing machines perhaps one in 50,000 shows complex behavior when started from a blank tape. Among 4-state 2-color Turing machines the same kind of complex behavior is also seen, as discussed on page 81, but now it occurs only in perhaps one out of 200,000 cases.

So what about Turing machines with 2 states and 3 colors? There are a total of 2,985,984 of these. And most of them yield fairly simple behavior. But it turns out that 14 of them, all essentially equivalent, produce considerable complexity, even when started from a blank tape.

The picture below shows an example.

![](Images/_page_724_Picture_5.jpeg)

![](Images/_page_724_Picture_6.jpeg)

![](Images/_page_724_Picture_7.jpeg)

One of the 14 essentially equivalent 2-state 3-color Turing machines that yield complicated behavior when started from a blank tape. The compressed picture above is made by taking the first 100,000 steps, and keeping only those at which the head is further to the left than ever before. The interior of the pattern that emerges is like an inverted version of the rule 60 additive cellular automaton; the boundary, however, is more complicated. In the numbering scheme of page 761 this is machine 596,440 out of the total of 2,985,984 with 2 states and 3 colors.

And although it will no doubt be very difficult to prove, it seems likely that this Turing machine will in the end turn out to be universal. And if so, then presumably it will by most measures be the very simplest Turing machine that is universal.

With 3 states and 2 colors it turns out that with blank initial conditions all of the 2,985,984 possible Turing machines of this type quickly evolve to produce simple repetitive or nested behavior. With more complicated initial conditions the behavior one sees can sometimes be more complicated, at least for a while, as in the pictures below. But in the end it still always seems to resolve into a simple form.

![](Images/_page_725_Figure_2.jpeg)

Yet despite this, it still seems conceivable that with appropriate initial conditions significantly more complex behavior might occur, and might ultimately allow universality in 3-state 2-color Turing machines.

From the universality of rule 110 we know that if one just starts enumerating cellular automata in a particular order, then after going through at most 110 rules, one will definitely see universality. And from other results earlier in this chapter it seems likely that in fact one would tend to see universality even somewhat earlier, after going through only perhaps just ten or twenty rules.

Among Turing machines, the universal 2-state 5-color rule on page 707 can be assigned the number 8,679,752,795,626. So this means that after going through perhaps nine trillion Turing machines one will definitely tend to find an example that is universal. But presumably one will actually find examples much earlier, since for example the 2-state 3-color machine on page 709 is only number 596,440.

And although these numbers are larger than for cellular automata, the fact remains that the simplest potentially universal Turing machines are still very simple in structure, suggesting that the threshold for universality in Turing machines, just like in cellular automata, is in many respects very low.

So what about other types of systems?

I suspect that in almost any case where we have seen complex behavior earlier in this book it will eventually be possible to show that there is universality. And indeed, as I will discuss at length in the next chapter, I believe that in general there is a close connection between universality and the appearance of complex behavior.

Previous examples of systems that are known to be universal have typically had rules that are far too complicated to see this with any clarity. But an almost unique instance where it could potentially have been seen even long ago are what are known as combinators.

Combinators are a particular case of the symbolic systems that we discussed on page 102 of Chapter 3. Originally intended as an idealized way to represent structures of functions defined in logic, combinators were actually first introduced in 1920, sixteen years before Turing machines. But although they have been investigated somewhat over the past eighty years, they have for the most part been viewed as rather obscure and irrelevant constructs.

The basic rules for combinators are given below.

![](Images/_page_726_Picture_8.jpeg)

Rules for symbolic systems known as combinators, first introduced in 1920, and proved universal by the mid-1930s.

With short initial conditions, the pictures at the top of the next page demonstrate that combinators tend to evolve quickly to simple fixed points. But with initial condition (e) of length 8 the pictures show that no fixed point is reached, and instead there is exponential growth in total size, with apparently rather random internal behavior.

![](Images/_page_727_Figure_1.jpeg)

Examples of combinator evolution. The expression in case (e) is the shortest that leads to unlimited growth. The plots at the bottom show the total sizes of expressions reached on successive steps. Note that the detailed pattern of evolution, though not any final fixed point reached, can depend on the fact that the combinator rules are applied at each step in *Mathematica 1* order.

Other combinators yield still more complicated behavior, sometimes with overall repetition or nesting, but often not.

There are features of combinators that are not easy to capture directly in pictures. But from pictures like the ones on the facing page it is rather clear that despite their fairly simple underlying rules, the behavior of combinators can be highly complex.

And while issues of typical behavior have not really been studied before, it has been known that combinators are universal almost since the concept of universality was first introduced in the 1930s.

One way that we can now show this is to demonstrate that combinators can emulate rule 110. And as the pictures on the next page illustrate, it turns out that just repeatedly applying the combinator expression below reproduces successive steps in the evolution of rule 110.

A combinator expression that corresponds to the operation of doing one step of rule 110 evolution.

There has in the past been no overall context for understanding universality in combinators. But now what we have seen suggests that such universality is in a sense just associated with general complex behavior.

Yet we saw in Chapter 3 that there are symbolic systems with rules even simpler than combinators that still show complex behavior. And so now I suspect that these too are universal.

And in fact wherever one looks, the threshold for universality seems to be much lower than one would ever have imagined. And this is one of the important basic observations that led me to formulate the Principle of Computational Equivalence that I discuss in the next chapter.

![](Images/_page_729_Figure_1.jpeg)

Emulating the rule 110 cellular automaton using combinators. The rule 110 combinator from the previous page is applied once for each step of rule 110 evolution. The initial state is taken to consist of a single black cell.

![](Images/_page_730_Picture_0.jpeg)
