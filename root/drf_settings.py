REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'shared.paginations.CustomPageNumberPagination',
    # 'PAGE_SIZE': 25
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Avto_Elon_Uz',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    "SWAGGER_UI_SETTINGS": {
        "persistAuthorization": True,  # Autorizatsiyani saqlash
    },
    "SECURITY": [
        {
            "apiKeyAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        },
    ],
    # OTHER SETTINGS
}
