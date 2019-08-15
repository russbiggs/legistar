from cachetools import TTLCache, cachedmethod
from cachetools.keys import hashkey
from datetime import datetime
from functools import reduce, partial
import json
import operator
from typing import List, Dict
import urllib.parse

from .models import *
from .wrapped_session import WrappedSession


class Legistar(WrappedSession):

    default_url = "https://webapi.legistar.com"

    def __init__(
        self,
        legistar_client: str,
        host: str = default_url,
        version: str = "v1",
        url_params={},
        maxsize=128,
        ttl=3600,
    ):
        self.host = host
        self.version = version
        self.cache = TTLCache(maxsize, ttl)
        self.legistar_client = legistar_client
        self._url_params = url_params
        self._url = f"{self.host}/{self.version}/{self.legistar_client}/"
        super(Legistar, self).__init__()

    def _build_url(self, *args, **kwargs) -> str:
        parts = [self._url, *[f"{arg}/" for arg in args]]
        url = reduce(urllib.parse.urljoin, parts).rstrip("/")
        odata = kwargs.pop('odata', '')
        if self._url_params or kwargs:
            params = {**kwargs, **self._url_params}
            param_string = urllib.parse.urlencode(params)
            url = urllib.parse.urljoin(url, f"?{param_string}")
            if odata:
                url += f'&{odata}'
        if odata:
            url += f'?{odata}'
        return url

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "action"))
    def action(self, action_id: int, odata:str="") -> Action:
        url = self._build_url("actions", action_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        action_data = action_from_dict(data)
        return action_data

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "all_actions"))
    def all_actions(self, odata:str="") -> List[Action]:
        url = self._build_url("actions", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        actions = [action_from_dict(item) for item in data]
        return actions

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "body"))
    def body(self, body_id: int, odata:str="") -> Body:
        url = self._build_url("bodies", body_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        body_data = body_from_dict(data)
        return body_data

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "all_bodies"))
    def all_bodies(self, odata:str="") -> List[Body]:
        url = self._build_url("bodies", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        bodies = [body_from_dict(item) for item in data]
        return bodies

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "body_type"))
    def body_type(self, body_type_id: int, odata:str="") -> BodyType:
        url = self._build_url("bodytypes", body_type_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        body_type_data = body_type_from_dict(data)
        return body_type_data

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "all_body_types"))
    def all_body_types(self, odata:str="") -> List[BodyType]:
        url = self._build_url("bodytypes", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        body_types = [body_type_from_dict(item) for item in data]
        return body_types

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_code_sections")
    )
    def all_code_sections(self, odata:str="") -> List[CodeSection]:
        url = self._build_url("codesections", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        code_sections = [code_section_from_dict(item) for item in data]
        return code_sections

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "code_section"))
    def code_section(self, code_section_id: int, odata:str="") -> CodeSection:
        url = self._build_url("codesections", code_section_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        code_section_data = code_section_from_dict(data)
        return code_section_data

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "event_item"))
    def event_item(
        self, event_id: int, event_item_id: int, odata:str="", **kwargs: Dict
    ) -> EventItem:
        agenda_note = kwargs.get("agenda_note", 0)
        minutes_note = kwargs.get("minutes_note", 0)
        attachments = kwargs.get("attachments", 0)
        url = self._build_url(
            "events",
            event_id,
            "eventitems",
            event_item_id,
            agendanote=agenda_note,
            minutesnote=minutes_note,
            attachments=attachments,
        )
        r = self.get(url)
        data = json.loads(r.text)
        event_item_data = event_item_from_dict(data)
        return event_item_data

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "all_event_items"))
    def all_event_items(self, event_id: int, odata:str="", **kwargs: Dict) -> List[EventItem]:
        agenda_note = kwargs.get("agenda_note", 0)
        minutes_note = kwargs.get("minutes_note", 0)
        attachments = kwargs.get("attachments", 0)
        url = self._build_url(
            "events",
            event_id,
            "eventitems",
            agendanote=agenda_note,
            minutesnote=minutes_note,
            attachments=attachments,
        )
        r = self.get(url)
        data = json.loads(r.text)
        event_items = [event_item_from_dict(item) for item in data]
        return event_items

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "all_events"))
    def all_events(self, odata:str="") -> List[Event]:
        url = self._build_url("events", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        events = [event_from_dict(item) for item in data]
        return events

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "event"))
    def event(self, event_id: int, odata:str="",  **kwargs: Dict) -> Event:
        event_items = kwargs.get("event_items", 0)
        agenda_note = kwargs.get("agenda_note", 0)
        minutes_note = kwargs.get("minutes_note", 0)
        event_item_attachments = kwargs.get("event_item_attachments", 0)
        url = self._build_url(
            "events",
            event_id,
            eventitems=event_items,
            agendanote=agenda_note,
            minutesnote=minutes_note,
            eventitemattachments=event_item_attachments,
        )
        r = self.get(url)
        data = json.loads(r.text)
        event_data = event_from_dict(data)
        return event_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "event_dates_by_body")
    )
    def event_dates_by_body(
        self, body_id: int, future_dates_only: bool = True, odata:str=""
    ) -> List[datetime]:
        url = self._build_url("eventdates", body_id, futuredatesonly=future_dates_only, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        event_dates = [from_datetime(item) for item in data]
        return event_dates

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "all_indexes"))
    def all_indexes(self, odata:str="") -> List[Index]:
        url = self._build_url("indexes", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        indexes = [index_from_dict(item) for item in data]
        return indexes

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "index"))
    def index(self, index_id: int, odata:str="") -> Index:
        url = self._build_url("indexes", index_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        index_data = index_from_dict(data)
        return index_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_matter_attachments")
    )
    def all_matter_attachments(self, matter_id: int, odata:str="") -> List[MatterAttachment]:
        url = self._build_url("matters", matter_id, "attachments", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_attachments = [matter_attachment_from_dict(item) for item in data]
        return matter_attachments

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "matter_attachment")
    )
    def matter_attachment(
        self, matter_id: int, matter_attachment_id: int, odata:str=""
    ) -> MatterAttachment:
        url = self._build_url("matters", matter_id, "attachments", matter_attachment_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_attachment = matter_attachment_from_dict(data)
        return matter_attachment

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "matter_attachment_file")
    )
    def matter_attachment_file(
        self, matter_id: int, matter_attachment_id: int, odata:str=""
    ) -> bytes:
        url = self._build_url(
            "matters", matter_id, "attachments", matter_attachment_id, "file"
        )
        r = self.get(url)
        return r.content

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "matter_code_section")
    )
    def matter_code_section(
        self, matter_id: int, matter_code_section_id: int, odata:str=""
    ) -> MatterCodeSection:
        url = self._build_url(
            "matters", matter_id, "codesections", matter_code_section_id
        )
        r = self.get(url)
        data = json.loads(r.text)
        matter_code_section_data = matter_code_section_from_dict(data)
        return matter_code_section_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_matter_code_sections")
    )
    def all_matter_code_sections(self, matter_id: int, odata:str="") -> List[MatterCodeSection]:
        url = self._build_url("matters", matter_id, "codesections", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_code_sections = [matter_code_section_from_dict(item) for item in data]
        return matter_code_sections

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "matter_history"))
    def matter_history(
        self, matter_id: int, matter_history_id: int,  odata:str="", **kwargs: Dict
    ) -> MatterHistory:
        agenda_note = kwargs.get("agenda_note", 0)
        minutes_note = kwargs.get("minutes_note", 0)
        url = self._build_url(
            "matters",
            matter_id,
            "histories",
            matter_history_id,
            agendanote=agenda_note,
            minutesnote=minutes_note,
        )
        r = self.get(url)
        data = json.loads(r.text)
        matter_history_data = matter_history_from_dict(data)
        return matter_history_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_matter_histories")
    )
    def all_matter_histories(
        self, matter_id: int, odata:str="", **kwargs: Dict
    ) -> List[MatterHistory]:
        agenda_note = kwargs.get("agenda_note", 0)
        minutes_note = kwargs.get("minutes_note", 0)
        url = self._build_url(
            "matters",
            matter_id,
            "histories",
            agendanote=agenda_note,
            minutesnote=minutes_note,
        )
        r = self.get(url)
        data = json.loads(r.text)
        matter_histories = [matter_history_from_dict(item) for item in data]
        return matter_histories

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "matter_text"))
    def matter_text(self, matter_id: int, matter_text_id: int, odata:str="") -> MatterText:
        url = self._build_url("matters", matter_id, "texts", matter_text_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_text_data = matter_text_from_dict(data)
        return matter_text_data

    @cachedmethod(
        operator.attrgetter("cache"),
        key=partial(hashkey, "all_matter_texts_version_by_matter"),
    )
    def all_matter_texts_version_by_matter(
        self, matter_id: int, odata:str=""
    ) -> List[MatterTextVersion]:
        url = self._build_url("matters", matter_id, "versions", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_text_versions = [matter_text_version_from_dict(item) for item in data]
        return matter_text_versions

    @cachedmethod(
        operator.attrgetter("cache"),
        key=partial(hashkey, "all_matter_indexes_by_matter"),
    )
    def all_matter_indexes_by_matter(self, matter_id: int, odata:str="") -> List[MatterIndex]:
        url = self._build_url("matterindexes", "matter", matter_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_indexes = [matter_index_from_dict(item) for item in data]
        return matter_indexes

    @cachedmethod(
        operator.attrgetter("cache"),
        key=partial(hashkey, "all_matter_indexes_by_index"),
    )
    def all_matter_indexes_by_index(self, index_id: int, odata:str="") -> List[MatterIndex]:
        url = self._build_url("matterindexes", "index", index_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_indexes = [matter_index_from_dict(item) for item in data]
        return matter_indexes

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_matter_indexes")
    )
    def all_matter_indexes(self, odata:str="") -> List[MatterIndex]:
        url = self._build_url("matterindexes", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_indexes = [matter_index_from_dict(item) for item in data]
        return matter_indexes

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "matter_index"))
    def matter_index(self, matter_index_id: int, odata:str="") -> MatterIndex:
        url = self._build_url("matterindexes", matter_index_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_text_data = matter_index_from_dict(data)
        return matter_text_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_matter_relations")
    )
    def all_matter_relations(self, matter_id: int, odata:str="") -> List[MatterRelation]:
        url = self._build_url("matters", matter_id, "relations", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_relations = [matter_relation_from_dict(item) for item in data]
        return matter_relations

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "matter_relation"))
    def matter_relation(
        self, matter_id: int, matter_relation_id: int, odata:str=""
    ) -> MatterRelation:
        url = self._build_url("matters", matter_id, "relations", matter_relation_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_relation_data = matter_relation_from_dict(data)
        return matter_relation_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_matter_sponsors")
    )
    def all_matter_sponsors(self, matter_id: int, odata:str="") -> List[MatterSponsor]:
        url = self._build_url("matters", matter_id, "sponsors", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_sponsors = [matter_sponsor_from_dict(item) for item in data]
        return matter_sponsors

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "matter_sponsor"))
    def matter_sponsor(self, matter_id: int, matter_sponsor_id: int, odata:str="") -> MatterSponsor:
        url = self._build_url("matters", matter_id, "sponsors", matter_sponsor_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_sponsor_data = matter_sponsor_from_dict(data)
        return matter_sponsor_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_matter_statuses")
    )
    def all_matter_statuses(self, odata:str="") -> List[MatterStatus]:
        url = self._build_url("matterstatuses", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_statuses = [matter_status_from_dict(item) for item in data]
        return matter_statuses

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "matter_status"))
    def matter_status(self, matter_status_id: int, odata:str="") -> MatterStatus:
        url = self._build_url("matterstatuses", matter_status_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_status_data = matter_status_from_dict(data)
        return matter_status_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_matter_requesters")
    )
    def all_matter_requesters(self, odata:str="") -> List[MatterRequester]:
        url = self._build_url("matterrequesters", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_requesters = [matter_requester_from_dict(item) for item in data]
        return matter_requesters

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "all_matters"))
    def all_matters(self, odata:str="") -> List[Matter]:
        url = self._build_url("matters", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matters = [matter_from_dict(item) for item in data]
        return matters

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "matter"))
    def matter(self, matter_id: int, odata:str="") -> Matter:
        url = self._build_url("matters", matter_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_data = matter_from_dict(data)
        return matter_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_matter_types")
    )
    def all_matter_types(self, odata:str="") -> List[MatterType]:
        url = self._build_url("mattertypes", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_types = [matter_type_from_dict(item) for item in data]
        return matter_types

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "matter_type"))
    def matter_type(self, matter_type_id: int, odata:str="") -> MatterType:
        url = self._build_url("mattertypes", matter_type_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        matter_type_data = matter_type_from_dict(data)
        return matter_type_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_office_records")
    )
    def all_office_records(self, odata:str="") -> List[OfficeRecord]:
        url = self._build_url("officerecords", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        office_records = [office_record_from_dict(item) for item in data]
        return office_records

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "office_record"))
    def office_record(self, person_id: int, odata:str="") -> OfficeRecord:
        url = self._build_url("officerecords", person_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        office_record = office_record_from_dict(data)
        return office_record

    @cachedmethod(
        operator.attrgetter("cache"),
        key=partial(hashkey, "all_office_records_by_person"),
    )
    def all_office_records_by_person(self, person_id: int, odata:str="") -> List[OfficeRecord]:
        url = self._build_url("persons", person_id, "officerecords", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        office_records = [office_record_from_dict(item) for item in data]
        return office_records

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_office_records_by_body")
    )
    def all_office_records_by_body(self, body_id: int, odata:str="") -> List[OfficeRecord]:
        url = self._build_url("bodies", body_id, "officerecords", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        office_records = [office_record_from_dict(item) for item in data]
        return office_records

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "all_persons"))
    def all_persons(self, odata:str="") -> List[Person]:
        url = self._build_url("persons", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        persons = [person_from_dict(item) for item in data]
        return persons

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "person"))
    def person(self, person_id: int, odata:str="") -> Person:
        url = self._build_url("persons", person_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        person_data = person_from_dict(data)
        return person_data

    @cachedmethod(
        operator.attrgetter("cache"),
        key=partial(hashkey, "all_roll_calls_by_event_item"),
    )
    def all_roll_calls_by_event_item(self, event_item_id: int, odata:str="") -> List[RollCall]:
        url = self._build_url("eventitems", event_item_id, "rollcalls", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        roll_calls = [roll_call_from_dict(item) for item in data]
        return roll_calls

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "roll_call_by_event_item")
    )
    def roll_call_by_event_item(
        self, event_item_id: int, roll_call_id: int, odata:str=""
    ) -> RollCall:
        url = self._build_url("eventitems", event_item_id, "rollcalls", roll_call_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        roll_call_data = roll_call_from_dict(data)
        return roll_call_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_roll_calls_by_person")
    )
    def all_roll_calls_by_person(self, person_id: int, odata:str="") -> List[RollCall]:
        url = self._build_url("persons", person_id, "rollcalls", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        roll_calls = [roll_call_from_dict(item) for item in data]
        return roll_calls

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_votes_by_event_item")
    )
    def all_votes_by_event_item(self, event_item_id: int, odata:str="") -> List[Vote]:
        url = self._build_url("eventitems", event_item_id, "votes", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        votes = [vote_from_dict(item) for item in data]
        return votes

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "vote_by_event_item")
    )
    def vote_by_event_item(self, event_item_id: int, vote_id: int, odata:str="") -> Vote:
        url = self._build_url("eventitems", event_item_id, "votes", vote_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        vote_data = vote_from_dict(data)
        return vote_data

    @cachedmethod(
        operator.attrgetter("cache"), key=partial(hashkey, "all_votes_by_person")
    )
    def all_votes_by_person(self, person_id: int, odata:str="") -> List[Vote]:
        url = self._build_url("persons", person_id, "votes", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        votes = [vote_from_dict(item) for item in data]
        return votes

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "all_vote_types"))
    def all_vote_types(self, odata:str="") -> List[VoteType]:
        url = self._build_url("votetypes", odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        vote_types = [vote_type_from_dict(item) for item in data]
        return vote_types

    @cachedmethod(operator.attrgetter("cache"), key=partial(hashkey, "vote_type"))
    def vote_type(self, vote_type_id: int, odata:str="") -> VoteType:
        url = self._build_url("votetypes", vote_type_id, odata=odata)
        r = self.get(url)
        data = json.loads(r.text)
        vote_type_data = vote_type_from_dict(data)
        return vote_type_data
