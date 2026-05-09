#### Fundamental Physics

#### The Problems of Physics

In the previous chapter, we saw that many important aspects of a wide variety of everyday systems can be understood by thinking in terms of simple programs. But what about fundamental physics? Can ideas derived from studying simple programs also be applied there?

Fundamental physics is the area in which traditional mathematical approaches to science have had their greatest success. But despite this success, there are still many central issues that remain quite unresolved. And in this chapter my purpose is to consider some of these issues in the light of what we have learned from studying simple programs.

It might at first not seem sensible to try to use simple programs as a basis for understanding fundamental physics. For some of the best established features of physical systems—such as conservation of energy or equivalence of directions in space—seem to have no obvious analogs in most of the programs we have discussed so far in this book.

As we will see, it is in fact possible for simple programs to show these kinds of features. But it turns out that some of the most important unresolved issues in physics concern phenomena that are in a sense more general—and do not depend much on such features.

And indeed what we will see in this chapter is that remarkably simple programs are often able to capture the essence of what is going on—even though traditional efforts have been quite unsuccessful.

Thus, for example, in the early part of this chapter I will discuss the so-called Second Law of Thermodynamics or Principle of Entropy Increase: the observation that many physical systems tend to become irreversibly more random as time progresses. And I will show that the essence of such behavior can readily be seen in simple programs.

More than a century has gone by since the Second Law was first formulated. Yet despite many detailed results in traditional physics, its origins have remained quite mysterious. But what we will see in this chapter is that by studying the Second Law in the context of simple programs, we will finally be able to get a clear understanding of why it so often holds—as well as of when it may not.

My approach in investigating issues like the Second Law is in effect to use simple programs as metaphors for physical systems. But can such programs in fact be more than that? And for example is it conceivable that at some level physical systems actually operate directly according to the rules of a simple program?

Looking at the laws of physics as we know them today, this might seem absurd. For at first the laws might seem much too complicated to correspond to any simple program. But one of the crucial discoveries of this book is that even programs with very simple underlying rules can yield great complexity.

And so it could be with fundamental physics. Underneath the laws of physics as we know them today it could be that there lies a very simple program from which all the known laws—and ultimately all the complexity we see in the universe—emerges.

To suppose that our universe is in essence just a simple program is certainly a bold hypothesis. But in the second part of this chapter I will describe some significant progress that I have made in investigating this hypothesis, and in working out the details of what kinds of simple programs might be involved.

There is still some distance to go. But from what I have found so far I am extremely optimistic that by using the ideas of this book the most fundamental problem of physics—and one of the ultimate problems of all of science—may finally be within sight of being solved.

#### The Notion of Reversibility

At any particular step in the evolution of a system like a cellular automaton the underlying rule for the system tells one how to proceed to the next step. But what if one wants to go backwards? Can one deduce from the arrangement of black and white cells at a particular step what the arrangement of cells must have been on previous steps?

All current evidence suggests that the underlying laws of physics have this kind of reversibility. So this means that given a sufficiently precise knowledge of the state of a physical system at the present time, it is therefore possible to deduce not only what the system will do in the future, but also what it did in the past.

In the first cellular automaton shown below it is also straightforward to do this. For any cell that has one color at a particular step must always have had the opposite color on the step before.

![](Images/_page_450_Picture_5.jpeg)

![](Images/_page_450_Picture_6.jpeg)

Examples of cellular automata that are and are not reversible. Rule 51 is reversible, so that it preserves enough information to allow one to go backwards from any particular step as well as forwards. Rule 254 is not reversible, since it always evolves to uniform black and preserves no information about the arrangement of cells on earlier steps.

But the second cellular automaton works differently, and does not allow one to go backwards. For after just a few steps, it makes every cell black, regardless of what it was before—with the result that there is no way to tell what color might have occurred on previous steps.

There are many examples of systems in nature which seem to organize themselves a little like the second case above. And indeed the conflict between this and the known reversibility of underlying laws of physics is related to the subject of the next section in this chapter.

But my purpose here is to explore what kinds of systems can be reversible. And of the 256 elementary cellular automata with two colors and nearest-neighbor rules, only the six shown below turn out to be reversible. And as the pictures demonstrate, all of these exhibit fairly trivial behavior, in which only rather simple transformations are ever made to the initial configuration of cells.

![](Images/_page_451_Picture_3.jpeg)

Examples of the behavior of the six elementary cellular automata that are reversible. In all cases the transformations made to the initial conditions are simple enough that it is straightforward to go backwards as well as forwards in the evolution.

So is it possible to get more complex behavior while maintaining reversibility? There are a total of 7,625,597,484,987 cellular automata with three colors and nearest-neighbor rules, and searching through these one finds just 1800 that are reversible. Of these 1800, many again exhibit simple behavior, much like the pictures above. But some exhibit more complex behavior, as in the pictures below.

![](Images/_page_451_Picture_6.jpeg)

Examples of some of the 1800 reversible cellular automata with three colors and nearest-neighbor rules. Even though these systems exhibit complex behavior that scrambles the initial conditions, all of them are still reversible, so that starting from the configuration of cells at the bottom of each picture, it is always possible to deduce the configurations on all previous steps.

How can one now tell that such systems are reversible? It is no longer true that their evolution leads only to simple transformations of the initial conditions. But one can still check that starting with the specific configuration of cells at the bottom of each picture, one can evolve backwards to get to the top of the picture. And given a particular rule it turns out to be fairly straightforward to do a detailed analysis that allows one to prove or disprove its reversibility.

But in trying to understand the range of behavior that can occur in reversible systems it is often convenient to consider classes of cellular automata with rules that are specifically constructed to be reversible. One such class is illustrated below. The idea is to have rules that explicitly remain the same even if they are turned upside-down, thereby interchanging the roles of past and future.

![](Images/_page_452_Picture_4.jpeg)

![](Images/_page_452_Picture_5.jpeg)

An example of a cellular automaton that is explicitly set up to be reversible. The rule for the system remains unchanged if all its elements are turned upside-down, effectively interchanging the roles of past and future. Patterns produced by the rule must exhibit the same time reversal symmetry, as shown on the left. The specific rule used here is based on taking elementary rule 214, then adding the specification that the new color of a cell should be inverted whenever the cell was black two steps back. Note that by allowing a total of four rather than two colors, a version of the rule that depends only on the immediately preceding step can be constructed.

Such rules can be constructed by taking ordinary cellular automata and adding dependence on colors two steps back.

The resulting rules can be run both forwards and backwards. In each case they require knowledge of the colors of cells on not one but two successive steps. Given this knowledge, however, the rules can be used to determine the configuration of cells on either future or past steps.

The next two pages show examples of the behavior of such cellular automata with both random and simple initial conditions.

![](Images/_page_453_Figure_2.jpeg)

Examples of reversible cellular automata starting from random and from simple initial conditions. In the upper block of pictures, every cell is chosen to be black or white with equal probability on the two successive first steps. In the lower block of pictures, only the center cell is taken to be black on these steps.

![](Images/_page_454_Picture_2.jpeg)

![](Images/_page_454_Picture_4.jpeg)

![](Images/_page_454_Picture_6.jpeg)

rule 214R

The evolution of three reversible cellular automata for 300 steps. In the first case, a regular nested pattern is obtained. In the other cases, the patterns show many features of randomness.

![](Images/_page_455_Picture_1.jpeg)

An example of a reversible cellular automaton whose evolution supports localized structures. Because of the reversibility of the underlying rule, every collision must be able to occur equally well when its initial and final states are interchanged.

In some cases, the behavior is fairly simple, and the patterns obtained have simple repetitive or nested structures. But in many cases, even with simple initial conditions, the patterns produced are highly complex, and seem in many respects random.

The reversibility of the underlying rules has some obvious consequences, such as the presence of triangles pointing sideways but not down. But despite their reversibility, the rules still manage to produce the kinds of complex behavior that we have seen in cellular automata and many other systems throughout this book.

So what about localized structures?

The picture on the facing page demonstrates that these can also occur in reversible systems. There are some constraints on the details of the kinds of collisions that are possible, but reversible rules typically tend to work very much like ordinary ones.

So in the end it seems that even though only a very small fraction of possible systems have the property of being reversible, such systems can still exhibit behavior just as complex as one sees anywhere else.

#### Irreversibility and the Second Law of Thermodynamics

All the evidence we have from particle physics and elsewhere suggests that at a fundamental level the laws of physics are precisely reversible. Yet our everyday experience is full of examples of seemingly irreversible phenomena. Most often, what happens is that a system which starts in a fairly regular or organized state becomes progressively more and more random and disorganized. And it turns out that this phenomenon can already be seen in many simple programs.

The picture at the top of the next page shows an example based on a reversible cellular automaton of the type discussed in the previous section. The black cells in this system act a little like particles which bounce around inside a box and interact with each other when they collide.

At the beginning the particles are placed in a simple arrangement at the center of the box. But over the course of time the picture shows that the arrangement of particles becomes progressively more random.

![](Images/_page_457_Picture_1.jpeg)

A reversible cellular automaton that exhibits seemingly irreversible behavior. Starting from an initial condition in which all black cells or particles lie at the center of a box, the distribution becomes progressively more random. Such behavior appears to be the central phenomenon responsible for the Second Law of Thermodynamics. The specific cellular automaton used here is rule 122R. The system is restricted to a region of size 100 cells.

Typical intuition from traditional science makes it difficult to understand how such randomness could possibly arise. But the discovery in this book that a wide range of systems can generate randomness even with very simple initial conditions makes it seem considerably less surprising.

But what about reversibility? The underlying rules for the cellular automaton used in the picture above are precisely reversible. Yet the picture itself does not at first appear to be at all reversible. For there appears to be an irreversible increase in randomness as one goes down successive panels on the page.

The resolution of this apparent conflict is however fairly straightforward. For as the picture on the facing page demonstrates, if the

![](Images/_page_458_Picture_1.jpeg)

An extended version of the picture on the facing page, in which the reversibility of the underlying cellular automaton is more clearly manifest. An initial condition is carefully constructed so that halfway through the evolution shown a simple arrangement of particles will be produced. If one starts with this arrangement, then the randomness of the system will effectively increase whether one goes forwards or backwards in time from that point.

simple arrangement of particles occurs in the middle of the evolution, then one can readily see that randomness increases in exactly the same way—whether one goes forwards or backwards from that point.

Yet there is still something of a mystery. For our everyday experience is full of examples in which randomness increases much as in the second half of the picture above. But we essentially never see the kind of systematic decrease in randomness that occurs in the first half.

By setting up the precise initial conditions that exist at the beginning of the whole picture it would certainly in principle be possible to get such behavior. But somehow it seems that initial conditions like these essentially never actually occur in practice.

There has in the past been considerable confusion about why this might be the case. But the key to understanding what is going on is simply to realize that one has to think not only about the systems one is studying, but also about the types of experiments and observations that one uses in the process of studying them.

The crucial point then turns out to be that practical experiments almost inevitably end up involving only initial conditions that are fairly simple for us to describe and construct. And with these types of initial conditions, systems like the one on the previous page always tend to exhibit increasing randomness.

But what exactly is it that determines the types of initial conditions that one can use in an experiment? It seems reasonable to suppose that in any meaningful experiment the process of setting up the experiment should somehow be simpler than the process that the experiment is intended to observe.

But how can one compare such processes? The answer that I will develop in considerable detail later in this book is to view all such processes as computations. The conclusion is then that the computation involved in setting up an experiment should be simpler than the computation involved in the evolution of the system that is to be studied by the experiment.

It is clear that by starting with a simple state and then tracing backwards through the actual evolution of a reversible system one can find initial conditions that will lead to decreasing randomness. But if one looks for example at the pictures on the last couple of pages the complexity of the behavior seems to preclude any less arduous way of finding such initial conditions. And indeed I will argue in Chapter 12 that the Principle of Computational Equivalence suggests that in general no such reduced procedure should exist.

The consequence of this is that no reasonable experiment can ever involve setting up the kind of initial conditions that will lead to decreases in randomness, and that therefore all practical experiments will tend to show only increases in randomness.

It is this basic argument that I believe explains the observed validity of what in physics is known as the Second Law of Thermodynamics. The law was first formulated more than a century ago, but despite many related technical results, the basic reasons for its validity have until now remained rather mysterious.

The field of thermodynamics is generally concerned with issues of heat and energy in physical systems. A fundamental fact known since the mid-1800s is that heat is a form of energy associated with the random microscopic motions of large numbers of atoms or other particles.

One formulation of the Second Law then states that any energy associated with organized motions of such particles tends to degrade irreversibly into heat. And the pictures at the beginning of this section show essentially just such a phenomenon. Initially there are particles which move in a fairly regular and organized way. But as time goes on, the motion that occurs becomes progressively more random.

There are several details of the cellular automaton used above that differ from actual physical systems of the kind usually studied in thermodynamics. But at the cost of some additional technical complication, it is fairly straightforward to set up a more realistic system.

The pictures on the next two pages show a particular two-dimensional cellular automaton in which black squares representing particles move around and collide with each other, essentially like particles in an ideal gas. This cellular automaton shares with the cellular automaton at the beginning of the section the property of being reversible. But it also has the additional feature that in every collision the total number of particles in it remains unchanged. And since each particle can be thought of as having a certain energy, it follows that the total energy of the system is therefore conserved.

In the first case shown, the particles are taken to bounce around in an empty square box. And it turns out that in this particular case only very simple repetitive behavior is ever obtained. But almost any change destroys this simplicity.

And in the second case, for example, the presence of a small fixed obstacle leads to rapid randomization in the arrangement of particles—very much like the randomization we saw in the one-dimensional cellular automaton that we discussed earlier in this section.

![](Images/_page_461_Figure_2.jpeg)

The behavior of a simple two-dimensional cellular automaton that emulates an ideal gas of particles. In the top group of pictures, the particles bounce around in an empty square box. In the bottom group of pictures, the box contains a small fixed obstacle. In the top group of pictures, the arrangement of particles shows simple repetitive behavior. In the bottom group, however, it becomes progressively more random with time. The underlying rules for the cellular automaton used here are reversible, and conserve the total number of particles. The specific rules are based on  $2 \times 2$  blocks—a two-dimensional generalization of the block cellular automata to be discussed in the next section. For each  $2 \times 2$  block the configuration of particles is taken to remain the same at a particular step unless there are exactly two particles arranged diagonally within the block, in which case the particles move to the opposite diagonal.

So even though the total energy of all particles remains the same, the distribution of this energy becomes progressively more random, just as the usual Second Law implies.

An important practical consequence of this is that it becomes increasingly difficult to extract energy from the system in the form of systematic mechanical work. At an idealized level one might imagine trying to do this by inserting into the system some kind of paddle which would experience force as a result of impacts from particles.

![](Images/_page_462_Picture_2.jpeg)

![](Images/_page_462_Picture_3.jpeg)

Time histories of the cellular automata from the facing page. In each case a slice is taken through the midline of the box. Black cells that are further from the midline are shown in progressively lighter shades of gray. Case (a) corresponds to an empty square box, and shows simple repetitive behavior. Case (b) corresponds to a box containing a fixed obstacle, and in this case rapid randomization is seen. Each panel corresponds to 100 steps in the evolution of the system; the box is 24 cells across.

The pictures below show how such force might vary with time in cases (a) and (b) above. In case (a), where no randomization occurs, the force can readily be predicted, and it is easy to imagine harnessing it to produce systematic mechanical work. But in case (b), the force quickly randomizes, and there is no obvious way to obtain systematic mechanical work from it.

![](Images/_page_462_Figure_6.jpeg)

The force on an idealized paddle placed on the midline of the systems shown above. The force reflects an imbalance in the number of particles at each step arriving at the midline from above and below. In case (a) this imbalance is readily predictable. In case (b), however, it rapidly becomes for most practical purposes random. This randomness is essentially what makes it impossible to build a physical perpetual motion machine which continually turns heat into mechanical work.

One might nevertheless imagine that it would be possible to devise a complicated machine, perhaps with an elaborate arrangement of paddles, that would still be able to extract systematic mechanical work even from an apparently random distribution of particles. But it turns out that in order to do this the machine would effectively have to be able to predict where every particle would be at every step in time.

And as we shall discuss in Chapter 12, this would mean that the machine would have to perform computations that are as sophisticated as those that correspond to the actual evolution of the system itself. The result is that in practice it is never possible to build perpetual motion machines that continually take energy in the form of heat—or randomized particle motions—and convert it into useful mechanical work.

The impossibility of such perpetual motion machines is one common statement of the Second Law of Thermodynamics. Another is that a quantity known as entropy tends to increase with time.

Entropy is defined as the amount of information about a system that is still unknown after one has made a certain set of measurements on the system. The specific value of the entropy will depend on what measurements one makes, but the content of the Second Law is that if one repeats the same measurements at different times, then the entropy deduced from them will tend to increase with time.

If one managed to find the positions and properties of all the particles in the system, then no information about the system would remain unknown, and the entropy of the system would just be zero. But in a practical experiment, one cannot expect to be able to make anything like such complete measurements.

And more realistically, the measurements one makes might for example give the total numbers of particles in certain regions inside the box. There are then a large number of possible detailed arrangements of particles that are all consistent with the results of such measurements. The entropy is defined as the amount of additional information that would be needed in order to pick out the specific arrangement that actually occurs.

We will discuss in more detail in Chapter 10 the notion of amount of information. But here we can imagine numbering all the possible arrangements of particles that are consistent with the results of our measurements, so that the amount of information needed to pick out a single arrangement is essentially the length in digits of one such number.

The pictures below show the behavior of the entropy calculated in this way for systems like the one discussed above. And what we see is that the entropy does indeed tend to increase, just as the Second Law implies.

![](Images/_page_464_Figure_3.jpeg)

The entropy as a function of time for systems of the type shown in case (b) from page 447. The top plot is exactly for case (b); the bottom one is for a system three times larger in size. The entropy is found in each case by working out how many possible configurations of particles are consistent with measurements of the total numbers of particles in a  $6 \times 6$  grid of regions within the system. Just as the Second Law of Thermodynamics suggests, the entropy tends to increase with time. Note that the plots above would be exactly symmetrical if they were continued to the left: the entropy would increase in the same way going both forwards and backwards from the simple initial conditions used.

In effect what is going on is that the measurements we make represent an attempt to determine the state of the system. But as the arrangement of particles in the system becomes more random, this attempt becomes less and less successful.

One might imagine that there could be a more elaborate set of measurements that would somehow avoid these problems, and would not lead to increasing entropy. But as we shall discuss in Chapter 12, it again turns out that setting up such measurements would have to involve the same level of computational effort as the actual evolution of the system itself. And as a result, one concludes that the entropy associated with measurements done in practical experiments will always tend to increase, as the Second Law suggests.

In Chapter 12 we will discuss in more detail some of the key ideas involved in coming to this conclusion. But the basic point is that the phenomenon of entropy increase implied by the Second Law is a more or less direct consequence of the phenomenon discovered in this book that even with simple initial conditions many systems can produce complex and seemingly random behavior.

One aspect of the generation of randomness that we have noted several times in earlier chapters is that once significant randomness has been produced in a system, the overall properties of that system tend to become largely independent of the details of its initial conditions.

In any system that is reversible it must always be the case that different initial conditions lead to at least slightly different states—otherwise there would be no unique way of going backwards. But the point is that even though the outcomes from different initial conditions differ in detail, their overall properties can still be very much the same.

The pictures on the facing page show an example of what can happen. Every individual picture has different initial conditions. But whenever randomness is produced the overall patterns that are obtained look in the end almost indistinguishable.

The reversibility of the underlying rules implies that at some level it must be possible to recognize outcomes from different kinds of initial conditions. But the point is that to do so would require a computation far more sophisticated than any that could meaningfully be done as part of a practical measurement process.

So this means that if a system generates sufficient randomness, one can think of it as evolving towards a unique equilibrium whose properties are for practical purposes independent of its initial conditions.

This fact turns out in a sense to be implicit in many everyday applications of physics. For it is what allows us to characterize all sorts of physical systems by just specifying a few parameters such as temperature and chemical composition—and avoids us always having to know the details of the initial conditions and history of each system.

The existence of a unique equilibrium to which any particular system tends to evolve is also a common statement of the Second Law of

![](Images/_page_466_Picture_1.jpeg)

The approach to equilibrium in a reversible cellular automaton with a variety of different initial conditions. Apart from exceptional cases where no randomization occurs, the behavior obtained with different initial conditions is eventually quite indistinguishable in its overall properties. Because the underlying rule is reversible, however, the details with different initial conditions are always at least slightly different—otherwise it would not be possible to go backwards in a unique way. The rule used here is 122R. Successive pairs of pictures have initial conditions that differ only in the color of a single cell at the center.

Thermodynamics. And once again, therefore, we find that the Second Law is associated with basic phenomena that we already saw early in this book.

But just how general is the Second Law? And does it really apply to all of the various kinds of systems that we see in nature?

Starting nearly a century ago it came to be widely believed that the Second Law is an almost universal principle. But in reality there is surprisingly little evidence for this.

Indeed, almost all of the detailed applications ever made of the full Second Law have been concerned with just one specific area: the behavior of gases. By now there is therefore good evidence that gases obey the Second Law—just as the idealized model earlier in this section suggests. But what about other kinds of systems?

![](Images/_page_467_Picture_2.jpeg)

Examples of reversible cellular automata with various rules. Some quickly randomize, as the Second Law of Thermodynamics would suggest. But others do not—and thus in effect do not obey the Second Law of Thermodynamics.

The pictures on the facing page show examples of various reversible cellular automata. And what we see immediately from these pictures is that while some systems exhibit exactly the kind of randomization implied by the Second Law, others do not.

The most obvious exceptions are cases like rule 0R and rule 90R, where the behavior that is produced has only a very simple fixed or repetitive form. And existing mathematical studies have indeed identified these simple exceptions to the Second Law. But they have somehow implicitly assumed that no other kinds of exceptions can exist.

The picture on the next page, however, shows the behavior of rule 37R over the course of many steps. And in looking at this picture, we see a remarkable phenomenon: there is neither a systematic trend towards increasing randomness, nor any form of simple predictable behavior. Indeed, it seems that the system just never settles down, but rather continues to fluctuate forever, sometimes becoming less orderly, and sometimes more so.

So how can such behavior be understood in the context of the Second Law? There is, I believe, no choice but to conclude that for practical purposes rule 37R simply does not obey the Second Law.

And as it turns out, what happens in rule 37R is not so different from what seems to happen in many systems in nature. If the Second Law was always obeyed, then one might expect that by now every part of our universe would have evolved to completely random equilibrium.

Yet it is quite obvious that this has not happened. And indeed there are many kinds of systems, notably biological ones, that seem to show, at least temporarily, a trend towards increasing order rather than increasing randomness.

How do such systems work? A common feature appears to be the presence of some kind of partitioning: the systems effectively break up into parts that evolve at least somewhat independently for long periods of time.

The picture on page 456 shows what happens if one starts rule 37R with a single small region of randomness. And for a while what one sees is that the randomness that has been inserted persists. But eventually the system instead seems to organize itself to yield just a small number of simple repetitive structures.

![](Images/_page_469_Figure_2.jpeg)

More steps in the evolution of the reversible cellular automaton with rule 37R. This system is an example of one that does not in any meaningful way obey the Second Law of Thermodynamics. Instead of exhibiting progressively more random behavior, it appears to fluctuate between quite ordered and quite disordered states.

This kind of self-organization is quite opposite to what one would expect from the Second Law. And at first it also seems inconsistent with the reversibility of the system. For if all that is left at the end are a few simple structures, how can there be enough information to go backwards and reconstruct the initial conditions?

The answer is that one has to consider not only the stationary structures that stay in the middle of the system, but also all various small structures that were emitted in the course of the evolution. To go backwards one would need to set things up so that one absorbs exactly the sequence of structures that were emitted going forwards.

If, however, one just lets the emitted structures escape, and never absorbs any other structures, then one is effectively losing information. The result is that the evolution one sees can be intrinsically not reversible, so that all of the various forms of self-organization that we saw earlier in this book in cellular automata that do not have reversible rules can potentially occur.

If we look at the universe on a large scale, then it turns out that in a certain sense there is more radiation emitted than absorbed. Indeed, this is related to the fact that the night sky appears dark, rather than having bright starlight coming from every direction. But ultimately the asymmetry between emission and absorption is a consequence of the fact that the universe is expanding, rather than contracting, with time.

The result is that it is possible for regions of the universe to become progressively more organized, despite the Second Law, and despite the reversibility of their underlying rules. And this is a large part of the reason that organized galaxies, stars and planets can form.

Allowing information to escape is a rather straightforward way to evade the Second Law. But what the pictures on the facing page demonstrate is that even in a completely closed system, where no information at all is allowed to escape, a system like rule 37R still does not follow the uniform trend towards increasing randomness that is suggested by the Second Law.

What instead happens is that kinds of membranes form between different regions of the system, and within each region orderly behavior can then occur, at least while the membrane survives.

![](Images/_page_471_Picture_2.jpeg)

An example of evolution according to rule 37R from an initial condition containing a fairly random region. Even though the system is reversible, this region tends to organize itself so as to take on a much simpler form. Information on the initial conditions ends up being carried by localized structures which radiate outwards.

This basic mechanism may well be the main one at work in many biological systems: each cell or each organism becomes separated from others, and while it survives, it can exhibit organized behavior.

But looking at the pictures of rule 37R on page 454 one may ask whether perhaps the effects we see are just transients, and that if we waited long enough something different would happen.

It is an inevitable feature of having a closed system of limited size that in the end the behavior one gets must repeat itself. And in rules like 0R and 90R shown on page 452 the period of repetition is always very short. But for rule 37R it usually turns out to be rather long. Indeed, for the specific example shown on page 454, the period is 293,216,266.

In general, however, the maximum possible period for a system containing a certain number of cells can be achieved only if the evolution of the system from any initial condition eventually visits all the possible states of the system, as discussed on page 258. And if this in fact happens, then at least eventually the system will inevitably spend most of its time in states that seem quite random.

But in rule 37R there is no such ergodicity. And instead, starting from any particular initial condition, the system will only ever visit a tiny fraction of all possible states. Yet since the total number of states is astronomically large—about  $10^{60}$  for size 100—the number of states visited by rule 37R, and therefore the repetition period, can still be extremely long.

There are various subtleties involved in making a formal study of the limiting behavior of rule 37R after a very long time. But irrespective of these subtleties, the basic fact remains that so far as I can tell, rule 37R simply does not follow the predictions of the Second Law.

And indeed I strongly suspect that there are many systems in nature which behave in more or less the same way. The Second Law is an important and quite general principle—but it is not universally valid. And by thinking in terms of simple programs we have thus been able in this section not only to understand why the Second Law is often true, but also to see some of its limitations.

#### Conserved Quantities and Continuum Phenomena

Reversibility is one general feature that appears to exist in the basic laws of physics. Another is conservation of various quantities—so that for example in the evolution of any closed physical system, total values of quantities like energy and electric charge appear always to stay the same.

With most rules, systems like cellular automata do not usually exhibit such conservation laws. But just as with reversibility, it turns out to be possible to find rules that for example conserve the total number of black cells appearing on each step.

Among elementary cellular automata with just two colors and nearest-neighbor rules, the only types of examples are the fairly trivial ones shown in the pictures below.

![](Images/_page_473_Picture_5.jpeg)

Elementary cellular automata whose evolution conserves the total number of black cells. The behavior of the rules shown here is simple enough that in each case it is fairly obvious how the number of black cells manages to stay the same on every step.

But with next-nearest-neighbor rules, more complicated examples become possible, as the pictures below demonstrate.

![](Images/_page_474_Picture_2.jpeg)

Examples of cellular automata with next-nearest-neighbor rules whose evolution conserves the total number of black cells. Even though it is not immediately obvious by eye, the total number of black cells stays exactly the same on each successive step in each picture. Among the 4,294,967,296 possible next-nearest-neighbor rules, only 428 exhibit the kind of conservation property shown here.

One straightforward way to generate collections of systems that will inevitably exhibit conserved quantities is to work not with ordinary cellular automata but instead with block cellular automata. The basic idea of a block cellular automaton is illustrated at the top of the next page. At each step what happens is that blocks of adjacent cells are replaced by other blocks of the same size according to some definite rule. And then on successive steps the alignment of these blocks shifts by one cell.

![](Images/_page_475_Figure_2.jpeg)

An example of a block cellular automaton. The system works by partitioning the sequence of cells that exists at each step into pairs, then replacing these pairs by other pairs according to the rule shown. The choice of whether to pair a cell with its left or right neighbor alternates on successive steps. Like many block cellular automata, the system shown is reversible, since in the rule each pair has a unique predecessor. It does not, however, conserve the total number of black cells.

And with this setup, if the underlying rules replace each block by one that contains the same number of black cells, it is inevitable that the system as a whole will conserve the total number of black cells.

With two possible colors and blocks of size two the only kinds of block cellular automata that conserve the total number of black cells are the ones shown below—and all of these exhibit rather trivial behavior.

![](Images/_page_475_Picture_6.jpeg)

Block cellular automata with two possible colors and blocks of size two that conserve the total number of black cells (the last example has this property only on alternate steps). It so happens that all but the second of the rules shown here not only conserve the total number of black cells but also turn out to be reversible.

But if one allows three possible colors, and requires, say, that the total number of black and gray cells together be conserved, then more complicated behavior can occur, as in the pictures below.

![](Images/_page_476_Figure_3.jpeg)

Block cellular automata with three possible colors which conserve the combined number of black and gray cells. In rule (a), black and gray cells remain in localized regions. In rule (b), they move in fairly simple ways, and in rules (c) and (d), they move in a seemingly somewhat random way. The rules shown here are reversible, although their behavior is similar to that of non-reversible rules, at least after a few steps.

Indeed, as the pictures on the next page demonstrate, such systems can produce considerable randomness even when starting from very simple initial conditions.

![](Images/_page_477_Figure_2.jpeg)

The behavior of rules (c) and (d) from the previous page, starting with very simple initial conditions. Each panel shows 500 steps of evolution, and rapid randomization is evident. The black and gray cells behave much like physical particles: their total number is conserved, and with the particular rules used here, their interactions are reversible. Note that the presence of boundaries is crucial; for without them there would in a sense be no collisions between particles, and the behavior of both systems would be rather trivial.

But there is still an important constraint on the behavior: even though black and gray cells may in effect move around randomly, their total number must always be conserved. And this means that if one looks at the total average density of colored cells throughout the system, it must always remain the same. But local densities in different parts of the system need not—and in general they will change as colored cells flow in and out.

The pictures below show what happens with four different rules, starting with higher density in the middle and lower density on the sides. With rules (a) and (b), each different region effectively remains separated forever. But with rules (c) and (d) the regions gradually mix.

As in many kinds of systems, the details of the initial arrangement of cells will normally have an effect on the details of the behavior that occurs. But what the pictures below suggest is that if one looks only at the overall distribution of density, then these details will become largely irrelevant—so that a given initial distribution of density will always tend to evolve in the same overall way, regardless of what particular arrangement of cells happened to make up that distribution.

![](Images/_page_478_Picture_5.jpeg)

![](Images/_page_478_Picture_6.jpeg)

![](Images/_page_478_Picture_7.jpeg)

![](Images/_page_478_Picture_8.jpeg)

The block cellular automata from previous pages started from initial conditions containing regions of different density. In rules (a) and (b) the regions remain separated forever, but in rules (c) and (d) they gradually diffuse into each other.

![](Images/_page_479_Picture_1.jpeg)

The evolution of overall density for block cellular automata (c) and (d) from the previous page. Even though at an underlying level these systems consist of discrete cells, their overall behavior seems smooth and continuous. The results shown here are obtained by averaging over progressively larger numbers of runs with initial conditions that differ in detail, but have the same overall density distribution. In the limit of an infinite number of runs (or infinite number of cells), the behavior in the second case approaches the form implied by the continuum diffusion equation. (In the first case correlations in effect last too long to yield exactly such behavior.)

The pictures above then show how the average density evolves in systems (c) and (d). And what is striking is that even though at the lowest level both of these systems consist of discrete cells, the overall distribution of density that emerges in both cases shows smooth continuous behavior.

And much as in physical systems like fluids, what ultimately leads to this is the presence of small-scale apparent randomness that washes out details of individual cells or molecules—as well as of conserved quantities that force certain overall features not to change too quickly. And in fact, given just these properties it turns out that essentially the same overall continuum behavior always tends to be obtained.

One might have thought that continuum behavior would somehow rely on special features of actual systems in physics. But in fact what we have seen here is that once again the fundamental mechanisms responsible already occur in a much more minimal way in programs that have some remarkably simple underlying rules.

#### Ultimate Models for the Universe

The history of physics has seen the development of a sequence of progressively more accurate models for the universe—from classical mechanics, through quantum mechanics, to quantum field theory, and beyond. And one may wonder whether this process will go on forever, or whether at some point it will come to an end, and one will reach a final ultimate model for the universe.

Experience with actual results in physics would probably not make one think so. For it has seemed that whenever one tries to get to another level of accuracy, one encounters more complex phenomena. And at least with traditional scientific intuition, this fact suggests that models of progressively greater complexity will be needed.

But one of the crucial points discovered in this book is that more complex phenomena do not always require more complex models. And indeed I have shown that even models based on remarkably simple programs can produce behavior that is in a sense arbitrarily complex.

So could this be what happens in the universe? And could it even be that underneath all the complex phenomena we see in physics there lies some simple program which, if run for long enough, would reproduce our universe in every detail?

The discovery of such a program would certainly be an exciting event—as well as a dramatic endorsement for the new kind of science that I have developed in this book.

For among other things, with such a program one would finally have a model of nature that was not in any sense an approximation or idealization. Instead, it would be a complete and precise representation of the actual operation of the universe—but all reduced to readily stated rules.

In a sense, the existence of such a program would be the ultimate validation of the idea that human thought can comprehend the construction of the universe. But just knowing the underlying program does not mean that one can immediately deduce every aspect of how the universe will behave. For as we have seen many times in this book, there is often a great distance between underlying rules and overall

behavior. And in fact, this is precisely why it is conceivable that a simple program could reproduce all the complexity we see in physics.

Given a particular underlying program, it is always in principle possible to work out what it will do just by running it. But for the whole universe, doing this kind of explicit simulation is almost by definition out of the question. So how then can one even expect to tell whether a particular program is a correct model for the universe? Small-scale simulation will certainly be possible. And I expect that by combining this with a certain amount of perhaps fairly sophisticated mathematical and logical deduction, it will be possible to get at least as far as reproducing the known laws of physics—and thus of determining whether a particular model has the potential to be correct.

So if there is indeed a definite ultimate model for the universe, how might one set about finding it? For those familiar with existing science, there is at first a tremendous tendency to try to work backwards from the known laws of physics, and in essence to try to "engineer" a universe that will have particular features that we observe.

But if there is in fact an ultimate model that is quite simple, then from what we have seen in this book, I strongly believe that such an approach will never realistically be successful. For human thinking—even supplemented by the most sophisticated ideas of current mathematics and logic—is far from being able to do what is needed.

Imagine for example trying to work backwards from a knowledge of the overall features of the picture on the facing page to construct a rule that would reproduce it. With great effort one might perhaps come up with some immensely complex rule that would work in most cases. But there is no serious possibility that starting from overall features one would ever arrive at the extremely simple rule that was actually used.

It is already difficult enough to work out from an underlying rule what behavior it will produce. But to invert this in any systematic way is probably even in principle beyond what any realistic computation can do.

So how then could one ever expect to find the underlying rule in such a case? Almost always, it seems that the best strategy is a simple one: to come up with an appropriate general class of rules, and then just

![](Images/_page_482_Figure_1.jpeg)

A typical example of a situation where it would be very difficult to deduce the underlying rule from a description of the overall behavior that it produces. There is in a sense too great a distance between the simple rule shown and the behavior that emerges from it. I suspect that the same will be true of the basic rule for the universe. The particular rule shown here is the elementary cellular automaton with rule number 94, and with initial condition

to search through these rules, trying each one in turn, and looking to see if it produces the behavior one wants.

But what about the rules for the universe? Surely we cannot simply search through possible rules of certain kinds, looking for one whose behavior happens to fit what we see in physics?

With the intuition of traditional science, such an approach seems absurd. But the point is that if the rule for the universe is sufficiently simple—and the results of this book suggest that it might be—then it becomes not so unreasonable to imagine systematically searching for it.

To start performing such a search, however, one first needs to work out what kinds of rules to consider. And my suspicion is that none of the specific types of rules that we have discussed so far in this book will turn out to be adequate. For I believe that all these types of rules in some sense probably already have too much structure built in.

Thus, for example, cellular automata probably already have too rigid a built-in notion of space. For a defining feature of cellular automata is that their cells are always arranged in a rigid array in space. Yet I strongly suspect that in the underlying rule for our universe there will be no such built-in structure. Rather, as I discuss in the sections

that follow, my guess is that at the lowest level there will just be certain patterns of connectivity that tend to exist, and that space as we know it will then emerge from these patterns as a kind of large-scale limit.

And indeed in general what I expect is that remarkably few familiar features of our universe will actually be reflected in any direct way in its ultimate underlying rule. For if all these features were somehow explicitly and separately included, the rule would necessarily have to be very complicated to fit them all in.

So if the rule is indeed simple, it almost inevitably follows that we will not be able to recognize directly in it most features of the universe as we normally perceive them. And this means that the rule—or at least its behavior—will necessarily seem to us unfamiliar and abstract.

Most likely for example there will be no easy way to visualize what the rule does by looking at a collection of elements laid out in space. Nor will there probably be any immediate trace of even such basic phenomena as motion.

But despite the lack of these familiar features, I still expect that the actual rule itself will not be too difficult for us to represent. For I am fairly certain that the kinds of logical and computational constructs that we have discussed in this book will be general enough to cover what is needed. And indeed my guess is that in terms of the kinds of pictures—or *Mathematica* programs—that we have used in this book, the ultimate rule for the universe will turn out to look quite simple.

No doubt there will be many different possible formulations—some quite unrecognizably different from others. And no doubt a formulation will eventually be found in which the rule somehow comes to seem quite obvious and inevitable.

But I believe that it will be essentially impossible to find such a formulation without already knowing the rule. And as a result, my guess is that the only realistic way to find the rule in the first place will be to start from some very straightforward representation, and then just to search through large numbers of possible rules in this representation.

Presumably the vast majority of rules will lead to utterly unworkable universes, in which there is for example no reasonable notion of space or no reasonable notion of time.

But my guess is that among appropriate classes of rules there will actually be quite a large number that lead to universes which share at least some features with our own. Much as the same laws of continuum fluid mechanics can emerge in systems with different underlying rules for molecular interactions, so also I suspect that properties such as the existence of seemingly continuous space, as well as certain features of gravitation and quantum mechanics, will emerge with many different possible underlying rules for the universe.

But my guess is that when it comes to something like the spectrum of masses of elementary particles—or perhaps even the overall dimensionality of space—such properties will be quite specific to particular underlying rules.

In traditional approaches to modelling, one usually tries first to reproduce some features of a system, then goes on to reproduce others. But if the ultimate rule for the universe is at all simple, then it follows that every part of this rule must in a sense be responsible for a great many different features of the universe. And as a result, it is not likely to be possible to adjust individual parts of the rule without having an effect on a whole collection of disparate features of the universe.

So this means that one cannot reasonably expect to use some kind of incremental procedure to find the ultimate rule for the universe. But it also means that if one once discovers a rule that reproduces sufficiently many features of the universe, then it becomes extremely likely that this rule is indeed the final and correct one for the whole universe.

And I strongly suspect that even in many of the most basic everyday physical processes, every element of the underlying rule for the universe will be very extensively exercised. And as a result, if these basic processes are reproduced correctly, then I believe that one can have considerable confidence that one in fact has the complete rule for the universe.

Looking at the history of physics, one might think that it would be completely inadequate just to reproduce everyday physical processes. For one might expect that there would always be some other esoteric phenomenon, say in particle physics, that would be discovered and would show that whatever rule one has found is somehow incomplete. But I do not think so. For if the rule for our universe is at all simple, then I expect that to introduce a new phenomenon, however esoteric, will involve modifying some basic part of the rule, which will also affect even common everyday phenomena.

But why should we believe that the rule for our universe is in fact simple? Certainly among all possible rules of a particular kind only a limited number can ever be considered simple, and these rules are by definition somehow special. Yet looking at the history of science, one might expect that in the end there would turn out to be nothing special about the rule for our universe—just as there has turned out to be nothing special about our position in the solar system or the galaxy.

Indeed, one might assume that there are in fact an infinite number of universes, each with a different rule, and that we simply live in a particular—and essentially arbitrary—one of them.

It is unlikely to be possible to show for certain that such a theory is not correct. But one of its consequences is that it gives us no reason to think that the rule for our particular universe should be in any way simple. For among all possible rules, the overwhelming majority will not be simple; in fact, they will instead tend to be almost infinitely complex.

Yet we know, I think, that the rule for our universe is not too complex. For if the number of different parts of the rule were, for example, comparable to the number of different situations that have ever arisen in the history of the universe, then we would not expect ever to be able to describe the behavior of the universe using only a limited number of physical laws.

And in fact if one looks at present-day physics, there are not only a limited number of physical laws, but also the individual laws often seem to have the simplest forms out of various alternatives. And knowing this, one might be led to believe that for some reason the universe is set up to have the simplest rules throughout.

But, unfortunately perhaps, I do not think that this conclusion necessarily follows. For as I have discussed above, I strongly suspect that the vast majority of physical laws discovered so far are not truly fundamental, but are instead merely emergent features of the large-scale behavior of some ultimate underlying rule. And what this means is that any simplicity observed in known physical laws may have little connection with simplicity in the underlying rule.

Indeed, it turns out that simple overall laws can emerge almost regardless of underlying rules. And thus, for example, essentially as a consequence of randomness generation, a wide range of cellular automata show the simple density diffusion law on page 464—whether or not their underlying rules happen to be simple.

So it could be that the laws that we have formulated in existing physics are simple not because of simplicity in an ultimate underlying rule, but rather because of some general property of emergent behavior for the kinds of overall features of the universe that we readily perceive.

Indeed, with this kind of argument, one could be led to think that there might be no single ultimate rule for the universe at all, but that instead there might somehow be an infinite sequence of levels of rules, with each level having a certain simplicity that becomes increasingly independent of the details of the levels below it.

But one should not imagine that such a setup would make it unnecessary to ask why our universe is the way it is: for even though certain features might be inevitable from the general properties of emergent behavior, there will, I believe, still be many seemingly arbitrary choices that have to be made in arriving at the universe in which we live. And once again, therefore, one will have to ask why it was these choices, and not others, that were made.

So perhaps in the end there is the least to explain if I am correct that the universe just follows a single, simple, underlying rule.

There will certainly be questions about why it is this particular rule, and not another one. And I am doubtful that such questions will ever have meaningful answers.

But to find the ultimate rule will be a major triumph for science, and a clear demonstration that at least in some direction, human thought has reached the edge of what is possible.

#### The Nature of Space

In the effort to develop an ultimate model for the universe, a crucial first step is to think about the nature of space—for inevitably it is in space that the processes in our universe occur.

Present-day physics almost always assumes that space is a perfect continuum, in which objects can be placed at absolutely any position. But one can certainly imagine that space could work very differently. And for example in a cellular automaton, space is not a continuum but instead consists just of discrete cells.

In our everyday experience space nevertheless appears to be continuous. But then so, for example, do fluids like air and water. And yet in the case of these fluids we know that at an underlying level they are composed of discrete molecules. And in fact over the course of the past century a great many aspects of the physical world that at first seemed continuous have in the end been discovered to be built up from discrete elements. And I very strongly suspect that this will also be true of space.

Particle physics experiments have shown that space acts as a continuum down to distances of around  $10^{-20}$  meters—or a hundred thousandth the radius of a proton. But there is absolutely no reason to think that discrete elements will not be found at still smaller distances.

And indeed, in the past one of the main reasons that space has been assumed to be a perfect continuum is that this makes it easier to handle in the context of traditional mathematics. But when one thinks in terms of programs and the kinds of systems I have discussed in this book, it no longer seems nearly as attractive to assume that space is a perfect continuum.

So if space is not in fact a continuum, what might it be? Could it, for example, be a regular array of cells like in a cellular automaton?

At first, one might think that this would be completely inconsistent with everyday observations. For even though the individual cells in the array might be extremely small, one might still imagine that one would for example see all sorts of signs of the overall orientation of the array.

The pictures below show three different cellular automata, all set up on the same two-dimensional grid. And to see the effect of the grid, I show what happens when each of these cellular automata is started from blocks of black cells arranged at three different angles.

![](Images/_page_488_Figure_2.jpeg)

Examples of orientation dependence in the behavior of two-dimensional cellular automata on a fixed grid. Three different initial conditions, consisting of blocks at three different angles, are shown. For rules (a) and (b) the patterns produced always exhibit features that remain aligned with directions in the underlying grid. But with rule (c) essentially the same rounded pattern is obtained regardless of orientation. The rules shown here are outer totalistic: (a) 4-neighbor code 468, (b) 4-neighbor code 686 and (c) 8-neighbor code 746. In cases (a) and (b) 40 steps of evolution are used; in case (c) 100 steps are used.

In all cases the patterns produced follow at least to some extent the orientation of the initial block. But in cases (a) and (b) the effects of the underlying grid remain quite obvious—for the patterns produced always have facets aligned with the directions in this grid. But in case (c) the situation is different, and now the patterns produced turn out always to have the same overall rounded form, essentially independent of their orientation with respect to the underlying grid.

And indeed what happens is similar to what we have seen many times in this book: the evolution of the cellular automaton generates enough randomness that the effects of the underlying grid tend to be washed out, with the result that the overall behavior produced ends up showing essentially no distinction between different directions in space.

So should one conclude from this that the universe is in fact a giant cellular automaton with rules like those of case (c)?

It is perhaps not impossible, but I very much doubt it.

For there are immediately simple issues like what one imagines happens at the edges of the cellular automaton array. But much more important is the fact that I do not believe in the distinction between space and its contents implied by the basic construction of a cellular automaton.

For when one builds a cellular automaton one is in a sense always first setting up an array of cells to represent space itself, and then only subsequently considering the contents of space, as represented by the arrangement of colors assigned to the cells in this array.

But if the ultimate model for the universe is to be as simple as possible, then it seems much more plausible that both space and its contents should somehow be made of the same stuff—so that in a sense space becomes the only thing in the universe.

Several times in the past ideas like this have been explored. And indeed the standard theory for gravity introduced in 1915 is precisely based on the notion that gravity can be viewed merely as a feature of space. But despite various attempts in the 1930s and more recently it has never seemed possible to extend this to cover the whole elaborate collection of forces and particles that we actually see in our universe.

Yet my suspicion is that a large part of the reason for this is just the assumption that space is a perfect continuum—described by traditional mathematics. For as we have seen many times in this book, if one looks at systems like programs with discrete elements then it immediately becomes much easier for highly complex behavior to emerge. And this is fundamentally what I believe is happening at the lowest level in space throughout our universe.

#### Space as a Network

In the last section I argued that if the ultimate model of physics is to be as simple as possible, then one should expect that all the features of our universe must at some level emerge purely from properties of space. But what should space be like if this is going to be the case?

The discussion in the section before last suggests that for the richest properties to emerge there should in a sense be as little rigid underlying structure built in as possible. And with this in mind I believe that what is by far the most likely is that at the lowest level space is in effect a giant network of nodes.

In an array of cells like in a cellular automaton each cell is always assigned some definite position. But in a network of nodes, the nodes are not intrinsically assigned any position. And indeed, the only thing that is defined about each node is what other nodes it is connected to.

Yet despite this rather abstract setup, we will see that with a sufficiently large number of nodes it is possible for the familiar properties of space to emerge—together with other phenomena seen in physics.

I already introduced in Chapter 5 a particular type of network in which each node has exactly two outgoing connections to other nodes, together with any number of incoming connections. The reason I chose this kind of network in Chapter 5 is that there happens to be a fairly easy way to set up evolution rules for such networks. But in trying to find an ultimate model of space, it seems best to start by considering networks that are somehow as simple as possible in basic structure—and it turns out that the networks of Chapter 5 are somewhat more complicated than is necessary.

For one thing, there is no need to distinguish between incoming and outgoing connections, or indeed to associate any direction with each connection. And in addition, nothing fundamental is lost by requiring that all the nodes in a network have exactly the same total number of connections to other nodes.

With two connections, only very trivial networks can ever be made. But if one uses three connections, a vast range of networks immediately become possible. One might think that one could get a

![](Images/_page_491_Picture_1.jpeg)

Examples of how nodes with more than three connections can be decomposed into collections of nodes with exactly three connections.

fundamentally larger range if one allowed, say, four or five connections rather than just three. But in fact one cannot, since any node with more than three connections can in effect always be broken into a collection of nodes with exactly three connections, as in the pictures on the left.

So what this means is that it is in a sense always sufficient to consider networks with exactly three connections at each node. And it is therefore these networks that I will use here in discussing fundamental models of space.

The pictures below show a few small examples of such networks. And already considerable diversity is evident. But none of the networks shown seem to have many properties familiar from ordinary space.

![](Images/_page_491_Picture_6.jpeg)

Examples of small networks with exactly three connections at each node. The first line shows all possible networks with up to four nodes. In what follows I consider only non-degenerate networks, in which there is at most one connection between any two nodes. Example (i) is the smallest network that cannot be drawn in two dimensions without lines crossing. Examples (k) and (l) are the smallest networks that have no symmetries between different nodes. Example (e) corresponds to the net of a tetrahedron, (j) to the net of a cube, and (m) to the net of a dodecahedron. Examples (o) through (u) show seven ways of drawing the same network, in this case the so-called Petersen network.

So how then can one get networks that correspond to ordinary space? The first step is to consider networks that have much larger numbers of nodes. And as examples of these, the pictures at the top of the facing page show networks that are specifically constructed to correspond to ordinary one-, two- and three-dimensional space.

![](Images/_page_492_Picture_2.jpeg)

Examples of networks with three connections at each node that are effectively one, two and three-dimensional. These networks can be continued forever, and all have the property of being homogeneous, in the sense that every node has an environment identical to every other node.

Each of these networks is at the lowest level just a collection of nodes with certain connections. But the point is that the overall pattern of these connections is such that on a large scale there emerges a clear correspondence to ordinary space of a particular dimension.

The pictures above are drawn so as to make this correspondence obvious. But what if one was just presented with the raw pattern of connections for some network? How could one see whether the network could correspond to ordinary space of a particular dimension?

The pictures below illustrate the main difficulty: given only its pattern of connections, a particular network can be laid out in many completely different ways, most of which tell one very little about its potential correspondence with ordinary space.

![](Images/_page_492_Picture_7.jpeg)

![](Images/_page_492_Picture_9.jpeg)

![](Images/_page_492_Picture_10.jpeg)

![](Images/_page_492_Picture_11.jpeg)

![](Images/_page_492_Picture_12.jpeg)

Six different ways of laying out the same network. (a) nodes arranged around a circle; (b) nodes arranged along a line; (c) nodes arranged across the page according to distance from a particular node; (d) 2D layout with network and spatial distances as close as possible; (e) planar layout; (f) 3D layout.

So how then can one proceed? The fundamental idea is to look at properties of networks that can both readily be deduced from their pattern of connections and can also be identified, at least in some

large-scale limit, with properties of ordinary space. And the notion of distance is perhaps the most fundamental of such properties.

A simple way to define the distance between two points is to say that it is the length of the shortest path between them. And in ordinary space, this is normally calculated by subtracting the numerical coordinates of the positions of the points. But on a network things become more direct, and the distance between two nodes can be taken to be simply the minimum number of connections that one has to follow in order to get from one node to the other.

But can one tell just by looking at such distances whether a particular network corresponds to ordinary space of a certain dimension?

To a large extent one can. And a test is to see whether there is a way to lay out the nodes in the network in ordinary space so that the distances between nodes computed from their positions in space agree—at least in some approximation—with the distances computed directly by following connections in the network.

The three networks at the top of the previous page were laid out precisely so as to make this the case respectively for one, two and three-dimensional space. But why for example can the second network not be laid out equally well in one-dimensional rather than two-dimensional space? One way to see this is to count the number of nodes that appear at a given distance from a particular node in the network.

And for this specific network, the answer for this is very simple: at distance r there are exactly 3 r nodes—so that the total number of nodes out to distance r grows like  $r^2$ . But now if one tried to lay out all these nodes in one dimension it is inevitable that the network would have to bulge out in order to fit in all the nodes. And it turns out that it is uniquely in two dimensions that this particular network can be laid out in a regular way so that distances based on following connections in it agree with ordinary distances in space.

For the other two networks at the top of the previous page similar arguments can be given. And in fact in general the condition for a network to correspond to ordinary d-dimensional space is precisely that the total number of nodes that appear in it out to distance r grows in some limiting sense like  $r^d$ —a result analogous to the standard

mathematical fact that the area of a two-dimensional circle is  $\pi r^2$ , while the volume of a three-dimensional sphere is  $4/3 \pi r^3$ , the volume of a four-dimensional hypersphere is  $1/2 \pi^2 r^4$ , and so on.

Below I show pictures of various networks. In each case the first picture is drawn to emphasize obvious regularities in the network. But the second picture is drawn in a more systematic way—by picking a specific starting node, and then laying out other nodes so that those at

![](Images/_page_494_Picture_4.jpeg)

Examples of various networks, shown first to emphasize their regularities, and second to illustrate the number of nodes reached by going successively more steps from a given node. For networks that in a limiting sense correspond to ordinary d-dimensional space, this number grows like  $r^{d-1}$ . All the larger networks shown are approximately uniform, in the sense that similar results are obtained starting from any node. Network (e) effectively has limiting dimension  $Log[2, 3] \approx 1.58$ .

successively greater network distances appear in successive columns across the page. And this setup has the feature that the height of column r gives the number of nodes that are at network distance r.

So by looking at how these heights grow across the page, one can see whether there is a correspondence with the  $r^{d-1}$  form that one expects for ordinary d-dimensional space. And indeed in case (g), for example, one sees exactly  $r^1$  linear growth, reflecting dimension 2.

Similarly, in case (d) one sees  $r^0$  growth, reflecting dimension 1, while in case (h) one sees  $r^2$  growth, reflecting dimension 3.

Case (f) illustrates slightly more complicated behavior. The basic network in this case locally has an essentially two-dimensional form—but at large scales it is curved by being wrapped around a sphere. And what therefore happens is that for fairly small r one sees  $r^1$  growth—reflecting the local two-dimensional form—but then for larger r there is slower growth, reflecting the presence of curvature.

Later in this chapter we will see how such curvature is related to the phenomenon of gravity. But for now the point is just that network (f) again behaves very much like ordinary space with a definite dimension.

So do all sufficiently large networks somehow correspond to ordinary space in a certain number of dimensions? The answer is definitely no. And as an example, network (i) from the previous page has a tree-like structure with  $3^r$  nodes at distance r. But this number grows faster than  $r^d$  for any d—implying that the network has no correspondence to ordinary space in any finite number of dimensions.

If the connections in a network are chosen at random—as in case (j)—then again there will almost never be the kind of locality that is needed to get something that corresponds to ordinary finite-dimensional space.

So what might an actual network for space in our universe be like?

It will certainly not be as simple and regular as most of the networks on the previous page. For within its pattern of connections must be encoded everything we see in our universe.

And so at the level of individual connections, the network will most likely at first look quite random. But on a larger scale, it must be arranged so as to correspond to ordinary three-dimensional space. And somehow whatever rules update the network must preserve this feature.

#### The Relationship of Space and Time

To make an ultimate theory of physics one needs to understand the true nature not only of space but also of time. And I believe that here again the idea of thinking in terms of programs provides some crucial insights.

In our everyday experience space and time seem very different. For example, we can move from one point in space to another in more or less any way we choose. But we seem to be forced to progress through time in a very specific way. Yet despite such obvious apparent differences, almost all models in present-day fundamental physics have been built on the idea that space and time somehow work fundamentally the same.

But for most of the systems based on programs that I have discussed in this book this is certainly not true. And thus for example in a cellular automaton moving from one point in space to another just corresponds to shifting from one cell to another. But moving from one point in time to another involves actually applying the cellular automaton rule.

When we make a picture of the behavior of a cellular automaton, however, we do nevertheless tend to represent space and time in the same visual kind of way—with space going across the page and time going down. And in fact the basic notion of extending the idea of position in space to an idea of position in time has been common in scientific thought for more than five centuries.

But in the past century what has happened is that space and time have come to be thought of as being much more fundamentally similar. As we will discuss later in this chapter, the main origin of this is that in relativity theory certain aspects of space and time seem to become interchangeable. And from this there emerged the idea of thinking in terms of a spacetime continuum in which time appears merely as a fourth dimension just like the three ordinary dimensions of space.

So while in a system like a cellular automaton one typically imagines that a new and separate state of the system is somehow produced at each step in time, present-day physics more tends to think of the complete history of the universe throughout time as being just a single structure laid out in the four dimensions of spacetime.

So what then might determine the form of this structure?

The laws of physics in effect provide a collection of constraints on the structure. And while these laws are traditionally stated in terms of sophisticated mathematical equations, their basic character is similar to the simple constraints on arrays of black and white cells that I discussed at the end of Chapter 5. But now instead of defining constraints just in space, the laws of physics can be thought of as defining constraints on what can happen in both space and time.

Just as for space, it is my strong belief that time is fundamentally discrete. And from the discussion of networks for space in the previous section, one might imagine that perhaps the whole history of the universe in spacetime could be represented by a giant four-dimensional network.

By analogy with the systems at the end of Chapter 5 a simple model would then be that this network is determined by the constraint that around every one of its nodes the overall arrangement of other nodes must match some particular template or set of templates.

Yet much as in Chapter 5 it turns out often not to be especially easy to find out which networks, if any, satisfy specific constraints of this kind. The pictures on the facing page nevertheless show results for quite a few choices of templates—where in each case the dangling connections in a template are taken to go to nodes that are not part of the template itself.

Pictures (a) and (b) show what happens with the two very simplest possible templates—involving just a single node. In case (a), all networks are allowed except for ones in which a node is connected directly to itself. In case (b), only the single network shown is allowed.

With templates that involve nodes out to distance one there are a total of 11 distinct non-trivial cases. And of these, 8 allow no complete networks to be formed, as in picture (e). But there turn out to be three cases—shown as pictures (c), (d) and (f)—in which complete networks can be formed, and in each of these one discovers that a fairly simple infinite set of networks are actually allowed.

In order to have a meaningful model for the universe, however, what must presumably happen is that essentially just one network can satisfy whatever constraints there are, and this one network must then represent all of the complex spacetime history of our universe.

![](Images/_page_498_Picture_1.jpeg)

Examples of networks determined by constraints. In each case the networks shown are required to satisfy the constraint that around every node their form must correspond to the template shown, in such a way that no dangling connections in the template are joined to each other. The pictures include all 14 templates that involve nodes out to distance at most two for which complete networks can be formed. In most cases where any such network can be formed, an infinite sequence of networks is allowed. But in cases (b), (h), (i) and (j) just a single network turns out to be allowed. The network constraint systems shown here are analogs of the two-dimensional systems based on constraints discussed at the end of Chapter 5.

So what does one find if one allows templates that include nodes out to distance two? There are a total of 690 distinct non-trivial such templates—and of these, 681 allow no complete networks to be formed, as in case (g). Six of the remaining templates then again allow an infinite sequence of networks. But there are three templates—shown as cases (h), (i) and (j)—that turn out to allow just single networks. These networks are however rather simple, and indeed the most complicated of them—case (i)—has just 20 nodes, and corresponds to a dodecahedron.

So are there in fact reasonably simple sets of constraints that in the end allow just one highly complex network, or perhaps a family of similar networks? I tend to doubt it. For our experience in Chapter 5 was that even in the much more rigid case of arrays of black and white squares, it was rather difficult to find constraints that would succeed in forcing anything but very simple patterns to occur.

So what does this mean for getting the kind of complexity that we see in our universe? We have not had difficulty in getting remarkable complexity from systems like cellular automata that we have discussed in this book. But such systems work not by being required to satisfy constraints, but instead by just repeatedly applying explicit rules.

So is it in the end sensible to think of the universe as a single structure in spacetime whose form is determined by a set of constraints? Should we really imagine that the complete spacetime history of the universe somehow always exists, and that as time progresses, we are merely exploring different parts of it? Or should we instead think that the universe—more like systems such as cellular automata—explicitly evolves in time, so that at each moment a new state of the universe is in effect created, and the old one is lost?

Models based on traditional mathematical equations—in which space and time appear just as abstract symbolic variables—have never had to make much distinction between these two views. But in trying to understand the ultimate underlying mechanisms of the universe, I believe that one must inevitably distinguish between these views.

And I strongly believe that the second view is the one most likely to provide a meaningful underlying model for our universe. But while this view is closer to our everyday perception of time, it seems to contradict the correspondence between space and time that is built into most of present-day physics. So one might wonder how then it could be consistent with experiments that have been done in physics?

One possibility, illustrated in the pictures below, is to have a system that evolves in time according to explicit rules, but for these rules to have built into them a symmetry between space and time.

![](Images/_page_500_Figure_3.jpeg)

Examples of one-dimensional cellular automata which exhibit a symmetry between space and time. Each picture can be generated by starting from initial conditions at the top, and then just evolving down the page repeatedly applying the cellular automaton rule. The particular rules shown are reversible second-order ones with numbers 90R and 150R.

But I very much doubt that any such obvious symmetry between space and time exists in the fundamental rules for our universe. And instead what I expect is much like we have seen many times before in this book: that even though at the lowest level there is no direct correspondence between space and time, such a correspondence nevertheless emerges when one looks in the appropriate way at larger scales of the kind probed by practical experiments.

As I will discuss in the next several sections, I suspect that for many purposes the history of the universe can in fact be represented by a certain kind of spacetime network. But the way this network is formed in effect treats space and time rather differently. And in particular—just as in a system like a cellular automaton—the network can be built up incrementally by starting with certain initial conditions and then applying appropriate underlying rules over and over again.

Any such rules can in principle be thought of as providing a set of constraints for the spacetime network. But the important point is that there is no need to do a separate search to find networks that satisfy such constraints—for the rules themselves instead immediately define a procedure for building up the necessary network.

#### Time and Causal Networks

I argued in the last section that the progress of time should be viewed at a fundamental level much like the evolution of a system like a cellular automaton. But one of the features of a cellular automaton is that it is set up to update all of its cells together, as if at each tick of some global clock. Yet just as it seems unreasonable to imagine that the universe consists of a rigid grid of cells in space, so also it seems unreasonable to imagine that there is a global clock which defines the updating of every element in the universe synchronized in time.

But what is the alternative? At first it may seem bizarre, but one possibility that I believe is ultimately not too far from correct is that the universe might work not like a cellular automaton in which all cells get updated at once, but instead like a mobile automaton or Turing machine, in which just a single cell gets updated at each step.

As discussed in Chapter 3—and illustrated in the picture on the right—a mobile automaton has just a single active cell which moves around from one step to the next. And because this active cell is the only one that ever gets updated, there is never any issue about synchronizing behavior of different elements at a given step.

Yet at first it might seem absurd to think that our universe could work like a mobile automaton. For certainly we do not notice any kind of active cell visiting different places in the universe in sequence. And indeed, to the contrary, our perception is that different parts of the universe seem to evolve in parallel and progress through time together.

But it turns out that what one perceives as happening in a system like a mobile automaton can depend greatly on whether one is looking at the system from outside, or whether one is oneself somehow part of the system. For from the outside, one can readily see each individual step in the evolution of a mobile automaton, and one can tell that there is just a single active cell that visits different parts of the system in sequence. But to an observer who is actually part of the mobile automaton, the perception can be quite different.

For in order to recognize that time has passed, or indeed that anything has happened, the state of the observer must somehow change. But if the observer itself just consists of a collection of cells inside a mobile automaton, then no such change can occur except on steps when the active cell in the mobile automaton visits this collection of cells.

And what this means is that between any two successive moments of time as perceived by an observer inside the mobile automaton, there can be a great many steps of underlying mobile automaton evolution.

If an observer could tell what was happening on every step, then it would be easy to recognize the sequential way in which cells are updated. But because an observer who is part of a mobile automaton can in effect only occasionally tell what has happened, then as far as such an observer is concerned, many cells can appear to have been updated in parallel between successive moments of time.

To see in more detail how this works it could be that it would be necessary to make a specific model for the observer. But in fact, it turns out that it is sufficient just to look at the evolution of the mobile

![](Images/_page_502_Picture_8.jpeg)

A mobile automaton in which only the single active cell indicated by a dot is updated at each step, thereby avoiding the issue of global synchronization.

automaton not in terms of individual steps, but rather in terms of updating events and the causal relationships between them.

The pictures on the facing page show an example of how this works. Picture (a) is a version of the standard representation that I have used for mobile automaton evolution elsewhere in the book—in which successive lines give the colors of cells on successive steps, and the position of the active cell is indicated at each step by a gray dot. The subsequent pictures on the facing page all ultimately give essentially the same information, but gradually present it to emphasize more a representation in terms of updating events and causal relationships.

Picture (b) is very similar to (a), but shows successive steps of mobile automaton evolution separated, with gray blobs in between indicating "updating events" corresponding to each application of the underlying mobile automaton rule. Picture (b) still has a definite row of cells for each individual step of mobile automaton evolution. But in picture (c) cells not updated on a given step are merged together, yielding vertical stripes of color that extend from one updating event to another.

So what is the significance of these stripes? In essence they serve to carry the information needed to determine what the next updating event will be. And as picture (d) begins to emphasize, one can think of these stripes as indicating what causal relationships or connections exist between updating events.

And this notion then suggests a quite different representation for the whole evolution of the mobile automaton. For rather than having a picture based on successive individual steps of evolution, one can instead form a network of the various causal relationships between updating events, with each updating event being a node in this network, and each stripe being a connection from one node to another.

A sequence of views of the evolution of a mobile automaton, showing how a network of causal relationships between updating events can be created. This network provides a very simple model for spacetime in the universe. Picture (a) is essentially the standard representation of mobile automaton evolution that I have used in this book. Picture (b) includes gray blobs to indicate updating events. Picture (c) merges cells that are not being updated. Picture (d) emphasizes the role of vertical stripes as connections between updating events. Pictures (e) through (g) show how a network can be formed with nodes corresponding to updating events. Pictures (h) and (i) demonstrate that with the particular underlying rule used here, a highly regular network is produced.

![](Images/_page_504_Picture_1.jpeg)

Picture (e) shows the updating events and stripes from the top of picture (d), with the updating events now explicitly numbered. Pictures (f) and (g) then show how one can take the pattern of connectivity from picture (e) and lay out the updating events as nodes so as to produce an orderly network. And for the particular mobile automaton rule used here, the network one gets ends up being highly regular, as illustrated in pictures (h) and (i).

So what is the significance of this network? It turns out that it can be thought of as defining a structure for spacetime as perceived by an observer inside the mobile automaton—in much the same way as the networks we discussed two sections ago could be thought of as defining a structure for space. Each updating event, corresponding to each node in the network, can be imagined to take place at some point in spacetime. And the connections between nodes in the network can then be thought of as defining the pattern of neighbors for points in spacetime.

But unlike in the space networks that we discussed two sections ago, the connections in the causal networks we consider here always go only one way: each connection corresponds to a causal relationship in which one event leads to another, but not the other way around.

This kind of directionality, however, is exactly what is needed if a meaningful notion of time is to emerge. For the progress of time can be defined by saying that only those events that occur later in time than a particular event can be affected by that event.

And indeed the networks in pictures (g) through (i) on the previous page were specifically laid out so that successive rows of nodes going down the page would correspond, at least roughly, to events occurring at successively later times.

As the numbering in pictures (e) through (g) illustrates, there is no direct correspondence between this notion of time and the sequence of updating events that occur in the underlying evolution of the mobile automaton. For the point is that an observer who is part of the mobile automaton will never see all the individual steps in this evolution. The most they will be able to tell is that a certain network of causal relationships exists—and their perception of time must therefore derive purely from the properties of this network.

So does the notion of time that emerges actually have the familiar features of time as we know it? One might think for example that in a network there could be loops that would lead to a deviation from the linear progression of time that we appear to experience. But in fact, with a causal network constructed from an underlying evolution process in the way we have done it here no such loops can ever occur.

So what about traces of the sequential character of evolution in the original mobile automaton? One might imagine that with only a single active cell being updated at each step different parts of the system would inevitably be perceived to progress through time one after another. But what the pictures on page 489 demonstrate is that this need not be the case. Indeed, in the networks shown there all the nodes on each row are in effect connected in parallel to the nodes on the row below. So even though the underlying rules for the mobile automaton involve no global synchronization, it is nevertheless possible for an observer inside the mobile automaton to perceive time as progressing in a synchronized way.

Later in this chapter I will discuss how space works in the context of causal networks—and how ideas of relativity theory emerge. But for now one can just think of networks like those on page 489 as being laid out so that time goes down the page and space goes across. And one can then see that if one follows connections in the network, one is always forced to go progressively down the page, even though one is able to move both backwards and forwards across the page—thus agreeing with our everyday experience of being able to move in more or less any direction in space, but always being forced to move onward in time.

So what happens with other mobile automata?

The pictures on the next two pages show a few examples.

Rules (a) and (b) yield very simple repetitive networks in which there is in effect a notion of time but not of space. The underlying way any mobile automaton works forces time to continue forever. But with rules (a) and (b) only a limited number of points in space can ever be reached.

The other rules shown do not, however, suffer from this problem: in all of them progressively more points are reached in space as time goes on. Rules (c) and (d) yield networks that can be laid out in a quite

![](Images/_page_507_Figure_1.jpeg)

Examples of mobile automata from Chapter 3 and the causal networks they generate. In each case the picture on the left is essentially the standard representation of mobile automaton evolution used in Chapter 3. The pictures on the right are then causal network representations of the same evolution. The networks are laid out in analogy to the space networks on page 479, with nodes being placed on successive rows if they take progressively more connections to reach from the top node.

![](Images/_page_508_Figure_2.jpeg)

Note that a single connection can join events that occur at very different steps in the evolution of the underlying mobile automaton. And indeed to construct even a small part of the causal network can require an arbitrarily long computation in the underlying mobile automaton. Thus for example to make the causal networks in pictures (e), (f) and (g) requires looking respectively at 2447, 731 and 322 steps of mobile automaton evolution. And indeed in some cases there can be connections that are in effect never resolved. And thus for example in picture (a) there are downward connections that never reach any other node—reflecting the presence of positions on the left in the mobile automata evolution to which the active cell never returns.

![](Images/_page_508_Figure_4.jpeg)

regular manner. But with rules (e), (f) and (g) the networks are more complicated, and begin to seem somewhat random.

The procedure that is used to lay out the networks on the previous two pages is a direct analog of the procedure used for space networks on page 479: the row in which a particular node will be placed is determined by the minimum number of connections that have to be followed in order to reach that node starting from the node at the top.

In cases (a) and (c) the networks obtained in this way have the property that all connections between nodes go either across or down the page. But in every other case shown, at least some connections also go up the page. So what does this mean for our notion of time? As mentioned earlier, there can never be a loop in any causal network that comes from an evolution process. But if one identifies time with position down the page, the presence of connections that go up as well as down the page implies that in some sense time does not always progress in the same direction. Yet at least in the cases shown here there is still a strong average flow down the page—agreeing with our everyday perception that time progresses only in one direction.

Like in so many other systems that we have studied in this book, the randomness that we find in causal networks will inevitably tend to wash out details of how the networks are constructed. And thus, for example, even though the underlying rules for a mobile automaton always treat space and time very differently, the causal networks that emerge nevertheless often exhibit a kind of uniform randomness in which space and time somehow work in many respects the same.

But despite this uniformity at the level of causal networks, the transformation from mobile automaton evolution to causal network is often far from uniform. And for example the pictures at the top of the facing page show the causal networks for rules (e) and (f) from the previous page—but now with each node numbered to specify the step of mobile automaton evolution from which it was derived.

And what we see is that even nodes that are close to the top of the causal network can correspond to events which occur after a large number of steps of mobile automaton evolution. Indeed, to fill in just twenty rows

![](Images/_page_510_Picture_1.jpeg)

Causal networks corresponding to rules (e) and (f) from page 493, with each node explicitly labelled to specify from which step of mobile automaton evolution it is derived. Even to fill in the first few rows of such causal networks, many steps of underlying mobile automaton evolution must be traced.

of the causal networks for rules (e) and (f) requires following the underlying mobile automaton evolution for 2447 and 731 steps respectively.

One feature of causal networks is that they tell one not only what the consequences of a particular event will be, but also in a sense what its causes were. Thus, for example, if one starts, say, with event 17 in the first causal network above, then to find out that its causes were events 11 and 16 one simply has to trace backwards along the connections which lead to it.

With the specific type of underlying mobile automaton used here, every node has exactly three incoming and three outgoing connections. And at least when there is overall apparent randomness, the networks that one gets by going forwards and backwards from a particular node will look very similar. In most cases there will still be small differences; but the causal network on the right above is specifically constructed to be exactly reversible—much like the cellular automata we discussed near the beginning of this chapter.

Looking at the causal networks we have seen so far, one may wonder to what extent their form depends on the particular properties of the underlying mobile automata that were used to produce them.

For example, one might think that the fact that all the networks we have seen so far grow at most linearly with time must be an inevitable consequence of the one-dimensional character of the mobile automaton rules we have used. But the picture below demonstrates that even with such one-dimensional rules, it is actually possible to get causal networks that grow more rapidly. And in fact in the case shown below there are roughly a factor 1.22 more nodes on each successive row—corresponding to overall approximate exponential growth.

![](Images/_page_511_Picture_3.jpeg)

A one-dimensional mobile automaton which yields a causal network that in effect grows exponentially with time. The underlying mobile automaton acts like a binary counter, yielding a pattern whose width grows logarithmically with the number of steps. The three cases not shown in the rule are never used with the initial conditions given here.

The causal network for a system is always in some sense dual to the underlying evolution of the system. And in the case shown here the slow growth of the region visited by the active cell in the underlying evolution is reflected in rapid growth of the corresponding causal network.

As we will see later in this chapter there are in the end some limitations on the kinds of causal networks that one-dimensional mobile automata and systems like them can produce. But with different mobile automaton rules one can still already get tremendous diversity.

And even though when viewed from outside, systems like mobile automata might seem to have almost none of the familiar features of our universe, what we see is that if we as observers are in a sense part of such systems then immediately some major features quite similar to those of our universe can emerge.

#### The Sequencing of Events in the Universe

In the last section I discussed one type of model in which familiar notions of time can emerge without any kind of built-in global clock. The particular models I used were based on mobile automata—in which the presence of a single active cell forces only one event ever to occur in the universe at once. But as we will see in this section, there is actually no need for the setup to be so rigid, or indeed for there to be any kind of construct like an active cell.

One can think of mobile automata as being special cases of substitution systems of the type I introduced in Chapter 3. Such systems in general take a string of elements and at each step replace blocks of these elements with other elements according to some definite rule.

The picture below shows an example of one such system, and illustrates how—just like in a mobile automaton—relations between updating events can be represented by a causal network.

![](Images/_page_512_Figure_5.jpeg)

![](Images/_page_513_Figure_1.jpeg)

Examples of sequential substitution systems of the type discussed on page 88, and the causal networks that emerge from them. In a sequential substitution system only the first replacement that is found to apply in a left-to-right scan is ever performed at any step. Rule (a) above yields a causal network that is purely repetitive and thus yields no meaningful notion of space. Rules (b), (c) and (d) yield causal networks that in effect grow roughly linearly with time. In rule (f) the causal network grows exponentially, while in rule (e) the causal network also grows quite rapidly, though its overall growth properties are not clear. Note that to obtain the 10 levels shown here in the causal network for rule (e), it was necessary to follow the evolution of the underlying substitution system for a total of 258 steps.

Substitution systems that correspond to mobile automata can be thought of as having rules and initial conditions that are specially set up so that only one updating event can ever occur on any particular step. But with most rules—including the one shown on the previous page—there are usually several possible replacements that can be made at each step.

One scheme for deciding which replacement to make is just to scan the string from left to right and then pick the first replacement that applies. This scheme corresponds exactly to the sequential substitution systems we discussed in Chapter 3.

The pictures on the facing page show a few examples of what can happen. The behavior one gets is often fairly simple, but in some cases it can end up being highly complex. And just as in mobile automata, the causal networks that emerge typically in effect grow linearly with time. But, again as in mobile automata, there are rules such as (a) in which there is no growth—and effectively no notion of space. And there are also rules such as (f)—which turn out to be much more common in general substitution systems than in mobile automata—in which the causal network in effect grows exponentially with time.

But why do only one replacement at each step? The pictures on the next page show what happens if one again scans from left to right, but now one performs all replacements that fit, rather than just the first one.

In the case of rules (a) and (b) the result is to update every single element at every step. But since the replacements in these particular rules involve only one element at a time, one in effect has a neighbor-independent substitution system of the kind we discussed on page 82. And as we discovered there, such systems can only ever produce rather simple behavior: each element repeatedly branches into several others, yielding a causal network that has the form of a regular tree.

So what happens with replacements that involve more than just one element? In many cases, the behavior is still quite simple. But as several of the pictures on the next page demonstrate, fairly simple rules are sufficient—as in so many other systems that we have discussed in this book—to obtain highly complex behavior.

![](Images/_page_515_Figure_1.jpeg)

Examples of general substitution systems and the causal networks that emerge from them. In the pictures shown here, every replacement that is found to fit in a left-to-right scan is performed at each step. Rules (a) and (b) act like neighbor-independent substitution systems of the type discussed on page 84, and yield exponentially growing tree-like causal networks. The plots at the bottom show the growth rates of the patterns produced by rules (f) and (g). In the case of rule (f) the pattern turns out to be repetitive, with a period of 796 steps.

One may wonder, however, to what extent the behavior one sees depends on the exact scheme that one uses to pick which replacements to apply at each step. The answer is that for the vast majority of rules including rules (c) through (g) in the picture on the facing page—using different schemes yields quite different behavior—and a quite different causal network.

But remarkably enough there do exist rules for which exactly the same causal network is obtained regardless of what scheme is used. And as it turns out, rules (a) and (b) from the picture on the facing page provide simple examples of this phenomenon, as illustrated in the pictures below.

![](Images/_page_516_Figure_4.jpeg)

The behavior of rules (a) and (b) from the facing page when replacements are performed at random. Even though the detailed patterns obtained are different, the causal networks in these particular rules that represent relationships between replacement events are always exactly the same.

For each rule, the three different pictures shown above correspond to three different ways that replacements can be made. And while the positions of particular updating events are different in every picture, the point is that the network of causal connections between these events is always exactly the same.

This is certainly not true for every substitution system. Indeed, the pictures on the right show how it can fail, for example, for rule (e) from the facing page. What one sees in these pictures is that after event 4, different choices of replacements are made in the two cases, and the causal relationships implied by these replacements are different.

So what could ensure that no such situation would ever arise in a particular substitution system? Essentially what needs to be true is that the sequence of elements alone must always uniquely determine what replacements can be made in every part of the system. One still has a

![](Images/_page_516_Picture_9.jpeg)

Examples of two different ways of performing replacements in rule (e) from the facing page, yielding two different causal networks.

choice of whether actually to perform a given replacement at a particular step, or whether to delay that replacement until a subsequent step. But what must be true is that there can never be any ambiguity about what replacement will eventually be made in any given part of the system.

In rules like the ones at the top of page 500 where each replacement involves just a single element this is inevitably how things must work. But what about rules that have replacements involving blocks of more than one element? Can such rules still have the necessary properties?

The pictures below show two examples of rules that do. In the first picture for each rule, replacements are made at randomly chosen steps, while in the second picture, they are in a sense always made at the earliest possible step. But the point is that in no case is there any ambiguity about what replacement will eventually be made at any particular place in the system. And as a result, the causal network that represents the relationships between different updating events is always exactly the same.

![](Images/_page_517_Picture_4.jpeg)

![](Images/_page_517_Picture_5.jpeg)

![](Images/_page_517_Picture_6.jpeg)

![](Images/_page_517_Picture_7.jpeg)

![](Images/_page_517_Picture_8.jpeg)

![](Images/_page_517_Picture_9.jpeg)

Examples of substitution systems in which the same causal networks are obtained regardless of the way in which replacements are performed. In the first picture for each rule, the replacements are performed essentially at random. In the second picture they are performed on the earliest possible step. Note that rule (a) effectively sorts the elements in its initial conditions, always placing black before white.

So what underlying property must the rules for a substitution system have in order to make the system as a whole operate in this way? The basic answer is that somehow different replacements must never be able to interfere with each other. And one way to guarantee this is if the blocks involved in replacements can never overlap.

In both the rules shown on the facing page, the only replacement specified is for a particular block. And it is inevitably the case that in any sequence generated by these rules, different instances of this block do not overlap. If one had replacements for other kinds of blocks, then these could overlap. But there is an infinite sequence of blocks for which no overlap is possible, and thus for which different replacements can never interfere.

If a rule involves replacements for several distinct blocks, then to avoid the possibility of interference one must require that these blocks can never overlap either themselves or each other. There are simple non-trivial pairs and triples of blocks that have this property, and any such set is guaranteed to yield the same causal network regardless of the order in which replacements are performed.

In general the condition is in fact somewhat weaker. For it is not necessary that no overlaps exist at all in the replacements—only that no overlaps occur in whatever sequences of elements can actually be generated by the evolution of the substitution systems.

And in the end there are then all sorts of substitution systems which have the property that the causal networks they generate are always independent of the order in which their rules are applied.

So what does this mean for models of the universe?

In a system like a cellular automaton, the same underlying rule is in a sense always applied in exact synchrony to every cell at every step. But what we have seen in this section is that there also exist systems in which rules can in effect be applied whenever and wherever one wants—but the same definite causal network always emerges.

So what this means is that there is no need for any built-in global clock, or even for any mechanism like an active cell. Simply by choosing the appropriate underlying rules it is possible to ensure that any sequence of events consistent with these rules will yield the same causal network and thus in effect the same perceived history for the universe.

#### Uniqueness and Branching in Time

If our universe has no built-in global clock and no construct like an active cell, then it is almost inevitable that at the lowest level there will be at least some arbitrariness in how its rules can be applied.

Yet in the previous section we discovered the rather remarkable fact that there exist rules with the property that essentially regardless of how they are applied, the same causal network—and thus the same perceived history for the universe—will always emerge.

But must it in the end actually be true that the underlying rules for our universe force there to be a unique perceived history? Near the end of Chapter 5 I introduced multiway systems as examples of systems that allow multiple histories. And it turns out that multiway systems are actually extremely similar in basic structure to the substitution systems that I discussed in the previous section.

Both types of systems perform the same type of replacements on strings of elements. But while in a substitution system one always carries out just a single set of replacements at each step, getting a single new string, in a multiway system one instead carries out every possible replacement, thereby typically generating many new strings.

The picture below shows a simple example of how this works. On the first step in this particular picture, there happens to be only one replacement that can be performed consistent with the rules, so only a single string is produced. But on subsequent steps several different replacements are possible, so several strings are produced. And in general every path through a picture like this corresponds to a possible history that exists in the evolution of the multiway system.

A simple example of a multiway system in which replacements are applied in all possible ways to each string at each step.

![](Images/_page_519_Picture_8.jpeg)

So is it conceivable that the ultimate model for our universe could be based on a multiway system? At first one might not think so. For our everyday impression is that our universe has just one definite history, not some kind of whole collection of different histories. And assuming that one is able to look at a multiway system from the outside, one will immediately see that different paths exist corresponding to different histories.

But the crucial point is that if the complete state of our universe is in effect like a single string in a multiway system, then there is no way for us ever to look at the multiway system from the outside. And as entities inside the multiway system, our perception will inevitably be that just a single path was followed, corresponding to a single history.

If one were able to look at the multiway system from the outside, this path would seem quite arbitrary. But for us inside the multiway system it is the unique path that represents the thread of experience we have had.

Up until a few centuries ago, it was widely believed that the Earth had some kind of fundamentally unique position in space. But gradually it became clear that this was not so, and that in a sense it was merely our own presence that made our particular location in space seem in any way unique. Yet for time the belief still exists that we—and our universe—somehow have a unique history. But if in fact our universe is part of a multiway system, then this will not be true. And indeed the only thing that will be unique about the particular history that our universe has had will be that it is the one we have experienced.

At a purely human level I find it rather disappointing to think that essentially none of the details of our existence are in any way unique, and that there might be other paths in the multiway system on which everything would be different. And scientifically it is also unsatisfying to have to say that there are features of our universe which are not determined by any finite set of underlying rules, but are instead in a sense just pure accidents of history associated with the particular path that we have happened to follow in a multiway system.

In the early parts of Chapter 7 we discussed various possible origins for the apparent randomness that we see in many natural systems. And if the universe is described by a multiway system, then there will be an additional source of randomness: the arbitrariness of the path corresponding to the history that we have experienced.

In many respects this randomness is similar to the randomness from the environment that we discussed at the beginning of Chapter 7. But an important difference is that it would occur even if one could in effect perfectly isolate a system from the rest of the universe. If in the past one had seen apparent randomness in such a system there might have seemed to be no choice but to assume something like an underlying multiway system. But one of the discoveries of this book is that it is actually quite possible to generate what appears to be almost perfect randomness just by following definite underlying rules.

And indeed I would not expect that observations of randomness could ever reasonably be used to show that our universe is part of a multiway system. And in fact my guess is that the only way to show this with any certainty would be actually to find a specific set of multiway system rules with the property that regardless of the path that gets followed these rules would always yield behavior that agrees with the various observed features of our universe.

At some level it might seem surprising that a multiway system could ever consistently exhibit any particular form of behavior. For one might imagine that with so many different paths to choose from it would often be the case that almost any behavior would be able to occur on some path or another. And indeed, as the picture on the left shows, it is not difficult to construct multiway systems in which all possible strings of a particular kind are produced.

But if one looks not just at individual strings but rather at the sequences of strings that exist along paths in the multiway system, then one finds that these can no longer be so arbitrary. And indeed, in any multiway system with a limited set of rules, such sequences must necessarily be subject to all sorts of constraints.

In general, each path in a multiway system can be thought of as being defined by a possible sequence of ways in which the replacements specified by a multiway system rule can be applied. And each such path in turn then defines a causal network of the kind we discussed in the previous section. But as we saw there, certain underlying rules have the

![](Images/_page_521_Figure_7.jpeg)

A multiway system in which strings of any length can be generated—but in which only specific sequences of lengths actually occur on any path.

property that the form of this causal network ends up being the same regardless of the order in which replacements are applied—and thus regardless of the path that is followed in the multiway system.

The pictures below show some simple examples of rules with this property. And as it turns out, it is fairly easy to recognize the presence of the property from the overall pattern of multiway system paths that occur.

![](Images/_page_522_Picture_4.jpeg)

![](Images/_page_522_Picture_5.jpeg)

Examples of multiway systems in which the causal network associated with every path is exactly the same. All such multiway systems have the property that every pair of paths which diverge at a particular step can converge again on the following step. The first rule shown has the effect of sorting the elements in the string.

![](Images/_page_522_Picture_7.jpeg)

![](Images/_page_522_Picture_8.jpeg)

If one starts from a given initial string, then typically one will generate different strings by applying different replacements. But if one is going to get the same causal network, then it must always be the case that there are replacements one can apply to the strings one has generated that yield the same final string. So what this means is that any pair of paths in the multiway system that diverge must be able to converge again within just one step—so that all the arrows in pictures like the ones above must lie on the edges of quadrilaterals.

Most multiway systems, however, do not have exactly this property, and as a result the causal networks that are obtained by following different paths in them will not be absolutely identical. But it still turns out that whenever paths can always eventually converge—even if not in a fixed number of steps—there will necessarily be similarities on a sufficiently large scale in the causal networks that are obtained.

At the level of individual events, the structure of the causal networks will typically vary greatly. But if one looks at large enough collections of events, these details will tend to be washed out, and

regardless of the path one chooses, the overall form of causal network will be essentially the same. And what this means is that on a sufficiently large scale, the universe will appear to have a unique history, even though at the level of individual events there will be considerable arbitrariness.

If there is not enough convergence in the multiway system it will still be possible to get stuck with different types of strings that never lead to each other. And if this happens, then it means that the history of the universe can in effect follow many truly separate branches. But whenever there is significant randomness produced by the evolution of the multiway system, this does not typically appear to occur.

So this suggests that in fact it is at some level not too difficult for multiway systems to reproduce our everyday perception that more or less definite things happen in the universe. But while this means that it might be possible for there to be arbitrariness in the causal network for the universe, it still tends to be my suspicion that there is not—and that in fact the particular rules followed by the universe do in the end have the property that they always yield the same causal network.

#### Evolution of Networks

Earlier in this chapter, I suggested that at the lowest level space might consist of a giant network of nodes. But how might such a network evolve?

The most straightforward possibility is that it could work much like the substitution systems that we have discussed in the past few sections—and that at each step some piece or pieces of the network could be replaced by others according to some fixed rule.

The pictures at the top of the facing page show two very simple examples. Starting with a network whose connections are like the edges of a tetrahedron, both the rules shown work by replacing each node at each step by a certain fixed cluster of nodes.

This setup is very much similar to the neighbor-independent substitution systems that we discussed on pages 83 and 187. And just as in these systems, it is possible for intricate structures to be produced, but the structures always turn out to have a highly regular nested form.

![](Images/_page_524_Picture_1.jpeg)

Network evolution in which each node is replaced at each step by a fixed cluster of nodes. The resulting networks have a regular nested form. The dimensions of the limiting networks are respectively  $Log[2, 3] \approx 1.58$  and  $Log[3, 7] \approx 1.77$ .

So what about more general substitution systems? Are there analogs of these for networks? The answer is that there are, and they are based on making replacements not just for individual nodes, but rather for clusters of nodes, as shown in the pictures below.

![](Images/_page_524_Picture_4.jpeg)

Examples of rules that involve replacing clusters of nodes in a network by other clusters of nodes. All these rules preserve the planarity of a network. Notice that some of them cannot be reversed since their right-hand sides are too symmetrical to determine which orientation of the left-hand side should be used.

In the substitution systems for strings discussed in previous sections, the rules that are given can involve replacing any block of elements by any other. But in networks there are inevitably some restrictions. For example, if a cluster of nodes has a certain number of connections to the rest of the network, then it cannot be replaced by a cluster which has a different number of connections. And in addition, one cannot have replacements

![](Images/_page_525_Picture_1.jpeg)

A replacement whose outcome orientation cannot be determined.

like the one on the left that go from a symmetrical cluster to one for which a particular orientation has to be chosen.

But despite these restrictions a fairly large number of replacements are still possible; for example, there are a total of 419 distinct ones that exist involving clusters with no more than five nodes.

So given a replacement for a cluster of a particular form, how should such a replacement actually be applied to a network? At first one might think that one could set up some kind of analog of a cellular automaton and just replace all relevant clusters of nodes at once.

But in general this will not work. For as the picture below illustrates, a particular form of cluster can in general appear in many overlapping ways within a given network.

![](Images/_page_525_Picture_7.jpeg)

![](Images/_page_525_Picture_8.jpeg)

The 12 ways in which the cluster of nodes on the left occurs in a particular network. In the particular case shown, each way turns out to overlap with nodes in exactly four others.

The issue is essentially no different from the one that we encountered in previous sections for blocks of elements in substitution systems on strings. But an additional complication is that in networks, unlike strings, there is no immediately obvious ordering of elements.

Nevertheless, it is still possible to devise schemes for deciding where in a network replacements should be carried out. One fairly simple scheme, illustrated on the facing page, allows only a single replacement to be performed at each step, and picks the location of this replacement so as to affect the least recently updated nodes.

In each pair of pictures in the upper part of the page, the top one shows the form of the network before the replacement, and the bottom one shows the result after doing the replacement—with the cluster of nodes involved in the replacement being highlighted in both cases. In the 3D pictures in the lower part of the page, networks that arise on successive steps are shown stacked one on top of the other, with the nodes involved in each replacement joined by gray lines.

![](Images/_page_526_Picture_2.jpeg)

Examples of the evolution of networks in which a single cluster of nodes is replaced at each step according to the rules shown. Each pair of pictures above represents the state of the network before and after each replacement. The nodes affected by the replacement are highlighted in both cases. The location at which the replacement is performed is determined by requiring that it involve the oldest possible nodes in the network. The nodes in the pictures above are drawn with a "clock". The angle of the beginning of the black sector in the clock indicates when the node was created, while the angle of its end represents the current step, so that older nodes have larger black sectors.

Inevitably there is a certain arbitrariness in the way these pictures are drawn. For the underlying rules specify only what the pattern of connections in a network should be—not how its nodes should be laid out on the page. And in the effort to make clear the relationship between networks obtained on different steps, even identical networks can potentially be drawn somewhat differently.

With rule (a), however, it is fairly easy to see that a simple nested structure is produced, directly analogous to the one shown on page 509. And with rule (b), obvious repetitive behavior is obtained.

So what about more complicated behavior? It turns out that even with rule (c), which is essentially just a combination of rules (a) and (b), significantly more complicated behavior can already occur.

The picture below shows a few more steps in the evolution of this rule. And the behavior obtained never seems to repeat, nor do the networks produced exhibit any kind of obvious nested form.

![](Images/_page_527_Picture_5.jpeg)

More steps in the evolution of rule (c) from the previous page. The number of nodes increases irregularly (though roughly linearly) with successive steps.

What about other schemes for applying replacements? The pictures on the facing page show what happens if at each step one allows not just a single replacement, but all replacements that do not overlap.

It takes fewer steps for networks to be built up, but the results are qualitatively similar to those on the previous page: rule (a) yields a nested structure, rule (b) gives repetitive behavior, while rule (c) produces behavior that seems complicated and in some respects random.

![](Images/_page_528_Figure_1.jpeg)

Just as for substitution systems on strings, one can find causal networks that represent the causal connections between different updating events on networks. And as an example the pictures below show such causal networks for the evolution processes on the previous page.

![](Images/_page_529_Picture_2.jpeg)

![](Images/_page_529_Picture_3.jpeg)

Causal networks that represent the relationship between updating events for the network evolution processes shown on the previous page.

In the rather simple case of rule (a) the results turn out to be independent of the updating scheme that was used. But for rules (b) and (c), different schemes in general yield different causal networks.

So what kinds of underlying replacement rules lead to causal networks that are independent of how the rules are applied? The situation is much the same as for strings—with the basic criterion just being that all replacements that appear in the rules should be for clusters of nodes that can never overlap themselves or each other.

The pictures below show all possible distinct clusters with up to five nodes—and all but three of these already can overlap themselves.

![](Images/_page_529_Picture_8.jpeg)

All possible distinct clusters containing up to five nodes, with planarity not required.

But among slightly larger clusters there turn out to be many that do not overlap themselves—and indeed this becomes common as soon as there are at least two connections between each dangling one.

The first few examples are shown below. And in almost all of these, there is no overlap not only within a single cluster, but also between different clusters. And this means that rules based on replacements for collections of these clusters will have the property that the causal networks they produce are independent of the updating scheme used.

![](Images/_page_530_Picture_3.jpeg)

The simplest clusters that have no overlaps with themselves—and mostly have no overlaps with each other. Replacements for sets of clusters that do not overlap have the property of causal invariance.

One feature of the various rules I showed earlier is that they all maintain planarity of networks—so that if one starts with a network that can be laid out in the plane without any lines crossing, then every subsequent network one gets will also have this property.

Yet in our everyday experience space certainly does not seem to have this property. But beyond the practical problem of displaying what happens, there is actually no fundamental difficulty in setting up rules that can generate non-planarity—and indeed many rules based on the clusters above will for example do this.

So in the end, if one manages to find the ultimate rules for the universe, my expectation is that they will give rise to networks that on a small scale look largely random. But this very randomness will most likely be what for example allows a definite and robust value of 3 to emerge for the dimensionality of space—even though all of the many complicated phenomena in our universe must also somehow be represented within the structure of the same network.

#### Space, Time and Relativity

Several sections ago I argued that as observers within the universe everything we can observe must at some level be associated purely with the network of causal connections between events in the universe. And in the past few sections I have outlined a series of types of models for how such a causal network might actually get built up.

But how do the properties of causal networks relate to our normal notions of space and time? There turn out to be some slight subtleties—but these seem to be exactly what end up yielding the theory of relativity.

As we saw in earlier sections, if one has an explicit evolution history for a system it is straightforward to deduce a causal network from it. But given only a causal network, what can one say about the evolution history?

The picture below shows an example of how successive steps in a particular evolution history can be recovered from a particular set of slices through the causal network derived from it. But what if one were to choose a different set of slices? In general, the sequence of strings that one would get would not correspond to anything that could arise from the same underlying substitution system.

![](Images/_page_531_Picture_6.jpeg)

An example of how the succession of states in an evolution history can be recovered by taking appropriate slices through a causal network. Any consistent choice of such slices will correspond to a possible evolution history—with the same underlying rules, but potentially a different scheme for determining the order in which to apply replacements.

But if one has a system that yields the same causal network independent of the scheme used to apply its underlying rules, then the situation is different. And in this case any slice that consistently divides the causal network into a past and a future must correspond to a possible state of the underlying system—and any non-overlapping sequence of such slices must represent a possible evolution history for the system.

If we could explicitly see the particular underlying evolution history for the system that corresponds to our universe then this would in a sense immediately provide absolute information about space and time in the universe. But if we can observe only the causal network for the universe then our information about space and time must inevitably be deduced indirectly from looking at slices of causal networks.

And indeed only some causal networks even yield a reasonable notion of space at all. For one can think of successive slices through a causal network as corresponding to states at successive moments in time. But for there to be something one can reasonably think of as space one has to be able to identify some background features that stay more or less the same—which means that the causal network must yield consistent similarities between states it generates at successive moments in time.

One might have thought that if one just had an underlying system which did not change on successive steps then this would immediately yield a fixed structure for space. But in fact, without updating events, no causal network at all gets built up. And so a system like the one at the top of the next page is about the simplest that can yield something even vaguely reminiscent of ordinary space.

In practice I certainly do not expect that even parts of our universe where nothing much seems to be going on will actually have causal networks as simple as at the top of the next page. And in fact, as I mentioned at the end of the previous section, what I expect instead is that there will always tend to be all sorts of complicated and seemingly random behavior at small scales—though at larger scales this will typically get washed out to yield the kind of consistent average properties that we ordinarily associate with space.

![](Images/_page_533_Picture_1.jpeg)

![](Images/_page_533_Picture_2.jpeg)

![](Images/_page_533_Picture_3.jpeg)

![](Images/_page_533_Picture_4.jpeg)

A very simple substitution system whose causal network has slices that can be thought of as corresponding to a highly regular idealization of one-dimensional ordinary space. The rule effectively just sorts elements so that black ones come first, and yields the same causal network regardless of what updating scheme is used.

One of the defining features of space as we normally experience it is a certain locality that leads most things that happen at some particular position to be able at first to affect only things very near them.

Such locality is built into the basic structure of systems like cellular automata. For in such systems the underlying rules allow the color of a particular cell to affect only its immediate neighbors at each step. And this has the consequence that effects in such systems can spread only at a limited rate, as manifest for example in a maximum slope for the edges of patterns like those in the pictures below.

![](Images/_page_533_Picture_8.jpeg)

![](Images/_page_533_Picture_9.jpeg)

![](Images/_page_533_Picture_10.jpeg)

![](Images/_page_533_Picture_11.jpeg)

Examples of patterns produced by cellular automata, illustrating the fact discussed in Chapter 6 that the edge of each pattern has a maximum slope equal to one cell per step, corresponding to an absolute upper limit on the rate of information transmission—similar to the speed of light in physics.

In physics there also seems to be a maximum speed at which the effects of any event can spread: the speed of light, equal to about 300

million meters per second. And it is common in spacetime physics to draw "light cones" of the kind shown at the right to indicate the region that will be reached by a light signal emitted from a particular position in space at a particular time. So what is the analog of this in a causal network?

The answer is straightforward, for the very definition of a causal network shows that to see how the effects of a particular event spread one just has to follow the successive connections from it in the causal network.

But in the abstract there is no reason that these connections should lead to points that can in any way be viewed as nearby in space. Among the various kinds of underlying systems that I have studied in this book many have no particular locality in their basic rules. But the particular kinds of systems I have discussed for both strings and networks in the past few sections do have a certain locality, in that each individual replacement they make involves only a few nearby elements.

One might choose to consider systems like these just because it seems easier to specify their rules. But their locality also seems important in giving rise to anything that one can reasonably recognize as space.

For without it there will tend to be no particular way to match up corresponding parts in successive slices through the causal networks that are produced. And as a result there will not be the consistency between successive slices necessary to have a stable notion of space.

In the case of substitution systems for strings, locality of underlying replacement rules immediately implies overall locality of effects in the system. For the different elements in the system are always just laid out in a one-dimensional string, with the result that local replacement rules can only ever propagate effects to nearby elements in the string—much like in a one-dimensional cellular automaton.

If one is dealing with an underlying system based on networks, however, then the situation can be somewhat more complicated. For as we discussed several sections ago—and will discuss again in the final sections of this chapter—there will typically be only an approximate correspondence between the structure of the network and the structure of ordinary space. And so for example—as we will discuss later in connection with quantum phenomena—there may sometimes be a kind of thread that connects parts of the network that would not

![](Images/_page_534_Picture_9.jpeg)

Schematic illustration of a light cone in physics. Light emitted at a point in space will normally spread out with time into a cone, whose cross-section is shown schematically here.

normally be considered nearby in three-dimensional space. And so when clusters of nodes that are nearby with respect to connections on the network get updated, they can potentially propagate effects to what might be considered distant points in space.

Nevertheless, if a network is going to correspond to space as it seems to exist in our universe, such phenomena must not be too important—and in the end there must to a good approximation be the kind of straightforward locality that exists for example in the simple causal network of page 518.

In the next section I will discuss how actual physical entities like particles propagate in systems represented by causal networks. But ultimately the whole point of causal networks is that their connections represent all possible ways that effects propagate. Yet these connections are also what end up defining our notions of space and time in a system. And particularly in a causal network as regular as the one on page 518 one can then immediately view each connection in the causal network as corresponding to an effect propagating a certain distance in space during a certain interval in time.

So what about a more complicated causal network? One might imagine that its connections could perhaps represent varying distances in space and varying intervals in time. But there is no independent way to work out distance in space or interval in time beyond looking at the connections in the causal network. So the only thing that ultimately makes sense is to measure space and time taking each connection in the causal network to correspond to an identical elementary distance in space and elementary interval in time.

One may guess that this elementary distance is around  $10^{-35}$  meters, and that the elementary time interval is around  $10^{-43}$  seconds. But whatever these values are, a crucial point is that their ratio must be a fixed speed, and we can identify this with the speed of light. So this means that in a sense every connection in a causal network can be viewed as representing the propagation of an effect at the speed of light.

And with this realization we are now close to being able to see how the kinds of systems I have discussed must almost inevitably succeed in reproducing the fundamental features of relativity theory. But first we must consider the concept of motion.

To say that one is not moving means that one imagines one is in a sense sampling the same region of space throughout time. But if one is moving—say at a fixed speed—then this means that one imagines that the region of space one is sampling systematically shifts with time, as illustrated schematically in the simple pictures on the right.

But as we have seen in discussing causal networks, it is in general quite arbitrary how one chooses to match up space at different times. And in fact one can just view different states of motion as corresponding to different such choices: in each case one matches up space so as to treat the point one is at as being the same throughout time.

Motion at a fixed speed is then the simplest case—and the one emphasized in the so-called special theory of relativity. And at least in the context of a highly regular causal network like the one in the picture on page 518 there is a simple interpretation to this: it just corresponds to looking at slices at different angles through the causal network.

Successive parallel slices through the causal network in general correspond to successive states of the underlying system at successive moments in time. But there is nothing that determines in any absolute way the overall angle of these slices in pictures like those on page 518. And the point is that in fact one can interpret slices at different angles as corresponding to motion at different fixed speeds.

If the angle is so great that there are connections going up as well as down between slices, then there will be a problem. But otherwise it will always be the case that regardless of angle, successive slices must correspond to possible evolution histories for the underlying system.

One might have thought that states obtained from slices at different angles would inevitably be consistent only with different sets of underlying rules. But in fact this is not the case, and instead the exact same rules can reproduce slices at all angles. And this is a consequence of the fact that the substitution system on page 518 has the property of causal invariance—so that it gives the same causal network independent of the scheme used to apply its underlying rules.

It is slightly more complicated to represent uniform motion in causal networks that are not as regular as the one on page 518. But

![](Images/_page_536_Picture_9.jpeg)

Graphical representation in space and time of motion at fixed speeds

whenever there is sufficient uniformity to give a stable structure to space one can still think of something like parallel slices at different angles as representing motion at different fixed speeds.

And the crucial point is that whenever the underlying system is causal invariant the exact same underlying rules will account for what one sees in slices at different angles. And what this means is that in effect the same rules will apply regardless of how fast one is going.

And the remarkable point is then that this is also what seems to happen in physics. For everyday experience—together with all sorts of detailed experiments—strongly support the idea that so long as there are no effects from acceleration or external forces, physical systems work exactly the same regardless of how fast they are moving.

At the outset it might not have seemed conceivable that any system which at some level just applies a fixed program to various underlying elements could successfully capture the phenomenon of motion. For certainly a system like a typical cellular automaton does not—since for example its effective rules for evolution at different angles will usually be quite different. But there are two crucial ideas that make motion work in the kinds of systems I am discussing here. First, that causal networks can represent everything that can be observed. And second, that with causal invariance different slices through a causal network can be produced by the same underlying rules.

Historically, the idea that physical processes should always be independent of overall motion goes back at least three hundred years. And from this idea one expects for example that light should always travel at its usual speed with respect to whatever emitted it. But what if one happens to be moving with respect to this emitter? Will the light then appear to be travelling at a different speed? In the case of sound it would. But what was discovered around the end of the 1800s is that in the case of light it does not. And it was essentially to explain this surprising fact that the special theory of relativity was developed.

In the past, however, there seemed to be no obvious underlying mechanism that could account for the validity of this basic theory. But now it turns out that the kinds of discrete causal network models that I have described almost inevitably end up being able to do this.

And essentially the reason for this is that—as I discussed above—each individual connection in any causal network must almost by definition represent propagation of effects at the speed of light. The overall structure of space that emerges may be complicated, and there may be objects that end up moving at all sorts of speeds. But at least locally the individual connections basically define the speed of light as a fixed maximum rate of propagation of any effect. And the point is that they do this regardless of how fast the source of an effect may be moving.

So from this one can use essentially standard arguments to derive all the various phenomena familiar from ordinary relativity theory. A typical example is time dilation, in which a fixed time interval for a system moving at some speed seems to correspond to a longer time interval for a system at rest. The picture on the next page shows schematically how this at first unexpected result arises.

The basic idea is to consider what happens when a system that can act as a simple clock moves at different speeds. At a traditional physics level one can think of the clock as having a photon of light bouncing backwards and forwards between mirrors a fixed distance apart. But more generally one can think of following criss-crossing connections that exist in some fixed fragment of a causal network.

In the picture on the next page time goes down the page. The internal mechanism of the clock is shown as a zig-zag black line—with each sweep of this line corresponding to the passage of one unit of time.

The black line is always assumed to be moving at the speed of light—so that it always lies on the surface of a light cone, as indicated in the top row of pictures. But then in successive pictures the whole clock is taken to move at increasing fractions of the speed of light.

The dark gray region in each picture represents a fixed amount of time for the clock—corresponding to a fixed number of sweeps of the black line. But as the pictures indicate, it is then essentially just a matter of geometry to see that this dark gray region will correspond to progressively larger amounts of time for a system at rest—in just the way predicted by the standard formula of relativistic time dilation.

![](Images/_page_539_Picture_2.jpeg)

A simple derivation of the classic phenomenon of relativistic time dilation. The pictures show the behavior of a very simple idealized clock going at different fractions of the speed of light. The clock can be thought of as consisting of a photon of light bouncing backwards and forwards between mirrors a fixed distance apart. (At a more general level in my approach it can also be thought of as a fragment of a causal network.) Time is shown going down the page, so that the photon in the clock traces out a zig-zag path. The fundamental assumption—that in my approach is just a consequence of basic properties of causal networks—is that the photon always goes at the speed of light, so that its path always lies on the surface of light cones like the ones in the top row of pictures. A fixed interval of time for the clock—as indicated by the length of the darker gray regions—corresponds to a progressively longer interval of time at rest. The amount of this time dilation is given by the classic relativistic formula  $1/\sqrt{1-v^2/c^2}$ , where v/c is the ratio of the speed of the clock to the speed of light. Such time dilation is routinely observed in particle accelerators—and has to be corrected for in GPS satellites. It leads to the so-called twin paradox in which less time will pass for a member of a twin going at high speed in a spacecraft than one staying at rest. The fact that time dilation is a general phenomenon not restricted to something like the simple clock shown relies in my approach on general properties of causal networks. Once the basic assumptions are established, the derivation of time dilation given here is no different in principle from the original one given in 1905, though I believe it is in many ways considerably clearer. Note that it is necessary to consider motion in two dimensions—so that the clock as a whole can be moving perpendicular to the path of the photon inside it. If these were parallel, one would inevitably get not just pure time dilation, but a mixture of it and length contraction.

#### Elementary Particles

There are some aspects of the universe—notably the structure of space and time—that present-day physics tends to assume are continuous. But over the past century it has at least become universally accepted that all matter is made up of identifiable discrete particles.

Experiments have found a fairly small number of fundamentally different kinds of particles, with electrons, photons, muons and the six basic types of quarks being a few examples. And it is one of the striking observed regularities of the universe that all particles of a given kind, say electrons, seem to be absolutely identical in their properties.

But what actually are particles? As far as present-day experiments can tell, electrons, for example, have zero size and no substructure. But particularly if space is discrete, it seems almost inevitable that electrons and other particles must be made up of more fundamental elements.

So how might this work? An immediate possibility that I suspect is actually not too far from the mark is that such particles are analogs of the localized structures that we saw earlier in this book in systems like the class 4 cellular automata shown on the right. And if this is so, then it means that at the lowest level, the rules for the universe need make no reference to particular particles. Instead, all the particles we see would just emerge as structures formed from more basic elements.

In networks it can be somewhat difficult to visualize localized structures. But the picture below nevertheless shows a simple example of how a localized structure can move across a regular planar network.

Both the examples on this page show structures that exist on very regular backgrounds. But to get any kind of realistic model for actual

![](Images/_page_540_Picture_9.jpeg)

Typical examples of particle-like localized structures in class 4 cellular automata.

![](Images/_page_540_Picture_11.jpeg)

![](Images/_page_540_Picture_12.jpeg)

A particle-like localized structure in a network.

particles in physics one must consider structures on much more complicated and random backgrounds. For any network that has a serious chance of representing actual space—even a supposedly empty part—will no doubt show all sorts of seemingly random activity. So any localized structure that might represent a particle will somehow have to persist even on this kind of random background.

Yet at first one might think that such randomness would inevitably disrupt any kind of definite persistent structure. But the pictures below show two simple examples where it does not. In the first case, there are localized cracks that persist. And in the second case, there are two different types of regions, separated by boundaries that act like localized structures with definite properties, and persist until they annihilate.

![](Images/_page_541_Picture_3.jpeg)

![](Images/_page_541_Picture_4.jpeg)

Examples of one-dimensional cellular automata that support various forms of persistent structures even on largely random backgrounds. These are 3-color totalistic rules with codes 294 and 1893.

So what about networks? It turns out that here again it is possible to get definite structures that persist even in the presence of randomness. And to see an example of this consider setting up rules like those on page 509 that preserve the planarity of networks.

Starting off with a network that is planar—so that it can be drawn flat on a page without any lines crossing—such rules can certainly give all sorts of complex and apparently random behavior. But the way the rules are set up, all the networks they produce must still be planar.

And if one starts off with a network like the one on the left that can only be drawn with lines crossing, then what will happen is that the non-planarity of the network will be preserved. But to what extent does this non-planarity correspond to a definite structure in the network?

![](Images/_page_541_Picture_9.jpeg)

A network with a single irreducible crossing of lines.

There are typically many different ways to draw a non-planar network, each with lines crossing in different places. But there is a fundamental result in graph theory that shows that if a network is not planar, then it must always be possible to identify in it a specific part that can be reduced to one of the two forms shown on the right—or just the second form for a network with three connections at each node.

So this implies that one can in fact meaningfully associate a definite structure with non-planarity. And while at some level the structure can be spread out in the network, the point is that it must always in effect have a localized core with the form shown on the right.

In general one can imagine having several pieces of non-planarity in a network—perhaps each pictured like a carrying handle. But if the underlying rules for the network preserve planarity then each of these pieces of non-planarity must on their own be persistent—and can in a sense only disappear through processes like annihilating with each other.

So might these be like actual particles in physics?

In the realistic case of network rules for the universe, planarity as such is presumably not preserved. But observations in physics suggest that there are several quantities like electric charge that are conserved. And ultimately the values of these quantities must reflect properties of underlying networks that are preserved by network evolution rules.

And if these rules satisfy the constraint of causal invariance that I discussed in previous sections, then I suspect that this means that they will inevitably exhibit various additional features—perhaps notably including for example what is usually known as local gauge invariance.

But what is most relevant here is that it seems likely that—much as for non-planarity—nonzero values of quantities conserved by network evolution rules can be thought of as being associated with some sort of local structures or tangles of connections in the network. And I suspect that it is essentially such structures that define the cores of the various types of elementary particles that are seen in physics.

Before the results of this book it might have seemed completely implausible that anything like this could be correct. For independent of any specific arguments about networks and their evolution, traditional intuition would tend to make one think that the elaborate properties of

![](Images/_page_542_Picture_10.jpeg)

![](Images/_page_542_Picture_11.jpeg)

The K<sub>5</sub> and K<sub>3,3</sub> forms that lead to non-planarity in networks.

![](Images/_page_542_Picture_13.jpeg)

How K<sub>3,3</sub> is embedded in the network from the facing page.

particles must inevitably be the result of an elaborate underlying setup. But what we have now seen over and over again in this book is that in fact it is perfectly possible to get phenomena of great complexity even with a remarkably simple underlying setup. And I suspect that particles in physics—with all their various properties and interactions—are just yet another example of this very general phenomenon.

One immediate thing that might seem to suggest that elementary particles must somehow be based on simple discrete structures is the fact that their values of quantities like electric charge always seem to be in simple rational ratios. In traditional particle physics this is explained by saying that many if not all particles are somehow just manifestations of the same underlying abstract object, related by a simple fixed group of symmetry operations. But in terms of networks one can imagine a much more explicit explanation: that there are just a simple discrete set of possible structures for the cores of particles—each perhaps related in some quite mechanical way by the group of symmetry operations.

But in addition to quantities like electric charge, another important intrinsic property of all particles is mass. And unlike for example electric charge the observed masses of elementary particles never seem to be in simple ratios—so that for example the muon is about 206.7683 times the mass of the electron, while the tau lepton is about 16.819 times the mass of the muon. But despite such results, it is still conceivable that there could in the end be simple relations between truly fundamental particle masses—since it turns out that the masses that have actually been observed in effect also include varying amounts of interaction energy.

A defining feature of any particle is that it can somehow move in space while maintaining its identity. In traditional physics, such motion has a straightforward mathematical representation, and it has not usually seemed meaningful to ask what might underlie it. But in the approach that I take here, motion is no longer such an intrinsic concept, and the motion of a particle must be thought of as a process that is made up of a whole sequence of explicit lower-level steps.

So at first, it might seem surprising that one can even set up a particular type of particle to move at different speeds. But from the discussion in the previous section it follows that this is actually an almost inevitable consequence of having underlying rules that show causal invariance. For assuming that around the particle there is some kind of uniformity in the causal network—and thus in the apparent structure of space—taking slices through the causal network at an appropriate angle will always make any particle appear to be at rest. And the point is that causal invariance then implies that the same underlying rules can be used to update the network in all such cases.

But what happens if one has two particles that are moving with different velocities? What will the events associated with the second particle look like if one takes slices through the causal network so that the first particle appears to be at rest? The answer is that the more the second particle moves between successive slices, the more updating events must be involved. For in effect any node that was associated with the particle on either one slice or the next must be updated—and the more the particle moves, the less these will overlap. And in addition, there will inevitably appear to be an asymmetry in the pattern of events relative to whatever direction the particle is moving.

There are many subtleties here, and indeed to explain the details of what is going on will no doubt require quite a few new and rather abstract concepts. But the general picture that I believe will emerge is that when particles move faster they will appear to have more nodes associated with them.

Most likely the intrinsic properties of a particle—like its electric charge—will be associated with some sort of core that corresponds to a definite network structure involving a roughly fixed number of nodes. But I suspect that the apparent motion of the particle will be associated with a kind of coat that somehow interpolates from the core to the uniform background of surrounding space. With different slices through the causal network, the apparent size of this coat can change. But I suspect that the size of the coat in a particular case will somehow be related to the apparent energy and momentum of a particle in that case.

An important fact in traditional physics is that interactions between particles seem to conserve total energy and momentum. And conceivably the reason for this is that such interactions somehow tend to preserve the total number of network nodes. Indeed, perhaps in most situations—save those associated with the overall expansion of the universe—the basic rules for the network at least on average just rearrange nodes and never change their number.

In traditional physics energy and momentum are always assumed to have continuous values. But just as in the case of position there is no contradiction with sufficiently small underlying discrete elements.

As I will discuss in the last section of this chapter, quantum mechanics tends to make one think of particles with higher momenta as being somehow progressively less spread out in space. So how can this be consistent with the idea that higher momentum is associated with having more nodes? Part of the answer probably has to do with the fact that outside the piece of the network that corresponds to the particle, the network presumably matches up to yield uniform space in much the same way as without the particle. And within the piece of the network corresponding to the particle, the effective structure of space may be very different—with for example more long-range connections added to reduce the effective overall distance.

#### The Phenomenon of Gravity

At an opposite extreme from elementary particles one can ask how the universe behaves on the largest possible scales. And the most obvious effect on such scales is the phenomenon of gravity. So how then might this emerge from the kinds of models I have discussed here?

The standard theory of gravity for nearly a century has been general relativity—which is based on the idea of associating gravity with curvature in space, then specifying how this curvature relates to the energy and momentum of whatever matter is present.

Something like a magnetic field in general has different effects on objects made of different materials. But a key observation verified experimentally to considerable accuracy is that gravity has exactly the same effect on the motion of different objects, regardless of what those objects are made of. And it is this that allows one to think of gravity as a general feature of space—rather than for example as some type of force that acts specifically on different objects.

In the absence of any gravity or forces, our normal definition of space implies that when an object moves from one point to another, it always goes along a straight line, which corresponds to the shortest path. But when gravity is present, objects in general move on curved paths. Yet these paths can still be the shortest—or so-called geodesics if one takes space to be curved. And indeed if space has appropriate curvature one can get all sorts of paths, as in the pictures below.

![](Images/_page_546_Picture_3.jpeg)

Examples of the effect of curvature in space on paths taken by objects. In each case all the paths shown start parallel, but do not remain so when there is curvature. The paths are geodesics which go the minimum distance on the surface to get to all the points they reach. (In general, the minimum may only be local.) Case (b) shows the top of a sphere, which is a surface of positive curvature. Case (c) shows the negatively curved surface  $z = x^2 - y^2$ , (d) a paraboloid  $z = x^2 + y^2$ , and (e,f)  $z = 1/(r + \delta)$  —a rough analog of curvature in space produced by a sphere of mass.

But in our actual universe what determines the curvature of space? The answer from general relativity is that the Einstein equations give conditions for the value of a particular kind of curvature in terms of the energy and momentum of matter that is present. And the point then is that the shortest paths in space with this curvature seem to be consistent with those followed by objects moving under the influence of gravity associated with the given distribution of matter.

For a continuous surface—or in general a continuous space—the idea of curvature is a familiar one in traditional geometry. But if the universe is at an underlying level just a discrete network of nodes then how does curvature work? At some level the answer is that on large scales the discrete network must approximate continuous space.

But it turns out that one can actually also recognize curvature in the basic structure of a network. If one has a simple array of hexagons—as in the picture on the left—then this can readily be laid out flat on a two-dimensional plane. But what if one replaces some of these hexagons by pentagons? One still has a fundamentally two-dimensional surface. But if one tries to keep all edges the same length the surface will inevitably become curved—like a soccer ball or a geodesic dome.

So what this suggests is that in a network just changing the pattern of connections can in effect change the overall curvature. And indeed the pictures below show a succession of networks that in effect have curvatures with a range of negative and positive values.

![](Images/_page_547_Picture_5.jpeg)

![](Images/_page_547_Picture_6.jpeg)

A hexagonal array corresponding to flat two-dimensional space.

![](Images/_page_547_Picture_8.jpeg)

Networks with various limiting curvatures. If every region in the network is in effect a hexagon—as in the picture at the top of the page—then the network will behave as if it is flat. But if pentagons are introduced, as in the cases on the left, the network will increasingly behave as if it has positive curvature—like part of a sphere. And if heptagons are introduced, as in the cases on the right, the network will behave as if it has negative curvature. In the bottom row of pictures, the networks are laid out as on page 479, so that successive heights give the number of nodes at successive distances r from a particular node. In the limit of large r, this number is approximately  $r^2 (1 - k r^2 + ...)$  where k turns out to be exactly proportional to the curvature.

But how can we determine the curvature from the structure of each network? Earlier in this chapter we saw that if a network is going to correspond to ordinary space in some number of dimensions *d* , then this means that by going r connections from any given node one must reach about  $r^{d-1}$  nodes. But it turns out that when curvature is present it leads to a systematic correction to this.

In each of the pictures on the facing page the network shown can be thought of as corresponding to two-dimensional space. And this means that to a first approximation the number of nodes reached must increase linearly with r. But the bottom row of pictures show that there are corrections to this. And what happens is that when there is positive curvature—as in the pictures on the left—progressively fewer than r nodes end up being reached. But when there is negative curvature—as on the right—progressively more nodes end up being reached. And in general the leading correction to the number of nodes reached turns out to be proportional to the curvature multiplied by  $r^{d+1}$ .

So what happens in more than two dimensions? In general the result could be very complicated, and could for example involve all sorts of different forms of curvature and other characteristics of space. But in fact the leading correction to the number of nodes reached is always quite simple: it is just proportional to what is called the Ricci scalar curvature, multiplied by  $r^{d+1}$ . And already here this is some suggestion of general relativity—for the Ricci scalar curvature also turns out to be a central quantity in the Einstein equations.

But in trying to see a more detailed correspondence there are immediately a variety of complications. Perhaps the most obvious is that the traditional mathematical formulation of general relativity seems to rely on many detailed properties of continuous space. And while one expects that sufficiently large networks should in some sense act on average like continuous space, it is far from clear at first how the kinds of properties of relevance to general relativity will emerge.

If one starts, say, from an ordinary continuous surface, then it is straightforward to approximate it as in the picture on the right by a collection of flat faces. And one might think that the edges of these faces would define a network of the kind I have been discussing.

![](Images/_page_548_Picture_7.jpeg)

A surface approximated by flat faces whose edges form a trivalent network.

But in fact, such a network has vastly less information. For given just a set of connections between nodes, there is no obvious way even to know which of these connections should be associated with the same face—let alone to work out anything like angles between faces.

Yet despite this, it turns out that all the geometrical features that are ultimately of relevance to general relativity can actually be determined in large networks just from the connectivity of nodes.

One of these is the value of the so-called Ricci tensor, which in effect specifies how the Ricci scalar curvature is made up from different curvature components associated with different directions.

As indicated above, the scalar curvature associated with a network is directly related to how many nodes lie within successive distances r of a given node on the network—or in effect how many nodes lie within successive generalized spheres around that node. And it turns out that the projection of the Ricci tensor along a particular direction is then just related to the number of nodes that lie within a cylinder oriented in that direction. But even just defining a consistent direction in a network is not entirely straightforward. But one way to do it is simply to pick two points in the network, then to say that paths in the network are going in the same direction if they are segments of the same shortest path between those points. And with this definition, a region that approximates a cylinder can be formed just by setting up spheres with centers at every point on the path.

But there is now another issue to address: at least in its standard formulation general relativity is set up in terms of properties not of three-dimensional space but rather of four-dimensional spacetime. And this means that what is relevant are properties not so much of specific networks representing space, but rather of complete causal networks.

And one immediate feature of causal networks that differs from space networks is that their connections go only one way. But it turns out that this is exactly what one needs in order to set up the analog of a spacetime Ricci tensor. The idea is to start at a particular event in the causal network, then to form what is in effect a cone of events that can be reached from there. To define the spacetime Ricci tensor, one considers—as on page 516—a sequence of spacelike slices through this

cone and asks how the number of events that lie within the cone increases as one goes to successive slices. After t steps, the number of events reached will be proportional to  $t^d$ . But there is then a correction proportional to  $t^{d+2}$ , that has a coefficient that is a combination of the spacetime Ricci scalar and a projection of the spacetime Ricci tensor along what is in effect the time direction defined by the sequence of spacelike slices chosen.

So how does this relate to general relativity? It turns out that when there is no matter present the Einstein equations simply state that the spacetime Ricci tensor—and thus all of its projections—are exactly zero. There can still for example be higher-order curvature, but there can be no curvature at the level described by the Ricci tensor.

So what this means is that any causal network whose behavior obeys the Einstein equations must at the level of counting nodes in a cone have the same uniform structure as it would if it were going to correspond to ordinary flat space. As we saw a few sections ago, many underlying replacement rules end up producing networks that are for example too extensively connected to correspond to ordinary space in any finite number of dimensions. But I suspect that if one has replacement rules that are causal invariant and that in effect successfully maintain a fixed number of dimensions they will almost inevitably lead to behavior that follows something close to the Einstein equations.

Probably the situation is somewhat analogous to what we saw with fluid behavior in cellular automata in Chapter 8—that at least if there are underlying rules whose behavior is complicated enough to generate significant effective randomness, then almost whenever the rules lead to conservation of total particle number and momentum something close to the ordinary Navier-Stokes equation behavior emerges.

So what about matter?

As a first step, one can ask what effect the structure of space has on something like a particle—assuming that one can ignore the effect of the particle back on space. In traditional general relativity it is always assumed that a particle which is not interacting with anything else will move along a shortest path—or so-called geodesic—in space.

But what about an explicit particle of the kind we discussed in the previous section that exists as a structure in a network? Given two nodes in a network, one can always identify a shortest path from one to the other that goes along a sequence of individual connections in the network. But in a sense a structure that corresponds to a particle will normally not fit through this path. For usually the structure will involve many nodes, and thus typically require many connections going in more or less the same direction in order to be able to move across the network.

But if one assumes a certain uniformity in networks—and in particular in the causal network—then it still follows that particles of the kind that we discussed in the previous section will tend to move along geodesics. And whereas in traditional general relativity the idea of motion along geodesics is essentially an assumption, this can now in principle be derived explicitly from an underlying network model.

One might have thought that in the absence of matter there would be little to say about gravity—since after all the Einstein equations then say that there can be no curvature in space, at least of the kind described by the Ricci tensor. But it turns out that there can still be other kinds of curvature—described for example by the so-called Riemann tensor—and these can in fact lead to all sorts of phenomena. Examples include familiar ones like inverse-square gravitational fields around massive objects, as well as unfamiliar ones like gravitational waves.

But while the mathematical structure of general relativity is complicated enough that it is often difficult to see just where in spacetime effects come from, it is usually assumed that matter is somehow ultimately required to provide a source for gravity. And in the full Einstein equations the Ricci tensor need not be zero; instead it is specified at every point in space as being equal to a certain combination of energy and momentum density for matter at that point. So this means that to know what will happen even in phenomena primarily associated with gravity one typically has to know all sorts of properties of matter.

But why exactly does matter have to be introduced explicitly at all? It has been the assumption of traditional physics that even though gravity can be represented in terms of properties of space, other elements of our universe cannot. But in my approach everything just emerges from the same underlying network—or in effect from the structure of space. And indeed even in traditional general relativity one can try avoiding introducing matter explicitly—for example by imagining that everything we call matter is actually made up of pure gravitational energy, or of something like gravitational waves.

But so far as one can tell, the details of this do not work out—so that at the level of general relativity there is no choice but to introduce matter explicitly. Yet I suspect that this is in effect just a sign of limitations in the Einstein equations and general relativity.

For while at a large scale these may provide a reasonable description of average behavior in a network, it is almost inevitable that closer to the scale of individual connections they will have to be modified. Yet presumably one can still use the Einstein equations on large scales if one introduces matter with appropriate properties as a way to represent small-scale effects in the network.

In the previous section I suggested that energy and momentum might in effect be associated with the presence of excess nodes in a network. And this now potentially seems to fit quite well with what we have seen in this section. For if the underlying rule for a network is going to maintain to a certain approximation the same average number of nodes as flat space, then it follows that wherever there are more nodes corresponding to energy and momentum, this must be balanced by something reducing the number of nodes. But such a reduction is exactly what is needed to correspond to positive curvature of the kind implied by the Einstein equations in the presence of ordinary matter.

#### Quantum Phenomena

From our everyday experience with objects that we can see and touch we develop a certain intuition about how things work. But nearly a century ago it became clear that when it comes to things like electrons some of this intuition is no longer correct. Yet there has developed an elaborate mathematical formalism in quantum theory that successfully reproduces much of what is observed. And while some aspects of this

formalism remain mysterious, it has increasingly come to be believed that any fundamental theory of physics must somehow be based on it.

Yet the kinds of programs I have discussed in this book are not in any obvious way set up to fit in with this formalism. But as we have seen a great many times in the course of the book, what emerges from a program can be very different from what is obvious in its underlying rules. And in fact it is my strong suspicion that the kinds of programs that I have discussed in the past few sections will actually in the end turn out to show many if not all the key features of quantum theory.

To see this, however, will not be easy. For the kinds of constructs that are emphasized in the standard formalism of quantum theory are very different from those immediately visible in the programs I have discussed. And ultimately the only reliable way to make contact will probably be to set up rather complete and realistic models of experiments—then gradually to see how limits and idealizations of these manage to match what is expected from the standard formalism. Yet from what we have seen in this chapter and earlier in this book there are already some encouraging signs that one can identify.

At first, though, things might not seem promising. For my model of particles such as electrons being persistent structures in a network might initially seem to imply that such particles are somehow definite objects just like ones familiar from everyday experience. But there are all sorts of phenomena in quantum theory that seem to indicate that electrons do not in fact behave like ordinary objects that have definite properties independent of us making observations of them.

So how can this be consistent? The basic answer is just that a network which represents our whole universe must also include us as observers. And this means that there is no way that we can look at the network from the outside and see the electron as a definite object. Instead, anything we deduce about the electron must come from processes that explicitly go on inside the network.

But this is not just an issue in studying things like electrons: it is actually a completely general feature of the models I have discussed. And in fact, as we saw earlier in this chapter, it is what allows them to support meaningful notions of even such basic concepts as time. At a

more formal level, it also implies that everything we can observe can be captured by a causal network. And as I will discuss a little below, I suspect that the idea of causal invariance for such a network will then be what turns out to account for some key features of quantum theory.

The basic picture of our universe that I have outlined in the past few sections is a network whose connections are continually updated according to some simple set of underlying rules. In the past one might have assumed that a system like this would be far too simple to correspond to our universe. But from the discoveries in this book we now know that even when the underlying rules for a system are simple, its overall behavior can still be immensely complex.

And at the lowest level what I expect is that even though the rules being applied are perfectly definite, the overall pattern of connections that will exist in the network corresponding to our universe will continually be rearranged in ways complicated enough to seem effectively random.

Yet on a slightly larger scale such randomness will then lead to a certain average uniformity. And it is then essentially this that I believe is responsible for maintaining something like ordinary space—with gradual variations giving rise to the phenomenon of gravity.

But superimposed on this effectively random background will then presumably also be some definite structures that persist through many updatings of the network. And it is these, I believe, that are what correspond to particles like electrons.

As I discussed in the last two sections, causal invariance of the underlying rules implies that such structures should be able to move at a range of uniform speeds through the background. Typically properties like charge will be associated with some specific pattern of connections at the core of the structure corresponding to a particle, while the energy and momentum of the particle will be associated with roughly the number of nodes in some outer region around the core.

So what about interactions? If the structures corresponding to different particles are isolated, then the underlying rules will make them persist. But if they somehow overlap, these same rules will usually make some different configuration of particles be produced.

![](Images/_page_555_Picture_1.jpeg)

A collision between localized structures in the rule 110 class 4 cellular automaton.

At some level the situation will no doubt be a little like in the evolution of a typical class 4 cellular automaton, as illustrated on the left. Given some initial set of persistent structures, these can interact to produce some intermediate pattern of behavior, which then eventually resolves into a final set of structures that again persist.

In the intermediate pattern of behavior one may also be able to identify some definite structures. Ones that do not last long can be very different from ones that would persist forever. But ones that last longer will tend to have properties progressively closer to genuinely persistent structures. And while persistent structures can be thought of as corresponding to real particles, intermediate structures are in many ways like the virtual particles of traditional particle physics.

So this means that a picture like the one on the left above can be viewed in a remarkably literal sense as being a spacetime diagram of particle interactions—a bit like a Feynman diagram from particle physics.

One immediate difference, however, is that in traditional particle physics one does not imagine a pattern of behavior as definite and determined as in the picture above. And indeed in my model for the universe it is already clear that there is more going on. For any process like the one in the picture above must occur on top of a background of apparently random small-scale rearrangements of the network. And in effect what this background does is to introduce a kind of random environment that can make many different detailed patterns of behavior occur with certain probabilities even with the same initial configuration of particles.

The idea that even a vacuum without particles will have a complicated and in some ways random form also exists in standard quantum field theory in traditional physics. The full mathematical structure of quantum field theory is far from completely worked out. But the basic notion is that for each possible type of particle there is some kind of continuous field that exists throughout space—with the presence of a particle corresponding to a simple type of structure in this field.

In general, the equations of quantum field theory seem to imply that there can be all sorts of complicated configurations in the field, even in the absence of actual particles. But as a first approximation, one can consider just short-lived pairs of virtual particles and antiparticles. And in fact one can often do something similar for networks. For even in the planar networks discussed on page 527 a great many different arrangements of connections can be viewed as being formed from different configurations of nearby pairs of non-planar persistent structures.

Talking about a random background affecting processes in the universe immediately tends to suggest certain definite relations between probabilities for different processes. Thus for example, if there are two different ways that some process can occur, it suggests that the total probability for the whole process should be just the sum of the probabilities for the process to occur in the two different ways.

But the standard formalism of quantum theory says that this is not correct, and that in fact one has to look at so-called probability amplitudes, not ordinary probabilities. At a mathematical level, such amplitudes are analogous to ones for things like waves, and are in effect just numbers with directions. And what quantum theory says is that the probability for a whole process can be obtained by linearly combining the amplitudes for the different ways the process can occur, then looking at the square of the magnitude of the result—or the analog of intensity for something like a wave.

So how might this kind of mathematical procedure emerge from the types of models I have discussed? The answer seems complicated. For even though the procedure itself may sound straightforward, the constructs on which it operates are actually far from easy to define just on the basis of an underlying network—and I have seen no easy way to unravel the various limits and idealizations that have to be made.

Nevertheless, a potentially important point is that it is in some ways misleading to think of particles in a network as just interacting according to some definite rule, and being perturbed by what is in essence a random background. For this suggests that there is in effect a unique history to every particle interaction—determined by the initial conditions and the configuration that exists in the random background.

But the true picture is more complicated. For the sequence of updates to the underlying network can be made in any order—yet each order in effect gives a different detailed history for the network. But if there is causal invariance, then ultimately all these different histories must in a sense be equivalent. And with this constraint, if one breaks some process into parts, there will typically be no simple way to describe how the effect of these parts combines together.

And for at least some purposes it may well make sense to think explicitly about different possible histories, combining something like amplitudes that one assigns to each of them. Yet quite how this might work will certainly depend on what feature of the network one tries to look at.

It has always been a major issue in quantum theory just how one tells what is happening with a particular particle like an electron. From our experience with everyday objects we might think that it should somehow be possible to do this without affecting the electron. But if the only things we have are particles, then to find out something about a given particle we inevitably have to have some other particle—say a photon of light—explicitly interact with it. And in this interaction the original particle will inevitably be affected in some way.

And in fact just one interaction will certainly not be enough. For we as humans cannot normally perceive individual particles. And indeed there usually have to be a huge number of particles doing more or less the same thing before we successfully register it.

Most often the way this is made to happen is by setting up some kind of detector that is initially in a state that is sufficiently unstable that just a single particle can initiate a whole cascade of consequences. And usually such a detector is arranged so that it evolves to one or another stable state that has sufficiently uniform properties that we can recognize it as corresponding to a definite outcome of a measurement.

At first, however, such evolution to an organized state might seem inconsistent with microscopic reversibility. But in fact—just as in so many other seemingly irreversible processes—all that is needed to preserve reversibility is that if one looks at sufficient details of the system there can be arbitrary and seemingly random behavior. And the point is just that in making conclusions about the result of a measurement we choose to ignore such details.

So even though the actual result that we take away from a measurement may be quite simple, many particles—and many events—

will always be involved in getting it. And in fact in traditional quantum theory no measurement can ultimately end up giving a definite result unless in effect an infinite number of particles are involved.

As I mentioned above, ordinary quantum processes can appear to follow different histories depending on what scheme is used to decide the order in which underlying rules are applied. But taking the idealized limit of a measurement in which an infinite number of particles are involved will probably in effect establish a single history.

And this implies that if one knew all of the underlying details of the network that makes up our universe, it should always be possible to work out the result of any measurement. I strongly believe that the initial conditions for the universe were quite simple. But like many of the processes we have seen in this book, the evolution of the universe no doubt intrinsically generates apparent randomness.

And the result is that most aspects of the network that represents the current state of our universe will seem essentially random. So this means that to know its form we would in essence have to sample every one of its details—which is certainly not possible if we have to use measurements that each involve a huge number of particles.

One might however imagine that as a first approximation one could take account of underlying apparent randomness just by saying that there are certain probabilities for particles to behave in particular ways. But one of the most often quoted results about foundations of quantum theory is that in practice there can be correlations observed between particles that seem impossible to account for in at least the most obvious kind of such a so-called hidden-variables theory.

For in particular, if one takes two particles that have come from a single source, then the result of a measurement on one of them is found in a sense to depend too much on what measurement gets done on the other—even if there is not enough time for information travelling at the speed of light to get from one to the other. And indeed this fact has often been taken to imply that quantum phenomena can ultimately never be the result of any definite underlying process of evolution.

But this conclusion depends greatly on traditional assumptions about the nature of space and of particles. And it turns out that for the kinds of models I have discussed here it in general no longer holds.

And the basic reason for this is that if the universe is a network then it can in a sense easily contain threads that continue to connect particles even when the particles get far apart in terms of ordinary space.

The picture that emerges is then of a background containing a very large number of connections that maintain an approximation to three-dimensional space, together with a few threads that in effect go outside of that space to make direct connections between particles.

If two particles get created together, it is reasonable to expect that the tangles that represent their cores will tend to have a few connections in common—and indeed this for example happens for lumps of non-planarity of the kind we discussed on page 527. But until there are interactions that change the structure of the cores, these common connections will then remain—and will continue to define a thread that goes directly from one particle to the other.

But there is immediately a slight subtlety here. For earlier in this chapter I discussed measuring distance on a network just by counting the minimum number of successive individual connections that one has to follow in order to get from one point to another. Yet if one uses this measure of distance then the distance between two particles will always tend to remain fixed as the number of connections in the thread.

But the point is that this measure of distance is in reality just a simple idealization of what is relevant in practice. For the only way we end up actually being able to measure physical distances is in effect by looking at the propagation of photons or other particles. Yet such particles always involve many nodes. And while they can get from one point to another through the large number of connections that define the background space, they cannot in a sense fit through a small number of connections in a thread. So this means that distance as we normally experience it is typically not affected by threads.

But it does not mean that threads can have no effect at all. And indeed what I suspect is that it is precisely the presence of threads that leads to the correlations that are seen in measurements on particles.

It so happens that the standard formalism of quantum theory provides a rather simple mathematical description of these correlations. And it is certainly far from obvious how this might emerge from detailed mechanisms associated with threads in a network. But the fact that this and other results seem simple in the standard formalism of quantum theory should not be taken to imply that they are in any sense particularly fundamental. And indeed my guess is that most of them will actually in the end turn out to depend on all sorts of limits and idealizations in quantum theory—and will emerge just as simple approximations to much more complex underlying behavior.

In its development since the early 1900s quantum theory has produced all sorts of elaborate results. And to try to derive them all from the kinds of models I have outlined here will certainly take an immense amount of work. But I consider it very encouraging that some of the most basic quantum phenomena seem to be connected to properties like causal invariance and the network structure of space that already arose in our discussion of quite different fundamental issues in physics.

And all of this supports my strong belief that in the end it will turn out that every detail of our universe does indeed follow rules that can be represented by a very simple program—and that everything we see will ultimately emerge just from running this program.
