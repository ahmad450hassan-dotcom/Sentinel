[app]
title = Sentinel
package.name = sentinel
package.domain = org.sentinel.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy==2.3.0,kivymd,pillow,requests,urllib3,chardet,certifi,idna
orientation = portrait

[buildozer]
log_level = 2

# Android
p4a.bootstrap = sdl2
p4a.port = 5000
android.permissions = INTERNET,CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.ant = auto
android.archs = arm64-v8a, armeabi-v7a

[app:android.permissions]
android.permission.INTERNET =
android.permission.CAMERA =

# iOS skip karo
