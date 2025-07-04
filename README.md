# 📦 Plex Label Remover

A pair of Python scripts to clean up and remove labels from your Plex libraries.

---

## ✅ Features (both versions)

- Supports Movies and TV Shows libraries
- Supports removing labels from individual items and collections
- Dry-run mode to preview changes before applying
- Optional logging to a file
- Simple to configure and use

---

## 🔁 Script Comparison

### 🧩 `remove_plex_labels.py`
> Basic version – quick and effective for cleaning all labels

- Removes **all labels** from every item and collection
- Logs what labels were removed
- Best for **blanket removal** of all metadata tags

### 🧠 `remove_plex_labels_v2.py`
> Enhanced version – smarter, safer, and more informative

- Removes labels from items and collections
- **Auto-detects or uses a preset list of leftover labels**
- **Scans for any labels still present afterward**
- Adds **post-run guidance**:
  - Check managed user restrictions
  - Optimize Plex database
- Best for **thorough cleanup and audit**

---

## ⚙️ Requirements

- Python 3.x
- [`plexapi`](https://pypi.org/project/plexapi/)

```bash
pip install plexapi
```

---

## 🔑 How to Get Your Plex Token

### Method 1

1. Visit: [https://app.plex.tv](https://app.plex.tv)
2. Open Dev Tools → Network tab
3. Filter by `X-Plex-Token`
4. Copy the token from one of the requests

### Method 2

1. Visit: [https://app.plex.tv](https://app.plex.tv)
2. Click into a Movie or Episode → 3-dot menu → Get Info → View XML
3. Token is in the URL (e.g. `&X-Plex-Token=XYZ`)

---

## 🛠️ Configuration

Open either script and update these variables:

```python
PLEX_URL = 'http://localhost:32400'       # Plex server address
PLEX_TOKEN = 'YOUR_PLEX_TOKEN_HERE'       # Your Plex token
DRY_RUN = True                             # True = preview only
ENABLE_LOG = True                          # True = enable logging
```

### Optional (v2 only):

```python
LEFTOVER_LABELS = []  # Leave empty to auto-detect or define manually
```

---

## ▶️ Usage

Run either script:

```bash
python remove_plex_labels.py
# or
python remove_plex_labels_v2.py
```

Start with `DRY_RUN = True` to simulate changes.  
Switch to `False` once you’re confident it’s safe.

---

## 📄 Logging

If `ENABLE_LOG = True`, all actions are recorded in:

```bash
label_removal.log
```

---

## ❗ Disclaimer

Always test with `DRY_RUN = True` first.  
Review logs carefully.  
Consider backing up your Plex database before running full removal.
