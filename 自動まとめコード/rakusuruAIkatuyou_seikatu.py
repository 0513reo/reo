# ----------------------------------------------------------------
# まとめサイト自動生成プログラム
# ----------------------------------------------------------------

# 1. 必要なライブラリを読み込む
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
import time

# ----------------------------------------------------------------
# 2. 設定項目（ここを自由に変更してください）
# ----------------------------------------------------------------

# ★検索したいキーワードを指定
SEARCH_KEYWORD = "生活が楽になる AI活用 家事"

# ★検索して情報を集めるサイトの数
NUM_SITES_TO_CHECK = 10

# ★生成されるHTMLファイル名
OUTPUT_FILENAME = "生活AI活用まとめ.html"

# ★各サイトから抽出する本文の最大文字数
MAX_TEXT_LENGTH = 150

# ----------------------------------------------------------------
# ここから下のコードは変更不要です
# ----------------------------------------------------------------

def search_web(keyword, max_results):
    """指定されたキーワードでWeb検索し、URLのリストを返す"""
    print(f"「{keyword}」でWeb検索を開始します...")
    results = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(keyword, region='jp-jp', max_results=max_results):
                results.append(r)
        print(f"{len(results)}件の検索結果を取得しました。")
        return [r['href'] for r in results]
    except Exception as e:
        print(f"検索中にエラーが発生しました: {e}")
        return []

def scrape_content(url):
    """指定されたURLからタイトルと本文の要点を抽出する"""
    print(f"-> {url} から情報を抽出中...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').text if soup.find('title') else "タイトル不明"
        paragraphs = soup.find_all('p')
        content_text = ""
        for p in paragraphs:
            content_text += p.get_text().strip()
            if len(content_text) > MAX_TEXT_LENGTH:
                break
        if len(content_text) < 50:
             content_text = ' '.join(soup.body.get_text().split())
        summary = content_text[:MAX_TEXT_LENGTH] + "..." if len(content_text) > MAX_TEXT_LENGTH else content_text
        if not summary:
            return None
        return {'title': title.strip(), 'summary': summary.strip(), 'url': url}
    except Exception as e:
        print(f"  (エラー: {url} の処理をスキップします - {e})")
        return None

def create_html(keyword, site_data_list):
    """抽出したデータからHTMLを生成する"""
    print("HTMLファイルを生成しています...")
    cards_html = ""
    for data in site_data_list:
        cards_html += f"""
        <div class="card">
            <h2><a href="{data['url']}" target="_blank">{data['title']}</a></h2>
            <p>{data['summary']}</p>
            <a href="{data['url']}" target="_blank" class="source-link">続きを読む</a>
        </div>
        """
    html_template = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{keyword} のまとめ</title>
    <style>
        body {{ font-family: 'Segoe UI', Meiryo, system-ui, sans-serif; background-color: #f4f7f6; color: #333; margin: 0; padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        header h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
        .card {{ background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 20px; padding: 20px; transition: transform 0.2s; }}
        .card:hover {{ transform: translateY(-5px); }}
        .card h2 {{ font-size: 1.4em; margin-top: 0; color: #3498db; }}
        .card h2 a {{ text-decoration: none; color: inherit; }}
        .card p {{ line-height: 1.7; }}
        .source-link {{ display: inline-block; margin-top: 10px; font-weight: bold; color: #3498db; text-decoration: none; }}
        footer {{ text-align: center; margin-top: 40px; color: #7f8c8d; font-size: 0.9em; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>「{keyword}」についての自動まとめ</h1>
        </header>
        <main>
            {cards_html}
        </main>
        <footer>
            <p>このページはPythonプログラムによって自動生成されました。</p>
        </footer>
    </div>
</body>
</html>
    """
    return html_template

# --- メインの処理 ---
if __name__ == "__main__":
    urls = search_web(SEARCH_KEYWORD, NUM_SITES_TO_CHECK)
    all_site_data = []
    if urls:
        for url in urls:
            content_data = scrape_content(url)
            if content_data:
                all_site_data.append(content_data)
            time.sleep(1)
    if all_site_data:
        final_html = create_html(SEARCH_KEYWORD, all_site_data)
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
            f.write(final_html)
        print("-" * 50)
        print(f"🎉 成功！ 「{OUTPUT_FILENAME}」が作成されました。")
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            import os
            print("デバッグ用Chromeに接続して、ページを開きます...")
            chrome_options = Options()
            chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            driver = webdriver.Chrome(options=chrome_options)
            file_path = os.path.abspath(OUTPUT_FILENAME)
            file_url = 'file:///' + file_path.replace('\\', '/')
            driver.get(file_url)
            print("ページを開きました！")
        except Exception as e:
            print(f"ブラウザの操作に失敗しました。デバッグ用Chromeが起動しているか確認してください。")
            print(f"エラー詳細: {e}")
        print("-" * 50)
    else:
        print("有効な情報を収集できませんでした。キーワードを変えて試してみてください。")