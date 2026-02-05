import pandas as pd
import numpy as np
import os
from itertools import product

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    Returns distance in miles
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    # Radius of earth in miles
    r = 3959
    
    return c * r

# Define paths to CSV files in the data subfolder

raw_data_folder = "data/raw"
procesed_data_folder = "data/processed"
customers_csv = os.path.join(raw_data_folder, "cincinnati_locations.csv")
warehouse_csv = os.path.join(raw_data_folder, "warehouse_locations.csv")


# Read the CSV file into a pandas DataFrame
df_customers = pd.read_csv(customers_csv)
df_warehouses = pd.read_csv(warehouse_csv)

# Create customer demand
df_customers['demand'] = np.random.randint(100, 1001, 100)

# Create warehouse capacity
default_capacity = np.ceil(df_customers['demand'].sum() / 3 * 1.2) 
df_warehouses['capacity'] = default_capacity

print(df_warehouses.dtypes)

# Create a list to store all distance calculations
distances = []

# Calculate distances between each Cincinnati location and each warehouse
for _, customer in df_customers.iterrows():
    for _, warehouse in df_warehouses.iterrows():
        distance = haversine_distance(
            customer['latitude'], 
            customer['longitude'],
            warehouse['latitude'], 
            warehouse['longitude']
        )
        
        distances.append({
            'customer_location': customer['location_name'],
            'customer_lat': customer['latitude'],
            'customer_lon': customer['longitude'],
            'warehouse': warehouse['location_name'],
            'warehouse_lat': warehouse['latitude'],
            'warehouse_lon': warehouse['longitude'],
            'distance_miles': round(distance, 2)
        })

# Create DataFrame from distances
df_distances = pd.DataFrame(distances)

df_customers.to_parquet(os.path.join(procesed_data_folder, "customers.parquet"))
df_warehouses.to_parquet(os.path.join(procesed_data_folder, "warehouses.parquet"))
df_distances.to_parquet(os.path.join(procesed_data_folder, "distances.parquet"))