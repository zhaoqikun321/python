##  kafka

#### 配置

| 配置文件             | 实现                    |
| -------------- | ---------------------- |
| producer.properties      | 生产端的配置文件。设置kafka节点列表、消息的压缩策略、序列化处理类、消息的确认机制、发送的消息的同步/异步模式、缓冲区设置 |
| consumer.properties |  消费端的配置文件。设置zookeeper连接服务器地址、当前consumer的标识、消费者客户端编号、每拉取一批消息的最大字节数|
| server.properties         | 服务端的配置文件。设置broker的全局唯一编号、监听链接的端口、处理网络请求的线程数量、发送、接收、请求套接字的缓冲区大小、kafka运行日志存放的路径 |



#### runtime

- 状态

```sh
./kafka-topics.sh --list --zookeeper localhost:2181    #能够正常显示里面的topic就表示运行正常的
```

- 进程

```sh
kafka
```