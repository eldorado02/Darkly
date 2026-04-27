IP_ADDRESS = 192.168.88.219

build:
	@if [ ! -d .venv ] ; then python3 -m venv .venv ; fi

install: build
	pip install --upgrade pip
	pip install -r requirements.txt

clean:
	rm -rf $$( find . -path "./.venv" -prune -type d -name __pycache__ )

robots:
	python robots/request.py ${IP_ADDRESS}

.PHONY : clean fclean robots