# cms-for-slack-block-kit

## How to Use

### Setup
Activate venv, and install dependencies.

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Enable API on GCP.
- Google Drive API
- Google Sheets API

Make Service Account on GCP, and make new Key as JSON.  
Put key file in `./keys` .

Make Google Spread Sheet, and share to mail address written in key.

After all, you can treat GSpreadSheet from this apps.

```bash
make run
```

### Set env

And Set environments.

```
set -a && source ./.env && set +a
```

### Run

```
python your-script.py
```

## Usage
Python 3.11.2

## Useful Command

**On usual develop**
- `source .venv/bin/activate`
- `set -a && source ./.env && set +a`
- `pip freeze > requirements.txt`

**On setup**
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

**Other**
- `deactivate`
- `python -m venv .venv`

## Ref
- https://zenn.dev/yamagishihrd/articles/2022-09_01-google-spreadsheet-with-python