import urllib.parse
import os

# ANSI escape sequence untuk warna merah
RED = '\033[91m'
RESET = '\033[0m'  # Reset untuk mengembalikan warna ke default

def url_decoder(encoded_url):
    return urllib.parse.unquote(encoded_url)

def remove_prefix(decoded_url, prefix):
    if decoded_url.startswith(prefix):
        decoded_url = decoded_url[len(prefix):]
    return decoded_url

def display_file_content():
    try:
        with open("HASILNYA-SIR.txt", "r") as file:
            content = file.read()
            print("\nContents of HASILNYA-SIR.txt:\n")
            print(content)
    except FileNotFoundError:
        print("HASILNYA-SIR.txt does not exist yet.")

def main():
    print("URL Decoder")
    print("=====================")
    
    # Check if HASILNYA-SIR.txt exists
    if not os.path.isfile("HASILNYA-SIR.txt"):
        print("Error: 'HASILNYA-SIR.txt' does not exist. Please create the file and try again.")
        return
    
    while True:
        print("Menu:")
        print("1. Decode URLs")
        print("2. Remove prefix from decoded URLs")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                encoded_url = input("Enter the encoded URL (or type 'done' to finish): ")
                if encoded_url.lower() == 'done':
                    break
                decoded_url = url_decoder(encoded_url)
                
                # Tambahkan teks sebelum dan sesudah write ke file
                with open("HASILNYA-SIR.txt", "a") as file:
                    file.write("==============HASILNYA SIR================\n")
                    file.write(f"{decoded_url}\n")
                    file.write("==============HASILNYA SIR================\n")
                
                print("Decoded URL has been saved to HASILNYA-SIR.txt")
        elif choice == '2':
            prefix = input("Enter the prefix to remove (leave blank to skip): ").strip()
            if prefix:
                with open("HASILNYA-SIR.txt", "r") as file:
                    lines = file.readlines()
                with open("HASILNYA-SIR.txt", "w") as file:
                    for line in lines:
                        file.write(remove_prefix(line, prefix))
                print(f"The prefix '{prefix}' was successfully removed.")
            else:
                print("Skipping prefix removal.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
