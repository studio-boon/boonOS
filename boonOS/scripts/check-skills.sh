#!/usr/bin/env sh
# Compatibility wrapper; Windows may run python scripts/check.py directly.
exec python3 "$(dirname "$0")/check.py" "$@"
