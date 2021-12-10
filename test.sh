#!/usr/bin/env bash

source .env

function usage() {
    echo "Usage: $0 [-w] [-d day] [-y year]" 1>&2
    echo "  -w:      watch tests" 1>&2
    echo "  -d day:  only test given day (will be 0 padded if not provided so)" 1>&2
    echo "  -y year: which year are we working on (must be yyyy, will default to current year, use 'all' to run all years)"
    exit 1
}

WATCH=0
DAY=""
YEAR=$(date +'%Y')

while getopts "wd:y:" o; do
    case "${o}" in
        w)
            WATCH=1
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

if [ "all" == "${YEAR}" ]; then
    TEST_TARGET=" ${TEST_DIR}/*"
else
    TEST_TARGET=" ${TEST_DIR}/${YEAR}"
fi

if [ "" != "${DAY}" ]; then
    TEST_TARGET="${TEST_TARGET}/test_day${DAY}.py"
fi

if [ 1 -eq $WATCH ]; then
    python -m pipenv run ptw --runner "pytest${TEST_TARGET}"
else
    python -m pipenv run pytest"${TEST_TARGET}"
fi
