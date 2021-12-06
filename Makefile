TARGET=aoc2021

.PHONY: $(TARGET) test testmon ptw

all: $(TARGET)

$(TARGET): $(FILES)

setup:
	python -m pipenv install --dev

test:
	python -m pipenv run pytest

ptw:
	python -m pipenv run ptw

generate:
	bash skeleton.sh $(DAY)

skeli:
	bash skeleton.sh $(DAY)

