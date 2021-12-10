#!/usr/bin/env bash
set -e
# get same env variables as python
source .env

function usage() {
    echo "Usage: $0 -d day [-y year]" 1>&2
    echo "  -d day:  which test day to generate (will be 0 padded if not provided so)"
    echo "  -y year: which year are we working on (must be yyyy, will default to current year)"
    exit 1
}

DAY=""
YEAR=$(date +'%Y')

while getopts "d:y:" o; do
    case "${o}" in
        d)
            # pad day with 0s
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

echo "Setting up skeleton for AOC ${YEAR} Day ${DAY}"

# make data dir for given day
DAY_DIR=${DATA_DIR}/${YEAR}/${DAY}
echo "  Ensuring data dir is present at ${DAY_DIR}"
mkdir -p "${DAY_DIR}"
echo "  Done"

# setup sample
echo "  Setting up sample input"
SAMPLE_INPUT_FILE=${DAY_DIR}/sample.in
if [ -f "${SAMPLE_INPUT_FILE}" ]; then
    echo "    Sample input file already exists at ${SAMPLE_INPUT_FILE}, skipping"
else
    echo "    Copy/paste or type sample input below. finish on an empty line and then Ctrl+D"
    SAMPLE=$(cat)
    echo "${SAMPLE}" > "${SAMPLE_INPUT_FILE}"
    echo "    Sample input saved to: ${SAMPLE_INPUT_FILE}"
fi
echo "  Done"

# setup input
echo "  Setting up input"
INPUT_FILE=${DAY_DIR}/input.in
if [ -f "${INPUT_FILE}" ]; then
    echo "    Input file already exists at ${INPUT_FILE}, skipping"
else
    echo "    Copy/paste or type input below. finish on an empty line and then Ctrl+D"
    INPUT=$(cat)
    echo "${INPUT}" > "${INPUT_FILE}"
    echo "    Input saved to: ${INPUT_FILE}"
fi
echo "  Done"

# sample results
echo "  Setting up results to sample input"
PART_1_OUTPUT="${DAY_DIR}/part1_sample.out"
echo "    Part 1"
if [ -f "${PART_1_OUTPUT}" ]; then
    echo "      Output file already exists, reading value from ${PART_1_OUTPUT}"
    PART_1_SAMPLE_RESULT=$(cat "${PART_1_OUTPUT}")
    echo "      Expected result when using sample input is: ${PART_1_SAMPLE_RESULT}"
else
    read -r -p "      Enter the result expected when using the sample input: " PART_1_SAMPLE_RESULT
    echo "${PART_1_SAMPLE_RESULT}" > "${PART_1_OUTPUT}"
    echo "    Saved to: ${PART_1_OUTPUT}"
fi
PART_2_OUTPUT="${DAY_DIR}/part2_sample.out"
echo "    Part 2"
if [ -f "${PART_2_OUTPUT}" ]; then
    echo "      Output file already exists, reading value from ${PART_2_OUTPUT}"
    PART_2_SAMPLE_RESULT=$(cat "${PART_2_OUTPUT}")
    echo "      Expected result when using sample input is: ${PART_2_SAMPLE_RESULT}"
else
    read -r -p "      Enter the result expected when using the sample input (use '-' if unknown): " PART_2_SAMPLE_RESULT
    echo "${PART_2_SAMPLE_RESULT}" > "${PART_2_OUTPUT}"
    echo "      Saved to: ${PART_2_OUTPUT}"
fi
echo "  Done"

# python file
echo "  Setting up python file skeleton"
DAY_SOURCE_DIR=${SOURCE_DIR}/year${YEAR}/day${DAY}
mkdir -p "${DAY_SOURCE_DIR}"

PYTHON_FILE=${DAY_SOURCE_DIR}/__init__.py
if [ -f "${PYTHON_FILE}" ]; then
    echo "    Python file already exists at ${PYTHON_FILE}, skipping"
else
    cat > "${PYTHON_FILE}" <<EOF
#!/usr/bin/env python

from aoc.common import input
from aoc.common import error

DAY: str = "${YEAR}/${DAY}"


def part01(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    return error.ERROR


def part02(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    return error.ERROR
EOF
    echo "    Python file created at ${PYTHON_FILE}"
fi
echo "  Done"

# test file
echo "  Setting up test file skeleton"
YEAR_TEST_DIR=${TEST_DIR}/${YEAR}
mkdir -p "${YEAR_TEST_DIR}"

TEST_FILE="${YEAR_TEST_DIR}/test_day${DAY}.py"
if [ -f "${TEST_FILE}" ]; then
    echo "    Test file already exists at ${TEST_FILE}, skipping"
else
    cat > "${TEST_FILE}" <<EOF
from aoc.year${YEAR} import day${DAY}


def test_year${YEAR}_day${DAY}_part01_sample():
    assert "${PART_1_SAMPLE_RESULT}" == day${DAY}.part01("sample")


def test_year${YEAR}_day${DAY}_part01_input():
    result: str = day${DAY}.part01("input")
    print(f"Day ${DAY} Part 01 Result: {result}")


def test_year${YEAR}_day${DAY}_part02_sample():
    assert "${PART_2_SAMPLE_RESULT}" == day${DAY}.part02("sample")


def test_year${YEAR}_day${DAY}_part02_input():
    result: str = day${DAY}.part02("input")
    print(f"Day ${DAY} Part 02 Result: {result}")
EOF
    echo "    Test file created at ${TEST_FILE}"
fi
echo "  Done"
