#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 00:30:19 2024

@author: pavelkim
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import plotly.express as px
import random
import datetime

# Simulate data
ips = [f"192.168.0.{i}" for i in range(1, 11)]
data = []
for ip in ips:
    open_ports = np.random.choice(range(20, 1024), size=np.random.randint(5, 15), replace=False)
    for port in open_ports:
        data.append({'IP': ip, 'Port': port, 'Timestamp': datetime.datetime.now() + datetime.timedelta(seconds=random.randint(1, 1000))})

df = pd.DataFrame(data)

# Save simulated data
df.to_csv('simulated_port_scanning_data.csv', index=False)

# Plotting
def plot_heatmap(df):
    df['IP_Num'] = df['IP'].apply(lambda x: int(x.split('.')[-1]))
    pivot_table = df.pivot_table(index='IP_Num', columns='Port', aggfunc='size', fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, cmap='coolwarm', cbar=True)
    plt.title('Heatmap of Open Ports by IP')
    plt.xlabel('Port')
    plt.ylabel('IP Address (Last Octet)')
    plt.show()

def plot_3d_scatter(df):
    df['IP_Num'] = df['IP'].apply(lambda x: int(x.split('.')[-1]))
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['Port'], df['IP_Num'], df.index, c='skyblue', s=60)
    ax.set_xlabel('Port')
    ax.set_ylabel('IP Address (Last Octet)')
    ax.set_zlabel('Index')
    plt.title('3D Scatter Plot of Open Ports')
    plt.show()

def plot_port_distribution(df):
    plt.figure(figsize=(12, 8))
    sns.histplot(df['Port'], kde=True, bins=30, color='skyblue')
    plt.title('Distribution of Open Ports')
    plt.xlabel('Port')
    plt.ylabel('Frequency')
    plt.show()

def plot_3d_scatter_with_plotly(df):
    fig = px.scatter_3d(df, x='Timestamp', y='Port', z='IP', color='IP', title='3D Scatter Plot of Packet Sizes Over Time')
    fig.update_layout(scene=dict(xaxis_title='Timestamp', yaxis_title='Port', zaxis_title='IP Address'))
    fig.show()

# Visualizations
plot_heatmap(df)
plot_3d_scatter(df)
plot_port_distribution(df)
plot_3d_scatter_with_plotly(df)

