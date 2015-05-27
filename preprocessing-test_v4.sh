#!/bin/bash

sed "s/^M//g" \
| tr '\n' ' ' \
| sed "s/\([a-zA-Z]*\)n't/\1 not/g" \
| sed "s/\([a-zA-Z]*\)'m/\1 am/g" \
| sed "s/\([a-zA-Z]*\)'re/\1 are/g" \
| sed "s/\([a-zA-Z]*\)'ll/\1 will/g" \
| sed "s/\([a-zA-Z]*\)'ve/\1 have/g" \
| sed "s/\t/ /g" \
| sed "s/(\([^()]*\))/\n\1\n/g" \
| sed "s/\"\([^\"]*\)\"/\n\1\n/g" \
| sed "s/\'\([^\']*\)\'/\n\1\n/g" \
| sed "s/[,:\/\` ]/ /g" \
| sed "s/ [\.\?\!] /\n/g" \
| sed "s/[^a-zA-Z0-9 ]/ /g" \
| sed "s/./\L&/g" \
| sed "s/ [ ]*/ /g" \
| sed "s/^[ \t]*//g" \
| sed "s/[\t ]*$//g" \
| sed "/^$/d" \
| sed "/^[^ ]*$/d" \
| sed "s/[^[:print:]]//g" \
| sed "s/^[0-9]*[a-e] //g"
