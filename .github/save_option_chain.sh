# Commit and push today's option chain file; the daily data run may push at the same time, so retry.
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add data/option_chain
git diff --cached --quiet && exit 0
git commit -m "Option chain $(TZ=Asia/Kolkata date +%F-%H%M)"
for i in 1 2 3 4; do
  git pull --rebase origin "$GITHUB_REF_NAME" && git push && exit 0
  sleep $((i * 5))
done
exit 1
