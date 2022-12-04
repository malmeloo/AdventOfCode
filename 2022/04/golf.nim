import ../../aoclib
import std/[strutils, sequtils, sugar, re];

proc challenge1(inp: seq[string]): int =
  len(inp.map(a=>findAll(a, re"\d+").map(parseInt)).filter(a=>(a[0]>=a[2] and a[1]<=a[3]) or (a[2]>=a[0] and a[3]<=a[1])))

proc challenge2(inp: seq[string]): int =
  len(inp.map(a=>findAll(a, re"\d+").map(parseInt)).filter(a=>min(a[1],a[3])>=max(a[0],a[2])))

let inp = getInput("input.txt")
echo(challenge1(inp))
echo(challenge2(inp))