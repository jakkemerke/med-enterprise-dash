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
all: well-formed run


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


.PHONY: well-formed
well-formed:
	@black .
