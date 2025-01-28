#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
WHITE='\033[0m'
UP_ARROW=$'\030'
DOWN_ARROW=$'\031'
PWD=$(pwd)
HOME="/Users/albertoreal/Projects/Khipulearn/"

repo_list=(
    "al-frontend" "al-creator" "al-template" "al-api" "al-hub"
)

for repo in ${repo_list[@]}
do
    cd $HOME$repo
    last_tag=$(git tag --sort=creatordate | tail -1)
    tag_info=$(git show $last_tag | grep -e "^-")
    
    echo -e ${GREEN}$repo${WHITE} "-" $last_tag
    #echo $tag_info
done


