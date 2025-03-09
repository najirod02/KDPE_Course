# Reichenbach assignment
Below the solutions to the questions

# 1 - Written problems

## 1 - The seating of the Diogenes Club

### a
If we have 10 distinct memebers then we have 10! permutations as we can decide for the first sitting from 10 people, the next sitting from 9 and so on to the last one obtaining 10 x 9 x 8 x ... x 1 = `10!`

### b
We can consider them as a single unit (a single person) so 10-1=9 person.
Moreover one of them can be seated on the left or on the right
so we have to multiply by 2.
We obtain `9! x 2` permutations.

### c
It's like having 2 groups, A (seasoned inspectors) and B (novice constables). Becasue we cannot put two peope of the same rank near, the only thing we can do is to alternate the groups like
ABAB... or BABA...
In both cases we have 5! x 5! combinations (5 x 5 x 4 x 4 x ...x 1 x 1) so we just need to multiply the result by 2 obtaining `2 x 5!`

### d
One coudl simply state that using the binomial factor would solve the problem but this solution doesn't keep in consideration the fact that we have to form "valid" pairs so binom(10,2) is not the solution.

We know that we have 5 informants and 5 handlers (otherwise we cannot form a valid pair). We dispone them on a line, the line of "Informants" and of "Handlers".

I_1 I_2 .. I_5

H_1 H_2 .. H_5

We start generating pairs by choosing only 1 group, let's say informants (as selecting both will only overcount). The first element can make a pair with 5 possible handlers. The second informant then can choose only from 4 handlers as one of them has already been choosen from the first informants. The last one can only choose from the remaining handler.

What I obtain is something like 1 x 5 + 1 x 4 x .. x 1 x 1 = `5! = 120`

We can think of the Handlers as the chairs and the Informants as the people. The process of pairing Informants with Handlers is similar to assigning Informants to the chairs (the Handlers), where the position of the chairs doesn't matter, it's the pairing between a specific Informant and a specific Handler (chair) that matters.

## 2 The Cipher Arrays of Irene Adler
We might think that the ordering adds some level of difficulty the problme but actually we can forget about it in fact, after choosing k elements, we can always reorder them as they are all distinct between them.

It turn out to be a problem of choosing k elements from a list of n elements: `binom(n,k)`.

## 3 The Paths of the Hound

### a
This is a well known dynamic programming problem, unique paths, and so we can use the dynamic programming approach to determine the number of unique paths that the hound can take.

First we have to set the base case which is DP[1][1] = 1 as there is only 1 way to visit the first cell.

We define then the "update" rule that is based on the values of the previous 2 cells: DP[i][j] = DP[i-1][j] + DP[i][j-1] as the actual cell can be visited by coming from the upper cell or the left one.

From this definition we can derive our final solution that is `binom(n+m-2,n-1)`. 

n+2-2 is the total number of moves that we have to take in order to reach the (n,m) cell in fact we will need n-1 moves down and m-1 moves rigth by summing them we obtain n - 1 + m - 1 = n + m - 2.

We can think of this number as a sequence of moves like BRRB...R we know for usre that this sequence needs to have exactly n-1 B and m-1 R. We just need to explore all possible permutations of each move by simply consider only the right or down move in fact they are equivalent as we would obtain the same result which is:<br/>
binom(n+m-2,n-1) = (n+m-2)! / [(n-1)!*(n+m-2-n+1)!] = (n+m-2)! / [(n-1)!*(m-1)!] = `binom(n+m-2,m-1)`

### b
If the first move is always right, it's like the matrix is not anymore n x m but n x (m-1) so we can adjust the solution of part a as:

`binom(n+m-3,n-1)` or equivalently `binom(n+m-3,m-2)`

### c
We know for sure that if the robot changes direction exactly 3 times then we can divide the sequence of moves in 4 segments.

Each segment has the same moves so a segmetn containing e.g BB..RBB is not valid as there are 2 changes in direction.

A valid sequence can be BB...B | RR...R | BB...B | RR...R<br/>
We can observe that we are simply alterning the moves by dividing the groups of B and R moves. Each of these groups can have a variable number of steps, the important thing is that they sum up at the end.

For example, the group of B moves have in total n-1 moves and has to be divided in 2 sub-groups so, binom(n-1,1). This take in consideration also the fact that the grops must contain at least one element so the bar cannot be at the start nor at the end.

Same thing can be done with the R moves so, binom(m-1,1).

Now I know in how many ways i can form groups but I also know that the total number of groups will always be 4 as this allows the robot to change exactly 3 times direction.

The toal number of ways I can change these 4 groups are 2.

The final value becomes simply the multiplication of all the intermediate results: binom(n-1,1) x binom(m-1,1) x 2 = `2 x (n-1) x (m-1)`

## 4 The Poker Game at Reichenbach



# 2 - Coding
TODO