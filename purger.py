import os

# Define the folder to scan
folder_path = "output"

# Load the blacklist words from file
blacklist_file = open("blacklist.txt", "r")
blacklist_words = []
for line in blacklist_file.readlines():
    line = line.strip()
    # Check if the line is empty or a comment
    if not line or line.startswith("#"):
        continue
    for word in line.split(","):
        # Add the entire line as the reason
        blacklist_words.append((word.strip(), line.strip()))
blacklist_file.close()

# Loop over all files in the folder
for file_name in os.listdir(folder_path):
    # Check if it's a text file
    if file_name.endswith(".txt"):
        # Load the contents of the file
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r") as text_file:
            file_contents = text_file.read()

        # Extract tags from the file name
        file_tags = [tag.strip() for tag in os.path.splitext(file_name)[0].split(",")]

        # Check if any of the blacklist words are in the file or tags
        should_delete = False
        for word, reason in blacklist_words:
            if word.startswith("-"):
                # Ignore blacklist words that start with a dash
                if any(file_contents.find(w.strip()) != -1 for w in word[1:].split(",")):
                    should_delete = False
                    break
                if any(tag == w.strip() for tag in file_tags for w in word[1:].split(",")):
                    should_delete = False
                    break
            else:
                # Check if the word is in the file contents or tags
                if any(file_contents.find(w.strip()) != -1 for w in word.split(",")):
                    # Check if there is an exclusion for this specific word
                    exclusion = "-" + word
                    if exclusion in [w for w,_ in blacklist_words]:
                        should_delete = False
                        break
                    else:
                        should_delete = True
                        reason_str = reason
                if any(tag == w.strip() for tag in file_tags for w in word.split(",")):
                    # Check if there is an exclusion for this specific word
                    exclusion = "-" + word
                    if exclusion in [w for w,_ in blacklist_words]:
                        should_delete = False
                        break
                    else:
                        should_delete = True
                        reason_str = reason

        # If any blacklist words were found, delete all files with the same base name
        if should_delete:
            file_base_name = os.path.splitext(file_name)[0]
            for file_to_delete in os.listdir(folder_path):
                if file_to_delete.startswith(file_base_name):
                    # Remove the file and log the deletion with the reason
                    os.remove(os.path.join(folder_path, file_to_delete))
                    with open("logDelete.txt", "a") as log_file:
                        log_file.write(f"Filename:\"{file_to_delete}\" Reason:\"{reason_str}\"\n")
        else:
            # Log the file that was kept
            with open("logKept.txt", "a") as log_file:
                log_file.write(f"Filename:\"{file_name}\" Reason:\"{None}\"\n")
