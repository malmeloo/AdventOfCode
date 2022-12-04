import ../../aoclib
import std/strutils;


proc charScore(character: char): int =
  if isUpperAscii(character):
    ord(character) - ord('A') + 27
  else:
    ord(character) - ord('a') + 1


proc challenge1(inp: seq[string]): int =
  for sack in inp:
    for item in sack[0 .. len(sack) div 2 - 1]:
      if item in sack[len(sack) div 2 .. ^1]:
        result += charScore(item)
        break


proc challenge2(inp: seq[string]): int =
  for i in countup(0, len(inp) - 3, 3):
    for item in inp[i]:
      if item in inp[i+1] and item in inp[i+2]:
        result += charScore(item)
        break;


let inp = getInput("input.txt")
echo(challenge1(inp))
echo(challenge2(inp))
