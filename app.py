
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#7057ef">
<title>مكتبتي الرقمية | My Digital Library</title>

<!-- الخطوط والأيقونات -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

<!-- PDF.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>

<style>
/* =========================
   1. المتغيرات والتصميم العام
========================= */
:root {
  --primary: #7057ef;
  --secondary: #a855f7;
  --accent: #00c9a7;
  --bg: #f7f7fc;
  --surface: #ffffff;
  --text: #25243a;
  --muted: #85849b;
  --border: #eceaf5;
  --shadow: 0 12px 40px rgba(65,45,130,.09);
  --gradient: linear-gradient(135deg,#7057ef,#b14df4);
}

body.dark {
  --bg: #12121e;
  --surface: #1d1d2d;
  --text: #f4f1ff;
  --muted: #aaa5c1;
  --border: #333047;
  --shadow: 0 12px 40px rgba(0,0,0,.25);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Cairo', sans-serif;
  background: var(--bg);
  color: var(--text);
  transition: background .35s,color .35s;
  overflow-x: hidden;
}

button,input,select {
  font: inherit;
}

button {
  cursor: pointer;
  border: none;
}

a {
  text-decoration: none;
  color: inherit;
}

.container {
  width: min(1250px,92%);
  margin: auto;
}

/* =========================
   2. الهيدر
========================= */
header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: color-mix(in srgb,var(--surface) 85%,transparent);
  backdrop-filter: blur(18px);
  border-bottom: 1px solid var(--border);
}

.navbar {
  height: 78px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 15px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 21px;
  font-weight: 900;
}

.logo-icon {
  width: 45px;
  height: 45px;
  border-radius: 15px;
  background: var(--gradient);
  display: grid;
  place-items: center;
  color: white;
  box-shadow: 0 6px 20px #7057ef55;
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.icon-btn {
  width: 42px;
  height: 42px;
  border-radius: 13px;
  background: var(--bg);
  color: var(--text);
  transition: .3s;
}

.icon-btn:hover {
  background: var(--primary);
  color: white;
  transform: translateY(-3px);
}

.admin-btn {
  padding: 11px 18px;
  border-radius: 12px;
  color: white;
  background: var(--gradient);
  font-weight: 700;
  transition: .3s;
}

.admin-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px #7057ef55;
}

/* =========================
   3. القسم الرئيسي
========================= */
.hero {
  margin-top: 35px;
  border-radius: 30px;
  padding: 55px 45px;
  color: white;
  background: linear-gradient(120deg,#5e49dd,#9e50ef,#d45ad8);
  background-size: 200% 200%;
  animation: gradientMove 8s ease infinite;
  position: relative;
  overflow: hidden;
  box-shadow: 0 20px 50px #7855dc30;
}

.hero::before,.hero::after {
  content: "";
  position: absolute;
  border-radius: 50%;
  background: #ffffff12;
  pointer-events: none;
}

.hero::before {
  width: 280px;
  height: 280px;
  top: -140px;
  right: -70px;
}

.hero::after {
  width: 200px;
  height: 200px;
  bottom: -120px;
  left: 15%;
}

.hero-content {
  position: relative;
  z-index: 2;
}

.hero-label {
  display: inline-block;
  background: #ffffff25;
  padding: 7px 16px;
  border-radius: 30px;
  font-size: 13px;
  margin-bottom: 18px;
}

.hero h1 {
  font-size: clamp(28px,5vw,48px);
  font-weight: 900;
  line-height: 1.5;
}

.hero p {
  margin-top: 12px;
  opacity: .9;
  font-size: 16px;
  max-width: 600px;
  line-height: 2;
}

.hero-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 35px;
  margin-top: 30px;
}

.hero-stat strong {
  display: block;
  font-size: 27px;
}

.hero-stat span {
  font-size: 13px;
  opacity: .8;
}

/* =========================
   4. البحث والإحصائيات
========================= */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 18px;
  margin: 30px 0;
}

.stat-card {
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 20px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  gap: 15px;
  box-shadow: var(--shadow);
  transition: .3s;
}

.stat-card:hover {
  transform: translateY(-5px);
}

.stat-icon {
  width: 50px;
  height: 50px;
  display: grid;
  place-items: center;
  border-radius: 16px;
  background: #7057ef18;
  color: var(--primary);
  font-size: 20px;
}

.stat-card strong {
  display: block;
  font-size: 23px;
}

.stat-card small {
  color: var(--muted);
}

.section-title {
  font-size: 23px;
  font-weight: 900;
  margin-bottom: 18px;
}

.toolbar {
  display: flex;
  gap: 12px;
  margin: 25px 0;
  flex-wrap: wrap;
}

.search-box {
  flex: 1;
  min-width: 200px;
  position: relative;
}

.search-box i {
  position: absolute;
  right: 17px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--muted);
}

.search-box input,
.toolbar select {
  width: 100%;
  height: 50px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  outline: none;
  padding: 0 45px 0 15px;
  color: var(--text);
  transition: .3s;
}

.toolbar select {
  width: auto;
  min-width: 145px;
  padding: 0 15px;
}

.search-box input:focus,
.toolbar select:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 4px #7057ef18;
}

.filters {
  display: flex;
  gap: 9px;
  flex-wrap: wrap;
  margin-bottom: 25px;
}

.filter-btn {
  padding: 9px 17px;
  border-radius: 30px;
  background: var(--surface);
  color: var(--muted);
  border: 1px solid var(--border);
  transition: .3s;
  font-size: 13px;
  font-weight: 700;
}

.filter-btn:hover,
.filter-btn.active {
  background: var(--primary);
  color: white;
  border-color: var(--primary);
}

/* =========================
   5. بطاقات الكتب
========================= */
.books-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(210px,1fr));
  gap: 23px;
  padding-bottom: 50px;
}

.book-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 21px;
  overflow: hidden;
  position: relative;
  box-shadow: var(--shadow);
  animation: cardIn .6s cubic-bezier(.2,.8,.2,1) both;
  transition: transform .35s,box-shadow .35s;
  transform-style: preserve-3d;
}

.book-card:hover {
  transform: translateY(-9px) rotateX(2deg);
  box-shadow: 0 22px 40px #7057ef20;
}

.book-cover {
  height: 245px;
  background: linear-gradient(135deg,#ded8ff,#b4a2fa);
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  position: relative;
}

.book-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .6s;
}

.book-card:hover .book-cover img {
  transform: scale(1.07);
}

.no-cover {
  color: #7057ef;
  font-size: 65px;
}

.book-category {
  position: absolute;
  top: 12px;
  right: 12px;
  background: #ffffffeb;
  color: #7057ef;
  padding: 5px 11px;
  font-size: 11px;
  border-radius: 20px;
  font-weight: 800;
}

.favorite-btn {
  position: absolute;
  top: 12px;
  left: 12px;
  width: 35px;
  height: 35px;
  border-radius: 50%;
  background: #ffffffeb;
  color: #888;
  z-index: 2;
  transition: .3s;
}

.favorite-btn.active {
  color: #f04472;
  transform: scale(1.1);
}

.book-info {
  padding: 17px;
}

.book-info h3 {
  font-size: 16px;
  font-weight: 900;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.author {
  font-size: 12px;
  color: var(--muted);
  margin: 7px 0;
}

.rating {
  color: #f4b400;
  font-size: 12px;
  margin: 7px 0;
}

.book-meta {
  display: flex;
  gap: 12px;
  font-size: 11px;
  color: var(--muted);
  margin: 10px 0;
}

.read-progress {
  height: 4px;
  border-radius: 10px;
  background: var(--border);
  margin: 12px 0;
  overflow: hidden;
}

.read-progress div {
  height: 100%;
  background: var(--gradient);
  border-radius: inherit;
  transition: width .4s;
}

.card-actions {
  display: flex;
  gap: 8px;
}

.card-btn {
  flex: 1;
  padding: 10px 5px;
  border-radius: 11px;
  font-size: 12px;
  font-weight: 800;
  transition: .3s;
}

.read-btn {
  background: var(--gradient);
  color: white;
}

.download-btn {
  background: var(--bg);
  color: var(--text);
}

.card-btn:hover {
  transform: translateY(-3px);
  filter: brightness(1.08);
}

/* =========================
   6. Skeleton Loading
========================= */
.skeleton {
  height: 350px;
  border-radius: 20px;
  background: linear-gradient(90deg,
    var(--border) 25%,var(--bg) 50%,var(--border) 75%);
  background-size: 200% 100%;
  animation: shimmer 1.4s infinite;
}

/* =========================
   7. النوافذ المنبثقة
========================= */
.modal {
  position: fixed;
  inset: 0;
  z-index: 500;
  background: #080817bb;
  backdrop-filter: blur(9px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 15px;
}

.modal.active {
  display: flex;
  animation: fadeIn .25s;
}

.modal-content {
  width: min(520px,100%);
  max-height: 90vh;
  overflow-y: auto;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 23px;
  padding: 25px;
  animation: springIn .4s cubic-bezier(.2,.9,.3,1.2);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.close-btn {
  width: 35px;
  height: 35px;
  background: var(--bg);
  color: var(--text);
  border-radius: 10px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 7px;
  font-weight: 800;
  font-size: 13px;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 13px;
  border: 1px solid var(--border);
  background: var(--bg);
  color: var(--text);
  border-radius: 12px;
  outline: none;
}

.form-group input:focus,
.form-group select:focus {
  border-color: var(--primary);
}

.submit-btn {
  width: 100%;
  padding: 14px;
  border-radius: 13px;
  background: var(--gradient);
  color: white;
  font-weight: 900;
  margin-top: 10px;
}

/* =========================
   8. قارئ PDF
========================= */
.reader-modal {
  padding: 0;
}

.reader-content {
  width: 100%;
  height: 100%;
  max-height: 100%;
  border-radius: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  background: #191923;
  color: white;
  overflow: hidden;
}

.reader-header {
  min-height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 10px 18px;
  background: #242434;
}

.reader-title {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-weight: 800;
}

.reader-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  flex-wrap: wrap;
  padding: 12px;
  background: #20202e;
}

.reader-controls button {
  background: #37374c;
  color: white;
  border-radius: 8px;
  padding: 8px 12px;
}

.reader-controls button:hover {
  background: var(--primary);
}

.reader-controls input {
  width: 50px;
  padding: 7px;
  text-align: center;
  border: 0;
  border-radius: 7px;
}

.reader-progress {
  height: 4px;
  background: #343447;
}

.reader-progress div {
  height: 100%;
  background: #a88aff;
  width: 0;
  transition: width .3s;
}

.reader-body {
  flex: 1;
  overflow: auto;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 25px;
  position: relative;
}

#pdfCanvas {
  max-width: 100%;
  height: auto;
  box-shadow: 0 5px 30px #0008;
}

.reader-loading {
  margin: 40px;
  color: white;
  text-align: center;
}

.reader-error {
  text-align: center;
  margin: auto;
  max-width: 400px;
  line-height: 2;
  color: #ffb5b5;
}

/* =========================
   9. Toast
========================= */
#toast-container {
  position: fixed;
  bottom: 25px;
  left: 20px;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.toast {
  background: var(--surface);
  color: var(--text);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
  padding: 14px 20px;
  border-radius: 13px;
  animation: toastIn .4s ease both;
  display: flex;
  align-items: center;
  gap: 10px;
}

.toast i {
  color: var(--accent);
}

/* =========================
   10. Scroll animations
========================= */
.reveal {
  opacity: 0;
  transform: translateY(25px);
  transition: .7s cubic-bezier(.2,.8,.2,1);
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

/* =========================
   11. Footer
========================= */
footer {
  background: var(--surface);
  border-top: 1px solid var(--border);
  padding: 30px 15px;
  text-align: center;
  color: var(--muted);
  font-size: 13px;
}

footer strong {
  color: var(--primary);
}

/* =========================
   12. Animations
========================= */
@keyframes gradientMove {
  0%,100% {background-position: 0% 50%}
  50% {background-position: 100% 50%}
}

@keyframes cardIn {
  from {opacity: 0;transform: translateY(25px) scale(.96)}
  to {opacity: 1;transform: translateY(0) scale(1)}
}

@keyframes springIn {
  from {opacity: 0;transform: scale(.85) translateY(25px)}
  to {opacity: 1;transform: scale(1) translateY(0)}
}

@keyframes fadeIn {
  from {opacity: 0}
  to {opacity: 1}
}

@keyframes shimmer {
  to {background-position: -200% 0}
}

@keyframes toastIn {
  from {opacity: 0;transform: translateX(-30px)}
  to {opacity: 1;transform: translateX(0)}
}

/* =========================
   13. Responsive
========================= */
@media(max-width:700px) {
  .hero {
    padding: 35px 22px;
    border-radius: 22px;
  }

  .hero-stats {
    gap: 20px;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .books-grid {
    grid-template-columns: repeat(2,minmax(0,1fr));
    gap: 12px;
  }

  .book-cover {
    height: 190px;
  }

  .book-info {
    padding: 12px;
  }

  .book-info h3 {
    font-size: 14px;
  }

  .card-btn {
    font-size: 10px;
  }

  .navbar {
    height: 68px;
  }

  .logo {
    font-size: 16px;
  }

  .admin-btn {
    padding: 10px;
    font-size: 11px;
  }

  .reader-header {
    font-size: 12px;
  }

  .reader-body {
    padding: 10px;
  }
}

@media(max-width:370px) {
  .books-grid {
    grid-template-columns: 1fr;
  }
}

@media(prefers-reduced-motion:reduce) {
  *,*::before,*::after {
    animation-duration: .01ms !important;
    transition-duration: .01ms !important;
  }
}
</style>
</head>

<body>

<!-- =========================
     الهيدر
========================= -->
<header>
  <div class="container navbar">

    <div class="logo">
      <div class="logo-icon">
        <i class="fas fa-book-open"></i>
      </div>
      <span>مكتبتي الرقمية</span>
    </div>

    <div class="nav-actions">
      <button class="icon-btn" id="themeBtn" title="تغيير المظهر">
        <i class="fas fa-moon"></i>
      </button>

      <button class="admin-btn" onclick="openAdmin()">
        <i class="fas fa-plus"></i>
        إضافة كتاب
      </button>
    </div>

  </div>
</header>

<main class="container">

  <!-- =========================
       Hero
  ========================= -->
  <section class="hero reveal">

    <div class="hero-content">

      <span class="hero-label">
        <i class="fas fa-book"></i>
        مرحباً بك في عالم المعرفة
      </span>

      <h1>اقرأ، اكتشف، وتعلّم<br>بلا حدود 📚</h1>

      <p>
        مكتبتك الرقمية الخاصة، اكتشف مجموعة متنوعة من الكتب
        والروايات، واقرأ مباشرة من متصفحك في أي وقت.
      </p>

      <div class="hero-stats">
        <div class="hero-stat">
          <strong id="heroBooks">0</strong>
          <span>كتاب</span>
        </div>

        <div class="hero-stat">
          <strong id="heroViews">0</strong>
          <span>مشاهدة</span>
        </div>

        <div class="hero-stat">
          <strong id="heroDownloads">0</strong>
          <span>تحميل</span>
        </div>
      </div>

    </div>
  </section>

  <!-- =========================
       Statistics
  ========================= -->
  <section class="stats-grid reveal">

    <div class="stat-card">
      <div class="stat-icon"><i class="fas fa-book"></i></div>
      <div>
        <strong id="statBooks">0</strong>
        <small>إجمالي الكتب</small>
      </div>
    </div>

    <div class="stat-card">
      <div class="stat-icon"><i class="fas fa-eye"></i></div>
      <div>
        <strong id="statViews">0</strong>
        <small>إجمالي المشاهدات</small>
      </div>
    </div>

    <div class="stat-card">
      <div class="stat-icon"><i class="fas fa-download"></i></div>
      <div>
        <strong id="statDownloads">0</strong>
        <small>إجمالي التحميلات</small>
      </div>
    </div>

  </section>

  <!-- =========================
       Books section
  ========================= -->
  <section id="library" class="reveal">

    <h2 class="section-title">
      <i class="fas fa-layer-group" style="color:var(--primary)"></i>
      اكتشف مكتبتنا
    </h2>

    <div class="toolbar">

      <div class="search-box">
        <i class="fas fa-search"></i>
        <input id="searchInput" type="search"
          placeholder="ابحث عن كتاب أو مؤلف...">
      </div>

      <select id="sortSelect">
        <option value="new">الأحدث</option>
        <option value="popular">الأكثر مشاهدة</option>
        <option value="downloads">الأكثر تحميلاً</option>
        <option value="rating">الأعلى تقييماً</option>
        <option value="title">حسب العنوان</option>
      </select>

    </div>

    <div class="filters" id="filters">
      <button class="filter-btn active" data-filter="all">الكل</button>
      <button class="filter-btn" data-filter="favorite">المفضلة ⭐</button>
    </div>

    <div class="books-grid" id="booksGrid">
      <div class="skeleton"></div>
      <div class="skeleton"></div>
      <div class="skeleton"></div>
      <div class="skeleton"></div>
    </div>

  </section>

</main>

<footer>
  <p>
    © 2026 <strong>مكتبتي الرقمية</strong> -
    جميع الحقوق محفوظة
  </p>
  <p style="margin-top:7px">صُنعت بحب من أجل عشاق القراءة ❤️</p>
</footer>

<!-- =========================
     لوحة إضافة كتاب
========================= -->
<div class="modal" id="adminModal">
  <div class="modal-content">

    <div class="modal-header">
      <h3>إضافة كتاب جديد 📚</h3>
      <button class="close-btn" onclick="closeModal('adminModal')">
        <i class="fas fa-times"></i>
      </button>
    </div>

    <form id="bookForm">

      <div class="form-group">
        <label>عنوان الكتاب *</label>
        <input id="bookTitle" required placeholder="أدخل عنوان الكتاب">
      </div>

      <div class="form-group">
        <label>اسم المؤلف *</label>
        <input id="bookAuthor" required placeholder="اسم المؤلف">
      </div>

      <div class="form-group">
        <label>رابط PDF *</label>
        <input id="bookUrl" type="url" required placeholder="https://example.com/book.pdf">
      </div>

      <div class="form-group">
        <label>رابط صورة الغلاف</label>
        <input id="bookCover" type="url" placeholder="https://example.com/cover.jpg">
      </div>

      <div class="form-group">
        <label>التصنيف</label>
        <select id="bookCategory">
          <option value="روايات">روايات</option>
          <option value="تطوير الذات">تطوير الذات</option>
          <option value="تاريخ">تاريخ</option>
          <option value="علوم">علوم</option>
          <option value="ثقافة">ثقافة</option>
          <option value="أخرى">أخرى</option>
        </select>
      </div>

      <button class="submit-btn" type="submit">
        <i class="fas fa-plus"></i>
        إضافة إلى المكتبة
      </button>

    </form>
  </div>
</div>

<!-- =========================
     قارئ PDF
========================= -->
<div class="modal reader-modal" id="readerModal">

  <div class="modal-content reader-content">

    <div class="reader-header">
      <div class="reader-title" id="readerTitle">قارئ PDF</div>

      <div style="display:flex;gap:8px">
        <button class="icon-btn" onclick="toggleFullscreen()" title="ملء الشاشة">
          <i class="fas fa-expand"></i>
        </button>

        <button class="icon-btn" onclick="closeReader()" title="إغلاق">
          <i class="fas fa-times"></i>
        </button>
      </div>
    </div>

    <div class="reader-progress">
      <div id="readerProgress"></div>
    </div>

    <div class="reader-controls">

      <button onclick="previousPage()">
        <i class="fas fa-chevron-right"></i>
      </button>

      <input id="pageInput" type="number" value="1" min="1">

      <span id="pageTotal">/ 0</span>

      <button onclick="nextPage()">
        <i class="fas fa-chevron-left"></i>
      </button>

      <button onclick="zoomOut()">
        <i class="fas fa-minus"></i>
      </button>

      <button onclick="zoomIn()">
        <i class="fas fa-plus"></i>
      </button>

    </div>

    <div class="reader-body" id="readerBody">
      <div class="reader-loading" id="readerLoading">
        <i class="fas fa-spinner fa-spin fa-2x"></i>
        <p>جاري تحميل الكتاب...</p>
      </div>

      <canvas id="pdfCanvas" hidden></canvas>
    </div>

  </div>
</div>

<div id="toast-container"></div>

<script>
/* =========================================
   1. إعداد PDF.js
========================================= */
pdfjsLib.GlobalWorkerOptions.workerSrc =
'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

/* =========================================
   2. قاعدة البيانات المحلية
========================================= */
const STORAGE_KEY = 'myDigitalLibrary_v1';
const THEME_KEY = 'libraryTheme';

let books = [];
let currentFilter = 'all';
let currentPDF = null;
let currentBook = null;
let currentPage = 1;
let zoom = 1.2;
let renderTask = null;
let renderToken = 0;

function saveBooks() {
  try {
    localStorage.setItem(STORAGE_KEY,JSON.stringify(books));
  } catch(error) {
    toast('مساحة التخزين ممتلئة!','error');
  }
}

function loadBooks() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    books = saved ? JSON.parse(saved) : [];
    if(!Array.isArray(books)) books = [];
  } catch(error) {
    books = [];
  }

  renderBooks();
  updateStats();
}

/* =========================================
   3. الإشعارات
========================================= */
function toast(message,type='success') {
  const container = document.getElementById('toast-container');
  const element = document.createElement('div');

  element.className = 'toast';

  const icon = type === 'error'
    ? 'fa-circle-exclamation'
    : 'fa-circle-check';

  element.innerHTML =
    `<i class="fas ${icon}"></i><span></span>`;

  element.querySelector('span').textContent = message;
  container.appendChild(element);

  setTimeout(() => {
    element.style.opacity = '0';
    element.style.transform = 'translateX(-20px)';
    setTimeout(() => element.remove(),300);
  },3000);
}

/* =========================================
   4. الإحصائيات
========================================= */
function updateStats() {
  const totalViews = books.reduce((a,b)=>a+(Number(b.views)||0),0);
  const totalDownloads = books.reduce((a,b)=>a+(Number(b.downloads)||0),0);

  document.getElementById('statBooks').textContent = books.length;
  document.getElementById('statViews').textContent = totalViews;
  document.getElementById('statDownloads').textContent = totalDownloads;

  document.getElementById('heroBooks').textContent = books.length;
  document.getElementById('heroViews').textContent = totalViews;
  document.getElementById('heroDownloads').textContent = totalDownloads;
}

/* =========================================
   5. إنشاء بطاقات الكتب
========================================= */
function renderBooks() {
  const grid = document.getElementById('booksGrid');
  const search = document.getElementById('searchInput').value
    .trim().toLowerCase();

  let filtered = books.filter(book => {
    const matchesSearch =
      book.title.toLowerCase().includes(search) ||
      book.author.toLowerCase().includes(search);

    const matchesCategory =
      currentFilter === 'all' ||
      (currentFilter === 'favorite' && book.favorite) ||
      book.category === currentFilter;

    return matchesSearch && matchesCategory;
  });

  const sort = document.getElementById('sortSelect').value;

  if(sort === 'popular') filtered.sort((a,b)=>b.views-a.views);
  if(sort === 'downloads') filtered.sort((a,b)=>b.downloads-a.downloads);
  if(sort === 'rating') filtered.sort((a,b)=>b.rating-a.rating);
  if(sort === 'title') filtered.sort((a,b)=>a.title.localeCompare(b.title,'ar'));
  if(sort === 'new') filtered.sort((a,b)=>b.id-a.id);

  updateFilters();

  if(filtered.length === 0) {
    grid.innerHTML = `
      <div style="grid-column:1/-1;text-align:center;padding:60px 10px;color:var(--muted)">
        <i class="fas fa-book-open fa-3x"></i>
        <h3 style="margin-top:15px">لا توجد كتب هنا</h3>
        <p>حاول البحث بكلمات أخرى أو أضف كتاباً جديداً.</p>
      </div>`;
    return;
  }

  grid.innerHTML = '';

  filtered.forEach((book,index) => {
    const card = document.createElement('article');
    card.className = 'book-card';
    card.style.animationDelay = `${Math.min(index*.05,.5)}s`;

    const progress = book.lastPage && book.totalPages
      ? Math.round(book.lastPage/book.totalPages*100)
      : 0;

    card.innerHTML = `
      <div class="book-cover">
        ${book.coverUrl
          ? `<img src="${escapeHTML(book.coverUrl)}" alt="غلاف الكتاب" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='block'">`
          : ''}
        <i class="fas fa-book no-cover" style="${book.coverUrl?'display:none':''}"></i>
        <span class="book-category">${escapeHTML(book.category||'أخرى')}</span>
        <button class="favorite-btn ${book.favorite?'active':''}"
          onclick="toggleFavorite(${book.id})">
          <i class="fas fa-heart"></i>
        </button>
      </div>

      <div class="book-info">
        <h3 title="${escapeHTML(book.title)}">${escapeHTML(book.title)}</h3>
        <p class="author"><i class="fas fa-user"></i> ${escapeHTML(book.author)}</p>

        <div class="rating" aria-label="التقييم ${book.rating||0} من 5">
          ${createStars(book.rating||0)}
          <span style="color:var(--muted)">(${book.rating||0}/5)</span>
        </div>

        <div class="book-meta">
          <span><i class="fas fa-eye"></i> ${book.views||0}</span>
          <span><i class="fas fa-download"></i> ${book.downloads||0}</span>
        </div>

        <div class="read-progress">
          <div style="width:${progress}%"></div>
        </div>

        <div class="card-actions">
          <button class="card-btn read-btn" onclick="openReader(${book.id})">
            <i class="fas fa-book-reader"></i> قراءة
          </button>

          <button class="card-btn download-btn" onclick="downloadBook(${book.id})">
            <i class="fas fa-download"></i> تحميل
          </button>
        </div>

        <div style="display:flex;gap:7px;margin-top:9px">
          <button class="card-btn download-btn" style="flex:1"
            onclick="rateBook(${book.id})">
            <i class="fas fa-star"></i> تقييم
          </button>
          <button class="card-btn download-btn" style="flex:1"
            onclick="shareBook(${book.id})">
            <i class="fas fa-share-alt"></i> مشاركة
          </button>
          <button class="card-btn download-btn" style="flex:1"
            onclick="deleteBook(${book.id})">
            <i class="fas fa-trash"></i> حذف
          </button>
        </div>
      </div>
    `;

    grid.appendChild(card);
  });
}

/* حماية النصوص قبل وضعها في HTML */
function escapeHTML(value) {
  return String(value??'').replace(/[&<>"']/g,char=>({
    '&':'&amp;',
    '<':'&lt;',
    '>':'&gt;',
    '"':'&quot;',
    "'":'&#39;'
  })[char]);
}

function createStars(rating) {
  let output = '';
  for(let i=1;i<=5;i++) {
    output += `<i class="fa${i<=rating?'s':'r'} fa-star"></i>`;
  }
  return output;
}

/* =========================================
   6. التصنيفات
========================================= */
function updateFilters() {
  const container = document.getElementById('filters');
  const categories = [...new Set(books.map(b=>b.category||'أخرى'))];

  container.innerHTML = '';

  const all = [
    {name:'الكل',value:'all'},
    {name:'المفضلة ⭐',value:'favorite'},
    ...categories.map(c=>({name:c,value:c}))
  ];

  all.forEach(item=>{
    const button = document.createElement('button');
    button.className = `filter-btn ${currentFilter===item.value?'active':''}`;
    button.textContent = item.name;

    button.addEventListener('click',()=>{
      currentFilter = item.value;
      renderBooks();
    });

    container.appendChild(button);
  });
}

/* =========================================
   7. إضافة كتاب
========================================= */
function openAdmin() {
  document.getElementById('adminModal').classList.add('active');
}

function closeModal(id) {
  document.getElementById(id).classList.remove('active');
}

document.getElementById('bookForm').addEventListener('submit',function(e) {
  e.preventDefault();

  const title = document.getElementById('bookTitle').value.trim();
  const author = document.getElementById('bookAuthor').value.trim();
  const downloadUrl = document.getElementById('bookUrl').value.trim();
  const coverUrl = document.getElementById('bookCover').value.trim();
  const category = document.getElementById('bookCategory').value;

  if(!isValidURL(downloadUrl) || (coverUrl && !isValidURL(coverUrl))) {
    toast('يرجى إدخال روابط صحيحة','error');
    return;
  }

  books.push({
    id:Date.now(),
    title,
    author,
    downloadUrl,
    coverUrl,
    category,
    views:0,
    downloads:0,
    favorite:false,
    rating:0,
    lastPage:1,
    totalPages:0
  });

  saveBooks();
  renderBooks();
  updateStats();
  this.reset();

  closeModal('adminModal');
  toast('تمت إضافة الكتاب بنجاح 📚');
});

function isValidURL(value) {
  try {
    const url = new URL(value);
    return url.protocol === 'http:' || url.protocol === 'https:';
  } catch {
    return false;
  }
}

/* =========================================
   8. المفضلة والتقييم والحذف
========================================= */
function toggleFavorite(id) {
  const book = books.find(b=>b.id===id);
  if(!book) return;

  book.favorite = !book.favorite;
  saveBooks();
  renderBooks();
  toast(book.favorite?'أضيف إلى المفضلة ⭐':'تمت إزالته من المفضلة');
}

function rateBook(id) {
  const book = books.find(b=>b.id===id);
  if(!book) return;

  const value = prompt('أدخل تقييمك من 1 إلى 5:');
  if(value === null || value.trim()==='') return;

  const rating = Number(value);
  if(!Number.isInteger(rating)||rating<1||rating>5) {
    toast('التقييم يجب أن يكون من 1 إلى 5','error');
    return;
  }

  book.rating = rating;
  saveBooks();
  renderBooks();
  toast('شكراً على تقييمك ⭐');
}

function deleteBook(id) {
  const book = books.find(b=>b.id===id);
  if(!book) return;

  if(!confirm(`هل تريد حذف "${book.title}"؟`)) return;

  books = books.filter(b=>b.id!==id);
  saveBooks();
  renderBooks();
  updateStats();
  toast('تم حذف الكتاب');
}

/* =========================================
   9. تحميل الكتاب
========================================= */
function downloadBook(id) {
  const book = books.find(b=>b.id===id);
  if(!book) return;

  const link = document.createElement('a');
  link.href = book.downloadUrl;
  link.target = '_blank';
  link.rel = 'noopener noreferrer';
  link.download = '';
  document.body.appendChild(link);
  link.click();
  link.remove();

  book.downloads = (book.downloads||0)+1;
  saveBooks();
  updateStats();
  renderBooks();
  toast('تم طلب تحميل الكتاب');
}

/* =========================================
   10. مشاركة الكتاب
========================================= */
async function shareBook(id) {
  const book = books.find(b=>b.id===id);
  if(!book) return;

  const data = {
    title:book.title,
    text:`أنصحك بقراءة ${book.title} - ${book.author}`,
    url:book.downloadUrl
  };

  try {
    if(navigator.share) {
      await navigator.share(data);
    } else {
      await navigator.clipboard.writeText(
        `${data.text}\n${data.url}`
      );
      toast('تم نسخ رابط الكتاب');
    }
  } catch(error) {
    if(error.name!=='AbortError') {
      toast('تعذرت المشاركة','error');
    }
  }
}

/* =========================================
   11. قارئ PDF
========================================= */
async function openReader(id) {
  const book = books.find(b=>b.id===id);
  if(!book) return;

  currentBook = book;
  currentPDF = null;
  currentPage = Math.max(1,Number(book.lastPage)||1);
  zoom = 1.2;

  document.getElementById('readerTitle').textContent = book.title;
  document.getElementById('readerModal').classList.add('active');
  document.getElementById('readerLoading').style.display = 'block';
  document.getElementById('readerLoading').innerHTML =
    '<i class="fas fa-spinner fa-spin fa-2x"></i><p>جاري تحميل الكتاب...</p>';

  document.getElementById('pdfCanvas').hidden = true;

  book.views = (book.views||0)+1;
  saveBooks();
  updateStats();
  renderBooks();

  try {
    const task = pdfjsLib.getDocument({
      url:book.downloadUrl,
      withCredentials:false
    });

    currentPDF = await task.promise;

    if(currentBook!==book) return;

    book.totalPages = currentPDF.numPages;

    currentPage = Math.min(currentPage,currentPDF.numPages);

    document.getElementById('pageTotal').textContent =
      `/ ${currentPDF.numPages}`;

    document.getElementById('pageInput').max = currentPDF.numPages;

    saveBooks();
    await renderPDFPage();

  } catch(error) {
    console.error('PDF Error:',error);

    document.getElementById('readerLoading').innerHTML = `
      <div class="reader-error">
        <i class="fas fa-exclamation-triangle fa-3x"></i>
        <h3>تعذر فتح ملف PDF</h3>
        <p>تأكد من صحة الرابط وأن الموقع يسمح بقراءة الملف من موقع خارجي (CORS).</p>
        <button onclick="window.open(currentBook.downloadUrl,'_blank')"
          style="padding:12px 20px;background:#7057ef;color:white;border-radius:10px;margin-top:15px">
          فتح الملف مباشرة
        </button>
      </div>`;
  }
}

async function renderPDFPage() {
  if(!currentPDF) return;

  const token = ++renderToken;

  if(renderTask) {
    try { renderTask.cancel(); } catch(e) {}
    renderTask = null;
  }

  try {
    const page = await currentPDF.getPage(currentPage);

    if(token!==renderToken) return;

    const canvas = document.getElementById('pdfCanvas');
    const context = canvas.getContext('2d');

    const viewport = page.getViewport({scale:zoom});
    const ratio = window.devicePixelRatio || 1;

    canvas.width = Math.floor(viewport.width*ratio);
    canvas.height = Math.floor(viewport.height*ratio);

    canvas.style.width = `${viewport.width}px`;
    canvas.style.height = `${viewport.height}px`;

    context.setTransform(ratio,0,0,ratio,0,0);

    renderTask = page.render({
      canvasContext:context,
      viewport:viewport
    });

    await renderTask.promise;

    if(token!==renderToken) return;

    document.getElementById('readerLoading').style.display='none';
    canvas.hidden=false;

    document.getElementById('pageInput').value=currentPage;

    const percentage = currentPage/currentPDF.numPages*100;
    document.getElementById('readerProgress').style.width =
      `${percentage}%`;

    if(currentBook) {
      currentBook.lastPage=currentPage;
      currentBook.totalPages=currentPDF.numPages;
      saveBooks();
      renderBooks();
    }

  } catch(error) {
    if(error.name!=='RenderingCancelledException') {
      console.error(error);
    }
  }
}

function nextPage() {
  if(currentPDF && currentPage<currentPDF.numPages) {
    currentPage++;
    renderPDFPage();
  }
}

function previousPage() {
  if(currentPDF && currentPage>1) {
    currentPage--;
    renderPDFPage();
  }
}

function zoomIn() {
  zoom=Math.min(zoom+.2,3);
  renderPDFPage();
}

function zoomOut() {
  zoom=Math.max(zoom-.2,.5);
  renderPDFPage();
}

document.getElementById('pageInput').addEventListener('change',function() {
  if(!currentPDF) return;

  const value = Number(this.value);

  if(Number.isInteger(value)&&value>=1&&value<=currentPDF.numPages) {
    currentPage=value;
    renderPDFPage();
  } else {
    this.value=currentPage;
    toast('رقم الصفحة غير صحيح','error');
  }
});

function closeReader() {
  if(currentBook) {
    currentBook.lastPage=currentPage;
    saveBooks();
  }

  currentPDF=null;
  currentBook=null;
  renderToken++;

  if(renderTask) {
    try { renderTask.cancel(); } catch(e) {}
    renderTask=null;
  }

  document.getElementById('readerModal').classList.remove('active');
  document.exitFullscreen?.().catch(()=>{});
}

function toggleFullscreen() {
  const reader = document.querySelector('.reader-content');

  if(!document.fullscreenElement) {
    reader.requestFullscreen?.().catch(()=>{});
  } else {
    document.exitFullscreen?.().catch(()=>{});
  }
}

/* =========================================
   12. لوحة المفاتيح
========================================= */
document.addEventListener('keydown',function(e) {
  if(!document.getElementById('readerModal').classList.contains('active')) return;

  if(e.key==='ArrowLeft') nextPage();
  if(e.key==='ArrowRight') previousPage();
  if(e.key==='Escape') closeReader();
});

/* =========================================
   13. البحث والفلترة
========================================= */
document.getElementById('searchInput').addEventListener('input',renderBooks);
document.getElementById('sortSelect').addEventListener('change',renderBooks);

/* =========================================
   14. الوضع الليلي
========================================= */
const themeBtn = document.getElementById('themeBtn');

function applyTheme(theme) {
  document.body.classList.toggle('dark',theme==='dark');
  themeBtn.innerHTML = theme==='dark'
    ? '<i class="fas fa-sun"></i>'
    : '<i class="fas fa-moon"></i>';

  localStorage.setItem(THEME_KEY,theme);
}

themeBtn.addEventListener('click',()=>{
  const next = document.body.classList.contains('dark')
    ? 'light'
    : 'dark';

  applyTheme(next);
});

applyTheme(localStorage.getItem(THEME_KEY)||'light');

/* =========================================
   15. Scroll animations
========================================= */
const observer = new IntersectionObserver(entries=>{
  entries.forEach(entry=>{
    if(entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
},{threshold:.1});

document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));

/* =========================================
   16. إغلاق النوافذ عند الضغط خارجها
========================================= */
document.querySelectorAll('.modal').forEach(modal=>{
  modal.addEventListener('click',e=>{
    if(e.target===modal) {
      if(modal.id==='readerModal') closeReader();
      else modal.classList.remove('active');
    }
  });
});

/* =========================================
   17. تشغيل المكتبة
========================================= */
loadBooks();

</script>

</body>
</html>
