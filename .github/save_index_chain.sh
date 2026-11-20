# Like save_sensex_chain.sh for any index sensex_chain.py reads: bash .github/save_index_chain.sh banknifty
set -u
export CHAIN_INDEX="$1"
DIR="data/${1}_chain"
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
for i in 1 2 3 4; do
  git fetch -q origin "$GITHUB_REF_NAME" && git reset -q --hard "origin/$GITHUB_REF_NAME" || { sleep $((i * 5)); continue; }
  python sensex_chain.py --apply
  if [ -d "$DIR" ]; then git add "$DIR"; fi
  git diff --cached --quiet && exit 0
  git commit -q -m "$1 chain $(TZ=Asia/Kolkata date +%F-%H%M)"
  git push -q origin "HEAD:$GITHUB_REF_NAME" && exit 0
  sleep $((i * 5))
done
exit 1
