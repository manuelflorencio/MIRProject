from sklearn.metrics import precision_recall_fscore_support
import numpy as np


#Hay que ver el average que más conviene:
#average : string, [None (default), ‘binary’, ‘micro’, ‘macro’, ‘samples’, ‘weighted’]
#
#   If None, the scores for each class are returned. Otherwise, this determines the type of averaging performed on the data:
#
#   'binary':
#
#       Only report results for the class specified by pos_label. This is applicable only if targets (y_{true,pred}) are binary.
#   'micro':
#
#       Calculate metrics globally by counting the total true positives, false negatives and false positives.
#   'macro':
#
#       Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.
#   'weighted':
#
#       Calculate metrics for each label, and find their average, weighted by support (the number of true instances for each label). This alters ‘macro’ to account for label imbalance; it can result in an F-score that is not between precision and recall.
#   'samples':
#
#       Calculate metrics for each instance, and find their average (only meaningful for multilabel classification where this differs from accuracy_score).

#Referencia: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html


#Meter en dos arrays los datos de los archivos de klapuri y Benetos y el GT y ejecutar la función
#y_true -> GT
#y_pred -> extracted 


#precision_recall_fscore_support(y_true, y_pred, average='micro')