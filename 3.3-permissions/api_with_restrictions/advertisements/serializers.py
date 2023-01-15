from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        user = self.context['request'].user
        open_adv = Advertisement.objects.filter(creator=user, status='OPEN').count()
        data_status = self.context["request"].data.get("status")
        methods = ['POST', 'PUT', 'PATCH']
        if open_adv >= 10 and self.context['request'].method == 'POST':
            raise serializers.ValidationError("Вы можете держать открытыми не более 10 объявлений")
        if open_adv >= 10 and self.context['request'].method == 'PUT':
            raise serializers.ValidationError("Вы можете держать открытыми не более 10 объявлений")
        if open_adv >= 10 and self.context['request'].method == 'PATCH' and data_status == 'OPEN':
            raise serializers.ValidationError("Вы можете держать открытыми не более 10 объявлений")
        return data
