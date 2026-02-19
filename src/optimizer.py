import numpy as np

def optimize_prices(predicted_prices):

    revenue_before = float(np.sum(predicted_prices))

    optimized_prices = predicted_prices * 1.1 

    revenue_after = float(np.sum(optimized_prices))

    return {
        "revenue_before": revenue_before,
        "revenue_after": revenue_after,
        "improvement_percent": 
            float(((revenue_after - revenue_before) / revenue_before)) * 100
    }