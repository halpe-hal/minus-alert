from supabase import create_client

# ★ここに自分のSupabase情報を入れる
SUPABASE_URL = "https://svexgvaaeeszdtsbggnf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN2ZXhndmFhZWVzemR0c2JnZ25mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDU2NDkyMzcsImV4cCI6MjA2MTIyNTIzN30.JgR8PN33icGZ4kkGZ9x1AyqDij5n-otn3OklH6AL3Rk"

# Supabaseクライアントを作成
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# 接続できてるかテスト（minusテーブルからデータ取得してみる）
def fetch_minus_data():
    data = supabase.table("minus").select("*").execute()
    return data.data

if __name__ == "__main__":
    results = fetch_minus_data()
    print("取得したデータ:", results)
