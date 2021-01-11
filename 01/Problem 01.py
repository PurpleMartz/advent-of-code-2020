# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 00:00:11 2020

@author: Marty
"""

data = open("Problem 01 Data.txt", "r").read()
data = data[:-1].split('\n')
numbers = [int(x) for x in data]

# PART 1: Looks for all pairs
target = 2020
targetHalf = target//2
# Finds all values x such that target - x is also present in the list.
goodnums = {target - x for x in numbers if x <= targetHalf} & {x for x in numbers if x > targetHalf}
pairs = {(target - x, x) for x in goodnums}
if len(pairs) < 1:
    raise Exception("No answer!")
if len(pairs) > 1:
    raise Exception("More than one possible answer!")
pair = next(iter(pairs))
print("PART 1:", pair[0] * pair[1])

# PART 2: Looks for the first match
numbers.sort()
# Fixes the first element (one by one) and finds the other two elements
for i in range(0, len(numbers) - 2): 
    # To find the other two elements, make two index variables from 
    # two corners of the array and move them toward each other
    left = i + 1 
    right = len(numbers) - 1 
    while left < right: 
        if numbers[i] + numbers[left] + numbers[right] == target: 
            triplet = (numbers[i], numbers[left], numbers[right])
            break
        elif numbers[i] + numbers[left] + numbers[right] < target: 
            left += 1
        else:
            right -= 1
if len(triplet) < 1:
  raise Exception("No answer!")
print("PART 2:", triplet[0] * triplet[1] * triplet[2])


"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

Your puzzle answer was 898299.

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 143933922.

Both parts of this puzzle are complete! They provide two gold stars: **
"""