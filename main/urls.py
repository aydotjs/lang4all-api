from django.urls import path
from . import views

urlpatterns = [
    # -------------------------
    # Teacher-related URLs
    # -------------------------
    path("teacher/", views.TeacherList.as_view()),  # List all teachers
    path(
        "teacher/<int:pk>/", views.TeacherDetail.as_view()
    ),  # Get details of a specific teacher
    path("teacher-login", views.teacher_login),  # Teacher login
    path(
        "teacher/dashboard/<int:pk>/", views.TeacherDashboard.as_view()
    ),  # Teacher dashboard
    path(
        "teacher-courses/<int:teacher_id>/", views.TeacherCourseList.as_view()
    ),  # List courses for a specific teacher
    path(
        "teacher-course-detail/<int:pk>/", views.TeacherCourseDetail.as_view()
    ),  # Get details of a specific teacher's course
    path(
        "teacher/change-password/<int:teacher_id>/", views.teacher_change_password
    ),  # Change password for a specific teacher
    # -------------------------
    # Category-related URLs
    # -------------------------
    path("category/", views.CategoryList.as_view()),  # List all categories
    # -------------------------
    # Course-related URLs
    # -------------------------
    path("course/", views.CourseList.as_view()),  # List all courses
    path(
        "course/<int:pk>/", views.CourseDetail.as_view()
    ),  # Get details of a specific course
    path(
        "course-chapters/<int:course_id>/", views.CourseChapterList.as_view()
    ),  # List chapters for a specific course
    path(
        "chapter/<int:pk>/", views.ChapterDetail.as_view()
    ),  # Get details of a specific chapter
    path("chapter/", views.ChapterList.as_view()),  # List and create chapters
    # -------------------------
    # Student-related URLs
    # -------------------------
    path("student/", views.StudentList.as_view()),  # List all students
    path("student-login", views.student_login),  # Student login
    path(
        "student-enroll-course/", views.StudentEnrolledCourseList.as_view()
    ),  # Enroll a student in a course
      path("create-payment-session/", views.CreatePaymentSession.as_view(), name="create-payment-session"),
    # path(
    #     "student-pay-for-course/", views.StripeCheckoutView.as_view()
    # ),  # Enroll a student in a course
    path(
        "fetch-enroll-status/<int:student_id>/<int:course_id>",
        views.fetch_enroll_status,
    ),  # Check enrollment status for a course
    path(
        "fetch-enrolled-students/<int:course_id>", views.EnrollStudentList.as_view()
    ),  # List students enrolled in a specific course
    path(
        "fetch-all-enrolled-students/<int:teacher_id>",
        views.EnrollStudentList.as_view(),
    ),  # List all students under a specific teacher
    path(
        "fetch-enrolled-courses/<int:student_id>", views.EnrollStudentList.as_view()
    ),  # List all courses a student is enrolled in
    path(
        "course-rating/<int:course_id>", views.CourseRatingList.as_view()
    ),  # List ratings for a specific course
    path(
        "fetch-rating-status/<int:student_id>/<int:course_id>",
        views.fetch_rating_status,
    ),  # Check rating status for a course
    # Optional: Add a course to favorites for a student
    # path('student-add-favorite-course/', views.StudentFavoriteCourseList.as_view()),
    # Optional: Remove a course from favorites for a student
    # path('student-remove-favorite-course/<int:course_id>/<int:student_id>', views.remove_favorite_course),
    path(
        "student/dashboard/<int:pk>/", views.StudentDashboard.as_view()
    ),  # Student dashboard
    path(
        "student/change-password/<int:student_id>/", views.student_change_password
    ),  # Change password for a specific student
    path(
        "student/<int:pk>/", views.StudentDetail.as_view()
    ),  # Get details of a specific teacher
    # -------------------------
    # Assignment-related URLs
    # -------------------------
    path(
        "student-assignment/<int:teacher_id>/<int:student_id>/",
        views.AssignmentList.as_view(),
    ),  # List assignments for a student assigned by a teacher
    path(
        "my-assignments/<int:student_id>/", views.MyAssignmentList.as_view()
    ),  # List assignments for a specific student
    path(
        "update-assignment/<int:pk>/", views.UpdateAssignment.as_view()
    ),  # Update assignment details
    # -------------------------
    # Messaging-related URLs
    # -------------------------
    path(
        "send-message/<int:teacher_id>/<int:student_id>/",
        views.save_teacher_student_msg,
    ),  # Send a message from teacher to student
    path(
        "get-messages/<int:teacher_id>/<int:student_id>/", views.MessageList().as_view()
    ),  # Get all messages between a teacher and student
    path(
        "send-group-message/<int:teacher_id>/", views.save_teacher_student_group_msg
    ),  # Send a group message from teacher to multiple students
    path(
        "send-group-message-from-student/<int:student_id>/",
        views.save_teacher_student_group_msg_from_student,
    ),  # Send a group message from student to teacher
    # -------------------------
    # Teacher-student relationship-related URLs
    # -------------------------
    path(
        "fetch-my-teachers/<int:student_id>", views.MyTeacherList.as_view()
    ),  # List all teachers a student has interacted with
     # -------------------------
    # Password reset-related URLs
    # -------------------------
    # path("password-reset/", views.PasswordResetAPIView.as_view(), name="password_reset"),
    # path(
    #     "password-reset-confirm/<uidb64>/<token>/",
    #     views.PasswordResetConfirmAPIView.as_view(),
    #     name="password_reset_confirm",
    # ),
    path('verify-teacher/<int:teacher_id>/', views.verify_teacher_via_otp),
    path('verify-student/<int:student_id>/', views.verify_student_via_otp),
    path('teacher-forgot-password/', views.teacher_forgot_password),
    path('student-forgot-password/', views.student_forgot_password),
    path('teacher-change-password/<int:teacher_id>/', views.teacher_change_password),
    path('student-change-password/<int:student_id>/', views.student_change_forgotten_password),

]
