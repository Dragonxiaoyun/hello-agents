# my-fastapi-app 🚀

晓云的 AI Agent 学习实战项目

## 当前进度

- [x] Day 1: Python 基础复习（类型系统、装饰器、生成器、上下文管理器）
- [ ] Day 2: FastAPI + async/await + LLM 接入（进行中 🔥）
- [ ] Day 3-7: RAG + 向量数据库
- [ ] Week 3-4: Agent 框架 + 多 Agent 协作
- [ ] Week 5-6: MCP 协议 + 高级 RAG
- [ ] Week 7-8: 项目打磨 + 面试准备

## 运行

```bash
# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 填入你的 API Key

# 启动服务
uvicorn app.main:app --reload
```

打开 http://127.0.0.1:8000/docs 查看自动生成的 API 文档

## 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/` | 欢迎页 |
| GET | `/health` | 健康检查 |
| POST | `/chat` | LLM 对话接口 |
