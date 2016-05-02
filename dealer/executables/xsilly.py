import os, sys, json, xsilly_tester

def main():
  configChoi = json.load(sys.stdin)
  output = xsilly_tester.xsilly_tester(configChoi)
  print output

main()
