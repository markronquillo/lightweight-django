import sys

from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='b0mqvak1p2sqm6p#_8o8fxf+ox(le)8&jh_5^sxa!=7!+wsj0',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        # this is deprecated in 1.8+ version
        # 'django.contrib.webdesign',
        'sitebuilder'
    ),
    STATIC_URL='/static/',
)


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
