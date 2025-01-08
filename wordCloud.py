import os
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Set the base directory where your PDFs are stored
base_dir = "."  # Replace with your actual path

# Count the number of PDF files in each subfolder
folder_counts = Counter()

# Traverse the directory and count PDFs
for root, _, files in os.walk(base_dir):
    pdf_count = sum(1 for file in files if file.lower().endswith('.pdf'))
    if pdf_count > 0:
        folder_name = os.path.basename(root)
        folder_counts[folder_name] += pdf_count

# Check if any PDFs were found
if folder_counts:
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(folder_counts)

    # Display the word cloud
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Categories")
    plt.show()
else:
    print("No PDFs found in the specified directory.")
