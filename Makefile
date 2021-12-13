TARGET=aoc

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
	bash skeleton.sh -d $(DAY)

skeli:
	bash skeleton.sh -d $(DAY)

edit:
	bash edit.sh -d $(DAY)

testedit:
	bash edit.sh -d $(DAY) -t

te: testedit

format:
	python -m pipenv run black .
