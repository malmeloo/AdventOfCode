# import nimprof;
import ../../aoclib;
import std/[strutils, sequtils, sugar, algorithm];


proc isEdge(trees: seq[seq[int]], x: int, y: int): bool =
  return (
    (x == 0) or
    (x == len(trees[0]) - 1) or
    (y == 0) or
    (y == len(trees) - 1)
  )


proc isVisible(trees: seq[seq[int]], x: int, y: int): bool =
  if isEdge(trees, x, y):
    return true;

  let treeHeight = trees[y][x];
  return (
    all(trees[y][x+1 .. ^1], x => x < treeHeight) or
    all(trees[y][0 ..< x], x => x < treeHeight) or
    all(trees[y+1 .. ^1], y => y[x] < treeHeight) or
    all(trees[0 ..< y], y => y[x] < treeHeight)
  )


proc scenicScore(trees: seq[seq[int]], x: int, y: int): int =
  let treeHeight = trees[y][x];

  result = 1;
  for i, tree in trees[y][x+1 .. ^1]:
    if tree >= treeHeight or isEdge(trees, x + i + 1, y):
      result *= (i + 1)
      break;
  for i, tree in trees[y][0 ..< x].reversed:
    if tree >= treeHeight or isEdge(trees, x - i - 1, y):
      result *= (i + 1)
      break;
  for i, tree in trees[y+1 .. ^1]:
    if tree[x] >= treeHeight or isEdge(trees, x, y + i + 1):
      result *= (i + 1)
      break;
  for i, tree in trees[0 ..< y].reversed:
    if tree[x] >= treeHeight or isEdge(trees, x, y - i - 1):
      result *= (i + 1)
      break;


proc challenge1(inp: seq[string]): int =
  let trees = inp.map(x => toSeq(x).map(y => parseInt($y)));
  
  for x in 0 .. len(trees[0]) - 1:
    for y in 0 .. len(trees) - 1:
      if isVisible(trees, x, y):
        result += 1

proc challenge2(inp: seq[string]): int =
  let trees = inp.map(x => toSeq(x).map(y => parseInt($y)));

  for x in 0 .. len(trees[0]) - 1:
    for y in 0 .. len(trees) - 1:
      result = max(result, scenicScore(trees, x, y));


let inp = getInput("input.txt");
echo(challenge1(inp));
echo(challenge2(inp));
