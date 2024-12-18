from rest_framework import serializers
from . import models
from django.core.mail import send_mail


# ===========================
# Teacher-Related Serializers
# ===========================

# Serializes Teacher information
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = [
            "id",
            "full_name",
            "email",
            "password",
            "qualification",
            "mobile_no",
            "profile_img",
            "teacher_courses",
            "otp_digit",
            "login_via_otp",
        ]

    def __init__(self, *args, **kwargs):
        super(TeacherSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        self.Meta.depth = 0
        if request and request.method == "GET":
            self.Meta.depth = 1
    def create(self, validate_data):
        email = self.validated_data['email']
        otp_digit = self.validated_data['otp_digit']
        instance = super(TeacherSerializer, self).create(validate_data)
        send_mail(
            'Verify Account',
            'Please verify your account',
            'codedynasty001@gmail.com',
            [email],
            fail_silently=False,
         html_message=f'<p>Your OTP is </p><p>{otp_digit}</p>'
        )
        return instance


# Serializes teacher's dashboard statistics
class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = [
            "total_teacher_courses",
            "total_teacher_students",
            "total_teacher_chapters",
        ]

# Serializes individual course details
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = [
            "id",
            "category",
            "teacher",
            "title",
            "description",
            "featured_img",
            "languages",
            "course_chapters",
            "related_videos",
            "total_enrolled_students",
            "course_rating",
            "price"
        ]
        depth = 1

    def __init__(self, *args, **kwargs):
        super(CourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        self.Meta.depth = 0
        if request and request.method == "GET":
            self.Meta.depth = 1

# Serializes Course Category information
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ["id", "title", "description"]

# Serializes chapter details within a course
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ["id", "course", "title", "description", "video", "remarks"]


# ===========================
# Student-Related Serializers
# ===========================

# Serializes Student information
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = [
            "id",
            "full_name",
            "email",
            "password",
            "username",
            "interested_categories",
            "otp_digit",
            "login_via_otp"
        ]
    def create(self, validate_data):
        email = self.validated_data['email']
        otp_digit = self.validated_data['otp_digit']
        instance = super(StudentSerializer, self).create(validate_data)
        send_mail(
            'Verify Account',
           'Please verify your account',
            'codedynasty001@gmail.com',
            [email],
            fail_silently=False,
            html_message=f'<p>Your OTP is </p><p>{otp_digit}</p>'
            )
        return instance

def __init__(self, *args, **kwargs):
    super(StudentSerializer, self).__init__(*args, **kwargs)
    request = self.context.get('request')
    self.Meta.depth = 0
    if request and request.method == 'GET':
        self.Meta.depth = 2


# Serializes student's course enrollment details
class StudentCourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentCourseEnrollment
        fields = ["id", "course", "student", "enrolled_time"]

    def __init__(self, *args, **kwargs):
        super(StudentCourseEnrollSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        self.Meta.depth = 0
        if request and request.method == "GET":
            self.Meta.depth = 2

# Serializes course rating and review details
class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseRating
        fields = ["id", "course", "student", "rating", "reviews", "review_time"]
        depth = 1

    def __init__(self, *args, **kwargs):
        super(CourseRatingSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        self.Meta.depth = 0
        if request and request.method == "GET":
            self.Meta.depth = 1

# Serializes student's favorite courses
# class StudentFavoriteCourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.StudentFavoriteCourse
#         fields = ["id", "course", "student", "status"]

#     def __init__(self, *args, **kwargs):
#         super(StudentFavoriteCourseSerializer, self).__init__(*args, **kwargs)
#         request = self.context.get("request")
#         self.Meta.depth = 0
#         if request and request.method == "GET":
#             self.Meta.depth = 2

# Serializes student assignments
class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentAssignment
        fields = [
            "id",
            "teacher",
            "student",
            "title",
            "detail",
            "student_status",
            "add_time",
        ]
        depth = 1

    def __init__(self, *args, **kwargs):
        super(StudentAssignmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        self.Meta.depth = 0
        if request and request.method == "GET":
            self.Meta.depth = 1


# Serializes student's dashboard statistics
class StudentDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['enrolled_courses',  'complete_assignments', 'pending_assignments']

class TeacherStudentChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeacherStudentChat
        fields = ["id", "teacher", "msg_from", "msg_text", "msg_time"]
    def to_representation(self, instance):
        representation = super(TeacherStudentChatSerializer, self).to_representation(instance)
        representation["msg_time"] = instance.msg_time.strftime("%Y-%m-%d %H:%M")
        return representation
