"""A New Kind of Science cellular automata library."""

from . import alphabets, frontiers, loci, neighborhoods, rng, rules, seeds
from .alphabets import Alphabet, boolean, float_range_alphabet, int_range_alphabet, symbolic
from .frontiers import Frontier, time_slice
from .neighborhoods import Neighborhood, ar2_0d, axis_shell, change_count_shell, directional_fov
from .neighborhoods import directional_line, eca, history, l1_shell, literal_offsets, metric_radius, moore
from .neighborhoods import self_at, shell, von_neumann
from .neighborhoods import dyadrads_1d as dyadrads_1d_neighborhood
from .neighborhoods import dyadaxes_2d as dyadaxes_2d_neighborhood
from .neighborhoods import dyadaxes_3d as dyadaxes_3d_neighborhood
from .rng import derive_episode_rng, numpy_rng, splitmix64
from .rollout import apply_rule, canonical_coords, rollout
from .rules import Rule, RuleChannel, ar2_modular_0d, instantiate, rule_count, valid_rule_ids
from .rules import dyadrads_1d as dyadrads_1d_rule
from .rules import dyadaxes_2d as dyadaxes_2d_rule
from .rules import dyadaxes_3d as dyadaxes_3d_rule
from .seeds import Seed, bernoulli, constant, pair, point, render, selector_seed, uniform_pair
from .specs import Dynamics, RawEpisode, dynamics_from_spec

__all__ = [
    "Alphabet",
    "Dynamics",
    "Frontier",
    "Neighborhood",
    "RawEpisode",
    "Rule",
    "RuleChannel",
    "Seed",
    "alphabets",
    "apply_rule",
    "ar2_0d",
    "ar2_modular_0d",
    "axis_shell",
    "bernoulli",
    "boolean",
    "canonical_coords",
    "change_count_shell",
    "constant",
    "derive_episode_rng",
    "directional_fov",
    "directional_line",
    "dyadrads_1d_neighborhood",
    "dyadrads_1d_rule",
    "dyadaxes_2d_neighborhood",
    "dyadaxes_2d_rule",
    "dyadaxes_3d_neighborhood",
    "dyadaxes_3d_rule",
    "dynamics_from_spec",
    "eca",
    "float_range_alphabet",
    "frontiers",
    "history",
    "instantiate",
    "int_range_alphabet",
    "l1_shell",
    "literal_offsets",
    "loci",
    "metric_radius",
    "moore",
    "neighborhoods",
    "numpy_rng",
    "pair",
    "point",
    "render",
    "rng",
    "rollout",
    "rule_count",
    "rules",
    "selector_seed",
    "seeds",
    "self_at",
    "shell",
    "splitmix64",
    "symbolic",
    "time_slice",
    "uniform_pair",
    "valid_rule_ids",
    "von_neumann",
]
