# 🤝 Contributing to RepoSmith | المساهمة في مشروع RepoSmith

شكراً لاهتمامك بالمساهمة! 🚀  
RepoSmith هو مشروع مفتوح المصدر (Python CLI) يساعدك على إنشاء مشاريع جديدة بسرعة.  
هذا المستند يشرح كيف تجهّز بيئة التطوير، وكيفية كتابة الكود، وإرسال مساهماتك.

---

## 🛠️ Development Setup | إعداد بيئة التطوير

1. **Clone the repo | استنسخ المستودع**
   ```bash
   git clone https://github.com/liebemama/RepoSmith.git
   cd RepoSmith
   ```

2. **Create a virtual environment | أنشئ بيئة افتراضية**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. **Install requirements (dev) | ثبّت المتطلبات**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests | شغّل الاختبارات**
   ```bash
   python -m unittest discover -s tests -v
   ```

---

## 📏 Code Style | أسلوب كتابة الكود

- Use **PEP8** for formatting. | استخدم معايير **PEP8** للتنسيق.
- Keep functions small with clear docstrings. | اجعل الدوال قصيرة وبها توثيق واضح.
- Use **atomic writes + backups** when writing files. | استخدم أسلوب الكتابة الآمنة مع النسخ الاحتياطي.
- Add type hints where possible. | أضف تلميحات الأنواع إن أمكن.

Recommended tools | أدوات مقترحة:
```bash
pip install black ruff
black reposmith/ tests/
ruff check reposmith/ tests/
```

---

## 🧪 Tests | الاختبارات

- All new features must include unit tests. | كل ميزة جديدة يجب أن يكون لها اختبارات.
- Run tests locally before submitting. | شغّل الاختبارات محليًا قبل إرسال التعديلات.
- CI (GitHub Actions) runs automatically. | نظام CI يعمل تلقائيًا لكل Pull Request.

---

## 🔄 Submitting Changes | إرسال التغييرات

1. **Fork and branch | أنشئ Fork وفرع جديد**
   ```bash
   git checkout -b feature/my-new-feature
   ```

2. **Commit with clear message | احفظ التغييرات برسالة واضحة**
   ```bash
   git commit -m "Add: support for --with-django gitignore preset"
   ```

3. **Push to your fork | ارفع التغييرات إلى Fork الخاص بك**
   ```bash
   git push origin feature/my-new-feature
   ```

4. **Open Pull Request | افتح طلب دمج (PR) إلى الفرع main**

---

## 💡 Feature Requests & Issues | طلبات الميزات والمشاكل

- Use GitHub Issues for bugs/features. | استخدم GitHub Issues للإبلاغ عن الأخطاء أو اقتراح الميزات.
- Provide steps to reproduce bugs. | اذكر خطوات إعادة إنتاج الخطأ.

---

## 📜 License | الرخصة

By contributing, you agree that your code will be licensed under the [MIT License](LICENSE).  
بالمساهمة، فأنت توافق أن يكون كودك مرخّص تحت [رخصة MIT](LICENSE).

---

💖 Thanks for making RepoSmith better! | شكراً لمساعدتك في تحسين RepoSmith!
