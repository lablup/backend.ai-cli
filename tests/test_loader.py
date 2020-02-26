from unittest import mock

import sys
from typing import Any, Dict

from ai.backend.cli.loader import load_entry_points

if sys.version_info < (3, 8, 0):
    from importlib_metadata import EntryPoint
else:
    from importlib.metadata import EntryPoint  # type: ignore


class DummyCommandGroup:
    def __init__(self, commands: Dict[str, Any]):
        self.commands = commands

    def add_command(self, obj: Any, *, name: str):
        self.commands[name] = obj


def test_entrypoint_detection_subgroups(mocker):

    def _load(self):
        return DummyCommandGroup({'subcmd': self.value})

    mocker.patch.object(EntryPoint, 'load', _load)
    _entry_points = {
        'console_scripts': [
            EntryPoint(name='not-this-one', group='console_scripts', value='testing.wrong:main'),
        ],
        'backendai_cli_v10': [
            EntryPoint(name='mgr', group='backendai_cli_v10', value='testing.manager.cli:main'),
            EntryPoint(name='ag', group='backendai_cli_v10', value='testing.agent.cli:main'),
            EntryPoint(name='mgr.start-server', group='backendai_cli_v10',
                       value='testing.manager.server:main'),
            EntryPoint(name='ag.start-server', group='backendai_cli_v10',
                       value='testing.agent.server:main'),
        ],
    }
    mock_entry_points = mock.MagicMock(return_value=_entry_points)
    mocker.patch('ai.backend.cli.loader.entry_points', mock_entry_points)

    dummy_main = load_entry_points()
    mock_entry_points.assert_called_once()

    assert 'not-this-one' not in dummy_main.commands
    assert 'mgr' in dummy_main.commands
    assert 'ag' in dummy_main.commands
    assert dummy_main.commands['mgr'].commands['subcmd'] == 'testing.manager.cli:main'
    assert dummy_main.commands['ag'].commands['subcmd'] == 'testing.agent.cli:main'
    # In actual packages, commands['start-server'] is just a Click command, instaed of command group.
    assert (dummy_main.commands['mgr'].commands['start-server'].commands['subcmd'] ==
            'testing.manager.server:main')
    assert (dummy_main.commands['ag'].commands['start-server'].commands['subcmd'] ==
            'testing.agent.server:main')


def test_entrypoint_detection_global_replace(mocker):

    def _load(self):
        return DummyCommandGroup({'subcmd': self.value})

    mocker.patch.object(EntryPoint, 'load', _load)
    _entry_points = {
        'console_scripts': [
            EntryPoint(name='not-this-one', group='console_scripts', value='testing.wrong:main'),
        ],
        'backendai_cli_v10': [
            EntryPoint(name='_', group='backendai_cli_v10', value='testing.client.cli:main'),
        ],
    }
    mock_entry_points = mock.MagicMock(return_value=_entry_points)
    mocker.patch('ai.backend.cli.loader.entry_points', mock_entry_points)

    dummy_main = load_entry_points()
    mock_entry_points.assert_called_once()

    assert 'not-this-one' not in dummy_main.commands
    assert dummy_main.commands['subcmd'] == 'testing.client.cli:main'
