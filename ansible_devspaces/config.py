"""Configuration management for Ansible DevSpaces."""

import os
from pathlib import Path
from typing import Dict, Any


class DevSpacesConfig:
    """Manage DevSpaces-specific Ansible configuration."""
    
    DEFAULT_CONFIG = {
        "ansible_python_interpreter": "/usr/bin/python3",
        "ansible_host_key_checking": False,
        "ansible_retry_files_enabled": False,
        "ansible_stdout_callback": "yaml",
        "ansible_callbacks_enabled": "profile_tasks, timer",
    }
    
    def __init__(self, config_path: Path = None):
        """Initialize configuration.
        
        Args:
            config_path: Optional path to custom configuration file
        """
        self.config_path = config_path
        self.config = self.DEFAULT_CONFIG.copy()
        
    def get_env_vars(self) -> Dict[str, str]:
        """Get environment variables for Ansible.
        
        Returns:
            Dictionary of environment variables
        """
        env_vars = {}
        for key, value in self.config.items():
            env_key = key.upper()
            if isinstance(value, bool):
                env_vars[env_key] = "True" if value else "False"
            else:
                env_vars[env_key] = str(value)
        return env_vars
    
    def apply_to_environment(self):
        """Apply configuration to current environment."""
        env_vars = self.get_env_vars()
        os.environ.update(env_vars)
