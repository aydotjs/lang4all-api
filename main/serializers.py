from rest_framework import serializers
from . import models

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
        ]

    def __init__(self, *args, **kwargs):
        super(TeacherSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        self.Meta.depth = 0
        if request and request.method == "GET":
            self.Meta.depth = 1

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
        ]

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
