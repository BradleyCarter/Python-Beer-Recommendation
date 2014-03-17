# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:05:16 2014

@author: BradC
"""

import pandas as pd
beers = pd.read_csv("C:/Users/BradC/Downloads/beer_reviews/beer_reviews.csv")

#Want to build a beer classifier.
#I'm going to need to into the reviews database and find where the same person
#has reviewed two different beers.
#We want to hold as many things as possible constant so we get a nice recommendation system.

#I would say that the style of the beer is probably going to be the most important thing
#for recommending similar beers. So maybe we want to look outside of that style.
#Oh, you like Bell's Oberon? Have you tried this beautiful peanut butter porter?

