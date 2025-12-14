# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
LOCALEDIR     = locale

SIZECHECKER   = python3 -m scripts.imagesizechecker
CONFEXCLUDE   = --exclude-file source/conf.py
SIZEMAX       = 500

AUTOBUILD = sphinx-autobuild
HTMLBUILDDIR = build/html
LATEXBUILDDIR = build/latex/
BOOKLETSBUILDDIR = build/booklets

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo ""
	@echo "Japanese translation targets:"
	@echo "  gettext     Extract translatable messages to POT files"
	@echo "  ja-update   Update Japanese PO files from POT files"
	@echo "  ja-build    Build Japanese HTML documentation"
	@echo "  ja-stats    Show translation statistics for Japanese"

.PHONY: help Makefile

setup:
	python -m pip install -r requirements.txt

autobuild:
	@$(AUTOBUILD) $(SOURCEDIR) $(HTMLBUILDDIR) --port=7350

--move-booklets:
	mkdir -p $(BOOKLETSBUILDDIR)
	cp $(addsuffix .pdf, $(basename $(wildcard $(LATEXBUILDDIR)*.tex))) $(BOOKLETSBUILDDIR)

--generate-booklets:
	BOOKLETS_BUILD="true" $(SPHINXBUILD) -M latexpdf $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $(O)

booklets: --generate-booklets --move-booklets
	
local-full:
	DOCS_BUILD="true" $(SPHINXBUILD) -b html $(SOURCEDIR) $(HTMLBUILDDIR) $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) -M latexpdf $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $(O)
	cp $(LATEXBUILDDIR)*.pdf $(HTMLBUILDDIR)

imagecheck:
	@$(SIZECHECKER) $(SOURCEDIR) $(SIZEMAX) $(CONFEXCLUDE) $(O)

# Japanese translation targets
ja-update:
	@echo "Updating Japanese PO files from POT files..."
	sphinx-intl update -p $(BUILDDIR)/gettext -l ja

ja-build:
	@echo "Building Japanese HTML documentation..."
	@$(SPHINXBUILD) -D language=ja -b html $(SOURCEDIR) $(BUILDDIR)/html/ja $(SPHINXOPTS) $(O)
	@echo "Japanese documentation built in $(BUILDDIR)/html/ja"

ja-stats:
	@echo "Translation statistics for Japanese:"
	@sphinx-intl stat -d $(LOCALEDIR) -l ja || echo "Run 'make gettext && make ja-update' first"

.PHONY: help autobuild ja-update ja-build ja-stats Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
