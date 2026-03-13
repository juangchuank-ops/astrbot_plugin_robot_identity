from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star
from astrbot.api.message_components import Plain

class RobotIdentity(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @filter.event_message_type(filter.EventMessageType.ALL)
    async def on_message(self, event: AstrMessageEvent):
        '''监听消息，当满足条件时确认机器人身份'''
        
        # 获取配置
        # 注意：不同版本的 AstrBot 获取配置方式可能不同，通常通过 context 获取
        # 这里假设 context.get_config(plugin_name) 或直接从 context.config 中获取
        # 根据 AstrBot 的设计，插件配置通常在初始化时加载，但动态获取更稳妥
        
        # 尝试获取配置，如果没有则使用默认值
        config = self.context.get_config() or {}
        trigger_keyword = config.get("trigger_keyword", "你")
        reply_content = config.get("reply_content", "我是 AstrBot 机器人，请问有什么可以帮您？")
        
        # 1. 解析纯文本内容（忽略 @、图片等组件）
        # 遍历消息链，提取所有 Plain 组件的文本并拼接
        text_content = "".join(
            [c.text for c in event.message_obj.message if isinstance(c, Plain)]
        ).strip()
        
        should_reply = False
        
        # 2. 判断触发逻辑
        # 条件：内容严格等于 触发关键词
        
        # 兼容性处理：安全获取事件属性
        is_group = getattr(event, 'is_group', False)
        is_private = getattr(event, 'is_private', False)
        is_at_me = getattr(event, 'is_at_me', False)
        
        # 如果 is_group/is_private 未定义，尝试从 message_obj 推断
        if not is_group and not is_private and hasattr(event, 'message_obj'):
            # 大多数适配器中，有 group_id 则为群聊，否则为私聊
            group_id = getattr(event.message_obj, 'group_id', None)
            if group_id:
                is_group = True
            else:
                is_private = True
                
        if text_content == trigger_keyword:
            # 场景A：群聊，且被 @
            if is_group and is_at_me:
                should_reply = True
            
            # 场景B：私聊
            elif is_private:
                should_reply = True
                
        # 3. 回复
        if should_reply:
            yield event.plain_result(reply_content)
