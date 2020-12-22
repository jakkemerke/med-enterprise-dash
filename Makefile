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


.PHONY: clean
clean:
	@py3clean .
	@echo ""


.PHONY: dev
dev: fixed test safer todo


.PHONY: fixed
fixed:
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


.PHONY: todo
todo:
	@echo "TODO:"
	@grep -Iirl 'todo' -A 1 ./ --color=always \
            --exclude=Makefile \
            --exclude-dir=.git \
            --exclude-dir=var \
            --exclude-dir=lib \
            --exclude-dir=bootstrap
