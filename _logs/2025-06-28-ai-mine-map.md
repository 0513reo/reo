---
layout: default
title: "【時間泥棒】AI初心者の俺がハマった、５つの無駄な作業と賢い避け方"
collection: "logs"
---
<div class="container blog-post">
    <header style="text-align:center; margin-bottom: 20px;">
        <h1 style="font-size: 2.2em; border-bottom: 2px solid #eee; padding-bottom:10px; margin-bottom: 5px;">{{ page.title }}</h1>
    </header>

    <div class="content">
        <!-- ▼▼▼ ここに、あなたの素晴らしい物語の本文を書いていきます ▼▼▼ -->

        <p>AIはすごい相棒だ。だが、正直に言おう。こいつは時々、とんでもない「時間泥棒」にもなる。<br>
        俺がこのサイトを作る過程で、マジで時間を無駄にした「地雷」を５つ、正直に白状する。<br>
        これからAIを触るあんたが、俺と同じ轍を踏まないための、未来の自分への備忘録でもある。</p>

        <hr>

        <h2>地雷１：漠然とした「丸投げ」質問</h2>
        <p><strong>【俺の失敗】</strong>「なんかいい感じのサイト作って」<br>
        AIにこう聞いたら、出てきたのはどこかで見たような、ありきたりなデザイン案ばかり。結局、何度もやり直すハメになり、数時間を溶かした。</p>
        <p><strong>【今ならこうする】役割と目的を最初に与える</strong><br>
        「<strong>あなたはプロのWebデザイナーです。</strong>アラフィフの親父が、AI挑戦記を書くための、温かみのあるブログサイトのデザイン案をください」と頼む。最初に「役割」を与えるだけで、AIの回答の質が劇的に変わることに気づいた。</p>

        <h2>地雷２：専門用語の放置</h2>
        <p><strong>【俺の失敗】</strong>「`_config.yml`に`collection`を追加して」と言われたが、`collection`が何なのか分からず、適当にコピペしてエラー発生。原因究明に半日かかった。</p>
        <p><strong>【今ならこうする】分からない言葉は、その場でAIに聞く</strong><br>
        「今の説明に出てきた`collection`って何？小学生でも分かるように、例え話で教えて」と、分からないことを恥ずかしがらずに聞く。AIは怒らないし、何度聞いてもタダだ。プライドは、時間の無駄でしかない。</p>

        <h2>地雷３：エラーメッセージの無視</h2>
        <p><strong>【俺の失敗】</strong>（ここに、あなたの具体的なエラー体験を書いてください。例えば「CSSが効かなくなった時、やみくもにあちこちいじって、さらに状況を悪化させた」など）</p>
        <p><strong>【今ならこうする】</strong>（解決策を書いてください。例えば「エラーメッセージをそのままコピーしてAIに『このエラーはどういう意味で、どうすれば直る？』と聞くのが一番の近道だった」など）</p>

        <h2>地雷４：（あなたの失敗談を書いてください）</h2>
        <p><strong>【俺の失敗】</strong>（ここに、あなたの具体的な失敗体験を書いてください）</p>
        <p><strong>【今ならこうする】</strong>（解決策を書いてください）</p>
        
        <h2>地雷５：（あなたの失敗談を書いてください）</h2>
        <p><strong>【俺の失敗】</strong>（ここに、あなたの具体的な失敗体験を書いてください）</p>
        <p><strong>【今ならこうする】</strong>（解決策を書いてください）</p>
        
        <hr>

        <p>まだまだ地雷はたくさん埋まってるだろう。だが、一つ一つクリアしていく過程こそが、一番の学びになる。この記録が、誰かの時間と、やる気を守ることになれば幸いだ。</p>

        <!-- ▲▲▲ 本文ここまで ▲▲▲ -->
    </div>
    
    <!-- ▼▼▼ ナビゲーション（ここは変更不要） ▼▼▼ -->
    <div class="navigation-links">
        {% assign collection_name = page.collection %}
        {% if collection_name %}
            {% assign posts_in_collection = site[collection_name] | sort: 'date' %}
            {% for post in posts_in_collection %}
                {% if post.url == page.url %}
                    {% assign prev_post_index = forloop.index0 | minus: 1 %}
                    {% if prev_post_index >= 0 %}
                        {% assign prev_post = posts_in_collection[prev_post_index] %}
                    {% endif %}
                    {% assign next_post_index = forloop.index0 | plus: 1 %}
                    {% if next_post_index < posts_in_collection.size %}
                        {% assign next_post = posts_in_collection[next_post_index] %}
                    {% endif %}
                {% endif %}
            {% endfor %}
            <div class="prev-link" style="width: 45%; text-align: left;">
                {% if prev_post %}<a href="{{ prev_post.url | relative_url }}" class="read-more-btn">« {{ prev_post.title }}</a>{% endif %}
            </div>
            <div class="next-link" style="width: 45%; text-align: right;">
                {% if next_post %}<a href="{{ next_post.url | relative_url }}" class="read-more-btn">{{ next_post.title }} »</a>{% endif %}
            </div>
        {% endif %}
    </div>
    <div class="back-link">
        <a href="{{ '/' | relative_url }}" class="main-button">« トップページに戻る</a>
    </div>
</div>