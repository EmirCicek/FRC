// Hide loader after a delay
window.addEventListener('load', function() {
    setTimeout(function() {
        document.querySelector('.loader').classList.add('hidden');
    }, 300); // Change 3000 to the number of milliseconds you want the loader to be visible
});


// Kullanıcı tarafından belirlenen tarih (örnek: 2024-12-31T23:59:00)
let targetDate = new Date('2024-12-31T18:10:00');
//                         yyyy-mm-ddThh-mm-ss

function updateCountdown() {
    const now = new Date();
    const timeDifference = targetDate - now;

    // Eğer belirlenen tarih geçmişse
    if (timeDifference <= 0) {
        document.querySelector('.time-box:nth-child(1) .number').innerText = '0';
        document.querySelector('.time-box:nth-child(2) .number').innerText = '0';
        document.querySelector('.time-box:nth-child(3) .number').innerText = '0';
        return;
    }

    // Zaman farkını hesaplama
    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));

    // Hesaplanan değerleri HTML'ye yerleştirme
    document.querySelector('.time-box:nth-child(1) .number').innerText = days;
    document.querySelector('.time-box:nth-child(2) .number').innerText = hours;
    document.querySelector('.time-box:nth-child(3) .number').innerText = minutes;
}

// Her saniyede bir geri sayımı güncelle
setInterval(updateCountdown, 1000);

// Sayfa yüklendiğinde geri sayımı başlat
updateCountdown();
