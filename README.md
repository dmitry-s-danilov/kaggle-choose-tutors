# [Kaggle competition. Choose tutors][1]
## Choose proper tutors for math exam

### Overview

#### Description

In this competition your task will be to predict the probability
for a tutor to be a proper one for preparing for the math exam.
You will be given two datasets:
_train.csv_ (contains all features and the target) and
_test.csv_ (only features).

#### Evaluation

The evaluation metric is [ROC AUC][2]

### Data

- train.csv
- test.csv
- submission_example.csv

### Rules

You can only use these imports:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
```

---

[1]: https://www.kaggle.com/c/choose-tutors
[2]: https://en.wikipedia.org/wiki/Receiver_operating_characteristic
