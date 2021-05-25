#!/usr/bin/env python

import sys
import yaml
import string
import re
import os

patternStr = r"(GameObject)_((\d+)_ID(\d+))"  #Objects da filtrare
pattern2Str = r"m_Name" #attributo da salvare

def out (s):
    sys.stdout.write(s)

uniq = 1

def getID():
    global uniq
    n = str(uniq)
    uniq += 1
    return n

def asAttr(attr, val):
    escaped = string.replace(val, '\"', '\\\"')  # " -> \"
    return " [" + attr + "=\"" + escaped + "\"]"

def render(ast, name=None):
    if name is None:
        name = getID()

    lab = ""
    color = "red"
    style = "filled"
    edges = []  # (from, to, attr)

    if type(ast) is dict: #renderizzo la root
        for key,val in ast.iteritems():
            containsPattern = re.search(patternStr, key)
            if containsPattern: #grafico solo gameobjects (generico)
                if type(val) is dict:
                    child = getID()
                    edges.append((name, child, asAttr("label", ""))) #archi che vanno da root a gameobject
                    render2(val, key, child) #vado ad analizzare i figli dei gameobject, passo il nome del nodo come param
    
                else:
                    lab += (str(key) + ": " + str(val) + "\\n")

    else:
        lab += str(ast)

    # output vertex
    out(name + asAttr("label", lab) + asAttr("color", color)+ asAttr("style", style) + ";\n" )

    # output edges
    for (src, dest, attr) in edges:
        out(src + " -> " + dest + attr + ";\n")

def render2(ast, nodo, name=None): #renderizzo i gameobjects
    if name is None:
        name = getID()

    lab = ""
    color = "lightskyblue1"
    style = "rounded,filled"
    shape = "box"
    edges = []  # (from, to, attr)

    if type(ast) is dict:
        for key,val in ast.iteritems():

            if type(val) is dict: #se hanno file collegati come attributi (fileid=0)
                child = getID()
                contains2Pattern = re.search(pattern2Str, key)
                if contains2Pattern:
                    lab += (str(key) + ": " + str(val) + "\\n")
                
            elif type(val) is list: #se hanno file collegati come component, renderizzo i componenti
                last = None
                for i in val:
                    child = getID()
                    edges.append((name, child, asAttr("label", "")))
                    render3(i, child)

            else: #se hanno attributi 
                contains2Pattern = re.search(pattern2Str, key)
                if contains2Pattern:
                    lab += (str(nodo) + "\\n") #leggo nome del padre
                    lab += (str(val) + "\\n")

    else:
        lab += str(ast)

    # output vertex
    out(name + asAttr("label", lab) + asAttr("color", color)+ asAttr("style", style) + asAttr("shape", shape) + ";\n" )

    # output edges
    for (src, dest, attr) in edges:
        out(src + " -> " + dest + attr + ";\n")

def render3(ast, name=None): #rendering dei componenti
    if name is None:
        name = getID()

    lab = ""
    color = "lightpink"
    style = "rounded,filled"
    shape = "box"
    edges = []  # (from, to, attr)

    if type(ast) is dict:
        for key,val in ast.iteritems():

            if type(val) is dict:
                child = getID()
                lab += (str(val) + "\\n")
                
            elif type(val) is list:
                last = None
                for i in val:
                    child = getID()
                    edges.append((name, child, asAttr("label", key)))
                    render(i, child)

            else:
                lab += (str(key) + ": " + str(val) + "\\n")

    else:
        lab += str(ast)

    # output vertex
    out(name + asAttr("label", lab) + asAttr("color", color)+ asAttr("style", style) + asAttr("shape", shape) + ";\n" )

    # output edges
    for (src, dest, attr) in edges:
        out(src + " -> " + dest + attr + ";\n")


######################
# "main"

# check args
myself = sys.argv[0]
if len(sys.argv) != 2:
    print "error: invalid number of arguments."
    print "usage:\t" + myself + " [path to YAML file]"
    sys.exit(1)

infile = sys.argv[1]

with open(infile, 'r') as stream:
    try:
        ast = yaml.load(stream, Loader=yaml.FullLoader)

        out ("digraph graphname {\n")

        render(ast)

        out ("}\n")

    except yaml.YAMLError as exc:
        print("pyYAML Parsing Error:")
        print(exc)
        sys.exit(1)
