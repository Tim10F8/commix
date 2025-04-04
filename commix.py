#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of Commix Project (https://commixproject.com).
Copyright (c) 2014-2025 Anastasios Stasinopoulos (@ancst).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

For more see the file 'readme/COPYING' for copying permission.
"""

import sys

# Dummy check for missing module(s).
try:
  __import__("src.utils.version")
  from src.utils import version
  version.python_version()

except ImportError as ex:
  err_msg = "Wrong installation detected (i.e \"" + str(ex) + "\"). "
  err_msg += "Visit 'https://github.com/commixproject/commix/' for further details."
  sys.exit(err_msg)

# Main
def main():
  import src.core.main

# Main
if __name__ == '__main__':
  try:
    main()
  except SystemExit:
    import sys
    raise SystemExit()
  except KeyboardInterrupt:
    import sys
    raise SystemExit()
  except IndentationError as err_msg:
    from src.utils import settings
    settings.print_data_to_stdout(settings.print_critical_msg(err_msg))
    raise SystemExit()
  except:
    from src.utils import common
    common.unhandled_exception()

# eof