#!/usr/bin/env bash

set -u

VENV_DIR=""
if [ -d ".venv" ]; then
  VENV_DIR=".venv"
elif [ -d "venv" ]; then
  VENV_DIR="venv"
fi

if [ -z "$VENV_DIR" ]; then
  echo "Virtual environment not found. Create one with:"
  echo "  python -m venv .venv"
  echo "Then activate and install deps:"
  echo "  source .venv/bin/activate && pip install -r requirements.txt"
  exit 1
fi


if [ -f "$VENV_DIR/bin/activate" ]; then

  source "$VENV_DIR/bin/activate"
elif [ -f "$VENV_DIR/Scripts/activate" ]; then

  source "$VENV_DIR/Scripts/activate"
else
  echo "Activate script not found in $VENV_DIR"
  exit 1
fi

echo "Activated virtualenv: $VENV_DIR"
echo "Running pytest..."
pytest -q
PYTEST_EXIT=$?

if [ $PYTEST_EXIT -eq 0 ]; then
  echo "All tests passed "
  exit 0
else
  echo "Some tests failed (pytest exit code: $PYTEST_EXIT)"
  exit 1
fi
