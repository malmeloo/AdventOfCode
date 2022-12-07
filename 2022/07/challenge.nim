# import nimprof;
import ../../aoclib;
import std/[strutils, sequtils, tables, os, sugar, algorithm];


proc parseDirs(inp: seq[string]): Table[string, int] =
  var curDir = ""

  for line in inp:
    let params = line.split(" ");
    if params[0] != "$" and params[0] != "dir":
      result[curDir] = result.getOrDefault(curDir, 0) + parseInt(params[0]);
    
    if params[1] == "cd":
      # echo "cd to ", params[2], " (was ", curDir, ")"
      if params[2] == "/":
        curDir = ""
      elif params[2] == "..":
        curDir = curDir.rsplit("/", maxsplit=1)[0]
      else:
        if curDir != "":
          curDir = curDir & "/";
        curDir = curDir & params[2]


proc dirSize(inp: Table[string, int], dir: string): int =
  for dirname in inp.keys:
    if dirname.startsWith(dir):
      result += inp[dirname];


proc challenge1(inp: seq[string]): int =
  let dirs = parseDirs(inp);
  
  for dirname in dirs.keys:
    let size = dirSize(dirs, dirname)
    
    echo dirname, " --> ", dirs[dirname]
    if size <= 100000:
      result += size;
  echo ""


proc challenge2(inp: seq[string]): int =
  let dirs = parseDirs(inp);

  var dirSizes = initTable[string, int]();
  for dirname in dirs.keys:
    let size = dirSize(dirs, dirname)
    dirSizes[dirname] = size;
  
  let sortedSizes = toSeq(dirSizes.pairs).sorted((a, b) => cmp(a[1], b[1]));
  let toFree = 30_000_000 - (70_000_000 - dirSizes[""]);
  for dir in sortedSizes:
    let (_, size) = dir;
    if size >= toFree:
      return size


let inp = getInput("input.txt");
echo(challenge1(inp));
echo(challenge2(inp));
