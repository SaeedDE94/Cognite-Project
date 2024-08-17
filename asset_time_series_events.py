import os
from dotenv import load_dotenv
from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthClientCredentials

# Load environment variables from .env file
load_dotenv()

# Authentication setup using environment variables
base_url = os.getenv("BASE_URL")
tenant_id = os.getenv("TENANT_ID")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

creds = OAuthClientCredentials(
    token_url=f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
    client_id=client_id,
    client_secret=client_secret,
    scopes=[f"{base_url}/.default"]
)

cnf = ClientConfig(
    client_name="OID-Api",
    project="publicdata",
    credentials=creds,
    base_url=base_url
)

client = CogniteClient(cnf)

print("Authenticated successfully ")

# Search for the asset by name
assets = client.assets.list(name="23-TT-92533", limit=10)

if len(assets) > 0:
    print(f"Found {len(assets)} assets with the name '23-TT-92533':")
    for asset in assets:
        print(f"External ID: {asset.external_id}, ID: {asset.id}, Name: {asset.name}")

    asset_id = assets[0].id

    # Count the number of time series associated  asset
    time_series = client.time_series.list(asset_ids=[asset_id])
    print(f"Number of time series: {len(time_series)}")

    # Count the number of events associated  asset
    events = client.events.list(asset_ids=[asset_id])
    print(f"Number of events: {len(events)}")

else:
    print("No assets found with the name '23-TT-92533'.")

# Retrieve the latest datapoint for the time series
latest_datapoint = client.time_series.data.retrieve_latest(external_id="pi:160884")
print(f"Latest datapoint: {latest_datapoint}")

# Getting  daily average over the last 4 weeks
from datetime import datetime, timedelta
start_time = datetime.now() - timedelta(weeks=4)
end_time = datetime.now()

datapoints = client.time_series.data.retrieve(
    external_id="pi:160884",
    start=start_time,
    end=end_time,
    aggregates=["average"],
    granularity="1d"
)

print(f"Daily averages over the last 4 weeks: {datapoints.average}")
