import json

from nose2.tools import params
import responses

from legistar.client import Legistar
from legistar.models import *


def test_build_url():
    api = Legistar("test")
    url = api._build_url("body", 42)
    expected = "https://webapi.legistar.com/v1/test/body/42"
    assert url == expected


def test_build_url_with_class_params():
    token = "9DdUbDYWLdZPl9DreGrupLvpl5MRWjjK"
    api = Legistar("test", url_params={"token": token})
    url = api._build_url("body", 42)
    expected = "https://webapi.legistar.com/v1/test/body/42?token=9DdUbDYWLdZPl9DreGrupLvpl5MRWjjK"
    assert url == expected


def test_build_url_with_method_params():
    api = Legistar("test")
    url = api._build_url("events", 42, eventitems=0)
    expected = "https://webapi.legistar.com/v1/test/events/42?eventitems=0"
    assert url == expected


def test_build_url_with_both_params():
    token = "9DdUbDYWLdZPl9DreGrupLvpl5MRWjjK"
    api = Legistar("test", url_params={"token": token})
    url = api._build_url("events", 42, eventitems=0)
    expected = "https://webapi.legistar.com/v1/test/events/42?eventitems=0&token=9DdUbDYWLdZPl9DreGrupLvpl5MRWjjK"
    assert url == expected


action_json = json.loads(
    """ 
{
            "ActionId": 42,
            "ActionGuid": "sample string 2",
            "ActionLastModifiedUtc": "2019-08-02T12:10:01.7978219-04:00",
            "ActionRowVersion": "QEA=",
            "ActionName": "sample string 4",
            "ActionActiveFlag": 5,
            "ActionUsedFlag": 6
        }
"""
)


@responses.activate
def test_action():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/actions/42",
        json=action_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.action(42)
    action = action_from_dict(action_json)
    assert resp == action


@responses.activate
def test_all_actions():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/actions",
        json=[action_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_actions()
    action = action_from_dict(action_json)
    assert resp == [action]


body_json = json.loads(
    """ 
{
            "BodyId": 1,
            "BodyGuid": "sample string 2",
            "BodyLastModifiedUtc": "2019-08-02T12:37:09.9891931-04:00",
            "BodyRowVersion": "QEA=",
            "BodyName": "sample string 4",
            "BodyTypeId": 5,
            "BodyTypeName": "sample string 6",
            "BodyMeetFlag": 7,
            "BodyActiveFlag": 8,
            "BodySort": 9,
            "BodyDescription": "sample string 10",
            "BodyContactNameId": 1,
            "BodyContactFullName": "sample string 11",
            "BodyContactPhone": "sample string 12",
            "BodyContactEmail": "sample string 13",
            "BodyUsedControlFlag": 14,
            "BodyNumberOfMembers": 15,
            "BodyUsedActingFlag": 16,
            "BodyUsedTargetFlag": 17,
            "BodyUsedSponsorFlag": 18
        }
"""
)


@responses.activate
def test_body():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/bodies/1",
        json=body_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.body(1)
    body = body_from_dict(body_json)
    assert resp == body


@responses.activate
def test_all_bodies():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/bodies",
        json=[body_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_bodies()
    body = body_from_dict(body_json)
    assert resp == [body]


body_type_json = json.loads(
    """ 
{
    "BodyTypeId": 1,
    "BodyTypeGuid": "sample string 2",
    "BodyTypeLastModifiedUtc": "2019-08-02T12:57:26.4811119-04:00",
    "BodyTypeRowVersion": "QEA=",
    "BodyTypeName": "sample string 4"
}
"""
)


@responses.activate
def test_body_type():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/bodytypes/1",
        json=body_type_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.body_type(1)
    body_type = body_type_from_dict(body_type_json)
    assert resp == body_type


@responses.activate
def test_all_body_types():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/bodytypes",
        json=[body_type_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_body_types()
    body_type = body_type_from_dict(body_type_json)
    assert resp == [body_type]


code_section_json = json.loads(
    """ 
{
    "CodeSectionId": 1,
    "CodeSectionGuid": "sample string 2",
    "CodeSectionLastModifiedUtc": "2019-08-07T11:05:24.6954449-04:00",
    "CodeSectionRowVersion": "QEA=",
    "CodeSectionNumber": "sample string 4",
    "CodeSectionName": "sample string 5",
    "CodeSectionActiveFlag": 6,
    "CodeSectionUsedFlag": 7
}
"""
)


@responses.activate
def test_code_section():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/codesections/42",
        json=code_section_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.code_section(42)
    code_section = code_section_from_dict(code_section_json)
    assert resp == code_section


@responses.activate
def test_all_code_sections():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/codesections",
        json=[code_section_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_code_sections()
    code_section = code_section_from_dict(code_section_json)
    assert resp == [code_section]


event_item_json = json.loads(
    """{
    "EventItemId": 1,
    "EventItemGuid": "sample string 2",
    "EventItemLastModifiedUtc": "2019-08-07T11:07:06.8928795-04:00",
    "EventItemRowVersion": "QEA=",
    "EventItemEventId": 4,
    "EventItemAgendaSequence": 1,
    "EventItemMinutesSequence": 1,
    "EventItemAgendaNumber": "sample string 5",
    "EventItemVideo": 1,
    "EventItemVideoIndex": 1,
    "EventItemVersion": "sample string 6",
    "EventItemAgendaNote": "sample string 7",
    "EventItemMinutesNote": "sample string 8",
    "EventItemActionId": 1,
    "EventItemActionName": "sample string 9",
    "EventItemActionText": "sample string 10",
    "EventItemPassedFlag": 1,
    "EventItemPassedFlagName": "sample string 11",
    "EventItemRollCallFlag": 1,
    "EventItemFlagExtra": 1,
    "EventItemTitle": "sample string 12",
    "EventItemTally": "sample string 13",
    "EventItemAccelaRecordId": "sample string 14",
    "EventItemConsent": 15,
    "EventItemMoverId": 1,
    "EventItemMover": "sample string 16",
    "EventItemSeconderId": 1,
    "EventItemSeconder": "sample string 17",
    "EventItemMatterId": 1,
    "EventItemMatterGuid": "sample string 18",
    "EventItemMatterFile": "sample string 19",
    "EventItemMatterName": "sample string 20",
    "EventItemMatterType": "sample string 21",
    "EventItemMatterStatus": "sample string 22",
    "EventItemMatterAttachments": [
      {
        "MatterAttachmentId": 1,
        "MatterAttachmentGuid": "sample string 2",
        "MatterAttachmentLastModifiedUtc": "2019-08-07T11:07:06.9084866-04:00",
        "MatterAttachmentRowVersion": "QEA=",
        "MatterAttachmentName": "sample string 4",
        "MatterAttachmentHyperlink": "sample string 5",
        "MatterAttachmentFileName": "sample string 6",
        "MatterAttachmentMatterVersion": "sample string 7",
        "MatterAttachmentIsHyperlink": true,
        "MatterAttachmentBinary": "QEA=",
        "MatterAttachmentIsSupportingDocument": true,
        "MatterAttachmentShowOnInternetPage": true,
        "MatterAttachmentIsMinuteOrder": true,
        "MatterAttachmentIsBoardLetter": true,
        "MatterAttachmentAgiloftId": 13,
        "MatterAttachmentDescription": "sample string 14",
        "MatterAttachmentPrintWithReports": true
      }
    ]
  }"""
)


def removekey(d, *args, child: str = ""):
    r = dict(d)
    if child:
        if type(r[child]) is list:
            for key in args:
                del r[child][0][key]
        else:
            for key in args:
                del r[child][key]
    else:
        for key in args:
            del r[key]
    return r


@responses.activate
@params(
    (
        0,
        0,
        0,
        removekey(
            event_item_json,
            "EventItemAgendaNote",
            "EventItemMinutesNote",
            "EventItemMatterAttachments",
        ),
    ),
    (
        1,
        0,
        0,
        removekey(
            event_item_json, "EventItemMinutesNote", "EventItemMatterAttachments"
        ),
    ),
    (
        0,
        1,
        0,
        removekey(event_item_json, "EventItemAgendaNote", "EventItemMatterAttachments"),
    ),
    (
        0,
        0,
        1,
        removekey(event_item_json, "EventItemAgendaNote", "EventItemMinutesNote"),
    ),
)
def test_event_item(agenda_note, minutes_note, attachments, result):
    responses.add(
        responses.GET,
        f"https://webapi.legistar.com/v1/test/events/4/eventitems/1?agendanote={agenda_note}&minutesnote={minutes_note}&attachments={attachments}",
        json=result,
        status=200,
    )
    api = Legistar("test")
    resp = api.event_item(
        4,
        1,
        agenda_note=agenda_note,
        minutes_note=minutes_note,
        attachments=attachments,
    )
    event_item = event_item_from_dict(result)
    assert resp == event_item


@responses.activate
def test_all_event_item():
    responses.add(
        responses.GET,
        f"https://webapi.legistar.com/v1/test/events/4/eventitems?agendanote=1&minutesnote=1&attachments=1",
        json=[event_item_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_event_items(4, agenda_note=1, minutes_note=1, attachments=1)
    event_item = event_item_from_dict(event_item_json)
    assert resp == [event_item]


event_json = json.loads(
    """{
  "EventId": 1,
  "EventGuid": "sample string 2",
  "EventLastModifiedUtc": "2019-08-07T17:20:06.5185459-04:00",
  "EventRowVersion": "QEA=",
  "EventBodyId": 4,
  "EventBodyName": "sample string 5",
  "EventDate": "2019-08-07T17:20:06.5185459-04:00",
  "EventTime": "sample string 6",
  "EventVideoStatus": "sample string 7",
  "EventAgendaStatusId": 8,
  "EventAgendaStatusName": "sample string 9",
  "EventMinutesStatusId": 10,
  "EventMinutesStatusName": "sample string 11",
  "EventLocation": "sample string 12",
  "EventAgendaFile": "sample string 13",
  "EventMinutesFile": "sample string 14",
  "EventAgendaLastPublishedUTC": "2019-08-07T17:20:06.5185459-04:00",
  "EventMinutesLastPublishedUTC": "2019-08-07T17:20:06.5185459-04:00",
  "EventComment": "sample string 15",
  "EventVideoPath": "sample string 16",
  "EventInSiteURL": "sample string 17",
  "EventItems": [
    {
      "EventItemId": 1,
      "EventItemGuid": "sample string 2",
      "EventItemLastModifiedUtc": "2019-08-07T17:20:06.5341535-04:00",
      "EventItemRowVersion": "QEA=",
      "EventItemEventId": 4,
      "EventItemAgendaSequence": 1,
      "EventItemMinutesSequence": 1,
      "EventItemAgendaNumber": "sample string 5",
      "EventItemVideo": 1,
      "EventItemVideoIndex": 1,
      "EventItemVersion": "sample string 6",
      "EventItemAgendaNote": "sample string 7",
      "EventItemMinutesNote": "sample string 8",
      "EventItemActionId": 1,
      "EventItemActionName": "sample string 9",
      "EventItemActionText": "sample string 10",
      "EventItemPassedFlag": 1,
      "EventItemPassedFlagName": "sample string 11",
      "EventItemRollCallFlag": 1,
      "EventItemFlagExtra": 1,
      "EventItemTitle": "sample string 12",
      "EventItemTally": "sample string 13",
      "EventItemAccelaRecordId": "sample string 14",
      "EventItemConsent": 15,
      "EventItemMoverId": 1,
      "EventItemMover": "sample string 16",
      "EventItemSeconderId": 1,
      "EventItemSeconder": "sample string 17",
      "EventItemMatterId": 1,
      "EventItemMatterGuid": "sample string 18",
      "EventItemMatterFile": "sample string 19",
      "EventItemMatterName": "sample string 20",
      "EventItemMatterType": "sample string 21",
      "EventItemMatterStatus": "sample string 22",
      "EventItemMatterAttachments": [
        {
          "MatterAttachmentId": 1,
          "MatterAttachmentGuid": "sample string 2",
          "MatterAttachmentLastModifiedUtc": "2019-08-07T17:20:06.5341535-04:00",
          "MatterAttachmentRowVersion": "QEA=",
          "MatterAttachmentName": "sample string 4",
          "MatterAttachmentHyperlink": "sample string 5",
          "MatterAttachmentFileName": "sample string 6",
          "MatterAttachmentMatterVersion": "sample string 7",
          "MatterAttachmentIsHyperlink": true,
          "MatterAttachmentBinary": "QEA=",
          "MatterAttachmentIsSupportingDocument": true,
          "MatterAttachmentShowOnInternetPage": true,
          "MatterAttachmentIsMinuteOrder": true,
          "MatterAttachmentIsBoardLetter": true,
          "MatterAttachmentAgiloftId": 13,
          "MatterAttachmentDescription": "sample string 14",
          "MatterAttachmentPrintWithReports": true
        }
      ]
    }
  ]}"""
)


@responses.activate
def test_all_events():
    responses.add(
        responses.GET,
        f"https://webapi.legistar.com/v1/test/events",
        json=[event_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_events()
    event = event_from_dict(event_json)
    assert resp == [event]


@responses.activate
@params(
    (1, 1, 1, 1, event_json),
    (
        1,
        1,
        1,
        0,
        removekey(event_json, "EventItemMatterAttachments", child="EventItems"),
    ),
    (1, 1, 0, 1, removekey(event_json, "EventItemMinutesNote", child="EventItems")),
    (1, 0, 1, 1, removekey(event_json, "EventItemAgendaNote", child="EventItems")),
    (0, 1, 1, 1, removekey(event_json, "EventItems")),
)
def test_event(event_items, agenda_note, minutes_note, event_item_attachments, result):
    responses.add(
        responses.GET,
        f"https://webapi.legistar.com/v1/test/events/1?eventitems={event_items}&agendanote={agenda_note}&minutesnote={minutes_note}&eventitemattachments={event_item_attachments}",
        json=result,
        status=200,
    )
    api = Legistar("test")
    resp = api.event(
        1,
        event_items=event_items,
        agenda_note=agenda_note,
        minutes_note=minutes_note,
        event_item_attachments=event_item_attachments,
    )
    event = event_from_dict(result)
    assert resp == event


@responses.activate
def test_event_dates_by_body():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/eventdates/1?futuredatesonly=True",
        json=["2019-08-08T19:54:05.3051663-04:00", "2019-08-08T19:54:05.3051663-04:00"],
        status=200,
    )
    api = Legistar("test")
    resp = api.event_dates_by_body(1)
    dates = [
        from_datetime(item)
        for item in [
            "2019-08-08T19:54:05.3051663-04:00",
            "2019-08-08T19:54:05.3051663-04:00",
        ]
    ]
    assert resp == dates


index_json = json.loads(
    """
{
    "IndexId": 1,
    "IndexGuid": "sample string 2",
    "IndexLastModifiedUtc": "2019-08-08T20:03:40.4824469-04:00",
    "IndexRowVersion": "QEA=",
    "IndexName": "sample string 4",
    "IndexActiveFlag": 5,
    "IndexUsedFlag": 6,
    "api_metadata": "sample string 7"
}
"""
)


@responses.activate
def test_index():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/indexes/1",
        json=index_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.index(1)
    index = index_from_dict(index_json)
    assert resp == index


@responses.activate
def test_all_indexes():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/indexes",
        json=[index_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_indexes()
    index = index_from_dict(index_json)
    assert resp == [index]


matter_attachment_json = json.loads(
    """{
    "MatterAttachmentId": 1,
    "MatterAttachmentGuid": "sample string 2",
    "MatterAttachmentLastModifiedUtc": "2019-08-08T20:16:22.1142933-04:00",
    "MatterAttachmentRowVersion": "QEA=",
    "MatterAttachmentName": "sample string 4",
    "MatterAttachmentHyperlink": "sample string 5",
    "MatterAttachmentFileName": "sample string 6",
    "MatterAttachmentMatterVersion": "sample string 7",
    "MatterAttachmentIsHyperlink": true,
    "MatterAttachmentBinary": "QEA=",
    "MatterAttachmentIsSupportingDocument": true,
    "MatterAttachmentShowOnInternetPage": true,
    "MatterAttachmentIsMinuteOrder": true,
    "MatterAttachmentIsBoardLetter": true,
    "MatterAttachmentAgiloftId": 13,
    "MatterAttachmentDescription": "sample string 14",
    "MatterAttachmentPrintWithReports": true
  }"""
)


@responses.activate
def test_all_matter_attachments():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/1/attachments",
        json=[matter_attachment_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_attachments(1)
    matter_attachment = matter_attachment_from_dict(matter_attachment_json)
    assert resp == [matter_attachment]


@responses.activate
def test_matter_attachment():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/1/attachments/1",
        json=matter_attachment_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.matter_attachment(1, 1)
    matter_attachment = matter_attachment_from_dict(matter_attachment_json)
    assert resp == matter_attachment


@responses.activate
def test_matter_attachment_file():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/1/attachments/1/file",
        body=b"\xff",
        status=200,
    )
    api = Legistar("test")
    resp = api.matter_attachment_file(1, 1)
    assert resp == b"\xff"


matter_code_section_json = json.loads(
    """{
    "MatterCodeSectionId": 1,
    "MatterCodeSectionGuid": "sample string 2",
    "MatterCodeSectionLastModifiedUtc": "2019-08-09T20:37:51.0494239-04:00",
    "MatterCodeSectionRowVersion": "QEA=",
    "MatterCodeSectionMatterId": 4,
    "MatterCodeSectionCodeSectionId": 5,
    "MatterCodeSectionNumber": "sample string 6",
    "MatterCodeSectionName": "sample string 7"
  }"""
)


@responses.activate
def test_matter_code_section():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/4/codesections/1",
        json=matter_code_section_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.matter_code_section(4, 1)
    matter_code_section = matter_code_section_from_dict(matter_code_section_json)
    assert resp == matter_code_section


@responses.activate
def test_all_matter_code_sections():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/4/codesections",
        json=[matter_code_section_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_code_sections(4)
    matter_code_section = matter_code_section_from_dict(matter_code_section_json)
    assert resp == [matter_code_section]


matter_history_json = json.loads(
    """ 
{
    "MatterHistoryId": 1,
    "MatterHistoryGuid": "sample string 2",
    "MatterHistoryLastModifiedUtc": "2019-08-12T20:47:38.3612083-04:00",
    "MatterHistoryRowVersion": "QEA=",
    "MatterHistoryEventId": 1,
    "MatterHistoryAgendaSequence": 1,
    "MatterHistoryMinutesSequence": 1,
    "MatterHistoryAgendaNumber": "sample string 4",
    "MatterHistoryVideo": 1,
    "MatterHistoryVideoIndex": 1,
    "MatterHistoryVersion": "sample string 5",
    "MatterHistoryAgendaNote": "sample string 6",
    "MatterHistoryMinutesNote": "sample string 7",
    "MatterHistoryActionDate": "2019-08-12T20:47:38.3612083-04:00",
    "MatterHistoryActionId": 1,
    "MatterHistoryActionName": "sample string 8",
    "MatterHistoryActionText": "sample string 9",
    "MatterHistoryActionBodyId": 1,
    "MatterHistoryActionBodyName": "sample string 10",
    "MatterHistoryPassedFlag": 1,
    "MatterHistoryPassedFlagName": "sample string 11",
    "MatterHistoryRollCallFlag": 1,
    "MatterHistoryFlagExtra": 1,
    "MatterHistoryTally": "sample string 12",
    "MatterHistoryAccelaRecordId": "sample string 13",
    "MatterHistoryConsent": 14,
    "MatterHistoryMoverId": 1,
    "MatterHistoryMoverName": "sample string 15",
    "MatterHistorySeconderId": 1,
    "MatterHistorySeconderName": "sample string 16",
    "MatterHistoryMatterStatusId": 1
  }
"""
)


@responses.activate
@params(
    (1, 1, matter_history_json),
    (1, 0, removekey(matter_history_json, "MatterHistoryAgendaNote")),
    (0, 1, removekey(matter_history_json, "MatterHistoryMinutesNote")),
)
def test_matter_history(agenda_note, minutes_note, result):
    responses.add(
        responses.GET,
        f"https://webapi.legistar.com/v1/test/matters/1/histories/1?agendanote={agenda_note}&minutesnote={minutes_note}",
        json=result,
        status=200,
    )
    api = Legistar("test")
    resp = api.matter_history(1, 1, agenda_note=agenda_note, minutes_note=minutes_note)
    matter_history = matter_history_from_dict(result)
    assert resp == matter_history


@responses.activate
@params(
    (1, 1, matter_history_json),
    (1, 0, removekey(matter_history_json, "MatterHistoryAgendaNote")),
    (0, 1, removekey(matter_history_json, "MatterHistoryMinutesNote")),
)
def test_all_matter_histories(agenda_note, minutes_note, result):
    responses.add(
        responses.GET,
        f"https://webapi.legistar.com/v1/test/matters/1/histories?agendanote={agenda_note}&minutesnote={minutes_note}",
        json=[result],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_histories(
        1, agenda_note=agenda_note, minutes_note=minutes_note
    )
    matter_history = matter_history_from_dict(result)
    assert resp == [matter_history]


matter_text_json = json.loads(
    """
{
  "MatterTextId": 1,
  "MatterTextGuid": "sample string 2",
  "MatterTextLastModifiedUtc": "2019-08-12T20:48:45.0853262-04:00",
  "MatterTextRowVersion": "QEA=",
  "MatterTextMatterId": 4,
  "MatterTextVersion": "sample string 5",
  "MatterTextPlain": "sample string 6",
  "MatterTextRtf": "sample string 7"
}
"""
)


@responses.activate
def test_matter_text():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/4/texts/1",
        json=matter_text_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.matter_text(4, 1)
    matter_text = matter_text_from_dict(matter_text_json)
    assert resp == matter_text


@responses.activate
def test_all_matter_texts_version_by_matter():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/4/versions",
        json=[{"Key": "sample string 1", "Value": "sample string 2"}],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_texts_version_by_matter(4)
    matter_text_version = matter_text_version_from_dict(
        {"Key": "sample string 1", "Value": "sample string 2"}
    )
    assert resp == [matter_text_version]


matter_index_json = json.loads(
    """ 
{
    "MatterIndexId": 1,
    "MatterIndexGuid": "sample string 2",
    "MatterIndexLastModifiedUtc": "2019-08-12T20:51:18.4507871-04:00",
    "MatterIndexRowVersion": "QEA=",
    "MatterIndexMatterId": 4,
    "MatterIndexIndexId": 5,
    "MatterIndexName": "sample string 6"
  }
"""
)


@responses.activate
def test_all_matter_indexes_by_matter():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matterindexes/matter/4",
        json=[matter_index_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_indexes_by_matter(4)
    matter_index = matter_index_from_dict(matter_index_json)
    assert resp == [matter_index]


@responses.activate
def test_all_matter_indexes_by_index():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matterindexes/index/1",
        json=[matter_index_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_indexes_by_index(1)
    matter_index = matter_index_from_dict(matter_index_json)
    assert resp == [matter_index]


@responses.activate
def test_all_matter_indexes():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matterindexes",
        json=[matter_index_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_indexes()
    matter_index = matter_index_from_dict(matter_index_json)
    assert resp == [matter_index]


@responses.activate
def test_matter_index():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matterindexes/1",
        json=matter_index_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.matter_index(1)
    matter_index = matter_index_from_dict(matter_index_json)
    assert resp == matter_index


matter_relation_json = json.loads(
    """{
    "MatterRelationId": 1,
    "MatterRelationGuid": "sample string 2",
    "MatterRelationLastModifiedUtc": "2019-08-12T20:52:22.9975238-04:00",
    "MatterRelationRowVersion": "QEA=",
    "MatterRelationMatterId": 3,
    "MatterRelationFlag": 4
  }"""
)


@responses.activate
def test_all_matter_relations():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/3/relations",
        json=[matter_relation_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_relations(3)
    matter_relation = matter_relation_from_dict(matter_relation_json)
    assert resp == [matter_relation]


@responses.activate
def test_matter_relation():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/3/relations/1",
        json=matter_relation_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.matter_relation(3, 1)
    matter_relation = matter_relation_from_dict(matter_relation_json)
    assert resp == matter_relation


matter_sponsor_json = json.loads(
    """ 
{
    "MatterSponsorId": 1,
    "MatterSponsorGuid": "sample string 2",
    "MatterSponsorLastModifiedUtc": "2019-08-12T20:52:56.5101933-04:00",
    "MatterSponsorRowVersion": "QEA=",
    "MatterSponsorMatterId": 4,
    "MatterSponsorMatterVersion": "sample string 5",
    "MatterSponsorNameId": 1,
    "MatterSponsorBodyId": 1,
    "MatterSponsorName": "sample string 6",
    "MatterSponsorSequence": 7,
    "MatterSponsorLinkFlag": 8
  }
"""
)


@responses.activate
def test_all_matter_sponsors():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/4/sponsors",
        json=[matter_sponsor_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_sponsors(4)
    matter_sponsor = matter_sponsor_from_dict(matter_sponsor_json)
    assert resp == [matter_sponsor]


@responses.activate
def test_matter_sponsor():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/3/sponsors/1",
        json=matter_sponsor_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.matter_sponsor(3, 1)
    matter_sponsor = matter_sponsor_from_dict(matter_sponsor_json)
    assert resp == matter_sponsor


matter_status_json = json.loads(
    """ 
{
    "MatterStatusId": 1,
    "MatterStatusGuid": "sample string 2",
    "MatterStatusLastModifiedUtc": "2019-08-12T20:53:28.9643135-04:00",
    "MatterStatusRowVersion": "QEA=",
    "MatterStatusName": "sample string 4",
    "MatterStatusSort": 5,
    "MatterStatusActiveFlag": 6,
    "MatterStatusDescription": "sample string 7",
    "MatterStatusUsedFlag": 8,
    "MatterStatusPublicFlag": 9
  }
"""
)


@responses.activate
def test_all_matter_statuses():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matterstatuses",
        json=[matter_status_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_statuses()
    matter_status = matter_status_from_dict(matter_status_json)
    assert resp == [matter_status]


@responses.activate
def test_matter_status():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matterstatuses/1",
        json=matter_status_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.matter_status(1)
    matter_status = matter_status_from_dict(matter_status_json)
    assert resp == matter_status


matter_requester_json = json.loads(
    """
{
    "MatterRequesterName": "sample string 1"
  }
"""
)


@responses.activate
def test_all_matter_requesters():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matterrequesters",
        json=[matter_requester_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_requesters()
    matter_requester = matter_requester_from_dict(matter_requester_json)
    assert resp == [matter_requester]


matter_json = json.loads(
    """
{
    "MatterId": 1,
    "MatterGuid": "sample string 2",
    "MatterLastModifiedUtc": "2019-08-13T19:27:31.4772144-04:00",
    "MatterRowVersion": "QEA=",
    "MatterFile": "sample string 3",
    "MatterName": "sample string 4",
    "MatterTitle": "sample string 5",
    "MatterTypeId": 6,
    "MatterTypeName": "sample string 7",
    "MatterStatusId": 8,
    "MatterStatusName": "sample string 9",
    "MatterBodyId": 10,
    "MatterBodyName": "sample string 11",
    "MatterIntroDate": "2019-08-13T19:27:31.4772144-04:00",
    "MatterAgendaDate": "2019-08-13T19:27:31.4772144-04:00",
    "MatterPassedDate": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEnactmentDate": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEnactmentNumber": "sample string 12",
    "MatterRequester": "sample string 13",
    "MatterNotes": "sample string 14",
    "MatterVersion": "sample string 15",
    "MatterText1": "sample string 16",
    "MatterText2": "sample string 17",
    "MatterText3": "sample string 18",
    "MatterText4": "sample string 19",
    "MatterText5": "sample string 20",
    "MatterDate1": "2019-08-13T19:27:31.4772144-04:00",
    "MatterDate2": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEXText1": "sample string 21",
    "MatterEXText2": "sample string 22",
    "MatterEXText3": "sample string 23",
    "MatterEXText4": "sample string 24",
    "MatterEXText5": "sample string 25",
    "MatterEXText6": "sample string 26",
    "MatterEXText7": "sample string 27",
    "MatterEXText8": "sample string 28",
    "MatterEXText9": "sample string 29",
    "MatterEXText10": "sample string 30",
    "MatterEXText11": "sample string 31",
    "MatterEXDate1": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEXDate2": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEXDate3": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEXDate4": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEXDate5": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEXDate6": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEXDate7": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEXDate8": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEXDate9": "2019-08-13T19:27:31.4772144-04:00",
    "MatterEXDate10": "2019-08-13T19:27:31.4928443-04:00",
    "MatterAgiloftId": 32,
    "MatterReference": "sample string 33",
    "MatterRestrictViewViaWeb": true,
    "MatterReports": [
      {
        "ReportName": "Legislation Details",
        "ReportURL": "http://example.com/ViewReport.ashx?M=R&N=Master&GID=000&LEGID=0000&Title=Legislation+Details",
        "ReportType": "InSite"
      },
      {
        "ReportName": "Legislation Details",
        "ReportURL": "http://example.com/ViewReport.ashx?M=R&N=Master&GID=000&LEGID=0000&Title=Legislation+Details",
        "ReportType": "InSite"
      }
    ]
  }
 """
)


@responses.activate
def test_all_matters():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters",
        json=[matter_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matters()
    matter = matter_from_dict(matter_json)
    assert resp == [matter]


@responses.activate
def test_matter():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/matters/1",
        json=matter_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.matter(1)
    matter = matter_from_dict(matter_json)
    assert resp == matter


matter_type_json = json.loads(
    """
{
    "MatterTypeId": 1,
    "MatterTypeGuid": "sample string 2",
    "MatterTypeLastModifiedUtc": "2019-08-13T19:44:28.3103336-04:00",
    "MatterTypeRowVersion": "QEA=",
    "MatterTypeName": "sample string 4",
    "MatterTypeSort": 5,
    "MatterTypeActiveFlag": 6,
    "MatterTypeDescription": "sample string 7",
    "MatterTypeUsedFlag": 8
  }

"""
)


@responses.activate
def test_all_matter_types():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/mattertypes",
        json=[matter_type_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_matter_types()
    matter_type = matter_type_from_dict(matter_type_json)
    assert resp == [matter_type]


@responses.activate
def test_matter_type():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/mattertypes/1",
        json=matter_type_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.matter_type(1)
    matter_type = matter_type_from_dict(matter_type_json)
    assert resp == matter_type


office_record_json = json.loads(
    """
{
    "OfficeRecordId": 1,
    "OfficeRecordGuid": "sample string 2",
    "OfficeRecordLastModifiedUtc": "2019-08-13T19:46:45.9123781-04:00",
    "OfficeRecordRowVersion": "QEA=",
    "OfficeRecordFirstName": "sample string 4",
    "OfficeRecordLastName": "sample string 5",
    "OfficeRecordEmail": "sample string 6",
    "OfficeRecordFullName": "sample string 7",
    "OfficeRecordStartDate": "2019-08-13T19:46:45.9123781-04:00",
    "OfficeRecordEndDate": "2019-08-13T19:46:45.9123781-04:00",
    "OfficeRecordSort": 9,
    "OfficeRecordPersonId": 10,
    "OfficeRecordBodyId": 11,
    "OfficeRecordBodyName": "sample string 12",
    "OfficeRecordTitle": "sample string 13",
    "OfficeRecordVoteDivider": 14.1,
    "OfficeRecordExtendFlag": 15,
    "OfficeRecordMemberTypeId": 16,
    "OfficeRecordMemberType": "sample string 17",
    "OfficeRecordSupportNameId": 1,
    "OfficeRecordSupportFullName": "sample string 18"
  }
"""
)


@responses.activate
def test_all_office_records():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/officerecords",
        json=[office_record_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_office_records()
    office_record = office_record_from_dict(office_record_json)
    assert resp == [office_record]


@responses.activate
def test_office_record():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/officerecords/1",
        json=office_record_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.office_record(1)
    office_record = office_record_from_dict(office_record_json)
    assert resp == office_record


@responses.activate
def test_all_office_records_by_person():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/persons/10/officerecords",
        json=[office_record_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_office_records_by_person(10)
    office_record = office_record_from_dict(office_record_json)
    assert resp == [office_record]


@responses.activate
def test_all_office_records_by_body():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/bodies/11/officerecords",
        json=[office_record_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_office_records_by_body(11)
    office_record = office_record_from_dict(office_record_json)
    assert resp == [office_record]


person_json = json.loads(
    """
{
    "PersonId": 1,
    "PersonGuid": "sample string 2",
    "PersonLastModifiedUtc": "2019-08-13T19:53:45.5516634-04:00",
    "PersonRowVersion": "QEA=",
    "PersonFirstName": "sample string 4",
    "PersonLastName": "sample string 5",
    "PersonFullName": "sample string 6",
    "PersonActiveFlag": 7,
    "PersonUsedSponsorFlag": 8,
    "PersonAddress1": "sample string 9",
    "PersonCity1": "sample string 10",
    "PersonState1": "sample string 11",
    "PersonZip1": "sample string 12",
    "PersonPhone": "sample string 13",
    "PersonFax": "sample string 14",
    "PersonEmail": "sample string 15",
    "PersonWWW": "sample string 16",
    "PersonAddress2": "sample string 17",
    "PersonCity2": "sample string 18",
    "PersonState2": "sample string 19",
    "PersonZip2": "sample string 20",
    "PersonPhone2": "sample string 21",
    "PersonFax2": "sample string 22",
    "PersonEmail2": "sample string 23",
    "PersonWWW2": "sample string 24"
  }
"""
)


@responses.activate
def test_all_persons():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/persons",
        json=[person_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_persons()
    person = person_from_dict(person_json)
    assert resp == [person]


@responses.activate
def test_person():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/persons/1",
        json=person_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.person(1)
    person = person_from_dict(person_json)
    assert resp == person


roll_call_json = json.loads(
    """
{
    "RollCallId": 1,
    "RollCallGuid": "sample string 2",
    "RollCallLastModifiedUtc": "2019-08-13T19:55:04.0158521-04:00",
    "RollCallRowVersion": "QEA=",
    "RollCallPersonId": 4,
    "RollCallPersonName": "sample string 5",
    "RollCallValueId": 1,
    "RollCallValueName": "sample string 6",
    "RollCallSort": 7,
    "RollCallResult": 1,
    "RollCallEventItemId": 8
  }
"""
)


@responses.activate
def test_all_roll_calls_by_event_item():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/eventitems/8/rollcalls",
        json=[roll_call_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_roll_calls_by_event_item(8)
    roll_call = roll_call_from_dict(roll_call_json)
    assert resp == [roll_call]


@responses.activate
def test_roll_call_by_event_item():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/eventitems/8/rollcalls/1",
        json=roll_call_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.roll_call_by_event_item(8, 1)
    roll_call = roll_call_from_dict(roll_call_json)
    assert resp == roll_call


@responses.activate
def test_all_roll_calls_by_person():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/persons/4/rollcalls",
        json=[roll_call_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_roll_calls_by_person(4)
    roll_call = roll_call_from_dict(roll_call_json)
    assert resp == [roll_call]


vote_json = json.loads(
    """
{
    "VoteId": 1,
    "VoteGuid": "sample string 2",
    "VoteLastModifiedUtc": "2019-08-13T19:57:51.3850647-04:00",
    "VoteRowVersion": "QEA=",
    "VotePersonId": 4,
    "VotePersonName": "sample string 5",
    "VoteValueId": 1,
    "VoteValueName": "sample string 6",
    "VoteSort": 7,
    "VoteResult": 1,
    "VoteEventItemId": 8
  }
"""
)


@responses.activate
def test_all_votes_by_event_item():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/eventitems/8/votes",
        json=[vote_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_votes_by_event_item(8)
    vote = vote_from_dict(vote_json)
    assert resp == [vote]


@responses.activate
def test_vote_by_event_item():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/eventitems/8/votes/1",
        json=vote_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.vote_by_event_item(8, 1)
    vote = vote_from_dict(vote_json)
    assert resp == vote


@responses.activate
def test_all_votes_by_person():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/persons/1/votes",
        json=[vote_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_votes_by_person(1)
    vote = vote_from_dict(vote_json)
    assert resp == [vote]


vote_type_json = json.loads(
    """
{
    "VoteTypeId": 1,
    "VoteTypeGuid": "sample string 2",
    "VoteTypeLastModifiedUtc": "2019-08-13T19:58:03.9835808-04:00",
    "VoteTypeRowVersion": "QEA=",
    "VoteTypeName": "sample string 4",
    "VoteTypePluralName": "sample string 5",
    "VoteTypeUsedFor": 6,
    "VoteTypeResult": 7,
    "VoteTypeSort": 8
  }
"""
)


@responses.activate
def test_all_vote_types():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/votetypes",
        json=[vote_type_json],
        status=200,
    )
    api = Legistar("test")
    resp = api.all_vote_types()
    vote_type = vote_type_from_dict(vote_type_json)
    assert resp == [vote_type]


@responses.activate
def test_vote_type():
    responses.add(
        responses.GET,
        "https://webapi.legistar.com/v1/test/votetypes/1",
        json=vote_type_json,
        status=200,
    )
    api = Legistar("test")
    resp = api.vote_type(1)
    vote_type = vote_type_from_dict(vote_type_json)
    assert resp == vote_type
