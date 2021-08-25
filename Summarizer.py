import numpy as np
import statistics

def statisticalSummarizer(data):
	return {
		'mean': np.sum(data) / float(len(data)),
		'median': np.median(data),
		'stdev': statistics.stdev(data),
		'variance': statistics.variance(data),
		'min': np.min(data),
		'max': np.max(data),
		'count': len(data)
	    }