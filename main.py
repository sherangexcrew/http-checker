import requests
from colorama import Fore, init
import os

# Inisialisasi colorama
init(autoreset=True)

def clear_terminal():
    # Membersihkan terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = r"""
███████╗██╗  ██╗███████╗██████╗  █████╗ ███╗   ██╗ ██████╗
██╔════╝██║  ██║██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔════╝
███████╗███████║█████╗  ██████╔╝███████║██╔██╗ ██║██║  ███╗
╚════██║██╔══██║██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║██║   ██║
███████║██║  ██║███████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝
╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝
    """
    print(Fore.GREEN + banner)

    # Tampilkan teks di tengah terminal
    terminal_width = os.get_terminal_size().columns
    text = "SHerang Exploiter Crew"
    centered_text = text.center(terminal_width)
    print(Fore.GREEN + centered_text)

    # Informasi tambahan dengan subjudul berwarna hijau dan isi berwarna putih
    print(Fore.GREEN + "Admin  :", end=' ')
    print(Fore.WHITE + "03xploit")
    print(Fore.GREEN + "Tools  :", end=' ')
    print(Fore.WHITE + "Http Checker")
    print(Fore.GREEN + "Github :", end=' ')
    print(Fore.WHITE + "github.com/sherangxcrew")
    print(Fore.GREEN + "Website:", end=' ')
    print(Fore.WHITE + "https://sherangxcrew.com")
    print("")
    print(Fore.LIGHTBLUE_EX + "Ketik exit untuk keluar")

def check_http_response(url):
    # Menambahkan http:// jika URL tidak memiliki prefix
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        response = requests.get(url, timeout=6)  # Set timeout to 15 seconds
        return response.status_code
    except requests.exceptions.Timeout:
        return "Tidak ada respons"  # Return message for timeout
    except requests.exceptions.ConnectionError:
        return "Domain not registered / disable"
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}")
        return None

def print_response(url, status_code, good_output_file):
    result = ""
    if status_code == 200:
        result = f"{Fore.GREEN}[+] {url} > 200 OK\n"
        good_output_file.write(url + "\n")  # Save only the URL with 200 OK
    elif status_code == 400:
        result = f"{Fore.YELLOW}[+] {url} > 400 Bad Request\n"
    elif status_code == 401:
        result = f"{Fore.LIGHTRED_EX}[+] {url} > 401 Not Authorized\n"
    elif status_code == 403:
        result = f"{Fore.RED}[+] {url} > 403 Forbidden\n"
    elif status_code == 404:
        result = f"{Fore.LIGHTRED_EX}[+] {url} > 404 Not Found\n"
    elif status_code == 503:
        result = f"{Fore.CYAN}[+] {url} > 503 Service Unavailable\n"
    elif status_code == "Tidak ada respons":
        result = f"{Fore.LIGHTRED_EX}[+] {url} > Not responding..\n"
    elif status_code == "Name or service not known":
        result = f"{Fore.LIGHTBLUE_EX}[+] {url} > Name or service not known\n"
    else:
        result = f"{Fore.WHITE}[+] {url} > {status_code} Bad status \n"

    print(result, end='')  # Print to console

def main():
    clear_terminal()  # Membersihkan terminal sebelum menampilkan banner
    print_banner()  # Menampilkan banner di awal

    while True:
        try:
            filename = input("Masukkan nama file: ")
            print("_________________________________________________________")

            if filename.lower() == 'exit':
                print(f"{Fore.YELLOW}Keluar dari tools.")                                                                                            break

            good_output_filename = f"good_{os.path.basename(filename)}"  # Nama file untuk hasil 200 OK
            with open(filename, 'r') as file, open(good_output_filename, 'w') as good_output_file:
                urls = file.readlines()

                for url in urls:
                    url = url.strip()  # Menghapus spasi di awal dan akhir
                    if url:  # Pastikan URL tidak kosong
                        status_code = check_http_response(url)
                        if status_code is not None:
                            print_response(url, status_code, good_output_file)

            print(f"{Fore.YELLOW}Hasil 200 OK telah disimpan di {good_output_filename}")
            break  # Keluar dari loop jika berhasil membaca file

        except FileNotFoundError:
            print(f"{Fore.RED}File tidak ditemukan: {filename}. Silakan coba lagi.")
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Keluar dari tools.")
            break
        except Exception as e:
            print(f"{Fore.RED}Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()

