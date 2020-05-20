
from __future__ import print_function

import py_trees

from srunner.scenarios.basic_scenario import BasicScenario
from srunner.scenarios.background_activity import BackgroundActivity


class ProactiveMergeScenario(BackgroundActivity):
    """
    Some documentation on ProactiveMergeScenario
    :param world is the CARLA world
    :param ego_vehicles is a list of ego vehicles for this scenario
    :param config is the scenario configuration (ScenarioConfiguration)
    :param randomize can be used to select parameters randomly (optional, default=False)
    :param debug_mode can be used to provide more comprehensive console output (optional, default=False)
    :param criteria_enable can be used to disable/enable scenario evaluation based on test criteria (optional, default=True)
    :param timeout is the overall scenario timeout (optional, default=60 seconds)
    """

    # some ego vehicle parameters
    # some parameters for the other vehicles

    def __init__(self, world, ego_vehicles, config, randomize=False, debug_mode=False, criteria_enable=True,
                 timeout=60 * 35):
        """
        Initialize all parameters required for ProactiveMergeScenario
        """

        # Call constructor of BasicScenario
        super(ProactiveMergeScenario, self).__init__(
          world,
          ego_vehicles,
          config,
          debug_mode,
          timeout=timeout,
          criteria_enable=criteria_enable,
          name='ProactiveMergeScenario')


    # def _create_behavior(self):
    #     """
    #     Setup the behavior for ProactiveMergeScenario
    #     """

    # def _create_test_criteria(self):
    #     """
    #     Setup the evaluation criteria for ProactiveMergeScenario
    #     """