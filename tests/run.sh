EXIT_STATUS=0

echo "Running unit tests..."
pytest ../tests|| EXIT_STATUS=$?
echo "\n"

echo "Running flake8..."
flake8 ../tests|| EXIT_STATUS=$?
flake8 ../mycat|| EXIT_STATUS=$?
echo "\n"

echo "Running mypy..."
mypy ../tests|| EXIT_STATUS=$?
mypy ../mycat|| EXIT_STATUS=$?
echo "\n"

echo "Exit status code $EXIT_STATUS!" 
exit $EXIT_STATUS
