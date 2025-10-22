.PHONY: help setup lint test navigator-run pre-commit clean

# Default target - show help
help:
	@echo "Ansible DevSpaces - Available Targets"
	@echo "======================================"
	@echo "  make setup          - Install ansible-dev-tools and dependencies"
	@echo "  make lint           - Run ansible-lint on all projects"
	@echo "  make test           - Run molecule tests"
	@echo "  make navigator-run  - Run ansible-navigator with local EE"
	@echo "  make pre-commit     - Install and configure pre-commit hooks"
	@echo "  make clean          - Clean up temporary files and caches"
	@echo ""
	@echo "For more information, see README.md"

# Install/upgrade ansible-dev-tools
setup:
	@echo "Installing ansible-dev-tools..."
	python3 -m pip install --upgrade ansible-dev-tools
	@echo "Setup complete!"

# Run ansible-lint on all projects in src/
lint:
	@echo "Running ansible-lint..."
	@if [ -d "src" ]; then \
		for dir in src/*/; do \
			if [ -d "$$dir" ]; then \
				echo "Linting $$dir..."; \
				cd "$$dir" && ansible-lint || true; \
				cd -; \
			fi; \
		done; \
	else \
		echo "No src/ directory found. Running lint in current directory..."; \
		ansible-lint; \
	fi

# Run molecule tests
test:
	@echo "Running molecule tests..."
	@if [ -d "src" ]; then \
		for dir in src/*/; do \
			if [ -d "$$dir" ] && [ -d "$$dir/molecule" ]; then \
				echo "Testing $$dir..."; \
				cd "$$dir" && molecule test || true; \
				cd -; \
			fi; \
		done; \
	else \
		echo "Running molecule test in current directory..."; \
		molecule test; \
	fi

# Run ansible-navigator with local EE
navigator-run:
	@echo "Starting ansible-navigator..."
	@echo "Note: You need to specify a playbook. Example: make navigator-run PLAYBOOK=src/platform-infra/site.yml"
	@if [ -n "$(PLAYBOOK)" ]; then \
		ansible-navigator run $(PLAYBOOK) --execution-environment-image quay.io/devspaces/ansible-workspace:latest; \
	else \
		ansible-navigator --help; \
	fi

# Install and configure pre-commit
pre-commit:
	@echo "Installing pre-commit..."
	python3 -m pip install pre-commit
	@echo "Configuring pre-commit hooks..."
	@if [ -f ".pre-commit-config.yaml" ]; then \
		pre-commit install; \
		echo "Pre-commit hooks installed!"; \
	else \
		echo "Warning: .pre-commit-config.yaml not found. Skipping hook installation."; \
		echo "You may want to create this file in your individual project repositories."; \
	fi

# Clean up temporary files and caches
clean:
	@echo "Cleaning up temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".molecule" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "Clean complete!"
