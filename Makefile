# ---------- ---------- ---------- ---------- ---------- ----------
#
#   med-enterprise-dash
#
# ---------- ---------- ---------- ---------- ---------- ----------


target: help


.PHONY: help
help:
	@echo "Usage: make [PHONY]"
	@sed -n -e '/sed/! s/\.PHONY: //p' Makefile


.PHONY: init
init:
	@git submodule sync
	@git submodule update --init
	@git submodule status


.PHONY: all
all: dev run


.PHONY: clean
clean:
	@py3clean .
	@echo ""


.PHONY: dev
dev:
	@black myapp.py ./src ./bin ./tests
	@echo ""


.PHONY: fe
fe:
	@./bin/rebuild_frontends
	@echo done


.PHONY: run
run:
	@./bin/start_testing_api_server
	@echo ""


.PHONY: safer
safer:
	@mypy src/med_enterprise_dash/utils/session.py --disallow-untyped-defs || echo ""
	@mypy src/med_enterprise_dash/utils/toml.py --disallow-untyped-defs \
            || echo "Try adding the path: export MYPYPATH=`pwd`/src/med_enterprise_dash"
	@echo ""


.PHONY: test
test:
	@python3 -m unittest discover
	@echo ""
