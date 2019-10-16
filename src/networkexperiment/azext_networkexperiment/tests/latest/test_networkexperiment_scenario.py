# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class ApimgmtScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_apimgmt')
    def test_apimgmt(self, resource_group):

        self.kwargs.update({
            'name': 'test1'
        })

# create_or_update -- create
        self.cmd('networkexperiment profiles create  --profile-name "Profile1" --name "rg1" --location "WestUs" --enabled-state "Enabled"', checks=[
        ])

        self.cmd('networkexperiment profiles create  --profile-name "Profile1" --name "rg1" --enabled-state "Enabled"', checks=[
        ])

        self.cmd('networkexperiment profiles create  --profile-name "Profile1" --name "rg1"', checks=[
        ])

# create_or_update -- update
        self.cmd('networkexperiment profiles update  --profile-name "Profile1" --name "rg1" --location "WestUs" --enabled-state "Enabled"', checks=[
        ])

        self.cmd('networkexperiment profiles update  --profile-name "Profile1" --name "rg1" --enabled-state "Enabled"', checks=[
        ])

        self.cmd('networkexperiment profiles update  --profile-name "Profile1" --name "rg1"', checks=[
        ])

# delete -- delete
        self.cmd('networkexperiment profiles delete  --name "rg1" --profile-name "Profile1"', checks=[
        ])

        self.cmd('networkexperiment profiles delete  --name "rg1" --profile-name "Profile1"', checks=[
        ])

        self.cmd('networkexperiment profiles delete  --name "rg1" --profile-name "Profile1"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('networkexperiment profiles list  --name "rg1"', checks=[
        ])

        self.cmd('networkexperiment profiles list  --name "rg1"', checks=[
        ])

        self.cmd('networkexperiment profiles list  --name "rg1"', checks=[
        ])

# list -- list
        self.cmd('networkexperiment profiles list  --name "rg1"', checks=[
        ])

        self.cmd('networkexperiment profiles list  --name "rg1"', checks=[
        ])

        self.cmd('networkexperiment profiles list  --name "rg1"', checks=[
        ])

# get -- show
        self.cmd('networkexperiment profiles show  --name "rg1" --profile-name "Profile1"', checks=[
        ])

        self.cmd('networkexperiment profiles show  --name "rg1" --profile-name "Profile1"', checks=[
        ])

        self.cmd('networkexperiment profiles show  --name "rg1" --profile-name "Profile1"', checks=[
        ])

# create_or_update -- create
        self.cmd('networkexperiment experiment create  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1" --description "this is my first experiment!" --endpoint-a-name "endpoint A" --endpoint-a-endpoint "endpointA.net" --endpoint-b-name "endpoint B" --endpoint-b-endpoint "endpointB.net" --enabled-state "Enabled"', checks=[
        ])

        self.cmd('networkexperiment experiment create  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1" --description "string" --enabled-state "Enabled"', checks=[
        ])

        self.cmd('networkexperiment experiment create  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1"', checks=[
        ])

# create_or_update -- update
        self.cmd('networkexperiment experiment update  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1" --description "this is my first experiment!" --endpoint-a-name "endpoint A" --endpoint-a-endpoint "endpointA.net" --endpoint-b-name "endpoint B" --endpoint-b-endpoint "endpointB.net" --enabled-state "Enabled"', checks=[
        ])

        self.cmd('networkexperiment experiment update  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1" --description "string" --enabled-state "Enabled"', checks=[
        ])

        self.cmd('networkexperiment experiment update  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1"', checks=[
        ])

# delete -- delete
        self.cmd('networkexperiment experiment delete  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1"', checks=[
        ])

        self.cmd('networkexperiment experiment delete  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1"', checks=[
        ])

        self.cmd('networkexperiment experiment delete  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1"', checks=[
        ])

# list_by_profile -- list
        self.cmd('networkexperiment experiment list  --resource-group "rg1" --profile-name "Profile1"', checks=[
        ])

        self.cmd('networkexperiment experiment list  --resource-group "rg1" --profile-name "Profile1"', checks=[
        ])

        self.cmd('networkexperiment experiment list  --resource-group "rg1" --profile-name "Profile1"', checks=[
        ])

# get -- show
        self.cmd('networkexperiment experiment show  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1"', checks=[
        ])

        self.cmd('networkexperiment experiment show  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1"', checks=[
        ])

        self.cmd('networkexperiment experiment show  --resource-group "rg1" --profile-name "Profile1" --name "Experiment1"', checks=[
        ])
