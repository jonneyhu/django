from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from app.const import DepositOrWithdrawStatus, LogType
from app.models import Withdraw, Fee, AuditLog
from app.serializers.withdraw import WithdrawList
from rest_framework.permissions import IsAuthenticated


class ListWithdraw(ListCreateAPIView):
    serializer_class = WithdrawList
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin():
            print(self.request.user)
            search = self.request.GET['search']
            type = self.request.GET['type']
            return Withdraw.get_withdraw_by_type(search, type)
        else:
            user_id = self.request.user.id
            return Withdraw.get_withdraw_by_user(user_id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        withdraw_sum = Withdraw.get_today_withdraw(user.id).first()
        if withdraw_sum == None:
            withdraw_sum = 0
        sum_amount = int(withdraw_sum.withdraw_sum) + int(request.data['amount'])
        if sum_amount > 1000000:
            return Response({'message': 'Max withdrawal 10,000,00.00 AUD per day'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        if int(request.data['amount'])<100:
            return Response({'message':'Min withdraw 100 AUD per day'},status=status.HTTP_406_NOT_ACCEPTABLE)
        self.perform_create(serializer)
        is_sms_active,is_mail_active=user.profile.is_withdraw_notification()
        if is_sms_active and user.profile.phone:
            pass
        if is_mail_active:
            pass
        return Response(serializer.data)
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user.profile)


class RetrieveWithdraw(RetrieveUpdateDestroyAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawList
    permission_classes = [IsAuthenticated]
    def update(self, request, *args, **kwargs):
        withdraw=self.get_object()
        if withdraw.status ==DepositOrWithdrawStatus.submitting.value:
            data=request.data
            if request.user.is_admin() and data['action'].lower() == 'accept':
                if not data['actual_amount']:
                    return Response({'message':'actual amount is required'})
                if not data['txid']:
                    return Response({'message':'txid is required'})
                withdraw.actual_amount=int(data['actual_amount'])
                withdraw_fee=data['actual_amount']*0.002
                if withdraw_fee<2:
                    withdraw_fee=2
                if withdraw_fee>1000:
                    withdraw_fee=1000
                fee=Fee(withdraw_id=withdraw,amount=withdraw_fee)
                if withdraw.is_exsit_txid(data['txid']):
                    return Response({'message':'txid already exsits'})
                withdraw.status=DepositOrWithdrawStatus.accepted.value
                withdraw.blcokchain_txid=data['txid']
                withdraw.save()
                fee.save()
                audit=AuditLog()
                audit.operate_id=request.user.id
                audit.actions='Update withdraw status accept.Withdraw id:' + \
                    str(withdraw.id)
                audit.type=LogType.update.value
                audit.operate_email=request.user.email
                return Response({
                    'message': 'Withdraw successfully',
                    'data': {
                               'type': 'withdraw',
                               'action': 'accept',
                               'amount': withdraw.actual_amount,
                               'id': withdraw.id
                    }
                }, 200)
            if request.user.is_admin() and data['action'].lower()=='cancel':
                pass
        else:
            data=request.data
            if request.user.is_admin() and data['action'].lower == 'accept':
                if withdraw.is_exsit_bank_txid(data['bank_txid']):
                    if not data['bank_txid']:
                        return Response({'message':'bank_txid is reuired'})
                    return Response({'message':'bank_txid already exsits'})
                withdraw.bank_txid=data['bank_txid']
                withdraw.save()
                audit = AuditLog()
                audit.operate_id = request.user.id
                audit.actions = 'Update withdraw status accept.Withdraw id:' + \
                                str(withdraw.id)
                audit.type = LogType.update.value
                audit.operate_email = request.user.email
                return Response({
                    'message': 'Withdraw successfully',
                    'data': {
                        'type': 'withdraw',
                        'action': 'accept',
                        'amount': withdraw.actual_amount,
                        'id': withdraw.id
                    }
                }, 200)


