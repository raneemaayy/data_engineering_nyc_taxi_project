import logging
import yaml 

from pipeline.extract import extract_all


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

trips_df, zones_df = extract_all(config)

print("\nTrips Shape:", trips_df.shape)
print("Zones Shape:", zones_df.shape)

print("\nTrips Columns Sample:")
print(trips_df.columns[:5].tolist())