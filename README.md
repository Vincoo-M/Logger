### [1.0] - Sep 30, 2020
**功能**
- 基于logging和colorlog模块编写的自定义logger模块
- 按照Log日志等级，在控制台显示不同的等级颜色
- 创建Logger对象即可使用，无需配置

**默认配置**
- logger名称: root
- 日志等级: WARNING
- 日志输出到文件: False
- fmt: [%(asctime)s] [%(levelname)-8s] [form:/%(module)s/%(funcName)s] [line:%(lineno)d]  Message: %(message)s
- datefmt: %Y-%m-%d %H:%M:%S

**参数说明**
- param name: 创建logger, 默认为空-root
- param level: 设置logger日志等级, 默认为debug
- param tofile: 设置是否将日志输出到文件, 默认路径 ./log/xxxxxx.log
- param fmt: 设置日志格式
- param datefmt: 设置时间格式