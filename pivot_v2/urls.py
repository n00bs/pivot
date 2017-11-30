from django.conf.urls import url
from pivot_v2.views import MajorInfoView, MajorView, \
                           MajorGPAView, MajorCourseView

# ALL ENDPOINTS REQUIRE 'year' AS A QUERY PARAM, eg: {year: 2005}
# ALL ENDPOINTS** SUPPORT MULTIPLE MAJOR QUERY WITH 'majorList' QUERY PARAM
# eg: {majorList: [123,122]}
urlpatterns = [
    # DATA INCLINED
    # the full featured api v2 endpoint
    url(r'^api/v2/majors/$',
        MajorView.as_view(), name='major'),
    # the full featured api v2 endpoint for a given major id
    # **'majorList' is not supported with this endpoint
    url(r'^api/v2/majors/(?P<major_id>[0-9]{1,5})/$',
        MajorView.as_view(), name='major_detail'),

    # PERFORMANCE INCLINED ENDPOINTS
    # the basic info api v2 endpoint
    url(r'^api/v2/majors/info/$',
        MajorInfoView.as_view(), name='major_info'),
    # the gpa inclined api v2 endpoint
    url(r'^api/v2/majors/gpas/$',
        MajorGPAView.as_view(), name='major_gpa'),
    # the courses inclined api v2 endpoint
    url(r'^api/v2/majors/courses/$',
        MajorCourseView.as_view(), name='major_course'),
]
