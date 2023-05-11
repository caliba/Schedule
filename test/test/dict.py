import time
import grpc
from concurrent import futures
import time
import threading
import conf.proto.msg_proto.msg_pb2 as pb2
import conf.proto.msg_proto.msg_pb2_grpc as pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60


class Test(pb2_grpc.TestServicer):
    def Test_getmsg(self, request, context):
        return pb2.Test_Response(flag=True)
        pass


def server_run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    # pb2_grpc.add_S2CServicer_to_server(S2C(self.recv_q), server)
    pb2_grpc.add_TestServicer_to_server(Test(), server)
    port = '[::]:' + str(50050)

    server.add_insecure_port(port)
    server.start()

    try:
        while True:
            print("server is running")
            time.sleep(_ONE_DAY_IN_SECONDS)  # 设置服务器启动一天, 一天后自动关闭
            print("server is over")
    except KeyboardInterrupt:  # 如果出现ctr+c硬中断, 直接退出
        server.stop(0)


def send_req():
    target_port = 'localhost:' + str(50050)
    with grpc.insecure_channel(target_port) as channel:

        stub = pb2_grpc.TestStub(channel)
        send_time = time.time()
        msg_send = pb2.Test_Request(msg=1)
        response = stub.Test_getmsg(msg_send)
        print("frontend to server time is {}".format(time.time() - send_time))

def main():
    server_run()

main()