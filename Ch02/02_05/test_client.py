from unittest.mock import MagicMock

import db_client

def test_metrics(monkeypatch):
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_conn
    mock_conn.execute.return_value = data
    monkeypatch.setattr(db_client, 'db_connect', lambda dsn: mock_conn)

    client = db_client.DBClient('/path/to/metrics.db')

    rows = client.metrics('2021-07-13', '2021-07-14')
    assert mock_conn.execute.called
    assert len(rows) == len(data)


data = [
    {"time":"2021-07-13T14:36:52.380Z","metric":"mem","value":227551548.0},
    {"time":"2021-07-13T14:36:52.380Z","metric":"cpu","value":30.04},
    {"time":"2021-07-13T14:36:53.337Z","metric":"mem","value":227567864.0},
    {"time":"2021-07-13T14:36:53.337Z","metric":"cpu","value":30.93},
    {"time":"2021-07-13T14:36:54.294Z","metric":"mem","value":227574696.0},
    {"time":"2021-07-13T14:36:54.294Z","metric":"cpu","value":32.61},
    {"time":"2021-07-13T14:36:55.251Z","metric":"mem","value":227567135.0},
    {"time":"2021-07-13T14:36:55.251Z","metric":"cpu","value":32.24},
    {"time":"2021-07-13T14:36:56.208Z","metric":"mem","value":227561333.0},
    {"time":"2021-07-13T14:36:56.208Z","metric":"cpu","value":31.27},
    {"time":"2021-07-13T14:36:57.165Z","metric":"cpu","value":31.33},
    {"time":"2021-07-13T14:36:57.165Z","metric":"mem","value":227586440.0},
]

