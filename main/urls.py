from django.urls import path
from . import views

urlpatterns = [
    # Teacher
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login', views.teacher_login),
    path('teacher/dashboard/<int:pk>/', views.TeacherDashboard.as_view()),

    # Category
    path('category/', views.CategoryList.as_view()),

    # Course
    path('course/', views.CourseList.as_view()),

    # Course Detail
    path('course/<int:pk>/', views.CourseDetail.as_view()),

    # Specific Course Chapter
    path('course-chapters/<int:course_id>/', views.CourseChapterList.as_view()),

    # Specific Chapter
    path('chapter/<int:pk>/', views.ChapterDetail.as_view()),

    # Chapter List (handles listing and creating chapters)
    path('chapter/', views.ChapterList.as_view()),
    
    path('student-assignment/', views.AssignmentList.as_view()),

    # Teacher Courses
    path('teacher-courses/<int:teacher_id>/', views.TeacherCourseList.as_view()),
    #  Course Detail
    path('teacher-course-detail/<int:pk>/', views.TeacherCourseDetail.as_view()),
    #  Student
    path('student/', views.StudentList.as_view()),
    path('student-login', views.student_login),
    path('student-enroll-course/', views.StudentEnrolledCourseList.as_view()),
    path('fetch-enroll-status/<int:student_id>/<int:course_id>', views.fetch_enroll_status),
    path('fetch-enrolled-students/<int:course_id>', views.EnrollStudentList.as_view()),
    path('fetch-all-enrolled-students/<int:teacher_id>', views.EnrollStudentList.as_view()),
    path('fetch-enrolled-courses/<int:student_id>', views.EnrollStudentList.as_view()),
    path('course-rating/<int:course_id>', views.CourseRatingList.as_view()),
    path('fetch-rating-status/<int:student_id>/<int:course_id>', views.fetch_rating_status),
    path('student-add-favorite-course/', views.StudentFavoriteCourseList.as_view()),
    path('student-remove-favorite-course/<int:course_id>/<int:student_id>', views.remove_favorite_course),

]
