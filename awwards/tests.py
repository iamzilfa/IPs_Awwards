from django.test import TestCase
# Create your tests here.
from .models import Profile,Project,Comments
from django.contrib.auth.models import User
import datetime as dt

class ProfileTestClass(TestCase):
    '''
    images test method
    '''

    def setUp(self):
        self.user = User.objects.create(id =1,username='zily')
        self.profile = Profile(bio = ' Zilfa',contact = 'cyamani',profile = 'wouw.jpeg', user = self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.profile.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=1) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
        self.profile.save_profile()
        profile=Profile.delete_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=0) 

class CommentTestClass(TestCase):
    def setUp(self):
        self.comment=Comments.objects.create(comment='yesss')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.comment.save_comments()
        comment=Comments.objects.all()
        self.assertTrue(len(comm)>0) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
        self.comment.save_comments()
        self.comment.delete_comments()
        comment=Comments.objects.all()
        self.assertTrue(len(comm)>0)

class ProjectTestClass(TestCase):
    '''
    project test method
    '''
    
    def setUp(self):
        self.project = Project(title ='leblog', project_image='kare.png', description='project testing',link='https://rithagallery.herokuapp.com/' ,date='12.9.2019',user='rita')

    def tearDown(self):
        Project.objects.all().delete()
        Profile.objects.all().delete()

        # Testing Instance
        def test_instance(self):
            self.assertTrue(isinstance(self.project,Project))

        # Testing the save method
        def test_save_method(self):
            self.project=Project(title='dog',description='scared',user=self.user1,rate="1")
            self.project.save_project()
            project = Project.objects.all()
            self.assertTrue(len(project) >= 1)

    def test_delete_method(self):
            self.project=Project(title='dog',description='scared',user=self.user1,rate="1")
            self.project.save_project()
            projects = self.project.delete_project
            deleted = Project.objects.all()
            self.assertTrue(len(deleted) <= 0)