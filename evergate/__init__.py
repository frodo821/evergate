"""Evergate the Python binding for Eve Online's ESI (Eve Swagger Interface)
"""

from evergate.datamodel.agent import AgentResearch
from evergate.datamodel.alliance import Alliance, AllianceIcon
from evergate.datamodel.blueprint import Blueprint
from evergate.datamodel.character import (
    Character, CharacterAffiliation, CharacterGender, CharacterMedal,
    CharacterPortrait, CharacterRoles, CharacterStanding, CharacterTitle,
    CorporationHistory, JumpFatigue, MedalGraphic, MetalStatus, RoleType,
    StandingType)
from evergate.datamodel.contact import Contact, ContactLabel, ContactType
from evergate.datamodel.item import LocationFlag
from evergate.datamodel.notification import (ContactNotification, Notification,
                                             NotificationType, SenderType)

from evergate.procedure.alliance import (get_alliance_by_id, get_alliance_icons,
                                         get_alliance_ids,
                                         get_corporations_of_alliance)
from evergate.procedure.authorization import add_token, expire_token
from evergate.procedure.character import (
    calculate_cspa_charge, get_character, get_character_affiliations,
    get_character_blueprints, get_character_contact_notifications,
    get_character_jump_fatigue, get_character_medals,
    get_character_notifications, get_character_portrait, get_character_research,
    get_character_roles, get_character_standings, get_character_titles,
    get_corporation_histories)
from evergate.procedure.contact import (
    delete_character_contacts, get_alliance_contact_labels,
    get_alliance_contacts, get_character_contact_labels, get_character_contacts,
    get_corporation_contact_labels, get_corporation_contacts,
    post_character_contacts, put_character_contacts)

__all__ = [
    "AgentResearch",
    "Alliance",
    "AllianceIcon",
    "Blueprint",
    "Character",
    "CharacterAffiliation",
    "CharacterGender",
    "CharacterMedal",
    "CharacterPortrait",
    "CharacterRoles",
    "CharacterStanding",
    "CharacterTitle",
    "CorporationHistory",
    "JumpFatigue",
    "MedalGraphic",
    "MetalStatus",
    "RoleType",
    "StandingType",
    "Contact",
    "ContactLabel",
    "ContactType",
    "LocationFlag",
    "ContactNotification",
    "Notification",
    "NotificationType",
    "SenderType",
    "add_token",
    "expire_token",
    "get_alliance_by_id",
    "get_alliance_icons",
    "get_alliance_ids",
    "get_corporations_of_alliance",
    "get_alliance_contacts",
    "get_alliance_contact_labels",
    "get_corporation_contacts",
    "get_corporation_contact_labels",
    "get_character_contacts",
    "get_character_contact_labels",
    "post_character_contacts",
    "put_character_contacts",
    "delete_character_contacts",
    "get_character",
    "get_character_affiliations",
    "get_character_blueprints",
    "get_character_contact_notifications",
    "get_character_jump_fatigue",
    "get_character_medals",
    "get_character_notifications",
    "get_character_portrait",
    "get_character_research",
    "get_character_roles",
    "get_character_standings",
    "get_character_titles",
    "get_corporation_histories",
    "calculate_cspa_charge",
]
