import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import itertools

from mlxtend.plotting import plot_decision_regions
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from mlxtend.classifier import EnsembleVoteClassifier
from mlxtend.data import iris_data

clf1 = LogisticRegression(random_state=0,solver='lbfgs', multi_class='auto' )

clf2 = RandomForestClassifier (random_state=0,n_estimators=100)

clf3= SVC(random_state=0, probability=True, gamma='auto')

eclf = EnsembleVoteClassifier(clfs=[clf1,clf2,clf3],weights=[2,1,1],voting='soft')

X,y= iris_data()
X=X[:,[0,2]]

gs = gridspec.GridSpec(1,4)

fig = plt.figure(figsize=(16,4))
for clf,lab,grd in zip(
[clf1,clf2,clf3,eclf],
[ 'Logistic Regression', 'Random Forest',
'RBF kernel SVM', 'Ensemble'],
itertools.product([0,1], repeat=2)):
    clf.fit(X,y)
    ax = plt.subplot (gs[0,grd[0]*2 +grd[1]])
    fig= plot_decision_regions (X=X,y=y,clf=clf,legend=2)
    plt.title(lab)
plt.show ()
