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
SEARCH_KEYWORD = "AI活用 副業 事例"

# ★検索して情報を集めるサイトの数
NUM_SITES_TO_CHECK = 10

# ★生成されるHTMLファイル名
OUTPUT_FILENAME = "副業AI活用まとめ.html"

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
        # duckduckgo_searchを使って検索を実行
        with DDGS() as ddgs:
            # ddgs.textはジェネレータを返すため、ループで回して結果を取得
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
        # サイトにアクセス
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # エラーがあればここで例外を発生させる
        response.encoding = response.apparent_encoding # 文字化け防止

        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(response.text, 'html.parser')

        # タイトルを取得
        title = soup.find('title').text if soup.find('title') else "タイトル不明"

        # 本文をpタグから抽出
        paragraphs = soup.find_all('p')
        content_text = ""
        for p in paragraphs:
            content_text += p.get_text().strip()
            if len(content_text) > MAX_TEXT_LENGTH:
                break
            
        # 抽出した本文が短すぎる場合は、body全体からテキストを抽出してみる
        if len(content_text) < 50:
            content_text = ' '.join(soup.body.get_text().split())

        # 最終的な本文を適切な長さにカット
        summary = content_text[:MAX_TEXT_LENGTH] + "..." if len(content_text) > MAX_TEXT_LENGTH else content_text
        
        if not summary:
            return None # 有効なコンテンツがなければNoneを返す

        return {'title': title.strip(), 'summary': summary.strip(), 'url': url}

    except Exception as e:
        print(f"  (エラー: {url} の処理をスキップします - {e})")
        return None

def create_html(keyword, site_data_list):
    """抽出したデータからHTMLを生成する"""
    print("HTMLファイルを生成しています...")
    
    # 各サイトの情報をカード形式でHTMLに変換
    cards_html = ""
    for data in site_data_list:
        cards_html += f"""
        <div class="card">
            <h2><a href="{data['url']}" target="_blank">{data['title']}</a></h2>
            <p>{data['summary']}</p>
            <a href="{data['url']}" target="_blank" class="source-link">続きを読む</a>
        </div>
        """

    # HTML全体のテンプレート
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
# --- メインの処理 ---
if __name__ == "__main__":
    # ①【調査】Web検索してURLリストを取得
    urls = search_web(SEARCH_KEYWORD, NUM_SITES_TO_CHECK)
    
    # ②【出力】各サイトから内容を抽出
    all_site_data = []
    if urls:
        for url in urls:
            content_data = scrape_content(url)
            if content_data:
                all_site_data.append(content_data)
            time.sleep(1) # サーバーに負荷をかけないための待機

    # ③・④【リスト化・サイト化】HTMLを生成してファイルに保存
    if all_site_data:
        final_html = create_html(SEARCH_KEYWORD, all_site_data)
        
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
            f.write(final_html)
        
        print("-" * 50)
        print(f"🎉 成功！ 「{OUTPUT_FILENAME}」が作成されました。")
        
        # 【追加部分】Seleniumで特定のブラウザを操作する
        print("デバッグ用Chromeに接続して、ページを開きます...")
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            import os

            # Chromeのオプションを設定
            chrome_options = Options()
            chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

            # Selenium WebDriverに接続
            driver = webdriver.Chrome(options=chrome_options)
            
            # HTMLファイルの絶対パスを取得して、URL形式に変換
            file_path = os.path.abspath(OUTPUT_FILENAME)
            file_url = 'file:///' + file_path.replace('\\', '/')

            # 接続したブラウザでURLを開く
            driver.get(file_url)
            print("ページを開きました！")

        except Exception as e:
            print(f"ブラウザの操作に失敗しました。デバッグ用Chromeが起動しているか確認してください。")
            print(f"エラー詳細: {e}")

        print("-" * 50)

    else:
        print("有効な情報を収集できませんでした。キーワードを変えて試してみてください。")