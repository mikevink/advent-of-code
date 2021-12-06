TARGET=aoc2021

.PHONY: $(TARGET) test testmon ptw

all: $(TARGET)

$(TARGET): $(FILES)

setup:
	python -m pipenv install --dev

test:
	python -m pipenv run pytest

testmon:
	python -m pipenv run pytest --testmon

ptw:
	python -m pipenv run ptw --runner "pytest --testmon"

generate:
	bash skeleton.sh $(DAY)

skeli:
	bash skeleton.sh $(DAY)
