from .base_region_sampler import *
from .workspace_region_sampler import *
from .object_property_sampler import *

"""

Define different regions for different problem domains.

Naming convention for registering region smapler:
key: lower-case naming, each word separated by hyphens
value: lower-case naming, {problem_name}.{region_sampler_class_name}

"""
REGION_SAMPLERS = {
    "robox_tabletop_manipulation": {"table": TableRegionSampler},
    "robox_floor_manipulation": {"floor": TableRegionSampler},
    "robox_coffee_table_manipulation": {"coffee_table": TableRegionSampler},
    "robox_living_room_tabletop_manipulation": {
        "living_room_table": Robox100TableRegionSampler
    },
    "robox_study_tabletop_manipulation": {"study_table": Robox100TableRegionSampler},
    "robox_kitchen_tabletop_manipulation": {
        "kitchen_table": Robox100TableRegionSampler
    },
}


def update_region_samplers(
    problem_name, region_sampler_name, region_sampler_class_name
):
    """
    This is for registering customized region samplers without adding to / modifying original codebase.
    """
    if problem_name not in REGION_SAMPLERS:
        REGION_SAMPLERS[problem_name] = {}
    REGION_SAMPLERS[problem_name][region_sampler_name] = eval(
        f"{problem_name}.{region_sampler_class_name}"
    )


def get_region_samplers(problem_name, region_sampler_name):
    return REGION_SAMPLERS[problem_name][region_sampler_name]
