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
	@echo ''


.PHONY: dev
dev:
	@black myapp.py ./src ./bin ./tests
	@echo ''


.PHONY: fe
fe:
	@cd lib/med-appointments/ \
            && make init \
            && make rebuild \
            && rsync -av --delete ./output/ \
                ../../src/med_enterprise_dash/static/med-appointments/ \
            && make clean
	@echo done


.PHONY: run
run:
	@echo "See server at the following address and port:"
	@grep '= make_server' -B 1 src/med_enterprise_dash/server.py
	@python3 src/med_enterprise_dash/server.py


.PHONY: safer
safer:
	@mypy src/med_enterprise_dash/utils/session.py --disallow-untyped-defs || echo ""
	@mypy src/med_enterprise_dash/utils/toml.py --disallow-untyped-defs \
            || echo "Try adding the path: export MYPYPATH=`pwd`/src/med_enterprise_dash"
	@echo ''


.PHONY: test
test:
	@python3 -m unittest tests.test_med_enterprise_dash
	@python3 -m unittest tests.test_views
	@echo ''
