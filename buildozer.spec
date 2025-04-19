[app]

# (str) Title of your application
title = APP

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,https://github.com/kivymd/KivyMD/archive/master.zip,materialyoucolor,exceptiongroup,asyncgui,asynckivy,pillow

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions (ajoute INTERNET pour utiliser l'async)
android.permissions = INTERNET

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android NDK API to use
android.ndk_api = 21

# (str) Android NDK version to use
android.ndk = 23b

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) Format to package the app for debug mode
android.debug_artifact = apk

# (str) Format to package the app for release mode
android.release_artifact = aab


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1


# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#[app]
#source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
#
#    This can be translated into:
#
#[app:source.exclude_patterns]
#license
#data/audio/*.wav
#data/images/original/*
#


#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, you want to deploy a demo version of your application without
#    HD content. You could first change the title to add "(demo)" in the name
#    and extend the excluded directories to remove the HD content.
#
#[app@demo]
#title = My Application (demo)
#
#[app:source.exclude_patterns@demo]
#images/hd/*
#
#    Then, invoke the command line with the "demo" profile:
#
#buildozer --profile demo android debug
