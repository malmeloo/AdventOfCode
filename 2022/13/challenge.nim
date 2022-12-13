import ../../aoclib
import std/[json, sequtils, sugar, algorithm];


proc compare(cmp1: JsonNode, cmp2: JsonNode): int =
  # echo "Compare ", cmp1, " & ", cmp2
  for i in 0 .. min(len(cmp1), len(cmp2)) - 1:
    # echo "  Check ", cmp1[i], " & ", cmp2[i]
    var item1 = cmp1[i]
    var item2 = cmp2[i]

    if item1.kind == JInt and item2.kind == JInt:
      if item1.getInt() < item2.getInt():
        return 1
      elif item1.getInt() > item2.getInt():
        return -1
      continue
    elif item1.kind != JArray:
      item1 = %([item1])
    elif item2.kind != JArray:
      item2 = %([item2])
    
    let status = compare(item1, item2)
    if status != 0:
      return status
  
  if len(cmp1) < len(cmp2):
    return 1
  elif len(cmp1) > len(cmp2):
    return -1
  return 0


proc challenge1(inp: seq[string]): int =
  for i, line in inp:
    if line == "" or i == high(inp):
      let ind = (if i == high(inp): i + 1 else: i)

      let node1 = parseJson(inp[ind - 2])
      let node2 = parseJson(inp[ind - 1])
      if compare(node1, node2) == 1:
        result += ind div 3 + 1


proc challenge2(inp: seq[string]): int =
  var nodes = inp.filter(line => line != "").map(line => parseJson(line))
  var div1 = %([[2]])
  var div2 = %([[6]])

  nodes.add(div1)
  nodes.add(div2)

  nodes.sort(compare, order=SortOrder.Descending)

  result = 1
  for i, node in nodes:
    if node == div1 or node == div2:
      result *= (i + 1)


let inp = getInput("input.txt")
echo(challenge1(inp))
echo(challenge2(inp))
