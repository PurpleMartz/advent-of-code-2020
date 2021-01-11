# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 00:26:49 2021

@author: Marty
"""

# Not the most efficient or readable solution :X
data = open("Problem 16 Data.txt", "r").read()
[rules, myTicket, nearbyTickets] = data[:-1].split('\n\n')

# PART 1
def getRanges(rule):
    ranges = rule.split(' or ')
    ranges = list(map(lambda x: [int(y) for y in  x.split('-')], ranges))
    ranges = set(range(ranges[0][0], ranges[0][1] + 1)).union(range(ranges[1][0], ranges[1][1] + 1))
    return ranges

rulesRanges = list(map(lambda x: x.split(': ')[1], rules.split('\n')))
nRules = len(rulesRanges)
rulesRanges = [getRanges(ruleRange) for ruleRange in rulesRanges]
rulesRangeAll = set().union(*rulesRanges)
nearbyTickets = nearbyTickets.replace('nearby tickets:\n', '').split('\n')
candidates = [list(range(nRules)) for _ in range(nRules)]
for ticket in nearbyTickets:
    ticketCandidates = []
    fields = ticket.split(',')
    for ind in range(nRules):
        field = int(fields[ind])
        if field in rulesRangeAll:
            # Finds which labels can potentially correspond to this field
            ticketCandidates.append([idx for idx in list(range(nRules)) if field in rulesRanges[idx]])
        else:
            # Handles invalid tickets (47 of them).
            ticketCandidates = None
            break            
    if ticketCandidates != None:
        candidates = [list(set(candidates[i]).intersection(ticketCandidates[i])) for i in range(nRules)]

# Informed solution: starting from the shortest list of options, an unambigious solution can be derived
# Sort by length of possible matching fields
indexOrder = sorted(range(nRules), key=lambda k: len(candidates[k]))
matchedSet = set() # contains all matched fields
fieldNames = list(map(lambda x: x.split(': ')[0], rules.split('\n')))
matches = dict()
for index in indexOrder:
    possibleMatches = set(candidates[index]) - matchedSet
    if len(possibleMatches) == 1:
        match = possibleMatches.pop()
        matches[fieldNames[match]] = index
        matchedSet.add(match)
    else:
        raise Exception("Ambiguous!")

# Can sort the mathces
# matches = dict(sorted(matches.items(), key=lambda item: item[1]))

myTicket = myTicket.replace('your ticket:\n', '').split(',')
myTicket = [int(x) for x in myTicket]

departureFields = [field for field in fieldNames if field.startswith('departure ')]
product = 1
for departureField in departureFields:
    product *= myTicket[matches[departureField]]

print("PART 2:", product)

"""
--- Day 16: Ticket Translation ---
As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!

Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?

Your puzzle answer was 29851.

--- Part Two ---
Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?

Your puzzle answer was 3029180675981.

Both parts of this puzzle are complete! They provide two gold stars: **
"""