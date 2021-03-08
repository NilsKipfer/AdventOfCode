with open("G:\\Dokumente\\Projects\\AdventOfCode\\2020\\DaySix2020\\antworten.txt") as f:   ## G:\\Dokumente\\Projects\\AdventOfCode\\2020\\DaySix2020\\antworten.txt
    answer_ugly = f.read().split("\n\n")

from functools import reduce

counter_union = 0
counter_intersection = 0
for a in answer_ugly:
    answer_union = reduce(set.union, map(set, a.split())) # denk an Mengenlehre (Verbunden mit)
    counter_union += len(answer_union)
    answer_intersection = reduce(set.intersection, map(set, a.split())) # denk an Mengenlehre (Gerschnitten mit)
    counter_intersection += len(answer_intersection)
print(counter_union)
print(counter_intersection)