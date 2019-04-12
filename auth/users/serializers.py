from rest_framework import serializers
from users.models import Profile

from django.contrib.auth import get_user_model
UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        print(validated_data)
        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.email = validated_data['email']
        user.save()

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields. These fields will
        #be included in the json representation.
        fields = ("username", "password", "email", "is_staff", )


class ProfileSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only=True)
    owner = UserSerializer(required=False)
    bio = serializers.CharField(required=False, allow_blank=True, max_length=500)
    firstName = serializers.CharField(required=False, allow_blank=True, max_length=500)
    lastName = serializers.CharField(required=False, allow_blank=True, max_length=500)
    
    def update(self, instance, validate_data):
        """
        Update and return an existing `Profile` instance, given the validated data.
        :param instance:
        :param validate_data:
        :return:
        """
        instance.bio = validate_data.get('bio', instance.bio)
        instance.firstName = validate_data.get('firstName', instance.firstName)
        instance.lastName = validate_data.get('lastName', instance.lastName)
        instance.save()
        return instance

'''
class JustNameUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("username", )
        read_only_fields = ("username", "email", )
        write_only_fields = ("password", )
'''
