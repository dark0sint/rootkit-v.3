from app.auth import Auth
from app.data import Data
from app.utils import input_int

def main():
    auth = Auth()
    data = Data()

    print("=== SimpleRootkit v3 - Simulasi Backend Mobile App ===")

    while True:
        if not auth.is_authenticated():
            print("\nSilakan login terlebih dahulu.")
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if auth.login(username, password):
                print(f"Login berhasil. Selamat datang, {username}!")
            else:
                print("Login gagal. Username atau password salah.")
                continue

        print("\nMenu Utama:")
        print("1. Lihat Profil")
        print("2. Lihat Daftar Berita")
        print("3. Logout")
        print("4. Keluar")

        choice = input_int("Pilih opsi: ", 1, 4)

        if choice == 1:
            user = auth.get_current_user()
            info = data.get_user_info(user)
            if info:
                print(f"\nProfil User: {user}")
                print(f"Role : {info['role']}")
                print(f"Email: {info['email']}")
            else:
                print("Data user tidak ditemukan.")
        elif choice == 2:
            news_list = data.list_news()
            print("\nDaftar Berita:")
            for item in news_list:
                print(f"{item['id']}. {item['title']}")
            news_id = input_int("Masukkan ID berita untuk baca detail (0 untuk kembali): ", 0)
            if news_id == 0:
                continue
            news_item = data.get_news_by_id(news_id)
            if news_item:
                print(f"\n{news_item['title']}\n{'-'*len(news_item['title'])}\n{news_item['content']}")
            else:
                print("Berita tidak ditemukan.")
        elif choice == 3:
            auth.logout()
            print("Anda telah logout.")
        elif choice == 4:
            print("Terima kasih telah menggunakan SimpleRootkit v3. Sampai jumpa!")
            break

if __name__ == "__main__":
    main()
