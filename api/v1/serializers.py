from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, user_logged_in, login

from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler

from posts.models import Post, Ratio

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomJWTSerializer(JSONWebTokenSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(required=False, allow_blank=True)

    username_field = 'username'

    def validate(self, attrs):

        password = attrs.get("password").lower()
        username = attrs.get("username")

        if len(password) < 1 or len(username) < 1:
            msg = {
                "non_field_errors": "Please enter both phone number and password."
            }

        if not User.objects.filter(username=username):
            msg = {
                "non_field_errors": "Sorry! No such user exist."}

        if User.objects.filter(username=username, is_active=False):
            msg = {
                "non_field_errors": "Sorry! This account has been blocked."}

        user_obj = User.objects.filter(username=attrs.get("username")).first()
        if user_obj is not None:
            credentials = {
                'username': user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                login(self.context['request'], user)
                print(self.context['request'].user)
                if user:
                    payload = jwt_payload_handler(user)
                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = {
                        "non_field_errors": "username and password do not match."
                    }
                    raise serializers.ValidationError(msg)

            else:
                msg = {
                    "non_field_errors": "Both username and password is required."
                }
                raise serializers.ValidationError(msg)

        else:
            msg = {
                "non_field_errors": "Account does not exists."}
            raise serializers.ValidationError(msg)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'get_ratio', 'created')
        extra_kwargs = {'get_ratio': {'read_only': True}}


class RatioSerializer(serializers.ModelSerializer):
    post_id = serializers.CharField(write_only=True)

    class Meta:
        model = Ratio
        fields = ('id', 'user', 'post_id', 'opinion', 'created')
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        print('mark_1', dir(self.context['request']))
        print('mark_2', self.context['request'].user)
        ratio, created = Ratio.objects.get_or_create(
            post_id=validated_data.pop('post_id'),
            user=self.context['request'].user
        )
        ratio.opinion = validated_data['opinion']
        ratio.save()

        return ratio
