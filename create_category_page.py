# ----------------------------------------------------------------
# 【最終完成版】Jekyllコレクション対応！全自動カテゴリページ生成プログラム
# ----------------------------------------------------------------
import os
import glob
import re
from datetime import datetime

# --- 1. 設定項目 ---

CATEGORIES_TO_CREATE = {
    'AI奮闘記': 'category-ai-challenge.html',
    'お金': 'category-money.html',
    '副業': 'category-sidejob.html',
    '時短': 'category-shortcut.html',
    '効率': 'category-efficiency.html',
    '悩み解決': 'category-trouble.html',
    '壁の越え方': 'category-wall.html',
    '釣り': 'category-fishing.html',
    'マリンスポーツ': 'category-marine.html',
    'DIY': 'category-diy.html',
    '営業': 'category-sales.html',
    '不動産': 'category-restate.html',
    '不労所得': 'category-unearned.html',
    '4つの財布': 'category-wallets.html',
    'ママ友': 'category-madam-friends.html',
    '子育て': 'category-madam-kids.html',
    '共働き': 'category-madam-work.html',
    '旦那への愚痴': 'category-madam-grumble.html',
}

COLLECTION_FOLDERS = ["_our_story", "_logs", "_tweets"]
OUTPUT_FOLDER = "category"

# --- 2. ここから下のコードは変更不要です ---

def find_relevant_posts(keyword, collection_folders):
    """指定されたすべてのコレクションフォルダから、キーワードを含む投稿を検索する"""
    print(f"--- 「{keyword}」で検索中 in {collection_folders} ---")
    found_posts = []
    
    for folder in collection_folders:
        if not os.path.exists(folder):
            print(f"  [警告] フォルダ '{folder}' が見つかりません。スキップします。")
            continue

        html_files = glob.glob(os.path.join(folder, "*.html"))
        
        for filepath in html_files:
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                parts = re.split(r'---\s*', content, 2)
                if len(parts) < 3: continue
                
                if keyword.lower() in content.lower():
                    title_match = re.search(r'title:\s*["\']?(.*?)["\']?\s*$', parts[1], re.MULTILINE)
                    title = title_match.group(1).strip() if title_match else "タイトル不明"

                    date_obj_match = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', parts[1])
                    if date_obj_match:
                        post_date = datetime.strptime(date_obj_match.group(1), "%Y-%m-%d")
                    else:
                        post_date = datetime.fromtimestamp(os.path.getmtime(filepath))

                    post_url_base = os.path.splitext(os.path.basename(filepath))[0]
                    post_url = f"/{folder.replace('_','')}/{post_url_base}.html"
                    
                    found_posts.append({ 'title': title, 'url': post_url, 'date': post_date })
                    print(f"  [発見！] -> {filepath}")
            except Exception as e:
                print(f"  [エラー] {filepath} の処理中: {e}")
    
    return sorted(found_posts, key=lambda x: x['date'], reverse=True)

def create_category_page_for_jekyll(keyword, posts_data, output_filepath):
    """Jekyll用のカテゴリページ（HTML）を生成する"""
    print(f"--- HTMLファイルを生成しています: {output_filepath} ---")
    
    # ★★★ ここが最重要修正点！ post.html と同じ骨組みを生成するように変更 ★★★
    page_content = f"""---
layout: post
title: 「{keyword}」に関する記事まとめ
---

<ul class="archive-list">
"""
    if not posts_data:
        page_content += "<li><p>このカテゴリに関連する記事はまだありません。</p></li>"
    else:
        for post in posts_data:
            page_content += f"""
            <li>
                <a href="{{{{ '{post['url']}' | relative_url }}}}">
                    <span class="post-title">{post['title']}</span>
                    <span class="post-date">{post['date'].strftime('%Y年%m月%d日')}</span>
                </a>
            </li>
            """
    page_content += "</ul>"
    
    output_dir = os.path.dirname(output_filepath)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"フォルダ '{output_dir}' を作成しました。")

    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write(page_content)
    print(f"🎉 成功！ 「{output_filepath}」が作成されました。")

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"フォルダ '{OUTPUT_FOLDER}' を作成しました。")

    for keyword, filename in CATEGORIES_TO_CREATE.items():
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        print(f"\n{'='*50}")
        found_posts = find_relevant_posts(keyword, COLLECTION_FOLDERS)
        create_category_page_for_jekyll(keyword, found_posts, output_path)
        print(f"{'='*50}")
        
    print("\n✨✨ すべてのカテゴリページの作成が完了しました！ ✨✨")