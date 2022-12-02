import std/[strutils, sequtils, sugar];


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
  result = 0
  for round in inp:
    var opp = ord(round[0]) - ord('A')
    var me = ord(round[2]) - ord('X')
    result += me + 1
    if (opp + 1) mod 3 == me:
      result += 6
    elif opp == me:
      result += 3


let inp = getInput("input.txt")
echo challenge1(inp)

# I lost the original so you're gonna have to do with this one-liner
echo inp.map(r=>3*ord(r[2])-263+(ord(r[2])+ord(r[0])-151)mod 3).foldl(a+b)
