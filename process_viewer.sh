#!/bin/bash

echo "Listing all running processes at system bootup..."

while true; do
    ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
    sleep 5
done
