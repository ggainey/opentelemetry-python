# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
The OpenTelemetry logging API describes the classes used to generate logs and events.

The :class:`.LoggerProvider` provides users access to the :class:`.Logger` which in
turn is used to create :class:`.Event` and :class:`.Log` objects.

This module provides abstract (i.e. unimplemented) classes required for
logging, and a concrete no-op implementation :class:`.NoOpLogger` that allows applications
to use the API package alone without a supporting implementation.

To get a logger, you need to provide the package name from which you are
calling the logging APIs to OpenTelemetry by calling `LoggerProvider.get_logger`
with the calling module name and the version of your package.

The following code shows how to obtain a logger using the global :class:`.LoggerProvider`::

    from opentelemetry._logs import get_logger

    logger = get_logger("example-logger")

.. versionadded:: 1.15.0
"""

# pylint: disable=unused-import

from opentelemetry._logs._internal import (  # noqa: F401
    Logger,
    LoggerProvider,
    LogRecord,
    NoOpLogger,
    NoOpLoggerProvider,
    get_logger,
    get_logger_provider,
    set_logger_provider,
)
from opentelemetry._logs.severity import (  # noqa: F401
    SeverityNumber,
    std_to_otel,
)

__all__ = []
for key, value in globals().copy().items():  # type: ignore
    if not key.startswith("_"):
        value.__module__ = __name__  # type: ignore
        __all__.append(key)