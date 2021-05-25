#!/bin/bash
cd /Users/alessandrocascino/Desktop/XREVERSE_TOOL/PROCESSING2
for f in /Users/alessandrocascino/Desktop/XREVERSE_TOOL/DATA/*; do 
	mkdir "${f%.*}"
  #	GENERAZIONE XML
	python yxml.py "$f" > "${f%.*}_hierarchy.xml" && echo eseguito parsing XML correttamente && python cleanify.py && echo eseguito clean XML correttamente && python cleanify_fase2.py && python cleanify_fase3.py && python cleanify_fase4.py && echo eseguito fix XML correttamente && mv "${f%.*}_hierarchy.xml" "${f%.*}"
	# GENERAZIONE FILE GRAPHVIZ
	# python show_full.py "$f" > "${f%.*}_full_graph.gv" && echo eseguito parsing full correttamente &&
  python show_gameobject.py "$f" > "${f%.*}_gameobject_graph.gv" && echo eseguito parsing gameobjects correttamente &&
  python show_monobehaviour.py "$f" > "${f%.*}_monobehaviour_graph.gv" && echo eseguito parsing monobehaviour correttamente &&
  #DISEGNO GRAFI FULL
  # twopi -Gsize=67! -Goverlap=prism -Tsvg "${f%.*}_full_graph.gv" > "${f%.*}_full_twopi.svg" && mv "${f%.*}_full_twopi.svg" "${f%.*}" && echo rendering twopi full completato &&
  # fdp -Gsize=67! -Goverlap=prism -Tsvg "${f%.*}_full_graph.gv" > "${f%.*}_full_fdp.svg" && mv "${f%.*}_full_fdp.svg" "${f%.*}" && echo rendering fdp full completato &&
  # sfdp -Gsize=67! -Goverlap=prism -Tsvg "${f%.*}_full_graph.gv" > "${f%.*}_full_sfdp.svg" && mv "${f%.*}_full_sfdp.svg" "${f%.*}" && echo rendering sfdp full completato &&
  # dot -Tsvg "${f%.*}_full_graph.gv" -o "${f%.*}_full_dot.svg" && mv "${f%.*}_full_dot.svg" "${f%.*}" && echo rendering dot full completato &&
  # DISEGNO GRAFI GAMEOBJECT
  twopi -Gsize=67! -Goverlap=scale -Tsvg "${f%.*}_gameobject_graph.gv" > "${f%.*}_gameobject_twopi.svg" && mv "${f%.*}_gameobject_twopi.svg" "${f%.*}" && echo rendering twopi gameobjects completato &&
  fdp -Gsize=67! -Goverlap=scale -Tsvg "${f%.*}_gameobject_graph.gv" > "${f%.*}_gameobject_fdp.svg" && mv "${f%.*}_gameobject_fdp.svg" "${f%.*}" && echo rendering fdp gameobjects completato &&
  sfdp -Gsize=67! -Goverlap=scale -Tsvg "${f%.*}_gameobject_graph.gv" > "${f%.*}_gameobject_sfdp.svg" && mv "${f%.*}_gameobject_sfdp.svg" "${f%.*}" && echo rendering sfdp gameobjects completato &&
  dot -Grankdir=LR -Tsvg "${f%.*}_gameobject_graph.gv" -o "${f%.*}_gameobject_dot.svg" && mv "${f%.*}_gameobject_dot.svg" "${f%.*}" && echo rendering dot gameobjects completato &&
  mv "${f%.*}_gameobject_graph.gv" "${f%.*}" &&
  # DISEGNO GRAFI MONOBEHAVIOUR
  twopi -Gsize=67! -Goverlap=scale -Tsvg "${f%.*}_monobehaviour_graph.gv" > "${f%.*}_monobehaviour_twopi.svg" && mv "${f%.*}_monobehaviour_twopi.svg" "${f%.*}" && echo rendering twopi monobehaviour completato &&
  fdp -Gsize=67! -Goverlap=scale -Tsvg "${f%.*}_monobehaviour_graph.gv" > "${f%.*}_monobehaviour_fdp.svg" && mv "${f%.*}_monobehaviour_fdp.svg" "${f%.*}" && echo rendering fdp monobehaviour completato &&
  sfdp -Gsize=67! -Goverlap=scale -Tsvg "${f%.*}_monobehaviour_graph.gv" > "${f%.*}_monobehaviour_sfdp.svg" && mv "${f%.*}_monobehaviour_sfdp.svg" "${f%.*}" && echo rendering sfdp monobehaviour completato &&
  dot -Grankdir=LR -Tsvg "${f%.*}_monobehaviour_graph.gv" -o "${f%.*}_monobehaviour_dot.svg" && mv "${f%.*}_monobehaviour_dot.svg" "${f%.*}" && echo rendering dot monobehaviour completato &&
  mv "${f%.*}_monobehaviour_graph.gv" "${f%.*}";

  # RIORDINAMENTO
  #mv "${f%.*}_full_graph.gv" "${f%.*}" &&

done