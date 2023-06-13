# FastApi Server

This is a guide to quickly setup the fast api python server to develop a test REST API.

## Steps 1:

Download the .zip file from above

## Step 2:

Create a virtual environment to run the server

`python -m venv environ`

## Step 4:

Activate the environment

`./environ/Scripts/activate`

## Step 5:

Install the dependencies

`pip install -r requirements.txt`

## Step 6:

Run server through uvicorn

`uvicorn server:app --host 0.0.0.0 --port 5000`

# Dependencies

- fastapi

- uvicorn[standard]
