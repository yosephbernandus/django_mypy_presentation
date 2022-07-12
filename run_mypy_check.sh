export DIFF_FILES=$(git diff --name-only --diff-filter=ACM $(git merge-base HEAD origin/master) | grep "\.py" | grep -v "settings" | grep -v "migrations")
if [[ ! -z $DIFF_FILES ]]
then
  echo "[MYPY] Checking ..." $DIFF_FILES
  mypy $DIFF_FILES --ignore-missing-imports --disallow-untyped-defs --follow-imports silent
  flake8 --exclude migrations,libraries,.coveragerc,settings.py,*.yml,*.txt,*.html,*.js,*.css,*.ini,*.scss,*.md,mortgage.py,yarn.lock,package.json --ignore=E501,W503 $DIFF_FILES;
fi
