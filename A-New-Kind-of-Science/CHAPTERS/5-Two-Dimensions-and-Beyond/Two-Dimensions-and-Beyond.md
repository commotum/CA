#### Two Dimensions and Beyond

#### Introduction

The physical world in which we live involves three dimensions of space. Yet so far in this book all the systems we have discussed have effectively been limited to just one dimension.

The purpose of this chapter, therefore, is to see how much of a difference it makes to allow more than one dimension.

At least in simple cases, the basic idea, as illustrated in the pictures below, is to consider systems whose elements do not just lie along a one-dimensional line, but instead are arranged for example on a two-dimensional grid.

![](Images/_page_184_Picture_6.jpeg)

Examples of simple arrangements of elements in one, two and three dimensions. In two dimensions, what is shown is a square grid; triangular and hexagonal grids are also possible. In three dimensions, what is shown is a cubic lattice; various other lattices, analogous to those for regular crystals, are also possible, as are arrangements that are not repetitive.

Traditional science tends to suggest that allowing more than one dimension will have very important consequences. Indeed, it turns out that many of the phenomena that have been most studied in traditional science simply do not occur in just one dimension.

Phenomena that involve geometrical shapes, for example, usually require at least two dimensions, while phenomena that rely on the existence of knotted structures require three dimensions. But what about the phenomenon of complexity? How much does it depend on dimension?

It could be that in going beyond one dimension the character of the behavior that we would see would immediately change. And indeed in the course of this chapter, we will come across many examples of specific effects that depend on having more than one dimension.

But what we will discover in the end is that at an overall level the behavior we see is not fundamentally much different in two or more dimensions than in one dimension. Indeed, despite what we might expect from traditional science, adding more dimensions does not ultimately seem to have much effect on the occurrence of behavior of any significant complexity.

#### Cellular Automata

The cellular automata that we have discussed so far in this book are all purely one-dimensional, so that at each step, they involve only a single line of cells. But one can also consider two-dimensional cellular automata that involve a whole grid of cells, with the color of each cell being updated according to a rule that depends on its neighbors in all four directions on the grid, as in the picture below.

The form of the rule for a typical two-dimensional cellular automaton. In the cases discussed in this section, each cell is either black or white. Usually I consider so-called totalistic rules in which the new color of the center cell depends only on the average of the previous colors of its four neighbors, as well as on its own previous color.

![](Images/_page_185_Picture_9.jpeg)

The pictures below show what happens with an especially simple rule in which a particular cell is taken to become black if any of its four neighbors were black on the previous step.

![](Images/_page_186_Picture_2.jpeg)

Successive steps in the evolution of a two-dimensional cellular automaton whose rule specifies that a particular cell should become black if any of its neighbors were black on the previous step. (In the numbering scheme described on page 173 this rule is code 1022.)

Starting from a single black cell, this rule just yields a uniformly expanding diamond-shaped region of black cells. But by changing the rule slightly, one can obtain more complicated patterns of growth. The pictures below show what happens, for example, with a rule in which each cell becomes black if just one or all four of its neighbors were black on the previous step, but otherwise stays the same color as it was before.

![](Images/_page_186_Picture_5.jpeg)

Steps in the evolution of a two-dimensional cellular automaton whose rule specifies that a particular cell should become black if exactly one or all four of its neighbors were black on the previous step, but should otherwise stay the same color. Starting with a single black cell, this rule yields an intricate, if very regular, pattern of growth. (In the numbering scheme on page 173, the rule is code 942.)

The patterns produced in this case no longer have a simple geometrical form, but instead often exhibit an intricate structure somewhat reminiscent of a snowflake. Yet despite this intricacy, the patterns still show great regularity. And indeed, if one takes the patterns from successive steps and stacks them on top of each other to form a three-dimensional object, as in the picture below, then this object has a very regular nested structure.

![](Images/_page_187_Picture_2.jpeg)

But what about other rules? The facing page and the one that follows show patterns produced by two-dimensional cellular automata with a sequence of different rules. Within each pattern there is often considerable complexity. But this complexity turns out to be very similar to the complexity we have already seen in one-dimensional cellular automata.

![](Images/_page_188_Figure_1.jpeg)

Patterns generated by a sequence of two-dimensional cellular automaton rules. The patterns are produced by starting from a single black square and then running for 22 steps. In each case the base 2 digit sequence for the code number specifies the rule as follows. The last digit specifies what color the center cell should be if all its neighbors were white on the previous step, and it too was white. The second-to-last digit specifies what happens if all the neighbors are white, but the center cell itself is black. And each earlier digit then specifies what should happen if progressively more neighbors are black. (Compare page 60.)

![](Images/_page_189_Figure_1.jpeg)

Patterns generated by two-dimensional cellular automata from the previous page, but now after twice as many steps.

![](Images/_page_190_Figure_1.jpeg)

Evolution of one-dimensional slices through some of the two-dimensional cellular automata from the previous two pages. Each picture shows the colors of cells that lie on the one-dimensional line that goes through the middle of each two-dimensional pattern. The results are strikingly similar to ones we saw in previous chapters in purely one-dimensional cellular automata.

And indeed the previous page shows that if one looks at the evolution of a one-dimensional slice through each two-dimensional pattern the results one gets are strikingly similar to what we have seen in ordinary one-dimensional cellular automata.

But looking at such slices cannot reveal much about the overall shapes of the two-dimensional patterns. And in fact it turns out that for all the two-dimensional cellular automata shown on the last few pages, these shapes are always very regular.

But it is nevertheless possible to find two-dimensional cellular automata that yield less regular shapes. And as a first example, the picture on the facing page shows a rule that produces a pattern whose surface has seemingly random irregularities, at least on a small scale.

In this particular case, however, it turns out that on a larger scale the surface follows a rather smooth curve. And indeed, as the picture on page 178 shows, it is even possible to find cellular automata that yield overall shapes that closely approximate perfect circles.

But it is certainly not the case that all two-dimensional cellular automata produce only simple overall shapes. The pictures on pages 179-181 show one rule, for example, that does not. The rule is actually rather simple: it just states that a particular cell should become black whenever exactly three of its eight neighbors, including diagonals, are black, and otherwise it should stay the same color as it was before.

In order to get any kind of growth with this rule one must start with at least three black cells. The picture at the top of page 179 shows what happens with various numbers of black cells. In some cases the patterns produced are fairly simple, and typically stop growing after just a few steps. But in other cases, much more complicated patterns are produced, which often apparently go on growing forever.

The pictures on page 181 show the behavior produced by starting from a row of eleven black cells, and then evolving for several hundred steps. The shapes obtained seem continually to go on changing, with no simple overall form ever being produced.

And so it seems that there can be great complexity not only in the detailed arrangement of black and white cells in a two-dimensional cellular automaton pattern, but also in the overall shape of the pattern.

![](Images/_page_192_Figure_2.jpeg)

step 200

![](Images/_page_192_Picture_4.jpeg)

A two-dimensional cellular automaton that yields a pattern with a rough surface. The rule used here includes diagonal neighbors, and so involves a total of 8 neighbors for each cell, as indicated in the icon on the left. The rule specifies that the center cell should become black if either 3 or 5 of its 8 neighbors were black on the step before, and should otherwise stay the same color as it was before. The initial condition in the case shown consists of a row of 7 black cells. In an extension to 8 neighbors of the scheme used in the pictures a few pages back, the rule has code number 175850.

![](Images/_page_193_Picture_2.jpeg)

A cellular automaton that yields a pattern whose shape closely approximates a circle. The rule used is of the same kind as on the previous page, but now takes the center cell to become black only if it has exactly 3 black neighbors. If it has 1, 2 or 4 black neighbors then it stays the same color as it was before, and if it has 5 or more black neighbors, then it becomes white on the next step (code number 746). The initial condition consists of a row of 7 black cells, just as in the picture on the previous page. The pattern shown here is the result of 400 steps in the evolution of the system. After t steps, the radius of the approximate circle is about 0.37 t.

![](Images/_page_194_Picture_1.jpeg)

Patterns produced by evolution according to a simple two-dimensional cellular automaton rule starting from rows of black cells of various lengths. The rule used specifies that a particular cell should become black if exactly three out of its eight neighbors (with diagonal neighbors included) are black (code number 174826). The patterns in the picture are obtained by 60 steps of evolution according to this rule. The smaller patterns above have all stopped growing after this number of steps, but many of the other patterns apparently go on growing forever.

So what about three-dimensional cellular automata? It is straightforward to generalize the setup for two-dimensional rules to the three-dimensional case. But particularly on a printed page it is fairly difficult to display the evolution of a three-dimensional cellular automaton in a way that can readily be assimilated.

Pages 182 and 183 do however show a few examples of three-dimensional cellular automata. And just as in the two-dimensional case, there are some specific new phenomena that can be seen. But overall it seems that the basic kinds of behavior produced are just the same as in one and two dimensions. And in particular, the basic phenomenon of complexity does not seem to depend in any crucial way on the dimensionality of the system one looks at.

![](Images/_page_195_Picture_2.jpeg)

![](Images/_page_196_Picture_2.jpeg)

![](Images/_page_196_Picture_3.jpeg)

![](Images/_page_196_Picture_4.jpeg)

![](Images/_page_196_Picture_5.jpeg)

Stages in the evolution of the cellular automaton from the facing page, starting with an initial condition consisting of a row of 11 black cells.

![](Images/_page_197_Picture_1.jpeg)

![](Images/_page_197_Figure_2.jpeg)

Examples of three-dimensional cellular automata. In the top set of pictures, the rule specifies that a cell should become black whenever any of the six neighbors with which it shares a face were black on the step before. In the bottom pictures, the rule specifies that a cell should become black only when exactly one of its six neighbors was black on the step before. In both cases, the initial condition contains a single black cell. In the top pictures, the limiting shape obtained is a regular octahedron. In the bottom pictures, it is a nested pattern analogous to the two-dimensional one on page 171.

![](Images/_page_198_Picture_2.jpeg)

![](Images/_page_198_Picture_3.jpeg)

Further examples of three-dimensional cellular automata, but now with rules that depend on all 26 neighbors that share either a face or a corner with a particular cell. In the top pictures, the rule specifies that a cell should become black when exactly one of its 26 neighbors was black on the step before. In the bottom pictures, the rule specifies that a cell should become black only when exactly two of its 26 neighbors were black on the step before. In the top pictures, the initial condition contains a single black cell; in the bottom pictures, it contains a line of three black cells.

#### Turing Machines

Much as for cellular automata, it is straightforward to generalize Turing machines to two dimensions. The basic idea, shown in the picture below, is to allow the head of the Turing machine to move around on a two-dimensional grid rather than just going backwards and forwards on a one-dimensional tape.

![](Images/_page_199_Figure_3.jpeg)

The three possible orientations of the arrow on this dot correspond to the three possible states of the head. The rule specifies in which of the four possible directions the head should move at each step. Note that the orientation of the arrow representing the state of the head has no direct relationship to directions on the grid, or to which way the head will move at the next step.

When we looked at one-dimensional Turing machines earlier in this book, we found that it was possible for them to exhibit complex behavior, but that such behavior was rather rare.

In going to two dimensions we might expect that complex behavior would somehow immediately become more common. But in fact what we find is that the situation is remarkably similar to one dimension.

For Turing machines with two or three possible states, only repetitive and nested behavior normally seem to occur. With four states, more complex behavior is possible, but it is still rather rare.

The facing page shows some examples of two-dimensional Turing machines with four states. Simple behavior is overwhelmingly the most common. But out of a million randomly chosen rules, there will typically be a few that show complex behavior. Page 186 shows one example where the behavior seems in many respects completely random.

![](Images/_page_200_Figure_2.jpeg)

(a) (step 1000)

![](Images/_page_200_Figure_3.jpeg)

![](Images/_page_200_Figure_4.jpeg)

(c) (step 3000)

![](Images/_page_200_Figure_5.jpeg)

![](Images/_page_200_Figure_6.jpeg)

Examples of patterns produced by two-dimensional Turing machines whose heads have four possible states. In each case, all cells are initially white, and one of the rules given on the left is applied for the specified number of steps. Note that in the later cases shown, the head often visits the same position on the grid many times.

(e) (step 10000)

![](Images/_page_201_Figure_2.jpeg)

100,000 steps

![](Images/_page_201_Figure_4.jpeg)

500,000 steps

The path traced out by the head of the two-dimensional Turing machine with rule (e) from the previous page. There are many seemingly random fluctuations in this path, though in general it tends to grow to the right.

#### Substitution Systems and Fractals

One-dimensional substitution systems of the kind we discussed on page 82 can be thought of as working by progressively subdividing each element they contain into several smaller elements.

One can construct two-dimensional substitution systems that work in essentially the same way, as shown in the pictures below.

![](Images/_page_202_Picture_4.jpeg)

A two-dimensional substitution system in which each square is replaced by four smaller squares at every step according to the rule shown on the left. The pattern generated has a nested form.

The next page gives some more examples of two-dimensional substitution systems. The patterns that are produced are certainly quite intricate. But there is nevertheless great regularity in their overall forms. Indeed, just like patterns produced by one-dimensional substitution systems on page 83, all the patterns shown here ultimately have a simple nested structure.

Why does such nesting occur? The basic reason is that at every step the rules for the substitution system simply replace each black square with several smaller black squares. And on subsequent steps, each of these new black squares is then in turn replaced in exactly the same way, so that it ultimately evolves to produce an identical copy of the whole pattern.

![](Images/_page_203_Figure_2.jpeg)

But in fact there is nothing about this basic process that depends on the squares being arranged in any kind of rigid grid. And the picture below shows what happens if one just uses a simple geometrical rule to replace each black square by two smaller black squares. The result, once again, is that one gets an intricate but highly regular nested pattern.

![](Images/_page_204_Picture_4.jpeg)

![](Images/_page_204_Picture_5.jpeg)

The pattern obtained by starting with a single black square and then at every step replacing each black cell with two smaller black cells according to the simple geometrical rule shown on the left. Note that in applying the rule to a particular square, one must take account of the orientation of that square. The final pattern obtained has an intricate nested structure.

In a substitution system where black squares are arranged on a grid, one can be sure that different squares will never overlap. But if there is just a geometrical rule that is used to replace each black square, then it is possible for the squares produced to overlap, as in the picture on the next page. Yet at least in this example, the overall pattern that is ultimately obtained still has a purely nested structure.

The general idea of building up patterns by repeatedly applying geometrical rules is at the heart of so-called fractal geometry.

![](Images/_page_205_Picture_1.jpeg)

The pattern obtained by repeatedly applying the simple geometrical rule shown on the right. Even though this basic rule does not involve overlapping squares, the pattern obtained even by step 3 already has squares that overlap. But the overall pattern obtained after a large number of steps still has a nested form.

![](Images/_page_205_Picture_3.jpeg)

The pictures on the facing page show several more examples of fractal patterns produced in this way.

The details of the geometrical rules used are different in each case. But what all the rules have in common is that they involve replacing one black square by two or more smaller black squares. And with this kind of setup, it is ultimately inevitable that all the patterns produced must have a completely regular nested structure.

So what does it take to get patterns with more complicated structure? The basic answer, much as we saw in one-dimensional substitution systems on page 85, is some form of interaction between different elements, so that the replacement for a particular element at a given step can depend not only on the characteristics of that element itself, but also on the characteristics of other neighboring elements.

But with geometrical replacement rules of the kind shown on the facing page there is a problem with this. For elements can end up anywhere in the plane, making it difficult to define an obvious notion of neighbors. And the result of this has been that in traditional fractal geometry the idea of interaction between elements is not considered, so that all patterns that are produced have a purely nested form.

![](Images/_page_206_Picture_1.jpeg)

Yet if one sets up elements on a grid it is straightforward to allow the replacements for a given element to depend on its neighbors, as in the picture at the top of the next page. And if one does this, one immediately gets all sorts of fairly complicated patterns that are often not just purely nested, as illustrated in the pictures on the next page.

In Chapter 3 we discussed both ordinary one-dimensional substitution systems, in which every element is replaced at each step, and sequential substitution systems, in which just a single block of elements are replaced at each step. And what we did to find which block of elements should be replaced at a given step was to scan the whole sequence of elements from left to right.

![](Images/_page_207_Figure_1.jpeg)

So how can this be generalized to higher dimensions? On a two-dimensional grid one can certainly imagine snaking backwards and forwards or spiralling outwards to scan all the elements. But as soon as one defines any particular order for elements, however they may be laid out, this in effect reduces one to dealing with a one-dimensional system.

And indeed there seems to be no immediate way to generalize sequential substitution systems to two or more dimensions. In Chapter 9, however, we will see that with more sophisticated ideas it is in fact possible in any number of dimensions to set up substitution systems in which elements are scanned in order, but whatever order is used, the results are in some sense always the same.

#### Network Systems

One feature of systems like cellular automata is that their elements are always set up in a regular array that remains the same from one step to the next. In substitution systems with geometrical replacement rules there is slightly more freedom, but still the elements are ultimately constrained to lie in a two-dimensional plane.

Indeed, in all the systems that we have discussed so far there is in effect always a fixed underlying geometrical structure which remains unchanged throughout the evolution of the system.

It turns out, however, that it is possible to construct systems in which there is no such invariance in basic structure, and in this section I discuss as an example one version of what I will call network systems.

A network system is fundamentally just a collection of nodes with various connections between these nodes, and rules that specify how these connections should change from one step to the next.

At any particular step in its evolution, a network system can be thought of a little like an electric circuit, with the nodes of the network corresponding to the components in the circuit, and the connections to the wires joining these components together.

And as in an electric circuit, the properties of the system depend only on the way in which the nodes are connected together, and not on any specific layout for the nodes that may happen to be used.

Of course, to make a picture of a network system, one has to choose particular positions for each of its nodes. But the crucial point is that these positions have no fundamental significance: they are introduced solely for the purpose of visual representation.

In constructing network systems one could in general allow each node to have any number of connections coming from it. But at least for the purposes of this section nothing fundamental turns out to be lost if one restricts oneself to the case in which every node has exactly two outgoing connections, each of which can then either go to another node, or can loop back to the original node itself.

With this setup the very simplest possible network consists of just one node, with both connections from the node looping back, as in the top picture below. With two nodes, there are already three possible patterns of connections, as shown on the second line below. And as the number of nodes increases, the number of possible different networks grows very rapidly.

![](Images/_page_209_Picture_2.jpeg)

Possible networks formed by having one, two or three nodes, with two connections coming out of each node. The picture shows all inequivalent cases ignoring labels, but excludes networks in which there are nodes which cannot be reached by connections from other nodes.

For most of these networks there is no way of laying out their nodes so as to get a picture that looks like anything much more than a random jumble of wires. But it is nevertheless possible to construct many specific networks that have easily recognizable forms, as shown in the pictures on the facing page.

Each of the networks illustrated at the top of the facing page consists at the lowest level of a collection of identical nodes. But the remarkable fact that we see is that just by changing the pattern of connections between these nodes it is possible to get structures that effectively correspond to arrays with different numbers of dimensions.

![](Images/_page_210_Picture_1.jpeg)

Examples of networks that correspond to arrays in one, two and three dimensions. At an underlying level, each network consists just of a collection of nodes with two connections coming from each node. But by setting up appropriate connections between these nodes it is possible to get structures that effectively correspond to arrays with different numbers of dimensions.

Example (a) shows a network that is effectively one-dimensional. The network consists of pairs of nodes that can be arranged in a sequence in which each pair is connected to one other pair on the left and another pair on the right.

But there is nothing intrinsically one-dimensional about the structure of network systems. And as example (b) demonstrates, it is just a matter of rearranging connections to get a network that looks like a two-dimensional rather than a one-dimensional array. Each individual node in example (b) still has exactly two connections coming out of it, but now the overall pattern of connections is such that every block of nodes is connected to four rather than two neighboring blocks, so that the network effectively forms a two-dimensional square grid.

Example (c) then shows that with appropriate connections, it is also possible to get a three-dimensional array, and indeed using the same principles an array with any number of dimensions can easily be obtained.

The pictures below show examples of networks that form infinite trees rather than arrays. Notice that the first and last networks shown actually have an identical pattern of connections, but they look different here because the nodes are arranged in a different way on the page.

![](Images/_page_211_Picture_3.jpeg)

Examples of networks that correspond to infinite trees. Note that networks (a) and (c) are identical, though they look different because the nodes are laid out differently on the page. All the networks shown are truncated at the leaves of each tree.

In general, there is great variety in the possible structures that can be set up in network systems, and as one further example the picture below shows a network that forms a nested pattern.

![](Images/_page_212_Picture_2.jpeg)

In the pictures above we have seen various examples of individual networks that might exist at a particular step in the evolution of a network system. But now we must consider how such networks are transformed from one step in evolution to the next.

The basic idea is to have rules that specify how the connections coming out of each node should be rerouted on the basis of the local structure of the network around that node.

But to see the effect of any such rules, one must first find a uniform way of displaying the networks that can be produced. The pictures at the top of the next page show one possible approach based on always arranging the nodes in each network in a line across the page. And although this representation can obscure the geometrical structure of a particular network, as in the second and third cases above, it more readily allows comparison between different networks.

![](Images/_page_213_Picture_1.jpeg)

Networks from previous pictures laid out in a uniform way. Network (a) corresponds to a one-dimensional array, (b) to a two-dimensional array, and (c) to a tree. In the layout shown here, all the networks have their nodes arranged along a line. Note that in cases (a) and (b) the connections are arranged so that the arrays effectively wrap around; in case (c) the leaves of the tree are taken to have connections that loop back to themselves.

In setting up rules for network systems, it is convenient to distinguish the two connections that come out of each node. And in the pictures above one connection is therefore always shown going above the line of nodes, while the other is always shown going below.

The pictures on the facing page show examples of evolution obtained with four different choices of underlying rules. In the first case, the rule specifies that the "above" connection from each node should be rerouted so that it leads to the node obtained by following the "below" connection and then the "above" connection from that node. The "below" connection is left unchanged.

The other rules shown are similar in structure, except that in cases (c) and (d), the "above" connection from each node is rerouted so that it simply loops back to the node itself.

In case (d), the result of this is that the network breaks up into several disconnected pieces. And it turns out that none of the rules I consider here can ever reconnect these pieces again. So as a consequence, what I do in the remainder of this section is to track only the piece that includes the first node shown in pictures such as those above. And in effect, this then means that other nodes are dropped from the network, so that the total size of the network decreases.

![](Images/_page_214_Picture_1.jpeg)

The evolution of network systems with four different choices of underlying rules. Successive steps in the evolution are shown on successive lines down the page. In case (a), the "above" connection of each node is rerouted at each step to lead to the node reached by following first the below connection and then the above connection from that node; the below connection is left unchanged. In case (b), the above connection of each node is rerouted to the node reached by following the above connection and then the above connection again; the below connection is left unchanged. In case (c), the above connection of each node is rerouted so as to loop back to the node itself, while the below connection is left unchanged. And in case (d), the above connection is rerouted so as to loop back, while the below connection is rerouted to lead to the node reached by following the above connection.

By changing the underlying rules, however, the number of nodes in a network can also be made to increase. The basic way this can be done is by breaking a connection coming from a particular node by inserting a new node and then connecting that new node to nodes obtained by following connections from the original node.

The pictures on the next page show examples of behavior produced by two rules that use this mechanism. In both cases, a new node is inserted in the "above" connection from each existing node in the network. In the first case, the connections from the new node are exactly the same as the connections from the existing node, while in the second case, the "above" and "below" connections are reversed.

![](Images/_page_215_Picture_3.jpeg)

![](Images/_page_215_Picture_4.jpeg)

Evolution of network systems whose rules involve the addition of new nodes. In both cases, the new nodes are inserted in the "above" connection from each node. In case (a), the connections from the new node lead to the same nodes as the connections from the original node. In case (b), the above and below connections for the new node are reversed. In the pictures above, new nodes are placed immediately after the nodes that give rise to them, and gray lines are used to indicate the origin of each node. Note that the initial conditions consist of a network that contains only a single node.

But in both cases the behavior obtained is quite simple. Yet much like neighbor-independent substitution systems these network systems have the property that exactly the same operation is always performed at each node on every step.

In general, however, one can set up network systems that have rules in which different operations are performed at different nodes, depending on the local structure of the network near each node.

One simple scheme for doing this is based on looking at the two connections that come out of each node, and then performing one operation if these two connections lead to the same node, and another if the connections lead to different nodes.

The pictures on the facing page show some examples of what can happen with this scheme. And again it turns out that the behavior is always quite simple, with the network having a structure that inevitably grows in an essentially repetitive way.

But as soon as one allows dependence on slightly longer-range features of the network, much more complicated behavior immediately becomes possible. And indeed, the pictures on the next two pages show examples of what can happen if the rules are allowed to depend on the number of distinct nodes reached by following not just one but up to two successive connections from each node.

![](Images/_page_216_Figure_1.jpeg)

Examples of network systems with rules that cause different operations to be performed at different nodes. Each rule contains two cases, as shown above. The first case specifies what to do if both connections from a particular node lead to the same node; the second case specifies what to do when they lead to different nodes. In the rules shown, the connections from a particular node (indicated by a solid circle) and from new nodes created from this node always go to the nodes indicated by open circles that are reached by following just a single above or below connection from the original node. Even if this restriction is removed, however, more complicated behavior does not appear to be seen.

With such rules, the sequence of networks obtained no longer needs to form any kind of simple progression, and indeed one finds that even the total number of nodes at each step can vary in a way that seems in many respects completely random.

When we discuss issues of fundamental physics in Chapter 9 we will encounter a variety of other types of network systems, and I suspect that some of these systems will in the end turn out to be closely related to the basic structure of space and spacetime in our universe.

![](Images/_page_217_Figure_1.jpeg)

Network systems in which the rule depends on the number of distinct nodes reached by going up to distance two away from each node. The plots show the total number of nodes obtained at each step. In cases (a) and (b), the behavior of the system is eventually repetitive. In case (c), it is nested, the size of the network at step t is related to the number of 1's in the base 2 digit sequence of t.

![](Images/_page_218_Figure_2.jpeg)

Network systems in which the total number of nodes obtained on successive steps appears to vary in a largely random way forever. About one in 10,000 randomly chosen network systems seem to exhibit the kind of behavior shown here.

#### Multiway Systems

The network systems that we discussed in the previous section do not have any underlying grid of elements in space. But they still in a sense have a simple one-dimensional arrangement of states in time. And in fact, all the systems that we have considered so far in this book can be thought of as having the same simple structure in time. For all of them are ultimately set up just to evolve progressively from one state to the next.

Multiway systems, however, are defined so that they can have not just a single state, but a whole collection of possible states at any given step.

The picture below shows a very simple example of such a system.

A very simple multiway system in which one element in each sequence is replaced at each step by either one or two elements. The main feature of multiway systems is that all the distinct sequences that result are kept.

![](Images/_page_219_Picture_6.jpeg)

Each state in the system consists of a sequence of elements, and in the particular case of the picture above, the rule specifies that at each step each of these elements either remains the same or is replaced by a pair of elements. Starting with a single state consisting of one element, the picture then shows that applying these rules immediately gives two possible states: one with a single element, and the other with two.

Multiway systems can in general use any sets of rules that define replacements for blocks of elements in sequences. We already saw exactly these kinds of rules when we discussed sequential substitution systems on page 88. But in sequential substitution systems the idea was to do just one replacement at each step. In multiway systems, however, the idea is to do all possible replacements at each step, and then to keep all the possible different sequences that are generated.

The pictures below show what happens with some very simple rules. In each of these examples the behavior turns out to be rather simple, with for example the number of possible sequences always increasing uniformly from one step to the next.

![](Images/_page_220_Picture_4.jpeg)

![](Images/_page_220_Picture_5.jpeg)

![](Images/_page_220_Figure_6.jpeg)

Examples of simple multiway systems. The number of distinct sequences at step t in these three systems is respectively Ceiling[t/2], t and Fibonacci[t + 1] (which increases approximately like 1.618^t).

In general, however, this number need not exhibit such uniform growth, and the pictures below show examples where fluctuations occur.

![](Images/_page_220_Figure_9.jpeg)

![](Images/_page_220_Figure_10.jpeg)

![](Images/_page_220_Figure_11.jpeg)

Examples of multiway systems with slightly more complicated behavior. The plots on the right show the total number of possible states obtained at each step, and the differences of these numbers from one step to the next. In both cases, essentially repetitive behavior is seen, every 40 and 161 steps respectively. Note that in case (a), the total number of possible states at step t increases roughly like t^2, while in case (b) it increases only like t.

But in both these cases it turns out to be not too long before these fluctuations essentially repeat. The picture below shows an example where a larger amount of apparent randomness is seen. Yet even in this case one finds that there ends up again being essential repetition, although now only every 1071 steps.

![](Images/_page_221_Figure_2.jpeg)

![](Images/_page_221_Figure_3.jpeg)

A multiway system with behavior that shows some signs of apparent randomness. The rule for this system involves three possible replacements. Note that the first replacement only removes elements and does not insert new ones. In the pictures sequences containing zero elements therefore sometimes appear. At least with the initial condition used here, despite considerable early apparent randomness, the differences in number of elements do repeat (shifted by 1) every 1071 steps.

If one looks at many multiway systems, most either grow exponentially quickly, or not at all; slow growth of the kind seen on the facing page is rather rare. And indeed even when such growth leads to a certain amount of apparent randomness it typically in the end seems to exhibit some form of repetition. If one allows more rapid growth, however, then there presumably start to be all sorts of multiway systems that never show any such regularity. But in practice it tends to be rather difficult to study these kinds of multiway systems, since the number of states they generate quickly becomes too large to handle.

One can get some idea about how such systems behave, however, just by looking at the states that occur at early steps. The picture below shows an example, with ultimately fairly simple nested behavior.

![](Images/_page_222_Picture_3.jpeg)

The collections of states generated on successive steps by a simple multiway system with rapid growth shown on page 205. The particular rule used here eventually generates all states beginning with a white cell. At step t there are Fibonacci[t+1] states; a given state with m white cells and n black cells appears at step 2m+n-1.

The pictures on the next page show some more examples. Sometimes the set of states that get generated at a particular step show essential repetition, though often with a long period. Sometimes this set in effect includes a large fraction of the possible digit sequences of a given length, and so essentially shows nesting. But in other cases there is at least a hint of considerably more complexity, even though the total number of states may still end up growing quite smoothly.

![](Images/_page_223_Figure_1.jpeg)

Looking carefully at the pictures of multiway system evolution on previous pages, a feature one notices is that the same sequences often occur on several different steps. Yet it is a consequence of the basic setup for multiway systems that whenever any particular sequence occurs, it must always lead to exactly the same behavior.

So this means that the complete evolution can be represented as in the picture at the top of the facing page, with each sequence shown explicitly only once, and any sequence generated more than once indicated just by an arrow going back to its first occurrence.

![](Images/_page_224_Picture_2.jpeg)

![](Images/_page_224_Picture_3.jpeg)

The evolution of a multiway system, first with every sequence explicitly shown at each step, and then with every sequence only ever shown once.

But there is no need to arrange the picture like this: for the whole behavior of the multiway system can in a sense be captured just by giving the network of what sequence leads to what other. The picture below shows stages in building up such a network. And what we see is that just as the network systems that we discussed in the previous section can build up their own pattern of connections in space, so also multiway systems can in effect build up their own pattern of connections in time, and this pattern can often be quite complicated.

![](Images/_page_224_Picture_6.jpeg)

The network built up by the evolution of the multiway system from the top of the page. This network in effect represents a network of connections in time between states of the multiway system.

#### Systems Based on Constraints

In the course of this book we have looked at many different kinds of systems. But in one respect all these systems have ultimately been set up in the same basic way: they are all based on explicit rules that specify how the system evolves from step to step.

In traditional science, however, it is common to consider systems that are set up in a rather different way: instead of having explicit rules for evolution, the systems are just given constraints to satisfy.

As a simple example, consider a line of cells in which each cell is colored black or white, and in which the arrangement of colors is subject to the constraint that every cell should have exactly one black and one white neighbor. Knowing only this constraint gives no explicit procedure for working out the color of each cell. And in fact it may at first not be clear that there will be any arrangement of colors that can satisfy the constraint. But it turns out that there is, as shown below.

![](Images/_page_225_Picture_5.jpeg)

A system consisting of a line of black and white cells whose form is defined by the constraint that every cell should have exactly one black and one white neighbor. The pattern shown is the only possible one that satisfies this constraint. The idea of implicitly determining the behavior of a system by giving constraints that it must satisfy is common in traditional science and mathematics.

And having seen this picture, one might then imagine that there must be many other patterns that would also satisfy the constraint. After all, the constraint is local to neighboring cells, so one might suppose that parts of the pattern sufficiently far apart should always be independent. But in fact this is not true, and instead the system works a bit like a puzzle in which there is only one way to fit in each piece. And in the end it is only the perfectly repetitive pattern shown above that can satisfy the required constraint at every cell.

Other constraints, however, can allow more freedom. Thus, for example, with the constraint that every cell must have at least one neighbor whose color is different from its own, any of the patterns in the picture at the top of the facing page are allowed, as indeed is any pattern that involves no more than two successive cells of the same color.

![](Images/_page_226_Picture_2.jpeg)

A system consisting of a line of black and white cells whose form is defined by the constraint that every cell should have at least one neighbor whose color is different from its own. There are many possible arrangements of colors that satisfy this constraint. Some, like the first arrangement above, look quite random. But others, like the second two arrangements above, are simple and repetitive. It turns out that in a one-dimensional system no set of local constraints can force arrangements of more complicated types.

But while the first arrangement of colors shown above looks somewhat random, the last two are simple and purely repetitive.

So what about other choices of constraints? We have seen in this book many examples of systems where simple sets of rules give rise to highly complex behavior. But what about systems based on constraints? Are there simple sets of constraints that can force complex patterns?

It turns out that in one-dimensional systems there are not. For in one dimension it is possible to prove that any local set of constraints that can be satisfied at all can always be satisfied by some simple and purely repetitive arrangement of colors.

But what about two dimensions? The proof for one dimension breaks down in two dimensions, and so it becomes at least conceivable that a simple set of constraints could force a complex pattern to occur.

As a first example of a two-dimensional system, consider an array of black and white cells in which the constraint is imposed that every black cell should have exactly one black neighbor, and every white cell should have exactly two white neighbors.

![](Images/_page_226_Picture_9.jpeg)

A system consisting of a grid of black and white cells defined by the constraint that every black cell should have exactly one black neighbor among its four neighbors, and every white cell should have exactly two white neighbors. The infinite repetitive pattern shown here, together with its rotations and reflections, is the only one that satisfies this constraint. (The picture is assumed to wrap around at each edge.) The pattern can be viewed as a tessellation of 5 x 5 blocks of cells.

As in one dimension, knowing the constraint does not immediately provide a procedure for finding a pattern which satisfies it.

But a little experimentation reveals that the simple repetitive pattern above satisfies the constraint, and in fact it is the only pattern to do so.

![](Images/_page_227_Figure_3.jpeg)

Patterns satisfying constraints which specify that every black cell and every white cell must have a certain fixed number of black and white neighbors. The blank rectangles in the upper right indicate constraints that cannot be satisfied by any pattern whatsoever. Most of the constraints are satisfied by a single pattern, together with its rotations and reflections. In some cases, two distinct patterns are possible, and in a few cases, an infinite set of patterns are possible. In all cases where the constraints can be satisfied at all, a simple repetitive pattern nevertheless suffices.

What about other constraints? The pictures on the facing page show schematically what happens with constraints that require each cell to have various numbers of black and white neighbors.

Several kinds of results are seen. In the two cases shown as blank rectangles on the upper right, there are no patterns at all that satisfy the constraints. But in every other case the constraints can be satisfied, though typically by just one or sometimes two simple infinite repetitive patterns. In the three cases shown in the center a whole range of mixtures of different repetitive patterns are possible. But ultimately, in every case where some pattern can work, a simple repetitive pattern is all that is needed.

So what about more complicated constraints? The pictures below show examples based on constraints that require the local arrangement of colors around every cell to match a fixed set of possible templates.

![](Images/_page_228_Figure_5.jpeg)

Systems specified by the constraint that the local arrangement of colors around every cell must match the fixed set of possible templates shown. Note that these templates apply to every cell, with templates of neighboring cells overlapping. Pattern (a) can be viewed as formed from a tessellation of 5 x 10 blocks of cells; pattern (b) from a tessellation of 24 x 24 blocks. With the numbering scheme for constraints used on the next two pages the cases shown here correspond to 1384774 and 328778790.

There are a total of 4,294,967,296 possible sets of such templates. And of these, 766,979,044 lead to constraints that cannot be satisfied by any pattern. But among the 3,527,988,252 that remain, it turns out that every single one can be satisfied by a simple repetitive pattern. In fact the number of different repetitive patterns that are ever needed is quite small: if a particular constraint can be satisfied by any pattern, then one of the set of 171 repetitive patterns on the next two pages is always sufficient.

![](Images/_page_229_Picture_1.jpeg)

![](Images/_page_230_Figure_2.jpeg)

The complete collection of all 171 patterns needed to satisfy constraints of the type shown on the previous page. If none of these 171 patterns satisfy a particular constraint, then it follows that no pattern at all will satisfy the constraint. The patterns are labelled by numbers which specify the minimal constraint which requires the given pattern. Patterns differing by overall reflection, rotation or interchange of black and white are not shown.

So how can one force more complex patterns to occur?

The basic answer is that one must extend at least slightly the kinds of constraints that one considers. And one way to do this is to require not only that the colors around each cell match a set of templates, but also that a particular template from this set must appear at least somewhere in the array of cells.

The pictures below show a few examples of patterns determined by constraints of this kind. A typical feature is that the patterns are divided into several separate regions, often emanating from some kind of center. But at least in all the examples below, the patterns that occur in each individual region are still simple and repetitive.

![](Images/_page_231_Picture_4.jpeg)

Examples of patterns produced by systems in which not only must the arrangement of colors in each neighborhood match one of a fixed set of templates, but also a certain template from this set must occur at least once in the pattern. The constraints are numbered as before, and in each picture the template that must occur is shown at the center. Constraint 1125528937 leads to a pattern that repeats in 98 x 98 blocks. The last pattern shown is also repetitive, repeating every 56 cells on the diagonal.

So how can one find constraints that force more complex patterns? To do so has been fairly difficult, and in fact has taken almost as much computational effort as any other single result in this book.

The basic problem is that given a constraint it can be extremely difficult to find out what pattern, if any, will satisfy the constraint.

In a system like a cellular automaton that is based on explicit rules, it is always straightforward to take the rule and apply it to see what pattern is produced. But in a system that is based on constraints, there is no such direct procedure, and instead one must in effect always go outside of the system to work out what patterns can occur.

The most straightforward approach might just be to enumerate every single possible pattern and then see which, if any, of them satisfy a particular constraint. But in systems containing more than just a few cells, the total number of possible patterns is absolutely astronomical, and so enumerating them becomes completely impractical.

A more practical alternative is to build up patterns iteratively, starting with a small region, and then adding new cells in essentially all possible ways, at each stage backtracking if the constraint for the system does not end up being satisfied.

The pictures on the next page show a few sequences of patterns produced by this method. In some cases, there emerge quite quickly simple repetitive patterns that satisfy the constraint. But in other cases, a huge number of possibilities have to be examined in order to find any suitable pattern.

And what if there is no pattern at all that can satisfy a particular constraint? One might think that to demonstrate this would effectively require examining every conceivable pattern on the infinite grid of cells. But in fact, if one can show that there is no pattern that satisfies the constraint in a limited region, then this proves that no pattern can satisfy the constraint on the whole grid. And indeed for many constraints, there are already quite small regions for which it is possible to establish that no pattern can be found.

But occasionally, as in the third picture on the next page, one runs into constraints that can be satisfied for regions containing thousands of cells, but not for the whole grid. And to analyze such cases inevitably requires examining huge numbers of possible patterns.

But with an appropriate collection of tricks, it is in the end feasible to take almost any system of the type discussed here, and determine what pattern, if any, satisfies its constraint.

So what kinds of patterns can be needed? In the vast majority of cases, simple repetitive patterns, or mixtures of such patterns, are the only ones that are needed.

![](Images/_page_233_Figure_1.jpeg)

Stages in finding patterns that satisfy constraints (a) 4670324, (b) 373384574, and (c) 387520105. Gray is used to indicate cells whose colors have not yet been determined. The first stage shown in each case corresponds to cells whose colors can be deduced immediately from the presence of a particular template at the center. In case (a) choices for additional cells can be made straightforwardly, and an infinite regular pattern can be built up without any backtracking. In case (b), many choices for additional cells have to be tried, with much backtracking, and in the end the automatic procedure fails to find a repetitive pattern. Nevertheless, as the last stage demonstrates, a repetitive pattern does in fact exist. In case (c), the automatic procedure finds a fairly large and almost regular pattern that satisfies the constraints, but in this case it turns out that no infinite pattern exists.

But if one systematically examines possible constraints in the order shown on pages 214 and 215, then it turns out that after examining more than 18 million of them, one finally discovers the system shown on the facing page. And in this system, unlike all others before it, no repetitive pattern is possible; the only pattern that satisfies the constraint is the non-repetitive nested pattern shown in the picture.

After testing millions of constraints, and tens of billions of candidate patterns, therefore, it is finally possible to establish that a system based on simple constraints of the type discussed here can be forced to exhibit behavior more complex than pure repetition.

![](Images/_page_234_Figure_2.jpeg)

The simplest system based on constraints that is forced to exhibit a non-repetitive pattern. The constraint requires that the arrangement of colors around each cell must match one of the 12 templates shown, and that at least somewhere in the pattern a template containing a pair of stacked black cells must occur. In the numbering scheme used on preceding pages, the constraint is number 18762389. The pattern shown is unique, in that no variations of it, except for trivial translations, will satisfy the constraints. The nested structure on the diagonal essentially corresponds to a progression of base 2 digit sequences for positive and negative numbers.

What about still more complex behavior?

There are altogether 137,438,953,472 constraints of the type shown on page 216. And of the millions of these that I have tested, none have forced anything more complicated than the kind of nested behavior seen on the previous page. But if one extends again the type of constraints one considers, it turns out to become possible to construct examples that force more complex behavior.

The idea is to set up templates that involve complete 3 x 3 blocks of cells, including diagonal neighbors. The picture below then shows an example of such a system, in which by allowing only a specific set of 33 templates, a nested pattern is forced to occur.

![](Images/_page_235_Picture_4.jpeg)

An example of a system based on a constraint involving 3 x 3 templates of cells. In this particular system, only the 33 templates shown above (out of the 512 possible ones) are allowed to occur. This constraint, together with the requirement that the first template must appear at least somewhere, then turns out to force a nested pattern to occur. The system shown was specifically constructed in correspondence with the rule 60 elementary one-dimensional cellular automaton.

![](Images/_page_235_Picture_6.jpeg)

What about more complex patterns? Searches have not succeeded in finding anything. But explicit construction, based on correspondence with one-dimensional cellular automata, leads to the example shown at the top of the facing page: a system with 56 allowed templates in which the only pattern satisfying the constraint is a complex and largely random one, derived from the rule 30 cellular automaton.

![](Images/_page_236_Picture_1.jpeg)

![](Images/_page_236_Picture_2.jpeg)

A system based on a constraint, in which a complex and largely random pattern is forced to occur. The constraint specifies that only the 56 3 x 3 templates shown at left can occur anywhere in the pattern, with the first template appearing at least once. The pattern required to satisfy this constraint corresponds to a shifted version of the one generated by the evolution of the rule 30 elementary one-dimensional cellular automaton.

So finally this shows that it is indeed possible to force complex behavior to occur in systems based on constraints. But from what we have seen in this section such behavior appears to be quite rare: unlike many of the simple rules that we have discussed in this book, it seems that almost all simple constraints lead only to fairly simple patterns.

Any phenomenon based on rules can always ultimately also be described in terms of constraints. But the results of this section indicate that these descriptions can have to be fairly complicated for complex behavior to occur. So the fact that traditional science and mathematics tends to concentrate on equations that operate like constraints provides yet another reason for their failure to identify the fundamental phenomenon of complexity that I discuss in this book.
