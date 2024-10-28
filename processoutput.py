def read_summary_from_file(filename):
    """
    Reads the summary data from a text file and returns a list.

    Args:
        filename (str): The name of the text file.

    Returns:
        list: A list containing the summary data (code issues, high issues).
    """

    with open(filename, 'r') as f:
        lines = f.readlines()

        # Find the index of the line starting with "Summary:"
        summary_index = lines.index("Summary:\n")

        # Extract summary data from the following lines
        summary_data = []
        for line in lines[summary_index+1:]:
            if line.strip():  # Skip empty lines
                summary_data.append(line.strip())

    return summary_data

# Example usage
filename = "output_file.txt"  # Replace with your actual filename
summary_data = read_summary_from_file(filename)

print(summary_data)
