# Add the fetched rows to today's file on the latest main and push. Starting from a fresh copy
# of main each try means a run never conflicts with another run's or the daily job's push.
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
for i in 1 2 3 4; do
  git fetch -q origin "$GITHUB_REF_NAME" && git reset -q --hard "origin/$GITHUB_REF_NAME" || { sleep $((i * 5)); continue; }
  python option_chain.py --apply
  git add data/option_chain
  git diff --cached --quiet && exit 0
  git commit -q -m "Option chain $(TZ=Asia/Kolkata date +%F-%H%M)"
  git push -q origin "HEAD:$GITHUB_REF_NAME" && exit 0
  sleep $((i * 5))
done
exit 1
