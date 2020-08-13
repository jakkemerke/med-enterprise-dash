from datetime import date

from pyramid.view import view_config


def get_today_string():
    return f"{date.today()}"


# TODO: Fill in more values.
def get_test_student():
    return {
        "academicAdvisor": "Alex Great",
        "academicStanding": "",
        "currentStudentLevel": "",
        "classStanding": "",
        "major": "Biology",
        "minor": "Chemistry",
        "preprof": "Pre-Med",
        "gpaPsuUndergradTrimmed": "",
        "gpaOverallUndergradTrimmed": "",
        "hoursOverallUndergradTrimmed": "",
        "attendedOrientation": "",
        "hasAdvisingHolds": True,
        "holdsReg": False,
        "admitTerm": "",
        "latestDecision": "",
        "appliedToGraduate": "",
        "collegeCode": "",
        "attribCode": "",
        "internationalStudent": "",
        "coenrolled": "",
        "attendanceTermLast": "",
        "certDeclaration": "",
        "honorsEnrollment": "",
        "degreeGuarantee": "",
    }


# TODO: Verify the return data matches the API in operations.
def get_test_contact():
    return {
        "fullName": "DJ Lastname",
        "firstName": "DJ",
        "middleName": "",
        "lastName": "Lastname",
        "badgeId": "987654321",
        "email": "dj.the.dj@foo.bar",
        "id": "453",
        "username": "djdjdj",
        "phone": "555-1212",
        "veteran": True,
        "residency": "Domestic",
        "gender": "Spivak",
        "studentRecord": get_test_student(),
    }


# TODO: Verify the dates match the API in operations.
def get_test_history():
    return [
        {
            "interactionId": "123",
            "appointmentId": "2",
            "interactionSubject": "Testing",
            "interactionTeamName": "Team Red",
            "interactionAssignedToName": "Alex Great",
            "interactionMedium": "In Person",
            "interactionState": "Open",
            "interactionLastUpdatedDateOnly": "2020-08-11T09:00:04",
            "interactionCreatedOn": "2020-08-11T09:00:04",
            "appointmentStartOn": "2020-08-11T09:00:00",
            "createdOnOrStartOnIso": "2020-08-11T09:00:04",
            "createdOnOrStartOn": "Tue, Aug 11, 2020 - 9:00 AM",
        },
        {
            "interactionId": "124",
            "appointmentId": "3",
            "interactionSubject": "Research",
            "interactionTeamName": "Team Red",
            "interactionAssignedToName": "Alex Great",
            "interactionMedium": "In Person",
            "interactionState": "Open",
            "interactionLastUpdatedDateOnly": "2020-08-11T09:00:04",
            "interactionCreatedOn": "2020-08-11T09:00:04",
            "appointmentStartOn": "2020-08-11T09:00:00",
            "createdOnOrStartOnIso": "2020-08-11T09:00:04",
            "createdOnOrStartOn": "Tue, Aug 11, 2020 - 9:00 AM",
        },
        {
            "interactionId": "125",
            "appointmentId": "4",
            "interactionSubject": "Lunch meeting",
            "interactionTeamName": "Team Red",
            "interactionAssignedToName": "Alex Great",
            "interactionMedium": "In Person",
            "interactionState": "Resolved",
            "interactionLastUpdatedDateOnly": "2020-08-11T09:00:04",
            "interactionCreatedOn": "2020-08-11T09:00:04",
            "appointmentStartOn": "2020-08-11T09:00:00",
            "createdOnOrStartOnIso": "2020-08-11T09:00:04",
            "createdOnOrStartOn": "Tue, Aug 11, 2020 - 9:00 AM",
        },
    ]


def get_test_messages():
    return [
        {
            "interactionId": 12345,
            "eventId": 1234567891,
            "attachmentIds": None,
            "attachments": {},
            "subject": "",
            "date": "8/11/2020 9:05:37 AM",
            "messageContent": "<p>Thanks for all the fish.</p>",
            "content": "Thanks for all the fish.",
        },
        {
            "interactionId": 12345,
            "eventId": 1234567890,
            "attachmentIds": [235, 236],
            "attachments": [
                {"attachmentId": "235", "attachmentFilename": "bar.txt",},
                {"attachmentId": "236", "attachmentFilename": "photo.png",},
            ],
            "subject": "",
            "date": "8/11/2020 9:01:00 AM",
            "messageContent": "<p>Hello world.</p>",
            "content": "Hello world.",
        },
    ]


# TODO: Fill in more values.
def get_test_interaction():
    return {
        "appointmentFk": "",
        "apptType": "",
        "aptCondition": "",
        "aptFirstName": "",
        "aptLastName": "",
        "aptName": "",
        "aptNotes": "",
        "aptReasons": "",
        "ciwiName": "",
        "ciwiReservedUserID": "",
        "contact": get_test_contact(),
        "contactId": "",
        "contactName": "",
        "createdOn": "",
        "expectedGradTerm": "",
        "honors": "",
        "id": "12345",
        "interactionPriority": "",
        "interactionState": "Open",
        "interactionThreadLastUpdated": "",
        "lastContactMessage": "",
        "lastResolvedAt": "",
        "lastUpdatedDate": "",
        "majorAsserted": "",
        "mediaType": "",
        "messageCount": "",
        "ownerId": "",
        "ownerName": "",
        "preProfAsserted": "",
        "replyState": "",
        "sessionEndTime": "",
        "sessionStartTime": "",
        "subject": "",
        "subtopic": "",
        "teamName": "",
        "topic": "",
        "unfinished": True,
    }


def get_test_contact_attachments():
    return {
        "engineering": [
            {
                "objectType": "contact",
                "contactId": "123",
                "attachmentId": "234",
                "attachmentFilename": "foo.txt",
            }
        ],
        "business": [
            {
                "objectType": "contact",
                "contactId": "123",
                "attachmentId": "235",
                "attachmentFilename": "bar.txt",
            },
            {
                "objectType": "contact",
                "contactId": "123",
                "attachmentId": "236",
                "attachmentFilename": "photo.png",
            },
        ],
    }


def get_api_test_current_user_view(request):
    return {
        "id": "999",
        "username": "notodin",
        "name": "Test O'Lastname",
        "teams": [
            {"id": 101, "name": "Team Red"},
            {"id": 102, "name": "Team Blue"},
            {"id": 103, "name": "Team Green"},
            {"id": 104, "name": "Team White"},
            {"id": 105, "name": "Team Black"},
        ],
    }


def get_api_test_current_user_route_name():
    return "ApiTestCurrentUser"


def get_api_test_filters_view(request):
    return {"teamId": 102, "userId": -1, "date": get_today_string()}


def get_api_test_filters_route_name():
    return "ApiTestFilters"


def get_api_test_users_view(request):
    return [
        {"id": "10", "name": "Zora Neal Hurston"},
        {"id": "11", "name": "Alice Walker"},
        {"id": "22", "name": "Alex Great"},
        {"id": "100", "name": "Ursula LeGuin"},
        {"id": "101", "name": "Jane Austin"},
        {"id": "110", "name": "Janice Y. K. Lee"},
        {"id": "111", "name": "Ailing Zhang"},
    ]


def get_api_test_users_route_name():
    return "ApiTestUsers"


def get_api_test_appt_users_view(request):
    return [
        {"id": "1", "name": "Nobody"},
        {"id": "10", "name": "Zora Neal Hurston"},
        {"id": "11", "name": "Alice Walker"},
        {"id": "22", "name": "Alex Great"},
        {"id": "100", "name": "Ursula LeGuin"},
        {"id": "101", "name": "Jane Austin"},
        {"id": "110", "name": "Janice Y. K. Lee"},
        {"id": "111", "name": "Ailing Zhang"},
        {"id": "1000", "name": "Someone On Another Team"},
    ]


def get_api_test_appt_users_route_name():
    return "ApiTestApptUsers"


def get_api_test_appointments_view(request):
    return [
        {
            "id": "1",
            "apptType": "scheduled",
            "condition": "Scheduled",
            "contactId": "450",
            "contactName": "Alex Lastname",
            "gradExpected": "202302",
            "honors": "yes",
            "interactionCreatedOn": f"{get_today_string()}T09:53",
            "interactionId": "97",
            "interactionOwnerId": "22",
            "interactionOwnerName": "Alex Great",
            "interactionState": "Open",
            "major": "Chemistry",
            "name": "Alex",
            "notes": "Notes go here.",
            "ownerId": "22",
            "ownerName": "Alex Great",
            "preprof": "Pre-Medicine",
            "reasons": "Reasons go here.",
            "startOn": f"{get_today_string()}T10:00",
            "subject": "Biology is easy",
            "teamId": "101",
            "teamName": "Team Red",
            "time": "10:00 AM - 10:50 AM",
        },
        {
            "id": "2",
            "apptType": "scheduled",
            "condition": "Checked In",
            "contactId": "451",
            "contactName": "Billie Lastname",
            "gradExpected": "unsure",
            "honors": "no",
            "interactionCreatedOn": f"{get_today_string()}T13:45",
            "interactionId": "98",
            "interactionOwnerId": "1",
            "interactionOwnerName": "(none)",
            "interactionState": "",
            "major": "Geology",
            "name": "Billie",
            "notes": "",
            "ownerId": "22",
            "ownerName": "Alex Great",
            "preprof": "",
            "reasons": "",
            "startOn": f"{get_today_string()}T14:00",
            "subject": "Biology is hard",
            "teamId": "101",
            "teamName": "Team Red",
            "time": "2:00 PM - 2:50 PM",
        },
        {
            "id": "3",
            "apptType": "scheduled",
            "condition": "Active",
            "contactId": "452",
            "contactName": "Carol Lastname",
            "gradExpected": "graduated",
            "honors": "",
            "interactionCreatedOn": f"{get_today_string()}T14:50",
            "interactionId": "99",
            "interactionOwnerId": "",
            "interactionOwnerName": "",
            "interactionState": "",
            "major": "Biology",
            "name": "Carol",
            "notes": "",
            "ownerId": "22",
            "ownerName": "Alex Great",
            "preprof": "",
            "reasons": "",
            "startOn": f"{get_today_string()}T15:00",
            "subject": "Biology is awesome",
            "teamId": "101",
            "teamName": "Team Red",
            "time": "3:00 PM - 3:30 PM",
        },
        {
            "id": "4",
            "apptType": "scheduled",
            "condition": "Canceled",
            "contactId": "453",
            "contactName": "DJ Lastname",
            "gradExpected": "graduated",
            "honors": "",
            "interactionCreatedOn": f"{get_today_string()}T16:00",
            "interactionId": "99",
            "interactionOwnerId": "",
            "interactionOwnerName": "",
            "interactionState": "",
            "major": "Biology",
            "name": "Carol",
            "notes": "",
            "ownerId": "22",
            "ownerName": "Alex Great",
            "preprof": "",
            "reasons": "",
            "startOn": f"{get_today_string()}T16:30",
            "subject": "Biology is awesome also",
            "teamId": "101",
            "teamName": "Team Red",
            "time": "4:30 PM - 5:00 PM",
        },
        {
            "id": "5",
            "apptType": "scheduled",
            "condition": "Finished",
            "contactId": "453",
            "contactName": "DJ Lastname",
            "gradExpected": "graduated",
            "honors": "",
            "interactionCreatedOn": f"{get_today_string()}T16:00",
            "interactionId": "99",
            "interactionOwnerId": "",
            "interactionOwnerName": "",
            "interactionState": "",
            "major": "Biology",
            "name": "Carol",
            "notes": "",
            "ownerId": "22",
            "ownerName": "Alex Great",
            "preprof": "",
            "reasons": "",
            "startOn": f"{get_today_string()}T16:30",
            "subject": "Biology is awesome also",
            "teamId": "101",
            "teamName": "Team Red",
            "time": "4:30 PM - 5:00 PM",
        },
        {
            "id": "6",
            "apptType": "scheduled",
            "condition": "No-show",
            "contactId": "453",
            "contactName": "DJ Lastname",
            "gradExpected": "graduated",
            "honors": "",
            "interactionCreatedOn": f"{get_today_string()}T16:00",
            "interactionId": "99",
            "interactionOwnerId": "",
            "interactionOwnerName": "",
            "interactionState": "",
            "major": "Biology",
            "name": "Carol",
            "notes": "",
            "ownerId": "22",
            "ownerName": "Alex Great",
            "preprof": "",
            "reasons": "",
            "startOn": f"{get_today_string()}T16:30",
            "subject": "Biology is awesome also",
            "teamId": "101",
            "teamName": "Team Red",
            "time": "4:30 PM - 5:00 PM",
        },
        {
            "id": "7",
            "apptType": "scheduled",
            "condition": "(Test)",
            "contactId": "453",
            "contactName": "DJ Lastname",
            "gradExpected": "graduated",
            "honors": "",
            "interactionCreatedOn": f"{get_today_string()}T16:00",
            "interactionId": "99",
            "interactionOwnerId": "",
            "interactionOwnerName": "",
            "interactionState": "",
            "major": "Biology",
            "name": "Carol",
            "notes": "",
            "ownerId": "22",
            "ownerName": "Alex Great",
            "preprof": "",
            "reasons": "",
            "startOn": f"{get_today_string()}T16:30",
            "subject": "Biology is awesome also",
            "teamId": "101",
            "teamName": "Team Red",
            "time": "4:30 PM - 5:00 PM",
        },
        {
            "id": "8",
            "apptType": "scheduled",
            "condition": "Scheduled",
            "contactId": "",
            "contactName": "Nobody Lastname",
            "gradExpected": "graduated",
            "honors": "",
            "interactionCreatedOn": "",
            "interactionId": "",
            "interactionOwnerId": "",
            "interactionOwnerName": "",
            "interactionState": "",
            "major": "Biology",
            "name": "Carol",
            "notes": "Testing the worst cases.",
            "ownerId": "1",
            "ownerName": "Xebeche",
            "preprof": "",
            "reasons": "",
            "startOn": f"{get_today_string()}T16:30",
            "subject": "Biology Tests",
            "teamId": "101",
            "teamName": "Team Red",
            "time": "4:30 PM - 5:00 PM",
        },
    ]


def get_api_test_appointments_route_name():
    return "ApiTestAppointments"


def get_api_test_reassign_view(request):
    return {"status": "success", "reason": "", "errors": {}, "testing": True}


def get_api_test_reassign_route_name():
    return "ApiTestReassign"


def get_api_test_take_begin_view(request):
    return {
        "status": "success",
        "reason": "",
        "errors": {},
        "testing": True,
        "appointment": {"interactionId": 98765},
    }


def get_api_test_take_begin_route_name():
    return "ApiTestTakeBegin"


def get_api_test_update_condition_view(request):
    return {"status": "success", "reason": "", "errors": {}, "testing": True}


def get_api_test_update_condition_route_name():
    return "ApiTestUpdate"


# ======== SEARCH ====================================================
def get_api_test_search_view(request):
    return [
        {
            "id": "987654321",
            "recordId": "1234",
            "name": "Alex Lastname",
            "email": "alex@foo.bar",
            "phone": "555-1212",
        },
        {
            "id": "987654321",
            "recordId": "1234",
            "name": "Billie Lastname",
            "email": "billie@foo.bar",
            "phone": "555-1212",
        },
        {
            "id": "987654321",
            "recordId": "1234",
            "name": "Carol Lastname",
            "email": "carol@foo.bar",
            "phone": "555-1212",
        },
        {
            "id": "987654321",
            "recordId": "1234",
            "name": "DJ Lastname",
            "email": "dj.the.dj@foo.bar",
            "phone": "555-1212",
        },
        {
            "id": "987654321",
            "recordId": "1234",
            "name": "Nobody Lastname",
            "email": "nobody@foo.bar",
            "phone": "555-1212",
        },
    ]


def get_api_test_search_route_name():
    return "ApiTestSearch"


# TODO: Verify the return data matches the API in operations.
def get_api_test_add_dropin_view(request):
    return {
        "status": "success",
        "reason": "",
        "errors": {},
        "testing": True,
        "appointment": {"interactionId": 98765},
    }


def get_api_test_add_dropin_route_name():
    return "ApiTestAddDropin"


def get_api_test_record_view(request):
    return {
        "attachments": get_test_contact_attachments(),
        "contact": get_test_contact(),
        "history": get_test_history(),
    }


def get_api_test_record_route_name():
    return "ApiTestRecord"


# TODO: Verify the return data matches the API in operations.
def get_api_test_add_interaction_view(request):
    return {
        "status": "success",
        "reason": "",
        "errors": {},
        "testing": True,
        "appointment": {"interactionId": 98765},
    }


def get_api_test_add_interaction_route_name():
    return "ApiTestAddInteraction"


# ======== APPOINTMENT aka INTERACTION aka CASE ======================
def get_api_test_appointment_view(request):
    return {
        "attachments": get_test_contact_attachments(),
        "contact": get_test_contact(),
        "history": get_test_history(),
        "interaction": get_test_interaction(),
        "messages": get_test_messages(),
        "pvtNote": "Private note goes here. Not everyone has one.",
    }


def get_api_test_appointment_route_name():
    return "ApiTestAppointment"


# TODO: Verify the return data matches the API in operations.
def get_api_test_add_message_view(request):
    return {
        "status": "success",
        "reason": "",
        "errors": {},
        "testing": True,
    }


def get_api_test_add_message_route_name():
    return "ApiTestAddMessage"


# TODO: Verify the return data matches the API in operations.
def get_api_test_clear_hold_view(request):
    return {
        "status": "success",
        "reason": "",
        "errors": {},
        "testing": True,
    }


def get_api_test_clear_hold_route_name():
    return "ApiTestClearHold"


# TODO: Verify the return data matches the API in operations.
def get_api_test_finish_view(request):
    return {
        "status": "success",
        "reason": "",
        "errors": {},
        "testing": True,
    }


def get_api_test_finish_route_name():
    return "ApiTestFinish"


# TODO: Verify the return data matches the API in operations.
def get_api_test_reassign_interaction_view(request):
    return {
        "status": "success",
        "reason": "",
        "errors": {},
        "testing": True,
    }


def get_api_test_reassign_interaction_route_name():
    return "ApiTestReassignInteraction"


# TODO: Verify the return data matches the API in operations.
def get_api_test_resolve_interaction_view(request):
    return {
        "status": "success",
        "reason": "",
        "errors": {},
        "testing": True,
    }


def get_api_test_resolve_interaction_route_name():
    return "ApiTestResolveInteraction"
