from rest_framework import serializers
from signup.models import CustomUser
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label="Email Address")

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        email = data.get("email", None)
        raw_pwd = data.get("password", None)

        raw_pwd = data['password']

        #EMU - Email-Mathced-Users
        emu = CustomUser.objects.get(email__exact=email)
        if emu:
            if emu.check_password(raw_pwd):
                user = authenticate(username=email, password=raw_pwd)
                if user:
                    data['user'] = user
                else:
                    raise ValueError("User auth failed")
            else:
                raise ValueError("Incorrect Password")
        else:
            raise ValueError("User Does Not Exist")

        return data
    
