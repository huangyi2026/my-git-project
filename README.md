# my-git-project

一个基于 Python 的全栈 Web 应用项目，提供用户管理及头像上传等功能。

## 快速开始

```bash
# 运行测试脚本
python test.py
```

输出：

```
Hello World
```

## 项目结构

```
my-git-project/
├── test.py              # 入口测试脚本
├── README.md            # 项目说明
├── server/              # 后端服务（规划中）
│   ├── routes/          # API 路由
│   ├── middleware/       # 中间件（上传校验等）
│   └── utils/           # 工具函数（图片压缩等）
├── client/              # 前端页面（规划中）
│   ├── pages/           # 页面组件
│   └── components/      # 通用组件
└── uploads/avatars/     # 头像存储目录
```

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端 | Python (Flask) |
| 前端 | HTML5 + JavaScript |
| 数据库 | SQLite |
| 存储 | 本地文件系统 |

## 功能规划

- [x] 项目初始化
- [ ] 用户头像上传（JPG/PNG，≤2MB）— [Issue #1](https://github.com/huangyi2026/my-git-project/issues/1)
- [ ] 用户个人中心页面
- [ ] 用户管理 API

## 贡献方式

1. 基于 `main` 创建特性分支：`git checkout -b feature/xxx`
2. 提交代码并推送
3. 创建 Pull Request 等待审核
