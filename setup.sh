# Get the output of the "whoami" command and store it in a variable
whoami_output=$(whoami)

# Get the contents of the "whoami" file and store it in a variable
whoami_file=$(cat whoami)

# Compare the two variables using an if-else statement
if [ "$whoami_output" = "$whoami_file" ]; then
  python Setup.py
else
  echo "SORRY , YOU DIDN'T PURCHASED THIS TOOL"
fi
