from django.urls import path
from . import views

urlpatterns = [
    # Teacher-related URLs
    path('teacher/', views.TeacherList.as_view()),  # List all teachers
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),  # Get details of a specific teacher
    path('teacher-login', views.teacher_login),  # Teacher login
    path('teacher/dashboard/<int:pk>/', views.TeacherDashboard.as_view()),  # Teacher dashboard
    path('teacher-courses/<int:teacher_id>/', views.TeacherCourseList.as_view()),  # List courses for a specific teacher
    path('teacher-course-detail/<int:pk>/', views.TeacherCourseDetail.as_view()),  # Get details of a specific teacher's course

    # Category-related URLs
    path('category/', views.CategoryList.as_view()),  # List all categories

    # Course-related URLs
    path('course/', views.CourseList.as_view()),  # List all courses
    path('course/<int:pk>/', views.CourseDetail.as_view()),  # Get details of a specific course
    path('course-chapters/<int:course_id>/', views.CourseChapterList.as_view()),  # List chapters for a specific course
    path('chapter/<int:pk>/', views.ChapterDetail.as_view()),  # Get details of a specific chapter
    path('chapter/', views.ChapterList.as_view()),  # List and create chapters

    # Student-related URLs
    path('student/', views.StudentList.as_view()),  # List all students
    path('student-login', views.student_login),  # Student login
    path('student-enroll-course/', views.StudentEnrolledCourseList.as_view()),  # List enrolled courses for a student
    path('fetch-enroll-status/<int:student_id>/<int:course_id>', views.fetch_enroll_status),  # Check enrollment status for a course
    path('fetch-enrolled-students/<int:course_id>', views.EnrollStudentList.as_view()),  # List students enrolled in a specific course
    path('fetch-all-enrolled-students/<int:teacher_id>', views.EnrollStudentList.as_view()),  # List all students enrolled under a specific teacher
    path('fetch-enrolled-courses/<int:student_id>', views.EnrollStudentList.as_view()),  # List all courses a student is enrolled in
    path('course-rating/<int:course_id>', views.CourseRatingList.as_view()),  # List ratings for a specific course
    path('fetch-rating-status/<int:student_id>/<int:course_id>', views.fetch_rating_status),  # Check rating status for a course
    # path('student-add-favorite-course/', views.StudentFavoriteCourseList.as_view()),  # Add a course to favorites for a student
    # path('student-remove-favorite-course/<int:course_id>/<int:student_id>', views.remove_favorite_course),  # Remove a course from favorites for a student
    path('student/dashboard/<int:pk>/', views.StudentDashboard.as_view()),  # Teacher dashboard

    # Assignment-related URLs
    path('student-assignment/<int:teacher_id>/<int:student_id>/', views.AssignmentList.as_view()),  # List assignments for a student assigned by a teacher
    path('my-assignments/<int:student_id>/', views.MyAssignmentList.as_view()),  # List assignments for a student assigned by a teacher
    path('update-assignment/<int:pk>/', views.UpdateAssignment.as_view()),  # List assignments for a student assigned by a teacher
]
