from datetime import datetime, timedelta
from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthClientCredentials

# Authentication setup
base_url = "https://api.cognitedata.com"
tenant_id = "48d5043c-cf70-4c49-881c-c638f5796997"

creds = OAuthClientCredentials(
    token_url=f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
    client_id="1b90ede3-271e-401b-81a0-a4d52bea3273",
    client_secret="qiN8Q~bDeR2KIl.TqGneUvdIxBNBI8veoYKWbbzd",
    scopes=[f"{base_url}/.default"]
)

cnf = ClientConfig(
    client_name="OID-Api",
    project="publicdata",
    credentials=creds,
    base_url=base_url
)

client = CogniteClient(cnf)

print("Authenticated successfully")

# The latest datapoint for the time series
latest_datapoint = client.time_series.data.retrieve_latest(external_id="pi:160884")
print(f"Latest datapoint: {latest_datapoint}")

# Here daily average over the last 4 weeks
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
