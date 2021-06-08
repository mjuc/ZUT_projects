import sklearn.datasets as sclr
import sklearn as sk
import matplotlib.pyplot as mpl
import pandas as pd
import numpy as np

#1

classes = sclr.make_classification()

mpl.scatter(classes)
mpl.show()

clasificators = []
clasificators.append(sk.naive_bayes.GaussianNB())
clasificators.append(sk.discriminant_analisys.QuadraticDiscriminantAnalysis())
clasificators.append(sk.neighbors.KNeighborsClassifier())
clasificators.append(sk.svm.SVC(probability=True))
clasificators.append(sk.tree.DecisionTreeClassifier())

acc = []
rec = []
prec = []
f1 = []
roc = []

for i in clasificators:
    temp_acc = []
    temp_rec = []
    temp_prec = []
    temp_f1 = []
    temp_roc = []
    for j in range(1,100):
        X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(i,0.2,0.8)
        test = i.fit(X_train,y_train)
        temp_acc.append(sk.metrics.accuracy_score(y_train,test))
        temp_rec.append(sk.metrics.recall_score(y_train,test))
        temp_prec.append(sk.metrics.precision_score(y_train,test))
        temp_f1.append(sk.metrics.f1_score(y_train,test))
        temp_roc.append(sk.metrics.roc_auc_score(y_train,test))
        
    acc.append(mean(temp_acc))
    rec.append(mean(temp_rec))
    prec.append(mean(temp_prec))
    f1.append(mean(temp_f1))
    roc.append(mean(temp_roc))

data = {'Accuracy':acc,'Recall':rec,'Precission':prec,'F1':f1,'AUC ROC':roc}
cls = pd.DataFrame(data)

print(cls.groupby('Accuracy'))