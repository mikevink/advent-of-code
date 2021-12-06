TARGET=aoc2021

.PHONY: $(TARGET) test testmon ptw

all: $(TARGET)

$(TARGET): $(FILES)

setup:
	python -m pipenv install --dev

test:
	bash test.sh

daytest:
	bash test.sh -d $(DAY)

ptw:
	bash test.sh -w

daywatch:
	bash test.sh -w -d $(DAY)

generate:
	bash skeleton.sh $(DAY)

skeli:
	bash skeleton.sh $(DAY)

