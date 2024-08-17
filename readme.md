
---

# Cognite Project

This Python project provides a hands-on experience with Cognite Data Fusion (CDF) by working with the Open Industrial Data project.

## Features

- **Authentication**: Securely authenticate with Cognite Data Fusion using environment variables.
- **Asset Management**: Search for assets by name and retrieve details.
- **Time Series Analysis**: Fetch and analyze time series data.
- **Event Counting**: Count and list events associated with specific assets.

## Setup

To install all the needed libraries, run this with pip:
```bash
pip install -r requirements.txt
```

You'll also need to create a .env file at the root directory with the following:
```
TENANT_ID=your_token_id
BASE_URL=your_base_url
CLIENT_ID=_your_client_id
CLIENT_SECRET=your_client_secrent 
```

## Usage

1. **Authentication**: Configure environment variables in a `.env` file.
2. **Running Scripts**: Execute Python scripts to retrieve and analyze data from CDF.

---

