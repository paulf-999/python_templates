#!/bin/bash
#================================================================
## HEADER
#================================================================
## Overview:    Git branch validation.
##
## Description: This script is used by pre-commit to verify the
##              user's git branch name follows the naming standard:
##              ^(feature|hotfix|release)\/[a-z0-9_]+$
##
## Usage: ./validate_git_branch_name.sh <input git branch name>
##
#================================================================

#=======================================================================
# Variables
#=======================================================================

# determine the name of the local git branch name
LOCAL_GIT_BRANCH_NAME="$(git rev-parse --abbrev-ref HEAD)"
# the regex for valid git branch names
VALID_GIT_BRANCH_NAME="^(feature|hotfix|release)\/[a-z0-9_]+$"

# setup colour formatting
# ANSI escape codes for color formatting
DEBUG='\033[0;36m' # cyan (for debug messages)
INFO='\033[0;32m' # green (for informational messages)
WARNING='\033[0;33m' # yellow (for warning messages)
ERROR='\033[0;31m' # red (for error messages)
CRITICAL='\033[1;31m' # bold red (for critical errors)
COLOUR_OFF='\033[0m' # Text Reset

#=======================================================================
# Main script logic
#=======================================================================

# Validate the Git branch name used
if [[ ! $LOCAL_GIT_BRANCH_NAME =~ $VALID_GIT_BRANCH_NAME ]]
then
    echo
    echo -e "${ERROR}#---------------------------------------------------------------------------------------------"
    echo -e "${ERROR}# ERROR: Invalid Git branch name."
    echo -e "${ERROR}#---------------------------------------------------------------------------------------------" && echo
    echo -e "${ERROR}Local git branch name = $LOCAL_GIT_BRANCH_NAME" && echo
    echo -e "${ERROR}Git branch name needs to adhere to the following regex: $VALID_GIT_BRANCH_NAME." && echo
    echo -e "${ERROR}I.e., it needs to:" && echo
    echo -e "${ERROR}* Start with either 'feature/', 'hotfix/' or 'release/'"
    echo -e "${ERROR}* Followed by a snake_case description of your change (note, hyphens aren't allowed)." && echo
    echo -e "${ERROR}E.g.: feature/my_eg_change" && echo
    echo -e "${ERROR}---------------------------------------------------------------------------------------------${COLOUR_OFF}" && echo
    exit 1
else
    echo -e "${INFO}#---------------------------------------------------------------------------------------------"
    echo -e "${INFO}# SUCCESS: Valid Git branch name"
    echo -e "${INFO}#---------------------------------------------------------------------------------------------${COLOUR_OFF}"
    echo
fi
