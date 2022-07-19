import json

from sklearn.metrics import accuracy_score


def test_regression(model, regression_data):
    out = model.clf.predict(regression_data.X)
    score = accuracy_score(regression_data.y, out)
    report = {
        'model_version': model.version,
        'data_version': regression_data.version,
        'accuracy': score,
    }
    print(f'regression: {json.dumps(report)}')
    # TODO: Report to regression database (Prometheus, InfluxDB ...)