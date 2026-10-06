[app]
title = SENTINEL
package.name = sentinel
package.domain = com.sentinel.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
main.filename = main.py

[buildozer]
log_level = 2

[app:android]
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
p4a.bootstrap = sdl2
android.accept_sdk_license_agreement = True
android.permissions = INTERNET
