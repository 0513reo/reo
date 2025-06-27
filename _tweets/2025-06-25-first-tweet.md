---
layout: default
title: "二日酔いと、失われた時間"
collection: tweets
---

<div class="container blog-post" style="max-width: 850px;">
    <header style="text-align:center; margin-bottom: 20px;">
        <!-- ★★★ Jekyllの魔法で、タイトルを自動表示 ★★★ -->
        <h1 style="font-size: 2.5em; border-bottom: 2px solid #eee; padding-bottom:10px; margin-bottom: 5px;">{{ page.title }}</h1>
        <p style="font-size: 1.1em; color: #555; margin-top: 0;">- 今日のつぶやき -</p>
    </header>

    <div class="content">
        <p>
            今日は、、、<br>
            二日酔い、、、
        </p>
        <p>
            久しぶりに無理をした。ここ2日間の合計睡眠時間は、わずか3時間。<br>
            そんな状態で、昨日の19時ごろから始まった宴。
        </p>
        <p>
            ビール、赤ワイン、白ワイン、シャンパン、ハイボール、テキーラ…。<br>
            そして、また飲めないのに、テキーラ…。
        </p>
        <p>
            日付が変わるまで飲み続け、まだ平気そうな顔をしている先輩たちをタクシーへ押し込む。<br>
            なんとか自分もタクシーに乗り込み、帰宅して、着替えて、ベッドに倒れ込んだはずだった。
        </p>

        <hr style="margin: 40px 0;">

        <p style="text-align:center; font-size: 2em; font-weight: bold; color: #e74c3c;">
            起きたら、16時。
        </p>
        
        <p>
            休みだったとは言え、さすがに、これは……。<br>
            まだ、眠い。
        </p>
    </div>

    <!-- ★★★ 究極の自動ナビゲーション (バグ修正版) ★★★ -->
    <div class="navigation-links" style="display: flex; justify-content: space-between; align-items: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee;">
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
                {% if prev_post %}
                    <a href="{{ prev_post.url | relative_url }}" class="read-more-btn">« {{ prev_post.title }}</a>
                {% endif %}
            </div>
            <div class="next-link" style="width: 45%; text-align: right;">
                {% if next_post %}
                    <a href="{{ next_post.url | relative_url }}" class="read-more-btn">{{ next_post.title }} »</a>
                {% endif %}
            </div>
        {% endif %}
    </div>
    <div class="back-link" style="text-align: center; margin-top: 50px;">
        <a href="{{ '/' | relative_url }}" class="main-button" style="display:inline-block; width:auto;">« トップページに戻る</a>
    </div>
</div>