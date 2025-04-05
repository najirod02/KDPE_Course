# Hogwarts Quests
List of exercises, each with the proposed solution

- [Ex1](#1)
- [Ex2](#2)
- [Ex3](#3)
- [Ex4](#4)
- [Ex5](#5)
- [Ex6](#6)
- [Ex7](#7)

[Back to list of assignments](../README.md)

# 1

### a
Given that my prior belief is a Gaussian N(98, 16), I can take these values and substitute them in the general PDF formula:

$$
\Large f(D) = \frac{1}{\sqrt{2*\pi*\sigma^2}} e^{-\frac{(D - \mu)^2}{2*\sigma^2}}
$$

$$
\Large f(D) = \frac{1}{\sqrt{32\pi}} e^{-\frac{(D - 98)^2}{32}}
$$

### b

I know that the instrument reading is the true distance, that is in this case t, plus Gaussian noise N(0,4). \
We can use this informations to build our PDF to determine the probability density of reading 100 leagues given the true distance t as follows:

$$
\Large f(100|t) = \frac{1}{\sqrt{8*\pi}} e^{-\frac{(100 - t)^2}{8}}
$$

### c
We can apply the bayes rule in order to find the posterior given the prior and our knowledge.

$$
p(D|I) = \frac{p(I|D)*p(D)}{p(I)}
$$

in particular we can say that p(I) is a constant and so can be "leaved" outside the computations. p(D) is already known, N(98,16) while p(I|D) can be found in a similar way as done in the previous point. \
p(I|D) is the likelihood of reading a certain distance after we defined the real distance with our belief meanign that p(I|D) ~ N(D,4) ~ N(100,4).\
As we have at the denominator a constant, we have to just multiply the Gaussians meanign that we obtain as posterior another Gaussian that is:

- Prior belief p(D) is already known: N(98,16), meaning our initial belief about the true distance is a Gaussian distribution with mean 98 and variance 16.

- Likelihood p(I∣D) represents the probability of the instrument reading I given the  distance D. Since we know that the instrument reading is the distance D plus Gaussian noise with variance 4, we can model this as a Gaussian distribution: p(I∣D)∼N(D,4) \

Since p(I) is constant, we do not need to compute it in the Bayes' update. This allows us to focus on multiplying the prior p(D) and the likelihood p(I∣D). The result of multiplying these Gaussians is another Gaussian distribution, which gives us our posterior. 

$$
p(D \mid I) \sim k * \left( \frac{1}{\sqrt{4\pi}} \exp\left( -\frac{(I - D)^2}{8} \right) \right) \left( \frac{1}{\sqrt{32\pi}} \exp\left( -\frac{(D - 98)^2}{32} \right) \right)
$$

And by applying the rule product of two Gaussians we obtain the new mean and variance obtainign as the final distribution:

$$
p(D \mid I) \sim k * N(99.6, 3.2)
$$

Thus, the posterior belief is a Gaussian distribution with a mean of 99.6 and a reduced variance of 3.2, indicating that our confidence in the true distance has increased as we have a much smaller variance and thus error on the estimation of the distance.

[Back to list of exercises](#hogwarts-quests)

# 2

We can see that the problem can be represented as a Poisson distribution with lambda = 5.5.
$$
X \sim P(\lambda = 5.5)
$$

## a
As it is stated, the problem asks simply to compute
$$
P(X > 7)
$$
where X is our Poisson distribution.\
A much simpler way to compute it (as there is no upper limit to the number of owls) is to just compute the "inverse" problem:

$$
P(X>7) = 1 - P(x<=7)
$$

using R we obtain that the probability is `0.1905147` (summing up all possible values form 0 to 7).

## b
Similar to the previous point but in this case we have to come up with the number of owls every two minute and NOT one. We simply have to multiply by 2 the number of owls per minute obtaining the new lambda = 5.5 * 2 = 11.

$$
X \sim P(\lambda = 11)
$$

$$
P(X>13) = 1 - P(x<=13)
$$

using R we obtain that the probability is `0.2187088`.

## c
Similar to the previous point but in this case we have to come up with the number of owls every three minute and NOT one. We simply have to multiply by 3 the number of owls per minute obtaining the new lambda = 5.5 * 3 = 16.5.

$$
X \sim P(\lambda = 16.5)
$$

$$
P(X>15) = 1 - P(x<=15)
$$

using R we obtain that the probability is `0.5819805`.

[Back to list of exercises](#hogwarts-quests)

# 3

To find the median m, we need to solve for m such that the cumulative distribution funciton equals 0.5 

$$
F_X(m) = 0.5
$$

## a
In the case of a uniform distribution is quite simple as every point has the same probability meaning that the median is exactly at the "center" of the range.

$$
F_X(m) = \frac{m-a}{b-a} = 0.5
$$
$$
2m - 2a = b - a
$$
$$
m = \frac{a+b}{2}
$$

## b
If we think how a Gaussian is drawn, we know that it is symmetric w.r.t the mean meaning that the median is exaclty the mean.

$$
m = \mu
$$

[Back to list of exercises](#hogwarts-quests)

# 4
As stated in the paper, the weekly visits are independent meaning that it is possible to compute the sum and/or product of Gaussians without any problem.

## a
$$
X_3 \sim N (2200, 52900)
$$
$$
X_4 \sim N (2200, 52900)
$$

The distribution for each week are equal and because they are independent I can sum up them to otain the distribution of the following two weeks.

$$
X_{34} = X_3 + X_4 \sim N (4400, 105800)
$$

Now it is easy to compute the probability:
$$
P(X_{34}>5000) = 1 - P(X_{34}<5000)
$$

using R we obtain as final result `0.03254595`.

## b
We can simplify a little the problem by considering the "inverse" problem that is I have 0 or 1 week where I don't exceed.

We can use the binomial distribution to compute the probability of having 1 week or no week where we don't exceed and then "invert" the result.

The probability of not exceeding:
$$
P(X <= 2000) = 0.192269
$$

The probability of exceeding at least two weeks:
$$
P(X>=2) = 1 - P(X<2) = 1 - (P(X = 0) + P(X = 1))
$$
where X is a binomial variable ~ Binomial(n=3, p=P(X <= 2000)).

We obtain that the probaiblity of exceeding at least 2 weeks is `0.9033132`.

[Back to list of exercises](#hogwarts-quests)

# 5
As they are all independent we can use the properties of Gaussian distributions.

## a
We simply sum them obtaining:
$$
A = X + Y = N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)
$$

## b
The constant 2 simply shifts the mean while 5 has to be multiplied to both mean and variance:
$$
A = 5X + 2 = N(5*\mu_1+2, 25*\sigma_1^2)
$$

It is important to not let be fooled by the variance as it requires the square value meaning that we cannot use direclty 5 but its square that is 25.

## c
We can use the same logic used in both point a and b to solve this:
$$
C = aX - bY + c^2Z = N(a*\mu_1, a^2*\sigma_1^2) - N(b*\mu_2, b^2*\sigma_2^2) + N(c^2*\mu_3, c^4*\sigma_3^2)
$$
Obtaining:
$$
C = N(a\mu_1 - b\mu_2 + c^4\mu_3, a^2\sigma_1^2 - b^2\sigma_2^2 + c^4\sigma_3^2)
$$

[Back to list of exercises](#hogwarts-quests)

# 6

## a
To solve this, we need to find the value c such that the integral of the joint PDF is equal to 1.\
We can define our problem as follows:
$$
\int_0^1 \int_0^x \frac{c \cdot y}{x} \, dy \, dx = 1
$$
The outer integral has range [0, 1] as given by the problem. The inner one is to make sure that y is in the range [0, x] following the problem interval.
It is also a way to set x to a constant value so that we can compute the integral with respect to y.

Integrating with respect to y:
$$
\int_0^x \frac{c \cdot y}{x} \, dy = \frac{c}{x} \cdot \int_0^x y \, dy = \frac{c}{x} \cdot \left[ \frac{y^2}{2} \right]_0^x = \frac{c}{x} \cdot \frac{x^2}{2} = \frac{c \cdot x}{2}
$$

Integrating with respect to x:
$$
\int_0^1 \frac{c \cdot x}{2} \, dx = \frac{c}{2} \cdot \int_0^1 x \, dx = \frac{c}{2} \cdot \left[ \frac{x^2}{2} \right]_0^1 = \frac{c}{2} \cdot \frac{1}{2}
$$

Now we simply set equal to 1:
$$
\frac{c}{4} = 1 \Rightarrow c = 4
$$

## b
If X and Y are independent, then their joint probability density function should be the same as the product of their marginal probability density functions, i.e.:
$$
f_{X,Y}(x,y) = f_X(x) * f_Y(y)
$$

We compute the integrals, by putting attention to the extremes of integration, and check the final result.
As a small note, c will be substituted by the value found in point a that is c = 4.

Marginal of X:
$$
f_X(x) = \int_0^x f_{X,Y}(x, y) \, dy = \int_0^x \frac{4 \cdot y}{x} \, dy = 2x
$$

Marginal of Y:
$$
f_Y(y) = \int_y^1 f_{X,Y}(x, y) \, dx = \int_y^1 \frac{4 \cdot y}{x} \, dx = -4y \ln(y)
$$

We obtain that:
$$
f_{X,Y}(x, y) = 4 \cdot \frac{y}{x}
$$

$$
f_X(x) \cdot f_Y(y) = (2x) \cdot (-4y \ln(y)) = -8xy \ln(y)
$$

they are clearly different meaning that `X and Y are NOT independent`.

## c
We already computed it to find out if X and Y are independent, we obtained:
$$
f_X(x) = \int_0^x f_{X,Y}(x, y) \, dy = \int_0^x \frac{4 \cdot y}{x} \, dy = 2x
$$

## d
We already computed it to find out if X and Y are independent, we obtained:
$$
f_Y(y) = \int_y^1 f_{X,Y}(x, y) \, dx = \int_y^1 \frac{4 \cdot y}{x} \, dx = -4y \ln(y)
$$

[Back to list of exercises](#hogwarts-quests)

# 7

## a
As we have 6 elements to choose from, the probability mass function of X is simply:
$$
P(X = x) = \frac{1}{6}
$$

For Y it is slightly different as the subset size is determined by x itself:
$$
P(Y = y | X = x) = \frac{1}{x}
$$
this means that we have to compute a conditional probability.

The joint probability mass function becomes:
$$
P(X = x, Y = y) = P(X=x) * P(Y=y|X=x) = \frac{1}{6} * \frac{1}{x} = \frac{1}{6x}
$$

This function is only valid when $$1 <= y <= x <= 6$$

## b
We can use the bayes rule to determine it:
$$
P(X=j|Y=i) = \frac{P(Y=i|X=j)\cdot P(X=j)}{P(Y=j)}
$$

From the previous point we already know that:
$$
P(X=j) = \frac{1}{6}
$$
$$
P(Y=i|X=j) = \frac{1}{j}
$$

what is missign now is the denominator. It is the marginal probability of Y, which is computed by summing over all possible values of X, since Y depends on X (this is crucial).
$$
P(Y = i) = \sum_{j=i}^{6} P(Y=i|X=j)\cdot P(X=j) = \frac{1}{6} \cdot \sum_{j=i}^{6} \frac{1}{j}
$$

We now have all parts obtaining:
$$
\Large P(X = j | Y = i) = \frac{1}{j} \times \frac{1}{\sum_{k=i}^{6} \frac{1}{k}}
$$

It is not written but the range of possible values has to be consisntent with the problem meanign that it shouldn't be possible to compute P(X=5,Y=6) (You can compute it but obtain a result larger than 1 meaning that it is not a possible event).

## c
We simply need to verify that
$$
P(X=x,Y=y) = P(X=x) \cdot P(Y=y)
$$

$$
P(X=x,Y=y) = \frac{1}{6x}
$$

$$
P(X=x) = \frac{1}{6}
$$

To be cleared with the following, this gives the probability of Y taking a specific value y, which is the sum of the probabilities for each j≥y. As y can be any number between 1 and 6, we have a probability of 1/6.
$$
P(Y=y) = \frac{1}{6} \cdot \sum_{j=y}^{6} \frac{1}{j}
$$

It is sufficient to see how Y is depending on other factors meaning that X and Y are depenent.

From my point of view, since the problem clearly states that the possible values of Y are constrained by X, meaning Y can only take values from 1 to X, we can immediately infer that X and Y are dependent, without doing any math.

Just to be sure, let's take x and y and see how the probabilities changes:

x = 5\
y = 3

$$
P(X=x,Y=y) = \frac{1}{6x} = \frac{1}{30}
$$

$$
P(X=x) = \frac{1}{6}
$$

$$
P(Y=y) = \frac{1}{6} \cdot \sum_{j=y}^{6} \frac{1}{j} = \frac{19}{120}
$$

$$
P(X=x) \cdot P(Y=y) = \frac{1}{6} \cdot \frac{19}{120} \neq \frac{1}{30}
$$

As said before, now we are sure that they are dependent.

[Back to list of exercises](#hogwarts-quests)