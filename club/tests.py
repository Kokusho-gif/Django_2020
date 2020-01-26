from django.test import TestCase
from .models import Meeting, Resource, Meetingminutes, Event
from .views import getResource, getMeeting
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.


class MeetingTest(TestCase):

   def test_string(self):
       type=Meeting(meetingtitle="environment")
       self.assertEqual(str(type), type.meetingtitle)

   def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'Meeting')


class EventTest(TestCase):

   def test_string(self):
       type=Event(eventtitle="official")
       self.assertEqual(str(type), type.eventtitle)

   def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'Event')


class MeetingminuteTest(TestCase):

   def test_string(self):
       type=Meetingminutes(minutestext="official")
       self.assertEqual(str(type), type.minutestext)

   def test_table(self):
       self.assertEqual(str(Meetingminutes._meta.db_table), 'Meetingminutes')


class ResourceTest(TestCase):

   def test_string(self):
       type=Resource(resourcename="official")
       self.assertEqual(str(type), type.resourcename)

   def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'Resource')


class GetResourceTest(TestCase):

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getresource'))
        self.assertEqual(response.status_code, 200)


class GetMeetingTest(TestCase):

    def setUp(self):
        self.meet = Meeting.objects.create(meetingtitle='environment',
                                           meetingtime=100,
                                           location='Seattle',
                                           meetingdate='2019-04-02',
                                           agenda='ASD')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getmeeting'))
        self.assertEqual(response.status_code, 200)

    def test_meeting_detail_success(self):
        response = self.client.get(reverse('meetingdetails', args=(self.meet.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)
