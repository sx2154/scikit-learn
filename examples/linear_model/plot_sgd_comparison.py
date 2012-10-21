"""
================================
Comparsing various Stochastic Gradient Solvers
================================

An example showing how the different SGDClassifiers perform
on the hand-written digits dataset

"""
# Author: Rob Zinkov <rob at zinkov dot com>
# License: Simplified BSD

import numpy as np
import pylab as pl
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import SGDClassifier, Perceptron

heldout = [0.95, 0.90, 0.75, 0.50, 0.01]
rounds = 20
digits = datasets.load_digits()

classifiers = [
    ("SGD", SGDClassifier()),
    ("Perceptron", Perceptron()),
    ("PA-I",  SGDClassifier(learning_rate='pa1', 
                            eta0=0.001, alpha=0.01)),
    ("PA-II", SGDClassifier(learning_rate='pa2', 
                            eta0=0.001, alpha=0.01)),
    ]

xx = 1-np.array(heldout)
for name,clf in classifiers:
    yy = []
    for i in heldout:
        yy_ = []
        for r in range(rounds):
            X_train, X_test, y_train, y_test = train_test_split(digits.data, 
                                                                digits.target, 
                                                                test_size=i)
            clf.fit(X_train,y_train)
            y_pred = clf.predict(X_test)
            yy_.append(1-np.mean(y_pred==y_test))
        yy.append(np.mean(yy_))
    pl.plot(xx, yy, label=name)

pl.legend(loc="upper right")
pl.xlabel("Proportion train")
pl.ylabel("Test Error Rate")
pl.show()
