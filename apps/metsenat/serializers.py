from rest_framework import serializers

from apps.metsenat.models import Homiy, Talaba, TalabaVaHomiy


class HomiySerializer(serializers.ModelSerializer):
    class Meta:
        model = Homiy
        fields = ['f_i_sh', 'phone_number', 'homiylik_summa', 'sarflangan_summa', 'sana', 'status', 'amallar']


class TalabaVaHomiySerializer(serializers.ModelSerializer):
    class Meta:
        model = TalabaVaHomiy
        fields = ['id', 'homiy', 'ajratilgan_summa']


class TalabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = ['id', 'f_i_sh', 'phone_number', 'otm', 'talabalik_turi', 'kontrakt_summa', 'atratilgan_summa']


class TalabaDetailSerializer(serializers.ModelSerializer):
    talabaga_homiylar = serializers.SerializerMethodField()

    class Meta:
        model = Talaba
        fields = ['id', 'f_i_sh', 'phone_number', 'otm', 'talabalik_turi', 'kontrakt_summa', 'atratilgan_summa',
                  'talabaga_homiylar']

    def get_talabaga_homiylar(self, obj):
        print(obj)
        print(TalabaVaHomiy.objects.filter(talaba=obj))
        return TalabaVaHomiySerializer(instance=TalabaVaHomiy.objects.filter(talaba=obj), many=True).data
