import strutils

proc getInput*(filename: string): seq[string] =
  let path: string = rsplit(currentSourcePath(), "/", maxsplit=1)[0]
  let f = open(path & "/" & filename)
  defer: f.close()

  result = @[]
  while true:
    try:
      result.add(readLine(f))
    except EOFError:
      return
