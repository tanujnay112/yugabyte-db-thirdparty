#
# Copyright (c) YugaByte, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations
# under the License.
#

import os

from yugabyte_db_thirdparty.build_definition_helpers import *  # noqa


class ZLibDependency(Dependency):
    def __init__(self) -> None:
        super(ZLibDependency, self).__init__(
            name='zlib',
            version='1.2.12-yb-1',
            url_pattern='https://github.com/yugabyte/zlib/archive/refs/tags/v{0}.tar.gz',
            build_group=BUILD_GROUP_COMMON)
        self.copy_sources = True

    def build(self, builder: BuilderInterface) -> None:
        os.environ['TEST_LDFLAGS'] = '-L. libz.a -fuse-ld=lld'
        builder.build_with_configure(
            log_prefix=builder.log_prefix(self)
        )
        del os.environ['TEST_LDFLAGS']
