import pandas as pd
import streamlit as st
df1 = pd.DataFrame({'Sr.no':[1,2,3,4,5],
                    'Gender':["M",'F','F','M','M'],
                    'Weight':[50,55,60,70,75],
                    'Height':[5.5,5.7,5.8,5.9,6.2]})
#print(df1)
st.table(df1)