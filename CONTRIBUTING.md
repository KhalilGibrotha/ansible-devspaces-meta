# Contributing to Ansible DevSpaces Meta

Thank you for your interest in contributing to Ansible DevSpaces Meta! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes
5. Run tests to ensure everything works
6. Commit your changes with clear commit messages
7. Push to your fork and submit a pull request

## Development Environment

### Setting up the Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ansible-devspaces-meta.git
cd ansible-devspaces-meta

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e .[dev]
```

### Using DevContainers

The easiest way to contribute is to use the provided DevContainer:

1. Open the repository in VS Code
2. Install the "Dev Containers" extension
3. Click "Reopen in Container" when prompted
4. The environment will be set up automatically

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose
- Write clear commit messages

## Testing

All contributions should include appropriate tests:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=ansible_devspaces

# Run a specific test file
pytest tests/test_cli.py

# Run a specific test
pytest tests/test_cli.py::test_version_command
```

## Pull Request Process

1. **Update Documentation**: If your change affects user-facing functionality, update the README.md
2. **Add Tests**: Include tests for new features or bug fixes
3. **Run Tests**: Ensure all tests pass before submitting
4. **Clear Description**: Provide a clear description of your changes in the PR
5. **Link Issues**: Reference any related issues in your PR description

## Types of Contributions

### Bug Reports

When reporting bugs, please include:
- A clear description of the issue
- Steps to reproduce the problem
- Expected behavior
- Actual behavior
- Environment details (OS, Python version, Ansible version)

### Feature Requests

When requesting features, please include:
- A clear description of the feature
- Use cases and benefits
- Possible implementation approach (if applicable)

### Code Contributions

We welcome:
- Bug fixes
- New features
- Documentation improvements
- Test coverage improvements
- Performance optimizations

## Code Review Process

1. All pull requests will be reviewed by maintainers
2. Feedback will be provided as comments on the PR
3. Make requested changes and push updates to your branch
4. Once approved, your PR will be merged

## Questions?

Feel free to open an issue for any questions about contributing!
