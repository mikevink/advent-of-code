TARGET=aoc2021

.PHONY: $(TARGET)

all: $(TARGET)

$(TARGET): $(FILES)

setup:
	python -m pipenv install --dev

test:
	python -m pipenv run pytest

generate:
	bash skeleton.sh $(DAY)

skeli:
	bash skeleton.sh $(DAY)

