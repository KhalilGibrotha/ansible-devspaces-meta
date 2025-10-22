"""Tests for CLI functionality."""

import pytest
from unittest.mock import patch, MagicMock
from ansible_devspaces import cli


def test_version_command(capsys):
    """Test version command."""
    with patch('sys.argv', ['ansible-devspaces', 'version']):
        result = cli.main()
        captured = capsys.readouterr()
        assert result == 0
        assert "ansible-devspaces version" in captured.out


def test_invalid_command():
    """Test handling of invalid commands."""
    with patch('sys.argv', ['ansible-devspaces', 'invalid']):
        with pytest.raises(SystemExit):
            cli.main()


@patch('subprocess.run')
def test_playbook_command(mock_run):
    """Test playbook command execution."""
    mock_run.return_value = MagicMock(returncode=0)
    
    with patch('sys.argv', ['ansible-devspaces', 'playbook', 'test.yml']):
        result = cli.main()
        
    assert result == 0
    mock_run.assert_called_once()
    call_args = mock_run.call_args[0][0]
    assert call_args[0] == 'ansible-playbook'
    assert 'test.yml' in call_args


@patch('subprocess.run')
def test_lint_command(mock_run):
    """Test lint command execution."""
    mock_run.return_value = MagicMock(returncode=0)
    
    with patch('sys.argv', ['ansible-devspaces', 'lint', 'playbooks/']):
        result = cli.main()
        
    assert result == 0
    mock_run.assert_called_once()
    call_args = mock_run.call_args[0][0]
    assert call_args[0] == 'ansible-lint'
    assert 'playbooks/' in call_args


@patch('subprocess.run')
def test_galaxy_command(mock_run):
    """Test galaxy command execution."""
    mock_run.return_value = MagicMock(returncode=0)
    
    with patch('sys.argv', ['ansible-devspaces', 'galaxy', 'install', '-r', 'requirements.yml']):
        result = cli.main()
        
    assert result == 0
    mock_run.assert_called_once()
    call_args = mock_run.call_args[0][0]
    assert call_args[0] == 'ansible-galaxy'
    assert 'install' in call_args
    assert 'requirements.yml' in call_args
