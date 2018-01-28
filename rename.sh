#!/bin/bash

NEW_NAME=`python <<END
import arxiv
import ntpath
fileName = ntpath.basename("$1")
arxiv_id = fileName[:fileName.rfind('.')]
title = arxiv.query(id_list=[arxiv_id])[0]['title_detail']['value']
print(title + ".pdf")
END`

mv "$1" "${NEW_NAME}"