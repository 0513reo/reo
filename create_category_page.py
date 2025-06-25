# ----------------------------------------------------------------
# 【究極版】Jekyll対応！全自動カテゴリページ生成プログラム (修正版)
# ----------------------------------------------------------------
import os
import glob
import re
from datetime import datetime

# --- 1. 設定項目 ---

# ★★★ ここに、作りたいカテゴリの情報をどんどん追加してください ★★★
CATEGORIES_TO_CREATE = {
    'AI奮闘記': 'category-ai-challenge.html',
    'お金': 'category-money.html',
    '副業': 'category-sidejob.html',
    '時短': 'category-shortcut.html',
    '効率': 'category-efficiency.html',
    '悩み解決': 'category-trouble.html',
    '壁の越え方': 'category-wall.html',
    '学歴いらない世界': 'category-no-degree.html',
    '投資': 'category-investment.html',
    '株': 'category-stock.html',
    '釣り': 'category-fishing.html',
    '船': 'category-boat.html',
    'マリンスポーツ': 'category-marine.html',
    'DIY': 'category-diy.html',
    '工具': 'category-tools.html',
    '営業': 'category-sales.html',
    '不動産': 'category-restate.html',
    '不労所得': 'category-unearned.html',
    '4つの財布': 'category-wallets.html',
    'FX': 'category-fx.html',
    'モンハン': 'category-monhan.html',
    '昔のパチンコの話': 'category-pachinko.html',
    'お付き合いゴルフ': 'category-golf.html',
    'ママ友': 'category-madam-friends.html',
    '子育て': 'category-madam-kids.html',
    '共働き': 'category-madam-work.html',
    '旦那への愚痴': 'category-madam-grumble.html',
}

# ★★★ Jekyllの投稿フォルダと、カテゴリページの出力先を指定 ★★★
POSTS_FOLDER = "_posts"
OUTPUT_FOLDER = "category"

# --- 2. ここから下のコードは変更不要です ---

def find_relevant_posts(keyword, posts_folder):
    """_postsフォルダ内の全マークダウンファイルを検索し、キーワードを含む投稿の情報を返す"""
    print(f"--- 「{keyword}」で検索中 in {posts_folder} ---")
    found_posts = []
    
    md_files = glob.glob(os.path.join(posts_folder, "*.md"))
    
    for filepath in md_files:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            parts = re.split(r'---\s*', content, 2)
            if len(parts) < 3: continue
            
            if keyword.lower() in content.lower():
                title_match = re.search(r'title:\s*["\']?(.*?)["\']?\s*$', parts[1], re.MULTILINE)
                title = title_match.group(1) if title_match else "タイトル不明"

                date_str = os.path.basename(filepath)[:10]
                post_date = datetime.strptime(date_str, "%Y-%m-%d")

                post_url = post_date.strftime("/%Y/%m/%d/") + os.path.basename(filepath)[11:].replace('.md', '.html')

                found_posts.append({
                    'title': title,
                    'url': post_url,
                    'date': post_date
                })
                print(f"  [発見！] -> {filepath}")
        except Exception as e:
            print(f"  [エラー] {filepath} の処理中: {e}")
    
    return sorted(found_posts, key=lambda x: x['date'], reverse=True)

def create_category_page_for_jekyll(keyword, posts_data, output_filepath):
    """Jekyll用のカテゴリページ（HTML）を生成する"""
    print(f"--- HTMLファイルを生成しています: {output_filepath} ---")
    
    front_matter = f"""---
layout: default
title: 「{keyword}」に関する記事一覧
---
"""
    
    cards_html = ""
    if not posts_data:
        cards_html = "<p>このカテゴリに関連する記事はまだありません。</p>"
    else:
        # ▼▼▼【重要】抜け落ちていたforループを、ここに追加しました！ ▼▼▼
        for post in posts_data:
            # リンクの閉じカッコも修正済み
            cards_html += f"""
            <a href="{{{{ site.baseurl }}}}{{post['url']}}" class="card">
                <h3>{post['title']}</h3>
                <p>公開日: {post['date'].strftime('%Y年%m月%d日')}</p>
            </a>
            """

    page_content = f"""
<div class="container">
    <header>
        <h1 class="section-title" style="font-size: 2.2em; border-bottom: 3px solid #3498db; padding-bottom: 10px;">「{keyword}」に関する記事まとめ</h1>
    </header>
    <div class="link-container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 40px;">
        {cards_html}
    </div>
</div>
"""
    
    final_content = front_matter + page_content
    
    output_dir = os.path.dirname(output_filepath)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"フォルダ '{output_dir}' を作成しました。")

    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"🎉 成功！ 「{output_filepath}」が作成されました。")


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"フォルダ '{OUTPUT_FOLDER}' を作成しました。")

    all_html_files = glob.glob(os.path.join(POSTS_FOLDER, "*.md"))
    
    for keyword, filename in CATEGORIES_TO_CREATE.items():
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        print(f"\n{'='*50}")
        # find_relevant_postsに渡す引数を修正
        found_posts = find_relevant_posts(keyword, POSTS_FOLDER)
        create_category_page_for_jekyll(keyword, found_posts, output_path)
        print(f"{'='*50}")
        
    print("\n✨✨ すべてのカテゴリページの作成が完了しました！ ✨✨")