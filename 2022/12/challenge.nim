import ../../aoclib
import std/[sugar, sequtils];


proc prepareMap(inp: var seq[string]): ((int, int), (int, int)) =
  for y, row in inp:
    for x, col in row:
      if col == 'S':
        result[0] = (x, y)
        inp[y][x] = 'a'
      elif col == 'E':
        result[1] = (x, y)
        inp[y][x] = 'z'


proc neigh(map: seq[string], pos: (int, int)): seq[(int, int)] =
  [
    (pos[0]+1, pos[1]),
    (pos[0]-1, pos[1]),
    (pos[0], pos[1]+1),
    (pos[0], pos[1]-1),
  ].filter(c => (
    c[0] >= 0 and
    c[0] < len(map[0]) and
    c[1] >= 0 and
    c[1] < len(map)
  ))


proc canTravel(map: seq[string], pos1: (int, int), pos2: (int, int), goUp: bool): bool =
  if goUp:
    (ord(map[pos2[1]][pos2[0]]) - ord(map[pos1[1]][pos1[0]])) <= 1
  else:
    (ord(map[pos2[1]][pos2[0]]) - ord(map[pos1[1]][pos1[0]])) >= -1


proc challenge1(inp: seq[string], startPos: (int, int), endPos: (int, int)): int =
  var
    visited: seq[(int, int)] = @[]
    toExplore: seq[(int, int)] = @[startPos]
  
  while len(toExplore) > 0:
    for i in 1 .. len(toExplore):
      if toExplore[0] == endPos:        
        return

      visited.add(toExplore[0])
      let neighbors = neigh(inp, toExplore[0])
      for neighbor in neighbors:
        if neighbor in visited or neighbor in toExplore:
          continue
        if not canTravel(inp, toExplore[0], neighbor, true):
          continue

        toExplore.add(neighbor)

      toExplore.delete(0)
    
    result += 1


proc challenge2(inp: var seq[string], startPos: (int, int)): int =
  var
    visited: seq[(int, int)] = @[]
    toExplore: seq[(int, int)] = @[startPos]
  
  while len(toExplore) > 0:
    for i in 1 .. len(toExplore):
      let cur = toExplore[0]
      if inp[cur[1]][cur[0]] == 'a':        
        return

      visited.add(cur)
      let neighbors = neigh(inp, cur)
      for neighbor in neighbors:
        if neighbor in visited or neighbor in toExplore:
          continue
        if not canTravel(inp, cur, neighbor, false):
          continue

        toExplore.add(neighbor)

      toExplore.delete(0)
    
    result += 1


var inp = getInput("input.txt")
var (startPos, endPos) = prepareMap(inp)

echo(challenge1(inp, startPos, endPos))
echo(challenge2(inp, endPos))
