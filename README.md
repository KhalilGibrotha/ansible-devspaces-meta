# Ansible DevSpaces Meta

A meta repository that wraps standard Ansible tooling with customizations optimized for DevSpaces and containerized development environments.

## Overview

This repository provides a pre-configured Ansible environment designed for use in DevSpaces (GitHub Codespaces, VS Code Dev Containers, etc.) with sensible defaults, useful extensions, and wrapper scripts to streamline Ansible development and automation tasks.

## Features

- **Pre-configured DevContainer**: Ready-to-use development container with Ansible and all necessary tools
- **Wrapper CLI**: Simplified command-line interface for common Ansible operations
- **Sensible Defaults**: Pre-configured ansible.cfg with DevSpaces-optimized settings
- **Example Playbooks**: Sample playbooks and inventory files to get started quickly
- **Python Package**: Installable package with custom tooling
- **VS Code Integration**: Pre-configured extensions and settings for Ansible development

## Quick Start

### Using in DevSpaces/Codespaces

1. Open this repository in GitHub Codespaces or VS Code with Dev Containers
2. The environment will automatically set up with all dependencies
3. Start using Ansible immediately!

### Local Installation

```bash
# Clone the repository
git clone https://github.com/KhalilGibrotha/ansible-devspaces-meta.git
cd ansible-devspaces-meta

# Install the package
pip install -e .

# Or install with development dependencies
pip install -e .[dev]
```

## Usage

### Using the Wrapper CLI

The `ansible-devspaces` CLI provides convenient wrappers around standard Ansible commands:

```bash
# Run a playbook
ansible-devspaces playbook examples/playbook.yml

# Lint your playbooks
ansible-devspaces lint examples/

# Install Ansible Galaxy collections
ansible-devspaces galaxy install -r examples/requirements.yml

# Show version
ansible-devspaces version
```

### Using Standard Ansible Commands

All standard Ansible commands work as expected:

```bash
# Run ansible-playbook directly
ansible-playbook examples/playbook.yml

# Use ansible ad-hoc commands
ansible localhost -m ping

# Install collections
ansible-galaxy collection install -r examples/requirements.yml
```

## Project Structure

```
ansible-devspaces-meta/
├── .devcontainer/           # DevContainer configuration
│   ├── devcontainer.json   # Container settings and VS Code customizations
│   └── Dockerfile          # Container image definition
├── ansible_devspaces/       # Python package
│   ├── __init__.py         # Package initialization
│   ├── cli.py              # Command-line interface
│   └── config.py           # Configuration management
├── examples/                # Example files
│   ├── ansible.cfg         # Sample Ansible configuration
│   ├── inventory.ini       # Sample inventory
│   ├── playbook.yml        # Sample playbook
│   └── requirements.yml    # Sample Galaxy requirements
├── tests/                   # Unit tests
│   ├── test_cli.py         # CLI tests
│   └── test_config.py      # Configuration tests
├── .gitignore              # Git ignore patterns
├── pyproject.toml          # Python package configuration
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Configuration

### Default Ansible Settings

The following settings are pre-configured for DevSpaces environments:

- `host_key_checking`: Disabled for easier development
- `retry_files_enabled`: Disabled to avoid clutter
- `stdout_callback`: Set to YAML for readable output
- `callbacks_enabled`: Includes profile_tasks and timer for performance insights
- `interpreter_python`: Set to auto_silent

### Customizing Configuration

You can override defaults by:

1. Creating a custom `ansible.cfg` in your project
2. Setting environment variables (e.g., `ANSIBLE_HOST_KEY_CHECKING=True`)
3. Using command-line flags with Ansible commands

## Development

### Running Tests

```bash
# Install development dependencies
pip install -e .[dev]

# Run tests
pytest

# Run tests with coverage
pytest --cov=ansible_devspaces
```

### Building the Package

```bash
# Build source and wheel distributions
python -m build

# Install locally
pip install -e .
```

## Examples

### Example 1: Running a Simple Playbook

```bash
cd examples
ansible-playbook playbook.yml
```

### Example 2: Testing Connectivity

```bash
ansible localhost -m ping
```

### Example 3: Installing Collections

```bash
ansible-galaxy collection install -r examples/requirements.yml
```

## Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and create pull requests.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure everything works
5. Submit a pull request

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Requirements

- Python 3.9 or higher
- Ansible Core 2.15.0 or higher
- Docker (for DevContainer support)

## Troubleshooting

### Issue: Ansible commands not found

**Solution**: Ensure you've installed the package and dependencies:
```bash
pip install -e .
```

### Issue: DevContainer not building

**Solution**: Ensure Docker is running and you have the Dev Containers extension installed in VS Code.

### Issue: Permission errors when running playbooks

**Solution**: Check your inventory and ensure the correct connection settings are configured.

## Resources

- [Ansible Documentation](https://docs.ansible.com/)
- [DevContainers Documentation](https://containers.dev/)
- [GitHub Codespaces](https://github.com/features/codespaces)

## Support

For questions, issues, or feature requests, please open an issue on the GitHub repository.