from flask import Flask, render_template, request, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

# =========================================================
# ⚠️ هنا فين غادي تحط مفاتيح Supabase ⚠️
# =========================================================
SUPABASE_URL = "https://vyqufwxcvidpbyicfxfy.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ5cXVmd3hjdmlkcGJ5aWNmeGZ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk4MjQwMDAsImV4cCI6MjAyNTQwMDAwMH0.xxxxx" # ✨ حط هنا الـ anon key اللي كيبدا بـ eyJ...

# تهيئة الاتصال بـ Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# =========================================================
# المسارات (Routes)
# =========================================================

# 1. الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# 2. جلب جميع الكتب من Supabase
@app.route('/api/books', methods=['GET'])
def get_books():
    try:
        response = supabase.table('books').select('*').order('id', desc=True).execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3. إضافة كتاب جديد
@app.route('/api/books', methods=['POST'])
def add_book():
    try:
        data = request.json
        # التحقق من البيانات
        if not data.get('title') or not data.get('author') or not data.get('downloadUrl'):
            return jsonify({"error": "Missing required fields"}), 400

        response = supabase.table('books').insert({
            "title": data['title'],
            "author": data['author'],
            "downloadUrl": data['downloadUrl'],
            "coverUrl": data.get('coverUrl', '')
        }).execute()
        return jsonify({"message": "Book added successfully", "data": response.data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 4. حذف كتاب
@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    try:
        response = supabase.table('books').delete().eq('id', id).execute()
        return jsonify({"message": "Book deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 5. تحديث الإحصائيات (مشاهدات / تحميلات)
@app.route('/api/books/<int:id>/stats', methods=['POST'])
def update_stats(id):
    try:
        data = request.json
        stat_name = data.get('stat') # 'views' أو 'downloads'
        
        if stat_name not in ['views', 'downloads']:
            return jsonify({"error": "Invalid stat"}), 400

        # جلب القيمة الحالية
        response = supabase.table('books').select(stat_name).eq('id', id).execute()
        if not response.data:
            return jsonify({"error": "Book not found"}), 404

        current_value = response.data[0].get(stat_name, 0) or 0
        new_value = current_value + 1

        # تحديث القيمة
        supabase.table('books').update({stat_name: new_value}).eq('id', id).execute()
        return jsonify({"message": "Stat updated", "new_value": new_value}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':

<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مكتبتي الرقمية | Flask + Supabase</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.11.338/pdf.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* نفس التصميم الزاهي اللي عطيتك قبيلة */
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
        :root {
            --primary: #6366f1; --secondary: #ec4899; --accent: #f59e0b;
            --success: #10b981; --danger: #ef4444;
            --bg-light: #f3f4f6; --text-light: #1f2937;
            --card-light: rgba(255, 255, 255, 0.9);
            --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
            --radius: 20px;
        }
        body.dark-mode {
            --bg-light: #111827; --text-light: #f9fafb;
            --card-light: rgba(31, 41, 55, 0.8);
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Cairo', sans-serif; transition: background-color 0.3s, color 0.3s; }
        body {
            background: linear-gradient(135deg, #e0e7ff 0%, #fce7f3 100%);
            color: var(--text-light); min-height: 100vh; display: flex; flex-direction: column; background-attachment: fixed;
        }
        body.dark-mode { background: linear-gradient(135deg, #1e1b4b 0%, #4c1d95 100%); }
        
        header {
            background: rgba(255, 255, 255, 0.25); backdrop-filter: blur(15px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.3); padding: 1rem 2rem;
            display: flex; justify-content: space-between; align-items: center;
            flex-wrap: wrap; gap: 1rem; position: sticky; top: 0; z-index: 100;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        }
        body.dark-mode header { background: rgba(0, 0, 0, 0.3); border-bottom: 1px solid rgba(255, 255, 255, 0.1); }
        header h1 {
            font-size: 1.8rem; font-weight: 900;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            display: flex; align-items: center; gap: 0.8rem;
        }
        .header-controls { display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; }
        .search-box { position: relative; }
        .search-box i { position: absolute; right: 15px; top: 50%; transform: translateY(-50%); color: var(--primary); font-size: 1.1rem; }
        #search-input {
            padding: 0.7rem 2.8rem 0.7rem 1.2rem; border-radius: 30px; border: 2px solid transparent;
            background: rgba(255, 255, 255, 0.8); width: 280px; font-size: 1rem; font-weight: 600;
            outline: none; transition: all 0.3s; box-shadow: var(--shadow);
        }
        #search-input:focus { border-color: var(--primary); background: white; transform: scale(1.02); }
        .btn {
            padding: 0.7rem 1.5rem; border-radius: 30px; font-size: 1rem; font-weight: 700;
            cursor: pointer; border: none; display: inline-flex; align-items: center;
            gap: 0.5rem; transition: all 0.3s; text-decoration: none; box-shadow: var(--shadow);
        }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 15px 30px -5px rgba(0, 0, 0, 0.2); }
        #theme-toggle { background: var(--accent); color: white; width: 45px; height: 45px; padding: 0; justify-content: center; border-radius: 50%; }
        #admin-toggle { background: linear-gradient(to right, var(--secondary), var(--primary)); color: white; }
        
        .books-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 2.5rem; padding: 3rem 2rem; max-width: 1400px; margin: 0 auto; width: 100%; }
        .book-card {
            background: var(--card-light); backdrop-filter: blur(10px); border-radius: var(--radius);
            box-shadow: var(--shadow); padding: 1.5rem; text-align: center; display: flex;
            flex-direction: column; justify-content: space-between; border: 1px solid rgba(255, 255, 255, 0.5);
            transition: all 0.4s ease; position: relative; overflow: hidden;
        }
        .book-card::before {
            content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 5px;
            background: linear-gradient(to right, var(--primary), var(--secondary)); opacity: 0; transition: opacity 0.3s;
        }
        .book-card:hover { transform: translateY(-10px) scale(1.02); box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.2); }
        .book-card:hover::before { opacity: 1; }
        .book-cover {
            width: 100%; height: 220px; border-radius: 15px; margin-bottom: 1.2rem;
            background: linear-gradient(135deg, #e0e7ff, #fce7f3); display: flex; align-items: center;
            justify-content: center; font-size: 4rem; color: var(--primary); overflow: hidden;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        .book-cover img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
        .book-card:hover .book-cover img { transform: scale(1.1); }
        .book-card h3 { font-size: 1.3rem; font-weight: 700; color: var(--text-light); margin-bottom: 0.5rem; min-height: 60px; display: flex; align-items: center; justify-content: center; }
        body.dark-mode .book-card h3 { color: var(--text-light); }
        .book-card p { color: #6b7280; font-size: 0.95rem; margin-bottom: 0.8rem; font-weight: 600; }
        .stats { display: flex; justify-content: center; gap: 1.5rem; margin: 0.8rem 0; font-size: 0.9rem; color: var(--text-light); font-weight: 700; background: rgba(0,0,0,0.05); padding: 0.5rem; border-radius: 10px; }
        body.dark-mode .stats { color: var(--text-light); background: rgba(255,255,255,0.1); }
        .stats span { display: flex; align-items: center; gap: 0.3rem; }
        .card-actions { display: flex; gap: 0.8rem; flex-wrap: wrap; margin-top: 1rem; }
        .btn-read { background: var(--primary); color: white; flex: 1; justify-content: center; font-size: 0.95rem; }
        .btn-download { background: var(--success); color: white; flex: 1; justify-content: center; font-size: 0.95rem; }
        .btn-delete { background: transparent; color: var(--danger); width: 100%; justify-content: center; margin-top: 0.8rem; font-size: 0.85rem; padding: 0.4rem; border: 2px solid var(--danger); }
        .btn-delete:hover { background: var(--danger); color: white; }
        
        #reader-screen { display: none; flex-direction: column; min-height: 100vh; background: #1f2937; }
        .reader-header { background: rgba(0, 0, 0, 0.8); backdrop-filter: blur(10px); padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; color: white; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
        #back-btn { background: var(--danger); color: white; }
        #reader-title { font-size: 1.3rem; font-weight: 700; color: var(--accent); }
        #reader-content { flex-grow: 1; display: flex; flex-direction: column; align-items: center; padding: 2rem; overflow-y: auto; }
        #pdf-canvas { background: white; box-shadow: 0 20px 50px rgba(0,0,0,0.5); max-width: 100%; height: auto; border-radius: 8px; }
        #pdf-controls { margin-top: 2rem; display: flex; gap: 1.5rem; align-items: center; font-size: 1.1rem; color: white; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 0.8rem 2rem; border-radius: 40px; border: 1px solid rgba(255,255,255,0.2); }
        #pdf-controls button { background: var(--primary); color: white; border-radius: 20px; font-size: 1rem; padding: 0.5rem 1.5rem; }
        #pdf-controls button:disabled { background: #4b5563; cursor: not-allowed; opacity: 0.5; }
        
        .modal-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(5px); z-index: 1000; justify-content: center; align-items: center; }
        .modal-content { background: white; padding: 2.5rem; border-radius: 25px; width: 90%; max-width: 500px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25); animation: slideUp 0.4s ease; }
        @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
        .modal-content h2 { margin-bottom: 1.5rem; color: var(--text-light); font-size: 1.5rem; text-align: center; background: linear-gradient(to right, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .form-group { margin-bottom: 1.2rem; }
        .form-group label { display: block; margin-bottom: 0.5rem; font-weight: 700; font-size: 0.95rem; color: var(--text-light); }
        .form-group input { width: 100%; padding: 0.8rem 1rem; border-radius: 12px; border: 2px solid #e5e7eb; background: #f9fafb; color: var(--text-light); font-size: 1rem; font-family: 'Cairo', sans-serif; transition: border-color 0.3s; }
        .form-group input:focus { border-color: var(--primary); outline: none; }
        .form-actions { display: flex; gap: 1rem; margin-top: 2rem; }
        .form-actions button { flex: 1; justify-content: center; padding: 0.8rem; font-size: 1rem; }
        .btn-save { background: linear-gradient(to right, var(--success), #059669); color: white; }
        .btn-cancel { background: #e5e7eb; color: var(--text-light); }
        
        @media (max-width: 768px) {
            header { flex-direction: column; padding: 1rem; }
            .header-controls { width: 100%; justify-content: center; }
            #search-input { width: 100%; }
            .books-grid { grid-template-columns: 1fr; padding: 1.5rem; }
            .reader-header { flex-direction: column; gap: 1rem; }
            #pdf-controls { flex-direction: column; gap: 0.5rem; }
        }
    </style>
</head>
<body>

    <div id="home-screen">
        <header>
            <h1><i class="fas fa-book-open"></i> مكتبتي الرقمية</h1>
            <div class="header-controls">
                <div class="search-box">
                    <i class="fas fa-search"></i>
                    <input type="text" id="search-input" placeholder="ابحث عن كتاب أو مؤلف...">
                </div>
                <button id="theme-toggle" class="btn"><i class="fas fa-moon"></i></button>
                <button id="admin-toggle" class="btn"><i class="fas fa-user-shield"></i> لوحة التحكم</button>
            </div>
        </header>
        <div id="books-container" class="books-grid"></div>
    </div>

    <div id="reader-screen">
        <div class="reader-header">
            <button id="back-btn" class="btn"><i class="fas fa-arrow-right"></i> رجوع</button>
            <h2 id="reader-title">عنوان الكتاب</h2>
            <a id="download-link" href="#" target="_blank" class="btn btn-download" download><i class="fas fa-download"></i> تحميل</a>
        </div>
        <div id="reader-content">
            <canvas id="pdf-canvas"></canvas>
            <div id="pdf-controls">
                <button id="prev-page" class="btn"><i class="fas fa-chevron-right"></i> السابق</button>
                <span>صفحة <span id="page-num">1</span> من <span id="page-count">--</span></span>
                <button id="next-page" class="btn">التالي <i class="fas fa-chevron-left"></i></button>
            </div>
        </div>
    </div>

    <div id="admin-modal" class="modal-overlay">
        <div class="modal-content">
            <h2><i class="fas fa-plus-circle"></i> إضافة كتاب جديد</h2>
            <div class="form-group"><label>عنوان الكتاب</label><input type="text" id="new-title" placeholder="عنوان الكتاب"></div>
            <div class="form-group"><label>اسم المؤلف</label><input type="text" id="new-author" placeholder="اسم المؤلف"></div>
            <div class="form-group"><label>رابط التحميل (Direct Link)</label><input type="text" id="new-url" placeholder="https://drive.google.com/uc?export=download&id=..."></div>
            <div class="form-group"><label>رابط صورة الغلاف (اختياري)</label><input type="text" id="new-cover" placeholder="https://..."></div>
            <div class="form-actions">
                <button id="save-book" class="btn btn-save"><i class="fas fa-save"></i> حفظ</button>
                <button id="cancel-admin" class="btn btn-cancel">إلغاء</button>
            </div>
        </div>
    </div>

    <script>
        // ==================== المتغيرات ====================
        let allBooks = [];
        let currentBook = null;
        let pdfDoc = null;
        let pageNum = 1;
        let pageRendering = false;
        let pageNumPending = null;
        const scale = 1.5;
        const canvas = document.getElementById('pdf-canvas');
        const ctx = canvas.getContext('2d');

        // ==================== دوال الـ API (Flask) ====================
        async function fetchBooks() {
            try {
                const response = await fetch('/api/books');
                allBooks = await response.json();
                displayBooks(allBooks);
            } catch (error) {
                console.error('خطأ في جلب الكتب:', error);
                document.getElementById('books-container').innerHTML = '<p>تعذر الاتصال بالسيرفر.</p>';
            }
        }

        async function addBookToServer(book) {
            try {
                const response = await fetch('/api/books', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(book)
                });
                if (response.ok) {
                    fetchBooks();
                    alert('✅ تزاد الكتاب بنجاح!');
                }
            } catch (error) {
                alert('❌ وقع خطأ فـ الإضافة.');
            }
        }

        async function deleteBookFromServer(id) {
            try {
                await fetch(`/api/books/${id}`, { method: 'DELETE' });
                fetchBooks();
            } catch (error) {
                console.error('خطأ في الحذف');
            }
        }

        async function incrementStat(id, statName) {
            try {
                await fetch(`/api/books/${id}/stats`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ stat: statName })
                });
                const localBook = allBooks.find(b => b.id === id);
                if (localBook) localBook[statName] = (localBook[statName] || 0) + 1;
            } catch (error) {
                console.error('خطأ في تحديث الإحصائيات');
            }
        }

        // ==================== الواجهة ====================
        function displayBooks(books) {
            const container = document.getElementById('books-container');
            container.innerHTML = ''; 
            if (books.length === 0) {
                container.innerHTML = '<p style="text-align:center; width:100%; font-size:1.2rem; font-weight:700; color:var(--primary);">مكتبتك خاوية. زيد كتب من لوحة التحكم!</p>';
                return;
            }
            books.forEach(book => {
                const bookCard = document.createElement('div');
                bookCard.className = 'book-card';
                
                let coverHtml = `<div class="book-cover"><i class="fas fa-book"></i></div>`;
                if (book.coverUrl) {
                    coverHtml = `<div class="book-cover"><img src="${book.coverUrl}" alt="${book.title}" onerror="this.style.display='none'; this.parentElement.innerHTML='<i class=\\'fas fa-book\\'></i>';"></div>`;
                }

                const views = book.views || 0;
                const downloads = book.downloads || 0;

                bookCard.innerHTML = `
                    ${coverHtml}
                    <h3>${book.title}</h3>
                    <p>${book.author}</p>
                    <div class="stats">
                        <span><i class="fas fa-eye" style="color:var(--primary);"></i> ${views}</span>
                        <span><i class="fas fa-download" style="color:var(--success);"></i> ${downloads}</span>
                    </div>
                    <div class="card-actions">
                        <button class="btn btn-read" onclick="readBook(${book.id})"><i class="fas fa-book-reader"></i> قراءة</button>
                        <a href="${book.downloadUrl}" target="_blank" class="btn btn-download" onclick="incrementStat(${book.id}, 'downloads')" download><i class="fas fa-download"></i> تحميل</a>
                    </div>
                    <button class="btn btn-delete" onclick="confirmDelete(${book.id})"><i class="fas fa-trash"></i> حذف</button>
                `;
                container.appendChild(bookCard);
            });
        }

        function confirmDelete(id) {
            if (confirm("واش نتا متأكد باغي تحذف هاد الكتاب؟")) {
                deleteBookFromServer(id);
            }
        }

        // ==================== القارئ (PDF) ====================
        function readBook(id) {
            const book = allBooks.find(b => b.id === id);
            if (!book) return;
            if (!book.downloadUrl) {
                alert('⚠️ رابط التحميل غير متوفر.');
                return;
            }
            incrementStat(id, 'views');

            currentBook = book;
            document.getElementById('home-screen').style.display = 'none';
            document.getElementById('reader-screen').style.display = 'flex';
            document.getElementById('reader-title').textContent = book.title;
            document.getElementById('download-link').href = book.downloadUrl;
            document.getElementById('download-link').download = book.title + '.pdf';
            loadPdf(book.downloadUrl);
        }

        function loadPdf(url) {
            pdfjsLib.getDocument(url).promise.then(function(pdfDoc_) {
                pdfDoc = pdfDoc_;
                document.getElementById('page-count').textContent = pdfDoc.numPages;
                pageNum = 1;
                renderPage(pageNum);
            }).catch(function(error) {
                console.error("خطأ:", error);
                alert('❌ ما قدرناش نقراو الملف. تأكد من أن الملف عام (Public) وأن الرابط صحيح.');
            });
        }

        function renderPage(num) {
            pageRendering = true;
            pdfDoc.getPage(num).then(function(page) {
                const viewport = page.getViewport({ scale: scale });
                canvas.height = viewport.height;
                canvas.width = viewport.width;
                const renderContext = { canvasContext: ctx, viewport: viewport };
                const renderTask = page.render(renderContext);
                renderTask.promise.then(function() {
                    pageRendering = false;
                    if (pageNumPending !== null) { renderPage(pageNumPending); pageNumPending = null; }
                });
            });
            document.getElementById('page-num').textContent = num;
            updateButtons();
        }

        function updateButtons() {
            document.getElementById('prev-page').disabled = (pageNum <= 1);
            document.getElementById('next-page').disabled = (pageNum >= pdfDoc.numPages);
        }

        function queueRenderPage(num) {
            if (pageRendering) { pageNumPending = num; } else { renderPage(num); }
        }

        // ==================== الأحداث ====================
        document.getElementById('prev-page').addEventListener('click', () => { if (pageNum > 1) { pageNum--; queueRenderPage(pageNum); } });
        document.getElementById('next-page').addEventListener('click', () => { if (pageNum < pdfDoc.numPages) { pageNum++; queueRenderPage(pageNum); } });
        document.getElementById('back-btn').addEventListener('click', () => {
            document.getElementById('reader-screen').style.display = 'none';
            document.getElementById('home-screen').style.display = 'block';
            currentBook = null; pdfDoc = null; pageNum = 1;
            fetchBooks();
        });

        document.getElementById('search-input').addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            const filtered = allBooks.filter(book => book.title.toLowerCase().includes(term) || book.author.toLowerCase().includes(term));
            displayBooks(filtered);
        });

        const themeToggle = document.getElementById('theme-toggle');
        if (localStorage.getItem('theme') === 'dark') {
            document.body.classList.add('dark-mode');
            themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
        }
        themeToggle.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            const isDark = document.body.classList.contains('dark-mode');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            themeToggle.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        });

        const adminModal = document.getElementById('admin-modal');
        document.getElementById('admin-toggle').addEventListener('click', () => adminModal.style.display = 'flex');
        document.getElementById('cancel-admin').addEventListener('click', () => adminModal.style.display = 'none');

        document.getElementById('save-book').addEventListener('click', () => {
            const title = document.getElementById('new-title').value;
            const author = document.getElementById('new-author').value;
            const url = document.getElementById('new-url').value;
            const cover = document.getElementById('new-cover').value;

            if (!title || !author || !url) { alert('عافاك عمر الخانات الأساسية.'); return; }

            const newBook = { title, author, downloadUrl: url, coverUrl: cover };
            addBookToServer(newBook);

            document.getElementById('new-title').value = '';
            document.getElementById('new-author').value = '';
            document.getElementById('new-url').value = '';
            document.getElementById('new-cover').value = '';
            adminModal.style.display = 'none';
        });

        // بدء التطبيق
        fetchBooks();
    </script>
</body>
</html>
    app.run(debug=True)
