import xarray
import numpy
import matplotlib

def retreive_from_netcdf(filename, variable):
	data = xarray.open_dataset(filename)
	exec('values = data.' + variable + '.values')
	data.close()
	return values

def create_plot(name, array, minimum, maximum, colormap='viridis', levels=16, normalizer='default', log_min=1**(-20), y_axis_title, y_axis_list, x_axis_title, x_axis_list, ylabel='Latitude', xlabel='Month', colorbar_label) 
	plot, array = matplotlib.pyplot.subplots(len(y_axis_list), len(x_axis_list), figsize=(len(y_axis_list)*2 + 4, len(x_axis_list)*3 + 1.5), sharex='col', sharey='row')
	
	match normalizer:
		case 'log':
			normalizer = matplotlib.colors.LogNorm(log_min, maximum*multiplier)
			clevels = numpy.geomspace(log_min, maximum*multiplier)
		case 'symmetric':
			if maximum < absolute(minimum):
				maximum = numpy.absolute(minimum)
			minimum = -1*maximum
			normalizer = matplotlib.colors.Normalize(minimum*multiplier, maximum*multiplier)
			clevels = numpy.linspace(minimum*multiplier, maximum*multiplier, levels)
		case 'default':
			normalizer = matplotlib.colors.Normalize(minimum*multiplier, maximum*multiplier)
			clevels = numpy.linspace(minimum*multiplier, maximum*multiplier, levels)

    for y in range(len(y_axis_list)):
        for x in range(len(x_axis_list)):
            im = matplotlib.color
	        if not y:
    		    array[x,y].set_ylabel(ylabel, fontsize=axis_label_fontsize)
	    	    array[x,y].annotate(y_axis_title + y_axis_list[y], xy=(-3,1), xycoords=arr[x,y].yaxis.label, fontsize=axis_label_fontsize, ha='left')
            if not x:
                array[x,y].set_title(x_axis_title + x_axis_list[x], fontsize=axis_label_fontsize)
            if x==(len(x_axis_list)-1):
                array[x,y].set_xlabel(xlabel, fontsize=axis_label_fontsize)

    cbar = plot.colorbar(im, ax=array, orientation='horizontal', shrink=0.5, aspect=40, pad=0.075, anchor=(0.5, 0.75), boundaries=clevels, extend='both', spacing='proportional')
    cbar.ax.tick_params(labelsize=tick_fontsize)
    cbar.set_label(colorbar_label, fontsize=large, weight='bold')
	plot.savefig(name, bbox_inches='tight', dpi=300)
	matplotlib.pyplot.close()

def create_production_plot
