#!/usr/bin/env sh

rm -rf Acre/Acre_test_lmdb

./python/LMDB_write_test.py

rm -rf Acre/Acre_train_lmdb

./python/LMDB_write_train.py
