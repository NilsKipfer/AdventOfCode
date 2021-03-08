import re

with open("G:\\Dokumente\\Projects\\AdventOfCode\\2020\\DaySeven2020\\seven.txt") as f:
    lines = f.readlines()

graph = {}


for i in lines:
    regex = re.match('(.+?) bags contain', i)
    color_primary = regex.group(1)
    color_inside = re.findall('(\d+) (.+?) bag', i)
    if len(color_inside) > 0:
        color_inside = color_inside
        graph[color_primary] = color_inside
    else:
        graph[color_primary] = []

def shiny_gold(color):
    if color == "shiny gold":
        return True
    else:
        return any(shiny_gold(child) for amount, child in graph[color])

print("part 1: ", sum(shiny_gold(color) for color in graph.keys())-1)

def count(color):
    return 1 + sum(int(amount)*count(child) for amount, child in graph[color])

print("part 2: ", count("shiny gold") - 1)