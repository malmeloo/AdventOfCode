import ../../aoclib
import std/[strutils, sequtils, sugar, algorithm];


type Monkey = object
  items: seq[int]
  op: char
  opNum: int
  test: int
  nextMonkey: array[2, int]

  inspectCount: int

proc newWorry(m: Monkey, item: int): int =
  result = item
  let op2 = (if m.opNum != -1: m.opNum else: item)
  if m.op == '*':
    result *= op2
  elif m.op == '+':
    result += op2
  
  result = result

proc findNextMonkey(m: Monkey, item: int): int =
  if item mod m.test == 0:
    return m.nextMonkey[0]
  return m.nextMonkey[1]


proc parseMonkeys(inp: seq[string]): seq[Monkey] =
  for line in inp:
    if line.startsWith("Monkey"):
      result.add(Monkey())
    elif "items" in line:
      result[^1].items = line.split(": ")[^1].split(", ").map(parseInt)
    elif "Operation" in line:
      let ops = line.split(" ")
      result[^1].op = ops[^2][0]
      result[^1].opNum = (if ops[^1] != "old": ops[^1].parseInt else: -1)
    elif "Test" in line:
      result[^1].test = line.split(" ")[^1].parseInt
    elif "true" in line:
      result[^1].nextMonkey[0] = line.split(" ")[^1].parseInt
    elif "false" in line:
      result[^1].nextMonkey[1] = line.split(" ")[^1].parseInt


proc iterMonkeys(inp: seq[string], cycles: int, divByThree: bool): seq[int] =
  var monkeys = parseMonkeys(inp)
  let maxWorry = monkeys.map(m => m.test).foldl(a * b)

  for _ in 1 .. cycles:
    for i, monkey in monkeys:
      for _ in 1 .. len(monkey.items):
        var worry = monkey.items[0]
        worry = monkey.newWorry(worry)
        if divByThree:
          worry = worry div 3
        worry = worry mod maxWorry
        
        monkeys[monkey.findNextMonkey(worry)].items.add(worry)
        monkeys[i].items.delete(0)
        monkeys[i].inspectCount += 1
  
  return monkeys.map(m => m.inspectCount)


proc challenge1(inp: seq[string]): int =
  var monkeys = iterMonkeys(inp, 20, true)
  
  return sorted(monkeys, order=SortOrder.Descending)[0 .. 1].foldl(a * b)


proc challenge2(inp: seq[string]): int =
  var monkeys = iterMonkeys(inp, 10000, false)

  return sorted(monkeys, order=SortOrder.Descending)[0 .. 1].foldl(a * b)


let inp = getInput("input.txt")
echo(challenge1(inp))
echo(challenge2(inp))
