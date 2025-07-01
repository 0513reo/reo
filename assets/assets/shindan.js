let currentQuestion = 1;
const userAnswers = [];

const analysisData = {
    q1: {
        A: "<h4>分析材料①：行動の起点 -「知の探求者」の側面</h4><p>あなたは、未知の課題に直面した時、まず理論や知識で全体像を把握しようとする傾向がありますね。闇雲に動き出すのではなく、まず自分の頭の中に「地図」を描こうとする。これは、物事を体系的に捉え、確実な一歩を踏み出す<strong>「学者」や「研究者」</strong>のような資質と言えるかもしれません。</p>",
        B: "<h4>分析材料①：行動の起点 -「実践的対話者」の側面</h4><p>あなたは、未知の課題に直面した時、一人で考え込むよりも、まず人に会い、対話の中から答えを見つけ出そうとする傾向がありますね。知識よりも経験を、理論よりも現場の声を重視する。これは、人との繋がりを力に変える<strong>「コミュニケーター」</strong>や<strong>「ジャーナリスト」</strong>のような資質と言えるかもしれません。</p>"
    },
    q2: {
        A: "<h4>分析材料②：完成の定義 -「改善主義者」の側面</h4><p>あなたは、完璧なものを一度で作り上げるよりも、不完全でもまず形にし、他者からのフィードバックを得て改善していくことを是とするスタイルのようです。これは、失敗を恐れず、対話の中からより良い答えを見つけ出そうとする、柔軟で<strong>アジャイル（俊敏）な開発者</strong>のような思考パターンです。</p>",
        B: "<h4>分析材料②：品質の追求者 -「職人」の側面</h4><p>あなたは、自分の仕事に高いプライドを持ち、中途半端な状態で世に出すことを良しとしない傾向がありますね。時間に追われても、守るべき品質のラインは譲らない。これは、自らの成果物に責任を持つ、プロフェッショナルな<strong>「職人」</strong>のようなスピリットです。</p>"
    },
    q3: {
        A: "<h4>分析材料③：喜びの源泉 -「戦略家」の側面</h4><p>あなたのモチベーションは、チームの成功の中でも、特に「自分の描いた戦略や貢献が正しかった」と証明される瞬間に、強く湧き出てくるようですね。プロセスよりも結果を、感情よりも論理を重視する。これは、勝利への道筋を描き、実行する<strong>「戦略家」</strong>や<strong>「指揮官」</strong>の資質です。</p>",
        B: "<h4>分析材料③：喜びの源泉 -「調和の創造者」の側面</h4><p>あなたのモチベーションは、個人的な成功よりも、チーム全体の成功や、そこに生まれる一体感から強く湧き出てくるようですね。自分が主役になることよりも、チームという「場」が良い雰囲気になることに価値を見出す。これは、優れた<strong>「ファシリテーター（進行役）」</strong>や<strong>「プロデューサー」</strong>が持つべき視点です。</p>"
    },
    q4: {
        A: "<h4>分析材料④：問題への対処法 -「堅実な実行者」の側面</h4><p>あなたは、目の前の課題に対し、ルールや決められた手順に従って、着実に処理していくことを得意とするようですね。創造性よりも規律を、革新よりも安定を重んじる。これは、組織を支える上で不可欠な<strong>「実務家」</strong>や<strong>「管理者」</strong>の強みです。</p>",
        B: "<h4>分析材料④：問題への対処法 -「改革者」の側面</h4><p>あなたは、目の前の面倒な作業をただこなすのではなく、常に「もっと良い方法はないか？」と問い続け、現状を疑う姿勢を持っています。現状維持を良しとせず、非効率なものを改善しようとする。これは、物事をより良く変えていこうとする<strong>「改革者」</strong>や<strong>「発明家」</strong>のスピリットです。</p>"
    },
    q5: {
        A: "<h4>分析材料⑤：リスクの捉え方 -「品質の番人」の側面</h4><p>あなたにとってのリスクとは、防げたはずのケアレスミスによって、信頼や品質を損なうことにあるようですね。細部への注意を怠らず、ミスのない完璧な仕事を目指す。これは、信頼性の高いシステムを構築する<strong>「エンジニア」</strong>や<strong>「監査役」</strong>のような価値観です。</p>",
        B: "<h4>分析材料⑤：リスクの捉え方 -「機会の探求者」の側面</h4><p>あなたにとってのリスクとは、挑戦しないことで未来の可能性を失うことにあるようですね。小さなミスを恐れて立ち止まるよりも、大きなチャンスを掴むために未知の領域へ飛び込むことを選ぶ。これは、未来の可能性に賭ける<strong>「投資家」</strong>や<strong>「冒険家」</strong>に近い価値観かもしれません。</p>"
    }
};

function answer(choice) {
    userAnswers.push({ q: 'q' + currentQuestion, choice: choice });
    document.getElementById('q' + currentQuestion).style.display = 'none';
    if (currentQuestion < 5) {
        currentQuestion++;
        document.getElementById('q' + currentQuestion).style.display = 'block';
    } else {
        showResult();
    }
}

function showResult() {
    document.getElementById('shindan-questions').style.display = 'none';
    const typeNames = [];
    const typeKeywords = {
        q1: { A: "学者/研究者", B: "コミュニケーター/ジャーナリスト" },
        q2: { A: "アジャイルな開発者", B: "プロの職人" },
        q3: { A: "戦略家/指揮官", B: "ファシリテーター/プロデューサー" },
        q4: { A: "堅実な実務家", B: "改革者/発明家" },
        q5: { A: "品質の番人", B: "投資家/冒険家" }
    };

    for (let i = 0; i < userAnswers.length; i++) {
        const answerData = userAnswers[i];
        const resultElementId = 'result' + (i + 1);
        const resultText = analysisData[answerData.q][answerData.choice];
        document.getElementById(resultElementId).innerHTML = resultText;
        typeNames.push(typeKeywords[answerData.q][answerData.choice]);
    }

    const summaryList = document.getElementById('summary-list');
    typeNames.forEach(name => {
        const listItem = document.createElement('li');
        listItem.textContent = `「${name}」のような側面`;
        summaryList.appendChild(listItem);
    });

    document.getElementById('shindan-result').style.display = 'block';
}