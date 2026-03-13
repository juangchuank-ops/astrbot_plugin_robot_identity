# AstrBot 机器人身份确认插件 (astrbot_plugin_robot_identity)

这是一个 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 的插件，用于在用户询问机器人身份时自动进行确认回复。

## 功能介绍

- **群聊场景**：当用户在群里 @机器人 并且发送内容仅为“你”（可配置）时，机器人会自动回复预设的身份确认信息。
- **私聊场景**：当用户在私聊中发送内容仅为“你”（可配置）时，机器人会自动回复预设的身份确认信息。

## 安装方法

1. 将 `astrbot_plugin_robot_identity` 文件夹放入 AstrBot 的 `data/plugins/` 目录下。
2. 重启 AstrBot 或在 Web 管理面板中重新加载插件。

## 配置说明

插件配置文件位于 `data/config/astrbot_plugin_robot_identity_config.json`（插件加载后自动生成），或者你可以在 AstrBot 的 Web 管理面板中直接修改配置。

| 配置项 | 类型 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- |
| `trigger_keyword` | string | `你` | 触发身份确认的关键词，必须完全匹配。 |
| `reply_content` | string | `我是 AstrBot 机器人，请问有什么可以帮您？` | 触发时机器人回复的内容。 |

## 使用示例

**默认配置下：**

- **群聊**：
  - 用户：@Bot 你
  - 机器人：我是 AstrBot 机器人，请问有什么可以帮您？

- **私聊**：
  - 用户：你
  - 机器人：我是 AstrBot 机器人，请问有什么可以帮您？

## 许可证

MIT
