from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

digits = load_digits()
X, y = digits.data, digits.target
X_train, X_test, y_train, y_test = \
    train_test_split(X, y)

clf = SVC()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)