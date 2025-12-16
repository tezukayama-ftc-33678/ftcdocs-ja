# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

SIZECHECKER   = python3 -m scripts.imagesizechecker
CONFEXCLUDE   = --exclude-file source/conf.py
SIZEMAX       = 500

AUTOBUILD = sphinx-autobuild
HTMLBUILDDIR = build/html
HTMLBUILDDIR_JA = build/html-ja
LATEXBUILDDIR = build/latex/
BOOKLETSBUILDDIR = build/booklets

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

setup:
	python -m pip install -r requirements.txt

autobuild:
	@$(AUTOBUILD) $(SOURCEDIR) $(HTMLBUILDDIR) --port=7350

autobuild-ja:
	@$(AUTOBUILD) -D language=ja $(SOURCEDIR) $(HTMLBUILDDIR_JA) --port=7351 --open-browser --watch ../locales

html-ja:
	@$(SPHINXBUILD) -b html -D language=ja $(SOURCEDIR) $(HTMLBUILDDIR_JA) $(SPHINXOPTS) $(O)

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

.PHONY: help autobuild autobuild-ja html-ja Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
