# Add this at the bottom or near the AUTH section
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # ✅ Set to False in production

# ✅ Security Headers
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# ✅ Cookie Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ✅ Recommended Additional (if using HTTPS and custom domains)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
