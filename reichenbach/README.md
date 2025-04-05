# Reichenbach assignment
List of exercises, each with the proposed solution

- [Ex1](#1---the-seating-of-the-diogenes-club)
- [Ex2](#2-the-cipher-arrays-of-irene-adler)
- [Ex3](#3-the-paths-of-the-hound)
- [Ex4](#4-the-poker-game-at-reichenbach)
- [Ex5](#5-the-binary-telegram-of-baskerville)
- [Ex6](#6-the-menagerie-of-moriarty)
- [Ex7](#7-the-investments-of-baker-street)
- [Ex8](#8-the-coding-conundrum-of-scotland-yard)
- [Ex9](#9-the-passwords-of-the-naval-treaty)
- [Ex10](#10-the-dice-of-the-speckled-band)
- [Ex11](#11-the-letters-of-the-red-headed-league)
- [Ex12](#12-the-buckets-of-bohemia)
- [Coding](#2---coding)

[Back to list of assignments](../README.md)

# 1 - Written problems

## 1 - The seating of the Diogenes Club

### a
If we have 10 distinct memebers then we have 10! permutations as we can decide for the first sitting from 10 people, the next sitting from 9 and so on to the last one obtaining 10 x 9 x 8 x ... x 1 = `10!`

### b
We can consider them as a single unit (a single person) so 10-1=9 people.
Moreover one of them can be seated on the left or on the right
so we have to multiply by 2.
We obtain `9! x 2` permutations.

### c
It's like having 2 groups, A (seasoned inspectors) and B (novice constables). Becasue we cannot put two peope of the same rank near, the only thing we can do is to alternate the groups like
ABAB... or BABA...
In both cases we have 5! x 5! combinations (5 x 5 x 4 x 4 x ...x 1 x 1) so we obtain `5! x 5!`

### d
One could simply state that using the binomial factor would solve the problem but this solution doesn't keep in consideration the fact that we have to form "valid" pairs so binom(10,2) is not the solution.

We know that we have 5 informants and 5 handlers (otherwise we cannot form a valid pair). We dispone them on a line, the line of "Informants" and of "Handlers".

I_1 I_2 .. I_5

H_1 H_2 .. H_5

We start generating pairs by choosing only 1 group, let's say informants (as selecting both will only overcount). The first element can make a pair with 5 possible handlers. The second informant then can choose only from 4 handlers as one of them has already been choosen from the first informants. The last one can only choose from the remaining handler.

What I obtain is something like 1 x 5 + 1 x 4 x .. x 1 x 1 = `5! = 120`

We can think of the Handlers as the chairs and the Informants as the people. The process of pairing Informants with Handlers is similar to assigning Informants to the chairs (the Handlers), where the position of the chairs doesn't matter, it's the pairing between a specific Informant and a specific Handler (chair) that matters.

[Back to list of exercises](#reichenbach-assignment)

## 2 The Cipher Arrays of Irene Adler
We might think that the ordering adds some level of difficulty to the problem but actually we can forget about it in fact, after choosing k elements, we can always reorder them as they are all distinct between them.

It turn out to be a problem of choosing k elements from a list of n elements: `binom(n,k)`.

[Back to list of exercises](#reichenbach-assignment)

## 3 The Paths of the Hound

### a
This is a well known dynamic programming problem, unique paths, and so we can use the dynamic programming approach to determine the number of unique paths that the hound can take.

First we have to set the base case which is DP[1][1] = 1 as there is only 1 way to visit the first cell.

We define then the "update" rule that is based on the values of the previous 2 cells: DP[i][j] = DP[i-1][j] + DP[i][j-1] as the actual cell can be visited by coming from the upper cell or the left one.

From this definition we can derive our final solution that is `binom(n+m-2,n-1)`. 

n+m-2 is the total number of moves that we have to take in order to reach the (n,m) cell in fact we will need n-1 moves down and m-1 moves rigth by summing them we obtain n - 1 + m - 1 = n + m - 2. We then have to take exactly n-1 down steps among these ones and the others are the right move.

We can think of this number as a sequence of moves like BRRB...R we know for sure that this sequence needs to have exactly n-1 B and m-1 R. We just need to explore all possible permutations of each move by simply consider only the right or down move in fact they are equivalent as we would obtain the same result which is:<br/>
binom(n+m-2,n-1) = (n+m-2)! / [(n-1)!*(n+m-2-n+1)!] = (n+m-2)! / [(n-1)!*(m-1)!] = `binom(n+m-2,m-1)`

### b
If the first move is always right, it's like the matrix is not anymore n x m but n x (m-1) so we can adjust the solution of part 'a' as:

`binom(n+m-3,n-1)` or equivalently `binom(n+m-3,m-2)`

### c
We know for sure that if the robot changes direction exactly 3 times then we can divide the sequence of moves in 4 segments.

Each segment has the same moves so a segment containing e.g BB..RBB is not valid as there are 2 changes in direction.

A valid sequence can be BB...B | RR...R | BB...B | RR...R<br/>
We can observe that we are simply alterning the moves by dividing the groups of B and R moves. Each of these groups can have a variable number of steps, the important thing is that they sum up at the end.

For example, the group of B moves have in total n-1 moves and has to be divided in 2 sub-groups so, 2^(n-2)-1. This take in consideration also the fact that the grops must contain at least one element so the bar cannot be at the start nor at the end.

Same thing can be done with the R moves so, 2^(m-2)-1.

Now I know in how many ways i can form groups but I also know that the total number of groups will always be 4 as this allows the robot to change exactly 3 times direction.

The toal number of ways I can change these 4 groups are 2.

The final value becomes simply the multiplication of all the intermediate results: `2^(n-2)-1 x 2^(m-2)-1 x 2`

[Back to list of exercises](#reichenbach-assignment)

## 4 The Poker Game at Reichenbach

### a
We can define S and E.

S is simply binom(52,5), the total number of hands we can have.

We know that there are 4 suits meaning that each of them has 13 cards. For a flush I must have 5 cards of the same suite so binom(13,5).<br/>
This is valid for a single suite so I just need to multiply by the number of suits, 4 x binom(13,5) and this is our |E|.

We obtian that P(E) where E is to have a generic flush is P(E) = |E| / |S| = [4 x binom(13,5)] / binom(52,5) = 0.001980792 = `0.002` (approximated).

### b
We can use the same strategy, S doesn't change while E does.

We start from 13 possible values and we choose 2, these will be used as the cards that will form the pairs, binom(13,2). For the 5th card, we can choose from the remaining values not already took that is binom(11,1).<br/>
So far we have decided only the value/rank and not the suit of the cards.<br/>
The 5th card can have any suit so, binom(4,1) while for the others we have to choose 2 different suit so, binom(4,2).

What we obtain for |E| is binom(13,2) x binom(4,2) x binom(4,2) x binom(11,1) x binom(4,1).

We can then compute P(E) as usual having as result 0.04753902 = `0.048` (approximated).

### c
Same logic as before. S remain the same.

I have to choose 4 equal ranks so, 1 of the 13 (one pick determines all the others) while the 5th has to be different so, binom(12,1).<br/>
We are sure that the 4 cards have different suit otherwise one at least two of them would have the same while, for the 5th card, we can choose any of the 4 suits.

Finally we obtai that |E| = binom(13,1) x binom(12,1) x binom(4,1)
and as P(E) = 0.000240096 = `0.00024` (approximated)

[Back to list of exercises](#reichenbach-assignment)

## 5 The Binary Telegram of Baskerville
First of all we have to define S, we set it as all the possible permutations of the first r bits so, |S| = binom(N+M,r).

For E we can now consider just the first r bits. The string need exactly k 1's so we can choose them from the N, binom(N,k) and the remaining bits from M, binom(M,r-k).

We don't care of the remainign N+M-r bits in fact, they can have any permutation but doesn't affect the prbability of E.

`P(E) = [binom(N,k) x binom(M,r-k)]/binom(N+M,r)`

[Back to list of exercises](#reichenbach-assignment)

## 6 The Menagerie of Moriarty

### a
Is a simple problem about choosing from undistinct objects.
The total number is binom(8,3) x binom(6,3) = `1120` in fact, the choices are independent.

### b
We can divide the problem in 2 cases:
- Do not take both hawk and raven meanign that we can choose only from 6 birds and not 8. binom(6,3) x binom(6,3)

- Choose one of the two problematic birds meaning that we cannot then choose the other. binom(2,1) x binom(6,2) x binom(6,3)

In total we obtain, from the sum of the two cases, `1000`

### c
S is still the same.<br/>
We can simply count the number of exhibits that are "venomous" which are binom(7,2)*binom(5,2) as the selection of the parrot and the cobra is fixed.

The final result is |S| - |#venomous| = 1120 - 210 = `910`

[Back to list of exercises](#reichenbach-assignment)

## 7 The Investments of Baker Street

### a
First of all, we need to invest at least the minimum for each enterprise so we remain with 20 - (1+2+3+4) = 10 milions.

We can then use the stars and bars method by considering our 10 milions as 10 units and 3 bars in order to obtain 4 subdivision. 
This allows us to distribute the 10 units (money) into the 4 segments (the enterprises) having in total binom(10+3, 3) = binom(13,3) = `286` strategies.

### b
At least 3 means that we take only 3 or 4 enterprises. Because we already solved the situation in which we take 4 enterprises, we just need to sum to that number the total strategies if we take only 3 enterprises at the start and the best way to do it is to check each combination.
Let's call the enterprires with letters A B C D
- Keep out A. The other enterprises needs 9M meaning we can then invest 11M in them meaning binom(11+2,2) = 78

- Keep out B, binom(12+2,2) = 91

- Keep out C, binom(13+2,2) = 105

- Keep out D, binom(14+2,2) = 120

Sum everything to obtain 78 + 91 + 105 + 120 + 286 = `680` strategies.

[Back to list of exercises](#reichenbach-assignment)

## 8 The Coding Conundrum of Scotland Yard

### a
We can compute the number of agents that evaded all courses but we have to keep in consideration that the same person might follow more than 1 course with the risk of overcounting. For this reason we use the rule of inclusion-exclusion. 

|A| (Java) = 27<br/>
|B| (C++) = 28<br/>
|C| (Python) = 20<br/>

|A intersect B| = 12<br/>
|A int. C| = 5<br/>
|B int. C| = 8<br/>
|A int. B int C| = 2

|A U B U C| = |A| + |B| + |C| - |A int. B| - |A int. C| - |B int. C| + |A int. B int. C|
= 27 + 28 + 20 - 12 - 5 - 8 + 2 = 52

We can obtain the total number of people that don't follow any course: 100 - 52 =  48.

The probability is simply 48/100 = `0.48`.

### b
In a similar way, we can simply remove from the corresponding courses the agents that doesn't follow it:
- |Java course| = |A| - |A int B| - |A int C| + |A int B int C| = 27 - 12 - 5 + 2 = 12

- |C++ course| = |B| - |B int A| - |B int C| + |A int B int C| = 28 - 12 - 8 + 2 = 10

- |Python course| = |C| - |C int A| - |C int B| + |A int B int C| = 20 - 5 - 8 + 2 = 9

We need to consider |A int B int C| to avoid double subtraction.

We obtain that the total number of people that follow only 1 course is 12 + 10 + 9 = 31 and the probability is then 31 / 100 = `0.31`.

### c
It is more simply to procede if we consider the complementary case, an agent that doesn't know any course.

This probability has been already discovered (52/100) and can be used to determine the probability that 2 person doesn't follow any course, 52/100 x 52/100.

Now we can determine the complementary probability that is P(at least one knows a course) = 1 - P(no one knows a course) = 1 - (52/100 x 52/100) = 0.7296 = `0.73` (approximated).

[Back to list of exercises](#reichenbach-assignment)

## 9 The Passwords of the Naval Treaty

### a
If I discard the failure then my sample space shrinks as I remove everytime a possible wrong password to choose from.
So the first try is n-1/n then it becomes n-2/n-1 as I remove one possible wrong password and so on until I try the right one which is 1/(n-k+1).

What I obtain is (a little difficult to visualize it):

`product[from i=0 to k-1]{(n-i-1 / n-i)} x (1 / n-k+1)`.

This simply says that for every i-th attempt, I have to reduce the number of possible password to choose from (S) until I reach the k-th attempt.

### b
It's just a sequence of independet events. If at the first try I don't crack the password, I try a second attempy and so on until I find the right password. The text says that I do not discard failures meaning that I can keep choosing the same wrong password and so, the sample space remain the same.

In general if I need k attempts, it means that the first k-1 were all wrong so:

P(E=crack on k-th attemp) = `[(n-1/n)^(k-1)]*1/n`
where n-1/n is the probability of choosing a wrong password and 1/n of choosing the right one.

[Back to list of exercises](#reichenbach-assignment)

## 10 The Dice of the Speckled Band

### a
This means that the sequence has only 2 numbers.
We have binom(6,2) possible ways of chosing 2 numbers to appear in such sequence and can be permutated in 6!/(3! x 3!) ways.<br/>
This defines our |E| but what about |S|? It is just all the possible sequences of 6 digits that is 6^6.

We obtain that P(E) = binom(6,2) x 6!/(3! x 3!) / 6^6 = 0.006430041 = `0.0064` (approximated).

### b
In a similar way we can procede as this:
- Select one number to be repeated exactly 3 times that is, binom(6,1)

- The remaining 3 digits can be choosen from the remainign 5 values that is, binom(5,3)

- We have then to consider all the possible permutations of the 6 digits that is, 6! / 3! as we have 3 equal digits

We finally obtain that P(E)= [binom(6,1) x binom(5,3) x (6! / 3!)] / 6^6 = 0.154321 = `0.154` (approximated).

[Back to list of exercises](#reichenbach-assignment)

## 11 The Letters of the Red-Headed League
We start from defining the total cases, as there is no limitation on the number of letters an informant can get (one possible limit case, 1 informant receive all 20 letters), we can have 12^20 possibilities.

For the favorable cases it is more complicated.
- First we choose 4 informants that will receive 2 letters, binom(12,4).

- These 4 informants receive 2 letters, binom(20,2) x binom(18,2) x binom(16,2) x binom(14,2)

- Same way for the 3 informants that receive 4 letters, binom(8,3).

- These 3 receive 4 letters, binom(12,4) x binom(8,4) x binom(4,4)

- The ones that receive nothing are unimportant.

We obtain that P(E) = #favorable cases / 12^20. Because the values are very big we use the log obtaining that `log(P)` = log(E) - log(S) = `-9.439357`.
If we want the "original" result we just apply the exponential obtainign `P = 7.953151 x 10^-5`

[Back to list of exercises](#reichenbach-assignment)

## 12 The Buckets of Bohemia

As already suggested, the total number of outcomes is N^m. For our favorable cases we can do as follows:
- Take k elements from m, these are going to be put in the first bucket, binom(m,k).

- The last n-k elements can be put whenever you want, even all in the same bucket (excluded the first one), meaning that we can have (N-1)^(n-k).

`P(E) = (binom(m,k)*(N-1)^(m-k)) / N^m`

[Back to list of exercises](#reichenbach-assignment)

# 2 - Coding
Simply run the python script proposed by opening a terminal and type:

```shell
python3 sherlock_game.py
```
The script should output the estimated Moriarty’s victory odds.

In this case there is no need for a virtual environment as there are no extra modules installed. 

In the case the script doesn't run, try to create a venv by following this [guide](https://docs.python.org/3/tutorial/venv.html).

Spolier: Moriarty's victory odds are about 47%!

[Back to list of exercises](#reichenbach-assignment)