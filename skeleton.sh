#!/usr/bin/env bash
set -e
# get same env variables as python
source .env

# pad day with 0s
printf -v DAY "%02d" ${1}
echo "Setting up skeleton for AOC 2021 Day ${DAY}"

# make data dir for given day
DAY_DIR=${DATA_DIR}/${DAY}
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
if [ -f "${PART_1_OUTPUT}" ]; then
    echo "    Part 1 output file already exists, reading value from ${PART_1_OUTPUT}"
    PART_1_SAMPLE_RESULT=$(cat "${PART_1_OUTPUT}")
    echo "    Expected result for Part 1 using sample input is: ${PART_1_SAMPLE_RESULT}"
else
    read -p "    Enter the result expected from Part 1, using the sample input: " PART_1_SAMPLE_RESULT
    echo "${PART_1_SAMPLE_RESULT}" > "${PART_1_OUTPUT}"
    echo "    Part 1 output saved to: ${PART_1_OUTPUT}"
fi
PART_2_OUTPUT="${DAY_DIR}/part2_sample.out"
if [ -f "${PART_2_OUTPUT}" ]; then
    echo "    Part 2 output file already exists, reading value from ${PART_2_OUTPUT}"
    PART_2_SAMPLE_RESULT=$(cat "${PART_2_OUTPUT}")
    echo "    Expected result for Part 2 using sample input is: ${PART_2_SAMPLE_RESULT}"
else
    read -p "    Enter the result expected from Part 2, using the sample input (use '-' if unknown): " PART_2_SAMPLE_RESULT
    echo "${PART_2_SAMPLE_RESULT}" > "${PART_2_OUTPUT}"
    echo "    Part 2 output saved to: ${PART_2_OUTPUT}"
fi
echo "  Done"

# python file
echo "  Seting up python file skeleton"
PYTHON_FILE="${SOURCE_DIR}/day${DAY}.py"
if [ -f "${PYTHON_FILE}" ]; then
    echo "    Python file already exitst at ${PYTHON_FILE}, skipping"
else
    cat > "${PYTHON_FILE}" <<EOF
#!/usr/bin/env python

from aoc2021 import input

DAY: str = "${DAY}"

def part01(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    return str(len(lines))

def part02(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    return str(len(lines))
EOF
    echo "    Python file created at ${PYTHON_FILE}"
fi
echo "  Done"

# test file
echo "  Setting up test file skeleton"
TEST_FILE="${TESTS_DIR}/test_day${DAY}.py"
if [ -f "${TEST_FILE}" ]; then
    echo "    Test file already exists at ${TEST_FILE}, skipping"
else
    cat > "${TEST_FILE}" <<EOF
from aoc2021 import day${DAY}

def test_sample_day${DAY}_part01():
    assert "${PART_1_SAMPLE_RESULT}" == day${DAY}.part01("sample")

def test_input_day${DAY}_part01():
    print(day${DAY}.part01("input"))

def test_sample_day${DAY}_part02():
    assert "${PART_2_SAMPLE_RESULT}" == day${DAY}.part02("sample")

def test_input_day${DAY}_part02():
    print(day${DAY}.part02("input"))
EOF
    echo "    Test file created at ${TEST_FILE}"
fi
echo "  Done"
