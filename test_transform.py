import logging
import yaml

from pipeline.extract import extract_all
from pipeline.transform import transform_all


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

# Load configuration
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Extract raw data
trips_df, zones_df = extract_all(config)

# Display raw shape
print("\nRaw Trips Shape:", trips_df.shape)

# Transform data
clean_df = transform_all(
    trips_df,
    zones_df,
    config
)

# Display transformed shape
print("\nClean Data Shape:", clean_df.shape)

# Preview engineered columns
print("\nEngineered Columns:")

print(
    clean_df[
        [
            "trip_duration_mins",
            "speed_mph",
            "fare_per_mile",
            "tip_percentage",
            "pickup_hour",
            "is_weekend"
        ]
    ].head()
)