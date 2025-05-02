from plexapi.server import PlexServer
import datetime

# === Configuration ===
PLEX_URL = 'http://localhost:32400'       # Your Plex server URL or IP
PLEX_TOKEN = 'YOUR_PLEX_TOKEN_HERE'       # Your Plex token
DRY_RUN = True                             # True = simulate only, False = actually remove labels
ENABLE_LOG = True                          # True = save actions to log file

LOG_FILE = "label_removal.log"             # Log filename

def log(message):
    """
    Logs a message to the console and optionally to a log file.
    """
    print(message)
    if ENABLE_LOG:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.datetime.now()} - {message}\n")

def remove_all_labels(library_name):
    """
    Removes all labels from items in the specified library.
    """
    plex = PlexServer(PLEX_URL, PLEX_TOKEN)
    library = plex.library.section(library_name)
    log(f"\n--- Processing library: {library_name} ---")

    for item in library.all():
        if item.labels:
            label_list = [label.tag for label in item.labels]
            log(f"{'[DRY RUN]' if DRY_RUN else '[REMOVE]'} {item.title} - Labels: {label_list}")
            
            if not DRY_RUN:
                for label in label_list:
                    item.removeLabel(label)
                item.reload()
        else:
            log(f"[SKIP] {item.title} has no labels.")

def main():
    """
    Main entry point for the script.
    """
    # Clear old log file if logging is enabled
    if ENABLE_LOG:
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            f.write("=== Plex Label Removal Log ===\n")

    for library in ['Movies', 'TV Shows']:
        try:
            remove_all_labels(library)
        except Exception as e:
            log(f"[ERROR] Failed to process {library}: {e}")

if __name__ == "__main__":
    main()
