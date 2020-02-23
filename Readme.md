# My Blog
[![Build Status](https://travis-ci.org/StrayDragon/straydragon.github.io.svg?branch=hexo)](https://travis-ci.org/StrayDragon/straydragon.github.io)

--- 
Record my coding experience and life... QAQ

# Automation Tool Support \[WIP\]
- Use the [tweedle](https://github.com/StrayDragon/tweedle) to manage this repo.

```bash
# need to run:
# 'hexo clean'
# 'hexo g -d'
# 'hexo clean'
tweedle blog publish
 
# need to run:
# 'git add -A'
# 'git commit -m "update blog"'
# 'git push'
tweedle blog finish
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
