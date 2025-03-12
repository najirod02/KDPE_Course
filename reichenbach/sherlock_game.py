#!/usr/bin/env python3
'''
Holmes and Moriarty duel with a device spitting integers from 1 to 100. 
Holmes adds to S (from 0) until S > 100, noting his last number x. 
Moriarty resumes, adding until S > 200, noting y. 
The higher wins. 
Simulate 100,000 rounds in Python 3 and estimate Moriarty’s victory odds, 
as if outsmarting Holmes at Reichenbach.
'''

import random

'''
the function simulates a single game round.
it will be called 'num_simulations' times

Returns true only if holmes wins that is, the value of x is strictly larger
than the values of y, the last number extracted from moriarty
'''
def simulate_round():
    #first it's the turn of holmes
    S = 0
    while S <= 100:
        x = random.randint(1, 100)
        S += x
    #we have gone beyond 100 and x contains the last element extracted at random
    
    #moriarty turn
    while S <= 200:
        y = random.randint(1, 100)
        S += y
    #we have gone beyond 200 and y contains the last element extracted at random
    
    #True if holmes wins
    #False otherwise
    return x > y

def simulate_rounds(num_simulations=100000):
    moriarty_wins = 0
    for _ in range(num_simulations):
        if(simulate_round()):
            moriarty_wins += 1

    #to estimate the probability simply divide the number of moriarty wins
    #with the number of games played
    victory_odds = moriarty_wins / num_simulations
    print(f"Estimated Moriarty's victory odds: {victory_odds:.4f}")

if __name__ == '__main__':
    simulate_rounds()
    #it turns out that Holmes has much more possibility to win the game (~54%)!