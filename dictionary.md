---
layout: default
title: "親父的・IT用語 翻訳辞典"
---
<div class="container blog-post">
    <header style="text-align:center; margin-bottom: 20px;">
        <h1 style="font-size: 2.2em; border-bottom: 2px solid #eee; padding-bottom:10px; margin-bottom: 5px;">{{ page.title }}</h1>
    </header>

    <div class="content">
        <!-- ▼▼▼ ここから、あなたの言葉で解説を書いていきます ▼▼▼ -->

        <p>サイト作りで出てくる、なんのこっちゃ分からん専門用語。<br>俺が「ああ、そういうことか！」と理解した言葉で、勝手に翻訳してみた。<br>俺と同じように、専門用語アレルギーの人のための避難所だ。</p>

        <hr>

        <h2>サイトの憲法編</h2>
        <p>サイト全体のルールを決める、一番大事な設定ファイルに関わる言葉たち。</p>
        
        <h3>_config.yml（こんふぃぐ・やむる）</h3>
        <p><strong>【俺的・翻訳】サイトの「憲法」あるいは「取扱説明書」</strong><br>
        ここにサイトのタイトルを書いたり、「うちのサイトには『物語』と『記録』と『つぶやき』の3つのコーナーがありますよ」って宣言したりする、一番偉いファイル。これをいじるとサイト全体が変わるから、緊張する。</p>

        <h3>collection（これくしょん）</h3>
        <p><strong>【俺的・翻訳】記事をしまう「引き出し」のこと</strong><br>
        「our_story（俺たちの物語）」「logs（日々の記録）」みたいに、仲間ごとに記事を分類するための仕組み。この「引き出し」を憲法（_config.yml）で宣言しておけば、Jekyll君が賢く整理整頓してくれる。</p>
        
        <hr>

        <h2>住所と設計図編</h2>
        <p>Webページがどうやって表示されるか、その仕組みに関わる言葉たち。</p>

        <h3>baseurl（べーす・ゆーあーるえる）</h3>
        <p><strong>【俺的・翻訳】サイトの「番地」</strong><br>
        GitHubでサイトを公開すると、住所が「https://あなたのID.github.io/reo/」みたいになる。この「/reo」の部分がサイトの基本の番地だよ、ってJekyll君に教えるための設定。これを間違えると、CSS（デザイン指示書）を読み込めなくて、サイトが裸んぼうになる。</p>

        <h3>_layouts（れいあうと）フォルダ</h3>
        <p><strong>【俺的・翻訳】家の「設計図」置き場</strong><br>
        サイトの全ページで共通して使う「骨組み」の設計図（HTMLファイル）を置いとく場所。「ヘッダーはこれで、フッターはこれ」みたいな基本構造を決めておけば、記事ごとにいちいち書かなくて済むから楽ちん。</p>

        <!-- ▲▲▲ 解説はここまで。今後、新しい用語が出てきたら、この下に追加していく ▲▲▲ -->
    </div>
    
    <div class="back-link">
        <a href="{{ '/' | relative_url }}" class="main-button">« トップページに戻る</a>
    </div>
</div>