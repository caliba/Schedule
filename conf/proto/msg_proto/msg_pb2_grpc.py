# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import conf.proto.msg_proto.msg_pb2 as msg__pb2


class C2FStub(object):
    """service client to frontend
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.C2F_getmsg = channel.unary_unary(
                '/C2F/C2F_getmsg',
                request_serializer=msg__pb2.C2F_Request.SerializeToString,
                response_deserializer=msg__pb2.C2F_Response.FromString,
                )


class C2FServicer(object):
    """service client to frontend
    """

    def C2F_getmsg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_C2FServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'C2F_getmsg': grpc.unary_unary_rpc_method_handler(
                    servicer.C2F_getmsg,
                    request_deserializer=msg__pb2.C2F_Request.FromString,
                    response_serializer=msg__pb2.C2F_Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'C2F', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class C2F(object):
    """service client to frontend
    """

    @staticmethod
    def C2F_getmsg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/C2F/C2F_getmsg',
            msg__pb2.C2F_Request.SerializeToString,
            msg__pb2.C2F_Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class F2SStub(object):
    """service frontend to server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.F2S_getmsg = channel.unary_unary(
                '/F2S/F2S_getmsg',
                request_serializer=msg__pb2.F2S_Request.SerializeToString,
                response_deserializer=msg__pb2.F2S_Response.FromString,
                )


class F2SServicer(object):
    """service frontend to server
    """

    def F2S_getmsg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_F2SServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'F2S_getmsg': grpc.unary_unary_rpc_method_handler(
                    servicer.F2S_getmsg,
                    request_deserializer=msg__pb2.F2S_Request.FromString,
                    response_serializer=msg__pb2.F2S_Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'F2S', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class F2S(object):
    """service frontend to server
    """

    @staticmethod
    def F2S_getmsg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/F2S/F2S_getmsg',
            msg__pb2.F2S_Request.SerializeToString,
            msg__pb2.F2S_Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class S2CStub(object):
    """service server to client
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.S2C_getmsg = channel.unary_unary(
                '/S2C/S2C_getmsg',
                request_serializer=msg__pb2.S2C_Request.SerializeToString,
                response_deserializer=msg__pb2.S2C_Response.FromString,
                )


class S2CServicer(object):
    """service server to client
    """

    def S2C_getmsg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_S2CServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'S2C_getmsg': grpc.unary_unary_rpc_method_handler(
                    servicer.S2C_getmsg,
                    request_deserializer=msg__pb2.S2C_Request.FromString,
                    response_serializer=msg__pb2.S2C_Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'S2C', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class S2C(object):
    """service server to client
    """

    @staticmethod
    def S2C_getmsg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/S2C/S2C_getmsg',
            msg__pb2.S2C_Request.SerializeToString,
            msg__pb2.S2C_Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SetupStub(object):
    """model config service F2S
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Setup_getmsg = channel.unary_unary(
                '/Setup/Setup_getmsg',
                request_serializer=msg__pb2.Setup_Request.SerializeToString,
                response_deserializer=msg__pb2.Setup_Response.FromString,
                )


class SetupServicer(object):
    """model config service F2S
    """

    def Setup_getmsg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SetupServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Setup_getmsg': grpc.unary_unary_rpc_method_handler(
                    servicer.Setup_getmsg,
                    request_deserializer=msg__pb2.Setup_Request.FromString,
                    response_serializer=msg__pb2.Setup_Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Setup', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Setup(object):
    """model config service F2S
    """

    @staticmethod
    def Setup_getmsg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Setup/Setup_getmsg',
            msg__pb2.Setup_Request.SerializeToString,
            msg__pb2.Setup_Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TestStub(object):
    """test msg
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Test_getmsg = channel.unary_unary(
                '/Test/Test_getmsg',
                request_serializer=msg__pb2.Test_Request.SerializeToString,
                response_deserializer=msg__pb2.Test_Response.FromString,
                )


class TestServicer(object):
    """test msg
    """

    def Test_getmsg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Test_getmsg': grpc.unary_unary_rpc_method_handler(
                    servicer.Test_getmsg,
                    request_deserializer=msg__pb2.Test_Request.FromString,
                    response_serializer=msg__pb2.Test_Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Test', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Test(object):
    """test msg
    """

    @staticmethod
    def Test_getmsg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Test/Test_getmsg',
            msg__pb2.Test_Request.SerializeToString,
            msg__pb2.Test_Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
