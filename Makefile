all:
	make rapport6

rapport1:
	cd rapport1 &&	pdflatex rapport.tex

rapport2:
	cd rapport2 && pdflatex rapport.tex


rapport3:
	cd rapport3 && pdflatex rapport.tex
	
rapport4:
	cd rapport4 && pdflatex rapport.tex

rapport5:
	cd rapport5 && pdflatex rapport.tex

rapport6:
	cd rapport6 && pdflatex rapport.tex
# clean:
# 	find rapport*\
# 	-type d -name figures -prune -o \
# 	-type f \
# 	! -name "*.pdf" \
# 	! -name "*.tex" \
# 	-exec rm -f {} +

.PHONY: rapport1 rapport2 rapport3 rapport4 rapport5 rapport6#clean