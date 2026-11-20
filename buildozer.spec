[app]
title = Интерактивная книга рецептов
package.name = recipebook
package.domain = org.interactive
source.dir = .
source.include_exts = py,json,png
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 28c
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
android.permissions =
