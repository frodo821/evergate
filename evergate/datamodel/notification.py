""""""

from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class SenderType(str, Enum):
  """Types of senders.
  """
  character = "character"
  corporation = "corporation"
  alliance = "alliance"
  faction = "faction"
  other = "other"


class NotificationType(str, Enum):
  """Types of notifications.
  """

  AcceptedAlly = "AcceptedAlly"
  AcceptedSurrender = "AcceptedSurrender"
  AgentRetiredTrigravian = "AgentRetiredTrigravian"
  AllAnchoringMsg = "AllAnchoringMsg"
  AllMaintenanceBillMsg = "AllMaintenanceBillMsg"
  AllStrucInvulnerableMsg = "AllStrucInvulnerableMsg"
  AllStructVulnerableMsg = "AllStructVulnerableMsg"
  AllWarCorpJoinedAllianceMsg = "AllWarCorpJoinedAllianceMsg"
  AllWarDeclaredMsg = "AllWarDeclaredMsg"
  AllWarInvalidatedMsg = "AllWarInvalidatedMsg"
  AllWarRetractedMsg = "AllWarRetractedMsg"
  AllWarSurrenderMsg = "AllWarSurrenderMsg"
  AllianceCapitalChanged = "AllianceCapitalChanged"
  AllianceWarDeclaredV2 = "AllianceWarDeclaredV2"
  AllyContractCancelled = "AllyContractCancelled"
  AllyJoinedWarAggressorMsg = "AllyJoinedWarAggressorMsg"
  AllyJoinedWarAllyMsg = "AllyJoinedWarAllyMsg"
  AllyJoinedWarDefenderMsg = "AllyJoinedWarDefenderMsg"
  BattlePunishFriendlyFire = "BattlePunishFriendlyFire"
  BillOutOfMoneyMsg = "BillOutOfMoneyMsg"
  BillPaidCorpAllMsg = "BillPaidCorpAllMsg"
  BountyClaimMsg = "BountyClaimMsg"
  BountyESSShared = "BountyESSShared"
  BountyESSTaken = "BountyESSTaken"
  BountyPlacedAlliance = "BountyPlacedAlliance"
  BountyPlacedChar = "BountyPlacedChar"
  BountyPlacedCorp = "BountyPlacedCorp"
  BountyYourBountyClaimed = "BountyYourBountyClaimed"
  BuddyConnectContactAdd = "BuddyConnectContactAdd"
  CharAppAcceptMsg = "CharAppAcceptMsg"
  CharAppRejectMsg = "CharAppRejectMsg"
  CharAppWithdrawMsg = "CharAppWithdrawMsg"
  CharLeftCorpMsg = "CharLeftCorpMsg"
  CharMedalMsg = "CharMedalMsg"
  CharTerminationMsg = "CharTerminationMsg"
  CloneActivationMsg = "CloneActivationMsg"
  CloneActivationMsg2 = "CloneActivationMsg2"
  CloneMovedMsg = "CloneMovedMsg"
  CloneRevokedMsg1 = "CloneRevokedMsg1"
  CloneRevokedMsg2 = "CloneRevokedMsg2"
  CombatOperationFinished = "CombatOperationFinished"
  ContactAdd = "ContactAdd"
  ContactEdit = "ContactEdit"
  ContainerPasswordMsg = "ContainerPasswordMsg"
  ContractRegionChangedToPochven = "ContractRegionChangedToPochven"
  CorpAllBillMsg = "CorpAllBillMsg"
  CorpAppAcceptMsg = "CorpAppAcceptMsg"
  CorpAppInvitedMsg = "CorpAppInvitedMsg"
  CorpAppNewMsg = "CorpAppNewMsg"
  CorpAppRejectCustomMsg = "CorpAppRejectCustomMsg"
  CorpAppRejectMsg = "CorpAppRejectMsg"
  CorpBecameWarEligible = "CorpBecameWarEligible"
  CorpDividendMsg = "CorpDividendMsg"
  CorpFriendlyFireDisableTimerCompleted = "CorpFriendlyFireDisableTimerCompleted"
  CorpFriendlyFireDisableTimerStarted = "CorpFriendlyFireDisableTimerStarted"
  CorpFriendlyFireEnableTimerCompleted = "CorpFriendlyFireEnableTimerCompleted"
  CorpFriendlyFireEnableTimerStarted = "CorpFriendlyFireEnableTimerStarted"
  CorpKicked = "CorpKicked"
  CorpLiquidationMsg = "CorpLiquidationMsg"
  CorpNewCEOMsg = "CorpNewCEOMsg"
  CorpNewsMsg = "CorpNewsMsg"
  CorpNoLongerWarEligible = "CorpNoLongerWarEligible"
  CorpOfficeExpirationMsg = "CorpOfficeExpirationMsg"
  CorpStructLostMsg = "CorpStructLostMsg"
  CorpTaxChangeMsg = "CorpTaxChangeMsg"
  CorpVoteCEORevokedMsg = "CorpVoteCEORevokedMsg"
  CorpVoteMsg = "CorpVoteMsg"
  CorpWarDeclaredMsg = "CorpWarDeclaredMsg"
  CorpWarDeclaredV2 = "CorpWarDeclaredV2"
  CorpWarFightingLegalMsg = "CorpWarFightingLegalMsg"
  CorpWarInvalidatedMsg = "CorpWarInvalidatedMsg"
  CorpWarRetractedMsg = "CorpWarRetractedMsg"
  CorpWarSurrenderMsg = "CorpWarSurrenderMsg"
  CustomsMsg = "CustomsMsg"
  DeclareWar = "DeclareWar"
  DistrictAttacked = "DistrictAttacked"
  DustAppAcceptedMsg = "DustAppAcceptedMsg"
  ESSMainBankLink = "ESSMainBankLink"
  EntosisCaptureStarted = "EntosisCaptureStarted"
  ExpertSystemExpired = "ExpertSystemExpired"
  ExpertSystemExpiryImminent = "ExpertSystemExpiryImminent"
  FWAllianceKickMsg = "FWAllianceKickMsg"
  FWAllianceWarningMsg = "FWAllianceWarningMsg"
  FWCharKickMsg = "FWCharKickMsg"
  FWCharRankGainMsg = "FWCharRankGainMsg"
  FWCharRankLossMsg = "FWCharRankLossMsg"
  FWCharWarningMsg = "FWCharWarningMsg"
  FWCorpJoinMsg = "FWCorpJoinMsg"
  FWCorpKickMsg = "FWCorpKickMsg"
  FWCorpLeaveMsg = "FWCorpLeaveMsg"
  FWCorpWarningMsg = "FWCorpWarningMsg"
  FacWarCorpJoinRequestMsg = "FacWarCorpJoinRequestMsg"
  FacWarCorpJoinWithdrawMsg = "FacWarCorpJoinWithdrawMsg"
  FacWarCorpLeaveRequestMsg = "FacWarCorpLeaveRequestMsg"
  FacWarCorpLeaveWithdrawMsg = "FacWarCorpLeaveWithdrawMsg"
  FacWarLPDisqualifiedEvent = "FacWarLPDisqualifiedEvent"
  FacWarLPDisqualifiedKill = "FacWarLPDisqualifiedKill"
  FacWarLPPayoutEvent = "FacWarLPPayoutEvent"
  FacWarLPPayoutKill = "FacWarLPPayoutKill"
  GameTimeAdded = "GameTimeAdded"
  GameTimeReceived = "GameTimeReceived"
  GameTimeSent = "GameTimeSent"
  GiftReceived = "GiftReceived"
  IHubDestroyedByBillFailure = "IHubDestroyedByBillFailure"
  IncursionCompletedMsg = "IncursionCompletedMsg"
  IndustryOperationFinished = "IndustryOperationFinished"
  IndustryTeamAuctionLost = "IndustryTeamAuctionLost"
  IndustryTeamAuctionWon = "IndustryTeamAuctionWon"
  InfrastructureHubBillAboutToExpire = "InfrastructureHubBillAboutToExpire"
  InsuranceExpirationMsg = "InsuranceExpirationMsg"
  InsuranceFirstShipMsg = "InsuranceFirstShipMsg"
  InsuranceInvalidatedMsg = "InsuranceInvalidatedMsg"
  InsuranceIssuedMsg = "InsuranceIssuedMsg"
  InsurancePayoutMsg = "InsurancePayoutMsg"
  InvasionCompletedMsg = "InvasionCompletedMsg"
  InvasionSystemLogin = "InvasionSystemLogin"
  InvasionSystemStart = "InvasionSystemStart"
  JumpCloneDeletedMsg1 = "JumpCloneDeletedMsg1"
  JumpCloneDeletedMsg2 = "JumpCloneDeletedMsg2"
  KillReportFinalBlow = "KillReportFinalBlow"
  KillReportVictim = "KillReportVictim"
  KillRightAvailable = "KillRightAvailable"
  KillRightAvailableOpen = "KillRightAvailableOpen"
  KillRightEarned = "KillRightEarned"
  KillRightUnavailable = "KillRightUnavailable"
  KillRightUnavailableOpen = "KillRightUnavailableOpen"
  KillRightUsed = "KillRightUsed"
  LocateCharMsg = "LocateCharMsg"
  MadeWarMutual = "MadeWarMutual"
  MercOfferRetractedMsg = "MercOfferRetractedMsg"
  MercOfferedNegotiationMsg = "MercOfferedNegotiationMsg"
  MissionCanceledTriglavian = "MissionCanceledTriglavian"
  MissionOfferExpirationMsg = "MissionOfferExpirationMsg"
  MissionTimeoutMsg = "MissionTimeoutMsg"
  MoonminingAutomaticFracture = "MoonminingAutomaticFracture"
  MoonminingExtractionCancelled = "MoonminingExtractionCancelled"
  MoonminingExtractionFinished = "MoonminingExtractionFinished"
  MoonminingExtractionStarted = "MoonminingExtractionStarted"
  MoonminingLaserFired = "MoonminingLaserFired"
  MutualWarExpired = "MutualWarExpired"
  MutualWarInviteAccepted = "MutualWarInviteAccepted"
  MutualWarInviteRejected = "MutualWarInviteRejected"
  MutualWarInviteSent = "MutualWarInviteSent"
  NPCStandingsGained = "NPCStandingsGained"
  NPCStandingsLost = "NPCStandingsLost"
  OfferToAllyRetracted = "OfferToAllyRetracted"
  OfferedSurrender = "OfferedSurrender"
  OfferedToAlly = "OfferedToAlly"
  OfficeLeaseCanceledInsufficientStandings = "OfficeLeaseCanceledInsufficientStandings"
  OldLscMessages = "OldLscMessages"
  OperationFinished = "OperationFinished"
  OrbitalAttacked = "OrbitalAttacked"
  OrbitalReinforced = "OrbitalReinforced"
  OwnershipTransferred = "OwnershipTransferred"
  RaffleCreated = "RaffleCreated"
  RaffleExpired = "RaffleExpired"
  RaffleFinished = "RaffleFinished"
  ReimbursementMsg = "ReimbursementMsg"
  ResearchMissionAvailableMsg = "ResearchMissionAvailableMsg"
  RetractsWar = "RetractsWar"
  SeasonalChallengeCompleted = "SeasonalChallengeCompleted"
  SovAllClaimAquiredMsg = "SovAllClaimAquiredMsg"
  SovAllClaimLostMsg = "SovAllClaimLostMsg"
  SovCommandNodeEventStarted = "SovCommandNodeEventStarted"
  SovCorpBillLateMsg = "SovCorpBillLateMsg"
  SovCorpClaimFailMsg = "SovCorpClaimFailMsg"
  SovDisruptorMsg = "SovDisruptorMsg"
  SovStationEnteredFreeport = "SovStationEnteredFreeport"
  SovStructureDestroyed = "SovStructureDestroyed"
  SovStructureReinforced = "SovStructureReinforced"
  SovStructureSelfDestructCancel = "SovStructureSelfDestructCancel"
  SovStructureSelfDestructFinished = "SovStructureSelfDestructFinished"
  SovStructureSelfDestructRequested = "SovStructureSelfDestructRequested"
  SovereigntyIHDamageMsg = "SovereigntyIHDamageMsg"
  SovereigntySBUDamageMsg = "SovereigntySBUDamageMsg"
  SovereigntyTCUDamageMsg = "SovereigntyTCUDamageMsg"
  StationAggressionMsg1 = "StationAggressionMsg1"
  StationAggressionMsg2 = "StationAggressionMsg2"
  StationConquerMsg = "StationConquerMsg"
  StationServiceDisabled = "StationServiceDisabled"
  StationServiceEnabled = "StationServiceEnabled"
  StationStateChangeMsg = "StationStateChangeMsg"
  StoryLineMissionAvailableMsg = "StoryLineMissionAvailableMsg"
  StructureAnchoring = "StructureAnchoring"
  StructureCourierContractChanged = "StructureCourierContractChanged"
  StructureDestroyed = "StructureDestroyed"
  StructureFuelAlert = "StructureFuelAlert"
  StructureImpendingAbandonmentAssetsAtRisk = "StructureImpendingAbandonmentAssetsAtRisk"
  StructureItemsDelivered = "StructureItemsDelivered"
  StructureItemsMovedToSafety = "StructureItemsMovedToSafety"
  StructureLostArmor = "StructureLostArmor"
  StructureLostShields = "StructureLostShields"
  StructureOnline = "StructureOnline"
  StructureServicesOffline = "StructureServicesOffline"
  StructureUnanchoring = "StructureUnanchoring"
  StructureUnderAttack = "StructureUnderAttack"
  StructureWentHighPower = "StructureWentHighPower"
  StructureWentLowPower = "StructureWentLowPower"
  StructuresJobsCancelled = "StructuresJobsCancelled"
  StructuresJobsPaused = "StructuresJobsPaused"
  StructuresReinforcementChanged = "StructuresReinforcementChanged"
  TowerAlertMsg = "TowerAlertMsg"
  TowerResourceAlertMsg = "TowerResourceAlertMsg"
  TransactionReversalMsg = "TransactionReversalMsg"
  TutorialMsg = "TutorialMsg"
  WarAdopted = "WarAdopted "
  WarAllyInherited = "WarAllyInherited"
  WarAllyOfferDeclinedMsg = "WarAllyOfferDeclinedMsg"
  WarConcordInvalidates = "WarConcordInvalidates"
  WarDeclared = "WarDeclared"
  WarEndedHqSecurityDrop = "WarEndedHqSecurityDrop"
  WarHQRemovedFromSpace = "WarHQRemovedFromSpace"
  WarInherited = "WarInherited"
  WarInvalid = "WarInvalid"
  WarRetracted = "WarRetracted"
  WarRetractedByConcord = "WarRetractedByConcord"
  WarSurrenderDeclinedMsg = "WarSurrenderDeclinedMsg"
  WarSurrenderOfferMsg = "WarSurrenderOfferMsg"


class Notification(BaseModel):
  """A data model for a notification.

  Attributes:
    is_read (bool): Whether the notification is read.
    notification_id (int): An id of the notification.
    sender_id (int): An id of the sender of the notification.
    sender_type (SenderType): The type of the sender.
    text (str): The text of the notification.
    timestamp (datetime): The timestamp of the notification.
    type (NotificationType): The type of the notification.
  """

  is_read: bool = Field(False, description="Whether the notification is read.")
  notification_id: int = Field(description="An id of the notification.")
  sender_id: int = Field(description="An id of the sender of the notification.")
  sender_type: SenderType = Field(description="The type of the sender.")
  text: str = Field("", description="The text of the notification.")
  timestamp: datetime = Field(description="The timestamp of the notification.")
  type: NotificationType = Field(description="The type of the notification.")


class ContactNotification(BaseModel):
  """A data model for a contact notification.

  Attributes:
    message (str): The message of the notification.
    notification_id (int): An id of the notification.
    send_date (datetime): The date the notification was sent.
    sender_character_id (int): An id of the sender of the notification.
    standing_level (float): A number representing the standing level the receiver has been added at by the sender.
  """

  message: str = Field(description="The message of the notification.")
  notification_id: int = Field(description="An id of the notification.")
  send_date: datetime = Field(description="The date the notification was sent.")
  sender_character_id: int = Field(
      description="An id of the sender of the notification.")
  standing_level: float = Field(description=(
      "A number representing the standing level the receiver has been added at by the sender. "
      "The standing levels are as follows: -10 -> Terrible | -5 -> Bad | 0 -> Neutral | 5 -> Good | 10 -> Excellent"
  ))