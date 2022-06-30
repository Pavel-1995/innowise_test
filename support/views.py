from django.http import HttpResponse

from rest_framework import generics, viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from .serializers import TicketSerializer, MessageSerializer
from .models import *
from .permissions import IsAdminOrIsAuthenticated
from .tasks import send_email


class TicketApiListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 30


class MessageApiListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 30


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    pagination_class = TicketApiListPagination
    permission_classes = (IsAdminOrIsAuthenticated,)

    def perform_update(self, serializer, default_status=1):
        serializer.save()
        if serializer.data["status"] != default_status:
            send_email.delay()
        else:
            print("error sent_email")

    def perform_create(self, serializer, default_status=1):
        serializer.validated_data["status"] = default_status
        serializer.save()

    @action(methods=["get", "post"], detail=True)
    def answer(self, request, pk=None):
        answer_s = Message.objects.get(number_ticket_id=pk)
        num_ticket = Ticket.objects.get(pk=pk)
        CreateModelMixin.create(self, request)
        return Response(
            {"ticket": num_ticket.text_ticket, "answer": answer_s.text_answer}
        )

    @action(methods=["get"], detail=False)
    def answer(self, request):
        answer_s = Message.objects.filter(user=self.request.user).values()
        num_ticket = Ticket.objects.filter(user=self.request.user).values()
        return Response({"ticket": num_ticket, "answer": answer_s})


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = MessageApiListPagination
    permission_classes = (IsAdminUser,)


def index(request):
    """Instead of page not foud"""
    return HttpResponse("Instead of page not foud")


