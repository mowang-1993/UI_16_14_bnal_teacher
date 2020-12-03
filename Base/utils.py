import logging.handlers, os


def init_log():
    """初始化日志配置"""

    # 日志器
    logger = logging.getLogger()
    # 日志级别
    logger.setLevel(logging.INFO)

    # 处理器 -控制台
    sh = logging.StreamHandler()
    # 日志路径
    log_path = "./Log" + os.sep + "bnal.log"
    # 处理器 -文件
    trfh = logging.handlers.TimedRotatingFileHandler(filename=log_path, when="midnight", interval=1,
                                                     backupCount=5, encoding="utf-8")

    # 格式化字符串
    fmt = '%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    # 格式化器
    formatter = logging.Formatter(fmt=fmt)

    # 格式化器 添加 处理器
    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)

    # 处理器 添加 日志器
    logger.addHandler(sh)
    logger.addHandler(trfh)
