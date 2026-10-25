import pandas as pd

a=["classA","classB","classC","classD"]
strength=[60,56,48,62]

s = pd.DataFrame(a,strength)
print(s)