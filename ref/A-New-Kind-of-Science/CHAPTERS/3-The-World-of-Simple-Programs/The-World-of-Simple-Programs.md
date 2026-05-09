#### The World of Simple Programs

#### The Search for General Features

At the beginning of the last chapter we asked the basic question of what simple programs typically do. And as a first step towards answering this question we looked at several specific examples of a class of programs known as cellular automata.

The basic types of behavior that we found are illustrated in the pictures on the next page. In the first of these there is pure repetition, and a very simple pattern is formed. In the second, there are many intricate details, but at an overall level there is still a very regular nested structure that emerges.

In the third picture, however, one no longer sees such regularity, and instead there is behavior that seems in many respects random. And finally in the fourth picture there is what appears to be still more complex behavior—with elaborate localized structures being generated that interact in complex ways.

At the outset there was no indication that simple programs could ever produce behavior so diverse and often complex. But having now seen these examples, the question becomes how typical they are. Is it only cellular automata with very specific underlying rules that produce such behavior? Or is it in fact common in all sorts of simple programs?

My purpose in this chapter is to answer this question by looking at a wide range of different kinds of programs. And in a sense my

![](Images/_page_67_Picture_1.jpeg)

Four basic examples from the previous chapter of behavior produced by cellular automata with simple underlying rules. In each case, the most obvious features that are seen are different. Note that all the pictures are shown on the same scale; the last picture appears coarser because the structures it contains are larger.

approach is to work like a naturalist—exploring and studying the various forms that exist in the world of simple programs.

I start by considering more general cellular automata, and then I go on to consider a whole sequence of other kinds of programs—with underlying structures further and further away from the array of black and white cells in the cellular automata of the previous chapter.

And what I discover is that whatever kind of underlying rules one uses, the behavior that emerges turns out to be remarkably similar to the basic examples that we have already seen in cellular automata.

Throughout the world of simple programs, it seems, there is great universality in the types of overall behavior that can be produced. And in a sense it is ultimately this that makes it possible for me to construct the coherent new kind of science that I describe in this book—and to use it to elucidate a large number of phenomena, independent of the particular details of the systems in which they occur.

#### More Cellular Automata

The pictures below show the rules used in the four cellular automata on the facing page. The overall structure of these rules is the same in each case; what differs is the specific choice of new colors for each possible combination of previous colors for a cell and its two neighbors.

![](Images/_page_68_Picture_3.jpeg)

The rules used for the four examples of cellular automata on the facing page. In each case, these specify the new color of a cell for each possible combination of colors of that cell and its immediate neighbors on the previous step. The rules are numbered according to the scheme described below.

There turn out to be a total of 256 possible sets of choices that can be made. And following my original work on cellular automata these choices can be numbered from 0 to 255, as in the picture below.

The sequence of 256 possible cellular automaton rules of the kind shown above. As indicated, the rules can conveniently be numbered from 0 to 255. The number assigned is such that when written in base 2, it gives a sequence of 0's and 1's that correspond to the sequence of new colors chosen for each of the eight possible cases covered by the rule.

![](Images/_page_68_Figure_7.jpeg)

But how do cellular automata with all these different rules behave? The next page shows a few examples in detail, while the following two pages show what happens in all 256 possible cases.

At first, the diversity of what one sees is a little overwhelming. But on closer investigation, definite themes begin to emerge.

In the very simplest cases, all the cells in the cellular automaton end up just having the same color after one step. Thus, for example, in

Evolution of cellular automata with a sequence of different possible rules, starting in all cases from a single black cell.

![](Images/_page_70_Picture_2.jpeg)

![](Images/_page_71_Picture_2.jpeg)

rules 0 and 128 all the cells become white, while in rule 255 all of them become black. There are also rules such as 7 and 127 in which all cells alternate between black and white on successive steps.

But among the rules shown on the last few pages, the single most common kind of behavior is one in which a pattern consisting of a single cell or a small group of cells persists. Sometimes this pattern remains stationary, as in rules 4 and 123. But in other cases, such as rules 2 and 103, it moves to the left or right.

It turns out that the basic structure of the cellular automata discussed here implies that the maximum speed of any such motion must be one cell per step. And in many rules, this maximum speed is achieved—although in rules such as 3 and 103 the average speed is instead only half a cell per step.

In about two-thirds of all the cellular automata shown on the last few pages, the patterns produced remain of a fixed size. But in about one-third of cases, the patterns instead grow forever. Of such growing patterns, the simplest kind are purely repetitive ones, such as those seen in rules 50 and 109. But while repetitive patterns are by a small margin the most common kind, about 14% of all the cellular automata shown yield more complicated kinds of patterns.

The most common of these are nested patterns, like those on the next page. And it turns out that although 24 rules in all yield such nested patterns, there are only three fundamentally different forms that occur. The simplest and by far the most common is the one exemplified by rules 22 and 60. But as the pictures on the next page show, other nested forms are also possible. (In the case of rule 225, the width of the overall pattern does not grow at a fixed rate, but instead is on average proportional to the square root of the number of steps.)

<sup>◆</sup> The behavior of all 256 possible cellular automata with rules involving two colors and nearest neighbors. In each case, thirty steps of evolution are shown, starting from a single black cell. Note that some of the rules are related just by interchange of left and right or black and white (e.g. rules 2 and 16 or rules 126 and 129). There are 88 fundamentally inequivalent such elementary rules.

![](Images/_page_73_Figure_1.jpeg)

Examples of cellular automata that produce nested or fractal patterns. Rule 22—like rule 90 from page 26—gives a pattern with fractal dimension  $Log[2, 3] \approx 1.59$ ; rule 150 gives one with fractal dimension  $Log[2, 1 + \sqrt{5} ] \approx 1.69$ . The width of the pattern obtained from rule 225 increases like the square root of the number of steps.

Repetition and nesting are widespread themes in many cellular automata. But as we saw in the previous chapter, it is also possible for cellular automata to produce patterns that seem in many respects random. And out of the 256 rules discussed here, it turns out that 10 yield such apparent randomness. There are three basic forms, as illustrated on the facing page.

Examples of cellular automata that produce patterns with many apparently random features. Three hundred steps of evolution are shown, starting in each case from a single black cell.

![](Images/_page_74_Picture_1.jpeg)

![](Images/_page_74_Picture_2.jpeg)

![](Images/_page_74_Picture_3.jpeg)

rule 45

![](Images/_page_74_Picture_5.jpeg)

rule 73

Beyond randomness, the last example in the previous chapter was rule 110: a cellular automaton whose behavior becomes partitioned into a complex mixture of regular and irregular parts. This particular cellular automaton is essentially unique among the 256 rules considered here: of the four cases in which such behavior is seen, all are equivalent if one just interchanges the roles of left and right or black and white.

So what about more complicated cellular automaton rules?

The 256 "elementary" rules that we have discussed so far are by most measures the simplest possible—and were the first ones I studied. But one can for example also look at rules that involve three colors, rather than two, so that cells can be not only black and white, but also gray. The total number of possible rules of this kind turns out to be immense—7,625,597,484,987 in all—but by considering only so-called "totalistic" ones, the number becomes much more manageable.

The idea of a totalistic rule is to take the new color of each cell to depend only on the average color of neighboring cells, and not on their individual colors. The picture below shows one example of how this works. And with three possible colors for each cell, there are 2187 possible totalistic rules, each of which can conveniently be identified by a code number as illustrated in the picture. The facing page shows a representative sequence of such rules.

Example of a totalistic cellular automaton with three possible colors for each cell. The rule is set up so that the new color of every cell is determined by the average of the previous colors of the cell and its immediate neighbors. With 0 representing white, 1 gray and 2 black, the rightmost element of the rule gives the result for average color 0, while the element immediately to its left gives the result for average color 1/3—and so on. Interpreting the sequence of new colors as a sequence of base 3 digits, one can assign a code number to each totalistic rule.

![](Images/_page_75_Figure_6.jpeg)

We might have expected that by allowing three colors rather than two we would immediately get noticeably more complicated behavior.

![](Images/_page_76_Figure_2.jpeg)

A sequence of totalistic cellular automata with three possible colors for each cell. Although their basic rules are more complicated, the cellular automata shown here do not seem to have fundamentally more complicated behavior than the two-color cellular automata shown on previous pages. Note that in the sequence of rules shown here, those that change the white background are not included. The symmetry of all the patterns is a consequence of the basic structure of totalistic rules. But in fact the behavior we see on the previous page is not unlike what we already saw in many elementary cellular automata a few pages back. Having more complicated underlying rules has not, it seems, led to much greater complexity in overall behavior.

And indeed, this is a first indication of an important general phenomenon: that at least beyond a certain point, adding complexity to the underlying rules for a system does not ultimately lead to more complex overall behavior. And so for example, in the case of cellular automata, it seems that all the essential ingredients needed to produce even the most complex behavior already exist in elementary rules.

Using more complicated rules may be convenient if one wants, say, to reproduce the details of particular natural systems, but it does not add fundamentally new features. Indeed, looking at the pictures on the previous page one sees exactly the same basic themes as in elementary cellular automata. There are some patterns that attain a definite size, then repeat forever, as shown below, others that continue to grow, but have a repetitive form, as at the top of the facing page, and still others that produce nested or fractal patterns, as at the bottom of the page.

Examples of three-color totalistic rules that yield patterns which attain a certain size, then repeat forever. The maximum repetition period is found to be 78 steps, and is achieved by the rule with code number 1329. In the pictures shown here and on the following pages, the initial condition used contains a single gray cell.

![](Images/_page_77_Figure_6.jpeg)

![](Images/_page_78_Figure_2.jpeg)

Examples of three-color totalistic rules that yield patterns which grow forever but have a fundamentally repetitive structure.

![](Images/_page_78_Figure_4.jpeg)

Examples of three-color totalistic rules which yield nested patterns. In most cases, these patterns have an overall form that is similar to what was found with two-color rules. But code 420, for example, yields a pattern with a slightly different structure.

![](Images/_page_79_Picture_2.jpeg)

Examples of three-color totalistic rules that yield patterns with seemingly random features. Three hundred steps of evolution are shown in each case.

In detail, some of the patterns are definitely more complicated than those seen in elementary rules. But at the level of overall behavior, there are no fundamental differences. And in the case of nested patterns even the specific structures seen are usually the same as for elementary rules. Thus, for example, the structure in codes 237 and 948 is the most common, followed by the one in code 1749. The only new structure not already seen in elementary rules is the one in code 420—but this occurs only quite rarely.

About 85% of all three-color totalistic cellular automata produce behavior that is ultimately quite regular. But just as in elementary cellular automata, there are some rules that yield behavior that seems in many respects random. A few examples of this are given on the facing page.

Beyond fairly uniform random behavior, there are also cases similar to elementary rule 110 in which definite structures are produced that interact in complicated ways. The next page gives a few examples. In the first case shown, the pattern becomes repetitive after about 150 steps. In the other two cases, however, it is much less clear what will ultimately happen. The following pages continue these patterns for 3000 steps. But even after this many steps it is still quite unclear what the final behavior will be.

Looking at pictures like these, it is at first difficult to believe that they can be generated just by following very simple underlying cellular automaton rules. And indeed, even if one accepts this, there is still a tendency to assume that somehow what one sees must be a consequence of some very special feature of cellular automata.

As it turns out, complexity is particularly widespread in cellular automata, and for this reason it is fortunate that cellular automata were the very first systems that I originally decided to study.

But as we will see in the remainder of this chapter, the fundamental phenomena that we discovered in the previous chapter are in no way restricted to cellular automata. And although cellular automata remain some of the very best examples, we will see that a vast range of utterly different systems all in the end turn out to exhibit extremely similar types of behavior.

![](Images/_page_81_Picture_1.jpeg)

![](Images/_page_81_Picture_2.jpeg)

![](Images/_page_81_Picture_3.jpeg)

Examples of three-color totalistic rules with highly complex behavior showing a mixture of regularity and irregularity. The partitioning into identifiable structures is similar to what we saw in rule 110 on page 32.

![](Images/_page_82_Picture_1.jpeg)

code 1635

![](Images/_page_83_Picture_1.jpeg)

code 2049

The pictures below show totalistic cellular automata whose overall patterns of growth seem, at least at first, quite complicated. But it turns out that after only about 100 steps, three out of four of these patterns have resolved into simple forms.

![](Images/_page_84_Picture_2.jpeg)

Examples of rules that yield patterns which seem to be on the edge between growth and extinction. For all but code 1599, the fate of these patterns in fact becomes clear after less than 100 steps. A total of 250 steps are shown here.

The one remaining pattern is, however, much more complicated. As shown on the next page, for several thousand steps it simply grows, albeit somewhat irregularly. But then its growth becomes slower. And inside the pattern parts begin to die out. Yet there continue to be occasional bursts of growth. But finally, after a total of 8282 steps, the pattern resolves into 31 simple repetitive structures.

<sup>◀</sup> Three thousand steps in the evolution of the last two cellular automata from page 66. Despite the simplicity of their underlying rules, the final patterns produced show immense complexity. In neither case is it clear what the final outcome will be—whether apparent randomness will take over, or whether a simple repetitive form will emerge.

![](Images/_page_85_Picture_2.jpeg)

Nine thousand steps in the evolution of the three-color totalistic cellular automaton with code number 1599. Starting from a single gray cell, each column corresponds to 3000 steps. The outcome of the evolution finally becomes clear after 8282 steps, when the pattern resolves into 31 simple repetitive structures.

#### **Mobile Automata**

One of the basic features of a cellular automaton is that the colors of all the cells it contains are updated in parallel at every step in its evolution.

But how important is this feature in determining the overall behavior that occurs? To address this question, I consider in this section a class of systems that I call "mobile automata".

Mobile automata are similar to cellular automata except that instead of updating all cells in parallel, they have just a single "active cell" that gets updated at each step, and then they have rules that specify how this active cell should move from one step to the next.

The picture below shows an example of a mobile automaton. The active cell is indicated by a black dot. The rule applies only to this active cell. It looks at the color of the active cell and its immediate neighbors, then specifies what the new color of the active cell should be, and whether the active cell should move left or right.

![](Images/_page_86_Picture_7.jpeg)

![](Images/_page_86_Picture_8.jpeg)

An example of a mobile automaton. Like a cellular automaton, a mobile automaton consists of a line of cells, with each cell having two possible colors. But unlike a cellular automaton, a mobile automaton has only one "active cell" (indicated here by a black dot) at any particular step. The rule for the mobile automaton specifies both how the color of this active cell should be updated, and whether it should move to the left or right. The result of evolution for a larger number of steps with the particular rule shown here is given as example (f) on the next page.

Much as for cellular automata, one can enumerate all possible rules of this kind; it turns out that there are 65,536 of them. The pictures at the top of the next page show typical behavior obtained with such rules. In cases (a) and (b), the active cell remains localized to a small region, and the behavior is very simple and repetitive. Cases (c) through (f) are similar,

![](Images/_page_87_Figure_2.jpeg)

Examples of mobile automata with various rules. In cases (a) through (f) the motion of the active cell is purely repetitive. In cases (g) and (h) it is not. The width of the pattern in these cases after t steps grows roughly like  $\sqrt{2t}$ .

except that the whole pattern shifts systematically to the right, and in cases (e) and (f) a sequence of stripes is left behind.

But with a total of 218 out of the 65,536 possible rules, one gets somewhat different behavior, as cases (g) and (h) above show. The active cell in these cases does not move in a strictly repetitive way, but instead sweeps backwards and forwards, going progressively further every time.

The overall pattern produced is still quite simple, however. And indeed in the compressed form below, it is purely repetitive.

![](Images/_page_87_Picture_7.jpeg)

Compressed versions of the evolution of mobile automata (g) and (h) above, obtained by showing only those steps at which the active cell is further to the left or right than it has ever been before.

Of the 65,536 possible mobile automata with rules of the kind discussed so far it turns out that not a single one shows more complex behavior. So can such behavior then ever occur in mobile automata?

One can extend the set of rules one considers by allowing not only the color of the active cell itself but also the colors of its immediate neighbors to be updated at each step. And with this extension, there are a total of 4,294,967,296 possible rules.

If one samples these rules at random, one finds that more than 99% of them just yield simple repetitive behavior. But once in every few thousand rules, one sees behavior of the kind shown below—that is not purely repetitive, but instead has a kind of nested structure.

![](Images/_page_88_Picture_5.jpeg)

![](Images/_page_88_Picture_6.jpeg)

A mobile automaton with slightly more complicated rules that yields a nested pattern. Each column on the left shows 200 steps in the mobile automaton evolution. The compressed form of the pattern is based on a total of 8000 steps.

![](Images/_page_88_Picture_8.jpeg)

The overall pattern is nevertheless still very regular. But after searching through perhaps 50,000 rules, one finally comes across a rule of the kind shown below—in which the compressed pattern exhibits very much the same kind of apparent randomness that we saw in cellular automata like rule 30.

![](Images/_page_89_Picture_3.jpeg)

A mobile automaton that yields a pattern with seemingly random features. The motion of the active cell is still quite regular, as the picture on the right shows. But when viewed in compressed form, as below, the overall pattern of colors seems in many respects random. Each column on the right shows 200 steps of evolution; the compressed form below corresponds to 50,000 steps.

![](Images/_page_89_Picture_5.jpeg)

![](Images/_page_89_Picture_6.jpeg)

But even though the final pattern left behind by the active cell in the picture above seems in many respects random, the motion of the active cell itself is still quite regular. So are there mobile automata in which the motion of the active cell is also seemingly random? At first, I believed that there might not be. But after searching through a few million rules, I finally found the example shown on the facing page.

![](Images/_page_90_Figure_2.jpeg)

![](Images/_page_90_Figure_3.jpeg)

![](Images/_page_90_Figure_4.jpeg)

A mobile automaton in which the position of the active cell moves in a seemingly random way. Each column above shows 400 steps; the compressed form corresponds to 50,000 steps. It took searching through a few million mobile automata to find one with behavior as complex as what we see here.

Despite the fact that mobile automata update only one cell at a time, it is thus still possible for them to produce behavior of great complexity. But while we found that such behavior is quite common in cellular automata, what we have seen in this section indicates that it is rather rare in mobile automata.

One can get some insight into the origin of this difference by studying a class of generalized mobile automata, that in a sense interpolate between ordinary mobile automata and cellular automata.

The basic idea of such generalized mobile automata is to allow more than one cell to be active at a time. And the underlying rule is then typically set up so that under certain circumstances an active cell can split in two, or can disappear entirely.

Thus in the picture below, for example, new active cells end up being created every few steps.

![](Images/_page_91_Figure_6.jpeg)

A generalized mobile automaton in which any number of cells can be active at a time. The rule given above is applied to every cell that is active at a particular step. In many cases, the rule specifies just that the active cell should move to the left or right. But in some cases, it specifies that the active cell should split in two, thereby creating an additional active cell.

![](Images/_page_91_Figure_8.jpeg)

If one chooses generalized mobile automata at random, most of them will produce simple behavior, as shown in the first few pictures on the facing page. But in a few percent of all cases, the behavior is much more complicated. Often the arrangement of active cells is still quite regular, although sometimes it is not.

But looking at many examples, a certain theme emerges: complex behavior almost never occurs except when large numbers of cells are active at the same time. Indeed there is, it seems, a significant correlation between overall activity and the likelihood of complex behavior. And this is part of why complex behavior is so much more common in cellular automata than in mobile automata.

![](Images/_page_92_Figure_1.jpeg)

Examples of generalized mobile automata with various rules. In case (a), only a limited number of cells ever become active. But in all the other cases shown active cells proliferate forever. In case (d), almost all cells are active, and the system operates essentially like a cellular automaton. In the remaining cases somewhat complicated patterns of cells are active. Note that unlike in ordinary mobile automata, examples of complex behavior like those shown here are comparatively easy to find.

#### **Turing Machines**

In the history of computing, the first widely understood theoretical computer programs ever constructed were based on a class of systems now called Turing machines.

Turing machines are similar to mobile automata in that they consist of a line of cells, known as the "tape", together with a single active cell, known as the "head". But unlike in a mobile automaton, the head in a Turing machine can have several possible states, represented by several possible arrow directions in the picture below.

And in addition, the rule for a Turing machine can depend on the state of the head, and on the color of the cell at the position of the head, but not on the colors of any neighboring cells.

![](Images/_page_93_Picture_5.jpeg)

![](Images/_page_93_Picture_6.jpeg)

An example of a Turing machine. Like a mobile automaton, the Turing machine has one active cell or "head", but now the head has several possible states, indicated by the directions of the arrows in this picture.

Turing machines are still widely used in theoretical computer science. But in almost all cases, one imagines constructing examples to perform particular tasks, with a huge number of possible states and a huge number of possible colors for each cell.

But in fact there are non-trivial Turing machines that have just two possible states and two possible colors for each cell. The pictures on the facing page show examples of some of the 4096 machines of this kind. Both repetitive and nested behavior are seen to occur, though nothing more complicated is found.

![](Images/_page_94_Figure_1.jpeg)

Examples of Turing machines with two possible states for the head. There are a total of 4096 rules of this kind. Repetitive and nested patterns are seen, but nothing more complicated ever occurs.

From our experience with mobile automata, however, we expect that there should be Turing machines that have more complex behavior.

With three states for the head, there are about three million possible Turing machines. But while some of these give behavior that looks slightly more complicated in detail, as in cases (a) and (b) on the next page, all ultimately turn out to yield just repetitive or nested patterns—at least if they are started with all cells white.

With four states, however, more complicated behavior immediately becomes possible. Indeed, in about five out of every million rules of this kind, one gets patterns with features that seem in many respects random, as in the pictures on the next two pages.

So what happens if one allows more than four states for the head? It turns out that there is almost no change in the kind of behavior one sees. Apparent randomness becomes slightly more common, but otherwise the results are essentially the same.

Once again, it seems that there is a threshold for complex behavior—that is reached as soon as one has at least four states. And just as in cellular automata, adding more complexity to the underlying rules does not yield behavior that is ultimately any more complex.

![](Images/_page_95_Figure_2.jpeg)

Examples of Turing machines with three and four possible states. With three possible states, only repetitive and nested patterns are ever ultimately produced, at least starting with all cells white. But with four states, more complicated patterns are generated. The top set of pictures show the first 150 steps of evolution according to various different rules, starting with the head in the first state (arrow pointing up), and all cells white. The bottom set of pictures show the evolution in each case in a compressed form. Each of these pictures includes the first 50 steps at which the head is further to the left or right than it has ever been before.

![](Images/_page_96_Picture_2.jpeg)

![](Images/_page_96_Picture_3.jpeg)

![](Images/_page_96_Picture_4.jpeg)

A Turing machine that exhibits behavior which seems in many respects random. The Turing machine has four possible states for its head, and two possible colors for each cell on its tape. It starts with all cells white, corresponding to a blank tape. Each column above shows 250 steps of evolution; the compressed form on the left corresponds to a total of 20,000 steps.

#### **Substitution Systems**

One of the features that cellular automata, mobile automata and Turing machines all have in common is that at the lowest level they consist of a fixed array of cells. And this means that while the colors of these cells can be updated according to a wide range of different possible rules, the underlying number and organization of cells always stays the same.

Substitution systems, however, are set up so that the number of elements can change. In the typical case illustrated below, one has a sequence of elements—each colored say black or white—and at each step each one of these elements is replaced by a new block of elements.

In the simple cases shown, the rules specify that each element of a particular color should be replaced by a fixed block of new elements, independent of the colors of any neighboring elements.

![](Images/_page_97_Picture_6.jpeg)

![](Images/_page_97_Picture_7.jpeg)

Examples of substitution systems with two possible kinds of elements, in which at every step each kind of element is replaced by a fixed block of new elements. In the first case shown, the total number of elements obtained doubles at every step; in the second case, it follows a Fibonacci sequence, and increases by a factor of roughly  $(1 + \sqrt{5})/2 \approx 1.618$  at every step. The two substitution systems shown here correspond to the second and third examples in the pictures on the following two pages.

And with these kinds of rules, the total number of elements typically grows very rapidly, so that pictures like those above quickly become rather unwieldy. But at least for these kinds of rules, one can make clearer pictures by thinking of each step not as replacing every element by a sequence of elements that are drawn the same size, but rather of subdividing each element into several that are drawn smaller.

In the cases on the facing page, I start from a single element represented by a long box going all the way across the picture. Then on successive steps the rules for the substitution system specify how each box should be subdivided into a sequence of shorter and shorter boxes.

![](Images/_page_98_Figure_2.jpeg)

Examples of substitution systems in which every element is drawn as being subdivided into a sequence of new elements at each step. In all cases the overall patterns obtained can be seen to have a very regular nested form. Rule (b) gives the so-called Thue-Morse sequence, which we will encounter many times in this book. Rule (c) is related to the Fibonacci sequence. Rule (d) gives a version of the Cantor set.

The pictures at the top of the next page show a few more examples. And what we see is that in all cases there is obvious regularity in the patterns produced. Indeed, if one looks carefully, one can see that every pattern just consists of a collection of identical nested pieces.

And ultimately this is not surprising. After all, the basic rules for these substitution systems specify that any time an element of a particular color appears it will always get subdivided in the same way.

The nested structure becomes even clearer if one represents elements not as boxes, but instead as branches on a tree. And with this setup the idea is to start from the trunk of the tree, and then at each step to use the rules for the substitution system to determine how every branch should be split into smaller branches.

![](Images/_page_99_Figure_1.jpeg)

More examples of neighbor-independent substitution systems like those on the previous page. Each rule yields a different sequence of elements, but all of them ultimately have simple nested forms.

Then the point is that because the rules depend only on the color of a particular branch, and not on the colors of any neighboring branches, the subtrees that are generated from all the branches of the same color must have exactly the same structure, as in the pictures below.

![](Images/_page_99_Picture_4.jpeg)

The evolution of the same substitution systems as on the previous page, but now shown in terms of trees. Starting from the trunk at the bottom, the rules specify that at each step every branch of a particular color should split into smaller branches in the same way. The result is that each tree consists of a collection of progressively smaller subtrees with the same structure. On page 400 I will use similar systems to discuss the growth of actual trees and leaves.

To get behavior that is more complicated than simple nesting, it follows therefore that one must consider substitution systems whose rules depend not only on the color of a single element, but also on the color of at least one of its neighbors. The pictures below show examples in which the rules for replacing an element depend not only on its own color, but also on the color of the element immediately to its right.

![](Images/_page_100_Picture_3.jpeg)

Examples of substitution systems whose rules depend not just on the color of an element itself, but also on the color of the element immediately to its right. Rules of this kind cannot readily be interpreted in terms of simple subdivision of one element into several. And as a result, there is no obvious way to choose what size of box should be used to represent each element in the picture. What I do here is simply to divide the whole width of the picture equally among all elements that appear at each step. Note that on every step the rightmost element is always dropped, since no rule is given for how to replace it.

In the first example, the pattern obtained still has a simple nested structure. But in the second example, the behavior is more complicated, and there is no obvious nested structure.

One feature of both examples, however, is that the total number of elements never decreases from one step to the next. The reason for this is that the basic rules we used specify that every single element should be replaced by at least one new element.

It is, however, also possible to consider substitution systems in which elements can simply disappear. If the rate of such disappearances is too large, then almost any pattern will quickly die out. And if there are too few disappearances, then most patterns will grow very rapidly.

But there is always a small fraction of rules in which the creation and destruction of elements is almost perfectly balanced.

Two views of a substitution system whose rules allow both creation and destruction of elements. In the view on the left, the boxes representing each element are scaled to keep the total width the same, whereas on the right each box has a fixed size, as in our original pictures of substitution systems on page 82. The right-hand view shows that the rates of creation and destruction of elements are balanced closely enough that the total number of elements grows by only a fixed amount at each step.

![](Images/_page_101_Picture_4.jpeg)

![](Images/_page_101_Picture_5.jpeg)

The picture above shows one example. The number of elements does end up increasing in this particular example, but only by a fixed amount at each step. And with such slow growth, we can again represent each element by a box of the same size, just as in our original pictures of substitution systems on page 82.

When viewed in this way, however, the pattern produced by the substitution system shown above is seen to have a simple repetitive form. And as it turns out, among substitution systems with the same type of rules, all those which yield slow growth also seem to produce only such simple repetitive patterns.

Knowing this, we might conclude that somehow substitution systems just cannot produce the kind of complexity that we have seen in systems like cellular automata. But as with mobile automata and with Turing machines, we would again be wrong. Indeed, as the pictures on the facing page demonstrate, allowing elements to have three or four colors rather than just two immediately makes much more complicated behavior possible.

![](Images/_page_102_Figure_2.jpeg)

Examples of substitution systems that have three and four possible colors for each element. The particular rules shown are ones that lead to slow growth in the total number of elements. Note that on each line in each picture, only the order of elements is ever significant: as the insets show, a particular element may change its position as a result of the addition or subtraction of elements to its left. Note that the pattern in case (a) does eventually repeat, while the one in case (b) eventually shows a nested structure.

![](Images/_page_102_Figure_4.jpeg)

As it turns out, the first substitution system shown works almost exactly like a cellular automaton. Indeed, away from the right-hand edge, all the elements effectively behave as if they were lying on a regular grid, with the color of each element depending only on the previous color of that element and the element immediately to its right.

The second substitution system shown again has patches that exhibit a regular grid structure. But between these patches, there are regions in which elements are created and destroyed. And in the other substitution systems shown, elements are created and destroyed throughout, leaving no trace of any simple grid structure. So in the end the patterns we obtain can look just as random as what we have seen in systems like cellular automata.

#### **Sequential Substitution Systems**

None of the systems we have discussed so far in this chapter might at first seem much like computer programs of the kind we typically use in practice. But it turns out that there are for example variants of substitution systems that work essentially just like standard text editors.

The first step in understanding this correspondence is to think of substitution systems as operating not on sequences of colored elements but rather on strings of elements or letters. Thus for example the state of a substitution system at a particular step can be represented by the string ABBBABA, where the A's correspond to white elements and the B's to black ones.

The substitution systems that we discussed in the previous section work by replacing each element in such a string by a new sequence of elements—so that in a sense these systems operate in parallel on all the elements that exist in the string at each step.

But it is also possible to consider sequential substitution systems, in which the idea is instead to scan the string from left to right, looking for a particular sequence of elements, and then to perform a replacement for the first such sequence that is found. And this setup is now directly analogous to the search-and-replace function of a typical text editor.

The picture below shows an example of a sequential substitution system in which the rule specifies simply that the first sequence of the form BA found at each step should be replaced with the sequence ABA.

![](Images/_page_104_Picture_3.jpeg)

An example of a very simple sequential substitution system. The light squares can be thought of as corresponding to the element A, and the dark squares to the element B. At each step, the rule then specifies that the string which exists at that step should be scanned from left to right, and the first sequence BA that is found should be replaced by ABA. In the picture, the black dots indicate which elements are being replaced at each step. In the case shown, the initial string is BABA. At each step, the rule then has the effect of adding an A inside the string.

The behavior in this case is very simple, with longer and longer strings of the same form being produced at each step. But one can get more complicated behavior if one uses rules that involve more than just one possible replacement. The idea in this case is at each step to scan the string repeatedly, trying successive replacements on successive scans, and stopping as soon as a replacement that can be used is found.

The picture on the next page shows a sequential substitution system with rule  $\{ABA \rightarrow AAB, A \rightarrow ABA\}$  involving two possible replacements. Since the sequence ABA occurs in the initial string that is given, the first replacement is used on the first step. But the string BAAB that is produced at the second step does not contain ABA, so now the first replacement cannot be used. Nevertheless, since the string does contain the single element A, the second replacement can still be used.

Despite such alternation between different replacements, however, the final pattern that emerges is very regular. Indeed, if one allows only two possible replacements—and two possible elements—

![](Images/_page_105_Picture_2.jpeg)

A sequential substitution system whose rule involves two possible replacements. At each step, the whole string is scanned once to try to apply the first replacement, and is then scanned again if necessary to try to apply the second replacement.

![](Images/_page_105_Figure_4.jpeg)

then it seems that no rule ever gives behavior that is much more complicated than in the picture above.

And from this one might be led to conclude that sequential substitution systems could never produce behavior of any substantial complexity. But having now seen complexity in many other kinds of systems, one might suspect that it should also be possible in sequential substitution systems.

And it turns out that if one allows more than two possible replacements then one can indeed immediately get more complex behavior. The pictures on the facing page show a few examples. In many cases, fairly regular repetitive or nested patterns are still produced.

But about once in every 10,000 randomly selected rules, rather different behavior is obtained. Indeed, as the picture on the following page demonstrates, patterns can be produced that seem in many respects random, much like patterns we have seen in cellular automata and other systems.

So this leads to the rather remarkable conclusion that just by using the simple operations available even in a very basic text editor, it is still ultimately possible to produce behavior of great complexity.

![](Images/_page_106_Figure_2.jpeg)

Examples of sequential substitution systems whose rules involve three possible replacements. In all cases, the systems are started from the initial string BAB. The black dots indicate the elements that are replaced at each step.

![](Images/_page_106_Figure_4.jpeg)

![](Images/_page_107_Picture_2.jpeg)

![](Images/_page_107_Picture_3.jpeg)

![](Images/_page_107_Picture_4.jpeg)

![](Images/_page_107_Picture_5.jpeg)

An example of a sequential substitution system that yields apparently random behavior. Each column on the right-hand side shows the evolution of the system for 250 steps. The compressed picture on the left is made by evolving for a million steps, but showing only steps at which the string becomes longer than it has ever been before. (The rule is the same as (g) on the previous page.)

#### **Tag Systems**

One of the goals of this chapter is to find out just how simple the underlying structure of a system can be while the system as a whole is still capable of producing complex behavior. And as one example of a class of systems with a particularly simple underlying structure, I consider here what are sometimes known as tag systems.

A tag system consists of a sequence of elements, each colored say black or white. The rules for the system specify that at each step a fixed number of elements should be removed from the beginning of the sequence. And then, depending on the colors of these elements, one of several possible blocks is tagged onto the end of the sequence.

The pictures below show examples of tag systems in which just one element is removed at each step. And already in these systems one sometimes sees behavior that looks somewhat complicated.

![](Images/_page_108_Figure_5.jpeg)

![](Images/_page_108_Figure_6.jpeg)

![](Images/_page_108_Figure_7.jpeg)

![](Images/_page_108_Figure_8.jpeg)

Examples of tag systems in which a single element is removed from the beginning of the sequence at each step, and a new block of elements is added to the end of the sequence according to the rules shown. Because only a single element is removed at each step, the systems effectively just cycle through all elements, replacing each one in turn. And after every complete cycle, the sequences obtained correspond exactly to the sequences produced on successive steps in the first three ordinary neighbor-independent substitution systems shown on page 83.

But in fact it turns out that if only one element is removed at each step, then a tag system always effectively acts just like a slow version of a neighbor-independent substitution system of the kind we discussed on page 83. And as a result, the pattern it produces must ultimately have a simple repetitive or nested form.

If two elements are removed at each step, however, then this is no longer true. And indeed, as the pictures on the next page demonstrate, the behavior that is obtained in this case can often be very complicated.

![](Images/_page_109_Figure_2.jpeg)

Examples of tag systems in which at each step two elements are removed from the beginning of the sequence and then, based on what these elements are, a specified block of new elements is added to the end of the sequence. (The three dots in the representation of each rule stand for the rest of the elements in the sequence.) The pictures at the top show the first hundred steps in evolution according to various rules starting from a pair of black elements. The plots show the total lengths of the sequences obtained in each case. Note that in case (c), all the elements are eventually removed from the sequence.

#### Cyclic Tag Systems

The basic operation of the tag systems that we discussed in the previous section is extremely simple. But it turns out that by using a slightly different setup one can construct systems whose operation is in some ways even simpler. In an ordinary tag system, one does not know in advance which of several possible blocks will be added at each step. But the idea of a cyclic tag system is to make the underlying rule already specify exactly what block can be added at each step.

In the simplest case there are two possible blocks, and the rule simply alternates on successive steps between these blocks, adding a block at a particular step when the first element in the sequence at that step is black. The picture below shows an example of how this works.

![](Images/_page_110_Picture_4.jpeg)

![](Images/_page_110_Picture_5.jpeg)

An example of a cyclic tag system. There are two cases in the rule, and these cases are used on alternate steps, as indicated by the circle icons on the left. In each case a single element is removed from the beginning of the sequence, and then a new block is added at the end whenever the element removed is black. The rule can be summarized just by giving the blocks to be used in each case, as shown below.

![](Images/_page_110_Picture_7.jpeg)

The next page shows examples of several cyclic tag systems. In cases (a) and (b) simple behavior is obtained. In case (c) the behavior is slightly more complicated, but if the pattern is viewed in the appropriate way then it turns out to have the same nested form as the third neighbor-independent substitution system shown on page 83.

So what about cases (d) and (e)? In both of these, the sequences obtained at successive steps grow on average progressively longer. But if one looks at the fluctuations in this growth, as in the plots on the next page, then one finds that these fluctuations are in many respects random.

![](Images/_page_111_Figure_1.jpeg)

Examples of cyclic tag systems. In each case the initial condition consists of a single black element. In case (c), alternate steps in the leftmost column (which in all cyclic tag systems determines the overall behavior) have the same nested form as the third neighbor-independent substitution system shown on page 83.

![](Images/_page_111_Figure_3.jpeg)

Fluctuations in the growth of sequences for cyclic tag systems (d) and (e) above. The fluctuations are shown with respect to growth at an average rate of half an element per step.

#### **Register Machines**

All of the various kinds of systems that we have discussed so far in this chapter can readily be implemented on practical computers. But none of them at an underlying level actually work very much like typical computers. Register machines are however specifically designed to be very simple idealizations of present-day computers.

Under most everyday circumstances, the hardware construction of the computers we use is hidden from us by many layers of software. But at the lowest level, the CPUs of all standard computers have registers that store numbers, and any program we write is ultimately converted into a sequence of simple instructions that specify operations to be performed on these registers.

Most practical computers have quite a few registers, and support perhaps tens of different kinds of instructions. But as a simple idealization one can consider register machines with just two registers—each storing a number of any size—and just two kinds of instructions: "increments" and "decrement-jumps". The rules for such register machines are then idealizations of practical programs, and are taken to consist of fixed sequences of instructions, to be executed in turn.

Increment instructions are set up just to increase by one the number stored in a particular register. Decrement-jump instructions, on the other hand, do two things. First, they decrease by one the number in a particular register. But then, instead of just going on to execute the next instruction in the program, they jump to some specified other point in the program, and begin executing again from there.

Since we assume that the numbers in our registers cannot be negative, however, a register that is already zero cannot be decremented. And decrement-jump instructions are then set up so that if they are applied to a register containing zero, they just do essentially nothing: they leave the register unchanged, and then they go on to execute the next instruction in the program, without jumping anywhere.

This feature of decrement-jump instructions may seem like a detail, but in fact it is crucial—for it is what makes it possible for our register machines to take different paths depending on values in registers through the programs they are given.

![](Images/_page_113_Figure_1.jpeg)

Examples of simple register machines, set up to mimic the low-level operation of practical computers. The machines shown have two registers, whose values on successive steps are given on successive lines down the page. Each machine follows a fixed program given at the top. The program consists of a sequence of increment ▶ and decrement-jump ◄ instructions. Instructions that are shown as light gray boxes refer to the first register; those shown as dark gray boxes refer to the second one. On each line going down the page, the black dot on the left indicates which instruction in the program is being executed at the corresponding step. With the particular programs shown here, each machine just executes successive instructions in turn, jumping to the beginning again when it reaches the end of the program.

And with this setup, the pictures above show three very simple examples of register machines with two registers. The programs for each of the machines are given at the top, with ▶ representing an increment instruction, and ◄ a decrement-jump. The successive steps in the evolution of each machine are shown on successive lines down the page. The instruction being executed is indicated at each step by the position of the dot on the left, while the numbers in each of the two registers are indicated by the gray blocks on the right.

All the register machines shown start by executing the first instruction in their programs. And with the particular programs used here, the machines are then set up just to execute all the other instructions in their programs in turn, jumping back to the beginning of their programs whenever they reach the end.

Both registers in each machine are initially zero. And in the first machine, the first register alternates between 0 and 1, while the second remains zero. In the second machine, however, the first register again

alternates between 0 and 1, but the second register progressively grows. And finally, in the third machine both registers grow.

But in all these three examples, the overall behavior is essentially repetitive. And indeed it turns out that among the 10,552 possible register machines with programs that are four or fewer instructions long, not a single one exhibits more complicated behavior.

However, with five instructions, slightly more complicated behavior becomes possible, as the picture below shows. But even in this example, there is still a highly regular nested structure.

![](Images/_page_114_Picture_5.jpeg)

A register machine that shows nested rather than strictly repetitive behavior. The register machine has a program which is five instructions long. It turns out that this program is one of only two (which differ just by interchange of the first and second registers) out of the 248,832 possible programs with five instructions that yield anything other than strictly repetitive behavior.

And it turns out that even with up to seven instructions, none of the 276,224,376 programs that are possible lead to substantially more complicated behavior. But with eight instructions, 126 out of the 11,019,960,576 possible programs finally do show more complicated behavior. The next page gives an example.

![](Images/_page_115_Figure_1.jpeg)

A register machine whose behavior seems in some ways random. The program for this register machine is eight instructions long. Testing all 11,019,960,576 possible programs of length eight revealed just this and 125 similar cases of complex behavior. Part (b) shows the evolution in compressed form, with only those steps included at which either of the registers has just decreased to zero. The values of the nonzero registers are shown using a logarithmic scale. Part (c) shows the instructions that are executed for the first 400 times that one of the registers is decreased to zero. Finally, part (d) gives the successive values attained by the second register at steps where the first register has just decreased to zero. These values are given here as binary digit sequences. As discussed on page 122, the values can in fact be obtained by a simple arithmetic rule, without explicitly following each step in the evolution of the register machine. If one value is n, then the next value is 3n/2 if n is even, and (3n+1)/2 if n is odd. The initial condition is n=1.

Looking just at the ordinary evolution labelled (a), however, the system might still appear to have quite simple and regular behavior. But a closer examination turns out to reveal irregularities. Part (b) of the picture shows a version of the evolution compressed to include only

those steps at which one of the two registers has just decreased to zero. And in this picture one immediately sees some apparently random variation in the instructions that are executed.

Part (c) of the picture then shows which instructions are executed for the first 400 times one of the registers has just decreased to zero. And part (d) finally shows the base 2 digits of the successive values attained by the second register when the first register has just decreased to zero. The results appear to show considerable randomness.

So even though it may not be as obvious as in some of the other systems we have studied, the simple register machine on the facing page can still generate complex and seemingly quite random behavior.

So what about more complicated register machines?

An obvious possibility is to allow more than two registers. But it turns out that very little is normally gained by doing this. With three registers, for example, seemingly random behavior can be obtained with a program that is seven rather than eight instructions long. But the actual behavior of the program is almost indistinguishable from what we have already seen with two registers.

Another way to set up more complicated register machines is to extend the kinds of underlying instructions one allows. One can for example introduce instructions that refer to two registers at a time, adding, subtracting or comparing their contents. But it turns out that the presence of instructions like these rarely seems to have much effect on either the form of complex behavior that can occur, or how common it is.

Yet particularly when such extended instruction sets are used, register machines can provide fairly accurate idealizations of the low-level operations of real computers. And as a result, programs for register machines are often very much like programs written in actual low-level computer languages such as C, BASIC, Java or assembler.

In a typical case, each variable in such a program simply corresponds to one of the registers in the register machine, with no arrays or pointers being allowed. And with this correspondence, our general results on register machines can also be expected to apply to simple programs written in actual low-level computer languages.

Practical details make it somewhat difficult to do systematic experiments on such programs. But the experiments I have carried out do suggest that, just as with simple register machines, searching through many millions of short programs typically yields at least a few that exhibit complex and seemingly random behavior.

#### Symbolic Systems

Register machines provide simple idealizations of typical low-level computer languages. But what about *Mathematica*? How can one set up a simple idealization of the transformations on symbolic expressions that *Mathematica* does? One approach suggested by the idea of combinators from the 1920s is to consider expressions with forms such as e[e[e][e]][e][e] and then to make transformations on these by repeatedly applying rules such as  $e[x_{-}][y_{-}] \rightarrow x[x[y]]$ , where  $x_{-}$  and  $y_{-}$  stand for any expression.

The picture below shows an example of this. At each step the transformation is done by scanning once from left to right, and applying the rule wherever possible without overlapping.

![](Images/_page_117_Figure_5.jpeg)

The structure of expressions like those on the facing page is determined just by their sequence of opening and closing brackets. And representing these brackets by dark and light squares respectively, the picture below shows the overall pattern of behavior generated.

![](Images/_page_118_Picture_3.jpeg)

![](Images/_page_118_Picture_4.jpeg)

![](Images/_page_118_Picture_5.jpeg)

![](Images/_page_118_Picture_6.jpeg)

More steps in the evolution on the previous page, with opening brackets represented by dark squares and closing brackets by light ones. In each case configurations wider than the picture are cut off on the right. For the initial condition from the previous page, the system evolves after 264 steps to a fixed configuration involving 256 opening brackets followed by 256 closing brackets. For the initial condition on the bottom right, the system again evolves to a fixed configuration, but now this takes 65,555 steps, and the configuration involves 65,536 opening and closing brackets. Note that the evolution rules are highly non-local, and are rather unlike those, say, in a cellular automaton. It turns out that this particular system always evolves to a fixed configuration, but for initial conditions of size n can take roughly n iterated powers of 2 (or  $2^{2^{2^{-}}}$ ) to do so.

With the particular rule shown, the behavior always eventually stabilizes—though sometimes only after an astronomically long time.

But it is quite possible to find symbolic systems where this does not happen, as illustrated in the pictures below. Sometimes the behavior that is generated in such systems has a simple repetitive or nested form. But often—just as in so many other kinds of systems—the behavior is instead complex and seemingly quite random.

![](Images/_page_119_Figure_3.jpeg)

The behavior of various symbolic systems starting from the initial condition e[e[e][e]][e][e]. The plots at the bottom show the difference in size of the expressions obtained on successive steps.

#### Some Conclusions

In the chapter before this one, we discovered the remarkable fact that even though their underlying rules are extremely simple, certain cellular automata can nevertheless produce behavior of great complexity.

Yet at first, this seems so surprising and so outside our normal experience that we may tend to assume that it must be a consequence of some rare and special feature of cellular automata, and must not occur in other kinds of systems.

For it is certainly true that cellular automata have many special features. All their elements, for example, are always arranged in a rigid array, and are always updated in parallel at each step. And one might think that features like these could be crucial in making it possible to produce complex behavior from simple underlying rules.

But from our study of substitution systems earlier in this chapter we know, for example, that in fact it is not necessary to have elements that are arranged in a rigid array. And from studying mobile automata, we know that updating in parallel is also not critical.

Indeed, I specifically chose the sequence of systems in this chapter to see what would happen when each of the various special features of cellular automata were taken away. And the remarkable conclusion is that in the end none of these features actually matter much at all. For every single type of system in this chapter has ultimately proved capable of producing very much the same kind of complexity that we saw in cellular automata.

So this suggests that in fact the phenomenon of complexity is quite universal—and quite independent of the details of particular systems.

But when in general does complexity occur?

The examples in this chapter suggest that if the rules for a particular system are sufficiently simple, then the system will only ever exhibit purely repetitive behavior. If the rules are slightly more complicated, then nesting will also often appear. But to get complexity in the overall behavior of a system one needs to go beyond some threshold in the complexity of its underlying rules.

The remarkable discovery that we have made, however, is that this threshold is typically extremely low. And indeed in the course of this chapter we have seen that in every single one of the general kinds of systems that we have discussed, it ultimately takes only very simple rules to produce behavior of great complexity.

One might nevertheless have thought that if one were to increase the complexity of the rules, then the behavior one would get would also become correspondingly more complex. But as the pictures on the facing page illustrate, this is not typically what happens.

Instead, once the threshold for complex behavior has been reached, what one usually finds is that adding complexity to the underlying rules does not lead to any perceptible increase at all in the overall complexity of the behavior that is produced.

The crucial ingredients that are needed for complex behavior are, it seems, already present in systems with very simple rules, and as a result, nothing fundamentally new typically happens when the rules are made more complex. Indeed, as the picture on the facing page demonstrates, there is often no clear correlation between the complexity of rules and the complexity of behavior they produce. And this means, for example, that even with highly complex rules, very simple behavior still often occurs.

One observation that can be made from the examples in this chapter is that when the behavior of a system does not look complex, it tends to be dominated by either repetition or nesting. And indeed, it seems that the basic themes of repetition, nesting, randomness and localized structures that we already saw in specific cellular automata in the previous chapter are actually very general, and in fact represent the dominant themes in the behavior of a vast range of different systems.

The details of the underlying rules for a specific system can certainly affect the details of the behavior it produces. But what we have seen in this chapter is that at an overall level the typical types of behavior that occur are quite universal, and are almost completely independent of the details of underlying rules.

And this fact has been crucial in my efforts to develop a coherent science of the kind I describe in this book. For it is what implies that

![](Images/_page_122_Figure_2.jpeg)

Examples of cellular automata with rules of varying complexity. The rules used are of the so-called totalistic type described on page 60. With two possible colors, just 4 cases need to be specified in such rules, and there are 16 possible rules in all. But as the number of colors increases, the rules rapidly become more complex. With three colors, there are 7 cases to be specified, and 2187 possible rules; with five colors, there are 13 cases to be specified, and 1,220,703,125 possible rules. But even though the underlying rules increase rapidly in complexity, the overall forms of behavior that we see do not change much. With two colors, it turns out that no totalistic rules yield anything other than repetitive or nested behavior. But as soon as three colors are allowed, much more complex behavior is immediately possible. Allowing four or more colors, however, does not further increase the complexity of the behavior, and, as the picture shows, even with five colors, simple repetitive and nested behavior can still occur.

there are general principles that govern the behavior of a wide range of systems, independent of the precise details of each system.

And it is this that means that even if we do not know all the details of what is inside some specific system in nature, we can still potentially make fundamental statements about its overall behavior. Indeed, in most cases, the important features of this behavior will actually turn out to be ones that we have already seen with the various kinds of very simple rules that we have discussed in this chapter.

#### How the Discoveries in This Chapter Were Made

This chapter—and the last—have described a series of surprising discoveries that I have made about what simple programs typically do. And in making these discoveries I have ended up developing a somewhat new methodology—that I expect will be central to almost any fundamental investigation in the new kind of science that I describe in this book.

Traditional mathematics and the existing theoretical sciences would have suggested using a basic methodology in which one starts from whatever behavior one wants to study, then tries to construct examples that show this behavior. But I am sure that had I used this approach, I would not have got very far. For I would have looked only for types of behavior that I already believed might exist. And in studying cellular automata, this would for example probably have meant that I would only have looked for repetition and nesting.

But what allowed me to discover much more was that I used instead a methodology fundamentally based on doing computer experiments.

In a traditional scientific experiment, one sets up a system in nature and then watches to see how it behaves. And in much the same way, one can set up a program on a computer and then watch how it behaves. And the great advantage of such an experimental approach is that it does not require one to know in advance exactly what kinds of behavior can occur. And this is what makes it possible to discover genuinely new phenomena that one did not expect.

Experience in the traditional experimental sciences might suggest, however, that experiments are somehow always fundamentally imprecise.

For when one deals with systems in nature it is normally impossible to set up or measure them with perfect precision—and indeed it can be a challenge even to make a traditional experiment be at all repeatable.

But for the kinds of computer experiments I do in this book, there is no such issue. For in almost all cases they involve programs whose rules and initial conditions can be specified with perfect precision—so that they work exactly the same whenever and wherever they are run.

In many ways these kinds of computer experiments thus manage to combine the best of both theoretical and experimental approaches to science. For their results have the kind of precision and clarity that one expects of theoretical or mathematical statements. Yet these results can nevertheless be found purely by making observations.

Yet as with all types of experiments it requires considerable skill and judgement to know how to set up a computer experiment that will yield meaningful results. And indeed, over the past twenty years or so my own methodology for doing such experiments has become vastly better.

Over and over again the single most important principle that I have learned is that the best computer experiments are ones that are as simple and straightforward as possible. And this principle applies both to the structure of the actual systems one studies, and to the procedures that one uses for studying them.

At some level the principle of looking at systems with the simplest possible structure can be viewed as an abstract aesthetic one. But it turns out also to have some very concrete consequences.

For a start, the simpler a structure is, the more likely it is that it will show up in a wide diversity of different places. And this means that by studying systems with the simplest possible structure one will tend to get results that have the broadest and most fundamental significance.

In addition, looking at systems with simpler underlying structures gives one a better chance of being able to tell what is really responsible for any phenomenon one sees—for there are fewer features that have been put into the system and that could lead one astray.

At a purely practical level, there is also an advantage to studying systems with simpler structures; for these systems are usually easier to implement on a computer, and can thus typically be investigated more extensively with given computational resources.

But an obvious issue with saying that one should study systems with the simplest possible structure is that such systems might just not be capable of exhibiting the kinds of behavior that one might consider interesting—or that actually occurs in nature.

And in fact, intuition from traditional science and mathematics has always tended to suggest that unless one adds all sorts of complications, most systems will never be able to exhibit any very relevant behavior. But the results so far in this book have shown that such intuition is far from correct, and that in reality even systems with extremely simple rules can give rise to behavior of great complexity.

The consequences of this fact for computer experiments are quite profound. For it implies that there is never an immediate reason to go beyond studying systems with rather simple underlying rules. But to absorb this point is not an easy matter. And indeed, in my experience the single most common mistake in doing computer experiments is to look at systems that are vastly more complicated than is necessary.

Typically the reason this happens is that one just cannot imagine any way in which a simpler system could exhibit interesting behavior. And so one decides to look at a more complicated system—usually with features specifically inserted to produce some specific form of behavior.

Much later one may go back and look at the simpler system again. And this is often a humbling experience, for it is common to find that the system does in fact manage to produce interesting behavior—but just in a way that one was not imaginative enough to guess.

So having seen this many times I now always try to follow the principle that one can never start with too simple a system. For at worst, one will just establish a lower limit on what is needed for interesting behavior to occur. But much more often, one will instead discover behavior that one never thought was possible.

It should however be emphasized that even in an experiment it is never entirely straightforward to discover phenomena one did not expect. For in setting up the experiment, one inevitably has to make assumptions about the kinds of behavior that can occur. And if it turns

out that there is behavior which does not happen to fit in with these assumptions, then typically the experiment will fail to notice it.

In my experience, however, the way to have the best chance of discovering new phenomena in a computer experiment is to make the design of the experiment as simple and direct as possible. It is usually much better, for example, to do a mindless search of a large number of possible cases than to do a carefully crafted search of a smaller number. For in narrowing the search one inevitably makes assumptions, and these assumptions may end up missing the cases of greatest interest.

Along similar lines, I have always found it much better to look explicitly at the actual behavior of systems, than to work from some kind of summary. For in making a summary one inevitably has to pick out only certain features, and in doing this one can remove or obscure the most interesting effects.

But one of the problems with very direct experiments is that they often generate huge amounts of raw data. Yet what I have typically found is that if one manages to present this data in the form of pictures then it effectively becomes possible to analyze very quickly just with one's eyes. And indeed, in my experience it is typically much easier to recognize unexpected phenomena in this way than by using any kind of automated procedure for data analysis.

It was in a certain sense lucky that one-dimensional cellular automata were the first examples of simple programs that I investigated. For it so happens that in these systems one can usually get a good idea of overall behavior just by looking at an array of perhaps 10,000 cells—which can easily be displayed in few square inches.

And since several of the 256 elementary cellular automaton rules already generate great complexity, just studying a couple of pages of pictures like the ones at the beginning of this chapter should in principle have allowed one to discover the basic phenomenon of complexity in cellular automata.

But in fact I did not make this discovery in such a straightforward way. I had the idea of looking at pictures of cellular automaton evolution at the very beginning. But the technological difficulty of producing these pictures made me want to reduce their number as

much as possible. And so at first I looked only at the 32 rules which had left-right symmetry and made blank backgrounds stay unchanged.

Among these rules I found examples of repetition and nesting. And with random initial conditions, I found more complicated behavior. But since I did not expect that any complicated behavior would be possible with simple initial conditions, I did not try looking at other rules in an attempt to find it. Nevertheless, as it happens, the first paper that I published about cellular automata—in 1983—did in fact include a picture of rule 30 from page 27, as an example of a non-symmetric rule. But the picture showed only 20 steps of evolution, and at the time I did not look carefully at it, and certainly did not appreciate its significance.

For several years, I did progressively more sophisticated computer experiments on cellular automata, and in the process I managed to elucidate many of their properties. But finally, when technology had advanced to the point where it became almost trivial for me to do so, I went back and generated some straightforward pages of pictures of all 256 elementary rules evolving from simple initial conditions. And it was upon seeing these pictures that I finally began to appreciate the remarkable phenomenon that occurs in systems like rule 30.

Seven years later, after I had absorbed some basic intuition from looking at cellular automata like rule 30, I resolved to find out whether similar phenomena also occurred in other kinds of systems. And the first such systems that I investigated were mobile automata.

Mobile automata in a sense evolve very slowly relative to cellular automata, so to make more efficient pictures I came up with a scheme for showing their evolution in compressed form. I then started off by generating pictures of the first hundred, then the first thousand, then the first ten thousand, mobile automata. But in all of these pictures I found nothing beyond repetitive and nested behavior.

Yet being convinced that more complicated behavior must be possible, I decided to persist, and so I wrote a program that would automatically search through large numbers of mobile automata. I set up various criteria for the search, based on how I expected mobile automata could behave. And quite soon, I had made the program search a million mobile automata, then ten million.

But still I found nothing.

So then I went back and started looking by eye at mobile automata with large numbers of randomly chosen rules. And after some time what I realized was that with the compression scheme I was using there could be mobile automata that would be discarded according to my search criteria, but which nevertheless still had interesting behavior. And within an hour of modifying my search program to account for this, I found the example shown on page 74.

Yet even after this, there were still many assumptions implicit in my search program. And it took some time longer to identify and remove them. But having done so, it was then rather straightforward to find the example shown on page 75.

A somewhat similar pattern has been repeated for most of the other systems described in this chapter. The main challenge was always to avoid assumptions and set up experiments that were simple and direct enough that they did not miss important new phenomena.

In many cases it took a large number of iterations to work out the right experiments to do. And had it not been for the ease with which I could set up new experiments using *Mathematica*, it is likely that I would never have gotten very far in investigating most of the systems discussed in this chapter. But in the end, after running programs for a total of several years of computer time—corresponding to more than a million billion logical operations—and creating the equivalent of tens of thousands of pages of pictures, I was finally able to find all of the various examples shown in this chapter and the ones that follow.
