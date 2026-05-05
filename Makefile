IP_ADDRESS = 10.11.200.182

build:
	@if [ ! -d .venv ] ; then python3 -m venv .venv ; fi

install: build
	pip install --upgrade pip
	pip install -r requirements.txt

clean:
	rm -rf $$( find . -path "./.venv" -prune -type d -name __pycache__ )
	rm -rf .venv

robots:
	python 04-Sensitive_Data_Exposure/Resources/request.py ${IP_ADDRESS}

.PHONY : clean fclean robots