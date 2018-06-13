# Archivo makefile - Compilación del trabajo
# ESCOM - IPN
# Autor: Rafael Landa
# Contribuyente: Alan Vieyra
# Febrero 5 de 2018
#

# Vars

MAIN = reporte_tecnico.tex
OUT = reporte_tecnico.pdf
OBJS = styles/*.sty \
	src/**/*.tex
BUILD_DIR = .build
OUT_DIR = pdf
#CONFIG = -synctex=1 -interaction=nonstopmode -output-directory=$(BUILD_DIR)
CONFIG = -quiet  -output-directory=$(BUILD_DIR) -pdf \
	 -pdflatex="pdflatex -synctex=1 -interaction=nonstopmode -output-directory=$(BUILD_DIR)"

# Reglas explícitas

.PHONY: all
all: clean $(OUT) copy
	@echo 'Done.'

$(OUT): $(MAIN) $(OBJS)
	@echo 'Creating output dir...'
	@mkdir -p $(BUILD_DIR)/ $(OUT_DIR)/
	@echo 'Building Latex -> pdf...'
#	@pdflatex $(CONFIG) $(MAIN)
	@latexmk $(CONFIG) $(MAIN)	

.PHONY: clean
clean:
	@echo 'Deleting output dirs...'
	@rm -rf $(BUILD_DIR)/*.*

.PHONY: move
move:
	@echo 'Moving pdf...'
	@mv $(BUILD_DIR)/$(OUT) $(OUT_DIR)/

.PHONY: copy
copy:
	@echo 'Copying pdf...'
	@cp $(BUILD_DIR)/$(OUT) $(OUT_DIR)/
