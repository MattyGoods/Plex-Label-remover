from plexapi.server import PlexServer
import datetime

# === Configuration ===
PLEX_URL = 'http://localhost:32400'      # Your Plex server URL or IP
PLEX_TOKEN = 'YOUR_PLEX_TOKEN_HERE'      # Your Plex authentication token
DRY_RUN = False                          # If True, simulate removals
ENABLE_LOG = True                        # Enable logging output
LOG_FILE = "label_removal.log"           # Log file path

# Leave empty to auto-detect all existing labels, or specify a list manually
LEFTOVER_LABELS = []


def log(message):
    """Log messages to the console and optionally to a log file."""
    print(message)
    if ENABLE_LOG:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.datetime.now()} - {message}\n")


def remove_labels_from_items(library):
    """Remove all labels from items in the specified library."""
    for item in library.all():
        item.reload()
        current_labels = [label.tag for label in item.labels]

        if current_labels:
            log(f"{'[DRY RUN]' if DRY_RUN else '[REMOVE]'} {item.title} - Labels: {current_labels}")
            if not DRY_RUN:
                for label in current_labels:
                    try:
                        item.removeLabel(label)
                    except Exception as e:
                        log(f"[WARNING] Couldn't remove label '{label}' from {item.title}: {e}")
                item.reload()
                remaining = [label.tag for label in item.labels]
                if remaining:
                    log(f"[WARNING] {item.title} still has labels: {remaining}")
        else:
            log(f"[SKIP] {item.title} has no labels.")


def remove_labels_from_collections(library):
    """Remove all labels from collections in the specified library."""
    collections = library.collections()
    log(f"Found {len(collections)} collections in {library.title}")

    for collection in collections:
        current_labels = [label.tag for label in collection.labels]

        if current_labels:
            log(f"{'[DRY RUN]' if DRY_RUN else '[REMOVE]'} [Collection] {collection.title} - Labels: {current_labels}")
            if not DRY_RUN:
                for label in current_labels:
                    try:
                        collection.removeLabel(label)
                    except Exception as e:
                        log(f"[WARNING] Couldn't remove label '{label}' from collection {collection.title}: {e}")
                collection.reload()
                remaining = [label.tag for label in collection.labels]
                if remaining:
                    log(f"[WARNING] Collection {collection.title} still has labels: {remaining}")
        else:
            log(f"[SKIP] Collection {collection.title} has no labels.")


def scan_for_leftover_labels(library):
    """Scan the library for any remaining items with specific leftover labels."""
    log("\n--- Scanning for leftover labels ---")

    # If LEFTOVER_LABELS is empty, auto-detect all labels in use
    detected = set()
    for item in library.all():
        for label in item.labels:
            detected.add(label.tag)
    for collection in library.collections():
        for label in collection.labels:
            detected.add(label.tag)

    global LEFTOVER_LABELS
    if not LEFTOVER_LABELS:
        LEFTOVER_LABELS = sorted(detected)

    # Search the library for each label
    for label in LEFTOVER_LABELS:
        results = library.search(label=label)
        if results:
            log(f"[FOUND] Label '{label}' still present on:")
            for item in results:
                log(f" - {item.title}")
        else:
            log(f"[OK] Label '{label}' not found on any items.")


def process_library(library_name):
    """Connect to Plex and process a single library for label removal and verification."""
    plex = PlexServer(PLEX_URL, PLEX_TOKEN)
    library = plex.library.section(library_name)
    log(f"\n=== Processing library: {library_name} ===")

    remove_labels_from_items(library)
    remove_labels_from_collections(library)
    scan_for_leftover_labels(library)

    log("\n[INFO] To fully remove label traces:")
    log(" - Make sure labels are not used in user restrictions (check each managed user)")
    log(" - Go to Plex Settings > Manage > Troubleshooting > Optimize database")


def main():
    """Main entry point to process all specified libraries."""
    if ENABLE_LOG:
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            f.write("=== Plex Label Removal Log ===\n")

    for lib in ['Movies', 'TV Shows']:
        try:
            process_library(lib)
        except Exception as e:
            log(f"[ERROR] Failed to process {lib}: {e}")


if __name__ == "__main__":
    main()
