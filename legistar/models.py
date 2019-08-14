from dataclasses import dataclass
import json
from typing import Any, Callable, Optional, TypeVar, Type, cast, List
from datetime import datetime
import dateutil.parser

T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Action:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    name: Optional[str]
    active_flag: Optional[int]
    used_flag: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> "Action":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("ActionId"))
        guid = from_union([from_str, from_none], obj.get("ActionGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("ActionLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("ActionRowVersion"))
        name = from_union([from_str, from_none], obj.get("ActionName"))
        active_flag = from_union([from_int, from_none], obj.get("ActionActiveFlag"))
        used_flag = from_union([from_int, from_none], obj.get("ActionUsedFlag"))
        return Action(
            id, guid, last_modified_utc, row_version, name, active_flag, used_flag
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["ActionId"] = from_union([from_int, from_none], self.id)
        result["ActionGuid"] = from_union([from_str, from_none], self.guid)
        result["ActionLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["ActionRowVersion"] = from_union([from_str, from_none], self.row_version)
        result["ActionName"] = from_union([from_str, from_none], self.name)
        result["ActionActiveFlag"] = from_union([from_int, from_none], self.active_flag)
        result["ActionUsedFlag"] = from_union([from_int, from_none], self.used_flag)
        return result


def action_from_dict(s: Any) -> Action:
    return Action.from_dict(s)


def action_to_dict(x: Action) -> Any:
    return to_class(Action, x)


@dataclass
class Body:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    name: Optional[str]
    type_id: Optional[int]
    type_name: Optional[str]
    meet_flag: Optional[int]
    active_flag: Optional[int]
    sort: Optional[int]
    description: Optional[str]
    contact_name_id: Optional[int]
    contact_full_name: Optional[str]
    contact_phone: Optional[str]
    contact_email: Optional[str]
    used_control_flag: Optional[int]
    number_of_members: Optional[int]
    used_acting_flag: Optional[int]
    used_target_flag: Optional[int]
    used_sponsor_flag: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> "Body":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("BodyId"))
        guid = from_union([from_str, from_none], obj.get("BodyGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("BodyLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("BodyRowVersion"))
        name = from_union([from_str, from_none], obj.get("BodyName"))
        type_id = from_union([from_int, from_none], obj.get("BodyTypeId"))
        type_name = from_union([from_str, from_none], obj.get("BodyTypeName"))
        meet_flag = from_union([from_int, from_none], obj.get("BodyMeetFlag"))
        active_flag = from_union([from_int, from_none], obj.get("BodyActiveFlag"))
        sort = from_union([from_int, from_none], obj.get("BodySort"))
        description = from_union([from_str, from_none], obj.get("BodyDescription"))
        contact_name_id = from_union(
            [from_int, from_none], obj.get("BodyContactNameId")
        )
        contact_full_name = from_union(
            [from_str, from_none], obj.get("BodyContactFullName")
        )
        contact_phone = from_union([from_str, from_none], obj.get("BodyContactPhone"))
        contact_email = from_union([from_str, from_none], obj.get("BodyContactEmail"))
        used_control_flag = from_union(
            [from_int, from_none], obj.get("BodyUsedControlFlag")
        )
        number_of_members = from_union(
            [from_int, from_none], obj.get("BodyNumberOfMembers")
        )
        used_acting_flag = from_union(
            [from_int, from_none], obj.get("BodyUsedActingFlag")
        )
        used_target_flag = from_union(
            [from_int, from_none], obj.get("BodyUsedTargetFlag")
        )
        used_sponsor_flag = from_union(
            [from_int, from_none], obj.get("BodyUsedSponsorFlag")
        )
        return Body(
            id,
            guid,
            last_modified_utc,
            row_version,
            name,
            type_id,
            type_name,
            meet_flag,
            active_flag,
            sort,
            description,
            contact_name_id,
            contact_full_name,
            contact_phone,
            contact_email,
            used_control_flag,
            number_of_members,
            used_acting_flag,
            used_target_flag,
            used_sponsor_flag,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["BodyId"] = from_union([from_int, from_none], self.id)
        result["BodyGuid"] = from_union([from_str, from_none], self.guid)
        result["BodyLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["BodyRowVersion"] = from_union([from_str, from_none], self.row_version)
        result["BodyName"] = from_union([from_str, from_none], self.name)
        result["BodyTypeId"] = from_union([from_int, from_none], self.type_id)
        result["BodyTypeName"] = from_union([from_str, from_none], self.type_name)
        result["BodyMeetFlag"] = from_union([from_int, from_none], self.meet_flag)
        result["BodyActiveFlag"] = from_union([from_int, from_none], self.active_flag)
        result["BodySort"] = from_union([from_int, from_none], self.sort)
        result["BodyDescription"] = from_union([from_str, from_none], self.description)
        result["BodyContactNameId"] = from_union(
            [from_int, from_none], self.contact_name_id
        )
        result["BodyContactFullName"] = from_union(
            [from_str, from_none], self.contact_full_name
        )
        result["BodyContactPhone"] = from_union(
            [from_str, from_none], self.contact_phone
        )
        result["BodyContactEmail"] = from_union(
            [from_str, from_none], self.contact_email
        )
        result["BodyUsedControlFlag"] = from_union(
            [from_int, from_none], self.used_control_flag
        )
        result["BodyNumberOfMembers"] = from_union(
            [from_int, from_none], self.number_of_members
        )
        result["BodyUsedActingFlag"] = from_union(
            [from_int, from_none], self.used_acting_flag
        )
        result["BodyUsedTargetFlag"] = from_union(
            [from_int, from_none], self.used_target_flag
        )
        result["BodyUsedSponsorFlag"] = from_union(
            [from_int, from_none], self.used_sponsor_flag
        )
        return result


def body_from_dict(s: Any) -> Body:
    return Body.from_dict(s)


def body_to_dict(x: Body) -> Any:
    return to_class(Body, x)


@dataclass
class BodyType:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    name: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "BodyType":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("BodyTypeId"))
        guid = from_union([from_str, from_none], obj.get("BodyTypeGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("BodyTypeLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("BodyTypeRowVersion"))
        name = from_union([from_str, from_none], obj.get("BodyTypeName"))
        return BodyType(id, guid, last_modified_utc, row_version, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["BodyTypeId"] = from_union([from_int, from_none], self.id)
        result["BodyTypeGuid"] = from_union([from_str, from_none], self.guid)
        result["BodyTypeLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["BodyTypeRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["BodyTypeName"] = from_union([from_str, from_none], self.name)
        return result


def body_type_from_dict(s: Any) -> BodyType:
    return BodyType.from_dict(s)


def body_type_to_dict(x: BodyType) -> Any:
    return to_class(BodyType, x)


@dataclass
class CodeSection:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    number: Optional[str]
    name: Optional[str]
    active_flag: Optional[int]
    used_flag: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> "CodeSection":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("CodeSectionId"))
        guid = from_union([from_str, from_none], obj.get("CodeSectionGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("CodeSectionLastModifiedUtc")
        )
        row_version = from_union(
            [from_str, from_none], obj.get("CodeSectionRowVersion")
        )
        number = from_union([from_str, from_none], obj.get("CodeSectionNumber"))
        name = from_union([from_str, from_none], obj.get("CodeSectionName"))
        active_flag = from_union(
            [from_int, from_none], obj.get("CodeSectionActiveFlag")
        )
        used_flag = from_union([from_int, from_none], obj.get("CodeSectionUsedFlag"))
        return CodeSection(
            id,
            guid,
            last_modified_utc,
            row_version,
            number,
            name,
            active_flag,
            used_flag,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["CodeSectionId"] = from_union([from_int, from_none], self.id)
        result["CodeSectionGuid"] = from_union([from_str, from_none], self.guid)
        result["CodeSectionLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["CodeSectionRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["CodeSectionNumber"] = from_union([from_str, from_none], self.number)
        result["CodeSectionName"] = from_union([from_str, from_none], self.name)
        result["CodeSectionActiveFlag"] = from_union(
            [from_int, from_none], self.active_flag
        )
        result["CodeSectionUsedFlag"] = from_union(
            [from_int, from_none], self.used_flag
        )
        return result


def code_section_from_dict(s: Any) -> CodeSection:
    return CodeSection.from_dict(s)


def code_section_to_dict(x: CodeSection) -> Any:
    return to_class(CodeSection, x)


@dataclass
class MatterAttachment:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    name: Optional[str]
    hyperlink: Optional[str]
    file_name: Optional[str]
    matter_version: Optional[str]
    is_hyperlink: Optional[bool]
    binary: Optional[str]
    is_supporting_document: Optional[bool]
    show_on_internet_page: Optional[bool]
    is_minute_order: Optional[bool]
    is_board_letter: Optional[bool]
    agiloft_id: Optional[int]
    description: Optional[str]
    print_with_reports: Optional[bool]

    @staticmethod
    def from_dict(obj: Any) -> "MatterAttachment":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("MatterAttachmentId"))
        guid = from_union([from_str, from_none], obj.get("MatterAttachmentGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("MatterAttachmentLastModifiedUtc")
        )
        row_version = from_union(
            [from_str, from_none], obj.get("MatterAttachmentRowVersion")
        )
        name = from_union([from_str, from_none], obj.get("MatterAttachmentName"))
        hyperlink = from_union(
            [from_str, from_none], obj.get("MatterAttachmentHyperlink")
        )
        file_name = from_union(
            [from_str, from_none], obj.get("MatterAttachmentFileName")
        )
        matter_version = from_union(
            [from_str, from_none], obj.get("MatterAttachmentMatterVersion")
        )
        is_hyperlink = from_union(
            [from_bool, from_none], obj.get("MatterAttachmentIsHyperlink")
        )
        binary = from_union([from_str, from_none], obj.get("MatterAttachmentBinary"))
        is_supporting_document = from_bool(
            obj.get("MatterAttachmentIsSupportingDocument")
        )
        show_on_internet_page = from_union(
            [from_bool, from_none], obj.get("MatterAttachmentShowOnInternetPage")
        )
        is_minute_order = from_union(
            [from_bool, from_none], obj.get("MatterAttachmentIsMinuteOrder")
        )
        is_board_letter = from_union(
            [from_bool, from_none], obj.get("MatterAttachmentIsBoardLetter")
        )
        agiloft_id = from_union(
            [from_int, from_none], obj.get("MatterAttachmentAgiloftId")
        )
        description = from_union(
            [from_str, from_none], obj.get("MatterAttachmentDescription")
        )
        print_with_reports = from_union(
            [from_bool, from_none], obj.get("MatterAttachmentPrintWithReports")
        )
        return MatterAttachment(
            id,
            guid,
            last_modified_utc,
            row_version,
            name,
            hyperlink,
            file_name,
            matter_version,
            is_hyperlink,
            binary,
            is_supporting_document,
            show_on_internet_page,
            is_minute_order,
            is_board_letter,
            agiloft_id,
            description,
            print_with_reports,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatterAttachmentId"] = from_union([from_int, from_none], self.id)
        result["MatterAttachmentGuid"] = from_union([from_str, from_none], self.guid)
        result["MatterAttachmentLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["MatterAttachmentRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["MatterAttachmentName"] = from_union([from_str, from_none], self.name)
        result["MatterAttachmentHyperlink"] = from_union(
            [from_str, from_none], self.hyperlink
        )
        result["MatterAttachmentFileName"] = from_union(
            [from_str, from_none], self.file_name
        )
        result["MatterAttachmentMatterVersion"] = from_union(
            [from_str, from_none], self.matter_version
        )
        result["MatterAttachmentIsHyperlink"] = from_union(
            [from_bool, from_none], self.is_hyperlink
        )
        result["MatterAttachmentBinary"] = from_union(
            [from_str, from_none], self.binary
        )
        result["MatterAttachmentIsSupportingDocument"] = from_bool(
            self.is_supporting_document
        )
        result["MatterAttachmentShowOnInternetPage"] = from_bool(
            self.show_on_internet_page
        )
        result["MatterAttachmentIsMinuteOrder"] = from_union(
            [from_bool, from_none], self.is_minute_order
        )
        result["MatterAttachmentIsBoardLetter"] = from_union(
            [from_bool, from_none], self.is_board_letter
        )
        result["MatterAttachmentAgiloftId"] = from_union(
            [from_int, from_none], self.agiloft_id
        )
        result["MatterAttachmentDescription"] = from_union(
            [from_str, from_none], self.description
        )
        result["MatterAttachmentPrintWithReports"] = from_union(
            [from_bool, from_none], self.print_with_reports
        )
        return result


def matter_attachment_from_dict(s: Any) -> MatterAttachment:
    return MatterAttachment.from_dict(s)


def matter_attachment_to_dict(x: MatterAttachment) -> Any:
    return to_class(MatterAttachment, x)


@dataclass
class EventItem:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    event_id: Optional[int]
    agenda_sequence: Optional[int]
    minutes_sequence: Optional[int]
    agenda_number: Optional[str]
    video: Optional[int]
    video_index: Optional[int]
    version: Optional[str]
    agenda_note: Optional[str]
    minutes_note: Optional[str]
    action_id: Optional[int]
    action_name: Optional[str]
    action_text: Optional[str]
    passed_flag: Optional[int]
    passed_flag_name: Optional[str]
    roll_call_flag: Optional[int]
    flag_extra: Optional[int]
    title: Optional[str]
    tally: Optional[str]
    accela_record_id: Optional[str]
    consent: Optional[int]
    mover_id: Optional[int]
    mover: Optional[str]
    seconder_id: Optional[int]
    seconder: Optional[str]
    matter_id: Optional[int]
    matter_guid: Optional[str]
    matter_file: Optional[str]
    matter_name: Optional[str]
    matter_type: Optional[str]
    matter_status: Optional[str]
    matter_attachments: Optional[List[MatterAttachment]]

    @staticmethod
    def from_dict(obj: Any) -> "EventItem":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("EventItemId"))
        guid = from_union([from_str, from_none], obj.get("EventItemGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("EventItemLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("EventItemRowVersion"))
        event_id = from_union([from_int, from_none], obj.get("EventItemEventId"))
        agenda_sequence = from_union(
            [from_int, from_none], obj.get("EventItemAgendaSequence")
        )
        minutes_sequence = from_union(
            [from_int, from_none], obj.get("EventItemMinutesSequence")
        )
        agenda_number = from_union(
            [from_str, from_none], obj.get("EventItemAgendaNumber")
        )
        video = from_union([from_int, from_none], obj.get("EventItemVideo"))
        video_index = from_union([from_int, from_none], obj.get("EventItemVideoIndex"))
        version = from_union([from_str, from_none], obj.get("EventItemVersion"))
        agenda_note = from_union([from_str, from_none], obj.get("EventItemAgendaNote"))
        minutes_note = from_union(
            [from_str, from_none], obj.get("EventItemMinutesNote")
        )
        action_id = from_union([from_int, from_none], obj.get("EventItemActionId"))
        action_name = from_union([from_str, from_none], obj.get("EventItemActionName"))
        action_text = from_union([from_str, from_none], obj.get("EventItemActionText"))
        passed_flag = from_union([from_int, from_none], obj.get("EventItemPassedFlag"))
        passed_flag_name = from_union(
            [from_str, from_none], obj.get("EventItemPassedFlagName")
        )
        roll_call_flag = from_union(
            [from_int, from_none], obj.get("EventItemRollCallFlag")
        )
        flag_extra = from_union([from_int, from_none], obj.get("EventItemFlagExtra"))
        title = from_union([from_str, from_none], obj.get("EventItemTitle"))
        tally = from_union([from_str, from_none], obj.get("EventItemTally"))
        accela_record_id = from_union(
            [from_str, from_none], obj.get("EventItemAccelaRecordId")
        )
        consent = from_union([from_int, from_none], obj.get("EventItemConsent"))
        mover_id = from_union([from_int, from_none], obj.get("EventItemMoverId"))
        mover = from_union([from_str, from_none], obj.get("EventItemMover"))
        seconder_id = from_union([from_int, from_none], obj.get("EventItemSeconderId"))
        seconder = from_union([from_str, from_none], obj.get("EventItemSeconder"))
        matter_id = from_union([from_int, from_none], obj.get("EventItemMatterId"))
        matter_guid = from_union([from_str, from_none], obj.get("EventItemMatterGuid"))
        matter_file = from_union([from_str, from_none], obj.get("EventItemMatterFile"))
        matter_name = from_union([from_str, from_none], obj.get("EventItemMatterName"))
        matter_type = from_union([from_str, from_none], obj.get("EventItemMatterType"))
        matter_status = from_union(
            [from_str, from_none], obj.get("EventItemMatterStatus")
        )
        matter_attachments = from_union(
            [lambda x: from_list(MatterAttachment.from_dict, x), from_none],
            obj.get("EventItemMatterAttachments"),
        )
        return EventItem(
            id,
            guid,
            last_modified_utc,
            row_version,
            event_id,
            agenda_sequence,
            minutes_sequence,
            agenda_number,
            video,
            video_index,
            version,
            agenda_note,
            minutes_note,
            action_id,
            action_name,
            action_text,
            passed_flag,
            passed_flag_name,
            roll_call_flag,
            flag_extra,
            title,
            tally,
            accela_record_id,
            consent,
            mover_id,
            mover,
            seconder_id,
            seconder,
            matter_id,
            matter_guid,
            matter_file,
            matter_name,
            matter_type,
            matter_status,
            matter_attachments,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["EventItemId"] = from_union([from_int, from_none], self.id)
        result["EventItemGuid"] = from_union([from_str, from_none], self.guid)
        result["EventItemLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["EventItemRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["EventItemEventId"] = from_union([from_int, from_none], self.event_id)
        result["EventItemAgendaSequence"] = from_union(
            [from_int, from_none], self.agenda_sequence
        )
        result["EventItemMinutesSequence"] = from_union(
            [from_int, from_none], self.minutes_sequence
        )
        result["EventItemAgendaNumber"] = from_union(
            [from_str, from_none], self.agenda_number
        )
        result["EventItemVideo"] = from_union([from_int, from_none], self.video)
        result["EventItemVideoIndex"] = from_union(
            [from_int, from_none], self.video_index
        )
        result["EventItemVersion"] = from_union([from_str, from_none], self.version)
        result["EventItemAgendaNote"] = from_union(
            [from_str, from_none], self.agenda_note
        )
        result["EventItemMinutesNote"] = from_union(
            [from_str, from_none], self.minutes_note
        )
        result["EventItemActionId"] = from_union([from_int, from_none], self.action_id)
        result["EventItemActionName"] = from_union(
            [from_str, from_none], self.action_name
        )
        result["EventItemActionText"] = from_union(
            [from_str, from_none], self.action_text
        )
        result["EventItemPassedFlag"] = from_union(
            [from_int, from_none], self.passed_flag
        )
        result["EventItemPassedFlagName"] = from_union(
            [from_str, from_none], self.passed_flag_name
        )
        result["EventItemRollCallFlag"] = from_union(
            [from_int, from_none], self.roll_call_flag
        )
        result["EventItemFlagExtra"] = from_union(
            [from_int, from_none], self.flag_extra
        )
        result["EventItemTitle"] = from_union([from_str, from_none], self.title)
        result["EventItemTally"] = from_union([from_str, from_none], self.tally)
        result["EventItemAccelaRecordId"] = from_union(
            [from_str, from_none], self.accela_record_id
        )
        result["EventItemConsent"] = from_union([from_int, from_none], self.consent)
        result["EventItemMoverId"] = from_union([from_int, from_none], self.mover_id)
        result["EventItemMover"] = from_union([from_str, from_none], self.mover)
        result["EventItemSeconderId"] = from_union(
            [from_int, from_none], self.seconder_id
        )
        result["EventItemSeconder"] = from_union([from_str, from_none], self.seconder)
        result["EventItemMatterId"] = from_union([from_int, from_none], self.matter_id)
        result["EventItemMatterGuid"] = from_union(
            [from_str, from_none], self.matter_guid
        )
        result["EventItemMatterFile"] = from_union(
            [from_str, from_none], self.matter_file
        )
        result["EventItemMatterName"] = from_union(
            [from_str, from_none], self.matter_name
        )
        result["EventItemMatterType"] = from_union(
            [from_str, from_none], self.matter_type
        )
        result["EventItemMatterStatus"] = from_union(
            [from_str, from_none], self.matter_status
        )
        result["EventItemMatterAttachments"] = from_list(
            lambda x: to_class(MatterAttachment, x), self.matter_attachments
        )
        return result


def event_item_from_dict(s: Any) -> EventItem:
    return EventItem.from_dict(s)


def event_item_to_dict(x: EventItem) -> Any:
    return to_class(EventItem, x)


@dataclass
class Event:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    body_id: Optional[int]
    body_name: Optional[str]
    date: Optional[datetime]
    time: Optional[str]
    video_status: Optional[str]
    agenda_status_id: Optional[int]
    agenda_status_name: Optional[str]
    minutes_status_id: Optional[int]
    minutes_status_name: Optional[str]
    location: Optional[str]
    agenda_file: Optional[str]
    minutes_file: Optional[str]
    agenda_last_published_utc: Optional[datetime]
    minutes_last_published_utc: Optional[datetime]
    comment: Optional[str]
    video_path: Optional[str]
    in_site_url: Optional[str]
    items: Optional[List[EventItem]]

    @staticmethod
    def from_dict(obj: Any) -> "Event":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("EventId"))
        guid = from_union([from_str, from_none], obj.get("EventGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("EventLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("EventRowVersion"))
        body_id = from_union([from_int, from_none], obj.get("EventBodyId"))
        body_name = from_union([from_str, from_none], obj.get("EventBodyName"))
        date = from_union([from_datetime, from_none], obj.get("EventDate"))
        time = from_union([from_str, from_none], obj.get("EventTime"))
        video_status = from_union([from_str, from_none], obj.get("EventVideoStatus"))
        agenda_status_id = from_union(
            [from_int, from_none], obj.get("EventAgendaStatusId")
        )
        agenda_status_name = from_union(
            [from_str, from_none], obj.get("EventAgendaStatusName")
        )
        minutes_status_id = from_union(
            [from_int, from_none], obj.get("EventMinutesStatusId")
        )
        minutes_status_name = from_union(
            [from_str, from_none], obj.get("EventMinutesStatusName")
        )
        location = from_union([from_str, from_none], obj.get("EventLocation"))
        agenda_file = from_union([from_str, from_none], obj.get("EventAgendaFile"))
        minutes_file = from_union([from_str, from_none], obj.get("EventMinutesFile"))
        agenda_last_published_utc = from_union(
            [from_datetime, from_none], obj.get("EventAgendaLastPublishedUTC")
        )
        minutes_last_published_utc = from_union(
            [from_datetime, from_none], obj.get("EventMinutesLastPublishedUTC")
        )
        comment = from_union([from_str, from_none], obj.get("EventComment"))
        video_path = from_union([from_str, from_none], obj.get("EventVideoPath"))
        in_site_url = from_union([from_str, from_none], obj.get("EventInSiteURL"))
        items = from_union(
            [lambda x: from_list(EventItem.from_dict, x), from_none],
            obj.get("EventItems"),
        )
        return Event(
            id,
            guid,
            last_modified_utc,
            row_version,
            body_id,
            body_name,
            date,
            time,
            video_status,
            agenda_status_id,
            agenda_status_name,
            minutes_status_id,
            minutes_status_name,
            location,
            agenda_file,
            minutes_file,
            agenda_last_published_utc,
            minutes_last_published_utc,
            comment,
            video_path,
            in_site_url,
            items,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["EventId"] = from_union([from_int, from_none], self.id)
        result["EventGuid"] = from_union([from_str, from_none], self.guid)
        result["EventLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["EventRowVersion"] = from_union([from_str, from_none], self.row_version)
        result["EventBodyId"] = from_union([from_int, from_none], self.body_id)
        result["EventBodyName"] = from_union([from_str, from_none], self.body_name)
        result["EventDate"] = from_union(
            [lambda x: x.isoformat(), from_none], self.date
        )
        result["EventTime"] = from_union([from_str, from_none], self.time)
        result["EventVideoStatus"] = from_union(
            [from_str, from_none], self.video_status
        )
        result["EventAgendaStatusId"] = from_union(
            [from_int, from_none], self.agenda_status_id
        )
        result["EventAgendaStatusName"] = from_union(
            [from_str, from_none], self.agenda_status_name
        )
        result["EventMinutesStatusId"] = from_union(
            [from_int, from_none], self.minutes_status_id
        )
        result["EventMinutesStatusName"] = from_union(
            [from_str, from_none], self.minutes_status_name
        )
        result["EventLocation"] = from_union([from_str, from_none], self.location)
        result["EventAgendaFile"] = from_union([from_str, from_none], self.agenda_file)
        result["EventMinutesFile"] = from_union(
            [from_str, from_none], self.minutes_file
        )
        result["EventAgendaLastPublishedUTC"] = from_union(
            [lambda x: x.isoformat(), from_none], self.agenda_last_published_utc
        )
        result["EventMinutesLastPublishedUTC"] = from_union(
            [lambda x: x.isoformat(), from_none], self.minutes_last_published_utc
        )
        result["EventComment"] = from_union([from_str, from_none], self.comment)
        result["EventVideoPath"] = from_union([from_str, from_none], self.video_path)
        result["EventInSiteURL"] = from_union([from_str, from_none], self.in_site_url)
        result["EventItems"] = from_list(lambda x: to_class(EventItem, x), self.items)
        return result


def event_from_dict(s: Any) -> Event:
    return Event.from_dict(s)


def event_to_dict(x: Event) -> Any:
    return to_class(Event, x)


@dataclass
class Index:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    name: Optional[str]
    active_flag: Optional[int]
    used_flag: Optional[int]
    api_metadata: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "Index":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("IndexId"))
        guid = from_union([from_str, from_none], obj.get("IndexGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("IndexLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("IndexRowVersion"))
        name = from_union([from_str, from_none], obj.get("IndexName"))
        active_flag = from_union([from_int, from_none], obj.get("IndexActiveFlag"))
        used_flag = from_union([from_int, from_none], obj.get("IndexUsedFlag"))
        api_metadata = from_union([from_str, from_none], obj.get("api_metadata"))
        return Index(
            id,
            guid,
            last_modified_utc,
            row_version,
            name,
            active_flag,
            used_flag,
            api_metadata,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["IndexId"] = from_union([from_int, from_none], self.id)
        result["IndexGuid"] = from_union([from_str, from_none], self.guid)
        result["IndexLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["IndexRowVersion"] = from_union([from_str, from_none], self.row_version)
        result["IndexName"] = from_union([from_str, from_none], self.name)
        result["IndexActiveFlag"] = from_union([from_int, from_none], self.active_flag)
        result["IndexUsedFlag"] = from_union([from_int, from_none], self.used_flag)
        result["api_metadata"] = from_union([from_str, from_none], self.api_metadata)
        return result


def index_from_dict(s: Any) -> Index:
    return Index.from_dict(s)


def index_to_dict(x: Index) -> Any:
    return to_class(Index, x)


@dataclass
class MatterCodeSection:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    matter_id: Optional[int]
    code_section_id: Optional[int]
    number: Optional[str]
    name: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "MatterCodeSection":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("MatterCodeSectionId"))
        guid = from_union([from_str, from_none], obj.get("MatterCodeSectionGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("MatterCodeSectionLastModifiedUtc")
        )
        row_version = from_union(
            [from_str, from_none], obj.get("MatterCodeSectionRowVersion")
        )
        matter_id = from_union(
            [from_int, from_none], obj.get("MatterCodeSectionMatterId")
        )
        code_section_id = from_union(
            [from_int, from_none], obj.get("MatterCodeSectionCodeSectionId")
        )
        number = from_union([from_str, from_none], obj.get("MatterCodeSectionNumber"))
        name = from_union([from_str, from_none], obj.get("MatterCodeSectionName"))
        return MatterCodeSection(
            id,
            guid,
            last_modified_utc,
            row_version,
            matter_id,
            code_section_id,
            number,
            name,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatterCodeSectionId"] = from_union([from_int, from_none], self.id)
        result["MatterCodeSectionGuid"] = from_union([from_str, from_none], self.guid)
        result["MatterCodeSectionLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["MatterCodeSectionRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["MatterCodeSectionMatterId"] = from_union(
            [from_int, from_none], self.matter_id
        )
        result["MatterCodeSectionCodeSectionId"] = from_union(
            [from_int, from_none], self.code_section_id
        )
        result["MatterCodeSectionNumber"] = from_union(
            [from_str, from_none], self.number
        )
        result["MatterCodeSectionName"] = from_union([from_str, from_none], self.name)
        return result


def matter_code_section_from_dict(s: Any) -> MatterCodeSection:
    return MatterCodeSection.from_dict(s)


def matter_code_section_to_dict(x: MatterCodeSection) -> Any:
    return to_class(MatterCodeSection, x)


@dataclass
class MatterHistory:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    event_id: Optional[int]
    agenda_sequence: Optional[int]
    minutes_sequence: Optional[int]
    agenda_number: Optional[str]
    video: Optional[int]
    video_index: Optional[int]
    version: Optional[str]
    agenda_note: Optional[str]
    minutes_note: Optional[str]
    action_date: Optional[datetime]
    action_id: Optional[int]
    action_name: Optional[str]
    action_text: Optional[str]
    action_body_id: Optional[int]
    action_body_name: Optional[str]
    passed_flag: Optional[int]
    passed_flag_name: Optional[str]
    roll_call_flag: Optional[int]
    flag_extra: Optional[int]
    tally: Optional[str]
    accela_record_id: Optional[str]
    consent: Optional[int]
    mover_id: Optional[int]
    mover_name: Optional[str]
    seconder_id: Optional[int]
    seconder_name: Optional[str]
    matter_status_id: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> "MatterHistory":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("MatterHistoryId"))
        guid = from_union([from_str, from_none], obj.get("MatterHistoryGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("MatterHistoryLastModifiedUtc")
        )
        row_version = from_union(
            [from_str, from_none], obj.get("MatterHistoryRowVersion")
        )
        event_id = from_union([from_int, from_none], obj.get("MatterHistoryEventId"))
        agenda_sequence = from_union(
            [from_int, from_none], obj.get("MatterHistoryAgendaSequence")
        )
        minutes_sequence = from_union(
            [from_int, from_none], obj.get("MatterHistoryMinutesSequence")
        )
        agenda_number = from_union(
            [from_str, from_none], obj.get("MatterHistoryAgendaNumber")
        )
        video = from_union([from_int, from_none], obj.get("MatterHistoryVideo"))
        video_index = from_union(
            [from_int, from_none], obj.get("MatterHistoryVideoIndex")
        )
        version = from_union([from_str, from_none], obj.get("MatterHistoryVersion"))
        agenda_note = from_union(
            [from_str, from_none], obj.get("MatterHistoryAgendaNote")
        )
        minutes_note = from_union(
            [from_str, from_none], obj.get("MatterHistoryMinutesNote")
        )
        action_date = from_union(
            [from_datetime, from_none], obj.get("MatterHistoryActionDate")
        )
        action_id = from_union([from_int, from_none], obj.get("MatterHistoryActionId"))
        action_name = from_union(
            [from_str, from_none], obj.get("MatterHistoryActionName")
        )
        action_text = from_union(
            [from_str, from_none], obj.get("MatterHistoryActionText")
        )
        action_body_id = from_union(
            [from_int, from_none], obj.get("MatterHistoryActionBodyId")
        )
        action_body_name = from_union(
            [from_str, from_none], obj.get("MatterHistoryActionBodyName")
        )
        passed_flag = from_union(
            [from_int, from_none], obj.get("MatterHistoryPassedFlag")
        )
        passed_flag_name = from_union(
            [from_str, from_none], obj.get("MatterHistoryPassedFlagName")
        )
        roll_call_flag = from_union(
            [from_int, from_none], obj.get("MatterHistoryRollCallFlag")
        )
        flag_extra = from_union(
            [from_int, from_none], obj.get("MatterHistoryFlagExtra")
        )
        tally = from_union([from_str, from_none], obj.get("MatterHistoryTally"))
        accela_record_id = from_union(
            [from_str, from_none], obj.get("MatterHistoryAccelaRecordId")
        )
        consent = from_union([from_int, from_none], obj.get("MatterHistoryConsent"))
        mover_id = from_union([from_int, from_none], obj.get("MatterHistoryMoverId"))
        mover_name = from_union(
            [from_str, from_none], obj.get("MatterHistoryMoverName")
        )
        seconder_id = from_union(
            [from_int, from_none], obj.get("MatterHistorySeconderId")
        )
        seconder_name = from_union(
            [from_str, from_none], obj.get("MatterHistorySeconderName")
        )
        matter_status_id = from_union(
            [from_int, from_none], obj.get("MatterHistoryMatterStatusId")
        )
        return MatterHistory(
            id,
            guid,
            last_modified_utc,
            row_version,
            event_id,
            agenda_sequence,
            minutes_sequence,
            agenda_number,
            video,
            video_index,
            version,
            agenda_note,
            minutes_note,
            action_date,
            action_id,
            action_name,
            action_text,
            action_body_id,
            action_body_name,
            passed_flag,
            passed_flag_name,
            roll_call_flag,
            flag_extra,
            tally,
            accela_record_id,
            consent,
            mover_id,
            mover_name,
            seconder_id,
            seconder_name,
            matter_status_id,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatterHistoryId"] = from_union([from_int, from_none], self.id)
        result["MatterHistoryGuid"] = from_union([from_str, from_none], self.guid)
        result["MatterHistoryLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["MatterHistoryRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["MatterHistoryEventId"] = from_union(
            [from_int, from_none], self.event_id
        )
        result["MatterHistoryAgendaSequence"] = from_union(
            [from_int, from_none], self.agenda_sequence
        )
        result["MatterHistoryMinutesSequence"] = from_union(
            [from_int, from_none], self.minutes_sequence
        )
        result["MatterHistoryAgendaNumber"] = from_union(
            [from_str, from_none], self.agenda_number
        )
        result["MatterHistoryVideo"] = from_union([from_int, from_none], self.video)
        result["MatterHistoryVideoIndex"] = from_union(
            [from_int, from_none], self.video_index
        )
        result["MatterHistoryVersion"] = from_union([from_str, from_none], self.version)
        result["MatterHistoryAgendaNote"] = from_union(
            [from_str, from_none], self.agenda_note
        )
        result["MatterHistoryMinutesNote"] = from_union(
            [from_str, from_none], self.minutes_note
        )
        result["MatterHistoryActionDate"] = from_union(
            [lambda x: x.isoformat(), from_none], self.action_date
        )
        result["MatterHistoryActionId"] = from_union(
            [from_int, from_none], self.action_id
        )
        result["MatterHistoryActionName"] = from_union(
            [from_str, from_none], self.action_name
        )
        result["MatterHistoryActionText"] = from_union(
            [from_str, from_none], self.action_text
        )
        result["MatterHistoryActionBodyId"] = from_union(
            [from_int, from_none], self.action_body_id
        )
        result["MatterHistoryActionBodyName"] = from_union(
            [from_str, from_none], self.action_body_name
        )
        result["MatterHistoryPassedFlag"] = from_union(
            [from_int, from_none], self.passed_flag
        )
        result["MatterHistoryPassedFlagName"] = from_union(
            [from_str, from_none], self.passed_flag_name
        )
        result["MatterHistoryRollCallFlag"] = from_union(
            [from_int, from_none], self.roll_call_flag
        )
        result["MatterHistoryFlagExtra"] = from_union(
            [from_int, from_none], self.flag_extra
        )
        result["MatterHistoryTally"] = from_union([from_str, from_none], self.tally)
        result["MatterHistoryAccelaRecordId"] = from_union(
            [from_str, from_none], self.accela_record_id
        )
        result["MatterHistoryConsent"] = from_union([from_int, from_none], self.consent)
        result["MatterHistoryMoverId"] = from_union(
            [from_int, from_none], self.mover_id
        )
        result["MatterHistoryMoverName"] = from_union(
            [from_str, from_none], self.mover_name
        )
        result["MatterHistorySeconderId"] = from_union(
            [from_int, from_none], self.seconder_id
        )
        result["MatterHistorySeconderName"] = from_union(
            [from_str, from_none], self.seconder_name
        )
        result["MatterHistoryMatterStatusId"] = from_union(
            [from_int, from_none], self.matter_status_id
        )
        return result


def matter_history_from_dict(s: Any) -> MatterHistory:
    return MatterHistory.from_dict(s)


def matter_history_to_dict(x: MatterHistory) -> Any:
    return to_class(MatterHistory, x)


@dataclass
class MatterIndex:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    matter_id: Optional[int]
    index_id: Optional[int]
    name: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "MatterIndex":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("MatterIndexId"))
        guid = from_union([from_str, from_none], obj.get("MatterIndexGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("MatterIndexLastModifiedUtc")
        )
        row_version = from_union(
            [from_str, from_none], obj.get("MatterIndexRowVersion")
        )
        matter_id = from_union([from_int, from_none], obj.get("MatterIndexMatterId"))
        index_id = from_union([from_int, from_none], obj.get("MatterIndexIndexId"))
        name = from_union([from_str, from_none], obj.get("MatterIndexName"))
        return MatterIndex(
            id, guid, last_modified_utc, row_version, matter_id, index_id, name
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatterIndexId"] = from_union([from_int, from_none], self.id)
        result["MatterIndexGuid"] = from_union([from_str, from_none], self.guid)
        result["MatterIndexLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["MatterIndexRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["MatterIndexMatterId"] = from_union(
            [from_int, from_none], self.matter_id
        )
        result["MatterIndexIndexId"] = from_union([from_int, from_none], self.index_id)
        result["MatterIndexName"] = from_union([from_str, from_none], self.name)
        return result


def matter_index_from_dict(s: Any) -> MatterIndex:
    return MatterIndex.from_dict(s)


def matter_index_to_dict(x: MatterIndex) -> Any:
    return to_class(MatterIndex, x)


@dataclass
class MatterRelation:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    matter_id: Optional[int]
    flag: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> "MatterRelation":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("MatterRelationId"))
        guid = from_union([from_str, from_none], obj.get("MatterRelationGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("MatterRelationLastModifiedUtc")
        )
        row_version = from_union(
            [from_str, from_none], obj.get("MatterRelationRowVersion")
        )
        matter_id = from_union([from_int, from_none], obj.get("MatterRelationMatterId"))
        flag = from_union([from_int, from_none], obj.get("MatterRelationFlag"))
        return MatterRelation(id, guid, last_modified_utc, row_version, matter_id, flag)

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatterRelationId"] = from_union([from_int, from_none], self.id)
        result["MatterRelationGuid"] = from_union([from_str, from_none], self.guid)
        result["MatterRelationLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["MatterRelationRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["MatterRelationMatterId"] = from_union(
            [from_int, from_none], self.matter_id
        )
        result["MatterRelationFlag"] = from_union([from_int, from_none], self.flag)
        return result


def matter_relation_from_dict(s: Any) -> MatterRelation:
    return MatterRelation.from_dict(s)


def matter_relation_to_dict(x: MatterRelation) -> Any:
    return to_class(MatterRelation, x)


@dataclass
class MatterTextVersion:
    key: str
    value: str

    @staticmethod
    def from_dict(obj: Any) -> "MatterTextVersion":
        assert isinstance(obj, dict)
        key = from_str(obj.get("Key"))
        value = from_str(obj.get("Value"))
        return MatterTextVersion(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Key"] = from_str(self.key)
        result["Value"] = from_str(self.value)
        return result


def matter_text_version_from_dict(s: Any) -> MatterTextVersion:
    return MatterTextVersion.from_dict(s)


def matter_text_version_to_dict(x: MatterTextVersion) -> Any:
    return to_class(MatterTextVersion, x)


@dataclass
class MatterRequester:
    name: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "MatterRequester":
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("MatterRequesterName"))
        return MatterRequester(name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatterRequesterName"] = from_union([from_str, from_none], self.name)
        return result


def matter_requester_from_dict(s: Any) -> MatterRequester:
    return MatterRequester.from_dict(s)


def matter_requester_to_dict(x: MatterRequester) -> Any:
    return to_class(MatterRequester, x)


@dataclass
class Report:
    name: Optional[str]
    url: Optional[str]
    type: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "Report":
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("ReportName"))
        url = from_union([from_str, from_none], obj.get("ReportURL"))
        type = from_union([from_str, from_none], obj.get("ReportType"))
        return Report(name, url, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ReportName"] = from_union([from_str, from_none], self.name)
        result["ReportURL"] = from_union([from_str, from_none], self.url)
        result["ReportType"] = from_union([from_str, from_none], self.type)
        return result


def report_from_dict(s: Any) -> Report:
    return Report.from_dict(s)


def report_to_dict(x: Report) -> Any:
    return to_class(Report, x)


@dataclass
class Matter:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    file: Optional[str]
    name: Optional[str]
    title: Optional[str]
    type_id: Optional[int]
    type_name: Optional[str]
    status_id: Optional[int]
    status_name: Optional[str]
    body_id: Optional[int]
    body_name: Optional[str]
    intro_date: Optional[datetime]
    agenda_date: Optional[datetime]
    passed_date: Optional[datetime]
    enactment_date: Optional[datetime]
    enactment_number: Optional[str]
    requester: Optional[str]
    notes: Optional[str]
    version: Optional[str]
    text1: Optional[str]
    text2: Optional[str]
    text3: Optional[str]
    text4: Optional[str]
    text5: Optional[str]
    date1: Optional[datetime]
    date2: Optional[datetime]
    ex_text1: Optional[str]
    ex_text2: Optional[str]
    ex_text3: Optional[str]
    ex_text4: Optional[str]
    ex_text5: Optional[str]
    ex_text6: Optional[str]
    ex_text7: Optional[str]
    ex_text8: Optional[str]
    ex_text9: Optional[str]
    ex_text10: Optional[str]
    ex_text11: Optional[str]
    ex_date1: Optional[datetime]
    ex_date2: Optional[datetime]
    ex_date3: Optional[datetime]
    ex_date4: Optional[datetime]
    ex_date5: Optional[datetime]
    ex_date6: Optional[datetime]
    ex_date7: Optional[datetime]
    ex_date8: Optional[datetime]
    ex_date9: Optional[datetime]
    ex_date10: Optional[datetime]
    agiloft_id: Optional[int]
    reference: Optional[str]
    restrict_view_via_web: Optional[bool]
    reports: List[Report]

    @staticmethod
    def from_dict(obj: Any) -> "Matter":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("MatterId"))
        guid = from_union([from_str, from_none], obj.get("MatterGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("MatterLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("MatterRowVersion"))
        file = from_union([from_str, from_none], obj.get("MatterFile"))
        name = from_union([from_str, from_none], obj.get("MatterName"))
        title = from_union([from_str, from_none], obj.get("MatterTitle"))
        type_id = from_union([from_int, from_none], obj.get("MatterTypeId"))
        type_name = from_union([from_str, from_none], obj.get("MatterTypeName"))
        status_id = from_union([from_int, from_none], obj.get("MatterStatusId"))
        status_name = from_union([from_str, from_none], obj.get("MatterStatusName"))
        body_id = from_union([from_int, from_none], obj.get("MatterBodyId"))
        body_name = from_union([from_str, from_none], obj.get("MatterBodyName"))
        intro_date = from_union([from_datetime, from_none], obj.get("MatterIntroDate"))
        agenda_date = from_union(
            [from_datetime, from_none], obj.get("MatterAgendaDate")
        )
        passed_date = from_union(
            [from_datetime, from_none], obj.get("MatterPassedDate")
        )
        enactment_date = from_union(
            [from_datetime, from_none], obj.get("MatterEnactmentDate")
        )
        enactment_number = from_union(
            [from_str, from_none], obj.get("MatterEnactmentNumber")
        )
        requester = from_union([from_str, from_none], obj.get("MatterRequester"))
        notes = from_union([from_str, from_none], obj.get("MatterNotes"))
        version = from_union([from_str, from_none], obj.get("MatterVersion"))
        text1 = from_union([from_str, from_none], obj.get("MatterText1"))
        text2 = from_union([from_str, from_none], obj.get("MatterText2"))
        text3 = from_union([from_str, from_none], obj.get("MatterText3"))
        text4 = from_union([from_str, from_none], obj.get("MatterText4"))
        text5 = from_union([from_str, from_none], obj.get("MatterText5"))
        date1 = from_union([from_datetime, from_none], obj.get("MatterDate1"))
        date2 = from_union([from_datetime, from_none], obj.get("MatterDate2"))
        ex_text1 = from_union([from_str, from_none], obj.get("MatterEXText1"))
        ex_text2 = from_union([from_str, from_none], obj.get("MatterEXText2"))
        ex_text3 = from_union([from_str, from_none], obj.get("MatterEXText3"))
        ex_text4 = from_union([from_str, from_none], obj.get("MatterEXText4"))
        ex_text5 = from_union([from_str, from_none], obj.get("MatterEXText5"))
        ex_text6 = from_union([from_str, from_none], obj.get("MatterEXText6"))
        ex_text7 = from_union([from_str, from_none], obj.get("MatterEXText7"))
        ex_text8 = from_union([from_str, from_none], obj.get("MatterEXText8"))
        ex_text9 = from_union([from_str, from_none], obj.get("MatterEXText9"))
        ex_text10 = from_union([from_str, from_none], obj.get("MatterEXText10"))
        ex_text11 = from_union([from_str, from_none], obj.get("MatterEXText11"))
        ex_date1 = from_union([from_datetime, from_none], obj.get("MatterEXDate1"))
        ex_date2 = from_union([from_datetime, from_none], obj.get("MatterEXDate2"))
        ex_date3 = from_union([from_datetime, from_none], obj.get("MatterEXDate3"))
        ex_date4 = from_union([from_datetime, from_none], obj.get("MatterEXDate4"))
        ex_date5 = from_union([from_datetime, from_none], obj.get("MatterEXDate5"))
        ex_date6 = from_union([from_datetime, from_none], obj.get("MatterEXDate6"))
        ex_date7 = from_union([from_datetime, from_none], obj.get("MatterEXDate7"))
        ex_date8 = from_union([from_datetime, from_none], obj.get("MatterEXDate8"))
        ex_date9 = from_union([from_datetime, from_none], obj.get("MatterEXDate9"))
        ex_date10 = from_union([from_datetime, from_none], obj.get("MatterEXDate10"))
        agiloft_id = from_union([from_int, from_none], obj.get("MatterAgiloftId"))
        reference = from_union([from_str, from_none], obj.get("MatterReference"))
        restrict_view_via_web = from_union(
            [from_bool, from_none], obj.get("MatterRestrictViewViaWeb")
        )
        reports = from_list(Report.from_dict, obj.get("MatterReports"))
        return Matter(
            id,
            guid,
            last_modified_utc,
            row_version,
            file,
            name,
            title,
            type_id,
            type_name,
            status_id,
            status_name,
            body_id,
            body_name,
            intro_date,
            agenda_date,
            passed_date,
            enactment_date,
            enactment_number,
            requester,
            notes,
            version,
            text1,
            text2,
            text3,
            text4,
            text5,
            date1,
            date2,
            ex_text1,
            ex_text2,
            ex_text3,
            ex_text4,
            ex_text5,
            ex_text6,
            ex_text7,
            ex_text8,
            ex_text9,
            ex_text10,
            ex_text11,
            ex_date1,
            ex_date2,
            ex_date3,
            ex_date4,
            ex_date5,
            ex_date6,
            ex_date7,
            ex_date8,
            ex_date9,
            ex_date10,
            agiloft_id,
            reference,
            restrict_view_via_web,
            reports,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatterId"] = from_union([from_int, from_none], self.id)
        result["MatterGuid"] = from_union([from_str, from_none], self.guid)
        result["MatterLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["MatterRowVersion"] = from_union([from_str, from_none], self.row_version)
        result["MatterFile"] = from_union([from_str, from_none], self.file)
        result["MatterName"] = from_union([from_str, from_none], self.name)
        result["MatterTitle"] = from_union([from_str, from_none], self.title)
        result["MatterTypeId"] = from_union([from_int, from_none], self.type_id)
        result["MatterTypeName"] = from_union([from_str, from_none], self.type_name)
        result["MatterStatusId"] = from_union([from_int, from_none], self.status_id)
        result["MatterStatusName"] = from_union([from_str, from_none], self.status_name)
        result["MatterBodyId"] = from_union([from_int, from_none], self.body_id)
        result["MatterBodyName"] = from_union([from_str, from_none], self.body_name)
        result["MatterIntroDate"] = from_union(
            [lambda x: x.isoformat(), from_none], self.intro_date
        )
        result["MatterAgendaDate"] = from_union(
            [lambda x: x.isoformat(), from_none], self.agenda_date
        )
        result["MatterPassedDate"] = from_union(
            [lambda x: x.isoformat(), from_none], self.passed_date
        )
        result["MatterEnactmentDate"] = from_union(
            [lambda x: x.isoformat(), from_none], self.enactment_date
        )
        result["MatterEnactmentNumber"] = from_union(
            [from_str, from_none], self.enactment_number
        )
        result["MatterRequester"] = from_union([from_str, from_none], self.requester)
        result["MatterNotes"] = from_union([from_str, from_none], self.notes)
        result["MatterVersion"] = from_union([from_str, from_none], self.version)
        result["MatterText1"] = from_union([from_str, from_none], self.text1)
        result["MatterText2"] = from_union([from_str, from_none], self.text2)
        result["MatterText3"] = from_union([from_str, from_none], self.text3)
        result["MatterText4"] = from_union([from_str, from_none], self.text4)
        result["MatterText5"] = from_union([from_str, from_none], self.text5)
        result["MatterDate1"] = from_union(
            [lambda x: x.isoformat(), from_none], self.date1
        )
        result["MatterDate2"] = from_union(
            [lambda x: x.isoformat(), from_none], self.date2
        )
        result["MatterEXText1"] = from_union([from_str, from_none], self.ex_text1)
        result["MatterEXText2"] = from_union([from_str, from_none], self.ex_text2)
        result["MatterEXText3"] = from_union([from_str, from_none], self.ex_text3)
        result["MatterEXText4"] = from_union([from_str, from_none], self.ex_text4)
        result["MatterEXText5"] = from_union([from_str, from_none], self.ex_text5)
        result["MatterEXText6"] = from_union([from_str, from_none], self.ex_text6)
        result["MatterEXText7"] = from_union([from_str, from_none], self.ex_text7)
        result["MatterEXText8"] = from_union([from_str, from_none], self.ex_text8)
        result["MatterEXText9"] = from_union([from_str, from_none], self.ex_text9)
        result["MatterEXText10"] = from_union([from_str, from_none], self.ex_text10)
        result["MatterEXText11"] = from_union([from_str, from_none], self.ex_text11)
        result["MatterEXDate1"] = from_union(
            [lambda x: x.isoformat(), from_none], self.ex_date1
        )
        result["MatterEXDate2"] = from_union(
            [lambda x: x.isoformat(), from_none], self.ex_date2
        )
        result["MatterEXDate3"] = from_union(
            [lambda x: x.isoformat(), from_none], self.ex_date3
        )
        result["MatterEXDate4"] = from_union(
            [lambda x: x.isoformat(), from_none], self.ex_date4
        )
        result["MatterEXDate5"] = from_union(
            [lambda x: x.isoformat(), from_none], self.ex_date5
        )
        result["MatterEXDate6"] = from_union(
            [lambda x: x.isoformat(), from_none], self.ex_date6
        )
        result["MatterEXDate7"] = from_union(
            [lambda x: x.isoformat(), from_none], self.ex_date7
        )
        result["MatterEXDate8"] = from_union(
            [lambda x: x.isoformat(), from_none], self.ex_date8
        )
        result["MatterEXDate9"] = from_union(
            [lambda x: x.isoformat(), from_none], self.ex_date9
        )
        result["MatterEXDate10"] = from_union(
            [lambda x: x.isoformat(), from_none], self.ex_date10
        )
        result["MatterAgiloftId"] = from_union([from_int, from_none], self.agiloft_id)
        result["MatterReference"] = from_union([from_str, from_none], self.reference)
        result["MatterRestrictViewViaWeb"] = from_union(
            [from_bool, from_none], self.restrict_view_via_web
        )
        result["MatterReports"] = from_list(lambda x: to_class(Report, x), self.reports)
        return result


def matter_from_dict(s: Any) -> Matter:
    return Matter.from_dict(s)


def matter_to_dict(x: Matter) -> Any:
    return to_class(Matter, x)


@dataclass
class MatterSponsor:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    matter_id: Optional[int]
    matter_version: Optional[str]
    name_id: Optional[int]
    body_id: Optional[int]
    name: Optional[str]
    sequence: Optional[int]
    link_flag: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> "MatterSponsor":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("MatterSponsorId"))
        guid = from_union([from_str, from_none], obj.get("MatterSponsorGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("MatterSponsorLastModifiedUtc")
        )
        row_version = from_union(
            [from_str, from_none], obj.get("MatterSponsorRowVersion")
        )
        matter_id = from_union([from_int, from_none], obj.get("MatterSponsorMatterId"))
        matter_version = from_union(
            [from_str, from_none], obj.get("MatterSponsorMatterVersion")
        )
        name_id = from_union([from_int, from_none], obj.get("MatterSponsorNameId"))
        body_id = from_union([from_int, from_none], obj.get("MatterSponsorBodyId"))
        name = from_union([from_str, from_none], obj.get("MatterSponsorName"))
        sequence = from_union([from_int, from_none], obj.get("MatterSponsorSequence"))
        link_flag = from_union([from_int, from_none], obj.get("MatterSponsorLinkFlag"))
        return MatterSponsor(
            id,
            guid,
            last_modified_utc,
            row_version,
            matter_id,
            matter_version,
            name_id,
            body_id,
            name,
            sequence,
            link_flag,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatterSponsorId"] = from_union([from_int, from_none], self.id)
        result["MatterSponsorGuid"] = from_union([from_str, from_none], self.guid)
        result["MatterSponsorLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["MatterSponsorRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["MatterSponsorMatterId"] = from_union(
            [from_int, from_none], self.matter_id
        )
        result["MatterSponsorMatterVersion"] = from_union(
            [from_str, from_none], self.matter_version
        )
        result["MatterSponsorNameId"] = from_union([from_int, from_none], self.name_id)
        result["MatterSponsorBodyId"] = from_union([from_int, from_none], self.body_id)
        result["MatterSponsorName"] = from_union([from_str, from_none], self.name)
        result["MatterSponsorSequence"] = from_union(
            [from_int, from_none], self.sequence
        )
        result["MatterSponsorLinkFlag"] = from_union(
            [from_int, from_none], self.link_flag
        )
        return result


def matter_sponsor_from_dict(s: Any) -> MatterSponsor:
    return MatterSponsor.from_dict(s)


def matter_sponsor_to_dict(x: MatterSponsor) -> Any:
    return to_class(MatterSponsor, x)


@dataclass
class MatterStatus:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    name: Optional[str]
    sort: Optional[int]
    active_flag: Optional[int]
    description: Optional[str]
    used_flag: Optional[int]
    public_flag: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> "MatterStatus":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("MatterStatusId"))
        guid = from_union([from_str, from_none], obj.get("MatterStatusGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("MatterStatusLastModifiedUtc")
        )
        row_version = from_union(
            [from_str, from_none], obj.get("MatterStatusRowVersion")
        )
        name = from_union([from_str, from_none], obj.get("MatterStatusName"))
        sort = from_union([from_int, from_none], obj.get("MatterStatusSort"))
        active_flag = from_union(
            [from_int, from_none], obj.get("MatterStatusActiveFlag")
        )
        description = from_union(
            [from_str, from_none], obj.get("MatterStatusDescription")
        )
        used_flag = from_union([from_int, from_none], obj.get("MatterStatusUsedFlag"))
        public_flag = from_union(
            [from_int, from_none], obj.get("MatterStatusPublicFlag")
        )
        return MatterStatus(
            id,
            guid,
            last_modified_utc,
            row_version,
            name,
            sort,
            active_flag,
            description,
            used_flag,
            public_flag,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatterStatusId"] = from_union([from_int, from_none], self.id)
        result["MatterStatusGuid"] = from_union([from_str, from_none], self.guid)
        result["MatterStatusLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["MatterStatusRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["MatterStatusName"] = from_union([from_str, from_none], self.name)
        result["MatterStatusSort"] = from_union([from_int, from_none], self.sort)
        result["MatterStatusActiveFlag"] = from_union(
            [from_int, from_none], self.active_flag
        )
        result["MatterStatusDescription"] = from_union(
            [from_str, from_none], self.description
        )
        result["MatterStatusUsedFlag"] = from_union(
            [from_int, from_none], self.used_flag
        )
        result["MatterStatusPublicFlag"] = from_union(
            [from_int, from_none], self.public_flag
        )
        return result


def matter_status_from_dict(s: Any) -> MatterStatus:
    return MatterStatus.from_dict(s)


def matter_status_to_dict(x: MatterStatus) -> Any:
    return to_class(MatterStatus, x)


@dataclass
class MatterText:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    matter_id: Optional[int]
    version: Optional[str]
    plain: Optional[str]
    rtf: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "MatterText":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("MatterTextId"))
        guid = from_union([from_str, from_none], obj.get("MatterTextGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("MatterTextLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("MatterTextRowVersion"))
        matter_id = from_union([from_int, from_none], obj.get("MatterTextMatterId"))
        version = from_union([from_str, from_none], obj.get("MatterTextVersion"))
        plain = from_union([from_str, from_none], obj.get("MatterTextPlain"))
        rtf = from_union([from_str, from_none], obj.get("MatterTextRtf"))
        return MatterText(
            id, guid, last_modified_utc, row_version, matter_id, version, plain, rtf
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatterTextId"] = from_union([from_int, from_none], self.id)
        result["MatterTextGuid"] = from_union([from_str, from_none], self.guid)
        result["MatterTextLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["MatterTextRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["MatterTextMatterId"] = from_union([from_int, from_none], self.matter_id)
        result["MatterTextVersion"] = from_union([from_str, from_none], self.version)
        result["MatterTextPlain"] = from_union([from_str, from_none], self.plain)
        result["MatterTextRtf"] = from_union([from_str, from_none], self.rtf)
        return result


def matter_text_from_dict(s: Any) -> MatterText:
    return MatterText.from_dict(s)


def matter_text_to_dict(x: MatterText) -> Any:
    return to_class(MatterText, x)


@dataclass
class MatterType:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    name: Optional[str]
    sort: Optional[int]
    active_flag: Optional[int]
    description: Optional[str]
    used_flag: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> "MatterType":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("MatterTypeId"))
        guid = from_union([from_str, from_none], obj.get("MatterTypeGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("MatterTypeLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("MatterTypeRowVersion"))
        name = from_union([from_str, from_none], obj.get("MatterTypeName"))
        sort = from_union([from_int, from_none], obj.get("MatterTypeSort"))
        active_flag = from_union([from_int, from_none], obj.get("MatterTypeActiveFlag"))
        description = from_union(
            [from_str, from_none], obj.get("MatterTypeDescription")
        )
        used_flag = from_union([from_int, from_none], obj.get("MatterTypeUsedFlag"))
        return MatterType(
            id,
            guid,
            last_modified_utc,
            row_version,
            name,
            sort,
            active_flag,
            description,
            used_flag,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatterTypeId"] = from_union([from_int, from_none], self.id)
        result["MatterTypeGuid"] = from_union([from_str, from_none], self.guid)
        result["MatterTypeLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["MatterTypeRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["MatterTypeName"] = from_union([from_str, from_none], self.name)
        result["MatterTypeSort"] = from_union([from_int, from_none], self.sort)
        result["MatterTypeActiveFlag"] = from_union(
            [from_int, from_none], self.active_flag
        )
        result["MatterTypeDescription"] = from_union(
            [from_str, from_none], self.description
        )
        result["MatterTypeUsedFlag"] = from_union([from_int, from_none], self.used_flag)
        return result


def matter_type_from_dict(s: Any) -> MatterType:
    return MatterType.from_dict(s)


def matter_type_to_dict(x: MatterType) -> Any:
    return to_class(MatterType, x)


@dataclass
class OfficeRecord:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    full_name: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    sort: Optional[int]
    person_id: Optional[int]
    body_id: Optional[int]
    body_name: Optional[str]
    title: Optional[str]
    vote_divider: Optional[float]
    extend_flag: Optional[int]
    member_type_id: Optional[int]
    member_type: Optional[str]
    support_name_id: Optional[int]
    support_full_name: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "OfficeRecord":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("OfficeRecordId"))
        guid = from_union([from_str, from_none], obj.get("OfficeRecordGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("OfficeRecordLastModifiedUtc")
        )
        row_version = from_union(
            [from_str, from_none], obj.get("OfficeRecordRowVersion")
        )
        first_name = from_union([from_str, from_none], obj.get("OfficeRecordFirstName"))
        last_name = from_union([from_str, from_none], obj.get("OfficeRecordLastName"))
        email = from_union([from_str, from_none], obj.get("OfficeRecordEmail"))
        full_name = from_union([from_str, from_none], obj.get("OfficeRecordFullName"))
        start_date = from_union(
            [from_datetime, from_none], obj.get("OfficeRecordStartDate")
        )
        end_date = from_union(
            [from_datetime, from_none], obj.get("OfficeRecordEndDate")
        )
        sort = from_union([from_int, from_none], obj.get("OfficeRecordSort"))
        person_id = from_union([from_int, from_none], obj.get("OfficeRecordPersonId"))
        body_id = from_union([from_int, from_none], obj.get("OfficeRecordBodyId"))
        body_name = from_union([from_str, from_none], obj.get("OfficeRecordBodyName"))
        title = from_union([from_str, from_none], obj.get("OfficeRecordTitle"))
        vote_divider = from_union(
            [from_float, from_none], obj.get("OfficeRecordVoteDivider")
        )
        extend_flag = from_union(
            [from_int, from_none], obj.get("OfficeRecordExtendFlag")
        )
        member_type_id = from_union(
            [from_int, from_none], obj.get("OfficeRecordMemberTypeId")
        )
        member_type = from_union(
            [from_str, from_none], obj.get("OfficeRecordMemberType")
        )
        support_name_id = from_union(
            [from_int, from_none], obj.get("OfficeRecordSupportNameId")
        )
        support_full_name = from_union(
            [from_str, from_none], obj.get("OfficeRecordSupportFullName")
        )
        return OfficeRecord(
            id,
            guid,
            last_modified_utc,
            row_version,
            first_name,
            last_name,
            email,
            full_name,
            start_date,
            end_date,
            sort,
            person_id,
            body_id,
            body_name,
            title,
            vote_divider,
            extend_flag,
            member_type_id,
            member_type,
            support_name_id,
            support_full_name,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["OfficeRecordId"] = from_union([from_int, from_none], self.id)
        result["OfficeRecordGuid"] = from_union([from_str, from_none], self.guid)
        result["OfficeRecordLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["OfficeRecordRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["OfficeRecordFirstName"] = from_union(
            [from_str, from_none], self.first_name
        )
        result["OfficeRecordLastName"] = from_union(
            [from_str, from_none], self.last_name
        )
        result["OfficeRecordEmail"] = from_union([from_str, from_none], self.email)
        result["OfficeRecordFullName"] = from_union(
            [from_str, from_none], self.full_name
        )
        result["OfficeRecordStartDate"] = from_union(
            [lambda x: x.isoformat(), from_none], self.start_date
        )
        result["OfficeRecordEndDate"] = from_union(
            [lambda x: x.isoformat(), from_none], self.end_date
        )
        result["OfficeRecordSort"] = from_union([from_int, from_none], self.sort)
        result["OfficeRecordPersonId"] = from_union(
            [from_int, from_none], self.person_id
        )
        result["OfficeRecordBodyId"] = from_union([from_int, from_none], self.body_id)
        result["OfficeRecordBodyName"] = from_union(
            [from_str, from_none], self.body_name
        )
        result["OfficeRecordTitle"] = from_union([from_str, from_none], self.title)
        result["OfficeRecordVoteDivider"] = to_float(self.vote_divider)
        result["OfficeRecordExtendFlag"] = from_union(
            [from_int, from_none], self.extend_flag
        )
        result["OfficeRecordMemberTypeId"] = from_union(
            [from_int, from_none], self.member_type_id
        )
        result["OfficeRecordMemberType"] = from_union(
            [from_str, from_none], self.member_type
        )
        result["OfficeRecordSupportNameId"] = from_union(
            [from_int, from_none], self.support_name_id
        )
        result["OfficeRecordSupportFullName"] = from_union(
            [from_str, from_none], self.support_full_name
        )
        return result


def office_record_from_dict(s: Any) -> OfficeRecord:
    return OfficeRecord.from_dict(s)


def office_record_to_dict(x: OfficeRecord) -> Any:
    return to_class(OfficeRecord, x)


@dataclass
class Person:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    full_name: Optional[str]
    active_flag: Optional[int]
    used_sponsor_flag: Optional[int]
    address1: Optional[str]
    city1: Optional[str]
    state1: Optional[str]
    zip1: Optional[str]
    phone: Optional[str]
    fax: Optional[str]
    email: Optional[str]
    www: Optional[str]
    address2: Optional[str]
    city2: Optional[str]
    state2: Optional[str]
    zip2: Optional[str]
    phone2: Optional[str]
    fax2: Optional[str]
    email2: Optional[str]
    www2: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "Person":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("PersonId"))
        guid = from_union([from_str, from_none], obj.get("PersonGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("PersonLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("PersonRowVersion"))
        first_name = from_union([from_str, from_none], obj.get("PersonFirstName"))
        last_name = from_union([from_str, from_none], obj.get("PersonLastName"))
        full_name = from_union([from_str, from_none], obj.get("PersonFullName"))
        active_flag = from_union([from_int, from_none], obj.get("PersonActiveFlag"))
        used_sponsor_flag = from_union(
            [from_int, from_none], obj.get("PersonUsedSponsorFlag")
        )
        address1 = from_union([from_str, from_none], obj.get("PersonAddress1"))
        city1 = from_union([from_str, from_none], obj.get("PersonCity1"))
        state1 = from_union([from_str, from_none], obj.get("PersonState1"))
        zip1 = from_union([from_str, from_none], obj.get("PersonZip1"))
        phone = from_union([from_str, from_none], obj.get("PersonPhone"))
        fax = from_union([from_str, from_none], obj.get("PersonFax"))
        email = from_union([from_str, from_none], obj.get("PersonEmail"))
        www = from_union([from_str, from_none], obj.get("PersonWWW"))
        address2 = from_union([from_str, from_none], obj.get("PersonAddress2"))
        city2 = from_union([from_str, from_none], obj.get("PersonCity2"))
        state2 = from_union([from_str, from_none], obj.get("PersonState2"))
        zip2 = from_union([from_str, from_none], obj.get("PersonZip2"))
        phone2 = from_union([from_str, from_none], obj.get("PersonPhone2"))
        fax2 = from_union([from_str, from_none], obj.get("PersonFax2"))
        email2 = from_union([from_str, from_none], obj.get("PersonEmail2"))
        www2 = from_union([from_str, from_none], obj.get("PersonWWW2"))
        return Person(
            id,
            guid,
            last_modified_utc,
            row_version,
            first_name,
            last_name,
            full_name,
            active_flag,
            used_sponsor_flag,
            address1,
            city1,
            state1,
            zip1,
            phone,
            fax,
            email,
            www,
            address2,
            city2,
            state2,
            zip2,
            phone2,
            fax2,
            email2,
            www2,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["PersonId"] = from_union([from_int, from_none], self.id)
        result["PersonGuid"] = from_union([from_str, from_none], self.guid)
        result["PersonLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["PersonRowVersion"] = from_union([from_str, from_none], self.row_version)
        result["PersonFirstName"] = from_union([from_str, from_none], self.first_name)
        result["PersonLastName"] = from_union([from_str, from_none], self.last_name)
        result["PersonFullName"] = from_union([from_str, from_none], self.full_name)
        result["PersonActiveFlag"] = from_union([from_int, from_none], self.active_flag)
        result["PersonUsedSponsorFlag"] = from_union(
            [from_int, from_none], self.used_sponsor_flag
        )
        result["PersonAddress1"] = from_union([from_str, from_none], self.address1)
        result["PersonCity1"] = from_union([from_str, from_none], self.city1)
        result["PersonState1"] = from_union([from_str, from_none], self.state1)
        result["PersonZip1"] = from_union([from_str, from_none], self.zip1)
        result["PersonPhone"] = from_union([from_str, from_none], self.phone)
        result["PersonFax"] = from_union([from_str, from_none], self.fax)
        result["PersonEmail"] = from_union([from_str, from_none], self.email)
        result["PersonWWW"] = from_union([from_str, from_none], self.www)
        result["PersonAddress2"] = from_union([from_str, from_none], self.address2)
        result["PersonCity2"] = from_union([from_str, from_none], self.city2)
        result["PersonState2"] = from_union([from_str, from_none], self.state2)
        result["PersonZip2"] = from_union([from_str, from_none], self.zip2)
        result["PersonPhone2"] = from_union([from_str, from_none], self.phone2)
        result["PersonFax2"] = from_union([from_str, from_none], self.fax2)
        result["PersonEmail2"] = from_union([from_str, from_none], self.email2)
        result["PersonWWW2"] = from_union([from_str, from_none], self.www2)
        return result


def person_from_dict(s: Any) -> Person:
    return Person.from_dict(s)


def person_to_dict(x: Person) -> Any:
    return to_class(Person, x)


@dataclass
class RollCall:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    person_id: Optional[int]
    person_name: Optional[str]
    value_id: Optional[int]
    value_name: Optional[str]
    sort: Optional[int]
    result: Optional[int]
    event_item_id: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> "RollCall":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("RollCallId"))
        guid = from_union([from_str, from_none], obj.get("RollCallGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("RollCallLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("RollCallRowVersion"))
        person_id = from_union([from_int, from_none], obj.get("RollCallPersonId"))
        person_name = from_union([from_str, from_none], obj.get("RollCallPersonName"))
        value_id = from_union([from_int, from_none], obj.get("RollCallValueId"))
        value_name = from_union([from_str, from_none], obj.get("RollCallValueName"))
        sort = from_union([from_int, from_none], obj.get("RollCallSort"))
        result = from_union([from_int, from_none], obj.get("RollCallResult"))
        event_item_id = from_union(
            [from_int, from_none], obj.get("RollCallEventItemId")
        )
        return RollCall(
            id,
            guid,
            last_modified_utc,
            row_version,
            person_id,
            person_name,
            value_id,
            value_name,
            sort,
            result,
            event_item_id,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["RollCallId"] = from_union([from_int, from_none], self.id)
        result["RollCallGuid"] = from_union([from_str, from_none], self.guid)
        result["RollCallLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["RollCallRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["RollCallPersonId"] = from_union([from_int, from_none], self.person_id)
        result["RollCallPersonName"] = from_union(
            [from_str, from_none], self.person_name
        )
        result["RollCallValueId"] = from_union([from_int, from_none], self.value_id)
        result["RollCallValueName"] = from_union([from_str, from_none], self.value_name)
        result["RollCallSort"] = from_union([from_int, from_none], self.sort)
        result["RollCallResult"] = from_union([from_int, from_none], self.result)
        result["RollCallEventItemId"] = from_union(
            [from_int, from_none], self.event_item_id
        )
        return result


def roll_call_from_dict(s: Any) -> RollCall:
    return RollCall.from_dict(s)


def roll_call_to_dict(x: RollCall) -> Any:
    return to_class(RollCall, x)


@dataclass
class Vote:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    person_id: Optional[int]
    person_name: Optional[str]
    value_id: Optional[int]
    value_name: Optional[str]
    sort: Optional[int]
    result: Optional[int]
    event_item_id: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> "Vote":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("VoteId"))
        guid = from_union([from_str, from_none], obj.get("VoteGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("VoteLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("VoteRowVersion"))
        person_id = from_union([from_int, from_none], obj.get("VotePersonId"))
        person_name = from_union([from_str, from_none], obj.get("VotePersonName"))
        value_id = from_union([from_int, from_none], obj.get("VoteValueId"))
        value_name = from_union([from_str, from_none], obj.get("VoteValueName"))
        sort = from_union([from_int, from_none], obj.get("VoteSort"))
        result = from_union([from_int, from_none], obj.get("VoteResult"))
        event_item_id = from_union([from_int, from_none], obj.get("VoteEventItemId"))
        return Vote(
            id,
            guid,
            last_modified_utc,
            row_version,
            person_id,
            person_name,
            value_id,
            value_name,
            sort,
            result,
            event_item_id,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["VoteId"] = from_union([from_int, from_none], self.id)
        result["VoteGuid"] = from_union([from_str, from_none], self.guid)
        result["VoteLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["VoteRowVersion"] = from_union([from_str, from_none], self.row_version)
        result["VotePersonId"] = from_union([from_int, from_none], self.person_id)
        result["VotePersonName"] = from_union([from_str, from_none], self.person_name)
        result["VoteValueId"] = from_union([from_int, from_none], self.value_id)
        result["VoteValueName"] = from_union([from_str, from_none], self.value_name)
        result["VoteSort"] = from_union([from_int, from_none], self.sort)
        result["VoteResult"] = from_union([from_int, from_none], self.result)
        result["VoteEventItemId"] = from_union(
            [from_int, from_none], self.event_item_id
        )
        return result


def vote_from_dict(s: Any) -> Vote:
    return Vote.from_dict(s)


def vote_to_dict(x: Vote) -> Any:
    return to_class(Vote, x)


@dataclass
class VoteType:
    id: Optional[int]
    guid: Optional[str]
    last_modified_utc: Optional[datetime]
    row_version: Optional[str]
    name: Optional[str]
    plural_name: Optional[str]
    used_for: Optional[int]
    result: Optional[int]
    sort: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> "VoteType":
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("VoteTypeId"))
        guid = from_union([from_str, from_none], obj.get("VoteTypeGuid"))
        last_modified_utc = from_union(
            [from_datetime, from_none], obj.get("VoteTypeLastModifiedUtc")
        )
        row_version = from_union([from_str, from_none], obj.get("VoteTypeRowVersion"))
        name = from_union([from_str, from_none], obj.get("VoteTypeName"))
        plural_name = from_union([from_str, from_none], obj.get("VoteTypePluralName"))
        used_for = from_union([from_int, from_none], obj.get("VoteTypeUsedFor"))
        result = from_union([from_int, from_none], obj.get("VoteTypeResult"))
        sort = from_union([from_int, from_none], obj.get("VoteTypeSort"))
        return VoteType(
            id,
            guid,
            last_modified_utc,
            row_version,
            name,
            plural_name,
            used_for,
            result,
            sort,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["VoteTypeId"] = from_union([from_int, from_none], self.id)
        result["VoteTypeGuid"] = from_union([from_str, from_none], self.guid)
        result["VoteTypeLastModifiedUtc"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_modified_utc
        )
        result["VoteTypeRowVersion"] = from_union(
            [from_str, from_none], self.row_version
        )
        result["VoteTypeName"] = from_union([from_str, from_none], self.name)
        result["VoteTypePluralName"] = from_union(
            [from_str, from_none], self.plural_name
        )
        result["VoteTypeUsedFor"] = from_union([from_int, from_none], self.used_for)
        result["VoteTypeResult"] = from_union([from_int, from_none], self.result)
        result["VoteTypeSort"] = from_union([from_int, from_none], self.sort)
        return result


def vote_type_from_dict(s: Any) -> VoteType:
    return VoteType.from_dict(s)


def vote_type_to_dict(x: VoteType) -> Any:
    return to_class(VoteType, x)
