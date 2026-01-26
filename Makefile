
rapport1:
	cd rapport1 &&	pdflatex rapport.tex

rapport2:
	cd rapport2 && pdflatex rapport.tex

clean:
	find rapport1 rapport2 \
	-type d -name figures -prune -o \
	-type f \
	! -name "*.pdf" \
	! -name "*.tex" \
	-exec rm -f {} +

.PHONY: rapport1 rapport2 clean