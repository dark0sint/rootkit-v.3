# app/data.py

class Data:
    def __init__(self):
        self.users_data = {
            "admin": {"role": "administrator", "email": "admin@polri.go.id"},
            "user1": {"role": "member", "email": "user1@example.com"}
        }
        self.news = [
            {"id": 1, "title": "Operasi Patuh 2025 Dimulai", "content": "Polri mulai operasi patuh untuk menekan pelanggaran lalu lintas."},
            {"id": 2, "title": "Kapolri Berikan Penghargaan", "content": "Kapolri memberikan penghargaan kepada personel berprestasi."},
            {"id": 3, "title": "Sosialisasi Program Presisi", "content": "Program Presisi disosialisasikan ke masyarakat luas."}
        ]

    def get_user_info(self, username):
        return self.users_data.get(username, None)

    def list_news(self):
        return self.news

    def get_news_by_id(self, news_id):
        for item in self.news:
            if item["id"] == news_id:
                return item
        return None
