# Ansible DevSpaces Meta Repository

This is a "meta" repository that configures a shared development workspace for Ansible teams using Red Hat OpenShift Dev Spaces. It automatically clones multiple Ansible repositories and sets up a consistent development environment with all the necessary tools.

## What's Included

- **Unified Development Environment**: A pre-configured container with Ansible tooling
- **Ansible Dev Tools Bundle**: Includes ansible-lint, molecule, ansible-navigator, and more
- **Multi-Repository Workspace**: Automatically clones all your team's Ansible repositories
- **Consistent Tooling**: Everyone gets the same versions of development tools
- **Execution Environment (EE) Support**: Run playbooks and tests inside containers

## Quick Start

### For Team Members

1. **Open in Dev Spaces**:
   - Navigate to your OpenShift Dev Spaces instance
   - Click "Create Workspace"
   - Paste the URL of this repository: `https://github.com/YourOrg/ansible-devspaces-meta`
   - Dev Spaces will read the `devfile.yaml` and set up everything automatically

2. **First-Time Setup**:
   - Once the workspace opens, run the setup command from the terminal:
     ```bash
     make setup
     ```
   - Or manually: Run the "setup-adt" task from Dev Spaces "Run Task" menu

3. **Start Working**:
   - All repositories are cloned into the `src/` directory
   - Use the provided commands and Makefile targets for common tasks

## Repository Structure

After workspace initialization, your layout will look like:

```
workspace/
├── src/
│   ├── platform-infra/      # Cloned from GitHub
│   ├── aap-content/          # Cloned from GitHub
│   └── windows-roles/        # Cloned from GitHub
├── devfile.yaml              # Workspace configuration
├── Makefile                  # Common developer tasks
└── README.md                 # This file
```

## Available Commands

### Via Makefile

Common development tasks are wrapped in the Makefile:

```bash
make setup          # Install ansible-dev-tools and pre-commit
make lint           # Run ansible-lint on all projects
make test           # Run molecule tests
make navigator-run  # Run ansible-navigator with local EE
make pre-commit     # Set up pre-commit hooks
```

### Via Dev Spaces UI

You can also run these commands from the Dev Spaces "Run Task" menu:
- `setup-adt`: Install/upgrade ansible-dev-tools
- `lint`: Run ansible-lint
- `molecule-test`: Run molecule test suite
- `navigator-run`: Run ansible-navigator
- `setup-pre-commit`: Install and configure pre-commit hooks

## Using Execution Environments (EE)

This workspace is configured to use Execution Environments, which ensures consistent Python dependencies and system packages.

### Local EE (default)

By default, commands run using the local podman engine with the workspace image:
```bash
ansible-navigator run playbook.yml
```

### Remote EE (for production-like testing)

To run against a remote podman instance (e.g., on test nodes):

1. Set up podman-remote configuration (see docs)
2. Use the remote configuration:
   ```bash
   ANSIBLE_NAVIGATOR_CONFIG=navigator-remote.yml ansible-navigator run playbook.yml
   ```

## Customizing for Your Team

### Adding More Repositories

Edit `devfile.yaml` and add entries to the `projects:` section:

```yaml
projects:
  - name: your-new-repo
    git:
      remotes: { origin: "https://github.com/YourOrg/your-new-repo.git" }
    clonePath: src/your-new-repo
```

### Using a Custom EE Image

If your team has a custom Execution Environment with ansible-dev-tools pre-installed:

1. Edit `devfile.yaml`
2. Change the `image:` line under `components`:
   ```yaml
   image: quay.io/yourorg/aap-ee/devspaces:2025.10
   ```

### Pinning Tool Versions

To ensure consistent tool versions across the team, edit the `setup-adt` command in `devfile.yaml`:

```yaml
- id: setup-adt
  exec:
    component: tools
    commandLine: |
      python3 -m pip install ansible-dev-tools==2.0.0 ansible-lint==6.22.0
      # Add any additional pins here
```

## Working with Private Repositories

If your team repositories are private:

1. **GitHub Authentication**: Dev Spaces can use your GitHub OAuth token
2. **SSH Keys**: Mount your SSH key as a secret in Dev Spaces
3. **Personal Access Tokens**: Configure in Dev Spaces secrets management

See [Dev Spaces documentation on secrets](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/) for details.

## Best Practices

### 1. Consistent Environment
- Always run `make setup` after major tool updates
- Use the provided EE image for all ansible operations
- Don't install Python packages directly in the shell; use the EE

### 2. Code Quality
- Run `make lint` before committing
- Set up pre-commit hooks: `make pre-commit`
- Use molecule for testing roles and collections

### 3. Collaboration
- Keep the devfile.yaml in sync with team requirements
- Document any custom workflows in this README
- Share navigator configurations for different environments

## Troubleshooting

### Workspace Won't Start
- Check that all repository URLs in `devfile.yaml` are accessible
- Verify you have permissions to the repositories
- Review Dev Spaces logs for authentication errors

### Tools Not Found
- Run `make setup` to install ansible-dev-tools
- Check that the container image includes Python 3

### Permission Denied on Git Operations
- Configure SSH keys or tokens in Dev Spaces
- Ensure your GitHub/GitLab credentials are current

## Resources

- [Ansible Dev Tools Documentation](https://ansible.readthedocs.io/projects/dev-tools/)
- [Ansible Navigator Guide](https://ansible.readthedocs.io/projects/navigator/)
- [Execution Environment Setup](https://ansible.readthedocs.io/projects/builder/)
- [Devfile Specification](https://devfile.io/)
- [Red Hat Dev Spaces Documentation](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/)

## Contributing

To improve this meta repository:

1. Make changes to `devfile.yaml` or documentation
2. Test in a fresh Dev Spaces workspace
3. Submit a pull request with your improvements

## Support

For questions or issues:
- Check the troubleshooting section above
- Review Dev Spaces documentation
- Contact the platform team
- Open an issue in this repository