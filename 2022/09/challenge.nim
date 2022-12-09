import ../../aoclib
import std/[strutils, tables, sets];


let MOV = {
  'U': (0, 1),
  'D': (0, -1),
  'L': (-1, 0),
  'R': (1, 0)
}.toTable


proc newPos(oldHeadPos: array[2, int], movement: char): array[2, int] =
  return [oldHeadPos[0] + MOV[movement][0], oldHeadPos[1] + MOV[movement][1]];


proc connect(head: array[2, int], tail: array[2, int]): array[2, int] =
  result = tail;
  if (
    (tail[0] < head[0]-1) or
    (tail[0] > head[0]+1) or
    (tail[1] < head[1]-1) or
    (tail[1] > head[1]+1)
  ):
    let xDir = (if tail[0] < head[0]: 1 elif tail[0] > head[0]: -1 else: 0)
    let yDir = (if tail[1] < head[1]: 1 elif tail[1] > head[1]: -1 else: 0)
    return [tail[0] + xDir, tail[1] + ydir];


proc challenge1(inp: seq[string]): int =
  var
    tailLocations = initHashSet[array[2, int]]()
    headPos: array[2, int]
    tailPos: array[2, int]
  for line in inp:
    let command = line.split(" ");
    for _ in 1 .. parseInt(command[1]):
      headPos = newPos(headPos, command[0][0]);
      tailPos = connect(headPos, tailPos);

      tailLocations.incl(tailPos)
  
  return len(tailLocations);


proc challenge2(inp: seq[string]): int =
  var
    tailLocations = initHashSet[array[2, int]]()
    knots: array[10, array[2, int]];
  
  for line in inp:
    let command = line.split(" ");
    for _ in 1 .. parseInt(command[1]):
      knots[0] = newPos(knots[0], command[0][0])

      for i, knot in knots[1 .. ^1]:
        knots[i + 1] = connect(knots[i], knot)

      tailLocations.incl(knots[^1])
  
  return len(tailLocations);


let inp = getInput("input.txt")
echo(challenge1(inp))
echo(challenge2(inp))
