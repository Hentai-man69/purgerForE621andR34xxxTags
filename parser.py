import os

# Input folder containing files with tags
input_folder = "input/"

# Output folder to save tag files
output_folder = "output/"

# Loop through files in input folder
for filename in os.listdir(input_folder):
    if "!tags" in filename:
        # Found a file with tags, read the lines and create output files
        with open(input_folder + filename, encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                # Extract filename and tags
                file_name, tag_line = line.split(": ", 1)
                tags = tag_line.split()[1:]

                # Remove underscores from tags and join with commas and spaces
                tags_str = ", ".join(tags)

                # Write tags to output file
                output_filename = file_name + ".txt"
                with open(output_folder + output_filename, "w", encoding="utf-8") as out_file:
                    out_file.write(tags_str)
