"""

    随机生成user——agent
"""
from fake_useragent import UserAgent
agent = UserAgent().random
print(agent)