# ----------------------------------------------------------------
# まとめサイト自動生成プログラム【最終デザイン対応版】
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
SEARCH_KEYWORD = "明日　アポイント獲得　コツ"

# ★検索して情報を集めるサイトの数
NUM_SITES_TO_CHECK = 10

# ★生成されるHTMLファイル名（フォルダの中に作るように設定済み！）
OUTPUT_FILENAME = "matome/明日は笑う仕事術.html"

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
            <div class="summary-card">
                <h2><a href="{data['url']}" target="_blank">{data['title']}</a></h2>
                <p>{data['summary']}</p>
                <a href="{data['url']}" target="_blank" class="source-link">続きを読む</a>
            </div>
        """
        
    # ▼▼▼【重要】ここが、新しいデザインのHTMLテンプレートです ▼▼▼
    html_template = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{keyword} のまとめ</title>
    
    <!-- 共通のデザイン指示書（style.css）を呼び出す -->
    <link rel="stylesheet" href="../style.css">

    <!-- このページ独自のスタイルを追加 -->
    <style>
        .container {{
            max-width: 850px;
        }}
        .summary-card {{
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            margin-bottom: 25px;
            padding: 25px;
            transition: transform 0.2s;
        }}
        .summary-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        }}
        .summary-card h2 {{
            font-size: 1.4em;
            margin-top: 0;
            color: #3498db;
        }}
        .summary-card h2 a {{
            text-decoration: none;
            color: inherit;
        }}
        .summary-card p {{
            line-height: 1.7;
            margin-bottom: 15px;
        }}
        .source-link {{
            display: inline-block;
            font-weight: bold;
            color: #3498db;
            text-decoration: none;
        }}
        footer {{
            text-align: center;
            margin-top: 40px;
            color: #7f8c8d;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1 class="section-title" style="font-size: 2.2em; border-bottom: 3px solid #3498db; padding-bottom: 10px;">「{keyword}」についての自動まとめ</h1>
        </header>
        <main>
            {cards_html}
        </main>
        
        <footer>
            <p>このページはPythonプログラムによって自動生成されました。</p>
        </footer>

        <!-- 戻るリンクを分かりやすく設置 -->
        <div class="back-link" style="text-align: center; margin-top: 40px; padding-top: 30px; border-top: 1px solid #eee;">
            <a href="./matome-list.html" class="back-button" style="margin-right: 20px;">« まとめ一覧に戻る</a>
            <a href="../index.html" class="back-button">« トップページに戻る</a>
        </div>
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
        # ファイルの出力先フォルダが存在するか確認し、なければ作成する
        output_dir = os.path.dirname(OUTPUT_FILENAME)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"フォルダ '{output_dir}' を作成しました。")

        final_html = create_html(SEARCH_KEYWORD, all_site_data)
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
            f.write(final_html)
        print("-" * 50)
        print(f"🎉 成功！ 「{OUTPUT_FILENAME}」が作成されました。")
        
        # Seleniumの部分は、ローカルでの確認用なので、今はそのままでOKです。
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