// ====================================================
// BAGIAN 1: DEKLARASI SEMUA VARIABEL (DILAKUKAN SEKALI DI AWAL)
// ====================================================

// Variabel untuk Hamburger Menu
const hamburger = document.querySelector("#hamburger");
const navMenu = document.querySelector("#nav-menu");
const garis1 = document.querySelector("#garis-1");
const garis2 = document.querySelector("#garis-2");
const garis3 = document.querySelector("#garis-3");

// Variabel untuk Sticky Navbar
const header = document.querySelector("#header");
const fixedNav = 0; // Offset scroll untuk mengaktifkan sticky

// Variabel untuk Dark Mode Toggle
const darkToggle = document.querySelector("#dark-toggle");
const html = document.querySelector("html");
const body = document.querySelector("body");

// ====================================================
// BAGIAN 2: FUNGSI HAMBURGER MENU (FUNGSI 1-3)
// ====================================================

hamburger.addEventListener("click", function () {
  // 1. Toggle Menu Navigasi
  navMenu.classList.toggle("hidden");

  // 2. Transisi Hamburger ke Silang
  garis1.classList.toggle("rotate-45");
  garis2.classList.toggle("scale-0"); // Menghilangkan garis tengah
  garis3.classList.toggle("-rotate-45");
});

// Tutup menu saat link navigasi di klik (penting untuk mobile)
const navLinks = navMenu.querySelectorAll("a");
navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    // Hanya tutup di mode mobile jika menu sedang terbuka
    if (!navMenu.classList.contains("hidden")) {
      navMenu.classList.add("hidden");
      // Hapus juga kelas rotasi/active dari hamburger
      garis1.classList.remove("rotate-45");
      garis2.classList.remove("scale-0");
      garis3.classList.remove("-rotate-45");
    }
  });
});
