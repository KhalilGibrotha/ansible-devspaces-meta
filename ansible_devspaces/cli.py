"""Command-line interface for Ansible DevSpaces."""

import argparse
import sys
import subprocess
from pathlib import Path


def main():
    """Main entry point for ansible-devspaces CLI."""
    parser = argparse.ArgumentParser(
        description="Ansible DevSpaces - Enhanced Ansible tooling for development environments",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available commands:
  ansible-devspaces playbook   Run ansible-playbook with DevSpaces defaults
  ansible-devspaces lint       Run ansible-lint on playbooks
  ansible-devspaces galaxy     Run ansible-galaxy commands
  ansible-devspaces version    Show version information
  
Examples:
  ansible-devspaces playbook site.yml
  ansible-devspaces lint playbooks/
  ansible-devspaces galaxy install -r requirements.yml
        """
    )
    
    parser.add_argument(
        "command",
        choices=["playbook", "lint", "galaxy", "version"],
        help="Command to run"
    )
    
    parser.add_argument(
        "args",
        nargs=argparse.REMAINDER,
        help="Additional arguments to pass to the command"
    )
    
    args = parser.parse_args()
    
    if args.command == "version":
        from . import __version__
        print(f"ansible-devspaces version {__version__}")
        return 0
    
    if args.command == "playbook":
        cmd = ["ansible-playbook"] + args.args
    elif args.command == "lint":
        cmd = ["ansible-lint"] + args.args
    elif args.command == "galaxy":
        cmd = ["ansible-galaxy"] + args.args
    else:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        return 1
    
    try:
        result = subprocess.run(cmd, check=False)
        return result.returncode
    except FileNotFoundError:
        print(f"Error: Command not found. Make sure Ansible is installed.", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
