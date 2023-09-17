let slideIndex = 0;
    showSlides();

    function showSlides() {
      let slides = document.getElementsByClassName("slide");
      
      for (let i = 0; i < slides.length; i++) {
          slides[i].style.opacity = 0; // 最初はすべてのスライドを非表示にする
      }
      
      slideIndex++;
      
      if (slideIndex > slides.length) {
          slideIndex = 1;
      }
      
      slides[slideIndex - 1].style.opacity = 1; // 次のスライドを表示する
      
      setTimeout(showSlides, 2000); // 2秒ごとにスライド切り替え

    }