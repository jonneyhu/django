from rest_framework.serializers import ModelSerializer
from app.const import IdDocumentType
from app.models import UserKyc
from django.conf import settings

class UserKycSerializer(ModelSerializer):
    class Meta:
        model=UserKyc
        fields='__all__'
    def validate(self, attrs):
        file=attrs['kyc_file']

        # args['kyc_file'] = UserKYC.file_stream(file)
        # args['user_id'] = g.user.id
        # args['birthday'] = datetime.strptime(args['birthday'], '%d-%m-%Y')
        # args['expire_date'] = datetime.strptime(
        #     args['expire_date'], '%d-%m-%Y')
        # document_type = args['id_document_type']
        # args['id_document_type'] = UserKYC.document_type(document_type)
        # if UserKYC.allowed_file(file.filename):
        #     current_kyc.update(**args)