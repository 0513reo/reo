import os
import glob

# --- 設定項目 ---
# 拡張子を変更したいコレクションフォルダのリスト
COLLECTION_FOLDERS = ["_our_story", "_logs", "_tweets"]
# ----------------

def convert_md_to_html_in_collections(folders):
    """
    指定されたコレクションフォルダ内の全.mdファイルを.htmlにリネームする
    """
    print("--- 拡張子一括変換プログラムを開始します ---")
    total_renamed_count = 0

    for folder in folders:
        if not os.path.exists(folder):
            print(f"[警告] フォルダ '{folder}' が見つかりません。スキップします。")
            continue

        print(f"\n>>> '{folder}' フォルダを検索中...")
        
        # .md ファイルをすべて検索
        md_files = glob.glob(os.path.join(folder, "*.md"))
        
        if not md_files:
            print("  -> .md ファイルは見つかりませんでした。")
            continue

        renamed_count_in_folder = 0
        for md_filepath in md_files:
            # 新しいファイルパスを生成 (.mdを.htmlに置換)
            html_filepath = os.path.splitext(md_filepath)[0] + ".html"
            
            try:
                # ファイル名を変更
                os.rename(md_filepath, html_filepath)
                print(f"  [成功] {os.path.basename(md_filepath)} -> {os.path.basename(html_filepath)}")
                renamed_count_in_folder += 1
            except OSError as e:
                print(f"  [エラー] {os.path.basename(md_filepath)} の名前変更に失敗しました: {e}")
        
        print(f"  -> '{folder}' フォルダで {renamed_count_in_folder} 個のファイルを変換しました。")
        total_renamed_count += renamed_count_in_folder

    print("\n--- 処理完了 ---")
    print(f"合計 {total_renamed_count} 個のファイルの拡張子を .html に変更しました。")

if __name__ == "__main__":
    convert_md_to_html_in_collections(COLLECTION_FOLDERS)