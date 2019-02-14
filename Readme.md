# Automation Tool Support
- Use the [dragon-cli](https://github.com/StrayDragon/dragon-cli) to manage this repo.
```bash
# need to run:
# 'hexo clean'
# 'hexo g -d'
# 'hexo clean'
dragon blog publish
 
# need to run:
# 'git add -A'
# 'git commit -m "update blog"'
# 'git push'
dragon blog finish
```

# Migration Guide

```bash
git pull <this repo>

# Some changes
git add -A
git commit -m "sync hexo"
git push origin hexo

# Depoly 
hexo clean 
hexo d -g
```
