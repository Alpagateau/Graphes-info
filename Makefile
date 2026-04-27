all:
	make rapport11

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


rapport7:
	cd rapport7 && pdflatex rapport.tex


rapport8:
	cd rapport8 && pdflatex rapport.tex

rapport9:
	cd rapport9 && pdflatex rapport.tex


rapport11:
	cd rapport11 && pdflatex rapport.tex
# clean:
# 	find rapport*\
# 	-type d -name figures -prune -o \
# 	-type f \
# 	! -name "*.pdf" \
# 	! -name "*.tex" \
# 	-exec rm -f {} +

.PHONY: rapport1 rapport2 rapport3 rapport4 rapport5 rapport6 rapport7 rapport8 rapport9 rapport11 #clean