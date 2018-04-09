#!/bin/bash

gsed -i 's/'\''/'\"'/g' *.preprocessed
find . -name '*.preprocessed' -exec bash -c ' mv $0 ${0/\preprocessed/json}' {} \;
