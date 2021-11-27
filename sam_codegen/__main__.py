"""Invokable module that calls through to the cli

usage: python -m sam_codegen
"""

from sam_codegen.cli.main import cli


if __name__ == "__main__":
    cli(prog_name="scg")
