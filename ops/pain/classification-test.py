#/usr/bin/python3
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier
from random import randrange
import numpy as np
import time

if __name__=='__main__':
	mnist = fetch_openml('mnist_784', version=1, cache=True, as_frame=False)
	mnist.target = mnist.target.astype(np.int8)
	#list of the image data, //pixel brightness
	X = mnist["data"]
	#labels, in this case 0 1 2 3 4 5 6 7...
	y = mnist["target"]

	X_train = X[:60000]
	X_test = X[60000:]
	y_train = y[:60000]
	y_test = y[60000:]

	shuffle = np.random.permutation(60000)

	X_train = X_train[shuffle]
	y_train = y_train[shuffle]

	y_train_5 = (y_train == 5)
	y_test_5 = (y_test == 5)

	sgd_clf = SGDClassifier(max_iter=5, tol=-np.infty, random_state=42)
	sgd_clf.fit(X_train, y_train_5)

	i=0
	while(True):
		pic = X[i]
		print("Trying number " + str(y[i]))
		print(sgd_clf.predict([pic]))
		time.sleep(.5)
		i=i+1