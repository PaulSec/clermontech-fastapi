#!/bin/bash
rm sql_app.db
sqlite3 sql_app.db < dump.sql
