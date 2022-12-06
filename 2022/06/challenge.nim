# import nimprof;
import ../../aoclib;
import std/[sugar, sequtils]


proc challenge1(inp: seq[string]): int =
  toSeq(3..<inp[0].len).filter(i=>deduplicate(inp[0][i-3..i]).len==4)[0]+1

proc challenge2(inp: seq[string]): int =
  toSeq(13..<inp[0].len).filter(i=>deduplicate(inp[0][i-13..i]).len==14)[0]+1

let inp = getInput("input.txt");
echo(challenge1(inp));
echo(challenge2(inp));
