# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import user_location_view_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_user__location__view__pb2
from google.ads.google_ads.v6.proto.services import user_location_view_service_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_services_dot_user__location__view__service__pb2


class UserLocationViewServiceStub(object):
    """Proto file describing the UserLocationView service.

    Service to manage user location views.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUserLocationView = channel.unary_unary(
                '/google.ads.googleads.v6.services.UserLocationViewService/GetUserLocationView',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_user__location__view__service__pb2.GetUserLocationViewRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_user__location__view__pb2.UserLocationView.FromString,
                )


class UserLocationViewServiceServicer(object):
    """Proto file describing the UserLocationView service.

    Service to manage user location views.
    """

    def GetUserLocationView(self, request, context):
        """Returns the requested user location view in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserLocationViewServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUserLocationView': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserLocationView,
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_user__location__view__service__pb2.GetUserLocationViewRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_user__location__view__pb2.UserLocationView.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.UserLocationViewService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserLocationViewService(object):
    """Proto file describing the UserLocationView service.

    Service to manage user location views.
    """

    @staticmethod
    def GetUserLocationView(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.UserLocationViewService/GetUserLocationView',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_user__location__view__service__pb2.GetUserLocationViewRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_user__location__view__pb2.UserLocationView.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)