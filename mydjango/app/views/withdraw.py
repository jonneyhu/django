from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from app.models import Withdraw
from app.serializers.withdraw import WithdrawList
from rest_framework.permissions import IsAuthenticated


class ListWithdraw(ListCreateAPIView):
    serializer_class = WithdrawList
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin():
            search = self.request.data['query']
            type = self.request.data['type']
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
        self.perform_create(serializer)
        return Response(serializer.data)
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user.profile)

class RetrieveWithdraw(RetrieveUpdateDestroyAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawList
    permission_classes = [IsAuthenticated]
