SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'ydr_files_db';
DROP DATABASE IF EXISTS ydr_files_db;
create database ydr_files_db;
