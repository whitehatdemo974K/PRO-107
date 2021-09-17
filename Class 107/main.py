from datetime import time
import pandas as pd
import csv
import plotly.graph_objects as go
df=pd.read_csv("student_id.csv")
student=df.loc[df['student_id']=="TRL_zet"]
print(student.groupby("level")["attempt"].mean())
fig=go.Figure(go.Scatter(
    x=student.groupby("level")["attempt"].mean(),
    y=['Level 1','Level 2','Level 3','Level 4'],
    orientation='h'))

fig.show()


