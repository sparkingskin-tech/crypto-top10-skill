#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
import os
from pathlib import Path

ROOT = Path("/Users/skin/Projects/量化")
RUNTIME = ROOT / "runtime"
RESPOND = ROOT / "services" / "respond-crypto.py"
VALID = {
    "brief",
    "daily",
    "full",
    "top10",
    "top3",
    "zones",
    "volume",
    "events",
    "whales",
    "institutions",
    "derivatives",
    "flows",
    "deep-btc",
    "deep-eth",
    "deep-bnb",
}


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: run.py <intent>")
        return 2
    intent = sys.argv[1].strip().lower()
    if intent not in VALID:
        print(f"unsupported intent: {intent}")
        return 2
    cmd = ["python3", str(RESPOND), intent]
    env = {**os.environ, "PYTHONPATH": str(RUNTIME)}
    proc = subprocess.run(cmd, cwd=str(ROOT), env=env, text=True)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
