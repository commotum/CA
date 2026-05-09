#### Starting from Randomness

#### The Emergence of Order

In the past several chapters, we have seen many examples of behavior that simple programs can produce. But while we have discussed a whole range of different kinds of underlying rules, we have for the most part considered only the simplest possible initial conditions—so that for example we have usually started with just a single black cell.

My purpose in this chapter is to go to the opposite extreme, and to consider completely random initial conditions, in which, for example, every cell is chosen to be black or white at random.

One might think that starting from such randomness no order would ever emerge. But in fact what we will find in this chapter is that many systems spontaneously tend to organize themselves, so that even with completely random initial conditions they end up producing behavior that has many features that are not at all random.

The picture at the top of the next page shows as a simple first example a cellular automaton which starts from a typical random initial condition, then evolves down the page according to the very simple rule that a cell becomes black if either of its neighbors are black.

What the picture then shows is that every region of white that exists in the initial conditions progressively gets filled in with black, so that in the end all that remains is a uniform state with every cell black.

![](Images/_page_239_Picture_1.jpeg)

![](Images/_page_239_Picture_2.jpeg)

A cellular automaton that evolves to a simple uniform state when started from any random initial condition. The rule in this case was first shown on page 24, and is number 254 in the scheme described on page 53. It specifies that a cell should become black whenever either of its neighbors is already black.

The pictures below show examples of other cellular automata that exhibit the same basic phenomenon. In each case the initial conditions are random, but the system nevertheless quickly organizes itself to become either uniformly white or uniformly black.

![](Images/_page_239_Picture_5.jpeg)

Four more examples of cellular automata that evolve from random initial conditions to completely uniform states. The rules shown here correspond to numbers 0, 32, 160 and 250.

The facing page shows cellular automata that exhibit slightly more complicated behavior. Starting from random initial conditions, these cellular automata again quickly settle down to stable states. But now these stable states are not just uniform in color, but instead involve a collection of definite structures that either remain fixed on successive steps, or repeat periodically.

So if they have simple underlying rules, do all cellular automata started from random initial conditions eventually settle down to give stable states that somehow look simple?

![](Images/_page_240_Figure_2.jpeg)

Examples of cellular automata that evolve from random initial conditions to produce a definite set of simple structures. For any particular rule, the form of these structures is always the same. But their positions depend on the details of the initial conditions given, and in many cases the final arrangement of structures can be thought of as a kind of filtered version of the initial conditions. Thus for example in the first rule shown here a structure consisting of a black cell occurs wherever there was an isolated black cell in the initial conditions. The rules shown are numbers 4, 108, 218 and 232.

It turns out that they do not. And indeed the picture on the next page shows one of many examples in which starting from random initial conditions there continues to be very complicated behavior forever. And indeed the behavior that is produced appears in many respects completely random. But dotted around the picture one sees many definite white triangles and other small structures that indicate at least a certain degree of organization.

![](Images/_page_241_Picture_2.jpeg)

![](Images/_page_241_Picture_3.jpeg)

A cellular automaton that never settles down to a stable state, but instead continues to show behavior that seems in many respects random. The rule is number 126.

![](Images/_page_242_Figure_2.jpeg)

![](Images/_page_242_Picture_4.jpeg)

![](Images/_page_242_Picture_5.jpeg)

Other examples of cellular automata that never settle down to stable states when started from random initial conditions. Each picture is a total of 300 cells across. Note the presence of triangles and other small structures dotted throughout all of the pictures.

![](Images/_page_243_Picture_1.jpeg)

Two more cellular automata that generate various small structures but continue to show seemingly quite random behavior forever.

The pictures above and on the previous page show more examples of cellular automata with similar behavior. There is considerable randomness in the patterns produced in each case. But despite this randomness there are always triangles and other small structures that emerge in the evolution of the system.

So just how complex can the behavior of a cellular automaton that starts from random initial conditions be? We have seen some examples where the behavior quickly stabilizes, and others where it continues to be quite random forever. But in a sense the greatest complexity lies between these extremes—in systems that neither stabilize completely, nor exhibit close to uniform randomness forever.

The facing page and the one that follows show as an example the cellular automaton that we first discussed on page 32. The initial conditions used are again completely random. But the cellular automaton quickly organizes itself into a set of definite localized structures. Yet now these structures do not just remain fixed, but instead move around and interact with each other in complicated ways. And the result of this is an elaborate pattern that mixes order and randomness—and is as complex as anything we have seen in this book.

![](Images/_page_244_Picture_2.jpeg)

Complex behavior in the rule 110 cellular automaton starting from a random initial condition. The system quickly organizes itself to produce a set of definite localized structures, which then move around and interact with each other in complicated ways.

![](Images/_page_245_Picture_1.jpeg)

A continuation of the pattern from the previous page. Each page shows 700 steps in the evolution of the cellular automaton.

#### Four Classes of Behavior

In the previous section we saw what a number of specific cellular automata do if one starts them from random initial conditions. But in this section I want to ask the more general question of what arbitrary cellular automata do when started from random initial conditions.

One might at first assume that such a general question could never have a useful answer. For every single cellular automaton after all ultimately has a different underlying rule, with different properties and potentially different consequences.

But the next few pages show various sequences of cellular automata, all starting from random initial conditions.

And while it is indeed true that for almost every rule the specific pattern produced is at least somewhat different, when one looks at all the rules together, one sees something quite remarkable: that even though each pattern is different in detail, the number of fundamentally different types of patterns is very limited.

Indeed, among all kinds of cellular automata, it seems that the patterns which arise can almost always be assigned quite easily to one of just four basic classes illustrated below.

![](Images/_page_246_Picture_8.jpeg)

![](Images/_page_246_Picture_9.jpeg)

![](Images/_page_246_Picture_10.jpeg)

![](Images/_page_246_Picture_11.jpeg)

Examples of the four basic classes of behavior seen in the evolution of cellular automata from random initial conditions. I first developed this classification in 1983.

These classes are conveniently numbered in order of increasing complexity, and each one has certain immediate distinctive features.

In class 1, the behavior is very simple, and almost all initial conditions lead to exactly the same uniform final state.

![](Images/_page_247_Figure_2.jpeg)

The behavior of all cellular automata that involve only nearest neighbors in a symmetrical way, have two possible colors for each cell, and leave states consisting only of white cells unchanged.

![](Images/_page_248_Figure_2.jpeg)

Totalistic cellular automata whose rules involve nearest and next-nearest neighbors, and where each cell has two possible colors.

![](Images/_page_249_Picture_1.jpeg)

A sequence of totalistic cellular automata with rules that involve only nearest neighbors, but where each cell can have three possible colors.

In class 2, there are many different possible final states, but all of them consist just of a certain set of simple structures that either remain the same forever or repeat every few steps.

In class 3, the behavior is more complicated, and seems in many respects random, although triangles and other small-scale structures are essentially always at some level seen.

And finally, as illustrated on the next few pages, class 4 involves a mixture of order and randomness: localized structures are produced which on their own are fairly simple, but these structures move around and interact with each other in very complicated ways.

I originally discovered these four classes of behavior some seventeen years ago by looking at thousands of pictures similar to those on the last few pages. And at first, much as I have done here, I based my classification purely on the general visual appearance of the patterns I saw.

But when I studied more detailed properties of cellular automata, what I found was that most of these properties were closely correlated with the classes that I had already identified. Indeed, in trying to predict detailed properties of a particular cellular automaton, it was often enough just to know what class the cellular automaton was in.

And in a sense the situation was similar to what is seen, say, with the classification of materials into solids, liquids and gases, or of living organisms into plants and animals. At first, a classification is made purely on the basis of general appearance. But later, when more detailed properties become known, these properties turn out to be correlated with the classes that have already been identified.

Often it is possible to use such detailed properties to make more precise definitions of the original classes. And typically all reasonable definitions will then assign any particular system to the same class.

Examples of class 4 cellular automata with totalistic rules involving nearest neighbors and three possible colors for each cell. Each picture shows 1500 steps of evolution from random initial conditions.

![](Images/_page_251_Picture_1.jpeg)

code 1815

![](Images/_page_252_Picture_2.jpeg)

code 2007

![](Images/_page_253_Picture_1.jpeg)

code 238

![](Images/_page_254_Picture_1.jpeg)

code 2043

But with almost any general classification scheme there are inevitably borderline cases which get assigned to one class by one definition and another class by another definition. And so it is with cellular automata: there are occasionally rules like those in the pictures below that show some features of one class and some of another.

![](Images/_page_255_Picture_2.jpeg)

![](Images/_page_255_Picture_3.jpeg)

![](Images/_page_255_Picture_4.jpeg)

![](Images/_page_255_Picture_5.jpeg)

Rare examples of borderline cellular automata that do not fit squarely into any one of the four basic classes described in the text. Different definitions based on different specific properties will place these cellular automata into different classes. The rules shown are totalistic ones involving nearest neighbors and three possible colors for each cell. The first rule can be either class 2 or class 4, the second class 3 or 4, the third class 2 or 3 and the fourth class 1, 2 or 3.

But such rules are quite unusual, and in most cases the behavior one sees instead falls squarely into one of the four classes described above.

So given the underlying rule for a particular cellular automaton, can one tell what class of behavior the cellular automaton will produce?

In most cases there is no easy way to do this, and in fact there is little choice but just to run the cellular automaton and see what it does.

But sometimes one can tell at least a certain amount simply from the form of the underlying rule. And so for example all rules that lie in the first two columns on page 232 can be shown to be unable ever to produce anything besides class 1 or class 2 behavior.

In addition, even when one can tell rather little from a single rule, it is often the case that rules which occur next to each other in some sequence have similar behavior. This can be seen for example in the pictures on the facing page. The top row of rules all have class 1 behavior. But then class 2 behavior is seen, followed by class 4 and then class 3. And after that, the remainder of the rules are mostly class 3.

The fact that class 4 appears between class 2 and class 3 in the pictures on the facing page is not uncommon. For while class 4 is above class 3 in terms of apparent complexity, it is in a sense intermediate

![](Images/_page_256_Figure_2.jpeg)

A sequence of totalistic rules involving nearest neighbors and four possible colors for each cell chosen to show transitions between rules with different classes of behavior. Note that class 4 seems to occur between class 2 and class 3.

between class 2 and class 3 in terms of what one might think of as overall activity.

The point is that class 1 and 2 systems rapidly settle down to states in which there is essentially no further activity. But class 3 systems continue to have many cells that change at every step, so that they in a sense maintain a high level of activity forever. Class 4 systems are then in the middle: for the activity that they show neither dies out completely, as in class 2, nor remains at the high level seen in class 3.

And indeed when one looks at a particular class 4 system, it often seems to waver between class 2 and class 3 behavior, never firmly settling on either of them.

In some respects it is not surprising that among all possible cellular automata one can identify some that are effectively on the boundary between class 2 and class 3. But what is remarkable about actual class 4 systems that one finds in practice is that they have definite characteristics of their own—most notably the presence of localized structures—that seem to have no direct relation to being somehow on the boundary between class 2 and class 3.

And it turns out that class 4 systems with the same general characteristics are seen for example not only in ordinary cellular automata but also in such systems as continuous cellular automata.

The facing page shows a sequence of continuous cellular automata of the kind we discussed on page 155. The underlying rules in such systems involve a parameter that can vary smoothly from 0 to 1.

For different values of this parameter, the behavior one sees is different. But it seems that this behavior falls into essentially the same four classes that we have already seen in ordinary cellular automata. And indeed there are even quite direct analogs of for example the triangle structures that we saw in ordinary class 3 cellular automata.

But since continuous cellular automata have underlying rules based on a continuous parameter, one can ask what happens if one smoothly varies this parameter—and in particular one can ask what sequence of classes of behavior one ends up seeing.

The answer is that there are normally some stretches of class 1 or 2 behavior, and some stretches of class 3 behavior. But at the transitions

![](Images/_page_258_Figure_1.jpeg)

Examples of the evolution of continuous cellular automata from random initial conditions. As discussed on page 155, each cell here can have any gray level between 0 and 1, and at each step the gray level of a given cell is determined by averaging the gray levels of the cell and its two neighbors, adding the specified constant, and then keeping only the fractional part of the result. The behavior produced once again falls into distinct classes that correspond well to the four classes seen on previous pages in ordinary cellular automata.

![](Images/_page_259_Picture_2.jpeg)

0.39

![](Images/_page_259_Picture_4.jpeg)

0.4

![](Images/_page_259_Picture_6.jpeg)

{0.5, 1.13}

Examples of continuous cellular automata that exhibit class 4 behavior. The rules are of the same kind as in the previous picture, except that in the third case shown here, the gray level of each neighboring cell is multiplied by 1.13 before the average is done. In addition, the actual gray levels in these pictures are obtained by taking the difference between the gray level of each cell and its neighbor, thus removing the uniform stripes visible in the previous picture. It is remarkable that class 4 behavior with discrete localized structures can still occur in the continuous systems shown here.

it turns out that class 4 behavior is typically seen—as illustrated on the facing page. And what is particularly remarkable is that this behavior involves the same kinds of localized structures and other features that we saw in ordinary discrete class 4 cellular automata.

So what about two-dimensional cellular automata? Do these also exhibit the same four classes of behavior that we have seen in one dimension? The pictures on the next two pages show various steps in the evolution of some simple two-dimensional cellular automata starting from random initial conditions. And just as in one dimension a few distinct classes of behavior can immediately be seen.

But the correspondence with one dimension becomes much more obvious if one looks not at the complete state of a two-dimensional cellular automaton at a few specific steps, but rather at a one-dimensional slice through the system for a whole sequence of steps.

The pictures on page 248 show examples of such slices. And what we see is that the patterns in these slices look remarkably similar to the patterns we already saw in ordinary one-dimensional cellular automata. Indeed, by looking at such slices one can readily identify the very same four classes of behavior as in one-dimensional cellular automata.

So in particular one sees class 4 behavior. In the examples on page 248, however, such behavior always seems to occur superimposed on some kind of repetitive background—much as in the case of the rule 110 one-dimensional cellular automaton on page 229.

So can one get class 4 behavior with a simple white background? Much as in one dimension this does not seem to happen with the very simplest possible kinds of rules. But as soon as one goes to slightly more complicated rules—though still very simple—one can find examples.

And so as one example page 249 shows a two-dimensional cellular automaton often called the Game of Life in which all sorts of localized structures occur even on a white background. If one watches a movie of the behavior of this cellular automaton its correspondence to a one-dimensional class 4 system is not particularly obvious. But as soon as one looks at a one-dimensional slice—as on page 249—what one sees is immediately strikingly similar to what we have seen in many one-dimensional class 4 cellular automata.

![](Images/_page_261_Figure_2.jpeg)

Examples of the evolution of two-dimensional cellular automata with various totalistic rules starting from random initial conditions. The rules involve a cell and its four immediate neighbors. Each successive base 2 digit in the code number for the rule gives the outcome when the total of the cell and its four neighbors runs from 5 down to 0.

![](Images/_page_262_Figure_2.jpeg)

Patterns produced after 500 steps in the evolution of a sequence of two-dimensional cellular automata starting from random initial conditions. The rules shown are of the same kind as on the facing page, and include most of the 64 possibilities that leave a state that contains only white cells unchanged.

![](Images/_page_263_Figure_2.jpeg)

One-dimensional slices through the evolution of various two-dimensional cellular automata. In each picture black cells further back from the position of the slice are shown in progressively lighter shades of gray, as if they were receding into a kind of fog. Note the presence of examples of both class 3 and class 4 behavior that look strikingly similar to examples in one dimension.

![](Images/_page_264_Picture_2.jpeg)

![](Images/_page_264_Picture_3.jpeg)

![](Images/_page_264_Picture_4.jpeg)

![](Images/_page_264_Picture_5.jpeg)

![](Images/_page_264_Picture_6.jpeg)

#### **Sensitivity to Initial Conditions**

In the previous section we identified four basic classes of cellular automata by looking at the overall appearance of patterns they produce. But these four classes also have other significant distinguishing features—and one important example of these is their sensitivity to small changes in initial conditions.

The pictures below show the effect of changing the initial color of a single cell in a typical cellular automaton from each of the four classes of cellular automata identified in the previous section.

![](Images/_page_265_Picture_4.jpeg)

The effect of changing the color of a single cell in the initial conditions for typical cellular automata from each of the four classes identified in the previous section. The black dots indicate all the cells that change. The way that such changes behave is characteristically different for each of the four classes of systems.

The results are rather different for each class.

In class 1, changes always die out, and in fact exactly the same final state is reached regardless of what initial conditions were used. In class 2, changes may persist, but they always remain localized in a small region of the system. In class 3, however, the behavior is quite different. For as the facing page shows, any change that is made

![](Images/_page_266_Picture_2.jpeg)

![](Images/_page_266_Picture_3.jpeg)

![](Images/_page_266_Picture_4.jpeg)

The effect of changing the color of a single initial cell in three typical class 3 cellular automata.

typically spreads at a uniform rate, eventually affecting every part of the system. In class 4, changes can also spread, but only in a sporadic way—as illustrated on the facing page and the one that follows.

So what is the real significance of these different responses to changes in initial conditions? In a sense what they reveal are basic differences in the way that each class of systems handles information.

In class 1, information about initial conditions is always rapidly forgotten—for whatever the initial conditions were, the system quickly evolves to a single final state that shows no trace of them.

In class 2, some information about initial conditions is retained in the final configuration of structures, but this information always remains completely localized, and is never in any way communicated from one part of the system to another.

A characteristic feature of class 3 systems, on the other hand, is that they show long-range communication of information—so that any change made anywhere in the system will almost always eventually be communicated even to the most distant parts of the system.

Class 4 systems are once again somewhat intermediate between class 2 and class 3. Long-range communication of information is in principle possible, but it does not always occur—for any particular change is only communicated to other parts of the system if it happens to affect one of the localized structures that moves across the system.

There are many characteristic differences between the four classes of systems that we identified in the previous section. But their differences in the handling of information are in some respects particularly fundamental. And indeed, as we will see later in this book, it is often possible to understand some of the most important features of systems that occur in nature just by looking at how their handling of information corresponds to what we have seen in the basic classes of systems that we have identified here.

The effect of small changes in initial conditions in the rule 110 class 4 cellular automaton. The changes spread only when they are in effect carried by localized structures that propagate across the system.

![](Images/_page_268_Picture_2.jpeg)

![](Images/_page_269_Picture_1.jpeg)

1 cell changed

#### Systems of Limited Size and Class 2 Behavior

In the past two sections we have seen two important features of class 2 systems: first, that their behavior is always eventually repetitive, and second, that they do not support any kind of long-range communication.

So what is the connection between these two features?

The answer is that the absence of long-range communication effectively forces each part of a class 2 system to behave as if it were a system of limited size. And it is then a general result that any system of limited size that involves discrete elements and follows definite rules must always eventually exhibit repetitive behavior. Indeed, as we will discuss in the next chapter, it is this phenomenon that is ultimately responsible for much of the repetitive behavior that we see in nature.

The pictures below show a very simple example of the basic phenomenon. In each case there is a dot that can be in one of six possible positions. And at every step the dot moves a fixed number of positions to the right, wrapping around as soon as it reaches the right-hand end.

![](Images/_page_270_Figure_6.jpeg)

A simple system that contains a single dot which can be in one of six possible positions. At each step, the dot moves some number of positions to the right, wrapping around as soon as it reaches the right-hand end. The behavior of this system, like other systems of limited size, is always repetitive.

Looking at the pictures we then see that the behavior which results is always purely repetitive—though the period of repetition is different in different cases. And the basic reason for the repetitive behavior is that whenever the dot ends up in a particular position, it must always repeat whatever it did when it was last in that position.

But since there are only six possible positions in all, it is inevitable that after at most six steps the dot will always get to a position where it has been before. And this means that the behavior must repeat with a period of at most six steps.

The pictures below show more examples of the same setup, where now the number of possible positions is 10 and 11. In all cases, the behavior is repetitive, and the maximum repetition period is equal to the number of possible positions.

![](Images/_page_271_Figure_5.jpeg)

More examples of the type of system shown on the previous page, but now with 10 and 11 possible positions for the dot. The behavior always repeats itself in at most 10 or 11 steps. But the exact number of steps in each case depends on the prime factors of the numbers that define the system.

Sometimes the actual repetition period is equal to this maximum value. But often it is smaller. And indeed it is a common feature of systems of limited size that the repetition period one sees can depend greatly on the exact size of the system and the exact rule that it follows.

In the type of system shown on the facing page, it turns out that the repetition period is maximal whenever the number of positions moved at each step shares no common factor with the total number of possible positions—and this is achieved for example whenever either of these quantities is a prime number.

The pictures below show another example of a system of limited size based on a simple rule. The particular rule is at each step to double the number that represents the position of the dot, wrapping around as soon as this goes past the right-hand end.

![](Images/_page_272_Figure_5.jpeg)

![](Images/_page_272_Figure_6.jpeg)

A system where the number that represents the position of the dot doubles at each step, wrapping around whenever it reaches the right-hand end. (After t steps the dot is thus at position  $Mod[2^t, n]$  in a size n system.) The plot at left gives the repetition period for this system as a function of its size; for odd n this period is equal to MultiplicativeOrder[2, n].

Once again, the behavior that results is always repetitive, and the repetition period can never be greater than the total number of possible positions for the dot. But as the picture shows, the actual repetition period jumps around considerably as the size of the system is changed. And as it turns out, the repetition period is again related to the factors of the number of possible positions for the dot—and tends to be maximal in those cases where this number is prime.

So what happens in systems like cellular automata?

The pictures on the facing page show some examples of cellular automata that have a limited number of cells. In each case the cells are in effect arranged around a circle, so that the right neighbor of the rightmost cell is the leftmost cell and vice versa.

And once again, the behavior of these systems is ultimately repetitive. But the period of repetition is often quite large.

The maximum possible repetition period for any system is always equal to the total number of possible states of the system.

For the systems involving a single dot that we discussed above, the possible states correspond just to possible positions for the dot, and the number of states is therefore equal to the size of the system.

But in a cellular automaton, every possible arrangement of black and white cells corresponds to a possible state of the system. With n cells there are thus  $2^n$  possible states. And this number increases very rapidly with the size n: for 5 cells there are already 32 states, for 10 cells 1024 states, for 20 cells 1,048,576 states, and for 30 cells 1,073,741,824 states.

The pictures on the next page show the actual repetition periods for various cellular automata. In general, a rapid increase with size is characteristic of class 3 behavior. Of the elementary rules, however, only rule 45 seems to yield periods that always stay close to the maximum of  $2^n$ . And in all cases, there are considerable fluctuations in the periods that occur as the size changes.

So how does all of this relate to class 2 behavior? In the examples we have just discussed, we have explicitly set up systems that have limited size. But even when a system in principle contains an infinite number of cells it is still possible that a particular pattern in that system will only grow to occupy a limited number of cells. And in any

![](Images/_page_274_Figure_2.jpeg)

The behavior of cellular automata with a limited number of cells. In each case the right neighbor of the rightmost cell is taken to be the leftmost cell and vice versa. The pattern produced always eventually repeats, but the period of repetition can increase rapidly with the size of the system.

![](Images/_page_275_Figure_1.jpeg)

Repetition periods for various cellular automata as a function of size. The initial conditions used in each case consist of a single black cell, as in the pictures on the previous page. The dashed gray line indicates the maximum possible repetition period of  $2^n$ . The maximum repetition period for rule 90 is  $2^{(n-1)/2} - 1$ . For rule 30, the peak repetition periods are of order  $2^{0.63n}$ , while for rule 45, they are close to  $2^n$  (for n = 29, for example, the period is 463,347,935, which is 86% of the maximum possible). For rule 110, the peaks seem to increase roughly like  $n^3$ .

such case, the pattern must repeat itself with a period of at most  $2^n$  steps, where n is the size of the pattern.

In a class 2 system with random initial conditions, a similar thing happens: since different parts of the system do not communicate with each other, they all behave like separate patterns of limited size. And in fact in most class 2 cellular automata these patterns are effectively only a few cells across, so that their repetition periods are necessarily quite short.

#### **Randomness in Class 3 Systems**

When one looks at class 3 systems the most obvious feature of their behavior is its apparent randomness. But where does this randomness ultimately come from? And is it perhaps all somehow just a reflection of randomness that was inserted in the initial conditions?

The presence of randomness in initial conditions—together with sensitive dependence on initial conditions—does imply at least some degree of randomness in the behavior of any class 3 system. And indeed when I first saw class 3 cellular automata I assumed that this was the basic origin of their randomness.

But the crucial point that I discovered only some time later is that random behavior can also occur even when there is no randomness in initial conditions. And indeed, in earlier chapters of this book we have already seen many examples of this fundamental phenomenon.

The pictures below now compare what happens in the rule 30 cellular automaton from page 27 if one starts from random initial conditions and from initial conditions involving just a single black cell.

![](Images/_page_276_Picture_6.jpeg)

![](Images/_page_276_Picture_7.jpeg)

Comparison of the patterns produced by the rule 30 cellular automaton starting from random initial conditions and from simple initial conditions involving just a single black cell. Away from the edge of the second picture, the patterns look remarkably similar.

The behavior we see in the two cases rapidly becomes almost indistinguishable. In the first picture the random initial conditions certainly affect the detailed pattern that is obtained. But the crucial point is that even without any initial randomness much of what we see in the second picture still looks like typical random class 3 behavior.

So what about other class 3 cellular automata? Do such systems always produce randomness even with simple initial conditions?

The pictures below show an example in which random class 3 behavior is obtained when the initial conditions are random, but where the pattern produced by starting with a single black cell has just a simple nested form.

![](Images/_page_277_Picture_5.jpeg)

Patterns produced by the rule 22 cellular automaton starting from random initial conditions and from an initial condition containing a single black cell. With random initial conditions typical class 3 behavior is seen. But with the specific initial condition shown on the right, a simple nested pattern is produced.

Nevertheless, the pictures on the facing page demonstrate that if one uses initial conditions that are slightly different—though still simple—then one can still see randomness in the behavior of this particular cellular automaton.

![](Images/_page_278_Figure_2.jpeg)

Rule 22 with various different simple initial conditions. In the top four cases, the pattern produced ultimately has a simple nested form. But in the bottom case, it is instead in many respects random, much like rule 30.

There are however a few cellular automata in which class 3 behavior is obtained with random initial conditions, but in which no significant randomness is ever produced with simple initial conditions.

The pictures below show one example. And in this case it turns out that all patterns are in effect just simple superpositions of the basic nested pattern that is obtained by starting with a single black cell.

![](Images/_page_279_Picture_4.jpeg)

Patterns generated by rule 90 with various initial conditions. This particular cellular automaton rule has the special property of additivity which implies that with any initial conditions the patterns that it produces can be obtained as simple superpositions of the first pattern shown above. Any initial condition that contains black cells only in a limited region will thus lead to a pattern that ultimately has a simple nested form. Unlike rule 30 or rule 22 therefore, rule 90 cannot intrinsically generate randomness starting from simple initial conditions. The randomness in the last picture shown here is thus purely a consequence of the randomness in its initial conditions. Note that the pictures above show only half as many steps of evolution as the corresponding pictures of rule 22 on the previous page.

As a result, when the initial conditions involve only a limited region of black cells, the overall pattern produced always ultimately has a simple nested form. Indeed, at each of the steps where a new white triangle starts in the center, the whole pattern consists just of two copies of the region of black cells from the initial conditions.

The only way to get a random pattern therefore is to have an infinite number of randomly placed black cells in the initial conditions.

And indeed when random initial conditions are used, rule 90 does manage to produce random behavior of the kind expected in class 3.

But if there are deviations from perfect randomness in the initial conditions, then these will almost inevitably show up in the evolution of the system. And thus, for example, if the initial density of black cells is low, then correspondingly low densities will occur again at various later steps, as in the second picture below.

With rule 22, on the other hand, there is no such effect, and instead after just a few steps no visible trace remains of the low density of initial black cells.

![](Images/_page_280_Figure_5.jpeg)

Examples of evolution from random initial conditions with a low density of black cells. In rule 22 the low initial density has no long-term effect. But in rule 90 its effect continues forever. The reason for this difference is that in rule 22 the randomness we see is intrinsically generated by the evolution of the system, while in rule 90 it comes from randomness in the initial conditions.

A couple of sections ago we saw that all class 3 systems have the property that the detailed patterns they produce are highly sensitive to detailed changes in initial conditions. But despite this sensitivity at the level of details, the point is that any system like rule 22 or rule 30 yields patterns whose overall properties depend very little on the form of the initial conditions that are given.

By intrinsically generating randomness such systems in a sense have a certain fundamental stability: for whatever is done to their initial conditions, they still give the same overall random behavior, with the same large-scale properties. And as we shall see in the next few chapters, there are in fact many systems in nature whose apparent stability is ultimately a consequence of just this kind of phenomenon.

#### **Special Initial Conditions**

We have seen that cellular automata such as rule 30 generate seemingly random behavior when they are started both from random initial conditions and from simple ones. So one may wonder whether there are in fact any initial conditions that make rule 30 behave in a simple way.

As a rather trivial example, one certainly knows that if its initial state is uniformly white, then rule 30 will just yield uniform white forever. But as the pictures below demonstrate, it is also possible to find less trivial initial conditions that still make rule 30 behave in a simple way.

![](Images/_page_281_Picture_6.jpeg)

![](Images/_page_281_Picture_7.jpeg)

![](Images/_page_281_Picture_8.jpeg)

Examples of special initial conditions that make the rule 30 cellular automaton yield simple repetitive behavior. Small patches with the same structures as shown here can be seen

embedded in typical random patterns produced by rule 30. At left is a representation of rule 30. Finding initial conditions that make cellular automata yield behavior with certain repetition periods is closely related to the problem of satisfying constraints discussed on page 210.

In fact, it turns out that in any cellular automaton it is inevitable that initial conditions which consist just of a fixed block of cells repeated forever will lead to simple repetitive behavior.

For what happens is that each block in effect independently acts like a system of limited size. The right-hand neighbor of the rightmost cell in any particular block is the leftmost cell in the next block, but since all the blocks are identical, this cell always has the same color as the leftmost cell in the block itself. And as a result, the block evolves just like one of the systems of limited size that we discussed on page 255. So this means that given a block that is n cells wide, the repetition period that is obtained must be at most  $2^n$  steps.

But if one wants a short repetition period, then there is a question of whether there is a block of any size which can produce it. The pictures on the next page show the blocks that are needed to get repetition periods of up to ten steps in rule 30. It turns out that no block of any size gives a period of exactly two steps, but blocks can be found for all larger periods at least up to 15 steps.

But what about initial conditions that do not just consist of a single block repeated forever? It turns out that for rule 30, no other kind of initial conditions can ever yield repetitive behavior.

But for many rules—including a fair number of class 3 ones—the situation is different. And as one example the picture on the right below shows an initial condition for rule 126 that involves two different blocks but which nevertheless yields repetitive behavior.

![](Images/_page_282_Picture_6.jpeg)

![](Images/_page_282_Picture_7.jpeg)

Rule 126 with a typical random initial condition, and with an initial condition that consists of a random sequence of two-cell blocks of the same color. Rule 126 in general shows class 3 behavior, as on the left. But with the special initial condition on the right it acts like a simple class 2 rule. Note the patches of class 2 behavior even in the picture on the left.

![](Images/_page_283_Picture_2.jpeg)

All patterns that repeat in 10 or less steps under evolution according to rule 30. In each case the initial conditions consist of a fixed block of cells that is repeated over and over again. Note that there are no initial conditions that yield a repetition period of exactly 2 steps. To get period 11, a block that contains 275 cells is required.

In a sense what is happening here is that even though rule 126 usually shows class 3 behavior, it is possible to find special initial conditions that make it behave like a simple class 2 rule.

And in fact it turns out to be quite common for there to exist special initial conditions for one cellular automaton that make it behave just like some other cellular automaton.

Rule 126 will for example behave just like rule 90 if one starts it from special initial conditions that contain only blocks consisting of pairs of black and white cells.

The pictures below show how this works: on alternate steps the arrangement of blocks in rule 126 corresponds exactly to the arrangement of individual cells in rule 90. And among other things this explains why it is that with simple initial conditions rule 126 produces exactly the same kind of nested pattern as rule 90.

![](Images/_page_284_Figure_6.jpeg)

Two examples of the fact that with special initial conditions rule 126 behaves exactly like rule 90. The initial conditions that are used consist of blocks of cells where each block contains either two black cells or two white cells. If one looks only on every other step, then the blocks behave exactly like individual cells in rule 90. This correspondence is the basic reason that rule 126 produces the same kind of nested patterns as rule 90 when it is started from simple initial conditions.

The point is that these initial conditions in effect contain only blocks for which rule 126 behaves like rule 90. And as a result, the overall patterns produced by rule 126 in this case are inevitably exactly like those produced by rule 90.

So what about other cellular automata that can yield similar patterns? In every example in this book where nested patterns like those from rule 90 are obtained it turns out that the underlying rules that are responsible can be set up to behave exactly like rule 90. Sometimes this will happen, say, for any initial condition that has black cells only in a limited region. But in other cases—like the example of rule 22 on page 263—rule 90 behavior is obtained only with rather specific initial conditions.

So what about rule 90 itself? Why does it yield nested patterns?

The basic reason can be thought of as being that just as other rules can emulate rule 90 when their initial conditions contain only certain blocks, so also rule 90 is able to emulate itself in this way.

The picture below shows how this works. The idea is to consider the initial conditions not as a sequence of individual cells, but rather as a sequence of blocks each containing two adjacent cells. And with an appropriate form for these blocks what one finds is that the configuration of blocks evolves exactly according to rule 90.

The fact that both individual cells and whole blocks of cells evolve according to the same rule then means that whatever pattern is

![](Images/_page_285_Figure_7.jpeg)

![](Images/_page_285_Figure_8.jpeg)

![](Images/_page_285_Picture_9.jpeg)

A demonstration of the fact that in rule 90 blocks of cells can behave just like individual cells. One consequence of this is that the patterns produced by rule 90 have a nested or self-similar form.

produced must have exactly the same structure whether it is looked at in terms of individual cells or in terms of blocks of cells. And this can be achieved in only two ways: either the pattern must be essentially uniform, or it must have a nested structure—just like we see in rule 90.

So what happens with other rules? It turns out that the property of self-emulation is rather rare among cellular automaton rules. But one other example is rule 150—as illustrated in the picture below.

![](Images/_page_286_Picture_3.jpeg)

![](Images/_page_286_Picture_4.jpeg)

![](Images/_page_286_Picture_5.jpeg)

Another example of a rule in which blocks of cells can behave just like individual cells. Rule 90 and rule 150 are also essentially the only fundamentally different elementary cellular automaton rules that have the property of being additive (see page 264).

So what else is there in common between rule 90 and rule 150? It turns out that they are both additive rules, implying that the patterns they produce can be superimposed in the way we discussed on page 264. And in fact one can show that any rule that is additive will be able to emulate itself and will thus yield nested patterns. But there are rather few additive rules, and indeed with two colors and nearest neighbors the only fundamentally different ones are precisely rules 90 and 150.

Ultimately, however, additive rules are not the only ones that can emulate themselves. An example of another kind is rule 184, in which blocks of three cells can act like a single cell, as shown below.

![](Images/_page_286_Picture_9.jpeg)

rule 184

![](Images/_page_286_Picture_11.jpeg)

A rule that is not additive, but in which blocks of cells can again behave just like individual cells.

With simple initial conditions of the type we have used so far this rule will always produce essentially trivial behavior. But one way to see the properties of the rule is to use nested initial conditions, obtained for example from substitution systems of the kind we discussed on page 82.

With most rules, including 90 and 150, such nested initial conditions typically yield results that are ultimately indistinguishable from those obtained with typical random initial conditions. But for rule 184, an appropriate choice of nested initial conditions yields the highly regular pattern shown below.

![](Images/_page_287_Picture_3.jpeg)

The pattern produced by rule 184 (shown at left) evolving from a nested initial condition. The particular initial condition shown can be obtained by applying the substitution system  $\blacksquare \to \blacksquare \blacksquare$ ,  $\Box \to \blacksquare \blacksquare$ , starting from a single black element  $\blacksquare$  (see page 83). With this initial condition, rule 184 exhibits an equal number of black and white stripes, which annihilate in pairs so as to yield a regular nested pattern.

The nested structure seen in this pattern can then be viewed as a consequence of the fact that rule 184 is able to emulate itself. And the picture below shows that rule 184—unlike any of the additive rules—still produces recognizably nested patterns even when the initial conditions that are used are random.

![](Images/_page_288_Picture_2.jpeg)

Rule 184 evolving from a random initial condition. Nested structure similar to what we saw in the previous picture is still visible. The presence of such structure is most obvious when there are equal numbers of black and white cells in the initial conditions, but it does not rely on any regularity in the arrangement of these cells.

As we will see on page 338 the presence of such patterns is particularly clear when there are equal numbers of black and white cells in the initial conditions—but how these cells are arranged does not usually matter much at all. And in general it is possible to find quite a few cellular automata that yield nested patterns like rule 184 even from random initial conditions. The picture on the next page shows a particularly striking example in which explicit regions are formed that contain patterns with the same overall structure as rule 90.

![](Images/_page_289_Picture_2.jpeg)

Another example of a cellular automaton that produces a nested pattern even from random initial conditions. The particular rule shown involves next-nearest as well as nearest neighbors and has rule number 4067213884. As in rule 184, the nested behavior seen here is most obvious when the density of black and white cells in the initial conditions is equal.

#### The Notion of Attractors

In this chapter we have seen many examples of patterns that can be produced by starting from random initial conditions and then following the evolution of cellular automata for many steps.

But what can be said about the individual configurations of black and white cells that appear at each step? In random initial conditions, absolutely any sequence of black and white cells can be present. But it is a feature of most cellular automata that on subsequent steps the sequences that can be produced become progressively more restricted.

The first picture below shows an extreme example of a class 1 cellular automaton in which after just one step the only sequences that can occur are those that contain only black cells.

![](Images/_page_290_Picture_6.jpeg)

Examples of simple cellular automata that evolve after just one step to attractors in which only certain sequences of black and white cells can occur. In the first case, the sequences that can occur are ones that involve only black cells. In the second case, the sequences are ones in which every black cell is surrounded by white cells. The rules shown are numbers 255 and 4.

The resulting configuration can be thought of as a so-called attractor for the cellular automaton evolution. It does not matter what initial conditions one starts from: one always reaches the same all-black attractor in the end. The situation is somewhat similar to what happens in a mechanical system like a physical pendulum. One can start the pendulum swinging in any configuration, but it will always tend to evolve to the configuration in which it is hanging straight down.

The second picture above shows a class 2 cellular automaton that once again evolves to an attractor after just one step. But now the attractor does not just consist of a single configuration, but instead consists of all configurations in which black cells occur only when they are surrounded on each side by at least one white cell.

The picture below shows that for any particular configuration of this kind, there are in general many different initial conditions that can lead to it. In a mechanical analogy each possible final configuration is like the lowest point in a basin—and a ball started anywhere in the basin will then always roll to that lowest point.

![](Images/_page_291_Figure_3.jpeg)

Four different initial conditions that all lead to the same final state in the rule 4 cellular automaton shown on the previous page. The final state can be thought of as one of the possible attractors for the evolution of the cellular automaton; the initial conditions shown then represent different elements in the basin of attraction for this attractor.

For one-dimensional cellular automata, it turns out that there is a rather compact way to summarize all the possible sequences of black and white cells that can occur at any given step in their evolution.

The basic idea is to construct a network in which each such sequence of black and white cells corresponds to a possible path.

In the pictures at the top of the facing page, the first network in each case represents random initial conditions in which any possible sequence of black and white cells can occur. Starting from the node in the middle, one can go around either the left or the right loop in the network any number of times in any order—representing the fact that black and white cells can appear any number of times in any order.

At step 2 in the rule 255 example on the facing page, however, the network has only one loop—representing the fact that at this step the only sequences which can occur with this rule are ones that consist purely of black cells, just as we saw on the previous page.

The case of rule 4 is slightly more complicated: at step 2, the possible sequences that can occur are now represented by a network with two nodes. Starting at the right-hand node one can go around the loop to the right any number of times, corresponding to sequences of

![](Images/_page_292_Figure_2.jpeg)

Networks representing possible sequences of black and white cells that can occur at successive steps in the evolution of the two cellular automata shown on the left. In each case the possible sequences correspond to possible paths through the network. Both rules start on step 1 from random initial conditions in which all sequences of black and white cells are allowed. On subsequent steps, rule 255 allows only sequences containing just black while rule 4 allows sequences that contain both black and white cells, but requires that every black cell be surrounded by white cells.

any number of white cells. At any point one can follow the arrow to the left to get a black cell, but the form of the network implies that this black cell must always be followed by at least one white cell.

The pictures on the next page show more examples of class 1 and 2 cellular automata. Unlike in the picture above, these rules do not reach their final states after one step, but instead just progressively evolve towards these states. And in the course of this evolution, the set of sequences that can occur becomes progressively smaller.

In rule 128, for example, the fact that regions of black shrink by one cell on each side at each step means that any region of black that exists after t steps must have at least t white cells on either side of it.

The networks shown on the next page capture all effects like this. And to do this we see that on successive steps they become somewhat more complicated. But at least for these class 1 and 2 examples, the progression of networks always continues to have a fairly simple form.

![](Images/_page_293_Picture_1.jpeg)

Networks representing possible sequences of black and white cells that can occur at successive steps in the evolution of several class 1 and 2 cellular automata. These networks never have more than about  $t^2$  nodes after t steps.

So what happens with class 3 and 4 systems? The pictures on the facing page show a couple of examples. In rule 126, the only effect at step 2 is that black cells can no longer appear on their own: they must always be in groups of two or more. By step 3, it becomes difficult to see any change if one just looks at an explicit picture of the cellular automaton evolution. But from the network, one finds that now an infinite collection of other blocks are forbidden, beginning with the length 12 block —————. And on later steps, the set of sequences that are allowed rapidly becomes more complicated—as reflected in a rapid increase in the complexity of the corresponding networks.

![](Images/_page_294_Figure_2.jpeg)

Networks representing possible sequences of black and white cells that can occur at successive steps in the evolution of typical class 3 and 4 cellular automata. The number of nodes in these networks seems to increase at a rate that is at least exponential.

Indeed, this kind of rapid increase in network complexity is a general characteristic of most class 3 and 4 rules. But it turns out that there are a few rules which at first appear to be exceptions.

The pictures at the top of the next page show four different rules that each have the property that if started from initial conditions in which all possible sequences of cells are allowed, these same sequences can all still occur at any subsequent step in the evolution.

The first two rules that are shown exhibit very simple class 2 behavior. But the last two show typical class 3 behavior.

What is going on, however, is that in a sense the particular initial conditions that allow all possible sequences are special for these rules.

![](Images/_page_295_Picture_2.jpeg)

Examples of cellular automata which continue to allow all possible sequences of black and white cells at any step in their evolution. Such cellular automata in effect define what are known as surjective or onto mappings.

And indeed if one starts with almost any other initial conditions—say for example ones that do not allow any pair of black cells together, then as the pictures below illustrate, rapidly increasing complexity in the sets of sequences that are allowed is again observed.

![](Images/_page_295_Picture_5.jpeg)

Networks representing possible sequences that can occur in the evolution of the cellular automata at the top of the page, starting from initial conditions in which black cells are only allowed to appear in pairs.

#### Structures in Class 4 Systems

The next page shows three typical examples of class 4 cellular automata. In each case the initial conditions that are used are completely random. But after just a few steps, the systems organize themselves to the point where definite structures become visible.

Most of these structures eventually die out, sometimes in rather complicated ways. But a crucial feature of any class 4 systems is that there must always be certain structures that can persist forever in it.

So how can one find out what these structures are for a particular cellular automaton? One approach is just to try each possible initial condition in turn, looking to see whether it leads to a new persistent structure. And taking the code 20 cellular automaton from the top of the next page, the page that follows shows what happens in this system with each of the first couple of hundred possible initial conditions.

In most cases everything just dies out. But when we reach initial condition number 151 we finally see a structure that persists.

This particular structure is fairly simple: it just remains fixed in position and repeats every two steps. But not all persistent structures are that simple. And indeed at initial condition 187 we see a considerably more complicated structure, that instead of staying still moves systematically to the right, repeating its basic form only every 9 steps.

The existence of structures that move is a fundamental feature of class 4 systems. For as we discussed on page 252, it is these kinds of structures that make it possible for information to be communicated from one part of a class 4 system to another—and that ultimately allow the complex behavior characteristic of class 4 to occur.

But having now seen the structure obtained with initial condition 187, we might assume that all subsequent structures that arise in the code 20 cellular automaton must be at least as complicated. It turns out, however, that initial condition 189 suddenly yields a much simpler structure—that just stays unchanged in one position at every step.

But going on to initial condition 195, we again find a more complicated structure—this time one that repeats only every 22 steps.

![](Images/_page_297_Picture_2.jpeg)

2 colors, next-nearest neighbors, code 20

![](Images/_page_297_Picture_4.jpeg)

3 colors, nearest neighbors, code 357

![](Images/_page_297_Picture_6.jpeg)

3 colors, nearest neighbors, code 1329

Three typical examples of class 4 cellular automata. In each case various kinds of persistent structures are seen.

![](Images/_page_298_Figure_2.jpeg)

The behavior of the code 20 cellular automaton from the top of the facing page for all initial conditions with black cells in a region of size less than nine. In most cases the patterns produced simply die out. But with some initial conditions, persistent structures are formed. Each initial condition is assigned a number whose base 2 digit sequence gives the configuration of black and white cells in that initial condition. Note that initial conditions 195 and 219 both yield the period 22 persistent structure shown on the next page.

So just what set of structures does the code 20 cellular automaton ultimately support? There seems to be no easy way to tell, but the picture below shows all the structures that I found by explicitly looking at evolution from the first twenty-five billion possible initial conditions.

![](Images/_page_299_Picture_3.jpeg)

Persistent structures found by testing the first twenty-five billion possible initial conditions for the code 20 cellular automaton shown on the previous page. Note that reflected versions of the structures shown are also possible. The base 2 digit sequences of the numbers given correspond to the initial conditions in each case, as on the previous page.

Are other structures possible? The largest structure in the picture above starts from a block that is 30 cells wide. And with the more than ten billion blocks between 30 and 34 cells wide, no new structures at all appear. Yet in fact other structures are possible. And the way to tell this is that for small repetition periods there is a systematic procedure that allows one to find absolutely all structures with a given period.

The picture on the facing page shows the results of using this procedure for repetition periods up to 15. And for all repetition periods up to 10—with the exception of 7—at least one fixed or moving structure ultimately turns out to exist. Often, however, the smallest structures for a given period are quite large, so that for example in the case of period 6 the smallest possible structure is 64 cells wide.

![](Images/_page_300_Figure_1.jpeg)

All the persistent structures with repetition periods up to 15 steps in the code 20 cellular automaton. The structures shown were found by a systematic method similar to the one used to find all sequences that satisfy the constraints on page 268.

So what about other class 4 cellular automata—like the ones I showed at the beginning of this section? Do they also end up having complicated sets of possible persistent structures?

The picture below shows the structures one finds by explicitly testing the first two billion possible initial conditions for the code 357 cellular automaton from page 282.

![](Images/_page_301_Picture_2.jpeg)

Persistent structures in the code 357 cellular automaton from page 282 obtained by testing the first two billion possible initial conditions. This cellular automaton allows three possible colors for each cell; the initial conditions thus correspond to the base 3 digits of the numbers given. No persistent structures of any size exist in this cellular automaton with repetition periods of less than 5 steps.

Already with initial condition number 28 a fairly complicated structure with repetition period 48 is seen. But with all the first million initial conditions, only one other structure is produced, and this structure is again one that does not move.

So are moving structures in fact possible in the code 357 cellular automaton? My experience with many different rules is that whenever sufficiently complicated persistent structures occur, structures that move can eventually be found. And indeed with code 357, initial condition 4,803,890 yields just such a structure.

So if moving structures are inevitable in class 4 systems, what other fundamentally different kinds of structures might one see if one were to look at sufficiently many large initial conditions?

The picture below shows the first few persistent structures found in the code 1329 cellular automaton from the bottom of page 282. The smallest structures are stationary, but at initial condition 916 a structure is found that moves—all much the same as in the two other class 4 cellular automata that we have just discussed.

![](Images/_page_302_Picture_3.jpeg)

Persistent structures in the code 1329 cellular automaton shown on page 282.

But when initial condition 54,889 is reached, one suddenly sees the rather different kind of structure shown on the next page. The right-hand part of this structure just repeats with a period of 256 steps, but as this part moves, it leaves behind a sequence of other persistent structures. And the result is that the whole structure continues to grow forever, adding progressively more and more cells.

![](Images/_page_303_Picture_2.jpeg)

Unbounded growth in code 1329. The initial condition contains a block of 10 cells. The right-hand side of the pattern repeats every 256 steps, and as it moves it leaves behind an infinite sequence of persistent structures.

initial condition number 54,889

Yet looking at the picture above, one might suppose that when unlimited growth occurs, the pattern produced must be fairly complicated. But once again code 1329 has a surprise in store. For the facing page shows that when one reaches initial condition 97,439 there is again unlimited growth—but now the pattern that is produced is very simple. And in fact if one were just to see this pattern, one would probably assume that it came from a rule whose typical behavior is vastly simpler than code 1329.

![](Images/_page_304_Picture_2.jpeg)

Further examples of unbounded growth in code 1329. Most of the patterns produced are complex—but some are simple.

![](Images/_page_305_Picture_2.jpeg)

A typical example of the behavior of the rule 110 cellular automaton with random initial conditions. The background pattern consists of blocks of 14 cells that repeat every 7 steps.

Indeed, it is a general feature of class 4 cellular automata that with appropriate initial conditions they can mimic the behavior of all sorts of other systems. And when we discuss computation and the notion of universality in Chapter 11 we will see the fundamental reason this ends up being so. But for now the main point is just how diverse and complex the behavior of class 4 cellular automata can be—even when their underlying rules are very simple.

And perhaps the most striking example is the rule 110 cellular automaton that we first saw on page 32. Its rule is extremely simple—involving just nearest neighbors and two colors of cells. But its overall behavior is as complex as any system we have seen.

The facing page shows a typical example with random initial conditions. And one immediate slight difference from other class 4 rules that we have discussed is that structures in rule 110 do not exist on a blank background: instead, they appear as disruptions in a regular repetitive pattern that consists of blocks of 14 cells repeating every 7 steps.

The next page shows the kinds of persistent structures that can be generated in rule 110 from blocks less than 40 cells wide. And just like in other class 4 rules, there are stationary structures and moving structures—as well as structures that can be extended by repeating blocks they contain.

So are there also structures in rule 110 that exhibit unbounded growth? It is certainly not easy to find them. But if one looks at blocks of width 41, then such structures do eventually show up, as the picture on page 293 demonstrates.

So how do the various structures in rule 110 interact? The answer, as pages 294–296 demonstrate, can be very complicated.

In some cases, one structure essentially just passes through another with a slight delay. But often a collision between two structures produces a whole cascade of new structures. Sometimes the outcome of a collision is evident after a few steps. But quite often it takes a very large number of steps before one can tell for sure what is going to happen.

So even though the individual structures in class 4 systems like rule 110 may behave in fairly repetitive ways, interactions between these structures can lead to behavior of immense complexity.

![](Images/_page_307_Figure_1.jpeg)

Persistent structures found in rule 110. Extended versions exist of all but structures (a) and (j). Structures (m) and (n) also exist in alternate forms shifted with respect to the background.

![](Images/_page_308_Picture_2.jpeg)

An example of unbounded growth in rule 110. The initial condition consists of a block of length 41 inserted between blocks of the background. New structures on both left and right are produced every 77 steps; the central structure moves 20 cells to the left during each cycle so that the structures on the left are separated by 37 steps while those on the right are separated by 107 steps.

![](Images/_page_309_Figure_1.jpeg)

Collisions between persistent structures (o) and (j) from page 292. (The first structure is actually an extended form containing four copies of structure (o) from page 292.) Each successive picture shows what happens when the original structures are started progressively further apart.

![](Images/_page_310_Picture_1.jpeg)

Collisions between structures (e) and (o) from page 292.

![](Images/_page_311_Picture_1.jpeg)

A collision between structures (l) and (i) from page 292. It takes more than 4000 steps for the final outcome involving 8 separate structures to become clear. The height of the picture corresponds to 2000 steps, and the third picture ends at step 4300.

![](Images/_page_312_Picture_0.jpeg)
