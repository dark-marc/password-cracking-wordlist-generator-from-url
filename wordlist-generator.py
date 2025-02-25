import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import Counter
import base64
import re
import json
import os

def print_byline():
    signature = r"CkBAQEBAQEBAQCUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSVAQEBAQEBAQEAKQEBAQEBAJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJUBAQEBAQApAQEBAQCUlJSUlIyMqKioqIyMjIyUlJSUlJSUlJSUlJSUlJSUlJSMjIyMqKioqIyMlJSUlJUBAQEBACkBAQEAlJSUlJTouICAgICAuLisqIyMjJSUlJSUlJSUlJSUlIyMjKisuLiAgICAgLjolJSUlJUBAQEAKQEBAJSUlJSUqICAgICAgICAgIC0qIyMjJSUlJSUlJSUlJSMjIyotICAgICAgICAgIColJSUlJUBAQApAQCUlJSUlIysgICAgICAgICAgLj0qIyMjIyUlJSUlJSMjIyMqPS4gICAgICAgICAgKyMlJSUlJUBACkBAJSUlJSUjKyAgICAgICAgICAgLj0qIyMjIyMlJSMjIyMjKj0uICAgICAgICAgICArIyUlJSUlQEAKQEAlJSUlJSMrICAgICAgICAgICAgLj0qIyMjIyMjIyMjIyo9LiAgICAgICAgICAgICsjJSUlJSVAQApAQCUlJSUlIysgICAgICAgICAgICAgLisqIyMjIyMjIyMqKy4gICAgICAgICAgICAgKyMlJSUlJUBACkBAJSUlJSUjKyAgICAgICAgICAgICAgLisqIyMjIyMqKisuICAgICAgICAgICAgICArIyUlJSUlQEAKQEAlJSUlJSMrICAgICAgICAgICAgICAuOisqKioqKiorOi4gICAgICAgICAgICAgICsjJSUlJSVAQApAQCUlJSUlIysgICAgICAgLi4uLiAgICAgOisqKioqKzogICAgIC4uLi4gICAgICAgKyMlJSUlJUBACkBAJSUlJSUjKyAgICAgLi0rKioqOiAgICAgLi0rKy0uICAgICA6KioqKy0uICAgICArIyUlJSUlJUAKQEAlJSUlJSMrICAgICAtKyoqKioqPS4gICAgICAgICAgICAuLSoqKioqKy0gICAgICsjJSUlJSVAQApAQCUlJSUlIysgICAgIC0rKiMjIyMqLSAgICAgICAgICAgIC0qIyMjIyorLSAgICAgKyMlJSUlJUBACkBAQCUlJSUjKyAgICAuLSsqIyMjIyMqLSAgICAgICAgICAtKiMjIyMjKistICAgICArIyUlJSVAQEAKQEBAJSUlJSMrICAgIC4tKyMjIyMjIyMqLS4gICAgICAgLSojIyMjIyMqKy0gICAgICsjJSUlJUBAQApAQEAlJSUlIysgICAgLi0rIyMjIyUjIyMqOiAgICAgIDoqIyMjJSMjIyorLSAgICAgKyMlJSVAQEBACkBAQEAlJSUjKyAgICAuOisjIyMlJSUlIyMjLS4gIC4tIyMjJSUlJSMjIys6ICAgICArJSUlJUBAQEAKQEBAQCUlJSUqICAgIC46KyMjJSUlJSUlJSMjKzotKiMjJSUlJSUlJSMjKzouICAgIColJSUlQEBAQApAQEBAQCUlJSMuICAgLisjJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSMjPS4gICAuIyUlJUBAQEBACkBAQEBAQCUlJSUtLj0jJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlIz0uLSUlJSVAQEBAQEAKQEBAQEBAQEAlJSUlJSUlJSUlJUBAQEBAQEBAQEBAQEBAQEBAQEBAJSUlJSUlJSUlJSVAQEBAQEBAQApAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBACkBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEAKICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgIPCdlY7wnZWg8J2Vo/CdlZUg8J2Vg/CdlZrwnZWk8J2VpSDwnZS+8J2VlvCdlZ/wnZWW8J2Vo/CdlZLwnZWl8J2VoPCdlaMg8J2Vk/Cdlaog8J2Uu/CdlZLwnZWj8J2VnCDwnZWE8J2VkvCdlaPwnZWUIAoKICAgICAgICAgICAgICAgIPCdlY3wnZWa8J2VpPCdlZrwnZWlIPCdlLvwnZWS8J2Vo/CdlZzwnZWE8J2VkvCdlaPwnZWULvCdlYrwnZWm8J2Vk/CdlaTwnZWl8J2VkvCdlZTwnZWcLvCdlZTwnZWg8J2Vngo=" 
    decrypted = base64.b64decode(signature.encode('utf-8')).decode('utf-8')
    print(decrypted)

def get_internal_links(url):
    """Get all internal links from the given URL, excluding fragment identifiers."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        base_domain = urlparse(url).netloc

        internal_links = set()
        for a_tag in soup.find_all('a', href=True):
            link = urljoin(url, a_tag['href'])
            parsed_link = urlparse(link)

            if parsed_link.netloc == base_domain and not parsed_link.fragment:
                internal_links.add(parsed_link._replace(fragment='').geturl())

        return list(internal_links)

    except requests.RequestException as e:
        print(f"Error getting internal links: {e}")
        return []


def get_text_with_numbers_and_phone_parts(url):
    """Extract words, numbers, and phone number parts from the given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)

        tokens = re.findall(r'\b\w+\b', text.lower())

        # Extract phone numbers (with or without country code)
        phone_pattern = r'\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        phone_numbers = re.findall(phone_pattern, text)

        for number in phone_numbers:
            clean_number = re.sub(r'\D', '', number)
            clean_number_without_cc = clean_number[-10:] if len(clean_number) > 10 else clean_number

            # Full number with country code
            tokens.append(clean_number)

            # Number without country code
            if len(clean_number) > 10:
                tokens.append(clean_number_without_cc)

            # Break into parts (without country code)
            tokens.extend([clean_number_without_cc[:3], clean_number_without_cc[3:6], clean_number_without_cc[6:]])

        return tokens

    except requests.RequestException as e:
        print(f"Error extracting text: {e}")
        return []


def filter_garbage_words(word_list, stop_words):
    """Remove user-defined or default stop words from the word list."""
    return [word for word in word_list if word not in stop_words]

def save_to_txt(data, save_directory, top_x=None):
    """Save the word count data to a TXT file, one word per line."""
    try:
        if top_x:
            data = data[:top_x]  # Save only top X words

        file_path = os.path.join(save_directory, 'wordlist.txt')
        with open(file_path, mode='w', encoding='utf-8') as file:
            for item in data:
                file.write(f"{item['word']}\n")
        print(f"\nResults saved to: {file_path}\n")
    except Exception as e:
        print(f"\nError saving to TXT: {e}\n")

def get_user_input(prompt, valid_options=None, allow_blank=False):
    """Get validated user input. Re-prompt if input is invalid."""
    while True:
        user_input = input(prompt).strip()
        if allow_blank and user_input == '':
            return user_input
        if valid_options and user_input.lower() not in valid_options:
            print("Invalid input. Please try again.")
            continue
        return user_input

def get_positive_integer_input(prompt, allow_all=False, allow_blank=False):
    """Get a positive integer input or 'all' if allowed."""
    while True:
        user_input = input(prompt).strip().lower()
        if allow_blank and user_input == '':
            return None
        if allow_all and user_input == 'all':
            return user_input
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Invalid input. Please enter a positive number or 'all'.")


def build_word_count_json(base_url, stop_words, max_pages, save_txt, save_path, top_x):
    """Main function to build a JSON object of words sorted by frequency from the entire site."""
    internal_links = get_internal_links(base_url)
    # Ensure unique links using a set, but keep base_url at the beginning
    internal_links_set = set(internal_links)
    internal_links = [base_url] + [link for link in internal_links_set if link != base_url]

    if max_pages != 'all':
        internal_links = internal_links[:int(max_pages)]

    print(f"\nTotal Internal Links to Process: {len(internal_links)}\n")

    master_list = []
    for url in internal_links:
        print(f"Processing: {url}")
        words = get_text_with_numbers_and_phone_parts(url)
        master_list.extend(words)

    master_list = filter_garbage_words(master_list, stop_words)
    word_counts = Counter(master_list)
    word_count_json = [{"word": word, "count": count} for word, count in word_counts.most_common()]

    if save_txt == 'y' and save_path:
        save_to_txt(word_count_json, save_path, top_x=top_x)

    return word_count_json

def admin_panel():
    """Interactive admin panel to configure and run the script."""
    print("\n=== Admin Panel ===\n")

    # Base URL
    base_url = input("Enter the base URL to target: ").strip()

    if not base_url.startswith(("http://", "https://")):
        https_url = f"https://{base_url}"
        http_url = f"http://{base_url}"

        try:
            response = requests.get(https_url, timeout=5)
            response.raise_for_status()
            base_url = https_url
        except requests.RequestException:
            try:
                response = requests.get(http_url, timeout=5)
                response.raise_for_status()
                base_url = http_url
            except requests.RequestException:
                base_url = None

    # Default stop words list
    default_stop_words = {
        'a', 'an', 'and', 'are', 'as', 'at', 'by', 'for', 'from', 'in', 'is', 
        'it', 'of', 'on', 'or', 'our', 'out', 'that', 'the', 'this', 'to', 
        'we', 'with', 'your', 'you', 'us', 'my', 'who', 'what', 'why', 'how', 
        'do', 'does', 'did', 'have', 'has', 'had', 'be', 'been', 'if', 'then', 
        'there', 'their', 'them', 'they', 'here', 'now', 'no', 'yes', 'all', 
        'any', 'some', 'each', 'every', 'more', 'most', 'many', 'few', 
        'such', 'only', 'also', 'about', 'above', 'below', 'under', 'over', 
        'between', 'into', 'through', 'during', 'before', 'after', 'again', 
        'further', 'once', 'both', 'either', 'neither', 'not', 'nor', 'so', 
        'too', 'very', 'just', 'but', 'yet', 'still', 'although', 'because', 
        'since', 'until', 'those', 'use'
    }

    # Exclusion words
    stop_words_input = input("\nEnter exclusion words (comma separated, leave blank for default list): ").strip()
    
    if stop_words_input:
        stop_words = {word.strip().lower() for word in stop_words_input.split(',')}
    else:
        stop_words = default_stop_words

    # Max pages
    max_pages = get_positive_integer_input("\nHow many pages to scan? (Enter a number or type 'all'): ", allow_all=True)

    # Save to TXT
    
    save_txt = get_user_input("\nSave results as TXT? (y/n): ", valid_options=['y', 'n'])
    save_directory = None
    top_x = None

    if save_txt == 'y':
        # Number of top words to save
        while True:
            top_x_input = input("\nHow many top words to save? (Enter a number or type 'all'): ").strip().lower()
            if top_x_input == 'all':
                top_x = None  # Use None to save all words
                break
            elif top_x_input.isdigit() and int(top_x_input) > 0:
                top_x = int(top_x_input)
                break
            else:
                print("Invalid input. Please enter a positive number or type 'all'.")

        # Save directory
        save_directory = input("\nEnter the directory to save 'wordlist.txt' (press Enter to use current directory): ").strip()
        if not save_directory or not os.path.isdir(save_directory):
            if save_directory and not os.path.isdir(save_directory):
                print("Invalid directory. Using current directory instead.")
            save_directory = os.getcwd()

    result = build_word_count_json(base_url, stop_words, max_pages, save_txt, save_directory, top_x)

    # Print final results
    print("\nFinal Word Count (Top 10):")
    print(json.dumps(result[:10], indent=4))

if __name__ == "__main__":
    print_byline()
    admin_panel()
