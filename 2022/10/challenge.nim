import ../../aoclib
import std/[strutils];


proc challenge1(inp: seq[string]): int =
  var
    reg = 1
    cycle = 1
    inpPtr = 0
    setCmd = (0, 0)
  
  while inpPtr < len(inp):
    if setCmd == (0, 0):
      let cmds = inp[inpPtr].split(" ")
      if cmds[0] == "noop":
        inpPtr += 1
      elif cmds[0] == "addx":
        setCmd = (cycle + 1, parseInt(cmds[1]))

    if (cycle - 20) mod 40 == 0:
      result += reg * cycle

    if cycle == setCmd[0]:
      reg += setCmd[1]
      setCmd = (0, 0)
      inpPtr += 1
    
    cycle += 1


proc challenge2(inp: seq[string]): string =
  var
    reg = 1
    cycle = 1
    inpPtr = 0
    setCmd = (0, 0)
  
  while inpPtr < len(inp):
    if setCmd == (0, 0):
      let cmds = inp[inpPtr].split(" ")
      if cmds[0] == "noop":
        inpPtr += 1
      elif cmds[0] == "addx":
        setCmd = (cycle + 1, parseInt(cmds[1]))
    
    let crtPos = cycle - 1
    if crtPos mod 40 == 0:
      result.add("\n")
    if crtPos mod 40 >= reg - 1 and crtPos mod 40 <= reg + 1:
      result.add("##")
    else:
      result.add("  ")

    if cycle == setCmd[0]:
      reg += setCmd[1]
      setCmd = (0, 0)
      inpPtr += 1
    
    cycle += 1


let inp = getInput("input.txt")
echo(challenge1(inp))
echo(challenge2(inp))
