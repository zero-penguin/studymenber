// DOMが読み込まれたら実行
document.addEventListener('DOMContentLoaded', function () {
  // ローディング画面を非表示にする
  function hideLoadingScreen() {
      var loadingContainer = document.getElementById('loading-container');
      loadingContainer.style.display = 'none';
  }

  // ページ全体のロードが完了したら、ローディング画面を非表示にする
  window.addEventListener('load', hideLoadingScreen);
});

