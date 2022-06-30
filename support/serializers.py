from rest_framework import serializers

from .models import Ticket, Message


class TicketSerializer(serializers.ModelSerializer):
    """Обработка данных in json"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.CreateOnlyDefault(0)

    class Meta:
        model = Ticket
        fields = (
            "user",
            "text_ticket",
            "time_create",
            "status",
        )


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = ("user", "number_ticket", "text_answer", "time_create")


