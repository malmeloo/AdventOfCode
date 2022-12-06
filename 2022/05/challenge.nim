# import nimprof;
import ../../aoclib;
import std/[strutils, sequtils, parseutils, re];


let numRe = re"\d+";


proc parseCrates(inp: seq[string]): (seq[seq[char]], seq[string]) =
  let stacks = (len(inp[0]) + 1) div 4;
  for i in countup(1, stacks):
    result[0].add(@[]);

  var ruleBound = 0;
  for ind, line in inp:
    if line == "":
      ruleBound = ind;
      break;
    
    for i in countup(1, stacks * 4, 4):
      if line[i] != ' ':
        result[0][i div 4].insert(line[i]);
  
  result[1] = inp[ruleBound + 1 .. ^1];


proc challenge1(inp: seq[string]): string =
  var (crates, rules) = parseCrates(inp);

  for line in rules:
    # let rule = findAll(line, numRe).map(parseInt);
    let rule = line.split(" ")

    for _ in countup(1, parseInt(rule[1])):
      let crate = pop(crates[parseInt(rule[3]) - 1]);
      crates[parseInt(rule[5]) - 1].add(crate);
  
  return crates.map(proc(x: seq[char]): char = x[^1]).join

proc challenge2(inp: seq[string]): string =
  var (crates, rules) = parseCrates(inp);

  for line in rules:
    let rule = line.split(" ")
    let insPos = len(crates[parseInt(rule[5]) - 1]);

    for _ in countup(1, parseInt(rule[1])):
      let crate = pop(crates[parseInt(rule[3]) - 1]);
      crates[parseInt(rule[5]) - 1].insert(crate, insPos);
  
  return crates.map(proc(x: seq[char]): char = x[^1]).join


let inp = getInput("input.txt");
echo(challenge1(inp));
echo(challenge2(inp));
