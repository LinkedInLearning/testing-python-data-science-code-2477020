def test_metrics(client):
    rows = client.metrics()
    assert len(rows) > 0