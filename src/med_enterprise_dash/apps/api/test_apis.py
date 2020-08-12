from pyramid.view import view_config


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
    return {"teamId": 102, "userId": -1, "date": "2020-08-10"}


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
            "interactionCreatedOn": "2020-08-10T09:53",
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
            "startOn": "2020-08-10T10:00",
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
            "interactionCreatedOn": "2020-08-10T13:45",
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
            "startOn": "2020-08-10T14:00",
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
            "interactionCreatedOn": "2020-08-10T14:50",
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
            "startOn": "2020-08-10T15:00",
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
            "interactionCreatedOn": "2020-08-10T16:00",
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
            "startOn": "2020-08-10T16:30",
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
            "interactionCreatedOn": "2020-08-10T16:00",
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
            "startOn": "2020-08-10T16:30",
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
            "interactionCreatedOn": "2020-08-10T16:00",
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
            "startOn": "2020-08-10T16:30",
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
            "interactionCreatedOn": "2020-08-10T16:00",
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
            "startOn": "2020-08-10T16:30",
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
            "startOn": "2020-08-10T16:30",
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


def get_api_test_record_view(request):
    return {"stub": True}


def get_api_test_record_route_name():
    return "ApiTestRecord"
