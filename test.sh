#!/usr/bin/env bash

source .env

function usage() {
    echo "Usage: $0 [-w] [-d day]" 1>&2
    echo "  -w:     watch tests" 1>&2
    echo "  -d day: only test given day (1-25)" 1>&2
    exit 1
}

WATCH=0
TEST_FILE=""

while getopts "wd:" o; do
    case "${o}" in
        w)
            WATCH=1
            ;;
        d)
            printf -v DAY "%02d" ${OPTARG}
            TEST_FILE=" ${TEST_DIR}/test_day${DAY}.py"
            ;;
        *)
            usage
            ;;
    esac
done

if [ 1 -eq $WATCH ]; then
    python -m pipenv run ptw --runner "pytest${TEST_FILE}"
else
    python -m pipenv run pytest${TEST_FILE}
fi
