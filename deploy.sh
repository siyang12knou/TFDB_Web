#! /bin/bash
cd ../tfdb_ui
flutter build web --release
rm -rf ../tfdb_web/tfdb/*
cp -r build/web/* ../tfdb_web/tfdb
