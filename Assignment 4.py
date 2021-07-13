#!/usr/bin/env python
# coding: utf-8

# # Name : Dhruvik Satani
# # Assignment 4

# # 1. What is Plotly?

# Plotly allows users to import, copy and paste, or stream data to be analyzed 
# and visualized. For analysis and styling graphs, Plotly offers a Python sandbox (NumPy supported), datagrid, and GUI. Python scripts can be saved, shared, and collaboratively edited in Plotly.
# 
# The Plotly Python graphing library is a scientific graphing library. Graphs can be styled with Python and a GUI, and shared with a URL for others to view, collaborate, or save a copy.
# 

# # 2. Where it is used?

# A major advantage of using Plotly is that it encourages us to be as creative as possible with your visualization since any complex plots only use three main concepts: data, layout, and figure objects. As an engineer, this is probably one of the best things to have as we can build and rebuild graphs in any way we want.
# 
# plotly enables Python users to create beautiful interactive web-based visualizations that can be displayed in Jupyter notebooks, saved to standalone HTML files, or served as part of pure Python-built web applications using Dash.

# # 3. Plot a Pie Chart of Indian Car companies market share % values

# In[1]:


import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd


# In[2]:


df = pd.read_csv("Car.csv")


# In[3]:


df


# In[4]:


fig = px.pie(df, values='Sales', names='Name', title='Cumulative Domestic Sales (April-Oct 2020)',
             hover_data=['Name'], labels={'Name':'Name'})
fig.update_traces(textposition='outside', textinfo='label+percent')
fig.show()


# # 4.Plot a Bar Chart with India's Covid-19 Active cases

# In[5]:


report = pd.read_csv('Book1.csv')


# In[6]:


report


# In[7]:


fig = px.bar(report, x="State", y="Positive", color="TotalSamples", title="Covid-19 Active Case (08/08/2020)",
            pattern_shape_sequence=["x"])
fig.show()


# # 5.Plot a Line Chart with India's active Covid-19 case recovery

# In[8]:


recovery = pd.read_csv("Book2.csv")


# In[9]:


recovery


# In[10]:


fig = px.line(recovery, x="Month", y="Recovered Cases", hover_name="Month",
        line_shape="spline", render_mode="svg")
fig.show()

