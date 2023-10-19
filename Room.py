# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 00:12:11 2023

@author: Gary
"""
import plotly.graph_objects as go
import plotly.io as pio

class Room:
    pio.renderers.default = 'browser'
    
    def __init__(self, unit_length = 1, zero=0):
        self.zero = zero
        self.unit_length = unit_length
        origin = 0+zero
        length = zero+unit_length
        self.origin = origin
        self.length = length
        self.room_x = [origin, length, length, origin]
        self.room_y = [origin, origin, length, length]
        self.room_z = [origin, origin, origin, origin]
        self.fig = go.Figure()
        self.AddFloor()
        self.AddRightWall()
        self.AddLeftWall()
        self.fig.update_layout(
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                # aspectmode='cube',
            )
        )
        self.fig.show()
    
    def AddFloor(self, color='gray',opacity=1):
        self.fig.add_trace(go.Mesh3d(
            x=self.room_x,
            y=self.room_y,
            z=[self.origin, self.origin, self.origin, self.origin],
            i=[0, 1, 2, 3, 0],
            j=[1, 2, 3, 0, 1],
            k=[3, 2, 1, 0, 3],
            opacity=opacity,
            color=color,
            showscale=False,
            name='Floor'
        ))
    
    def AddRightWall(self, color='red',opacity=0.7):
        new_wall_x = [self.origin, self.origin, self.origin, self.origin, self.origin]
        new_wall_y = [self.origin, self.origin, self.length, self.length, self.origin]
        new_wall_z = [self.origin, self.length, self.length, self.origin, self.origin]
        self.fig.add_trace(go.Mesh3d(
            x=new_wall_x,
            y=new_wall_y,
            z=new_wall_z,
            i=[1, 2, 3, 0],
            j=[2, 3, 0, 1],
            k=[2, 1, 0, 3],
            showscale=False,
            opacity=opacity,
            color=color,
            name='Right Wall'
        ))
    
    def AddLeftWall(self, color='purple',opacity=0.7):
        new_wall_x = [self.origin, self.length, self.length, self.origin, self.origin]
        new_wall_y = [self.origin, self.origin, self.origin, self.origin, self.origin]
        new_wall_z = [self.origin, self.origin, self.length, self.length, self.origin]
        self.fig.add_trace(go.Mesh3d(
            x=new_wall_x,
            y=new_wall_y,
            z=new_wall_z,
            i=[1, 2, 3, 0],
            j=[2, 3, 0, 1],
            k=[2, 1, 0, 3],
            showscale=False,
            opacity=opacity,
            color=color,
            name='Left Wall'
        ))

room = Room()
