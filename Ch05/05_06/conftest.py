from collections import namedtuple

import pytest
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

Data = namedtuple('Data', 'version X y')


def _load_data():
    digits = load_digits()
    return digits['data'], digits['target']


@pytest.fixture
def regression_data():
    # TODO: Load from regression database
    X, y = _load_data()
    return Data(
        version='2022-02-17',
        X=X,
        y=y,
    )


Model = namedtuple('Model', 'version clf')

@pytest.fixture
def model():
    # TODO: Load model from model store
    X, y = _load_data()
    X_train, _, y_train, _ = train_test_split(X, y, random_state=123)

    clf = Pipeline(steps=[
        ('pca', PCA(n_components=10)),
        ('svc', SVC(random_state=353))
    ])

    clf.fit(X_train, y_train)
    return Model(version='2022-03-24', clf=clf)