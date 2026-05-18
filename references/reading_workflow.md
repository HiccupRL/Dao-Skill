# 阅读与回答流程

## 1. 明确问题类型

- 原文释义：先定位单一文本，再解释词句。
- 主题综述：先按关键词查多篇，再按材料组归纳。
- 三家比较：分别抽取毛泽东、王阳明、曾国藩材料，再比较问题意识、方法论和局限。
- 写作辅助：先列原典证据，再写现代转化，不要先写观点后补材料。

## 2. 检索命令

```bash
python scripts/retrieve.py "现实问题或比较问题" --require-collections all --top-k 12
python scripts/search.py "实践" "调查" --collection maozedong
python scripts/search.py "知行合一" "良知" --collection wang_yangming
python scripts/search.py "自强" "戒傲" "勤" --collection zeng_guofan
```

Windows / PowerShell 可用 `powershell -ExecutionPolicy Bypass -File references/search_corpus.ps1 ...`；类 Unix 环境可用 `bash references/search_corpus.sh ...`。

现实问题优先使用 `retrieve.py`，因为它会执行“概念映射 + BM25/短语召回 + 三家覆盖约束”。`search.py` 保留给明确关键词或单家材料定位。

## 3. 回答模板

1. 原文依据：不少于 7 条原文，出处写作者、篇名、章节/条目，不贴网页链接。
2. 现实含义：结合原文和读者问题解释含义，避免大白话重述。
3. 行动建议：给出少而准、可执行的做法。

## 4. 引用要求

- 每次引用都标注作者、篇名、章节/条目。
- URL 只作内部追溯，不进入回答正文。
- 不确定版本时写明“当前 corpus 版本”。
- 对现代整理本、译注、选编本保持版权谨慎。
