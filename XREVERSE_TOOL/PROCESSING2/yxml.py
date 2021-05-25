#!/usr/bin/env python
#coding: utf-8

import yaml
from yaml import load
from sys import stdin, stdout, stderr, exit
from xml.etree.ElementTree import Element, ElementTree
from optparse import OptionParser

parser = OptionParser(usage="%prog [options] [filename]")
parser.add_option("-e", dest="encoding", default='UTF-8',
    help="target XML encoding (default: UTF-8)")
parser.add_option("-r", dest="root", default=None,
    help="root element's tag (default: 'yaml', used only if there are " +
    "multiple root elements in the input file)")
parser.add_option("-o", dest="output", default=None,
    help="write output to a file named OUTPUT (default: standard output)")
parser.add_option("-n", dest="newline", default=True, action="store_false",
    help="don't add a new line character at the end")
(options, args) = parser.parse_args()

def list_to_elem(key, input):
  root = Element(key)
  singular = key[0:-1] if key[-1] == "s" else "child"
  for val in input:
    root.append(to_elem(singular, val))
  return root

def dict_to_elem(key, input):
  root = Element(key)
  for (key, val) in input.items():
    root.append(to_elem(key, val))
  return root

def to_elem(key, input):
  if isinstance(input, list):
    return list_to_elem(key, input)
  elif isinstance(input, dict):
    return dict_to_elem(key, input)
  else:
    elem = Element(key)
    elem.text = str(input)
    return elem

if len(args) > 1:
  parser.print_help(stderr)
  exit(1)

input = open(args[0], "r") if any(args) and args[0] != "-" else stdin
inputRead = input.read()
inputStream = yaml.load(inputRead, Loader=yaml.FullLoader)
element = to_elem(options.root or 'yaml', inputStream)
if not options.root and len(list(element)) == 1:
  element = list(element)[0]
output = open(options.output, "w") if options.output else stdout
ElementTree(element).write(output, options.encoding)
if options.newline:
  output.write("\n")
