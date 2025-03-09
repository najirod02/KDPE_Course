# Reichenbach assignment
Below the solutions to the questions

# 1 - Written problems

## 1 - The seating of the Diogenes Club

### a
If we have 10 distinct memebers then we have 10! permutations as we can decide for the first sitting from 10 people, the next sitting from 9 and so on to the last one obtaining 10 x 9 x 8 x ... x 1 = 10! 

### b
We can consider them as a single unit (a single person) so 10-1=9 person.
Moreover one of them can be seated on the left or on the right
so we have to multiply by 2.
We obtain 9! x 2 permutations.

### c
It's like having 2 groups, A (seasoned inspectors) and B (novice constables). Becasue we cannot put two peope of the same rank near, the only thing we can do is to alternate the groups like
ABAB... or BABA...
In both cases we have 5! x 5! combinations (5 x 5 x 4 x 4 x ...x 1 x 1) so we just need to multiply the result by 2 obtaining 2 x 5!

### d
One coudl simply state that using the binomial factor would solve the problem but this solution doesn't keep in consideration the fact that we have to form "valid" pairs so binom(10,2) is not the solution.

We know that we have 5 informants and 5 handlers (otherwise we cannot form a valid pair). We dispone them on a line, the line of "Informants" and of "Handlers".

I_1 I_2 .. I_5

H_1 H_2 .. H_5

We start generating pairs by choosing only 1 group, let's say informants (as selecting both will only overcount). The first element can make a pair with 5 possible handlers. The second informant then can choose only from 4 handlers as one of them has already been choosen from the first informants. The last one can only choose from the remaining handler.

What I obtain is something like 1 x 5 + 1 x 4 x .. x 1 x 1 = 5! = 120

We can think of the Handlers as the chairs and the Informants as the people. The process of pairing Informants with Handlers is similar to assigning Informants to the chairs (the Handlers), where the position of the chairs doesn't matter, it's the pairing between a specific Informant and a specific Handler (chair) that matters.

## 2 The Cipher Arrays of Irene Adler


# 2 - Coding
TODO