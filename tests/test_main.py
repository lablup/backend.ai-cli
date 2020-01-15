from unittest import mock


def test_entrypoint_detection(mocker):
    mock_iter_entry_points = mock.MagicMock(return_value=[])
    mocker.patch('pkg_resources.iter_entry_points', mock_iter_entry_points)
    import ai.backend.cli.__main__  # noqa
    mock_iter_entry_points.assert_called_once()

    # TODO: It's impossible to mock main() before importing.
    #       Find a way to mock main.add_command...
