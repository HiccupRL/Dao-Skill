# 来源索引

当前仓库只提交抓取与索引流程，不默认提交大体量抓取产物。

运行以下命令后，本文件会被 `scripts/build_references.py` 按 `data/corpus/all.json` 自动更新：

```bash
python scripts/scraper.py --config config/sources.yaml --out data/corpus
python scripts/build_references.py --data data/corpus --out references
```
