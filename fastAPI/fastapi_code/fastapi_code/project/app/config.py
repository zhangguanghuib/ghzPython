from typing import Dict

# Tortoise-ORM 配置
TORTOISE_ORM: Dict = {
    "connections": {
        # 生产环境示例：MySQL
        "default": "mysql://root:123456@192.168.31.152:3306/fastapi_db5",
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],  # 模型模块和 Aerich 迁移模型
            "default_connection": "default",
        }
    },
    # 连接池配置（推荐）
    "use_tz": False,  # 是否使用时区
    "timezone": "UTC",  # 默认时区
    "db_pool": {
        "max_size": 10,  # 最大连接数
        "min_size": 1,   # 最小连接数
        "idle_timeout": 30  # 空闲连接超时（秒）
    }
}
