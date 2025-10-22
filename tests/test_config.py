"""Tests for configuration management."""

import pytest
from ansible_devspaces.config import DevSpacesConfig


def test_default_config():
    """Test that default configuration is loaded correctly."""
    config = DevSpacesConfig()
    assert config.config is not None
    assert "ansible_python_interpreter" in config.config
    assert config.config["ansible_host_key_checking"] is False


def test_get_env_vars():
    """Test environment variable generation."""
    config = DevSpacesConfig()
    env_vars = config.get_env_vars()
    
    assert "ANSIBLE_PYTHON_INTERPRETER" in env_vars
    assert env_vars["ANSIBLE_HOST_KEY_CHECKING"] == "False"
    assert "ANSIBLE_RETRY_FILES_ENABLED" in env_vars


def test_boolean_conversion():
    """Test that boolean values are converted correctly."""
    config = DevSpacesConfig()
    env_vars = config.get_env_vars()
    
    # Test boolean True conversion
    config.config["test_true"] = True
    env_vars = config.get_env_vars()
    assert env_vars["TEST_TRUE"] == "True"
    
    # Test boolean False conversion
    config.config["test_false"] = False
    env_vars = config.get_env_vars()
    assert env_vars["TEST_FALSE"] == "False"
