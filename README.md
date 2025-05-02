# 📦 Plex Label Remover

A Python script to remove **all labels** from all Movies and TV Shows in your Plex Media Server.

## ✅ Features

- Supports both `Movies` and `TV Shows` libraries
- Dry-run mode to preview changes
- Optional logging to a file
- Simple to configure and run

## ⚙️ Requirements

- Python 3.x
- `plexapi` library

## 💻 Installation

```bash
pip install plexapi
```

## 🔑 How to Get Your Plex Token
 Way 1
1. Open [https://app.plex.tv](https://app.plex.tv)
2. Open Developer Tools > Network tab
3. Filter for `X-Plex-Token` in network requests
4. Copy your token from a request

 Way 2
1. Open [https://app.plex.tv](https://app.plex.tv)
2. Go to an Episode or Movie
3. Click 3 dots
4. Choose Get Info
5. Click View XML
6. This will open in a new tab the Plex token will be at the end of the url

## 🛠️ Configuration

Edit the script:

```python
PLEX_URL = 'http://localhost:32400'       # Plex server address
PLEX_TOKEN = 'YOUR_PLEX_TOKEN_HERE'       # Your Plex token
DRY_RUN = True                             # True = preview only
ENABLE_LOG = True                          # True = enable logging
```

## ▶️ Usage

Run the script:

```bash
python remove_plex_labels.py
```

- Start with `DRY_RUN = True` to simulate changes.
- Change to `DRY_RUN = False` to apply changes.

## 📄 Logging

If enabled, actions are logged to `label_removal.log`.

## ❗ Disclaimer

Always use dry-run mode first. Make backups if needed.
