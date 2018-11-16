from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from app.models import Notification
from app.serializers.notification import NotificationSerializer

# notifications=['0_1_1','1_1_0','2_1_0']
class NotificationResource(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        user = self.request.user
        notifications = Notification.objects.filter(profile_id__users=user)
        serializer = NotificationSerializer(notifications,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        notifications = request.data['notifications']
        notifications= notifications.strip('[').strip(']').split(',')
        print(notifications)
        user = self.request.user
        old_notifications = user.profile.notification_set.order_by('operate')
        for n in notifications:
            l = n.split('_')
            if len(l) != 3 or (int(l[0]) not in (0, 1, 2)) or (int(l[1]) not in (0, 1)) or (int(l[2]) not in (0, 1)):
                return Response({'message': 'params invalid'})
        if old_notifications:
            for i in range(3):
                old_notifications[i].is_sms_active = notifications[i].split('_')[1]
                old_notifications[i].is_email_active = notifications[i].split('_')[2]
                old_notifications[i].save()
        else:
            for i in range(3):
                n = Notification(profile_id=user.profile)
                n.operate = notifications[i].split('_')[0]
                n.is_sms_active = notifications[i].split('_')[1]
                n.is_mail_active = notifications[i].split('_')[2]
                n.save()
        return Response({'message': 'save successfully'})
