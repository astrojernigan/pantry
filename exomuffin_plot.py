import xarray

def retreive_from_netcdf(filename, variable):
	data = xarray.open_dataset(filename)
	exec('values = data.' + variable + '.values')
	data.close()
	return values

def create_plot(name, array, minimum, maximum, colormap='viridis', levels=16, normalizer='default', logMin=1**(-20), y_axis_title_base, y_axis_list, x_axis_title_base, x_axis_list,
	plot, array = plt.subplots(len(y_axis_list), len(x_axis_list), figsize=(len(y_axis_list)*2 + 4, len(x_axis_list)*3 + 1.5), sharex='col', sharey='row')
	
	match normalizer:
		case 'log':
			normalizer = colors.LogNorm(logMin, maximum*multiplier)
			clevels = np.geomspace(logMin, varMax*multiplier)
		case 'symmetric':
			if maximum < absolute(minimum):
				maximum = np.absolute(minimum)
			minimum = -1*maximum
			normalizer = colors.Normalize(minimum*multiplier, maximum*multiplier)
			clevels = np.linspace(minimum*multiplier, maximum*multiplier, levels)
		case 'default':
			normalizer = colors.Normalize(minimum*multiplier, maximum*multiplier)
			clevels = np.linspace(minimum*multiplier, maximum*multiplier, levels)

	if not y:
		arr[x,y].set_ylabel(ylabel, fontsize=axis_label_fontsize)
		arr[x,y].annotate(y_axis_title_base + y_axis_list[x], xy=(-3,1), xycoords=arr[x,y].yaxis.label, fot=axis_label_fontsize)

	

	plot.savefig(name, bbox_inches='tight', dpi=300)
	plt.close()

def create_production_plot
