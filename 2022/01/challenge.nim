import std/[strutils, parseutils, algorithm];


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
  result = 0;
  var sum = 0;
  for line in inp:
    if line == "":
      if sum > result:
        result = sum;
      sum = 0;
      continue

    sum += parseInt(line);


proc challenge2(inp: seq[string]): int =
  var values: seq[int] = @[];

  var sum = 0;
  for line in inp:
    if line == "":
      values.add(sum);
      sum = 0;
      continue
    sum += parseInt(line)

  values.sort(SortOrder.Descending)
  return values[0] + values[1] + values[2]


let inp = getInput("input.txt")
echo(challenge1(inp))
echo(challenge2(inp))
