#!/usr/bin/env bash
set -euo pipefail

uv run -m nuitka src/run-7/main.py \
  --follow-imports \
  --include-data-dir=src/run-7/qml=qml \
  --output-filename="run-7" \
  --output-dir="build"
