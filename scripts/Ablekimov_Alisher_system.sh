#!/bin/bash
# Shows student information and basic system information

LINE="=============================="
INFO_FILE="$(dirname "$0")/../Ablekimov_Alisher_info.txt"

echo "$LINE"
echo "Student Information"
echo "$LINE"
echo
echo "Name: Alisher"
echo "Surname: Ablekimov"
echo "Group: IT2-2312"
echo "Student ID: 37637"
echo
echo "$LINE"
echo "System Information"
echo "$LINE"
echo
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(grep PRETTY_NAME /etc/os-release | cut -d '"' -f 2), kernel $(uname -r)"
echo "Disk Usage:"
df -h /
echo "Memory Usage:"
free -h
echo

# check that the student information file is in the project folder
if [ -f "$INFO_FILE" ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
