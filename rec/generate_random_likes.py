import os
import pandas as pd
import numpy as np
# cwd = os.getcwd()
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))
st = ""
with open(r'rec\daily_challenges.txt','r') as f:
    st = f.read()
    st = st.split('\n')
name_mapping = pd.DataFrame(st, columns=['Daily_challenges'])
df = pd.DataFrame(np.random.randint(0,2,size=(100, 88)),columns = name_mapping.index, index=list(range(100,200)))
df.to_csv(r'rec\user_challenges_likes.csv')
