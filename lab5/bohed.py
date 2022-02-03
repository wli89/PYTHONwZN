#Program5
#Lis
#Wykresy, bohed

from math import pi
import pandas as pd
from bokeh.palettes import Category20b
from bokeh.transform import cumsum
from bokeh.io import output_notebook

from bokeh.io import show
from bokeh.plotting import figure

from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral10
from bokeh.transform import factor_cmap

print("loading...")
#output_notebook()

x = {
    'Tlen' : 45,
    'Krzem': 26,
    'Glin' :  8,
    'Żelazo': 6,
    'Wapń' :  6,
    'Magnez': 3,
    'Inne' :  6,
}

data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'country'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20b[len(x)]

plot = figure(height=350, title="SKŁAD SKORUPY ZIEMSKIEJ", title_location="above", toolbar_location="below",
           tools="hover", tooltips="@country: @value", x_range=(-1.0, 1.0))

plot.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="pink", fill_color='color', legend_field='country', source=data)

plot.axis.axis_label = None
plot.axis.visible = False
plot.grid.grid_line_color = None

show(plot)

##########################

data = ['Tlen', 'Krzem','Glin','Żelazo','Wapń', 'Magnez', 'Inne']
count = [45,26,8,6,6,3,6]

plot1 = figure(title="SKŁAD SKORUPY ZIEMSKIEJ", tools="", toolbar_location=None,
           y_range=data, x_range=[0,100])

plot1.segment(0, data, count, data, line_width=2, line_color="black", )
plot1.circle(count, data, size=10, fill_color="pink", line_color="black", line_width=2, )

show(plot1)

###########################

source = ColumnDataSource(data=dict(data=data, count=count))

plot2 = figure(x_range=data, height=500, toolbar_location=None, title="SKŁAD SKORUPY ZIEMSKIEJ")
plot2.vbar(x='data', top='count', width=0.9, source=source, legend_field="counts",
       line_color='white', fill_color=factor_cmap('data', palette=Spectral10, factors=data))

plot2.xgrid.grid_line_color = None
plot2.y_range.start = 0
plot2.y_range.end = 100
plot2.legend.location = "top_right"

show(plot2)
