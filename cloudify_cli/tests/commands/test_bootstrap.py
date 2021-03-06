########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

"""
Tests 'cfy bootstrap'
"""

from cloudify_cli import common
from cloudify_cli.tests import cli_runner
from cloudify_cli.tests.commands.test_cli_command import \
    CliCommandTest, BLUEPRINTS_DIR


class BootstrapTest(CliCommandTest):

    def test_bootstrap_install_plugins(self):

        cli_runner.run_cli('cfy init')
        blueprint_path = '{0}/local/{1}.yaml'\
                         .format(BLUEPRINTS_DIR,
                                 'blueprint_with_plugins')
        self.assert_method_called(
            cli_command='cfy bootstrap --install-plugins -p {0}'
                        .format(blueprint_path),
            module=common,
            function_name='install_blueprint_plugins',
            kwargs={'blueprint_path': blueprint_path}
        )

    def test_bootstrap_no_validations_install_plugins(self):

        cli_runner.run_cli('cfy init')
        blueprint_path = '{0}/local/{1}.yaml' \
            .format(BLUEPRINTS_DIR,
                    'blueprint_with_plugins')
        self.assert_method_called(
            cli_command='cfy bootstrap --skip-validations '
                        '--install-plugins -p {0}'
            .format(blueprint_path),
            module=common,
            function_name='install_blueprint_plugins',
            kwargs={'blueprint_path': blueprint_path}
        )

    def test_bootstrap_missing_plugin(self):

        cli_runner.run_cli('cfy init')
        blueprint_path = '{0}/local/{1}.yaml' \
            .format(BLUEPRINTS_DIR,
                    'blueprint_with_plugins')
        cli_command = 'cfy bootstrap -p {0}'.format(
            blueprint_path)

        self._assert_ex(
            cli_cmd=cli_command,
            err_str_segment='No module named tasks',
            possible_solutions=[
                "Run 'cfy local install-plugins -p {0}'"
                .format(blueprint_path),
                "Run 'cfy bootstrap --install-plugins -p {0}'"
                .format(blueprint_path)
            ]
        )

    def test_bootstrap_no_validation_missing_plugin(self):

        cli_runner.run_cli('cfy init')
        blueprint_path = '{0}/local/{1}.yaml' \
            .format(BLUEPRINTS_DIR,
                    'blueprint_with_plugins')
        cli_command = 'cfy bootstrap --skip-validations -p {0}'.format(
            blueprint_path)

        self._assert_ex(
            cli_cmd=cli_command,
            err_str_segment='No module named tasks',
            possible_solutions=[
                "Run 'cfy local install-plugins -p {0}'"
                .format(blueprint_path),
                "Run 'cfy bootstrap --install-plugins -p {0}'"
                .format(blueprint_path)
            ]
        )
