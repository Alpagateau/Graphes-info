
rapport1:
	cd rapport1 &&	pdflatex rapport.tex

rapport2:
	cd rapport2 && pdflatex rapport.tex


rapport3:
	cd rapport3 && pdflatex rapport.tex

clean:
	find rapport1 rapport2 rapport3\
	-type d -name figures -prune -o \
	-type f \
	! -name "*.pdf" \
	! -name "*.tex" \
	-exec rm -f {} +

.PHONY: rapport1 rapport2 rapport3  clean