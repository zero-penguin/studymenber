// DOMが読み込まれたら実行
document.addEventListener('DOMContentLoaded', function () {
  // 画面全体をフェードインさせる
  function fadeInPage() {
    var body = document.body;
    body.style.opacity = '1'; // opacityプロパティを1に設定

    // 通常のコンテンツを表示させる
    var normalContent = document.querySelectorAll('.normal-content');
    for (var i = 0; i < normalContent.length; i++) {
        normalContent[i].style.display = 'block';
    }
  }

  fadeInPage(); // 画面をフェードインさせる関数を呼び出し
});
