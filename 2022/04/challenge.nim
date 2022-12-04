import std/[strutils, sequtils, sugar, re];

proc getInput(filename: string): seq[string] =
  let path: string = rsplit(currentSourcePath(), "/", maxsplit=1)[0]
  let f = open(path & "/" & filename)
  defer: f.close()

  result = @[]
  while true:
    try:
      result.add(readLine(f))
    except EOFError:
      return


proc challenge1(inp: seq[string]): int =
  for assignments in inp:
    var a = assignments.split(",").map(ass => ass.split("-").map(x => parseInt(x)))
    if (a[0][0] >= a[1][0] and a[0][1] <= a[1][1]) or (a[1][0] >= a[0][0] and a[1][1] <= a[0][1]):
      result += 1


proc challenge2(inp: seq[string]): int =
  for assignments in inp:
    var a = assignments.split(",").map(ass => ass.split("-").map(x => parseInt(x)))
    if min(a[0][1], a[1][1]) >= max(a[0][0], a[1][0]):
      result += 1


let inp = getInput("input.txt")
echo(challenge1(inp))
echo(challenge2(inp))
