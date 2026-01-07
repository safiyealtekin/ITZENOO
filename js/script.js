// --- Global Değişkenler ---
const searchForm = document.querySelector(".search-form");
const cartItem = document.querySelector(".cart-items-container");
const navbar = document.querySelector(".navbar");

const searchBtn = document.querySelector("#search-btn");
const cartBtn = document.querySelector("#cart-btn");
const menuBtn = document.querySelector("#menu-btn");


// --- Navigasyon Buton İşleyicileri (Arama, Sepet, Menü) ---

// Bu fonksiyonlar, butonlara tıklandığında ilgili öğeyi açar/kapatır
// ve sayfanın herhangi bir yerine tıklandığında kapatır.
function setupToggleBehavior(button, element) {
    button.addEventListener("click", function() {
        // Tıklandığında öğeyi aç/kapat
        element.classList.toggle("active");
    });

    // Açık olan öğenin dışına tıklandığında kapatma işlemi
    document.addEventListener("click", function(e) {
        // e.composedPath() modern tarayıcılarda tıklanan yolu verir.
        // Tıklanan yol, butonu veya açılan öğeyi içermiyorsa kapat.
        if (
            !e.composedPath().includes(button) &&
            !e.composedPath().includes(element) &&
            element.classList.contains("active") // Sadece açıksa kontrol et
        ) {
            element.classList.remove("active");
        }
    });
}

// Butonlara davranışları ata
if (searchBtn && searchForm) setupToggleBehavior(searchBtn, searchForm);

// if (cartBtn && cartItem) setupToggleBehavior(cartBtn, cartItem); 
if (menuBtn && navbar) setupToggleBehavior(menuBtn, navbar);


// --- Açılır Menü (Alanlar) İşleyicisi ---

/* Alanlar açılır menüsünü göster/gizle fonksiyonu */
function toggleDropdown() {
    document.getElementById("alanDropdown").classList.toggle("show");
}

/* Sayfanın herhangi bir yerine tıklandığında Alanlar menüsünü kapat */
window.onclick = function(event) {
    // Eğer tıklanan yer açılır menü düğmesi (.dropbtn) değilse
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            // Açık menüyü kapat
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}


// --- DOMContentLoaded: Slider ve Diğer İşlemler ---

document.addEventListener('DOMContentLoaded', function() {
    // 1. Elementlerin doğru seçildiğinden emin olun (Sadece bir kez tanımlanmalı)
    const sliderTrack = document.querySelector('.menu .slider-track');
    const prevBtn = document.querySelector('.menu .prev-btn');
    const nextBtn = document.querySelector('.menu .next-btn');
    const sliderItems = document.querySelectorAll('.menu .slider-item');

    // Elementler yoksa durdur
    if (!sliderTrack || sliderItems.length === 0 || !prevBtn || !nextBtn) {
        // console.error("Slider elementlerinden bazıları DOM'da bulunamadı.");
        return; 
    }

    // 2. Kaydırma Miktarı Hesaplama
    // Dikkat: Kaydırma miktarını bir kutu genişliği + aralık olarak doğru hesaplamalıyız
    const itemWidth = sliderItems[0].offsetWidth; 
    
    // CSS'ten gap değerini al (daha doğru bir yöntem)
    const gapValue = parseFloat(window.getComputedStyle(sliderTrack).getPropertyValue('gap'));
    
    // Eğer gap değeri NaN dönerse (geçersiz), varsayılan bir değer kullan
    const calculatedGap = isNaN(gapValue) ? 24 : gapValue; // 24px = 1.5rem (tahmini)

    // Kaydırma miktarı = Bir kutu genişliği + Aradaki boşluk
    const scrollAmount = itemWidth + calculatedGap; 
    
    // 3. Olay Dinleyicileri
    nextBtn.addEventListener('click', () => {
        sliderTrack.scrollLeft += scrollAmount;
    });



    const modal = document.getElementById("infoModal");
const modalTitle = document.getElementById("modalTitle");
const modalText = document.getElementById("modalText");
const closeBtn = document.getElementById("closeModal");

function openModal(title, text) {
  modalTitle.textContent = title;
  modalText.textContent = text;
  modal.style.display = "flex";
}

closeBtn.addEventListener("click", () => {
  modal.style.display = "none";
});

window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.style.display = "none";
  }
});


    prevBtn.addEventListener('click', () => {
        sliderTrack.scrollLeft -= scrollAmount;
    });
});