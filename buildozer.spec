[app]
title = Sentinel
package.name = sentinel
package.domain = com.sentinel.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk_version = 33
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET
android.release_artifact = aab
