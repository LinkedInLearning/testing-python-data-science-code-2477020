def test_metrics(client):
    rows = client.metrics()
    assert len(rows) > 0


def test_apiclient_logs_on_create_and_close(caplog):
    from api_client import APIClient  # adjust import if needed

    with caplog.at_level("INFO"):
        client = APIClient()
        client.close()

    assert any("created" in msg for msg in caplog.messages)
    assert any("closed" in msg for msg in caplog.messages)
