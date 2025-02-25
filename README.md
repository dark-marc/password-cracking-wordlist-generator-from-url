# Wordlist Generator from URL

A Python script that scrapes a website, extracts text, filters out stop words, and generates a wordlist sorted by frequency. The final wordlist is saved as "wordlist.txt" in a user-specified directory.

![Script](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcG5lbWdmN3o2YzU1a2Z5Z3JldzZ6b2ZoY3lnM3A0dzY2cmtnYWR6bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IX3ADEa37v9aHvPeFX/giphy.gif)


## Prerequisites

- **Python:** Download and install the latest version from https://www.python.org/downloads/.
- **Beautiful Soup and Requests:** These are external packages used for parsing HTML and making HTTP requests.

## Setup Instructions

1. **Clone or Download the Repository**  
   Clone this repository or download the source code to your local machine.

2. **Create a Virtual Environment**  
   Navigate to the project folder in your terminal or command prompt, then run:
   ```
   python -m venv venv
   ```

4. **Activate the virtual environment:** 
- On Windows:  
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:  
  ```
  source venv/bin/activate
  ```

4. **Install Dependencies**  
Ensure you have a `requirements.txt` file with the following content:

5. **Install dependencies by running:**
  ```
  pip install -r requirements.txt
  ```

## How the Script Works

- **User Input:**  
  When the script starts, it presents an interactive admin panel that prompts you for:
  - **Target URL:** The website you want to scrape. The script automatically corrects the URL by adding "http://" or "https://" if necessary.
  - **Stop Words:** A list of common words to ignore. You can use a default list or provide your own custom, comma-separated list.
  - **Page Limit:** The number of pages to scan. You can enter a specific number or type "all" to process every linked page.
  - **Save Options:**  
    - Confirm whether to save the results as a text file.
    - Specify how many of the top words to include in the output.
    - Enter the directory where the file "wordlist.txt" should be saved.

- **Data Processing:**  
  The script then proceeds through these steps:
  - **Link Collection:** It scrapes the target URL to collect all internal links on the site.
  - **Content Extraction:** It visits each collected page and extracts all text and numbers.  
    - **Phone Number Extraction:**  
      The script uses a regular expression to identify phone numbers (with or without country codes). It captures the complete phone number and also extracts parts of the number (such as the area code, prefix, and line number). This is useful because these individual components are often used as password variants in cracking tools.
  - **Filtering:** It removes words that match the stop words (either the default set or your custom list).
  - **Counting:** It counts the frequency of each remaining word using a counter and sorts the words from most to least frequent.

- **Output:**  
  Finally, the script:
  - Saves the complete, sorted wordlist as "wordlist.txt" in the specified directory, with each word on its own line.
  - Displays a summary of the analysis in the terminal by printing the top 10 most frequent words along with their counts in JSON format.

## Running the Script

Execute the script with:
  ```
  python wordlist-generator.py
  ```

Follow the on-screen prompts to generate your wordlist.

## Ethical Use:

This script is intended for ethical security testing and research. Use it only on websites where you have permission to test or as part of an authorized security audit. Its purpose is to help identify weak password choices and improve security—not for illegal access.

## License

This project is open-source and may be used or modified freely. 

Credit must be given to **DARK MARC** (https://darkmarc.substack.com/) for the original work.

Enjoy!
