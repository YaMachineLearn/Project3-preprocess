#Project 3 - preprocess
###Initialize
1. put the raw training data "Holmes_Training_Data/" here.
2. run ```python trimTrainingData.py``` and it will create "trim_Holmes_Training_Data/" folder, which contains header-removed .txt files.

###Pre-process training and testing data
Preprocess training data with tag < s > (for word2vec training) <br/>
```cat trim_Holmes_Training_Data/*.TXT | ./preprocessing-train_v4.sh > training_v4_tag.txt```

Remove tag < s > from training_vxxx_tag.txt (for RNN training) <br/>
```cat training_v4_tag.txt | ./remove_s_tag.sh > training_v4_noTag.txt```

Word2vec training <br/>
```word2vec -train training_v4_tag.txt -output vec_v4.txt -size 300 -min-count 10```
Unused parameters <br/>
```-window 5 -sample 1e-4 -negative 5 -hs 0 -binary 0 -cbow 1 -iter 3```

Preprocess testing data <br/>
```cat testing_data.txt | ./preprocessing-test_v4.sh > test_v4.txt```

###other utilities
Extract sentences that is shorter than a threshold <br/>
(Before run the following code, you should change the file names or threshold in the .py file)<br/>
```python cutTrainingData_threshold.py```

Extract part of training data randomly from training_vxxx_tag.txt or training_vxxx_noTag.txt<br/>
(Before run the following code, you should change the file names in the .py file)<br/>
```python resizeTrainingData.py```


