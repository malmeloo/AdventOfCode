import std/[strutils, os]

proc getInput*(filename: string): seq[string] =
  let path: string = getAppFilename().parentDir()
  let f = open(path & "/" & filename)
  defer: f.close()

  result = @[]
  while true:
    try:
      result.add(readLine(f))
    except EOFError:
      return
