import os
import time
from requestProxy import switch_tor_identity, fetch_using_proxy

def save_content_to_file(content, file_name, file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_full_path = os.path.join(file_path, file_name)
    with open(file_full_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"[INFO] Content saved to {file_full_path}")

def main():
    url = "https://www.freecodecamp.org/news/creating-a-directory-in-python-how-to-create-a-folder/"
    file_name = "news.html"
    file_path = "data"

    max_attempts = 3  # Maximum attempts to fetch the content

    for attempt in range(max_attempts):
        try:
            print(f"[INFO] Attempt {attempt + 1} to fetch content from {url} via TOR...")
            switch_tor_identity()  # Switch TOR identity
            time.sleep(5)  # Wait for the new identity to establish

            # Fetch the content
            content = fetch_using_proxy(url)
            print("[INFO] Content fetched successfully.")

            # Save the content to a file
            save_content_to_file(content, file_name, file_path)
            
            # Exit the loop after successful execution
            print("[INFO] Successfully fetched and saved the content. Exiting...")
            break
        except Exception as e:
            print(f"[ERROR] Attempt {attempt + 1} failed: {e}")
            if attempt == max_attempts - 1:
                print("[ERROR] Max attempts reached. Could not fetch the content.")
            else:
                print("[INFO] Retrying...")
                time.sleep(10)  # Wait before the next attempt

if __name__ == "__main__":
    main()
