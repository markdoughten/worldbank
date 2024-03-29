# builtin libraries
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.gridspec as gridspec
import math
import numpy as np

class Chart:    

    def subplots(self, commands):
        # set the parameters
        height = math.ceil(len(commands) / 3)
        width = len(commands)

        # adjust the width for small subplots 
        if width < 3:
            fig = plt.figure(figsize=(width * 5, height * 4))
        else:
            fig = plt.figure(figsize=(15, height * 4))
            width = 3

        # create the grid layout based on the command inputs 
        spec = gridspec.GridSpec(height, width, figure=fig)
        
        return fig, height, spec


    def chart(self, commands):
        fig, height, spec = self.subplots(commands)
        return fig, height, spec


    def add_window(self, fig, spec, y_pos, x_pos):
        ax = fig.add_subplot(spec[y_pos, x_pos])
        return fig, ax


    def plot(self, ax, series, country_name):
        x = series.index
        y = series.values

        ax.plot(x, y, label=country_name)

        return ax


    def set_label(self, ax, country_name):
        ax.set_title(country_name)

        return ax


    def set_units(self, ax, units):
        # units
        if units == '$':
            ax.yaxis.set_major_formatter(self.currency)
        elif units == '%':
            ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
        else:
            ax.yaxis.set_major_formatter(self.standard)

        return ax


    def currency(self, x, pos):
        """Format the currency values for the chart"""

        if x >= 1e12:
            x = '${:1.1f}T'.format(x * 1e-12)
        elif x >= 1e9:
            x = '${:1.1f}B'.format(x * 1e-9)
        else:
            x = '${:1.1f}M'.format(x * 1e-6)
        return x


    def standard(self, x, pos):
        """Format regular values"""

        if x >= 1e9:
            x = '{:1.1f}B'.format(x * 1e-9)
        elif x >= 1e6:
            x = '{:1.1f}M'.format(x * 1e-6)
        else:
            x = '{:1.1f}K'.format(x * 1e-3)
        return x
