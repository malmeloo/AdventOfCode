import ../../aoclib
import std/[sets, strutils, sugar, sequtils];


proc drawMap(inp: seq[string]): HashSet[(int, int)] =
  for line in inp:
    let edges = line.split(" -> ").map(coord => coord.split(",").map(parseInt))
    var lastEdge = edges[0]
    for edge in edges[1 .. ^1]:
      for x in min(lastEdge[0], edge[0]) .. max(lastEdge[0], edge[0]):
        for y in min(lastEdge[1], edge[1]) .. max(lastEdge[1], edge[1]):
          result.incl((x, y))
      
      lastEdge = edge


proc calcSand(sandMap: HashSet[(int, int)], bottom: int): (int, int) =
  result = (500, 0)
  while result[1] < bottom-1:
    let directions = [(result[0]-1, result[1]+1), (result[0], result[1]+1), (result[0]+1, result[1]+1)]
    if directions[1] notin sandMap:  # down
      result = directions[1]
    elif directions[0] notin sandMap:  # down left
      result = directions[0]
    elif directions[2] notin sandMap:  # down right
      result = directions[2]
    else:  # no way to go
      return result


proc mapBottom(sandMap: HashSet[(int, int)]): int =
  for coord in sandMap:
    if coord[1] > result: result = coord[1]
  
  result += 2


proc challenge1(inp: seq[string]): int =
  var sandMap = drawMap(inp)
  let bottom = mapBottom(sandMap)
  
  var sandPos = calcSand(sandMap, bottom)
  while sandPos[1] < bottom-1:
    sandMap.incl(sandPos)
    result += 1

    sandPos = calcSand(sandMap, bottom)


proc challenge2(inp: seq[string]): int =
  var sandMap = drawMap(inp)
  let bottom = mapBottom(sandMap)
  
  var sandPos = calcSand(sandMap, bottom)
  while sandPos != (500, 0):
    sandMap.incl(sandPos)
    result += 1

    sandPos = calcSand(sandMap, bottom)
  result += 1


let inp = getInput("input.txt")
echo(challenge1(inp))
echo(challenge2(inp))
