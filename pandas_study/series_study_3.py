import pandas as pd
print(pd.__version__)
# Series 計算 1
s = pd.Series([1, 2, 3, 4, 5], index=pd.date_range('20211101', periods=5))
print("max:", s.max())
print("max:", s.min())
print("max:", s.sum())
print("max:", s.mean())
print("max:", s.std())
