from enum import Enum

class RaterEnum(str, Enum):
    NULL = None    
    SELF_RATE = "self-rate"
    RESPONDENTS = "respondents"
    SUPERVISOR = "supervisor"

class PotentialPerformanceEnum(str, Enum):
    NULL = None
    POTENTIAL = 'potential'
    PERFORMANCE = 'performance'
