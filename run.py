"""Thin wrapper around ``aizynthcli`` for running retrosynthesis planning on a single SMILES."""

import argparse
import subprocess
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run retrosynthesis planning on a single target molecule."
    )
    parser.add_argument("--smiles", required=True, help="the target molecule SMILES")
    parser.add_argument(
        "--config",
        default="data/config.yml",
        help="the filename of the aizynthfinder configuration file (default: data/config.yml)",
    )
    args = parser.parse_args()

    cmd = ["aizynthcli", "--config", args.config, "--smiles", args.smiles]
    sys.exit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
