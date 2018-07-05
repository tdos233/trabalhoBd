#!/usr/bin/env bash

# run the voltdb server locally
function server() {
    
    sudo bash -c "echo never > /sys/kernel/mm/transparent_hugepage/enabled"
    sudo bash -c "echo never > /sys/kernel/mm/transparent_hugepage/defrag"
    python2.7 ../voltdb/bin/voltdb init
    python2.7 ../voltdb/bin/voltdb start
}
function serverCInit() {
    
    sudo bash -c "echo never > /sys/kernel/mm/transparent_hugepage/enabled"
    sudo bash -c "echo never > /sys/kernel/mm/transparent_hugepage/defrag"
    #python2.7 ../voltdb/bin/voltdb init
    python2.7 ../voltdb/bin/voltdb start
}

# load schema and procedures
function init() {
   
    ../voltdb/bin/sqlcmd < tabela.sql
}

# run the client that drives the example
function client() {
    
    #../voltdb/bin/sqlcmd < tabela.sql
    python2.7 Read.py
}

function help() {
    echo "Usage: ./run.sh {clean|init|client|server}"
}

# Run the target passed as the first arg on the command line
# If no first arg, run server
if [ $# -gt 1 ]; then help; exit; fi
if [ $# = 1 ]; then $1; else server; fi
