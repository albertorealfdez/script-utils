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
    echo "Checking " $repo
    cd $HOME$repo
    folder_name=$(basename $PWD)
  
    local=$(git rev-parse --abbrev-ref HEAD)
    remote=$(git rev-parse --abbrev-ref --symbolic-full-name @{u})
    ahead=$(git rev-list --left-only --count ${local}...${remote})
    behind=$(git rev-list --right-only --count ${local}...${remote})

    echo -e "*" ${GREEN}$folder_name${WHITE} "-" $local "- ${YELLOW}$behind${DOWN_ARROW} $ahead${UP_ARROW}${WHITE}"

    if [[ $# == 2 ]] && [[ $1 == '-u' || $1 == '--update' ]] && [[ $behind -gt 0 ]]; then
        git pull origin HEAD
    fi
done

