import std/[sequtils, sugar];

echo readLines("input.txt", 2500).map(r=>3*ord(r[2])-263+(ord(r[2])+ord(r[0])-151)mod 3).foldl(a+b)