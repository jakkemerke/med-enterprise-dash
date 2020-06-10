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

.PHONY: all
all: well-formed run

.PHONY: run
run:
	@echo "See server at the following address and port:"
	@grep '= make_server' -B 1 src/med_enterprise_dash/server.py
	@python3 src/med_enterprise_dash/server.py

.PHONY: well-formed
well-formed:
	@black .
