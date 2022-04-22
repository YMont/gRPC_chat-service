# gRPC_chat-service

## Outline
This implement is using gRPC to build a chat feature with Python.</br>
And mostly I reference this author's project([alanjhone grpc-chat-python](https://github.com/alanjhone/grpc-chat-python/blob/master/client.py)).</br>

But I also record about gRPC HelloWorld's implement([gRPC-Hello-service-with-Python](https://github.com/YMont/gRPC-Hello-service-with-Python)).</br>
Just for a memorandum.</br>

## Introduce
### Requirements
```
grpcio==1.44.0
grpcio-tools==1.44.0
protobuf==3.20.0
six==1.16.0
virtualenv==20.14.1
```

### gRPC code
`chatServer.proto`
```txt
syntax = "proto3";
package grpc;

message Note {
    string name = 1;
    string message = 2;
}

message Empty {}

service ChatServer {
    rpc ChatStream (Empty) returns (stream Note);
    rpc SendNote (Note) returns (Empty);
}
```

### Update gRPC command

You can use cmd terminal or others, just execute it.</br>
And I found some parameter and rules, as following:</br>

**update command**
```
python -m grpc_tools.protoc -I=proto/ --python_out=. --grpc_python_out=. proto/chatServer.proto
```
```
-m: run library module as a script (terminates option list).
-I: isolate Python from the user's environment (implies -E and -s).

First "=proto/" indicates transfer module.
Second "=." indicatis output file(chatServer_pb2.py) location.
Third "=." indicatis output file(chatServer_pb2_rpc.py) location.
```


### Server
`server.py`</br>
Detail Python code can reference it.([server.py](https://github.com/YMont/gRPC_chat-service/blob/main/server.py))</br>
And one point is server connection(localhost), then using class \_\_init\_\_ can auto receive client session among communication.</br>
Also, server provide two function for client using, one is **ChatStream**, another is **SendNote**.</br>
Thus, `python server.py`(command)</br>
Or you can open this Python file and push **F5** execute it.</br>

### Client
`client.py`</br>
Detail Python code can reference it.([client.py](https://github.com/YMont/gRPC_chat-service/blob/main/client.py))</br>
Mostly same as `server.py`.</br>
Otherwise, when the connection complete, then client will call `ChatStream` and `SendNote` in the different field.</br>

---

## Operation process
**server**</br>
![](https://i.imgur.com/zoiy7uG.png)</br>

**client1(John)**</br>
![](https://i.imgur.com/TEivDHp.png)

**client2(Mary)**</br>
![](https://i.imgur.com/Xb0MTzF.png)
