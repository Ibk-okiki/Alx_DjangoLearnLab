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
# --- HTTPS Redirects and Security ---
# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# --- Secure Cookies ---
# Ensures cookies are only sent via HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# --- Secure Headers ---
# Prevent clickjacking
X_FRAME_OPTIONS = 'DENY'

# Prevent content type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser XSS filter
SECURE_BROWSER_XSS_FILTER = True

# Enforce HTTPS and Secure Redirects
SECURE_SSL_REDIRECT = True  # Redirect all non-HTTPS requests to HTTPS

# Set HSTS headers to enforce HTTPS in browser
SECURE_HSTS_SECONDS = 31536000  # One year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Secure headers
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# Trust the X-Forwarded-Proto header set by your proxy (e.g., Heroku, Nginx)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



