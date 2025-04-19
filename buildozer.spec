[app]

# (str) Title of your application
title = MonAppKivyMD

# (str) Package name
package.name = monapp

# (str) Package domain (must be unique)
package.domain = org.rayane.kivymd

# (str) Source code where main.py is located
source.dir = .

# (str) The main .py file
source.main = main.py

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Icon of the application
icon = icons/icon.png

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 24

# (str) Android NDK version to use
android.ndk = 23b

# (bool) Use --private data storage (true) or --dir public storage (false)
android.private_storage = true

# (bool) Android logcat filters
log_level = 2

# (list) Android requirements (comma separated)
# Add kivymd and its dependencies
requirements = python3,kivy,kivymd

# (str) Presplash screen used before loading kivy
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Path to a custom .java file (if any)
# android.add_src =

# (list) Additional Java .jar files to add to the libs
# android.add_jars =

# (list) Android aars to include
# android.add_aars =

# (list) Assets to include (image, fonts, etc.)
android.add_assets = assets/fonts/,assets/images/

# (str) Entry point for your application
entrypoint = main.py

# (str) Supported screens
android.supported_screens = small, normal, large, xlarge

# (str) Application versioning
version = 0.1

# (str) Android app version code
android.version_code = 1

# (str) Android app version name
android.version_name = 0.1

# (str) Application metadata to pass to the AndroidManifest.xml
# android.meta_data =

# (str) Android theme (e.g. 'android:Theme.Material', 'android:Theme.Holo.Light')
android.theme = @android:style/Theme.Material.NoActionBar

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (bool) Use the Kivy launcher (only for debugging)
# kivy.launcher = 0

# (list) Patterns to whitelist for the whole project
android.whitelist = assets/*, icons/*

# (list) Java classes to add to the manifest
# android.add_classes =

# (list) Gradle dependencies
# android.gradle_dependencies =

# (str) Path to a custom AndroidManifest.xml
# android.manifest =

# (str) Custom Java package folder
# android.java_src =

# (bool) Include Android native service
# android.add_service =

# (str) Custom build.gradle file
# android.gradle_file =

# (list) Requirements for python-for-android
# p4a.whitelist =

# (str) Custom bootstrap to use
# android.bootstrap = sdl2

# (str) Path to a custom keystore for release
# android.release_keyalias = mykey
# android.release_keystore = my-release-key.keystore

# (bool) Sign release APK
android.release = 0

# (str) Directory in which python-for-android should store its cache
# p4a.local_recipes =

# (list) Additional dirs to include in site-packages
# p4a.extra_packages_dir =

# (str) Wheel directory path
# p4a.wheel_dir =

# (str) Custom logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) Copy project resources to `.buildozer/android/platform/build-armeabi-v7a/dists`
# android.copy_resources = 1
