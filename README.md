# 产品经理skill

面向软件、智能硬件、AI产品、手机应用、微信小程序、平台后端和设备端项目的产品文档技能包。

它可以根据项目阶段选择并生成：竞品分析、功能大纲、PRD、MVP与版本规划、交互说明、硬件需求、客户端需求、平台后端需求、会议纪要、项目排期和验收清单。

## 目录

```text
product-manager/
├─ SKILL.md                    Skill入口与通用工作规则
├─ agents/openai.yaml          Codex界面信息
├─ references/                 各类文档的写作框架
├─ assets/templates/           可编辑的Markdown空模板
└─ scripts/scaffold_product_docs.py
```

## 使用

在 Codex 中调用：

```text
使用 $product-manager，根据现有原型和会议纪要生成本项目需要的产品文档。
```

也可生成一套可编辑模板：

```bash
python scripts/scaffold_product_docs.py \
  --output ./product-docs \
  --project-name "示例项目" \
  --docs all
```

只生成部分文档：

```bash
python scripts/scaffold_product_docs.py \
  --output ./product-docs \
  --project-name "示例项目" \
  --docs prd,hardware,software,backend,roadmap,meeting,acceptance,competitor
```

本仓库提供通用框架，不包含原始公司资料、客户数据、项目账号、密钥或未授权的产品文档。使用时应结合真实项目重写内容并删除所有占位符。
