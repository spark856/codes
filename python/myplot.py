#!/usr/bin/env python
# -*- coding: utf-8 -*-
import plotly.offline as offline
import plotly.graph_objs as go
import numpy as np
from plotly.offline import init_notebook_mode
init_notebook_mode()

def myplot(x,y,z):

    scatter = go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color='red', size=0.5))

    data = [scatter]

    layout = go.Layout(
                    scene = dict(
                    xaxis = dict(
                        nticks=4, range = [0,100],),
                    yaxis = dict(
                        nticks=4, range = [0,100],),
                    zaxis = dict(
                        nticks=4, range = [0,100],),
                    aspectmode='cube'),
                    width=700,
                    margin=dict(
                    r=20, l=10,
                    b=10, t=10),
                    updatemenus=[{
                   'buttons': [
                       {'args': [None],
                        'label': 'Play',
                        'method': 'animate'}
                       ]}]
                  )

    frames = [dict(data=[dict(x=[x[k]],
                              y=[y[k]],
                              z=[z[k]],
                              mode='markers',
                              marker=dict(color='red', size=0.5),
                              type='scatter3d'
                              )
                         ]) for k in range(len(x))]
    figure = dict(data=data, layout=layout)
    offline.iplot(figure, filename='EparaB.html')