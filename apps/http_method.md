## GET

浏览器告知服务器:只获取页面上的信息,并发送给我,是最常用的请求方法.

## POST

浏览器告知服务器:想在URL上发条消息.
并且服务器必须确保 数据已储存且仅储存一次,这是HTML表单提交常用的方法.

## PUT

类似POST但是服务器可以触发多次储存,多次覆盖掉旧的数据.
考虑到传输过程中连接可能会丢失,通过浏览器和服务器之间的第二次接受请求,而不破坏其他数据.

## DELETE

删除给定位置的数据

## HEAD

浏览器获取服务器数据:但是只关心消息头.
应用应像处理GET请求一样处理它,但是不发布实际内容.

## OPTIONS

给客户端一个敏捷的途经来弄清这个URL支持哪些HTTP方法.