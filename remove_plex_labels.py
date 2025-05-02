from plexapi.server import PlexServer

# === Configuration Section ===
PLEX_URL = 'http://localhost:32400'  # URL of your Plex server (use IP if not local)
PLEX_TOKEN = 'YOUR_PLEX_TOKEN_HERE'  # Your Plex token from browser developer tools
DRY_RUN = True  # Set to False to actually remove labels; True = simulate only

def remove_all_labels(library_name):
    """
    Connects to the specified library and removes all labels from each item.
    In dry-run mode, it only prints what it would do.
    """
    # Connect to Plex
    plex = PlexServer(PLEX_URL, PLEX_TOKEN)
    
    # Access the specific library (Movies or TV Shows)
    library = plex.library.section(library_name)
    print(f"\n--- Processing library: {library_name} ---")

    # Loop through every item in the library
    for item in library.all():
        if item.labels:
            # Collect the current labels
            label_list = [label.tag for label in item.labels]
            print(f"{'[DRY RUN]' if DRY_RUN else '[REMOVE]'} {item.title} - Labels: {label_list}")
            
            # If not a dry run, remove all labels
            if not DRY_RUN:
                for label in label_list:
                    item.removeLabel(label)
                item.reload()  # Reload the item to reflect changes
        else:
            print(f"[SKIP] {item.title} has no labels.")  # Nothing to remove

def main():
    """
    Main function that processes both the Movies and TV Shows libraries.
    """
    for library in ['Movies', 'TV Shows']:  # Modify if your library names differ
        try:
            remove_all_labels(library)
        except Exception as e:
            print(f"[ERROR] Failed to process {library}: {e}")

# === Entry Point ===
if __name__ == "__main__":
    main()
