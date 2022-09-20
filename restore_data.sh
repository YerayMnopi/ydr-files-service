#!/bin/bash

export PGPASSWORD="password"
echo "DROP AND CREATE DATABASES" >> log.txt
psql -h localhost -p 5433 -U user -f ./create-databases.sql >> log.txt
#psql -h 165.22.121.147 -p 5432 -U user -f ./create-databases.sql >> log.txt
#psql -h yeraydiaz.ddns.net -p 3441 -U user -f ./create-databases.sql >> log.txt
