#!/usr/bin/python
#
# Copyright 2014 Vasilis Vontikakis  website(www.vontikakis.com)
#
# Problem optimize marketing budget for conversion rates of your product/service by 
# using pay per click providers like adwords search, adwords display network,
# facebooks ads and linkedin ads, # we model the problem as 
# linear mathematical program in python  and pulp solver was for solving linear program
#
# objective fucntion: maximize conversion rates
# desicion variables: amount to spend in each provider
# constraints: 
# maximum budget per ppc provider is 500 euros
# maximum Total budget is 1800 euros
# program dependency is pulp solver https://code.google.com/p/pulp-or/

from pulp import *

# initialize the model maximize conversion rate 
marketing_budget = pulp.LpProblem('Pay Per Click Budget Optimization', pulp.LpMaximize)

# list of ppc providers
ppc_providers = ['Adwords_Search', 'Adwords_Display', 'Facebook_Ads', 'Linkedin_Ads']

# the decision variables that will be spend in every ppc provider 
x = pulp.LpVariable.dict('x_%s', ppc_providers, lowBound =0)

# average cost per click by ppc provider 0.55 eurs etc
avg_cpc = dict(zip(ppc_providers, [0.55, 0.35, 0.75, 0.60]))

# average conversion rates by ppc provider
avg_conv_rate = dict(zip(ppc_providers, [0.11, 0.10, 0.08, 0.14]))

# objective function max conversion rates
marketing_budget += sum([ (x[i]*avg_cpc[i])*avg_conv_rate[i] for i in ppc_providers])

# total budget constraint < 1800 euros
marketing_budget += sum([ x[i] for i in ppc_providers]) <= 1800

# adwords search contstraing  equal or less than 500 euros
marketing_budget += x['Adwords_Search'] <= 500

marketing_budget += x['Adwords_Display'] <= 500

marketing_budget += x['Facebook_Ads'] <= 500

marketing_budget += x['Linkedin_Ads'] <= 500


#we using the default solver
marketing_budget.solve()

#print the result
for ppc_provider in ppc_providers:
	print 'The amount of euros for %s is %s '%(ppc_provider,x[ppc_provider].value())