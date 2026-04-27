IP_ADDRESS = 10.11.200.182

build:
	@if [ ! -d .venv ] ; then python3 -m venv .venv ; fi

install: build
	pip install --upgrade pip
	pip install -r requirements.txt

clean:
	rm -rf $$( find . -path "./.venv" -prune -type d -name __pycache__ )

robots:
	python 04-robots/Resources/request.py ${IP_ADDRESS}

.PHONY : clean fclean robots