all: makePPM.py
	python makePPM.py
	convert pic.ppm pic.png
	display pic.png
