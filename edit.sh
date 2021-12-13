#!/usr/bin/env bash

source .env

function usage() {
    echo "Usage: $0 -d day [-y year] [-t] [-f]" 1>&2
    echo "  -d day:  only test given day (will be 0 padded if not provided so)" 1>&2
    echo "  -y year: which year are we working on (must be yyyy, will default to current year)"
    echo "  -t:      edit tests" 1>&2
    echo "  -f:      which file to edit (no extension, will default to __init__, ignore for tests)"
    exit 1
}

TEST=0
DAY=""
YEAR=$(date +'%Y')
FILE="__init__"

while getopts "d:y:tf:" o; do
    case "${o}" in
        t)
            TEST=1
            ;;
        d)
            printf -v DAY "%02d" "${OPTARG}"
            ;;
        y)
            YEAR=${OPTARG}
            ;;
        *)
            usage
            ;;
    esac
done

if [ "" == "${DAY}" ]; then
    usage
fi

if [ 0 -eq $TEST ]; then
    TARGET="${SOURCE_DIR}/year${YEAR}/day${DAY}/${FILE}.py"
else
    TARGET="${TEST_DIR}/${YEAR}/test_day${DAY}.py"
fi

vim "${TARGET}"

