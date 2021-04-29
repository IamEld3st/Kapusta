.PHONY: all pack clean test doc pip_install run profile
AUTHORS=xhrabo14_xhomol28_xdobro23_xszcze01

all:

pack: clean doc
	mkdir ../../$(AUTHORS) ../../$(AUTHORS)/doc ../../$(AUTHORS)/install
	cp -r ../docs/html ../../$(AUTHORS)/doc/
	cp ../docs/documentation.pdf ../../$(AUTHORS)/doc/
	cp -r ../../Kapusta ../../$(AUTHORS)/repo

	cp -a ../install/. ../../$(AUTHORS)/install/
	rm -r ../../$(AUTHORS)/repo/venv
	rm -r ../../$(AUTHORS)/repo/.idea
	cd ../../ && zip -r $(AUTHORS).zip $(AUTHORS)


clean:
	rm -rf .pytest_cache ../docs/html ../../$(AUTHORS) ../../$(AUTHORS).zip

test:
	pytest

doc:
	doxygen ../docs/doxygen.conf

pip_install:
	pip3 install -r ../requirements.txt

run: pip_install
	python main.py

profile:
	echo "No need to compile python program"
