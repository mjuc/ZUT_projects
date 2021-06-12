import pandas as pd
import sklearn.naive_bayes as skn
import sklearn.model_selection as msl
import sklearn.preprocessing as prep

data=pd.read_csv('wine.data',sep=',')
Y=data.iloc[:,0]
X=data.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12,13]]

dicreet=input("Use discreet nbc(y/n): ")
if dicreet=='y':
    #6.1
    bins=int(input("Number of classes: "))
    disc=prep.KBinsDiscretizer(n_bins=bins,strategy='uniform')
    disc.fit(X)
    Xt=disc.transform(X)
    X_train, X_test, Y_train, Y_test = msl.train_test_split(Xt.toarray(), Y, test_size=0.5, random_state=0)
else:
    #6.2
    X_train, X_test, Y_train, Y_test = msl.train_test_split(X, Y, test_size=0.5, random_state=0)

lpl=input("Use Laplace smoothing(y/n): ")
if lpl=='n':
    #gaussian bayes
    gnb=skn.GaussianNB()
    y_pred = gnb.fit(X_train, Y_train).predict(X_test)
    prc=100-(X_test.shape[0]/((Y_test != y_pred).sum()))
    #print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (Y_test != y_pred).sum()))
    print("Percentage of correctly labeld points: %d" % prc)
else:
    #bayes with Laplace smoothing
    mnb=skn.MultinomialNB()
    y_pred = mnb.fit(X_train, Y_train).predict(X_test)
    prc=100-(X_test.shape[0]/((Y_test != y_pred).sum()))
    #print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (Y_test != y_pred).sum()))
    print("Percentage of correctly labeld points: %d" % prc)